# DSA-FND-050-X02 — Repeated query work

| Field | Value |
|---|---|
| Owning unit | [DSA-FND-050](../../README.md) |
| Curriculum | [CURRICULUM.md](../../../../../CURRICULUM.md#dsa-fnd-050) |
| Question | How do request count and range width affect the arithmetic work of scans versus an eager prefix table? |
| Scope | Algorithm / Python operation counts; not a timing benchmark |
| Runnable script | [query_batches.py](query_batches.py) |
| Status | Run |

## Why observation is necessary

The phrase “constant-time query” can hide a build, empty workload, or unfair operation counter.
Instrumenting two worked strategies makes those components independently visible while checking
that both return the same answers. The observation checks a finite workload; the unit's
invariant and sums supply the general reasoning.

The code here is a worked teaching specimen, not the answer to a practice contract. A learner
should record predictions and reasoning before opening its output. The supplied expectations
are model calculations for reproduction, not recorded learner work.

## Hypothesis

> With `n` unchanged values and `q` queries of width `w`, direct scans perform `qw` additions.
> Eager preprocessing performs `n` additions, followed by `q` subtractions. As query width and
> count change, neither strategy minimizes this selected counter for every workload.

Both strategies should return identical scalar totals, including negative values and empty
ranges. Zero arithmetic still permits nonzero request handling and output-storage work.

## Environment

| Item | Recorded value |
|---|---|
| Date | 2026-08-30 UTC |
| Operating system / architecture | Linux / x86_64 |
| Python | CPython 3.14.7, locked project environment |
| Dependencies | Standard library for the script; pytest for correctness checks |
| Values | `values[i] = (i % 7) - 3`, with `n = 12` |
| Request widths | 0, 3, and 12 |
| Request counts | 0, 1, 2, 4, and 8 |
| Request starts | Cycle over valid left endpoints; no random sampling |
| Trial count | One deterministic comparison for each width/count pair |
| Timing / warm-up | Not applicable; elapsed time is not measured |

## Controls and measured variables

- Controlled: same unchanged input and same half-open ranges for both strategies.
- Changed: request count and range width; each batch starts with a fresh eagerly built table.
- Measured: direct additions, build additions, query subtractions, and answer equality.
- Excluded from this counter: indexing, comparisons, validation, loop dispatch, allocation,
  reference writes, counter increments, and output materialization. These still consume runtime.
- Space: the recorder retains both answer collections and the prefix table during comparison;
  its peak storage is `O(n + q + 1)` words under a bounded-integer model, apart from supplied
  inputs. It is not measuring either strategy's isolated peak memory.

## Reproduction command

From the owning unit directory:

```bash
uv run --group dev python experiments/DSA-FND-050-X02-repeated-query-work/query_batches.py --n 12
uv run --group dev python -m pytest -q experiments/DSA-FND-050-X02-repeated-query-work/test_query_batches.py
```

The recorded verification used the equivalent repository `.venv/bin/python` after the locked
development group was synced. All code uses Python 3.11-compatible syntax and APIs.

## Predicted output

Calculate the arithmetic columns for each new run before inspecting observed output:

```text
scan additions = q*w
build additions = n, including q=0 because this particular strategy builds eagerly
query subtractions = q, including empty ranges
indexed total = n+q
answer equality = True for every valid range
```

For example, the model predicts 24 scan additions versus 20 indexed arithmetic operations for
`n=12, w=3, q=8`. This is a comparison of selected operations, not a predicted speed ratio.

## Observed output

Actual maintainer run:

```text
date_utc=2026-08-30
python=CPython 3.14.7
os=Linux; architecture=x86_64
values[i]=(i % 7)-3; fixed widths; left endpoints cycle; dependencies=stdlib
n width queries scan_additions build_additions query_subtractions indexed_total equal
12 0 0 0 12 0 12 True
12 0 1 0 12 1 13 True
12 0 2 0 12 2 14 True
12 0 4 0 12 4 16 True
12 0 8 0 12 8 20 True
12 3 0 0 12 0 12 True
12 3 1 3 12 1 13 True
12 3 2 6 12 2 14 True
12 3 4 12 12 4 16 True
12 3 8 24 12 8 20 True
12 12 0 0 12 0 12 True
12 12 1 12 12 1 13 True
12 12 2 24 12 2 14 True
12 12 4 48 12 4 16 True
12 12 8 96 12 8 20 True
A zero arithmetic count does not remove per-query runtime or output storage.
```

## Visual interpretation

| Workload | Direct arithmetic | Eager index arithmetic | Lower selected count |
|---|---:|---:|---|
| One width-3 request | 3 | 13 | Scan |
| Eight width-3 requests | 24 | 20 | Index |
| One width-12 request | 12 | 13 | Scan |
| Two width-12 requests | 24 | 14 | Index |
| No requests | 0 | 12 | No build |

### How to read this visual

Every row keeps `n = 12`. Compare the two arithmetic totals for that workload, then check which
costs the counter excludes before making a broader performance claim.

### Key insight

Request count alone is insufficient: request widths and whether construction is reused matter.
For this counter, solve `qw > n + q`; when `w <= 1`, an eager table cannot win that inequality.

### Simplification or limitation

Per-query setup still exists even for empty ranges. Actual strategy time is
`Theta(1 + q + sum(w_i))` for scans versus `Theta(1 + n + q)` for the eager table under bounded
integer costs. Repeated requests can invite additional caching strategies, but this experiment
compares only the two specified strategies and does not establish global optimality.

## Interpretation

1. **Directly observed:** arithmetic counters agree with the predicted formulas on these
   batches, and both strategies return identical results.
2. **Supported inference:** in this model, more sufficiently wide requests can offset a shared
   build; very short or absent requests may not. The prefix invariant explains why answers agree.
3. **Not established:** a universal timing crossover, a speedup factor, a memory measurement,
   correctness with stale data, or suitability for every query operation.

The companion tests enumerate every valid range on all lists of lengths zero through four
over three signed values, compare against an independent small slicing oracle, reject invalid
boundaries, and check input preservation. Passing tests supplement rather than replace the
general invariant. They do not answer the learner's catalog-budget task.

## Threats to validity

- The artificial counter weights addition and subtraction equally and ignores other work.
- Python arbitrary-size integers can invalidate a constant-word arithmetic model as values grow.
- Values are immutable during a batch; updates require a new lifecycle analysis.
- The eager build is deliberate. A strategy that avoids unused construction has a different
  zero-request cost and should be named explicitly.
- Printing and instrumentation make this script unsuitable as a benchmark of production code.

## Sources

- **Original algorithm model:** the [unit's query trace and proof](../../README.md#6-detailed-visual-trace)
  define the prefix invariant, output contract, and work counters used here.
- **Documented Python semantics:** [Python 3.14 sequence operations](https://docs.python.org/3.14/library/stdtypes.html#typesseq)
  for index/slice boundaries used by the independent small-input oracle.

Sources read on 2026-08-30. Scripts, synthetic inputs, and explanations are original; no
external solution or proprietary problem statement is included.
