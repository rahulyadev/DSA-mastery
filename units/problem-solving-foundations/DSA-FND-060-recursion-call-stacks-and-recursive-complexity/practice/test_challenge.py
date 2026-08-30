"""Unsolved contracts: collect during initialization; run only after an attempt.

Literal expected results and boundary checks specify behavior, not an algorithm.
Complexity, recursive structure, and the no-copy rule also require code review.
"""

from __future__ import annotations

import pytest
from starter import Packet, is_mirror, summarize_packet


@pytest.mark.parametrize(
    ("values", "lo", "hi", "expected"),
    [
        ([], 0, 0, True),
        ([6], 0, 1, True),
        ([6], 1, 1, True),
        ([4, 4], 0, 2, True),
        ([4, 5], 0, 2, False),
        ([2, 5, 2], 0, 3, True),
        ([2, 5, 5, 2], 0, 4, True),
        ([2, 5, 6, 2], 0, 4, False),
        ([90, -2, 0, -2, 91], 1, 4, True),
        ([90, -2, 0, -2, 91], 0, 5, False),
        ([8, 8, 8, 7, 8, 8], 0, 6, False),
    ],
)
def test_mirror_contract(values: list[int], lo: int, hi: int, expected: bool) -> None:
    original = values.copy()
    assert is_mirror(values, lo, hi) is expected
    assert values == original


@pytest.mark.parametrize("bounds", [(-1, 1), (0, 4), (2, 1), (4, 4), (0, -1)])
def test_invalid_interval_is_rejected(bounds: tuple[int, int]) -> None:
    with pytest.raises(ValueError):
        is_mirror([1, 2, 1], *bounds)


@pytest.mark.parametrize(
    ("packet", "expected"),
    [
        (7, (7, 0)),
        (-3, (-3, 0)),
        ((), (0, 1)),
        ((2, -1, 4), (5, 1)),
        ((((),),), (0, 3)),
        ((2, (6, ()), -3), (5, 3)),
        (((), (1, (2, -4)), 5), (4, 3)),
    ],
)
def test_packet_contract(packet: Packet, expected: tuple[int, int]) -> None:
    assert summarize_packet(packet) == expected


def test_shared_subtuple_is_counted_by_occurrence() -> None:
    shared = (2, -1)
    assert summarize_packet((shared, shared)) == (2, 2)


def test_calls_do_not_reuse_an_earlier_result_or_accumulator() -> None:
    assert summarize_packet((4, (1,))) == (5, 2)
    assert summarize_packet(()) == (0, 1)
    assert summarize_packet(-8) == (-8, 0)
    assert is_mirror([1, 2, 1], 0, 3) is True
    assert is_mirror([1, 2], 0, 2) is False


def test_depth_and_width_are_independent_boundaries() -> None:
    nested: Packet = 7
    for _ in range(40):
        nested = (nested,)
    assert summarize_packet(nested) == (7, 40)
    assert summarize_packet((1,) * 1000) == (1000, 1)
