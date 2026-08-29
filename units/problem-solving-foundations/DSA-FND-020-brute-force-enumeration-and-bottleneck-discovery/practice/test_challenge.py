from __future__ import annotations

from starter import enumerate_target_triples


def test_one_match_still_checks_every_legal_triple() -> None:
    values = [1, 2, 3, 4]
    original = values.copy()
    matches, checks = enumerate_target_triples(values, target=6)
    assert matches == [(0, 1, 2)]
    assert checks == 4
    assert values == original


def test_equal_values_remain_distinct_positional_candidates() -> None:
    matches, checks = enumerate_target_triples([0, 0, 0, 0], target=0)
    assert matches == [
        (0, 1, 2),
        (0, 1, 3),
        (0, 2, 3),
        (1, 2, 3),
    ]
    assert checks == 4


def test_too_few_positions_have_no_triples() -> None:
    assert enumerate_target_triples([], target=0) == ([], 0)
    assert enumerate_target_triples([5], target=5) == ([], 0)
    assert enumerate_target_triples([5, -5], target=0) == ([], 0)


def test_no_match_reports_all_candidate_checks() -> None:
    matches, checks = enumerate_target_triples([1, 2, 4, 8, 16], target=100)
    assert matches == []
    assert checks == 10
