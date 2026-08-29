from __future__ import annotations

import pytest
from trace_lab import (
    audit_transition,
    default_cases,
    loop_head_invariant,
    render_report,
    trace_first_index_at_least,
)


def test_matching_trace_preserves_invariant_and_decreases_variant() -> None:
    report = trace_first_index_at_least([2, 5, 1, 7], threshold=6)

    assert report.result == 3
    assert [row.index for row in report.rows] == [0, 1, 2, 3]
    assert [row.variant for row in report.rows] == [4, 3, 2, 1]
    assert all(row.invariant_holds for row in report.rows)
    assert [row.guard_holds for row in report.rows] == [True, True, True, False]
    assert report.rows[-1].processed_prefix == (2, 5, 1)
    assert report.exit_reason == "current candidate satisfies the predicate"


def test_first_position_match_has_no_body_transition() -> None:
    report = trace_first_index_at_least([6], threshold=6)

    assert report.result == 0
    assert len(report.rows) == 1
    assert report.rows[0].processed_prefix == ()
    assert report.rows[0].guard_holds is False
    assert report.rows[0].variant == 1


def test_no_match_reaches_exhausted_head_safely() -> None:
    report = trace_first_index_at_least([1], threshold=6)

    assert report.result is None
    assert [row.index for row in report.rows] == [0, 1]
    assert [row.current for row in report.rows] == [1, None]
    assert [row.variant for row in report.rows] == [1, 0]
    assert report.rows[-1].processed_prefix == (1,)
    assert report.exit_reason == "input exhausted after every candidate failed"


def test_empty_input_exits_without_current_item() -> None:
    report = trace_first_index_at_least([], threshold=6)

    assert report.result is None
    assert len(report.rows) == 1
    assert report.rows[0].index == 0
    assert report.rows[0].current is None
    assert report.rows[0].variant == 0
    assert report.rows[0].invariant_holds is True


def test_trace_does_not_mutate_input() -> None:
    values = [2, 5, 1, 7]
    original = values.copy()

    trace_first_index_at_least(values, threshold=6)

    assert values == original


def test_transition_audit_separates_preservation_from_progress() -> None:
    correct = audit_transition([1, 7], 6, index=0, next_index=1)
    skipped = audit_transition([1, 7], 6, index=0, next_index=2)
    stutter = audit_transition([1], 6, index=0, next_index=0)

    assert correct.preserves_invariant is True
    assert correct.makes_strict_progress is True
    assert skipped.preserves_invariant is False
    assert skipped.makes_strict_progress is True
    assert stutter.preserves_invariant is True
    assert stutter.makes_strict_progress is False


def test_transition_audit_rejects_illegal_boundaries() -> None:
    with pytest.raises(ValueError, match="current input position"):
        audit_transition([], 6, index=0, next_index=0)
    with pytest.raises(ValueError, match="loop boundary"):
        audit_transition([1], 6, index=0, next_index=2)


def test_invariant_exposes_skipped_valid_candidate() -> None:
    values = (1, 7)

    assert loop_head_invariant(values, threshold=6, index=1) is True
    assert loop_head_invariant(values, threshold=6, index=2) is False


def test_render_and_default_cases_are_deterministic() -> None:
    assert default_cases() == (
        ([2, 5, 1, 7], 6),
        ([6], 6),
        ([1], 6),
        ([], 6),
    )
    rendered = render_report(trace_first_index_at_least([1], threshold=6))
    assert "processed" in rendered
    assert "guard" in rendered
    assert "V" in rendered
    assert "result=None" in rendered
