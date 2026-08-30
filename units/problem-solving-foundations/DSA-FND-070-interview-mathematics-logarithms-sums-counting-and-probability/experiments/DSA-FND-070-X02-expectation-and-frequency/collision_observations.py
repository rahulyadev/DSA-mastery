"""Compare exact tiny sample spaces with seeded observations of a declared model."""

import platform
from collections.abc import Sequence
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from random import Random


@dataclass(frozen=True)
class Summary:
    trials: int
    pair_total: int
    trials_with_collision: int

    @property
    def mean_pairs(self) -> Fraction:
        return Fraction(self.pair_total, self.trials)

    @property
    def probability_any(self) -> Fraction:
        return Fraction(self.trials_with_collision, self.trials)


def collision_pairs(labels: Sequence[int]) -> int:
    """Count matching position pairs, which differs from counting occupied buckets."""
    return sum(
        1 for i in range(len(labels)) for j in range(i + 1, len(labels)) if labels[i] == labels[j]
    )


def exact_summary(items: int, buckets: int) -> Summary:
    """Enumerate a deliberately small space of independent uniform assignments."""
    if not 0 <= items <= 8 or not 1 <= buckets <= 100:
        raise ValueError("exact lab requires 0..8 items and 1..100 buckets")
    if buckets**items > 100_000:
        raise ValueError("exact lab is limited to 100000 assignments")
    trials = pair_total = trials_with_collision = 0
    for labels in product(range(buckets), repeat=items):
        count = collision_pairs(labels)
        trials += 1
        pair_total += count
        trials_with_collision += int(count > 0)
    return Summary(trials, pair_total, trials_with_collision)


def sampled_summary(items: int, buckets: int, trials: int, seed: int) -> Summary:
    """Use a local generator; the same inputs reproduce a run in the same environment."""
    if not 0 <= items <= 8 or not 1 <= buckets <= 100 or not 1 <= trials <= 100_000:
        raise ValueError("sample lab requires 0..8 items, 1..100 buckets, 1..100000 trials")
    rng = Random(seed)
    pair_total = trials_with_collision = 0
    for _ in range(trials):
        labels = [rng.randrange(buckets) for _ in range(items)]
        count = collision_pairs(labels)
        pair_total += count
        trials_with_collision += int(count > 0)
    return Summary(trials, pair_total, trials_with_collision)


def main() -> None:
    print(f"Python: {platform.python_implementation()} {platform.python_version()}")
    print(f"Platform: {platform.system()} {platform.machine()}")
    items, buckets = 3, 4
    exact = exact_summary(items, buckets)
    print(f"Model: {items} labelled items independently choose one of {buckets} uniform buckets")
    print(
        f"Exact: assignments={exact.trials} E[pairs]={exact.mean_pairs} "
        f"P(any)={exact.probability_any}"
    )
    print("seed trials pair_total trials_with_collision mean_pairs frequency_any")
    for seed in (7, 23):
        for trials in (100, 1000, 10000):
            sample = sampled_summary(items, buckets, trials, seed)
            print(
                seed,
                trials,
                sample.pair_total,
                sample.trials_with_collision,
                f"{float(sample.mean_pairs):.6f}",
                f"{float(sample.probability_any):.6f}",
            )
    print("Rows with the same seed share prefixes. No monotone-convergence assertion is made.")


if __name__ == "__main__":
    main()
