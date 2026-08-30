"""Unsolved learner boundaries for DSA-FND-060-P02 and DSA-FND-060-P03.

Record a contract, a tiny trace, a correctness argument, and costs before coding.
Do not replace an earlier attempt; preserve it when making a later revision.
"""

from __future__ import annotations

from typing import TypeAlias

Packet: TypeAlias = int | tuple["Packet", ...]  # noqa: UP040 -- Python 3.11 compatibility.


def is_mirror(values: list[int], lo: int, hi: int) -> bool:
    """Test whether values[lo:hi] reads identically in either direction.

    hi is exclusive. Invalid bounds raise ValueError. Empty intervals are valid.
    The implementation must use recursion, avoid copies, and preserve values.
    See the practice contract for the bounded input sizes used in this exercise.
    """
    raise NotImplementedError("DSA-FND-060-P02: make and record your first attempt")


def summarize_packet(packet: Packet) -> tuple[int, int]:
    """Return (sum of integer leaves, maximum tuple nesting depth).

    An integer has depth zero; an empty tuple has depth one. Reused subtuples
    count once per occurrence in the expanded input. No state carries between calls.
    """
    raise NotImplementedError("DSA-FND-060-P03: make and record your first attempt")
