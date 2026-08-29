# Practice — DSA-FND-020 Brute-force enumeration and bottleneck discovery

| Field | Value |
|---|---|
| Unit note | [DSA-FND-020](../README.md) |
| Curriculum | [CURRICULUM.md](../../../../CURRICULUM.md#dsa-fnd-020) |
| Problem bank | [PROBLEM_BANK.md](../../../../PROBLEM_BANK.md) |
| Evidence target | E+T+I+P+D+R+M |
| Attempt required before comparison | Yes |
| Passing scaffold command | `uv run --group dev python -m pytest -q practice/test_examples.py` |
| Challenge validation command | `uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py` |
| Status | Not attempted |

## Learning questions

1. Can you turn a legality predicate such as `i < j < k` into loop bounds with complete coverage and no duplicate candidates?
2. Can you distinguish candidate count from the work hidden inside one evaluation?
3. Can you name the exact repeated operation an optimization must remove without guessing a pattern first?

## Cycle

~~~text
predict → trace → implement → run → observe → explain → optimize → vary → recall
~~~

## File and test separation

- [micro_lab.py](micro_lab.py) and [test_examples.py](test_examples.py) are complete scaffold evidence. They reveal pair-space mechanics without implementing the learner challenge.
- [starter.py](starter.py) remains intentionally incomplete. Preserve the first implementation attempt and the reasoning written before it.
- [test_challenge.py](test_challenge.py) defines the triple-enumeration contract. During initialization it is collected, not run as a passing check.
- The [repeated-interval-work experiment](../experiments/DSA-FND-020-X01-repeated-interval-work/README.md) is a completed teaching observation, not an answer to the protected challenge.
- Do not create a comparison implementation until Rahul closes the challenge after a meaningful attempt.

## Exercise index

| Exercise ID | Type | Difficulty | Objective | Files | Status |
|---|---|---:|---|---|---|
| `DSA-FND-020-P01` | Predict / Trace / Debug | 2 | Audit legal unordered-pair coverage, matches, and wasted ordered-grid states | `micro_lab.py`, `test_examples.py` | Not attempted |
| `DSA-FND-020-P02` | Implement / Prove | 2 | Enumerate every matching index triple exactly once and report the exact candidate count | `starter.py`, `test_challenge.py` | Not attempted |
| `DSA-FND-020-P03` | Predict / Experiment / Explain | 3 | Separate interval candidate count from repeated element-addition work | experiment files | Not attempted |

## DSA-FND-020-P01 — Audit the unordered pair space

### Task

Before opening `micro_lab.py`, draw the full `4 x 4` ordered index grid for `values = [4, 1, 7, 4]`. Classify every cell as a self-pair, reverse duplicate, legal non-match, or legal match for target `8`. Then predict the exact row order emitted by the lab, the final matches, and all three candidate counts. Run the lab, reconcile each difference, and explain the first rule that any incorrect prediction violated.

### Constraints and expected behavior

- Input or initial state: the fixed four-element list `[4, 1, 7, 4]`, target `8`, and positional identity even when two values are equal.
- Required observation or output: a sixteen-cell classification, a six-row legal trace in canonical order, matches `(0, 3)` and `(1, 2)`, and counts for ordered-with-self, ordered-distinct, and unordered-distinct candidate spaces.
- Performance target: the legal trace must perform exactly `n(n-1)/2` predicate checks and use constant candidate state beyond the returned trace rows.

### Required edge cases

- With `n = 0` and `n = 1`, the unordered pair generator emits no candidates and does not form a negative count.
- With `[4, 4]` and target `8`, equal values at two distinct positions form one legal match.
- With `[4]` and target `8`, the lone position cannot be paired with itself.
- With no matching pair, every legal candidate must still be checked before an all-matches result is complete.

### Before running

Record the candidate object, legality rule, loop-order invariant, exact count derivation, expected trace, final output, time, auxiliary space, output space, recursion stack, and Python materialization costs.

### Acceptance criteria

- [ ] The grid is classified before execution.
- [ ] Self-pairs and reverse duplicates are distinguished rather than grouped as “wrong.”
- [ ] Every legal pair appears exactly once in the predicted trace.
- [ ] Equal values are not confused with equal positions.
- [ ] The exact candidate counts are derived from rules or row lengths.
- [ ] The first prediction discrepancy is tied to a specific invariant or boundary.
- [ ] Complexity separates streamed candidate state from stored trace output.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## DSA-FND-020-P02 — Enumerate target triples

### Task

Implement `enumerate_target_triples(values, target)` in `starter.py`. Return every index triple whose three distinct positions sum to the target, together with the total number of legal candidates examined. The result order must be deterministic and defined by increasing index triples. Write the legality predicate and coverage invariant before coding; do not import a ready-made combination generator for this first-principles exercise.

### Constraints and expected behavior

- Input contract: `values` is a finite list of integers with `0 <= len(values) <= 60`; `target` is an integer; input order and contents must remain unchanged.
- Output contract: return `(matches, checks)`, where `matches` is a list of every tuple `(i, j, k)` satisfying `0 <= i < j < k < n` and `values[i] + values[j] + values[k] == target`, in lexicographic index order; `checks` is the number of legal triples evaluated even when matches exist.
- Performance target: exactly `n(n-1)(n-2)/6` candidate evaluations for `n >= 3`, zero for smaller inputs, constant auxiliary state excluding the `Theta(r)` returned matches, and no recursion stack.

### Required edge cases

- `[]`, `[5]`, and `[5, -5]` produce `([], 0)` without invalid indexing.
- `[1, 2, 3, 4]` with target `6` returns only `(0, 1, 2)` but reports four checks.
- `[0, 0, 0, 0]` with target `0` returns all four index triples; equal values must not collapse distinct positional candidates.
- An input with no matching triple still reports every legal candidate check.
- The function must leave the input list byte-for-byte equivalent in value and order.

### Before coding

- Exact candidate object and legality rule:
- Brute-force loop bounds:
- Coverage and no-duplicate invariant:
- Exact candidate-count derivation:
- Dominant operation:
- Planned time, auxiliary space, output space, and recursion stack:
- One dry-run across an outer-loop boundary:
- One tempting but incorrect generator and its smallest counterexample:

### Acceptance criteria

- [ ] The original attempt and pre-code reasoning are preserved.
- [ ] Passing scaffold tests remain green.
- [ ] Challenge tests collect before implementation.
- [ ] After a genuine attempt, the learner implementation satisfies the challenge contract.
- [ ] Every emitted triple has distinct increasing indices and the required sum.
- [ ] Every legal triple is checked exactly once, including after an early match.
- [ ] Correctness covers soundness, completeness, no duplication, progress, and termination.
- [ ] Complexity names `n`, candidate checks, auxiliary/output/stack space, and relevant Python costs.
- [ ] A changed contract that returns only one witness is analyzed with separate best- and worst-case costs.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## DSA-FND-020-P03 — Explain repeated interval work

### Task

Read only the question and hypothesis in the experiment README, not its script or observed table. For each `n` in `4, 8, 16, 32, 64`, predict the number of non-empty intervals, element additions performed when every interval total is rebuilt from zero, and element additions performed when a running total is extended for each fixed left boundary. Then run the experiment and explain precisely which work changed even though both methods enumerated the same interval boundaries and produced the same checksum.

### Constraints and expected behavior

- Input or initial state: deterministic lists containing the integers `1` through `n` for `n` in `4, 8, 16, 32, 64`.
- Required observation or output: a prediction table, actual deterministic table, discrepancy log, and a bottleneck statement naming candidate count and evaluator work separately.
- Performance target: derive symbolic counts before interpreting growth; do not convert these addition counts into a universal elapsed-time promise.

### Required edge cases

- For `n = 0`, both methods would produce zero intervals, zero additions, and checksum zero.
- For `n = 1`, both methods perform one addition, so the optimization has no visible advantage yet.
- Equal checksums are required but do not by themselves prove that either operation count was recorded correctly.
- If every interval total must be materialized, both methods still owe output space proportional to the number of intervals.

### Before running

Record formulas, all five predicted rows, the expected ratio trend, what each counter measures, what it excludes, and one claim that the experiment cannot support.

### Acceptance criteria

- [ ] Predictions are recorded before the script is inspected or executed.
- [ ] Interval count is not confused with element-addition count.
- [ ] Both symbolic totals are derived rather than guessed from measured seconds.
- [ ] Equal checksums are used only as a consistency check, not a general correctness proof.
- [ ] The explanation names repeated interval aggregation as the removed bottleneck.
- [ ] Auxiliary space, required output space, and Python slicing differences are addressed separately.
- [ ] The limitation of deterministic abstract counts is stated.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## Review record

- What is correct:
- First missing reasoning step:
- Smallest counterexample:
- Hint level used:
- Actual commands and observed results:
- Remaining weakness:
- Next review date:

A later comparison may be added only after Rahul explicitly closes an exercise, and it must not replace the preserved attempt.
