"""Passing checks for the provided teaching trace; no learner implementation is run."""

from __future__ import annotations

import pytest
from micro_lab import trace_prefix_sum


def test_tiny_trace_shows_descent_and_return_values() -> None:
    run = trace_prefix_sum([7, -2, 4])
    assert (run.total, run.calls, run.max_active) == (9, 4, 4)
    assert [(event.action, event.prefix_size, event.returned) for event in run.events] == [
        ("call", 3, None),
        ("call", 2, None),
        ("call", 1, None),
        ("call", 0, None),
        ("return", 0, 0),
        ("return", 1, 7),
        ("return", 2, 5),
        ("return", 3, 9),
    ]


@pytest.mark.parametrize("values", [[], [0], [-4], [3, -3], [2, 2, -5, 9]])
def test_returns_match_an_independent_prefix_oracle_and_frames_balance(
    values: list[int],
) -> None:
    original = values.copy()
    run = trace_prefix_sum(values)
    active: list[int] = []
    for event in run.events:
        if event.action == "call":
            active.append(event.prefix_size)
            assert event.returned is None
        else:
            assert active[-1] == event.prefix_size
            assert event.returned == sum(values[: event.prefix_size])
        assert tuple(active) == event.active_sizes
        if event.action == "return":
            active.pop()
    assert active == []
    assert values == original
    assert run.total == sum(values)
    assert run.calls == len(values) + 1
    assert run.max_active == len(values) + 1
    assert len(run.events) == 2 * run.calls


def test_snapshots_expose_their_own_storage_cost() -> None:
    run = trace_prefix_sum([1] * 8)
    # Every active depth occurs once on entry and once on return.
    assert sum(len(event.active_sizes) for event in run.events) == 9 * 10
    assert run.events[0].active_sizes == (8,)


def test_trace_guard_prevents_accidental_large_snapshot_output() -> None:
    with pytest.raises(ValueError, match="at most 32"):
        trace_prefix_sum([1] * 33)
