"""Check exact inequalities without assuming any platform-specific log rounding."""

import pytest
from integer_boundaries import boundary_rows, exact_bounds


def test_bounds_satisfy_defining_integer_inequalities() -> None:
    values = [*range(1, 513), 2**100 - 1, 2**100, 2**100 + 1, 2**4096 + 1]
    for n in values:
        lower, upper = exact_bounds(n)
        assert 2**lower <= n < 2 ** (lower + 1)
        assert n <= 2**upper
        if upper > 0:
            assert 2 ** (upper - 1) < n


def test_observation_rows_keep_exact_columns_separate() -> None:
    rows = boundary_rows(53)
    assert [row[0] for row in rows] == ["2^53-1", "2^53+0", "2^53+1"]
    assert [(row[3], row[5]) for row in rows] == [(52, 53), (53, 53), (53, 54)]


@pytest.mark.parametrize("n", [0, -1])
def test_nonpositive_input_is_outside_log_domain(n: int) -> None:
    with pytest.raises(ValueError):
        exact_bounds(n)


@pytest.mark.parametrize("exponent", [0, 4097])
def test_observation_workload_has_a_bound(exponent: int) -> None:
    with pytest.raises(ValueError):
        boundary_rows(exponent)
