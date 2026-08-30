"""Observe shallow Python-list size changes without inferring copy counts.

The workload appends one shared None reference at a time. No timing, process
memory, internal address, or backing-array capacity is measured. Python 3.11+.
"""

from __future__ import annotations

import argparse
import platform
import sys
from collections.abc import Iterator
from datetime import UTC, datetime


def size_events(appends: int) -> Iterator[tuple[int, int, int]]:
    """Yield (length, shallow bytes, byte change), including the empty list."""
    if appends < 0:
        raise ValueError("appends must be non-negative")
    values: list[None] = []
    previous = sys.getsizeof(values)
    yield 0, previous, 0
    for length in range(1, appends + 1):
        values.append(None)
        current = sys.getsizeof(values)
        if current != previous:
            yield length, current, current - previous
        previous = current


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--appends", type=int, default=40)
    args = parser.parse_args()
    if not 0 <= args.appends <= 10_000:
        parser.error("appends must be 0..10000 for this small observation")
    if platform.python_implementation() != "CPython":
        parser.error("this recorded implementation observation requires CPython")

    print(f"date_utc={datetime.now(UTC).date()}")
    print(f"python={platform.python_implementation()} {platform.python_version()}")
    print(f"os={platform.system()}; architecture={platform.machine()}")
    print(f"appends={args.appends}; item=shared None; dependencies=stdlib")
    print("length shallow_bytes change_bytes")
    for event in size_events(args.appends):
        print(*event)
    print("Unprinted lengths had unchanged shallow size.")
    print("Size changes do not establish a physical move, copy count, or latency.")


if __name__ == "__main__":
    main()
