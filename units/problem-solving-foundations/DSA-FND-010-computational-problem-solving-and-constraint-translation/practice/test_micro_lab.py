from __future__ import annotations

import pytest
from micro_lab import (
    Scenario,
    default_scenarios,
    dominant_operation_count,
    render_trace,
    trace_scenario,
)


def test_operation_shapes_keep_independent_variables() -> None:
    assert dominant_operation_count("single_scan", n=7) == 7
    assert dominant_operation_count("all_unordered_pairs", n=6) == 15
    assert dominant_operation_count("scan_per_query", n=7, q=5) == 35
    assert dominant_operation_count("build_once_then_one_per_query", n=7, q=5) == 12
    assert dominant_operation_count("output_lower_bound", n=7, output_items=30) == 30


def test_zero_items_produce_zero_pairs() -> None:
    assert dominant_operation_count("all_unordered_pairs", n=0) == 0


def test_work_equal_to_budget_is_retained() -> None:
    row = trace_scenario(Scenario("boundary", "single_scan", 8, 1, 1, 8))
    assert row.within_budget is True


def test_invalid_sizes_and_shapes_are_rejected() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        dominant_operation_count("single_scan", n=-1)
    with pytest.raises(ValueError, match="unknown work shape"):
        dominant_operation_count("mystery", n=1)


def test_default_trace_is_deterministic_and_explanatory() -> None:
    rows = tuple(trace_scenario(scenario) for scenario in default_scenarios())
    rendered = render_trace(rows)
    assert len(rows) == 7
    assert "empty pair boundary" in rendered
    assert "n(n-1)/2" in rendered
    assert "KEEP" in rendered
    assert "REJECT" in rendered
