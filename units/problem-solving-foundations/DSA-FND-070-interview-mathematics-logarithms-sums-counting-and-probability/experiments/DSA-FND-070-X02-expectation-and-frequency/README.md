# DSA-FND-070-X02 — Expectation and observed frequency

| Field | Value |
|---|---|
| Owning unit | [DSA-FND-070](../../README.md) |
| Curriculum | [CURRICULUM.md](../../../../../CURRICULUM.md#dsa-fnd-070) |
| Question | How do the mean number of matching pairs and the frequency of any match differ, and how do finite observations compare with an exact tiny model? |
| Scope | Algorithm/probability model and seeded standard-library observation; not a benchmark |
| Runnable script | [collision_observations.py](collision_observations.py) |
| Checks | [test_collision_observations.py](test_collision_observations.py) |
| Status | Interpreted |

## Why observation is necessary

Two statistics can be computed on exactly the same random outcomes and converge toward different
targets. Finite prefixes can also move away from a target when more trials are added. Comparing
an exact tiny enumeration with several observed prefixes makes both distinctions inspectable.
It does not prove a randomness guarantee, a convergence rate, or a hash-table performance bound.

## Hypothesis

In the ideal model, three distinguishable items independently choose one of four equally likely
bucket labels. Let `X` count matching unordered pairs of item positions; let `Y` be one when
`X > 0`, otherwise zero. We predict `E[X] = 3/4` and `E[Y] = P(X>0) = 5/8`. Empirical means
should fluctuate around their own targets. There is no prediction that every larger prefix is
closer, or that two seeds must have a particular ordering.

## Environment

- Date: 2026-08-30 (maintainer initialization run).
- Python implementation/version, operating system, and architecture are printed by the script.
- Dependencies: Python standard library; pytest only for deterministic scaffold checks.
- Declared model: independent uniform bucket choices, sampled with a local `random.Random`.
- Exact workload: all `4^3 = 64` assignments.
- Observation workloads: seeds `7` and `23`, each with `100`, `1000`, and `10000` trials.
- Timing/warm-up: not applicable; this experiment measures counts and frequencies, not speed.

## Controls and measured variables

- Controlled: three items, four labels, the event/count definitions, and generator seed per block.
- Changed: seed and number of sampled trials.
- Measured: pair total, number of trials containing any pair, mean pairs, and event frequency.
- The generator is restarted for each row. Rows with the same seed share prefixes and are
  not independent experiments. Do not treat the six displayed rows as six independent estimates.
- Exact enumeration is capped at 100000 assignments. Both helpers also bound items and buckets;
  sample trials are capped at 100000. No unbounded search is performed.

## Reproduction command

From this experiment directory:

```bash
uv run --group dev python collision_observations.py
uv run --group dev python -m pytest -q test_collision_observations.py
```

In a restricted sandbox, prefix a command with `env UV_CACHE_DIR=/tmp/dsa-fnd-070-uv-cache`
if the default uv cache is read-only. No credentials or network connection are needed by the script.

## Predicted output

```text
Exact assignment count: 64
Assignments with any matching pair: 40
Total matching pairs across all assignments: 48
Exact E[pairs]: 48/64 = 3/4
Exact P(any):   40/64 = 5/8
Observed rows: specific integer totals are not predicted in advance.
```

There are three position pairs, and each matches with probability `1/4`, so linearity gives the
first mean. The no-match assignments choose three distinct labels in order: `4*3*2 = 24`.
Their complement gives the second probability. The pair-match events are not mutually
independent, so multiplying all their failure probabilities would need an invalid assumption.

## Observed output

Executed on 2026-08-30 during initialization, using the command above. This is a maintainer
observation; Rahul has not yet completed the predict/run/interpret cycle.

```text
Python: CPython 3.14.7
Platform: Linux x86_64
Model: 3 labelled items independently choose one of 4 uniform buckets
Exact: assignments=64 E[pairs]=3/4 P(any)=5/8
seed trials pair_total trials_with_collision mean_pairs frequency_any
7 100 77 63 0.770000 0.630000
7 1000 720 610 0.720000 0.610000
7 10000 7478 6216 0.747800 0.621600
23 100 70 62 0.700000 0.620000
23 1000 729 607 0.729000 0.607000
23 10000 7475 6203 0.747500 0.620300
Rows with the same seed share prefixes. No monotone-convergence assertion is made.
```

Exact enumeration agrees with the two distinct predicted targets. For seed 7, mean-pair
error increases from `0.02` at 100 trials to `0.03` at 1000 trials before decreasing at 10000.
Thus this actual run also illustrates why a larger prefix is not guaranteed to be closer.
The observed frequencies remain measurements of this model, not proofs about arbitrary data.

## Visual interpretation

```text
item labels       matching pairs X      any match Y
(0, 1, 2)                0                   0
(0, 0, 2)                1                   1
(0, 0, 0)                3                   1
```

### How to read this visual

Each row is an example complete assignment. Compare the count column with the yes/no indicator.
These are examples, not three equally weighted categories of the full sample space.

### Key insight

One trial can contribute several matching pairs but only one “any match.” Consequently the two
column averages need not coincide; an expected pair count can even exceed one in other inputs.

### Simplification or limitation

The ideal model supplies equal independent choices. A seeded pseudorandom stream is used to
observe that model; it is not evidence that arbitrary real-world labels or Python hashes behave
this way. Counting matching pairs is also different from counting occupied buckets.

## Interpretation

Exact enumeration checks the stated finite model, not every possible sampling model. The
empirical mean is `pair_total/trials`; empirical event frequency is `trials_with_collision/trials`.
Finite differences from the exact targets are observations, not algorithmic counterexamples.
No arbitrary closeness threshold is used in tests. Tests compare exact enumeration to separate
counting arguments, check degenerate models, and check same-environment seed reproducibility.

For `m` items, `b` buckets, and `T` trials, each measured assignment performs `C(m,2)` equality
checks. Exact enumeration has `b^m` assignments and needs
`O(b + b^m * (1 + m + m^2))` word-model work including outcome construction and iterator setup.
`itertools.product` stores its input pool, so exact auxiliary storage is `O(b+m)` items, not
merely `O(m)`. It retains no list of all outcomes. Sampled work is
`O(T * (1 + m + m^2))` assuming unit-cost draws/comparisons; auxiliary storage is `O(m)` items
plus generator state. Scalar aggregate output and constant call-stack depth are separate.
Large counters, random range generation, and rational reduction add bit-dependent costs.

## Threats to validity

- More samples need not improve each prefix monotonically; seeds must not be cherry-picked.
- Shared prefixes are correlated. No confidence interval or rate-of-convergence claim is made.
- If choices become biased or dependent, these exact target values no longer describe the model.
- Python documents version limits for random-module reproducibility; no portable sequence of
  `randrange` outputs is asserted across all future Python versions.
- The generator is for simulation, not security. The repository records no secret seed or real data.
- A maintainer's initialization run is artifact evidence, not Rahul's experiment completion.

## Sources

Read on 2026-08-30: [MIT's linearity-of-expectation treatment, section 18.3](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/93cad640cf3ed0b23ef70688f452d4d5_MIT6_042JF10_notes.pdf),
[Python random and reproducibility](https://docs.python.org/3.14/library/random.html#notes-on-reproducibility),
and [Python Fraction construction](https://docs.python.org/3.14/library/fractions.html).
The count derivations and experimental code are original; measured frequencies are runtime observations.
