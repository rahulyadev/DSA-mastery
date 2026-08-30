# Practice — DSA-FND-040 Asymptotic notation and input-variable modeling

| Field | Value |
|---|---|
| Unit note | [DSA-FND-040](../README.md) |
| Curriculum | [CURRICULUM.md](../../../../CURRICULUM.md#dsa-fnd-040) |
| Problem bank | [PROBLEM_BANK.md](../../../../PROBLEM_BANK.md) |
| Evidence target | E+T+P+D+R+M |
| Attempt required before solution | Yes |
| Passing scaffold command | `uv run --group dev python -m pytest -q practice/test_work_counts.py` |
| Challenge validation command | Not applicable: no implementation challenge is required by this unit's evidence profile |
| Status | Not attempted |

## Learning questions

1. Which quantity does a counter measure, and which costs does it leave out?
2. Can your bound survive unequal dimensions, early exit, expensive primitives, and empty inputs?
3. Can you defend the statement without timing the program or recalling a label from its shape?

## Cycle

```text
predict → trace → implement an instrument if useful → run → observe
        → explain → optimize the reasoning → vary → recall
```

Write predictions before running anything. Keep the first attempt and append corrections with
their reasons; do not replace it with the final explanation. Ask for one hint only when you can
identify the remaining gap.

## File and test separation

- [micro_lab.py](micro_lab.py) contains worked rectangular, triangular, and doubling specimens.
  [test_work_counts.py](test_work_counts.py) tests only that teaching scaffold.
- This unit requires analysis and proof, not a learner implementation. There is no `starter.py`,
  no incomplete challenge test suite, and no claimed challenge-test success.
- Code below is input to an analysis task. Its output is not the answer to the requested cost
  audit. No completed audit, bound table, proof, or mixed-task implementation is supplied.
- Keep later attempt files here and link them from [REVIEW.md](../REVIEW.md). Add a comparison
  answer only after Rahul explicitly closes that exercise, preserving the original attempt.

After setting up the repository with `uv sync --group dev`, run these commands from this unit's
directory:

```bash
uv run --group dev python practice/micro_lab.py
uv run --group dev python -m pytest -q practice/test_work_counts.py
uv run --group dev python experiments/DSA-FND-040-X01-counts-and-clock-time/experiment.py
uv run --group dev python -m pytest -q experiments/DSA-FND-040-X01-counts-and-clock-time/test_growth_experiment.py
```

These commands do not validate a learner's reasoning. Do not run large quadratic specimens simply
to confirm an asymptotic guess; use small traces and a general argument.

## Exercise index

| Exercise ID | Type | Difficulty | Objective | Files/evidence | Status |
|---|---|---:|---|---|---|
| `DSA-FND-040-P01` | Trace / Prove | 2 | Account for coordinates omitted by a stepped range | Hand table, then an optional local counter | Not attempted |
| `DSA-FND-040-P02` | Model / Compare | 3 | Preserve two dimensions under a dependent cap | Sum, input families, and defended bounds | Not attempted |
| `DSA-FND-040-P03` | Explain / Debug | 2 | Qualify bounds with witnesses or counterexamples | Claim table and spoken defense | Not attempted |
| `DSA-FND-040-P04` | Audit / Vary | 3 | Account for hidden Python work and lifetimes | Operation ledger and space categories | Not attempted |
| `DSA-FND-040-P05` | Compare / Prove | 3 | Separate case selection from bound notation | Count functions and distribution model | Not attempted |
| `DSA-FND-040-P06` | Transfer | 3 | Reanalyze a program after changing the size model | State trace, magnitude/bit analysis | Not attempted |
| `DSA-FND-040-P07` | Mixed / Mock | 3 | Solve the supplied contract independently | Preserved attempt and interview explanation | Not attempted |

<a id="dsa-fnd-040-p01"></a>

## DSA-FND-040-P01 — Account for skipped coordinates

### Task

Analyze this specimen without running it first. Write every visited `(i, j)` for `n = 5`, the
visits in each outer row, and the cumulative count after that row. Then derive a count expression
for general `n`, a tight growth bound, and a boundary-specific counting invariant.

```python
count = 0
for i in range(n):
    for j in range(0, i, 2):
        count += 1
```

### Constraints and expected behavior

- Input: integer `0 <= n <= 10**6`; only execute small cases, at most `n = 32`.
- Output: predicted table, exact count expression, bound argument, and storage analysis.
- Performance target: accurately characterize this fixed program, including outer overhead;
  changing it to a different algorithm does not answer the question.
- Assume fixed-cost integer control operations, then state what that assumption excludes.

### Required edge cases

- `n = 0` and `n = 1`; distinguish no outer iterations from an empty inner row.
- `n = 2`, `n = 3`, and `n = 6`; check parity boundaries rather than only one odd size.
- A proposed answer that divides every inner length by two using ordinary real division.

### Acceptance criteria

- [ ] Predictions precede any execution and include all allowed coordinates exactly once.
- [ ] The invariant names the exact row boundary and matches every transition.
- [ ] Exact count and asymptotic class are distinct statements.
- [ ] A lower-bound argument accompanies the upper bound.
- [ ] Time, auxiliary/output/stack space, and excluded Python costs are explicit.

### Progressive hints

1. Locked until Rahul requests it.
2. Locked until Rahul has attempted the first hint.
3. Locked until Rahul has described the remaining gap.

<a id="dsa-fnd-040-p02"></a>

## DSA-FND-040-P02 — Model capped dependent work

### Task

A colleague calls the following program “always `Theta(n*m)` because there are two loops.” Audit
that claim. Produce row counts and a general total, identify the size relationships under which a
bound is tight, and use an unbounded family to repair any overstatement. Do not assume `m = n`.

```python
events = 0
for i in range(n):
    for j in range(min(i, m)):
        events += 1
```

### Constraints and expected behavior

- Inputs: independently chosen integers `0 <= n, m <= 10**6`; execute only tiny specimens.
- Output: two predicted tables for `(n, m) = (5, 2)` and `(2, 7)`, followed by a general analysis.
- Performance target: derive a justified bound for the fixed program in each relevant regime,
  retaining constant/outer overhead for empty cases. No replacement algorithm is requested.
- Record where `min` is evaluated and whether it changes the asymptotic cost under this model.

### Required edge cases

- `(0, 7)`, `(5, 0)`, and `(1, 100)`.
- Keep `m = 1` while increasing `n`; separately keep `n` small while increasing `m`.
- Let both inputs grow with substantially different magnitudes.

### Acceptance criteria

- [ ] Neither dimension silently becomes the other.
- [ ] Each simplification states the relationship that makes it valid.
- [ ] A claimed tight bound has feasible inputs supporting its lower bound.
- [ ] The empty inner-loop case includes work outside that loop.
- [ ] Auxiliary, output, and recursion-stack space are stated separately.

### Progressive hints

1. Locked until Rahul requests it.
2. Locked until Rahul has attempted the first hint.
3. Locked until Rahul has described the remaining gap.

<a id="dsa-fnd-040-p03"></a>

## DSA-FND-040-P03 — Qualify each bound claim

### Task

For positive integer `n`, let `f(n) = 5*n + 7` and `g(n) = n*n + 2*n`. Decide each mathematical
claim below. For a true claim give constants and a threshold; for a false claim explain why every
possible fixed witness fails. Separately assess the search statement, naming its hidden input-case
assumption rather than merely marking it wrong.

| Claim to assess | Decision and justification |
|---|---|
| `f in O(n)` | Not attempted |
| `f in Theta(n)` | Not attempted |
| `f in Omega(n*n)` | Not attempted |
| `g in O(n*n*n)` | Not attempted |
| `g in Theta(n*n)` | Not attempted |
| “A search has worst-case Omega(n), so every input requires at least linear time.” | Not attempted |

### Constraints and expected behavior

- Inputs are mathematical functions and the stated claim; the asymptotic domain is unbounded.
- Output: completed claim table, witness inequalities, and a two-minute verbal explanation.
- Performance target: not a runtime optimization task. The result must use valid quantifiers
  and constants independent of `n`, rather than a finite table of values.
- Use algorithmic capital `Omega`; lowercase omega is outside this exercise.

### Required edge cases

- Check whether a witness works from `n = 1` or needs a larger threshold.
- Distinguish a loose but true upper bound from a false tight bound.
- Test a proposed witness `c = n`: does it meet the definition?
- Consider a search that exits immediately on some valid inputs.

### Acceptance criteria

- [ ] Every constant and threshold is explicit and independent of the input.
- [ ] A finite failing example is not the entire argument against an eventual bound.
- [ ] Best/worst/average cases are not renamed `Omega`/`O`/`Theta`.
- [ ] The explanation distinguishes a bound on one implementation from a problem lower bound.

### Progressive hints

1. Locked until Rahul requests it.
2. Locked until Rahul has attempted the first hint.
3. Locked until Rahul has described the remaining gap.

<a id="dsa-fnd-040-p04"></a>

## DSA-FND-040-P04 — Audit a report builder

### Task

The following correct report builder returns the sum of the most recent at most `width` input
values at each position. Audit its time and peak space; do not implement a replacement. Account
for list creation, copying, arithmetic, and result retention. Explain what changes if the consumer
requires all intermediate slices to be retained as part of the report as well.

```python
def report(values: list[int], width: int) -> list[int]:
    n = len(values)
    totals = [0] * n
    for i in range(n):
        totals[i] = sum(values[max(0, i - width + 1) : i + 1])
    return totals
```

### Constraints and expected behavior

- Input: unchanged built-in list, `0 <= n <= 10**6`, values between `-10**6` and `10**6`, and
  `1 <= width <= 10**6`. Treat these bounded sums as word-cost arithmetic for the first analysis.
- Behavior example: `values = [4, -1, 3]`, `width = 2` returns `[4, 3, 2]`.
- Required output: an operation ledger and derived bounds in explicitly named variables,
  plus the changed-contract analysis. There is no optimization target for a replacement.
- Distinguish list reference copying from copying the integer objects themselves.

### Required edge cases

- Empty input, one value, width one, and width larger than the entire input.
- Negative values and zeros; do they affect the number of additions?
- A fresh slice discarded each iteration versus every slice retained.
- State why width zero is outside this input contract.

### Acceptance criteria

- [ ] The first few slices and their lengths are predicted before executing the specimen.
- [ ] Counts cover the executed slice lengths rather than blindly substituting `width` everywhere.
- [ ] Input storage, peak auxiliary, output, and recursion-stack space are separate.
- [ ] Cumulative allocation is not confused with peak live memory.
- [ ] The analysis names what would change for unbounded integers or a custom sequence type.

### Progressive hints

1. Locked until Rahul requests it.
2. Locked until Rahul has attempted the first hint.
3. Locked until Rahul has described the remaining gap.

<a id="dsa-fnd-040-p05"></a>

## DSA-FND-040-P05 — Select the input case

### Task

Analyze a first-match search using the inputs and distribution below. Derive its exact comparison
count on each input family, best- and worst-case functions over all allowed lists, and expected
comparison count under the stated distribution. Decide whether the expected result could be
generalized to arbitrary inputs. State a bound on total runtime as a separate step.

```python
def contains_target(values: list[int], target: int) -> bool:
    for value in values:
        if value == target:
            return True
    return False
```

### Constraints and expected behavior

- Base contract: a finite unchanged list of bounded integers and one target; equality costs one
  unit and all list lengths from zero upward are permitted for best/worst-case reasoning.
- Distribution for this exercise only: for each `n >= 2`, search for `1` in `[1] + [0]*(n-1)`
  with probability `1 - 1/n`, and in `[0]*n` with probability `1/n`.
- Output: count functions, a weighted expectation with its stated domain, and a spoken defense.
- Performance target: accurately characterize the given search; do not substitute another data
  structure. Input construction is excluded from the measured search but must be named as excluded.

### Required edge cases

- Empty input, match at the first position, match at the last position, and no match.
- The separate best/worst-case domain includes lists absent from the two-family distribution.
- Change the no-match probability to a fixed positive constant and reconsider the expectation.
- Replace each value with an equality-comparable record whose comparison costs at most `c`.

### Acceptance criteria

- [ ] Search result correctness and comparison counts are both traced.
- [ ] The expectation uses the supplied probabilities, not an unstated uniform-position model.
- [ ] Statements distinguish comparisons, runtime, and the resource's input-case function.
- [ ] A tight claim with expensive records has a feasible input family, not just multiplied upper bounds.
- [ ] Working space, Boolean output, and recursion-stack space are explicit.

### Progressive hints

1. Locked until Rahul requests it.
2. Locked until Rahul has attempted the first hint.
3. Locked until Rahul has described the remaining gap.

<a id="dsa-fnd-040-p06"></a>

## DSA-FND-040-P06 — Change the input representation

### Task

Trace the following program for `N = 17`, recording `x` before and after each transition. Analyze
it first by the numeric value `N`, then by the bit length of a positive input. Give the discrete
stopping argument rather than a floating-point estimate. Finally reanalyze it under the explicitly
different bit-cost model below and explain why the resource statements change.

```python
x = N
steps = 0
while x > 0:
    x //= 4
    steps += 1
```

### Constraints and expected behavior

- Input: one non-negative integer `N < 2**4096`; for asymptotic reasoning generalize to unbounded
  finite positive integers. Analyze `N = 0` separately.
- Output: predicted transitions, exact iteration expression or discrete characterization,
  bounds with named variables, and auxiliary/output/stack storage in words and bits.
- Model A: scalar control and arithmetic operations cost one unit.
- Model B: division of a `b_current`-bit positive integer by four costs `Theta(b_current)`;
  count that work as the size shrinks. This is an exercise model, not a universal language guarantee.
- Performance target: characterize this program under both models; no new implementation is required.

### Required edge cases

- `N = 0`, `1`, `3`, `4`, `16`, and `17`.
- The distinction between `N.bit_length()` for zero and the one-character encoding `"0"`.
- A mistaken stopping condition that waits for a non-integer fractional value.
- The storage needed for `x` compared with the much smaller final transition count.

### Acceptance criteria

- [ ] The state update follows integer floor division and reaches a legal stopping state.
- [ ] Each logarithm names its argument, and value size is not equated with encoded size.
- [ ] Model B sums the changing primitive costs rather than assuming every step costs one.
- [ ] The bit analysis includes the lifetime of newly created integer values.
- [ ] The explanation names which assumptions would need source/runtime verification in production.

### Progressive hints

1. Locked until Rahul requests it.
2. Locked until Rahul has attempted the first hint.
3. Locked until Rahul has described the remaining gap.

<a id="dsa-fnd-040-p07"></a>

## DSA-FND-040-P07 — Batch acceptance

### Task

A service receives a finite list of batches. Each batch is a finite list of signed integer
identifiers. Given a required identifier, return whether every batch contains that identifier.
An empty batch makes the result false; an empty outer list makes it true. Develop and defend an
approach from the contract. Preserve the first proposal and its dry-run before receiving feedback.

### Constraints and expected behavior

- Input: at most `10**5` batches, at most `2*10**5` identifiers across all batches, identifier values
  between `-10**9` and `10**9`. Duplicates are allowed and neither input may be mutated.
- Output: one Boolean. `[[2, 7], [7], [7, 7]]` with required `7` returns true; `[[7], []]` returns
  false; `[]` returns true.
- Performance target, intended structure, and pattern label are deliberately withheld for this
  mixed/mock task. Derive your own variables and defend resource use against the constraints.
- If unseen, use twenty minutes including clarification, an approach, a trace, and a spoken
  defense. If already studied, request a fresh contract instead of treating recall as unseen work.

### Required edge cases

- No batches, a single empty batch, a missing identifier, and repeated identifiers.
- One very large batch and many empty batches within the stated size limits.
- Required identifier equal to zero or a negative value.

### Acceptance criteria

- [ ] The response starts from the contract without a supplied pattern, invariant, or complexity.
- [ ] Chosen variables and their constraints are explicit.
- [ ] Correctness, termination, time, and auxiliary/output/stack space are defended independently.
- [ ] The original approach and any hints remain visible in the attempt record.
- [ ] No input mutation occurs, and all boundary contracts are addressed.

### Progressive hints

1. Locked until Rahul requests it.
2. Locked until Rahul has attempted the first hint.
3. Locked until Rahul has described the remaining gap.

## Review record

- Date and exercise: Not attempted.
- Original prediction or approach: Not recorded.
- What is correct: Not evaluated.
- First missing reasoning step: Not evaluated.
- Smallest counterexample or unbounded family: Not recorded.
- Hint level used: None; all hints remain locked.
- Actual commands and observations: No learner run recorded.
- Remaining weakness and next review: Set after evidence, not after file generation.
