"""Check count contracts, never machine-dependent timing ratios."""

from __future__ import annotations

import pytest
from experiment import measure_per_call, rectangle_visits, separate_visits


@pytest.mark.parametrize(
    ("n", "m", "separate", "rectangle"),
    [(0, 0, 0, 0), (0, 8, 8, 0), (8, 0, 8, 0), (2, 3, 5, 6), (3, 2, 5, 6)],
)
def test_counts_keep_input_dimensions_distinct(
    n: int, m: int, separate: int, rectangle: int
) -> None:
    assert separate_visits(n, m) == separate
    assert rectangle_visits(n, m) == rectangle


def test_changing_one_axis_differs_from_changing_both() -> None:
    assert rectangle_visits(16, 8) == 2 * rectangle_visits(8, 8)
    assert rectangle_visits(16, 16) == 4 * rectangle_visits(8, 8)
    assert separate_visits(16, 16) == 2 * separate_visits(8, 8)


@pytest.mark.parametrize(("n", "m"), [(-1, 3), (3, -1)])
def test_negative_sizes_are_rejected(n: int, m: int) -> None:
    with pytest.raises(ValueError, match="non-negative"):
        separate_visits(n, m)
    with pytest.raises(ValueError, match="non-negative"):
        rectangle_visits(n, m)


@pytest.mark.parametrize(("number", "repeat"), [(0, 5), (20, 0), (-1, 5), (20, -1)])
def test_invalid_timing_configuration_is_rejected(number: int, repeat: int) -> None:
    with pytest.raises(ValueError, match="positive"):
        measure_per_call(lambda: 0, number=number, repeat=repeat)
