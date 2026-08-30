# DSA-FND-060-X01 — Calls and depth

| Field | Value |
|---|---|
| Owning unit | [DSA-FND-060](../../README.md) |
| Curriculum | [CURRICULUM.md](../../../../../CURRICULUM.md#dsa-fnd-060) |
| Question | Can similar recursion depths hide very different amounts of executed work? |
| Scope | Algorithm counters; Python runtime context |
| Runnable script | [call_shapes.py](call_shapes.py) |
| Status | Interpreted maintenance run; learner reproduction pending |

## Why observation is necessary

A drawing can make all siblings look simultaneously active. Running the bounded shapes counts
actual calls while recording only the greatest active depth. It also exposes floors, empty-base
conventions, and whether a purported single child actually executes twice.

These are synthetic execution shapes, not implementations of the learner challenges.

## Hypothesis

At size eight, a decrementing chain and a repeated decrementing tree both reach nine active
calls, while their total invocations differ. One halved child and both disjoint halved children
have the same maximum active depth on powers of two but different total invocation counts.

## Environment

The script prints implementation, Python version, operating system, architecture, and the
current recursion limit. Input sizes are deterministic. Each shape/size runs once; this is
an exact-count experiment, not a timing benchmark. No warm-up or clock measurement is needed.
Only the Python standard library is used.

Recorded run: **2026-08-30**, CPython **3.14.7**, Linux **x86_64**. The printed recursion limit
was **1000**. The reproduction command was run through the locked project environment
with `UV_CACHE_DIR=/tmp/dsa-fnd-060-uv-cache` to accommodate the host's cache permissions.

## Controls and measured variables

- Controlled: sequential child execution, constant-size local state, no saved tree, no cache.
- Changed: initial size and execution shape.
- Measured: every invocation including base calls, number of base calls, maximum active calls.
- `chain`: one child of size `n-1`, base at zero.
- `halve`: one child of size `floor(n/2)`, base at zero or one.
- `split`: children `floor(n/2)` and `n-floor(n/2)`, base at zero or one.
- `repeat`: two separate children of size `n-1`, base at zero.

## Reproduction command

From the unit directory:

```bash
uv run --group dev python experiments/DSA-FND-060-X01-calls-and-depth/call_shapes.py
uv run --group dev python -m pytest -q experiments/DSA-FND-060-X01-calls-and-depth/test_call_shapes.py
```

## Predicted output

Written before the full script run:

```text
shape   n   calls  leaves  max_active
chain   8       9       1           9
halve   8       4       1           4
split   8      15       8           4
repeat  8     511     256           9
```

Every shape's size-zero case is one invocation, one leaf, and one active frame. Runtime header
values are read from the environment rather than predicted.

## Observed output

Actual stdout from the recorded run:

```text
Python: CPython 3.14.7
Platform: Linux x86_64
Recursion limit (read only): 1000
shape       n     calls    leaves  max_active
chain       0         1         1           1
chain       1         2         1           2
chain       4         5         1           5
chain       8         9         1           9
chain      16        17         1          17
chain      64        65         1          65
halve       0         1         1           1
halve       1         1         1           1
halve       4         3         1           3
halve       8         4         1           4
halve      16         5         1           5
halve      64         7         1           7
split       0         1         1           1
split       1         1         1           1
split       4         7         4           3
split       8        15         8           4
split      16        31        16           5
split      64       127        64           7
repeat      0         1         1           1
repeat      1         3         2           2
repeat      4        31        16           5
repeat      8       511       256           9
repeat     12      8191      4096          13
```

## Visual interpretation

```text
all executed invocations ----------> total work, if local work is bounded
longest active root-to-current path -> logical recursion-stack depth
saved buffers or returned results --> an additional storage calculation
```

### How to read this visual

Use separate ledgers for events across time and objects alive at one instant. A frame count
includes the base call but excludes the experiment wrapper and unrelated Python callers.

### Key insight

Branching adds work across calls. Sequential sibling execution does not add their depths.

### Simplification or limitation

Each shape performs only bounded bookkeeping. Real algorithms can do nonconstant local work,
allocate buffers, retain partial results, or short-circuit before all children execute.

## Interpretation

1. Every listed count prediction matched. At size eight, chain and repeat both reached depth
   nine, but executed nine and 511 calls respectively. Halve and split both reached depth
   four, but executed four and 15 calls.
2. Agreement with the independently derived formulas supports the counter implementation.
   The formulas, rather than a finite sample, justify the general growth claims.
3. No timing speedup, peak byte count, native-stack layout, or maximum safe recursion depth
   can be inferred from these counters.

## Threats to validity

- Instrumentation adds work but does not change which synthetic children are requested.
- Integer counters are treated as bounded words for analysis; all supplied sizes are small.
- The chain is capped at 128, split at 4096, and repeated decrement at 12 to bound resources.
- The runtime recursion limit is only read. The script does not test a crash threshold or alter
  the limit; a host configured with a very low limit can still reject a run.
- A cached version or parallel sibling execution would be a different experiment.

## Sources

- [Unit derivations](../../README.md#9-complexity-derivation): original node-count and depth arguments.
- [Python recursion-limit API](https://docs.python.org/3.14/library/sys.html#sys.getrecursionlimit):
  standard-library context; checked 2026-08-30.

Maintenance execution is not learner evidence. Rahul should record a prediction and explain a
fresh size independently before adding anything to REVIEW.md.
