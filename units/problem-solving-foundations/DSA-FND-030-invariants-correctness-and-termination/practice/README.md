# Practice — DSA-FND-030 Invariants, correctness, and termination

| Field | Value |
|---|---|
| Unit note | [DSA-FND-030](../README.md) |
| Curriculum | [CURRICULUM.md](../../../../CURRICULUM.md#dsa-fnd-030) |
| Problem bank | [PROBLEM_BANK.md](../../../../PROBLEM_BANK.md) |
| Evidence target | E+T+P+D+R+M |
| Attempt required before comparison | Yes |
| Runnable trace command | `uv run --group dev python practice/trace_lab.py` |
| Passing scaffold command | `uv run --group dev python -m pytest -q practice/test_trace_lab.py` |
| Learner implementation contract | Not applicable; this unit's evidence profile excludes I |
| Status | Not attempted |

## Learning questions

1. Can you state an invariant at one exact program boundary and test every clause during a trace?
2. Can you derive the postcondition from the invariant and the false guard rather than from
   intuition?
3. Can you distinguish a correctness defect from a safety defect and a termination defect?
4. Can you find a well-founded progress measure for an unfamiliar finite-state process?

## Cycle

```text
predict → trace → run → observe → explain → vary → recall
```

## File and test separation

- [trace_lab.py](trace_lab.py) is a complete deterministic trace scaffold. It exposes loop-head
  state, guard outcome, invariant status, and ranking values for a teaching scan.
- [test_trace_lab.py](test_trace_lab.py) checks only the supplied trace behavior, boundaries, and
  transition analysis.
- No `starter.py` or challenge test is created because `DSA-FND-030` requires explanation, trace,
  proof, debugging, recall, and mixed transfer—not implementation evidence.
- Written tasks remain unsolved. Preserve Rahul's prediction, proof, smallest counterexample, and
  hint history before recording any later comparison.

## Exercise index

| Exercise ID | Type | Difficulty | Objective | Files | Status |
|---|---|---:|---|---|---|
| `DSA-FND-030-P01` | Predict / Trace / Prove | 2 | Reconcile loop-head state with four proof obligations | `trace_lab.py`, `test_trace_lab.py` | Not attempted |
| `DSA-FND-030-P02` | Debug / Counterexample | 3 | Classify four defects by the first failed proof obligation | This file | Not attempted |
| `DSA-FND-030-P03` | Mixed transfer | 3 | Solve and defend an unseen ordered-event contract without a supplied pattern or target bound | This file | Not attempted |

## DSA-FND-030-P01 — Predict the proof-state trace

### Task

Without opening or running `trace_lab.py`, trace the supplied first-index contract for each input
below. At every loop head record `index`, the half-open processed prefix, whether the invariant is
true, the full guard result, the ranking value, and the action or exit conclusion. Then run the lab,
compare its deterministic trace with your prediction, and explain the first discrepancy rather than
silently replacing your work.

### Constraints and expected behavior

- Input cases, in order:
  - `values=[2, 5, 1, 7]`, `threshold=6`;
  - `values=[6]`, `threshold=6`;
  - `values=[1]`, `threshold=6`;
  - `values=[]`, `threshold=6`.
- Required observation or output: four hand traces plus the exact returned index or `None`, followed
  by the program output and a discrepancy note.
- State boundary: immediately before each guard evaluation, including the initial and exiting head.
- Performance target: deterministic state reasoning only; do not infer wall-clock performance from
  this small trace.

### Required edge cases

- Empty input must reach an exit head without reading `values[0]`.
- Equality with the threshold is valid and must not enter the loop body.
- A no-match singleton must perform one body transition and exit at `index == len(values)`.
- The ranking value may be zero only at an exhausted exit state.

### Before running

Record:

- exact precondition and postcondition;
- loop-head invariant with bounds and semantic prefix meaning;
- guard and its safe evaluation order;
- ranking measure and lower bound;
- initialization argument;
- one preservation step using old and new state names;
- both false-guard exit cases;
- time, auxiliary/output/stack space, and any trace-only costs.

### Acceptance criteria

- [ ] Every prediction is recorded before execution.
- [ ] The invariant uses `[0,index)` consistently at every loop head.
- [ ] Empty-prefix truth is explained rather than assumed.
- [ ] The false guard is split into exhausted and current-match exits.
- [ ] Strict ranking decrease is checked on every continuing transition.
- [ ] The production algorithm's cost is separated from prefix materialization in the trace.
- [ ] Every discrepancy names the earliest mistaken proof step.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## DSA-FND-030-P02 — Diagnose four plausible loops

### Task

Review the four fragments below for the same contract: return the first index whose integer value is
at least `threshold`, or `None` if no such index exists. For each fragment, do not begin by rewriting
the code. First give the smallest allowed counterexample, classify the earliest failed obligation
among contract, initialization, guard safety, preservation, progress, exit implication, soundness,
and completeness, and state the smallest conceptual repair. Write a corrected proof outline only
after all four diagnoses.

Fragment A:

```python
index = 0
while values[index] < threshold and index < len(values):
    index += 1
```

Fragment B:

```python
index = 0
while index < len(values) and values[index] < threshold:
    index += 2
```

Fragment C:

```python
index = 0
while index < len(values):
    if values[index] < 0:
        continue
    if values[index] >= threshold:
        break
    index += 1
```

Fragment D:

```python
index = 0
while index + 1 < len(values) and values[index] < threshold:
    index += 1
```

### Constraints and expected behavior

- Input contract: a finite reusable `list[int]`; any length `n >= 0`; fixed integer threshold; no
  mutation during the call.
- Output contract: the smallest valid index or `None` exactly when no valid index exists.
- Required observation or output: a four-row defect table, one minimal counterexample trace per row,
  and a corrected proof outline that covers both return cases.
- Performance target: the repaired reasoning must derive an honest best/worst time and separate
  auxiliary, output, and stack space. No target bound is supplied.

### Required edge cases

- Use empty input or the smallest no-match input to test guard safety.
- Use a two-position input when checking whether an update skips a valid state.
- Do not execute a fragment once your reasoning shows that a branch can repeat without progress.
- Include a case where only the last position is valid.

### Before proposing repairs

- Chosen loop boundary:
- Intended invariant:
- First broken obligation for A:
- First broken obligation for B:
- First broken obligation for C:
- First broken obligation for D:
- Candidate ranking measure:
- One reason a passing normal example would not expose the defect:

### Acceptance criteria

- [ ] Each counterexample is minimal or its extra state is justified.
- [ ] Safety, preservation, completeness, and termination failures are not conflated.
- [ ] Fragment C is analyzed symbolically without launching an unbounded run.
- [ ] Every branch returning to a guard is checked for strict progress.
- [ ] The last-position case is used to test the exit implication.
- [ ] The repair is described at the reasoning level before corrected code is considered.
- [ ] The final proof derives its postcondition from invariant plus false guard.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## DSA-FND-030-P03 — Audit the dispatch ledger

### Task

A warehouse receives a finite ordered list of signed stock changes. Starting stock is a
non-negative integer. Return the earliest event index after whose change the stock becomes
negative; return `None` if stock never becomes negative. Events cannot be reordered, the input list
must remain unchanged, and the stock value may later recover after first becoming negative. Derive
the simplest correct method, its state meaning, a full correctness and termination argument, and an
honest complexity analysis. No algorithm family, intended state representation, invariant, or
target complexity is supplied.

### Constraints and expected behavior

- Input contract: `starting_stock` is an integer with `starting_stock >= 0`; `changes` is a finite
  reusable `list[int]` of length `n`, where `0 <= n <= 200_000`; applying a change uses exact integer
  addition.
- Output contract: the smallest index `k` such that
  `starting_stock + changes[0] + ... + changes[k] < 0`, otherwise `None`.
- Mutation/order contract: preserve `changes` byte-for-byte and respect arrival order.
- Required observation or output: contract ledger, three adversarial traces, baseline, derived state
  claim, initialization/preservation/exit proof, termination measure, and complexity categories.
- Performance target: none is provided. Derive the bound of your proposal and explain whether the
  maximum constraints make it reasonable without inventing a universal seconds threshold.

### Required edge cases

- `starting_stock=0`, `changes=[]` returns `None`.
- `starting_stock=0`, `changes=[-1, 5]` returns `0`; later recovery cannot change “earliest.”
- `starting_stock=3`, `changes=[-3]` returns `None` because zero is not negative.
- Equal total sum does not imply equal earliest-failure behavior: compare two orders of the same
  changes.
- Very large positive and negative integers must use exact Python integer semantics.

### Before designing

- Inputs and explicit variables:
- Exact postcondition and quantifier:
- Simplest correct baseline:
- Dominant operation:
- Candidate state descriptions:
- Rejected alternatives and counterexamples:
- Chosen proof boundary:
- Safety obligation:
- Progress measure:
- Time and auxiliary/output/stack space:
- One changed contract that would invalidate the reasoning:

### Acceptance criteria

- [ ] The answer is derived without a pattern label or assumed target complexity.
- [ ] “Earliest” is defended; returning merely some failing index is rejected.
- [ ] State meaning accounts for exactly the processed events and current stock.
- [ ] Initialization handles the empty list.
- [ ] Every continuing transition preserves the stated meaning and makes strict progress.
- [ ] Exit reasoning covers both a found failure and full exhaustion.
- [ ] Original order and input immutability are preserved.
- [ ] `n`, dominant additions/comparisons, auxiliary space, output space, and stack space are explicit.
- [ ] A changed constraint is analyzed without silently reusing an invalid proof.

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
- Failed proof-obligation category:
- Hint level used:
- Actual commands and observed results:
- Remaining weakness:
- Next review date:

A later comparison may be added only after Rahul explicitly closes an exercise, and it must not
replace the preserved prediction, trace, proof, or counterexample.
