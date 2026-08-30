"""Count additions/subtractions for two worked snapshot-query strategies.

Direct scans and an eager prefix table must return identical scalar answers.
The selected arithmetic counter excludes indexing, validation, loop overhead,
allocation, and result storage. It is not a timing comparison. Python 3.11+.
"""

from __future__ import annotations

import argparse
import platform
from collections.abc import Sequence
from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True)
class BatchResult:
    direct_answers: tuple[int, ...]
    indexed_answers: tuple[int, ...]
    direct_additions: int
    build_additions: int
    query_subtractions: int
    table_entries: int

    @property
    def indexed_arithmetic(self) -> int:
        return self.build_additions + self.query_subtractions


def compare_batch(values: Sequence[int], queries: Sequence[tuple[int, int]]) -> BatchResult:
    """Compare fixed strategies on valid half-open ranges of an unchanged input.

    Deliberately build the prefix table even if there are no queries, so the
    cost of eager preprocessing remains visible. Inputs are never mutated.
    """
    n = len(values)
    for left, right in queries:
        if not 0 <= left <= right <= n:
            raise ValueError("each query must satisfy 0 <= left <= right <= len(values)")

    direct: list[int] = []
    direct_additions = 0
    for left, right in queries:
        total = 0
        for index in range(left, right):
            total += values[index]
            direct_additions += 1
        direct.append(total)

    prefix = [0]
    build_additions = 0
    for value in values:
        prefix.append(prefix[-1] + value)
        build_additions += 1

    indexed: list[int] = []
    query_subtractions = 0
    for left, right in queries:
        indexed.append(prefix[right] - prefix[left])
        query_subtractions += 1

    return BatchResult(
        direct_answers=tuple(direct),
        indexed_answers=tuple(indexed),
        direct_additions=direct_additions,
        build_additions=build_additions,
        query_subtractions=query_subtractions,
        table_entries=len(prefix),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=12)
    args = parser.parse_args()
    if not 0 <= args.n <= 1000:
        parser.error("n must be 0..1000 for this deterministic experiment")

    print(f"date_utc={datetime.now(UTC).date()}")
    print(f"python={platform.python_implementation()} {platform.python_version()}")
    print(f"os={platform.system()}; architecture={platform.machine()}")
    print("values[i]=(i % 7)-3; fixed widths; left endpoints cycle; dependencies=stdlib")
    print("n width queries scan_additions build_additions query_subtractions indexed_total equal")
    values = [(index % 7) - 3 for index in range(args.n)]
    for width in sorted({0, min(3, args.n), args.n}):
        for count in (0, 1, 2, 4, 8):
            queries = [
                (index % (args.n - width + 1), index % (args.n - width + 1) + width)
                for index in range(count)
            ]
            result = compare_batch(values, queries)
            if result.direct_answers != result.indexed_answers:
                raise AssertionError("worked strategies returned different answers")
            print(
                args.n,
                width,
                count,
                result.direct_additions,
                result.build_additions,
                result.query_subtractions,
                result.indexed_arithmetic,
                True,
            )
    print("A zero arithmetic count does not remove per-query runtime or output storage.")


if __name__ == "__main__":
    main()
