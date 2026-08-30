"""Check measured trees against independently derived node and height identities."""

from __future__ import annotations

import pytest
from call_shapes import count_shape


@pytest.mark.parametrize("size", [0, 1, 2, 3, 4, 7, 8, 9, 31, 64])
def test_chain_has_one_leaf_and_keeps_every_ancestor(size: int) -> None:
    counts = count_shape(size, "chain")
    assert (counts.calls, counts.leaves, counts.max_active) == (size + 1, 1, size + 1)


@pytest.mark.parametrize("size", [0, 1, 2, 3, 4, 7, 8, 9, 31, 64])
def test_halving_rounding_and_empty_base(size: int) -> None:
    counts = count_shape(size, "halve")
    height = max(1, size.bit_length())
    assert (counts.calls, counts.leaves, counts.max_active) == (height, 1, height)


@pytest.mark.parametrize("size", [1, 2, 3, 4, 7, 8, 9, 31, 64])
def test_split_tree_has_one_leaf_per_item_and_full_binary_node_count(size: int) -> None:
    counts = count_shape(size, "split")
    assert counts.leaves == size
    assert counts.calls == 2 * counts.leaves - 1
    assert counts.max_active == (size - 1).bit_length() + 1


@pytest.mark.parametrize("size", [0, 1, 2, 4, 8, 12])
def test_repeated_work_can_grow_exponentially_without_exponential_depth(size: int) -> None:
    counts = count_shape(size, "repeat")
    assert counts.leaves == 2**size
    assert counts.calls == 2 ** (size + 1) - 1
    assert counts.max_active == size + 1


def test_empty_split_and_safety_caps() -> None:
    assert count_shape(0, "split").calls == 1
    with pytest.raises(ValueError, match="between"):
        count_shape(-1, "chain")
    with pytest.raises(ValueError, match="between"):
        count_shape(13, "repeat")
    with pytest.raises(ValueError, match="between"):
        count_shape(129, "chain")
