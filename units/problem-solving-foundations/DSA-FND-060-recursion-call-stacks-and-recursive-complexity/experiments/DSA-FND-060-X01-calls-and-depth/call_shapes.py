"""Count logical calls and simultaneous depth for four bounded recursion shapes."""

from __future__ import annotations

import platform
import sys
from dataclasses import dataclass
from typing import Literal

Shape = Literal["chain", "halve", "split", "repeat"]
LIMITS: dict[Shape, int] = {"chain": 128, "halve": 1_000_000, "split": 4096, "repeat": 12}


@dataclass(frozen=True)
class Counts:
    calls: int
    leaves: int
    max_active: int


def count_shape(size: int, shape: Shape) -> Counts:
    """Run the selected shape without saving a call tree or changing recursion limits."""
    if shape not in LIMITS:
        raise ValueError("unknown recursion shape")
    if not 0 <= size <= LIMITS[shape]:
        raise ValueError(f"{shape} size must be between 0 and {LIMITS[shape]}")

    calls = 0
    leaves = 0
    max_active = 0

    def visit(remaining: int, depth: int) -> None:
        nonlocal calls, leaves, max_active
        calls += 1
        max_active = max(max_active, depth)
        base = remaining == 0 if shape in ("chain", "repeat") else remaining <= 1
        if base:
            leaves += 1
            return
        if shape == "chain":
            visit(remaining - 1, depth + 1)
        elif shape == "halve":
            visit(remaining // 2, depth + 1)
        elif shape == "split":
            left_size = remaining // 2
            visit(left_size, depth + 1)
            visit(remaining - left_size, depth + 1)
        else:
            visit(remaining - 1, depth + 1)
            visit(remaining - 1, depth + 1)

    visit(size, 1)
    return Counts(calls, leaves, max_active)


def main() -> None:
    print(f"Python: {platform.python_implementation()} {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.machine()}")
    print(f"Recursion limit (read only): {sys.getrecursionlimit()}")
    print("shape       n     calls    leaves  max_active")
    cases: tuple[tuple[Shape, tuple[int, ...]], ...] = (
        ("chain", (0, 1, 4, 8, 16, 64)),
        ("halve", (0, 1, 4, 8, 16, 64)),
        ("split", (0, 1, 4, 8, 16, 64)),
        ("repeat", (0, 1, 4, 8, 12)),
    )
    for shape, sizes in cases:
        for size in sizes:
            counts = count_shape(size, shape)
            print(f"{shape:7} {size:5} {counts.calls:9} {counts.leaves:9} {counts.max_active:11}")


if __name__ == "__main__":
    main()
