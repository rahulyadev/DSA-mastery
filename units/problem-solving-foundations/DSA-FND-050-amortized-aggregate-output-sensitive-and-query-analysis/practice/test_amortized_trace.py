"""Check the teaching counter against independent sums and prefix invariants."""

from __future__ import annotations

import pytest
from micro_lab import growth_trace


@pytest.mark.parametrize("appends", [0, 1, 2, 3, 4, 5, 8, 9, 16, 17, 65])
def test_doubling_matches_geometric_copy_sum(appends: int) -> None:
    rows = list(growth_trace(appends))
    # Old capacities copied are exactly powers of two strictly below appends.
    expected_copies = sum(1 << bit for bit in range(appends.bit_length()) if 1 << bit < appends)
    assert sum(row.copied for row in rows) == expected_copies
    assert sum(row.actual for row in rows) == appends + expected_copies
    assert len(rows) == appends


def test_every_prefix_is_paid_for_including_just_after_growth() -> None:
    rows = list(growth_trace(129))
    assert all(row.total < 3 * row.append_number for row in rows)
    assert all(row.credit >= 0 for row in rows)
    assert all(row.size_before + 1 <= row.capacity_after for row in rows)
    assert rows[8].actual == 9
    assert rows[8].total == 24
    assert rows[8].credit == 3


@pytest.mark.parametrize("appends", [0, 1, 5, 6, 9, 32])
def test_exact_fit_has_triangular_work_and_can_exhaust_fixed_credit(appends: int) -> None:
    rows = list(growth_trace(appends, "plus_one"))
    total = rows[-1].total if rows else 0
    assert total == appends * (appends + 1) // 2
    if appends >= 6:
        assert rows[-1].credit < 0


def test_negative_operation_count_is_rejected_on_iteration() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        list(growth_trace(-1))
