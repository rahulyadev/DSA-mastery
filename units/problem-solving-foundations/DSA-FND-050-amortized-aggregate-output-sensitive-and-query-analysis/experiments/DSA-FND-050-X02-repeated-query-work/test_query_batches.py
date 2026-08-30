"""Validate query boundaries, snapshot preservation, and counted work."""

from __future__ import annotations

from itertools import product

import pytest
from query_batches import compare_batch


@pytest.mark.parametrize("length", range(5))
def test_all_small_signed_inputs_and_valid_ranges(length: int) -> None:
    queries = [(left, right) for left in range(length + 1) for right in range(left, length + 1)]
    for values in product((-2, 0, 3), repeat=length):
        before_queries = queries.copy()
        result = compare_batch(values, queries)
        # A tiny slicing oracle is intentionally independent of prefix indexing.
        expected = tuple(sum(values[left:right]) for left, right in queries)
        assert result.direct_answers == expected
        assert result.indexed_answers == expected
        assert result.direct_additions == sum(right - left for left, right in queries)
        assert result.build_additions == length
        assert result.query_subtractions == len(queries)
        assert result.table_entries == length + 1
        assert queries == before_queries


def test_eager_build_cost_is_visible_without_requests() -> None:
    result = compare_batch([5, -2, 4, 1], [])
    assert result.direct_answers == result.indexed_answers == ()
    assert result.direct_additions == result.query_subtractions == 0
    assert result.indexed_arithmetic == 4


def test_mutable_inputs_and_repeated_requests_are_preserved() -> None:
    values = [5, -2, 4, 1]
    queries = [(1, 4), (1, 4), (4, 4)]
    result = compare_batch(values, queries)
    assert result.direct_answers == result.indexed_answers == (3, 3, 0)
    assert values == [5, -2, 4, 1]
    assert queries == [(1, 4), (1, 4), (4, 4)]


@pytest.mark.parametrize("query", [(-1, 2), (2, 1), (0, 5), (5, 5)])
def test_invalid_boundaries_are_rejected_instead_of_using_python_negative_indices(
    query: tuple[int, int],
) -> None:
    with pytest.raises(ValueError, match="each query must satisfy"):
        compare_batch([5, -2, 4, 1], [query])
