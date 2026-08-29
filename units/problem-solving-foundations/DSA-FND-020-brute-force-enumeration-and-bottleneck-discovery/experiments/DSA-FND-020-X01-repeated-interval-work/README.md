# DSA-FND-020-X01 — Repeated interval work

| Field | Value |
|---|---|
| Owning unit | [DSA-FND-020](../../README.md) |
| Curriculum | [CURRICULUM.md](../../../../../CURRICULUM.md#dsa-fnd-020) |
| Question | When two exhaustive methods visit the same non-empty intervals, how much extra addition work comes from rebuilding each interval total instead of extending retained state? |
| Scope | Algorithm instrumentation |
| Runnable script | `experiment.py` |
| Source classification | Original deterministic experiment; no external dataset or copied benchmark |
| Status | Run / Interpreted |

## Why observation is necessary

The phrase “both methods have two visible loops” hides the evaluator inside one method. Instrumented execution exposes three quantities side by side: interval candidates, additions used to rebuild totals, and additions used to extend totals. Equal checksums provide a local consistency check while the counters make the bottleneck concrete.

## Hypothesis

> Both methods will visit `n(n+1)/2` interval boundaries and produce the same checksum. Rebuilding will perform `n(n+1)(n+2)/6` element additions, while extending will perform `n(n+1)/2`; therefore their counted-addition ratio will be `(n+2)/3` and will grow with `n`.

## Environment

~~~text
Date: 2026-08-29
Operating system: Linux 7.0.0-30-generic
Architecture: x86_64
Python version: 3.14.4
Implementation: CPython
Dependencies: Python standard library only
Input distribution: deterministic integers 1 through n
Trial count: one deterministic count per n; no timing trials
~~~

## Controls and measured variables

- Controlled: input values, interval boundary order, checksum definition, Python process, and the set of `n` values.
- Changed: the evaluator either rebuilds each interval total from zero or carries a running total for one fixed left boundary.
- Measured: interval visits, element additions used inside interval-total evaluation, checksum equality, and the ratio of counted additions.
- Deliberately excluded: checksum-update additions, loop-control work, allocation bytes, cache behavior, and elapsed time.

## Reproduction command

From the repository root:

~~~bash
python units/problem-solving-foundations/DSA-FND-020-brute-force-enumeration-and-bottleneck-discovery/experiments/DSA-FND-020-X01-repeated-interval-work/experiment.py
~~~

## Predicted output

The prediction was symbolic so it remains valid independently of machine speed:

~~~text
for n in 4, 8, 16, 32, 64:
    intervals      = n(n+1)/2
    rebuilt_adds   = n(n+1)(n+2)/6
    extended_adds  = n(n+1)/2
    ratio           = (n+2)/3
    checksums must be equal within each row
~~~

The ratio was predicted to increase from `2.00` at `n = 4` to `22.00` at `n = 64`.

## Observed output

~~~text
  n  intervals   rebuilt_adds  extended_adds    ratio     checksum
------------------------------------------------------------------
  4         10             20             10     2.00           50
  8         36            120             36     3.33          540
 16        136            816            136     6.00         6936
 32        528           5984            528    11.33        98736
 64       2080          45760           2080    22.00      1487200

Counts are abstract additions; no wall-clock threshold is inferred.
~~~

The observation matched the symbolic prediction for every recorded count and ratio.

## Visual interpretation

~~~text
same interval candidates
        |
        +--> rebuild evaluator:  [left..right] added again from zero
        |                         additions = 20, 120, 816, 5984, 45760
        |
        +--> extend evaluator:   previous [left..right-1] total retained
                                  additions = 10, 36, 136, 528, 2080

n = 64: 2,080 interval candidates in both methods
        45,760 versus 2,080 counted element additions
        equal checksum: 1,487,200
~~~

### How to read this visual

Read the shared candidate branch first: neither method removed an interval. Then compare the evaluator branches. The larger count arises because overlapping values are added again for each rebuilt interval. The checksum at the bottom checks that both branches aggregate the same interval totals on this input.

### Key insight

Candidate count alone is not the full complexity. Retaining exactly the previous interval total reduces evaluation from work proportional to interval length to one new element addition, even though the interval candidate space is unchanged.

### Simplification or limitation

The counters measure selected abstract additions, not every Python operation or byte. They demonstrate the intended work difference but do not establish elapsed-time ratios, cache behavior, or a universal input threshold.

## Interpretation

1. What the output directly shows: both implementations visited identical interval counts, returned equal checksums for the tested deterministic inputs, and recorded the predicted addition counts.
2. What can reasonably be inferred: repeated rebuilding is the named bottleneck in this baseline, and carrying a per-left running total removes that repeated element-addition work under the chosen model.
3. What cannot be inferred: equal checksums on five inputs do not prove general correctness; addition ratios do not equal wall-clock ratios; and this experiment does not prove that the retained-state method is globally optimal for every changed contract.

## Threats to validity

- Only positive consecutive integers were used. Different values can change checksum magnitude, though they do not change the deterministic loop counts.
- Python integer magnitude, interpreter overhead, branch prediction, caches, and memory allocation are outside the selected counter model.
- Equal aggregate checksums could theoretically hide compensating per-interval errors; separate correctness reasoning and tests remain necessary.
- If every interval total must be returned rather than reduced into one checksum, both methods still require output writes and materialized output proportional to `n(n+1)/2`.

## Sources

- Source classification: original repository experiment derived from the unit's original interval example.
- [Python 3.14 language reference: `for` statements](https://docs.python.org/3.14/reference/compound_stmts.html#the-for-statement) — consulted only for the language-level iteration construct; it does not supply the experiment's result or complexity conclusion.

The observed table was produced locally by `experiment.py` in the recorded environment; no external benchmark result was imported.
