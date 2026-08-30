"""Passing checks for the worked lab only; no learner answers are tested here."""

from __future__ import annotations

import pytest
from micro_lab import (
    CountRow,
    DoublingRow,
    doubling_trace,
    rectangle_trace,
    render_counts,
    render_doubling,
    triangle_trace,
)


def test_rectangle_preserves_both_dimensions() -> None:
    assert rectangle_trace(2, 3) == [CountRow(0, 3, 3), CountRow(1, 3, 6)]
    assert rectangle_trace(3, 2) == [CountRow(0, 2, 2), CountRow(1, 2, 4), CountRow(2, 2, 6)]


def test_empty_inner_loop_still_has_outer_iterations() -> None:
    assert rectangle_trace(3, 0) == [CountRow(0, 0, 0), CountRow(1, 0, 0), CountRow(2, 0, 0)]
    assert rectangle_trace(0, 3) == []
    assert rectangle_trace(0, 0) == []


def test_triangle_counts_only_the_strict_lower_half() -> None:
    assert triangle_trace(4) == [
        CountRow(0, 0, 0),
        CountRow(1, 1, 1),
        CountRow(2, 2, 3),
        CountRow(3, 3, 6),
    ]
    assert triangle_trace(1) == [CountRow(0, 0, 0)]
    assert triangle_trace(0) == []


def test_doubling_retains_the_state_that_crosses_the_limit() -> None:
    assert doubling_trace(10) == [
        DoublingRow(0, 1, 2),
        DoublingRow(1, 2, 4),
        DoublingRow(2, 4, 8),
        DoublingRow(3, 8, 16),
    ]


@pytest.mark.parametrize(("limit", "visits"), [(0, 0), (1, 0), (2, 1), (8, 3), (9, 4)])
def test_doubling_boundaries(limit: int, visits: int) -> None:
    rows = doubling_trace(limit)
    assert len(rows) == visits
    final = rows[-1].after if rows else 1
    assert final >= limit
    assert all(row.before < limit and row.after == 2 * row.before for row in rows)


def test_negative_dimensions_are_not_silently_treated_as_empty() -> None:
    with pytest.raises(ValueError, match="n must be non-negative"):
        rectangle_trace(-1, 3)
    with pytest.raises(ValueError, match="m must be non-negative"):
        rectangle_trace(3, -1)
    with pytest.raises(ValueError, match="n must be non-negative"):
        triangle_trace(-1)
    with pytest.raises(ValueError, match="limit must be non-negative"):
        doubling_trace(-1)


def test_display_distinguishes_no_body_work_from_no_outer_work() -> None:
    assert "outer_iterations=3; body_visits=0" in render_counts(
        "empty inner", rectangle_trace(3, 0)
    )
    assert "outer_iterations=0; body_visits=0" in render_counts(
        "empty outer", rectangle_trace(0, 3)
    )
    assert "body_visits=0; final_position=1; guard=false" in render_doubling(0, [])
