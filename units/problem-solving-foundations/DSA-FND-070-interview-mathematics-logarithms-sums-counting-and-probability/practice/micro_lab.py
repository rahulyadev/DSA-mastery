"""Small, complete teaching traces; independent practice remains unsolved."""

from fractions import Fraction
from itertools import product


def halving_trace(n: int) -> list[tuple[int, int]]:
    """Return (completed divisions, remaining) including initial and terminal states."""
    if n < 1:
        raise ValueError("n must be positive")
    rows = [(0, n)]
    remaining = n
    steps = 0
    while remaining > 1:
        remaining //= 2
        steps += 1
        rows.append((steps, remaining))
    return rows


def pair_trace(n: int) -> list[tuple[int, int, int]]:
    """Summarize i < j rows as (i, row size, cumulative size), without visiting pairs."""
    if n < 0:
        raise ValueError("n must be nonnegative")
    rows = []
    cumulative = 0
    for i in range(n):
        row_size = n - i - 1
        cumulative += row_size
        rows.append((i, row_size, cumulative))
    return rows


def series_trace(terms: int) -> list[tuple[int, int, int, Fraction]]:
    """Return (term number, power of two, geometric prefix, harmonic prefix)."""
    if terms < 0:
        raise ValueError("terms must be nonnegative")
    rows = []
    power = 1
    geometric = 0
    harmonic = Fraction(0)
    for term in range(1, terms + 1):
        geometric += power
        harmonic += Fraction(1, term)
        rows.append((term, power, geometric, harmonic))
        power *= 2
    return rows


def two_coin_outcomes() -> list[tuple[str, int, int]]:
    """Each fair independent two-coin outcome has mass 1/4."""
    rows = []
    for first, second in product("HT", repeat=2):
        heads = int(first == "H") + int(second == "H")
        rows.append((first + second, heads, int(heads > 0)))
    return rows


def main() -> None:
    print("FLOOR HALVING n=13: (divisions, remaining)")
    for halving_row in halving_trace(13):
        print(halving_row)
    print("PAIR ROW SUMMARIES n=4: (i, row size, cumulative)")
    for pair_row in pair_trace(4):
        print(pair_row)
    print("SERIES: term power geometric_sum harmonic_sum")
    for term, power, geometric, harmonic in series_trace(4):
        print(term, power, geometric, str(harmonic))
    print("TWO FAIR INDEPENDENT COINS: outcome heads any_heads")
    outcomes = two_coin_outcomes()
    for outcome, heads, any_heads in outcomes:
        print(outcome, heads, any_heads)
    print("E[heads] =", Fraction(sum(row[1] for row in outcomes), len(outcomes)))
    print("P(any heads) =", Fraction(sum(row[2] for row in outcomes), len(outcomes)))


if __name__ == "__main__":
    main()
