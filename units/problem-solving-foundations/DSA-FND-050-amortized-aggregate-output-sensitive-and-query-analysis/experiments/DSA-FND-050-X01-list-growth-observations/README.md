# DSA-FND-050-X01 — List growth observations

| Field | Value |
|---|---|
| Owning unit | [DSA-FND-050](../../README.md) |
| Curriculum | [CURRICULUM.md](../../../../../CURRICULUM.md#dsa-fnd-050) |
| Question | Does repeated append produce plateaus in shallow list storage, and what can those observations establish about cost? |
| Scope | CPython / platform observation, contrasted with an algorithm model |
| Runnable script | [list_growth.py](list_growth.py) |
| Status | Run |

## Why observation is necessary

A logical doubling trace cannot tell us which shallow byte sizes this Python build reports.
Observing a real list separates that runtime fact from the mathematical copy-count model.
The experiment intentionally does not time appends or infer invisible copies from size changes.

The recorded run is maintainer verification, not Rahul's learning evidence. Before a learner
reproduction, hide the observed-output section and record a prediction and its assumptions.
The expectations below come from the model and source contract, not a blind benchmark.

## Hypothesis

> A CPython list built by one-at-a-time appends will show runs of unchanged shallow size and
> occasional increases. Those increases need not match the toy doubling schedule. Shallow
> sizes alone will not establish append latency or the number of physically moved references.

Separately, the worked logical model predicts total copy/write counts of 24 for nine doubling
appends and 45 for nine exact-fit appends. Both contain an append costing nine modeled units;
their total work differs. These counts are derived before using runtime allocation observations.

## Environment

| Item | Recorded value |
|---|---|
| Date | 2026-08-30 UTC |
| Operating system / architecture | Linux / x86_64 |
| Python | CPython 3.14.7, locked project environment |
| Dependencies | Python standard library |
| Input distribution | Empty built-in list; append the same `None` reference 40 times |
| Observation passes | One deterministic traversal |
| Timing / warm-up / benchmark trials | Not applicable; no elapsed time is measured |

## Controls and measured variables

- Controlled: interpreter, initial empty list, built-in `append`, shared item, and no deletions.
- Changed: number of appended references, one at a time.
- Measured: `sys.getsizeof(values)` after each append, reported only when it changes.
- Initial observation: length zero, so the empty container's own shallow size remains visible.
- Not measured: deep object memory, process RSS, reserved allocator arenas, physical addresses,
  backing-array movement, copies, or individual/aggregate latency.

## Reproduction command

Run from the owning unit directory after the repository development environment is synced:

```bash
uv run --group dev python practice/micro_lab.py --appends 9 --policy double
uv run --group dev python practice/micro_lab.py --appends 9 --policy plus_one
uv run --group dev python experiments/DSA-FND-050-X01-list-growth-observations/list_growth.py --appends 40
```

The recorded verification used the equivalent repository `.venv/bin/python` after
`uv sync --group dev --locked`. The scripts are compatible with Python 3.11; the bytes below
are tied to the recorded interpreter and machine, not promised for every compatible runtime.

## Predicted output

For a fresh reproduction:

```text
Logical double model:   total=24; max_single=9
Logical plus_one model: total=45; max_single=9
Actual list: an initial size row, then occasional changes separated by unprinted lengths.
Exact byte sizes and transition lengths are observations, not portable expectations.
```

Write your own prediction before reading further. Do not label these supplied expectations
as a learner prediction or substitute a model count for an actual allocator measurement.

## Observed output

Actual maintainer run on the environment above:

```text
date_utc=2026-08-30
python=CPython 3.14.7
os=Linux; architecture=x86_64
appends=40; item=shared None; dependencies=stdlib
length shallow_bytes change_bytes
0 56 0
1 88 32
5 120 32
9 184 64
17 248 64
25 312 64
33 376 64
Unprinted lengths had unchanged shallow size.
Size changes do not establish a physical move, copy count, or latency.
```

The separate model runs reported:

| Policy | Appends | Total copy/write units | Largest single cost | Credit after charging 3 each |
|---|---:|---:|---:|---:|
| `double` | 9 | 24 | 9 | 3 |
| `plus_one` | 9 | 45 | 9 | -18 |

## Visual interpretation

```text
observed length range     shallow list bytes
0                          56
1..4                       88
5..8                      120
9..16                     184
17..24                    248
25..32                    312
33..40                    376   (40 is where this run stopped)
```

### How to read this visual

Every length in one row had the same reported shallow size during the run. The right edge of
the final row is an observation limit, not evidence of the next growth boundary.

### Key insight

The list's reported storage does not increase on every append. Its observed steps also differ
from the model capacities. A separate mathematical model is needed to bound copying work.

### Simplification or limitation

The numbers omit recursively referenced objects and allocator details. The unchanged size
between appends does not establish zero work or constant elapsed time for those appends.
The logical model simulates work counts and must not be benchmarked as an actual buffer.

## Interpretation

1. **Directly observed:** the shallow sizes and plateaus shown above on one environment.
2. **Supported inference:** spare backing storage is consistent with these observations and
   the versioned CPython implementation; the observations alone do not expose its physical
   allocation mechanism.
3. **Not established:** a byte change caused a physical copy; every append has constant latency;
   the list doubles; the empty container's bytes describe all memory retained by its elements.

Reconstruct the aggregate model proof independently. A finite table, even when repeated, is
not a proof for arbitrary operation sequences or an unspecified Python implementation.

## Threats to validity

- Versions, builds, architectures, and alternative interpreters may report different bytes.
- `sys.getsizeof` is shallow; appending shared `None` keeps object payload out of this workload.
- Growing via extension, concatenation, or preallocation is a different input history.
- Instrumentation and printing add work. No timing conclusion follows from this script.
- This append-only experiment says nothing about mixed grow/shrink histories or hard latency caps.

## Sources

- **Documented measurement contract:** [Python 3.14 sys.getsizeof](https://docs.python.org/3.14/library/sys.html#sys.getsizeof)
  excludes recursively referenced objects.
- **CPython implementation detail:** [CPython 3.14.7 list implementation](https://github.com/python/cpython/blob/v3.14.7/Objects/listobject.c)
  describes overallocated list storage. Exact allocation observations are platform facts.
- **Algorithm model:** the original [worked trace and aggregate proof](../../README.md#5-derivation-and-invariant)
  count references under a deliberately simpler policy.

Sources read on 2026-08-30; no external implementation code is copied.
