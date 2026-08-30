# DSA-FND-060-X02 — Slices and retained data

| Field | Value |
|---|---|
| Owning unit | [DSA-FND-060](../../README.md) |
| Curriculum | [CURRICULUM.md](../../../../../CURRICULUM.md#dsa-fnd-060) |
| Question | Can the same result, call count, and depth conceal different retained-data costs? |
| Scope | Algorithm copy accounting; CPython allocation observation |
| Runnable script | [slice_retention.py](slice_retention.py) |
| Status | Interpreted maintenance run; learner reproduction pending |

## Why observation is necessary

Both versions make one recursive call per remaining element and compute the same scalar total.
One uses an index into shared input; the other creates actual tail slices. Counters expose the
extra references, while an allocation sample shows why reference counts and measured bytes
must not be treated as interchangeable.

## Hypothesis

For `n` input values, both versions invoke `n+1` calls and reach depth `n+1`.
The bounds version copies no input references. The slices version creates
`n(n-1)/2` copied payload references and retains all of those payload slots at its deepest
point. Traced byte peaks should differ on sufficiently large samples, but no exact ratio or
byte threshold is a portable expectation.

## Environment

Implementation, version, operating system, architecture, and the read-only recursion limit are
printed by the script. Inputs contain `n` references to the already existing integer `1`.
Sizes are `0, 8, 32, 64, 128`, each measured once per strategy.

This is one allocation observation per row, not an elapsed-time benchmark. No warm-up is
performed. Garbage collection precedes each fresh trace session. Dependencies are the standard
library; no plotting package, native profiler, or operating-system memory monitor is required.

Recorded run: **2026-08-30**, CPython **3.14.7**, Linux **x86_64**; recursion limit **1000**.
The reproduction command was run through the locked project environment with
`UV_CACHE_DIR=/tmp/dsa-fnd-060-uv-cache`. This setting changes where uv stores its local cache,
not the experiment's algorithm or recursion policy.

## Controls and measured variables

- Controlled: input values, answer contract, recursion order, scalar output, and size cap.
- Changed: shared-input bounds versus freshly copied tails.
- Counted: invocations, maximum active logical calls, cumulative copied payload references,
  and peak simultaneously retained copied payload references.
- Observed: peak bytes among allocations visible to a fresh `tracemalloc` session.
- Original input is built before tracing and excluded from copy accounting.
- The input and its integers are not deep-copied. Frame references to the same tail list do
  not multiply that list's payload count.

## Reproduction command

From the unit directory:

```bash
uv run --group dev python experiments/DSA-FND-060-X02-slices-and-retained-data/slice_retention.py
uv run --group dev python -m pytest -q experiments/DSA-FND-060-X02-slices-and-retained-data/test_slice_retention.py
```

## Predicted output

Written before the full script run; byte peaks remain unpredicted:

```text
n     calls/depth (both)   copied refs (bounds)   copied refs (slices)
0                     1                     0                      0
8                     9                     0                     28
32                   33                     0                    496
64                   65                     0                   2016
128                 129                     0                   8128
```

The scalar total should equal `n`. Peak copied payload slots should equal cumulative copies
for this chain of tail slices because all ancestor tails remain reachable.

## Observed output

Actual stdout from the recorded run:

```text
Python: CPython 3.14.7
Platform: Linux x86_64
Recursion limit (read only): 1000
Input: n existing references to integer 1; input allocation excluded
One allocation sample per row; no elapsed-time benchmark
strategy     n   total  calls  depth  copies  peak_copy_slots  traced_peak_bytes
bounds       0       0      1      1       0                0               1576
slices       0       0      1      1       0                0               1568
bounds       8       8      9      9       0                0               1560
slices       8       8      9      9      28               28               2144
bounds      32      32     33     33       0                0               1544
slices      32      32     33     33     496              496               7344
bounds      64      64     65     65       0                0               1520
slices      64      64     65     65    2016             2016              21272
bounds     128     128    129    129       0                0               1504
slices     128     128    129    129    8128             8128              73736
```

## Visual interpretation

```text
original size 4 (borrowed; excluded from extra payload)
   tail size 3  ┐
     tail size 2├─ simultaneously retained copied payload = 6 references
       tail 1  ┘
         empty tail = 0 payload references, but still a list object
```

### How to read this visual

Descend through successive tail slices. Each nonempty tail remains referenced while its
smaller child runs. Count each distinct list's payload once and ignore the borrowed input.

### Key insight

Linear frame count is not a bound on everything those frames retain.

### Simplification or limitation

The picture counts payload references. Measured bytes also depend on list headers, bookkeeping,
allocator behavior, interpreter details, and which allocations the tracer sees.

## Interpretation

1. All predicted totals, call counts, depths, and copy counts matched. At size 128, both
   versions reached 129 logical calls, but the slice version retained 8128 extra payload
   references. Its sampled peak was 73,736 traced bytes versus 1504 for bounds.
2. The copy formula supports quadratic payload growth for this particular sliced program.
   Index bounds remove those copies; they do not remove its growing logical call stack.
3. Finite measurements do not prove an asymptotic bound. A small or flat traced peak does not
   prove constant stack space. Traced Python allocation blocks are not a complete account of
   process memory, native stack, or every interpreter allocation.

The bounds peaks even decrease slightly across these rows while logical depth grows.
That observation is not evidence of shrinking stack use. The experiment does not isolate which
allocator or interpreter detail causes that small byte variation, so no such explanation is
claimed. Repeat runs may produce different byte values.

## Threats to validity

- Both strategies include instrumentation and setup. Exact byte values are not assertions.
- Input creation is excluded; the scalar result and bookkeeping are included.
- Empty slices cost objects even though they contribute zero payload references.
- One sample has no statistical interpretation. There is no claimed timing speedup.
- The script refuses to reset or stop an existing tracing session and never changes the
  recursion limit. A specially lowered runtime limit can still prevent execution.
- The 128-element cap bounds the demonstration; do not remove it to provoke a crash.

## Sources

Read on 2026-08-30:

- [Python sequence copying](https://docs.python.org/3.14/library/stdtypes.html#mutable-sequence-types):
  shallow-copy contract.
- [CPython 3.14.7 list implementation](https://github.com/python/cpython/blob/v3.14.7/Objects/listobject.c):
  allocation and reference-copy implementation evidence.
- [tracemalloc API](https://docs.python.org/3.14/library/tracemalloc.html#tracemalloc.get_traced_memory):
  definition of traced current and peak allocation bytes.

Recorded maintenance runs belong here. Rahul's predictions, interpretation, hints, and delayed
recall belong in the separate learning evidence record.
