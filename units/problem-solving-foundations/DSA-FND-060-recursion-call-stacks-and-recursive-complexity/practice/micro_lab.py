"""A bounded teaching trace of prefix sums, separate from the learner challenges.

Stack snapshots describe logical calls, not CPython's physical frame layout.
Saving every snapshot costs quadratic reference storage; the plain sum does not.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

MAX_TRACE_LENGTH = 32


@dataclass(frozen=True)
class Event:
    action: Literal["call", "return"]
    prefix_size: int
    active_sizes: tuple[int, ...]
    returned: int | None


@dataclass(frozen=True)
class TraceRun:
    total: int
    calls: int
    max_active: int
    events: tuple[Event, ...]


def trace_prefix_sum(values: list[int]) -> TraceRun:
    """Trace the sum of a list of at most 32 integers without changing it."""
    if len(values) > MAX_TRACE_LENGTH:
        raise ValueError("teaching trace accepts at most 32 values")

    events: list[Event] = []
    active: list[int] = []
    calls = 0
    max_active = 0

    def visit(size: int) -> int:
        nonlocal calls, max_active
        active.append(size)
        calls += 1
        max_active = max(max_active, len(active))
        events.append(Event("call", size, tuple(active), None))
        if size == 0:
            total = 0
        else:
            child_total = visit(size - 1)
            total = child_total + values[size - 1]
        # The returning call is still active in this snapshot.
        events.append(Event("return", size, tuple(active), total))
        active.pop()
        return total

    total = visit(len(values))
    return TraceRun(total, calls, max_active, tuple(events))


def main() -> None:
    values = [7, -2, 4]
    run = trace_prefix_sum(values)
    print(f"values={values}; one shared input list")
    print("event   size  active calls (root -> current)  returned")
    for event in run.events:
        stack = " > ".join(str(size) for size in event.active_sizes)
        returned = "-" if event.returned is None else str(event.returned)
        print(f"{event.action:6}  {event.prefix_size:4}  {stack:30}  {returned}")
    print(f"total={run.total} calls={run.calls} max_active={run.max_active}")
    print("Snapshots include the returning frame and are not constant-size records.")


if __name__ == "__main__":
    main()
