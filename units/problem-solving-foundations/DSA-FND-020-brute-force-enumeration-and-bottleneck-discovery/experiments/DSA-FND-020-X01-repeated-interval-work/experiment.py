"""Instrument repeated work across two exhaustive interval evaluators.

Both evaluators visit the same non-empty interval boundaries. They differ only
in whether an interval total is rebuilt from zero or extended from retained
state. Counts are deterministic abstract additions, not elapsed-time claims.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WorkReport:
    """Comparable work and result state for one input size."""

    n: int
    intervals: int
    rebuilt_additions: int
    extended_additions: int
    checksum: int

    @property
    def addition_ratio(self) -> float:
        if self.extended_additions == 0:
            return 1.0
        return self.rebuilt_additions / self.extended_additions


def checksum_with_rebuilt_totals(values: list[int]) -> tuple[int, int, int]:
    """Return checksum, interval count, and additions after rebuilding totals."""

    checksum = 0
    intervals = 0
    additions = 0
    for left in range(len(values)):
        for right in range(left, len(values)):
            interval_total = 0
            for index in range(left, right + 1):
                interval_total += values[index]
                additions += 1
            checksum += interval_total
            intervals += 1
    return checksum, intervals, additions


def checksum_with_extended_totals(values: list[int]) -> tuple[int, int, int]:
    """Return the same checksum while extending one total per left boundary."""

    checksum = 0
    intervals = 0
    additions = 0
    for left in range(len(values)):
        interval_total = 0
        for right in range(left, len(values)):
            interval_total += values[right]
            additions += 1
            checksum += interval_total
            intervals += 1
    return checksum, intervals, additions


def run_case(n: int) -> WorkReport:
    """Run one deterministic case and assert comparable result state."""

    if n < 0:
        raise ValueError("n must be non-negative")
    values = list(range(1, n + 1))
    rebuilt_checksum, rebuilt_intervals, rebuilt_additions = (
        checksum_with_rebuilt_totals(values)
    )
    extended_checksum, extended_intervals, extended_additions = (
        checksum_with_extended_totals(values)
    )
    if rebuilt_checksum != extended_checksum:
        raise AssertionError("the evaluators produced different checksums")
    if rebuilt_intervals != extended_intervals:
        raise AssertionError("the evaluators visited different interval counts")
    return WorkReport(
        n=n,
        intervals=rebuilt_intervals,
        rebuilt_additions=rebuilt_additions,
        extended_additions=extended_additions,
        checksum=rebuilt_checksum,
    )


def render_reports(reports: tuple[WorkReport, ...]) -> str:
    """Render deterministic counts for prediction-versus-observation."""

    header = (
        f"{'n':>3} {'intervals':>10} {'rebuilt_adds':>14} "
        f"{'extended_adds':>14} {'ratio':>8} {'checksum':>12}"
    )
    divider = "-" * len(header)
    lines = [header, divider]
    for report in reports:
        lines.append(
            f"{report.n:3d} {report.intervals:10d} "
            f"{report.rebuilt_additions:14d} "
            f"{report.extended_additions:14d} "
            f"{report.addition_ratio:8.2f} {report.checksum:12d}"
        )
    return "\n".join(lines)


def main() -> None:
    reports = tuple(run_case(n) for n in (4, 8, 16, 32, 64))
    print(render_reports(reports))
    print("\nCounts are abstract additions; no wall-clock threshold is inferred.")


if __name__ == "__main__":
    main()
