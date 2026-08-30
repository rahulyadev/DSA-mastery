"""Deterministic model checks; never assert that a random estimate must be close."""

from fractions import Fraction
from math import comb, perm

import pytest
from collision_observations import collision_pairs, exact_summary, sampled_summary


@pytest.mark.parametrize(
    "labels, expected", [([], 0), ([0], 0), ([0, 1, 2], 0), ([0, 0, 0], 3), ([0, 1, 0, 1], 2)]
)
def test_pair_count_is_not_a_yes_or_no_event(labels: list[int], expected: int) -> None:
    assert collision_pairs(labels) == expected


@pytest.mark.parametrize("items, buckets", [(0, 1), (1, 4), (2, 3), (3, 4), (4, 2)])
def test_enumeration_matches_separate_counting_arguments(items: int, buckets: int) -> None:
    summary = exact_summary(items, buckets)
    assert summary.trials == buckets**items
    assert summary.mean_pairs == Fraction(comb(items, 2), buckets)
    distinct_assignments = perm(buckets, items)
    assert summary.probability_any == 1 - Fraction(distinct_assignments, buckets**items)


def test_seed_reproduction_and_degenerate_models() -> None:
    assert sampled_summary(3, 4, 50, 7) == sampled_summary(3, 4, 50, 7)
    always = sampled_summary(3, 1, 10, 7)
    assert (always.mean_pairs, always.probability_any) == (Fraction(3), Fraction(1))
    empty = sampled_summary(0, 4, 10, 7)
    assert (empty.mean_pairs, empty.probability_any) == (Fraction(0), Fraction(0))


def test_invalid_domains_and_exhaustive_budget_are_rejected() -> None:
    for items, buckets in [(-1, 4), (3, 0), (9, 2), (8, 100)]:
        with pytest.raises(ValueError):
            exact_summary(items, buckets)
    for items, buckets, trials in [(3, 4, 0), (3, 4, 100001), (-1, 4, 10), (3, 0, 10)]:
        with pytest.raises(ValueError):
            sampled_summary(items, buckets, trials, 7)
