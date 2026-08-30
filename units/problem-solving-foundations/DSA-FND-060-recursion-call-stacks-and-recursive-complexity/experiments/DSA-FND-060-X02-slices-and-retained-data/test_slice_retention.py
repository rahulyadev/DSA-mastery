"""Check sums, preservation, retained-copy accounting, and safe sampling boundaries."""

from __future__ import annotations

import tracemalloc

import pytest
from slice_retention import allocation_sample, walk


@pytest.mark.parametrize("size", [0, 1, 2, 5, 16, 32])
def test_same_result_and_depth_but_different_copy_cost(size: int) -> None:
    values = list(range(-size, 0))
    original = values.copy()
    bounds = walk(values, "bounds")
    slices = walk(values, "slices")
    assert bounds.total == slices.total == sum(values)
    assert bounds.calls == slices.calls == size + 1
    assert bounds.max_active == slices.max_active == size + 1
    assert bounds.copied_refs == bounds.peak_copied_refs == 0
    expected_slots = size * (size - 1) // 2
    assert slices.copied_refs == slices.peak_copied_refs == expected_slots
    assert values == original


def test_allocation_sample_reports_an_observation_without_a_fixed_byte_expectation() -> None:
    work, peak = allocation_sample(8, "slices")
    assert work.total == 8
    assert work.copied_refs == 28
    assert peak > 0
    assert not tracemalloc.is_tracing()


def test_existing_tracer_is_not_disabled_or_reset() -> None:
    tracemalloc.start()
    try:
        with pytest.raises(RuntimeError, match="existing tracemalloc"):
            allocation_sample(8, "bounds")
        assert tracemalloc.is_tracing()
    finally:
        tracemalloc.stop()


def test_size_caps_reject_unbounded_experiments() -> None:
    with pytest.raises(ValueError, match="at most 128"):
        walk([1] * 129, "slices")
    with pytest.raises(ValueError, match="between 0 and 128"):
        allocation_sample(-1, "bounds")
