from __future__ import annotations

import pytest
from micro_lab import (
    CandidateCounts,
    candidate_counts,
    matching_pairs,
    trace_all_pair_sums,
    unordered_index_pairs,
)


def test_candidate_counts_expose_wasted_ordered_states() -> None:
    assert candidate_counts(4) == CandidateCounts(
        ordered_with_self=16,
        ordered_distinct=12,
        unordered_distinct=6,
    )


def test_unordered_pairs_cover_small_space_once_in_order() -> None:
    assert list(unordered_index_pairs(0)) == []
    assert list(unordered_index_pairs(1)) == []
    assert list(unordered_index_pairs(4)) == [
        (0, 1),
        (0, 2),
        (0, 3),
        (1, 2),
        (1, 3),
        (2, 3),
    ]


def test_trace_preserves_equal_values_at_distinct_positions() -> None:
    rows = trace_all_pair_sums([4, 1, 7, 4], target=8)
    assert len(rows) == 6
    assert matching_pairs(rows) == ((0, 3), (1, 2))
    assert rows[2].total == 8
    assert rows[2].is_match is True


def test_too_few_positions_have_no_candidates() -> None:
    assert candidate_counts(0).unordered_distinct == 0
    assert candidate_counts(1).unordered_distinct == 0
    assert trace_all_pair_sums([4], target=8) == ()


def test_negative_size_is_rejected() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        candidate_counts(-1)
    with pytest.raises(ValueError, match="non-negative"):
        list(unordered_index_pairs(-1))
