"""Compare deterministic work counts with optional, machine-specific timings.

No timing threshold is a correctness test. This experiment does not solve any of
the learner contracts in practice/README.md. Python 3.11+; standard library only.
"""

from __future__ import annotations

import argparse
import platform
import timeit
from collections.abc import Callable
from datetime import UTC, datetime
from functools import partial

COUNT_CASES = ((0, 8), (8, 0), (8, 8), (16, 8), (8, 16), (16, 16))
TIMING_CASES = ((128, 128), (256, 128), (128, 256), (256, 256))
WARMUP_CALLS = 3


def require_sizes(n: int, m: int) -> None:
    if n < 0 or m < 0:
        raise ValueError("n and m must be non-negative")


def separate_visits(n: int, m: int) -> int:
    """One counted event per item in each of two separate phases."""
    require_sizes(n, m)
    visits = 0
    for _ in range(n):
        visits += 1
    for _ in range(m):
        visits += 1
    return visits


def rectangle_visits(n: int, m: int) -> int:
    """One counted event per pair; the outer-loop overhead is not counted."""
    require_sizes(n, m)
    visits = 0
    for _ in range(n):
        for _ in range(m):
            visits += 1
    return visits


def measure_per_call(
    operation: Callable[[], int], *, number: int, repeat: int
) -> tuple[float, ...]:
    """Return every repeat in seconds per call; keep all data, not just a ratio."""
    if number <= 0 or repeat <= 0:
        raise ValueError("number and repeat must be positive")
    for _ in range(WARMUP_CALLS):
        operation()
    return tuple(elapsed / number for elapsed in timeit.Timer(operation).repeat(repeat, number))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--timing", action="store_true", help="also print noisy timing observations"
    )
    parser.add_argument("--number", type=int, default=20, help="calls per timing repeat")
    parser.add_argument("--repeat", type=int, default=5, help="timing repeats per specimen")
    args = parser.parse_args()
    if not 1 <= args.number <= 100 or not 1 <= args.repeat <= 20:
        parser.error("number must be 1..100 and repeat must be 1..20 for this small experiment")

    print("Deterministic counts (body visits; guards and allocation excluded)")
    print("n m separate rectangle")
    for n, m in COUNT_CASES:
        print(n, m, separate_visits(n, m), rectangle_visits(n, m))

    if not args.timing:
        return

    print("\nTiming observations; these are not asymptotic proofs")
    print(f"date_utc={datetime.now(UTC).isoformat(timespec='seconds')}")
    print(f"python={platform.python_implementation()} {platform.python_version()}")
    print(f"platform={platform.platform()}")
    print(f"architecture={platform.machine()}; processor={platform.processor() or 'not reported'}")
    print(f"warmup_calls={WARMUP_CALLS}; repeat={args.repeat}; number={args.number}")
    print("timer=perf_counter; cyclic_gc=disabled_during_timeit; dependencies=stdlib")
    print("workload=fixed integer dimensions; no I/O or input allocation in timed calls")
    print("function n m body_visits min_us_per_call all_us_per_call")
    for n, m in TIMING_CASES:
        for name, function in (("separate", separate_visits), ("rectangle", rectangle_visits)):
            operation = partial(function, n, m)
            body_visits = operation()
            samples = measure_per_call(operation, number=args.number, repeat=args.repeat)
            microseconds = tuple(sample * 1_000_000 for sample in samples)
            all_samples = ",".join(f"{value:.3f}" for value in microseconds)
            print(f"{name} {n} {m} {body_visits} {min(microseconds):.3f} [{all_samples}]")


if __name__ == "__main__":
    main()
