"""Verify teaching invariants and small independent counts, not learner answers."""

from fractions import Fraction

import pytest
from micro_lab import halving_trace, pair_trace, series_trace, two_coin_outcomes


@pytest.mark.parametrize("n", [1, 2, 3, 7, 8, 9, 13, 63, 64, 65])
def test_halving_states_and_stopping_boundary(n: int) -> None:
    rows = halving_trace(n)
    assert rows[0] == (0, n)
    assert rows[-1][1] == 1
    divisions = rows[-1][0]
    assert 2**divisions <= n < 2 ** (divisions + 1)
    assert len(rows) == divisions + 1
    for step, remaining in rows:
        assert remaining == n // 2**step


@pytest.mark.parametrize("n", [0, 1, 2, 4, 9])
def test_pair_summaries_match_explicit_candidates(n: int) -> None:
    rows = pair_trace(n)
    assert len(rows) == n
    for i, row_size, cumulative in rows:
        assert row_size == len([(a, b) for a in range(n) for b in range(a + 1, n) if a == i])
        assert cumulative == sum(1 for a in range(i + 1) for b in range(a + 1, n))


def test_series_have_distinct_growth_and_exact_fractions() -> None:
    assert series_trace(0) == []
    assert series_trace(4) == [
        (1, 1, 1, Fraction(1)),
        (2, 2, 3, Fraction(3, 2)),
        (3, 4, 7, Fraction(11, 6)),
        (4, 8, 15, Fraction(25, 12)),
    ]


def test_outcomes_distinguish_expected_count_from_event_probability() -> None:
    rows = two_coin_outcomes()
    assert {row[0] for row in rows} == {"HH", "HT", "TH", "TT"}
    assert len(rows) == 4
    assert sum(row[1] for row in rows) == 4
    assert sum(row[2] for row in rows) == 3
    assert next(row for row in rows if row[0] == "HH") == ("HH", 2, 1)


def test_invalid_trace_domains_are_rejected() -> None:
    with pytest.raises(ValueError):
        halving_trace(0)
    with pytest.raises(ValueError):
        halving_trace(-1)
    with pytest.raises(ValueError):
        pair_trace(-1)
    with pytest.raises(ValueError):
        series_trace(-1)
