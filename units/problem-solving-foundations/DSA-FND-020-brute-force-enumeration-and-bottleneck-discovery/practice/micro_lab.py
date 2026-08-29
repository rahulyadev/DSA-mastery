"""Deterministic candidate-space trace for DSA-FND-020.

Predict the default trace before running this file. The lab materializes trace
rows only so the small teaching state is visible; candidate generation itself
is lazy and can be inspected independently.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(frozen=True)
class CandidateCounts:
    """Counts for three pair interpretations over the same n positions."""

    ordered_with_self: int
    ordered_distinct: int
    unordered_distinct: int


@dataclass(frozen=True)
class PairCheck:
    """Observable state after evaluating one legal unordered index pair."""

    step: int
    left: int
    right: int
    total: int
    is_match: bool


def candidate_counts(n: int) -> CandidateCounts:
    """Return exact candidate counts for common pair legality rules."""

    if n < 0:
        raise ValueError("n must be non-negative")
    return CandidateCounts(
        ordered_with_self=n * n,
        ordered_distinct=n * (n - 1),
        unordered_distinct=n * (n - 1) // 2,
    )


def unordered_index_pairs(n: int) -> Iterator[tuple[int, int]]:
    """Yield every pair 0 <= left < right < n in lexicographic order."""

    if n < 0:
        raise ValueError("n must be non-negative")
    for left in range(n):
        for right in range(left + 1, n):
            yield left, right


def trace_all_pair_sums(values: list[int], target: int) -> tuple[PairCheck, ...]:
    """Trace all legal candidates for an all-matching-pairs contract."""

    rows: list[PairCheck] = []
    for step, (left, right) in enumerate(
        unordered_index_pairs(len(values)), start=1
    ):
        total = values[left] + values[right]
        rows.append(
            PairCheck(
                step=step,
                left=left,
                right=right,
                total=total,
                is_match=total == target,
            )
        )
    return tuple(rows)


def matching_pairs(rows: tuple[PairCheck, ...]) -> tuple[tuple[int, int], ...]:
    """Project matching index pairs from an already-produced trace."""

    return tuple((row.left, row.right) for row in rows if row.is_match)


def render_trace(
    values: list[int], target: int, rows: tuple[PairCheck, ...]
) -> str:
    """Render candidate state without making an elapsed-time claim."""

    header = "step  pair    values   total  match"
    divider = "-" * len(header)
    lines = [
        f"values={values} target={target}",
        header,
        divider,
    ]
    for row in rows:
        pair = f"({row.left},{row.right})"
        pair_values = f"({values[row.left]},{values[row.right]})"
        lines.append(
            f"{row.step:>4}  {pair:<6}  {pair_values:<8} "
            f"{row.total:>5}  {'yes' if row.is_match else 'no'}"
        )
    return "\n".join(lines)


def main() -> None:
    values = [4, 1, 7, 4]
    target = 8
    counts = candidate_counts(len(values))
    rows = trace_all_pair_sums(values, target)

    print("candidate counts")
    print(f"  ordered with self : {counts.ordered_with_self}")
    print(f"  ordered distinct  : {counts.ordered_distinct}")
    print(f"  unordered distinct: {counts.unordered_distinct}")
    print()
    print(render_trace(values, target, rows))
    print(f"matches={matching_pairs(rows)}")
    print(f"checks={len(rows)}")


if __name__ == "__main__":
    main()
