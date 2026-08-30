"""Trace counted body visits, not elapsed time or every Python operation.

These are worked teaching specimens. The practice contracts use different loops.
Inputs are non-negative integers. The CLI deliberately limits display sizes.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class CountRow:
    outer_index: int
    body_visits: int
    total_visits: int


@dataclass(frozen=True)
class DoublingRow:
    step: int
    before: int
    after: int


def require_non_negative(value: int, name: str) -> None:
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def rectangle_trace(n: int, m: int) -> list[CountRow]:
    """Count one event per (i, j); keep a summary even for an empty inner loop."""
    require_non_negative(n, "n")
    require_non_negative(m, "m")
    rows: list[CountRow] = []
    total = 0
    for i in range(n):
        visits = 0
        for _ in range(m):
            visits += 1
            total += 1
        rows.append(CountRow(i, visits, total))
    return rows


def triangle_trace(n: int) -> list[CountRow]:
    """Count one event for each 0 <= j < i < n, including the empty first row."""
    require_non_negative(n, "n")
    rows: list[CountRow] = []
    total = 0
    for i in range(n):
        visits = 0
        for _ in range(i):
            visits += 1
            total += 1
        rows.append(CountRow(i, visits, total))
    return rows


def doubling_trace(limit: int) -> list[DoublingRow]:
    """Record the states of p = 1; while p < limit: p *= 2."""
    require_non_negative(limit, "limit")
    rows: list[DoublingRow] = []
    position = 1
    step = 0
    while position < limit:
        after = position * 2
        rows.append(DoublingRow(step, position, after))
        position = after
        step += 1
    return rows


def render_counts(label: str, rows: list[CountRow]) -> str:
    lines = [label, "outer  body_visits  total_visits"]
    lines.extend(f"{r.outer_index:5d}  {r.body_visits:11d}  {r.total_visits:12d}" for r in rows)
    total = rows[-1].total_visits if rows else 0
    lines.append(f"outer_iterations={len(rows)}; body_visits={total}")
    return "\n".join(lines)


def render_doubling(limit: int, rows: list[DoublingRow]) -> str:
    lines = [f"doubling: limit={limit}", "step  before  after"]
    lines.extend(f"{r.step:4d}  {r.before:6d}  {r.after:5d}" for r in rows)
    final_position = rows[-1].after if rows else 1
    lines.append(f"body_visits={len(rows)}; final_position={final_position}; guard=false")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=4)
    parser.add_argument("--m", type=int, default=3)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    if not 0 <= args.n <= 30 or not 0 <= args.m <= 30:
        parser.error("display sizes n and m must be between 0 and 30")
    if not 0 <= args.limit <= 1_000_000:
        parser.error("display limit must be between 0 and 1,000,000")

    print("Teaching traces: predict the rows before running.")
    print("Counts exclude guards, allocation, formatting, and integer bit costs.\n")
    print(render_counts(f"rectangle: n={args.n}, m={args.m}", rectangle_trace(args.n, args.m)))
    print()
    print(render_counts(f"triangle: n={args.n}", triangle_trace(args.n)))
    print()
    print(render_doubling(args.limit, doubling_trace(args.limit)))


if __name__ == "__main__":
    main()
