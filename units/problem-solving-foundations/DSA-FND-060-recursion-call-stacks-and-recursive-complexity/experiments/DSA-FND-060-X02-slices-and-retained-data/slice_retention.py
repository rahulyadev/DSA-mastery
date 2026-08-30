"""Compare actual tail slices with shared-input bounds in bounded recursive sums.

Copied-reference counters describe list payload slots, not deep copies of integers.
tracemalloc is supplementary; its peak is not total process or C-stack memory.
"""

from __future__ import annotations

import gc
import platform
import sys
import tracemalloc
from dataclasses import dataclass
from typing import Literal

Strategy = Literal["bounds", "slices"]
MAX_SIZE = 128


@dataclass
class Work:
    total: int = 0
    calls: int = 0
    max_active: int = 0
    copied_refs: int = 0
    peak_copied_refs: int = 0


def walk(values: list[int], strategy: Strategy) -> Work:
    """Execute one teaching sum, excluding the supplied input from copy counts."""
    if len(values) > MAX_SIZE:
        raise ValueError("experiment accepts at most 128 values")
    if strategy not in ("bounds", "slices"):
        raise ValueError("unknown traversal strategy")
    work = Work()
    live_copied_refs = 0

    def by_index(index: int, depth: int) -> int:
        work.calls += 1
        work.max_active = max(work.max_active, depth)
        if index == len(values):
            return 0
        child_total = by_index(index + 1, depth + 1)
        return values[index] + child_total

    def by_slice(part: list[int], depth: int) -> int:
        nonlocal live_copied_refs
        work.calls += 1
        work.max_active = max(work.max_active, depth)
        if not part:
            return 0
        tail = part[1:]
        work.copied_refs += len(tail)
        live_copied_refs += len(tail)
        work.peak_copied_refs = max(work.peak_copied_refs, live_copied_refs)
        child_total = by_slice(tail, depth + 1)
        live_copied_refs -= len(tail)
        return part[0] + child_total

    work.total = by_index(0, 1) if strategy == "bounds" else by_slice(values, 1)
    return work


def allocation_sample(size: int, strategy: Strategy) -> tuple[Work, int]:
    """Measure one fresh traced-allocation peak; do not disturb an existing tracer."""
    if not 0 <= size <= MAX_SIZE:
        raise ValueError("sample size must be between 0 and 128")
    if tracemalloc.is_tracing():
        raise RuntimeError("run this sample without an existing tracemalloc session")
    values = [1] * size  # Construct input before tracing.
    gc.collect()
    tracemalloc.start()
    try:
        work = walk(values, strategy)
        _, peak = tracemalloc.get_traced_memory()
    finally:
        tracemalloc.stop()
    return work, peak


def main() -> None:
    print(f"Python: {platform.python_implementation()} {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.machine()}")
    print(f"Recursion limit (read only): {sys.getrecursionlimit()}")
    print("Input: n existing references to integer 1; input allocation excluded")
    print("One allocation sample per row; no elapsed-time benchmark")
    print("strategy     n   total  calls  depth  copies  peak_copy_slots  traced_peak_bytes")
    strategies: tuple[Strategy, ...] = ("bounds", "slices")
    for size in (0, 8, 32, 64, 128):
        for strategy in strategies:
            work, peak = allocation_sample(size, strategy)
            print(
                f"{strategy:8} {size:5} {work.total:7} {work.calls:6}"
                f" {work.max_active:6} {work.copied_refs:7}"
                f" {work.peak_copied_refs:16} {peak:18}"
            )


if __name__ == "__main__":
    main()
