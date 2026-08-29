"""Deterministic operation-budget trace for DSA-FND-010.

This lab counts abstract dominant operations. It deliberately does not time code:
machine timing cannot establish a universal algorithmic feasibility threshold.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Scenario:
    """One translated candidate and its abstract resource budget."""

    label: str
    shape: str
    n: int
    q: int
    output_items: int
    budget: int


@dataclass(frozen=True)
class TraceRow:
    """The observable reasoning state for one scenario."""

    label: str
    formula: str
    work: int
    budget: int
    within_budget: bool


FORMULAS = {
    "single_scan": "n",
    "all_unordered_pairs": "n(n-1)/2",
    "scan_per_query": "nq",
    "build_once_then_one_per_query": "n+q",
    "output_lower_bound": "r",
}


def dominant_operation_count(
    shape: str,
    *,
    n: int,
    q: int = 1,
    output_items: int = 1,
) -> int:
    """Return the exact abstract count for a named work shape."""

    if min(n, q, output_items) < 0:
        raise ValueError("n, q, and output_items must be non-negative")

    if shape == "single_scan":
        return n
    if shape == "all_unordered_pairs":
        return n * (n - 1) // 2
    if shape == "scan_per_query":
        return n * q
    if shape == "build_once_then_one_per_query":
        return n + q
    if shape == "output_lower_bound":
        return output_items
    raise ValueError(f"unknown work shape: {shape}")


def trace_scenario(scenario: Scenario) -> TraceRow:
    """Translate one scenario into count, budget, and decision state."""

    if scenario.budget < 0:
        raise ValueError("budget must be non-negative")

    work = dominant_operation_count(
        scenario.shape,
        n=scenario.n,
        q=scenario.q,
        output_items=scenario.output_items,
    )
    return TraceRow(
        label=scenario.label,
        formula=FORMULAS[scenario.shape],
        work=work,
        budget=scenario.budget,
        within_budget=work <= scenario.budget,
    )


def default_scenarios() -> tuple[Scenario, ...]:
    """Return fixed cases chosen to expose independent constraint pressures."""

    return (
        Scenario("empty pair boundary", "all_unordered_pairs", 0, 1, 1, 0),
        Scenario("small single scan", "single_scan", 12, 1, 1, 100),
        Scenario("pair boundary rejection", "all_unordered_pairs", 6, 1, 1, 14),
        Scenario("large pair family", "all_unordered_pairs", 200_000, 1, 1, 3_000_000),
        Scenario("many full scans", "scan_per_query", 200_000, 100_000, 100_000, 3_000_000),
        Scenario(
            "build once and answer",
            "build_once_then_one_per_query",
            200_000,
            100_000,
            100_000,
            3_000_000,
        ),
        Scenario("output pressure", "output_lower_bound", 10, 1, 5_000_000, 3_000_000),
    )


def render_trace(rows: tuple[TraceRow, ...]) -> str:
    """Render a compact table suitable for prediction-versus-observation."""

    header = f"{'scenario':28} {'formula':12} {'work':>15} {'budget':>12} decision"
    divider = "-" * len(header)
    lines = [header, divider]
    for row in rows:
        decision = "KEEP" if row.within_budget else "REJECT"
        lines.append(
            f"{row.label:28} {row.formula:12} {row.work:15,d} "
            f"{row.budget:12,d} {decision}"
        )
    return "\n".join(lines)


def main() -> None:
    rows = tuple(trace_scenario(scenario) for scenario in default_scenarios())
    print(render_trace(rows))
    print("\nCounts are abstract operations, not measured seconds.")


if __name__ == "__main__":
    main()
