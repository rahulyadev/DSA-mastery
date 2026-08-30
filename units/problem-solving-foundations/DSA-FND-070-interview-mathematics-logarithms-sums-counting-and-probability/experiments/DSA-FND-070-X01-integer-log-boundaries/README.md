# DSA-FND-070-X01 — Integer logarithm boundaries

| Field | Value |
|---|---|
| Owning unit | [DSA-FND-070](../../README.md) |
| Curriculum | [CURRICULUM.md](../../../../../CURRICULUM.md#dsa-fnd-070) |
| Question | Can rounded floating logarithms reliably determine exact floor and ceiling exponents next to an integer power of two? |
| Scope | Mathematical identity, standard-library contract, and platform-dependent numerical observation |
| Runnable script | [integer_boundaries.py](integer_boundaries.py) |
| Checks | [test_integer_boundaries.py](test_integer_boundaries.py) |
| Status | Interpreted |

## Why observation is necessary

On small integers, an approximate logarithm often gives the expected floor or ceiling, making
the shortcut appear exact. Observing neighboring large integers tests that assumption on the
actual interpreter and math library. A single failure disproves universal reliability; a small
sample with no failures cannot prove it. This is a numerical experiment, not a speed benchmark.

## Hypothesis

For positive `n`, integer bit lengths will satisfy the defining floor and ceiling inequalities.
Near sufficiently large powers of two, a floating logarithm may round a neighbor to the exponent
of the power itself. Small cases should distinguish the neighbors. We predict exact columns
before execution, but do not assume which float rows must fail on every platform.

## Environment

- Date: 2026-08-30 (maintainer initialization run).
- Python, implementation, operating system, architecture, float radix, and mantissa digits:
  printed by the script, without hostname or other private machine identifiers.
- Dependencies: Python standard library; pytest only for the supplied deterministic checks.
- Input distribution: fixed values `2^k-1`, `2^k`, `2^k+1` for `k` in `3, 53, 100`.
- Workload: nine observations; no timing, warm-up, or statistical-trial claims.

## Controls and measured variables

- Controlled: the same exact integer is passed to both calculations; positive domain only.
- Changed: exponent and offset from a power of two.
- Measured: the floating `log2`, its floor and ceiling, and the exact integer boundaries.
- Guard: CLI exponents must lie in `1..4096`, so an accidental huge allocation is rejected.

## Reproduction command

From this experiment directory:

```bash
uv run --group dev python integer_boundaries.py
uv run --group dev python -m pytest -q test_integer_boundaries.py
```

To choose other bounded cases, use `--exponents 1 10 54`. In a restricted sandbox, prefix a
command with `env UV_CACHE_DIR=/tmp/dsa-fnd-070-uv-cache` if the default cache is read-only.

## Predicted output

For every tested exponent `k >= 2`, the exact columns must follow:

```text
input          exact floor     exact ceiling
2^k - 1           k-1               k
2^k               k                k
2^k + 1           k                k+1
```

At `k=1`, the first row is `n=1` and its exact ceiling is **zero**, so that row is the
exception to the displayed ceiling pattern. The default exponents are all greater than one.
Float columns are predictions to test, not stipulated output: one or both large neighbors may
share the displayed exponent, producing a wrong integer boundary after floor or ceiling.

## Observed output

Executed on 2026-08-30 during initialization, using the command above. This is a maintainer
observation; Rahul has not yet completed the predict/run/interpret cycle.

```text
Python: CPython 3.14.7
Platform: Linux x86_64
float radix=2 mant_dig=53
n log2(n) floor_float floor_exact ceil_float ceil_exact mismatch
2^3-1 2.80735492206 2 2 3 3 False
2^3+0 3 3 3 3 3 False
2^3+1 3.16992500144 3 3 4 4 False
2^53-1 53 53 52 53 53 True
2^53+0 53 53 53 53 53 False
2^53+1 53 53 53 53 54 True
2^100-1 100 100 99 100 100 True
2^100+0 100 100 100 100 100 False
2^100+1 100 100 100 100 101 True
A displayed logarithm is rounded; exact inequalities decide integer boundaries.
```

Four neighbor rows disagree with the exact integer boundary in this run: the floor below
`2^53` and `2^100`, and the ceiling above each power. Exact powers and the small neighbors
agree. This supplies concrete counterexamples to a universal float-boundary shortcut, while
leaving platform-specific rounding behavior explicitly qualified.

## Visual interpretation

```text
2^k - 1       2^k       2^k + 1       exact integers are different
   |            |            |
   +------ approximate log2 values can round to the same float ------+
```

### How to read this visual

The top row shows neighboring integer inputs; the lower line warns of information loss in the
reported logarithm. It does not assert that all three results always coincide.

### Key insight

The needed answer is an integer inequality. More displayed decimal places cannot recover a
distinction that the floating result has already lost.

### Simplification or limitation

The sketch is conceptual, not a drawing of the spacing of floating-point numbers. The script
prints only 12 significant digits, but computes floor/ceiling from the original float, so display
rounding alone does not determine the mismatch flag.

## Interpretation

The exact calculation uses the integer bit-length contract. For floor `f`, verify
`2^f <= n < 2^(f+1)`. For ceiling `c`, verify `n <= 2^c` and, if `c > 0`, `2^(c-1) < n`.
`n=1` gives both zero. These inequalities are the correctness argument; agreeing with a rounded
float is not. The supplied tests use integer inequalities and do not assert platform-specific
float failures.

For `r` observed inputs of at most `B` bits, the program retains `O(r)` records plus arithmetic
workspace and constructs `O(B)`-bit input values. The exact decrement/bit-length operations
and logarithm have implementation-dependent costs; no constant-time or speedup claim follows
from the short source code. The default workload is fixed and deliberately tiny.

## Threats to validity

- Numerical-library and Python-version differences can change the last bits of logarithms.
- Nine inputs cannot characterize every magnitude, base, or floating-point operation.
- The experiment addresses exact integer thresholds, not the usefulness of approximate logs
  in numerical calculations.
- An initialization run verifies the artifact; Rahul still needs a prior prediction and a
  personal interpretation to create learning evidence.

## Sources

Read on 2026-08-30: the Python [`int.bit_length` contract](https://docs.python.org/3.14/library/stdtypes.html#int.bit_length)
and [`math.log2` documentation](https://docs.python.org/3.14/library/math.html#math.log2).
Integer bounds are mathematical identities; recorded float differences are runtime observations.
