"""Trace a logical resize model, not CPython's actual allocator.

One modeled unit is a copied old reference or a newly written reference. The
generator updates counters rather than moving an array. Python 3.11+; stdlib only.
"""

from __future__ import annotations

import argparse
from collections.abc import Iterator
from dataclasses import dataclass
from typing import Literal

GrowthPolicy = Literal["double", "plus_one"]


@dataclass(frozen=True)
class GrowthRow:
    append_number: int
    size_before: int
    capacity_before: int
    capacity_after: int
    copied: int
    actual: int
    total: int
    credit: int


def growth_trace(appends: int, policy: GrowthPolicy = "double") -> Iterator[GrowthRow]:
    """Yield each transition; validation occurs when iteration starts.

    Credit charges three units per append. It is a valid coverage certificate
    for doubling, but it may go negative for plus_one. Both start empty.
    """
    if appends < 0:
        raise ValueError("appends must be non-negative")
    if policy not in ("double", "plus_one"):
        raise ValueError("policy must be double or plus_one")

    capacity = total = 0
    for size in range(appends):
        append_number = size + 1
        capacity_before = capacity
        copied = 0
        if size == capacity:
            copied = size
            capacity = max(1, 2 * capacity) if policy == "double" else capacity + 1
        actual = copied + 1
        total += actual
        yield GrowthRow(
            append_number=append_number,
            size_before=size,
            capacity_before=capacity_before,
            capacity_after=capacity,
            copied=copied,
            actual=actual,
            total=total,
            credit=3 * append_number - total,
        )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--appends", type=int, default=9)
    parser.add_argument("--policy", choices=("double", "plus_one"), default="double")
    args = parser.parse_args()
    if not 0 <= args.appends <= 1000:
        parser.error("appends must be 0..1000 for this small printed trace")

    print(f"policy={args.policy}; count=copy_old_reference + write_new_reference")
    print("append size_before cap_before cap_after copied actual total credit_at_charge_3")
    total = maximum = 0
    for row in growth_trace(args.appends, args.policy):
        print(
            row.append_number,
            row.size_before,
            row.capacity_before,
            row.capacity_after,
            row.copied,
            row.actual,
            row.total,
            row.credit,
        )
        total = row.total
        maximum = max(maximum, row.actual)
    print(f"total={total}; max_single={maximum}")
    if args.appends:
        print(f"actual_mean={total / args.appends:.3f}; a sample mean is not a proof")
    else:
        print("actual_mean=undefined (no operations)")
    print("This script simulates copy counts; it does not allocate the modeled buffers.")


if __name__ == "__main__":
    main()
