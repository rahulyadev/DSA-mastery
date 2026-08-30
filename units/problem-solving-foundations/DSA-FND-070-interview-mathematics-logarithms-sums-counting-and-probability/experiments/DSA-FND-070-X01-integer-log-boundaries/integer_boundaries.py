"""Observe floating logarithms next to exact integer power boundaries."""

import argparse
import platform
import sys
from math import ceil, floor, log2


def exact_bounds(n: int) -> tuple[int, int]:
    """Return floor(log2(n)), ceil(log2(n)) for a positive integer, without floats."""
    if n < 1:
        raise ValueError("n must be positive")
    return n.bit_length() - 1, (n - 1).bit_length()


def boundary_rows(exponent: int) -> list[tuple[str, float, int, int, int, int]]:
    """Return labels, observed logs, and float/exact floor and ceiling pairs."""
    if not 1 <= exponent <= 4096:
        raise ValueError("choose an exponent from 1 through 4096 for this lab")
    rows = []
    for offset in (-1, 0, 1):
        n = 2**exponent + offset
        exact_floor, exact_ceil = exact_bounds(n)
        approximate = log2(n)
        label = f"2^{exponent}{offset:+d}"
        rows.append(
            (label, approximate, floor(approximate), exact_floor, ceil(approximate), exact_ceil)
        )
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--exponents", type=int, nargs="+", default=[3, 53, 100])
    args = parser.parse_args()
    if any(not 1 <= exponent <= 4096 for exponent in args.exponents):
        parser.error("exponents must be from 1 through 4096")
    print(f"Python: {platform.python_implementation()} {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.machine()}")
    print(f"float radix={sys.float_info.radix} mant_dig={sys.float_info.mant_dig}")
    print("n log2(n) floor_float floor_exact ceil_float ceil_exact mismatch")
    for exponent in args.exponents:
        for (
            label,
            approximate,
            observed_floor,
            exact_floor,
            observed_ceil,
            exact_ceil,
        ) in boundary_rows(exponent):
            mismatch = (observed_floor, observed_ceil) != (exact_floor, exact_ceil)
            print(
                label,
                f"{approximate:.12g}",
                observed_floor,
                exact_floor,
                observed_ceil,
                exact_ceil,
                mismatch,
            )
    print("A displayed logarithm is rounded; exact inequalities decide integer boundaries.")


if __name__ == "__main__":
    main()
