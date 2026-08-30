# Practice — DSA-FND-070 Interview mathematics: logarithms, sums, counting, and probability

| Field | Value |
|---|---|
| Unit note | [DSA-FND-070](../README.md) |
| Curriculum | [CURRICULUM.md](../../../../CURRICULUM.md#dsa-fnd-070) |
| Problem bank | [PROBLEM_BANK.md](../../../../PROBLEM_BANK.md) |
| Evidence target | E+T+P+R+M |
| Attempt required before solution | Yes |
| Passing scaffold command | `uv run --group dev python -m pytest -q practice/test_math_traces.py experiments` from the unit directory |
| Challenge validation command | Not applicable: this unit has no required implementation evidence or challenge test file |
| Status | Not attempted |

## Learning questions

1. Which endpoint, counted object, or probability assumption determines the expression?
2. How can a small trace challenge a claim without proving it for every input?
3. What changes when the answer must be materialized rather than counted?

## Cycle

```text
predict -> trace -> implement a small check if useful -> run -> observe
        -> explain -> optimize the reasoning -> vary -> recall
```

Record predictions before opening the micro-lab or experiment output. Preserve each original
attempt, even if later corrected. A meaningful attempt includes an explicit contract, a tiny
trace, a proposed argument, and the first uncertain step; a final number alone is insufficient.

## File and test separation

- [micro_lab.py](micro_lab.py) contains complete teaching examples from the unit note, not
  implementations of the tasks below. Predict those examples before running the file.
- [test_math_traces.py](test_math_traces.py) checks the provided teaching state and arithmetic.
  Experiment tests check the demonstration code. Passing them does not complete the exercises.
- The evidence profile has no `I`, so no artificial `starter.py` or failing challenge suite is
  added. Optional learner code belongs with its original attempt, not in a supplied answer file.
- These tasks begin unsolved. No comparison solution is supplied. Ask for at most one new hint
  after an attempt, and record the hint and resulting change in reasoning.
- For a mixed or timed attempt, open only its packet section. Read the neighboring teaching
  sections and postmortem comparisons after the attempt closes.

## Exercise index

| Exercise ID | Type | Difficulty | Objective | Status |
|---|---|---:|---|---|
| DSA-FND-070-P01 | Trace / Boundary audit | 2 | Defend two stopping contracts | Not attempted |
| DSA-FND-070-P02 | Work-count derivation | 3 | Explain three concrete schedules | Not attempted |
| DSA-FND-070-P03 | Counting / Proof | 3 | Count role assignments without duplicate outputs | Not attempted |
| DSA-FND-070-P04 | Probability / Compare | 3 | State and change a sampling model | Not attempted |
| DSA-FND-070-P05 | Representation analysis | 3 | Account for the required output | Not attempted |
| DSA-FND-070-P06 | Mixed | 3 | Packet A | Not attempted |
| DSA-FND-070-P07 | Timed interview | 3 | Packet B | Not attempted |

## DSA-FND-070-P01 — Stopping contracts in base three

### Task

For each input `n` in `1, 2, 8, 9, 10, 26, 27, 28`, predict two full traces. Process A starts
with `x=n` and repeatedly performs `x //= 3` while `x >= 3`. Process B starts with `capacity=1`
and repeatedly performs `capacity *= 3` while `capacity < n`. Report every state, the number
of updates, and the exact final inequality in terms of the initial `n`. Then analyze the proposed
change to Process A's guard, `x > 1`, and find its first counterexample among the inputs.

### Constraints and expected behavior

- Inputs are positive integers, generally `1 <= n <= 10^100`; zero is outside this contract.
- Output: two state tables per supplied input, followed by a general argument for each count.
- Performance target: derive counts symbolically or with logarithmically many updates, not by
  listing every integer up to `n`. Distinguish the output trace from scalar counter storage.
- Do not use a floating logarithm as the justification for an exact boundary.

### Required edge cases

- No update, just below/exactly at/just above a power, and the input two.
- Explain what the changed guard can do when a final positive value is smaller than three.

### Before running

Write the predicted initial and terminal states, invariant, number of arrows, and the first state
where the proposed guard disagrees with the original contract. A self-written checker is optional.

### Acceptance criteria

- [ ] Predictions precede any code output.
- [ ] Each count is justified by an inequality, including its strict and non-strict endpoints.
- [ ] The original guard and changed guard are not treated as the same process.
- [ ] Time, auxiliary/output/stack space, and growing integer costs are stated.

### Progressive hints

Hint 1 is locked until requested. Hint 2 requires another attempt; hint 3 requires Rahul to
identify the remaining gap. No hints have been used.

## DSA-FND-070-P02 — Three work schedules

### Task

`visit()` represents one constant-cost action and has no effect on the loop variables. For each
schedule below, make a row-by-row table for `n=5`, report the exact number of visits, and derive
a tight asymptotic bound for general positive `n`. A teammate reports “all three have a doubling
or nested loop, so their costs are the same.” Assess this claim with a proof, not a timing result.

```text
A: for i = 1..n:
       j = 1
       while j <= i:
           visit()
           j *= 2

B: width = 1
   while width <= n:
       perform width visits
       width *= 2

C: for step = 1..n:
       position = step
       while position <= n:
           visit()
           position += step
```

### Constraints and expected behavior

- `1 <= n <= 10^6`; `..` includes both endpoints and all updates use exact integers.
- Output: three tiny traces, exact summations with endpoints, and upper/lower arguments.
- Performance target: derive the general bounds on paper; do not execute the large workloads.
  A checking program, if written after prediction, should initially use only `n <= 8`.
- Count the represented visits separately from arithmetic used to summarize their number.

### Required edge cases

- `n=1`; values around powers of two; a final incomplete group of steps.
- Explain which part of the contract would need revision to accept `n=0`.

### Before running

Name one row or level, write its legal range, and predict its contribution. Choose a lower bound
that accounts for many rows, rather than only the single most expensive row.

### Acceptance criteria

- [ ] All supplied traces and exact sums agree.
- [ ] Both directions of each tight bound are justified.
- [ ] The statement about loop shape is either supported or refuted with a concrete distinction.
- [ ] Analysis includes loop state, stored trace/output, stack, and Python numeric costs.

### Progressive hints

Hint 1 is locked until requested. Further hints require another attempt and a stated remaining gap.

## DSA-FND-070-P03 — One coordinator and two reviewers

### Task

There are `n` distinguishable people, identified by integers `0..n-1`. Only people `0..e-1`
may coordinate. A valid assignment chooses exactly one coordinator and two different reviewers;
the coordinator cannot review, and swapping the two reviewers does not create a new assignment.
Derive a count from `(n,e)`. For `(4,2)`, list the assignments by hand and explain how the list
checks completeness and duplicate handling. Do not submit only a library call.

### Constraints and expected behavior

- `0 <= e <= n <= 10^9`; inputs describe identities, not displayed names.
- Output: an exact nonnegative integer and a construction-based argument.
- Performance target: avoid enumerating people or assignments for the general count. Count
  arithmetic operations separately from the bit cost and size of the returned integer.
- Variation after the first attempt: the reviewer roles become “primary” and “secondary.”

### Required edge cases

- Too few people, no eligible coordinator, and everyone eligible to coordinate.
- Two people have the same displayed name but different IDs; does the contract change?

### Before running

Describe an output object, a simple enumeration, its bottleneck, any repeated representations,
and how you will show that each valid object is counted the same number of times.

### Acceptance criteria

- [ ] The tiny hand enumeration uses the contract's equality of assignments.
- [ ] Every factor or division is justified, with no extra restrictions invented.
- [ ] Empty and impossible cases have explicit behavior.
- [ ] The changed roles are analyzed without overwriting the original argument.

### Progressive hints

Hint 1 is locked until requested. Hint 2 follows a revised attempt; hint 3 follows an explanation
of the remaining uncertainty.

## DSA-FND-070-P04 — Auditing two draws

### Task

Seven distinguishable tokens have IDs `0..6`; IDs `0,1,2` are marked. An auditor draws two
tokens uniformly without replacement, in order. Determine the probability that both are marked,
the probability that at least one is marked, the expected number of marked draws, and the
probability that the second is marked conditional on the first being marked. Define elementary
outcomes and their weights first. Repeat the analysis when the first token is returned before
the second draw, and identify which reasoning changes.

### Constraints and expected behavior

- General parameters are `n >= 2` distinguishable tokens, `0 <= g <= n` marked tokens, two draws.
- Output: exact rational values, a sample-space description, and explicit assumptions.
- Performance target: use a symbolic derivation for the general case; tiny enumeration may
  verify it but must not be the only proof. Do not replace reasoning with simulation.
- If a conditioning event is impossible, say the conditional probability is undefined.

### Required edge cases

- No marked tokens, all marked tokens, exactly one marked token, and `n=2`.
- State whether a repeated token ID is a legal outcome in each version.

### Before running

Write the event definitions, the measured count, and the probability of a single elementary
outcome. Keep predicted values separate from any observed simulation frequencies.

### Acceptance criteria

- [ ] Every rational result has a derivation with legal denominators.
- [ ] Independence is used only where justified.
- [ ] Expected count and the probability of a positive count are not interchanged.
- [ ] The changed replacement policy and degenerate cases are explained in plain language.

### Progressive hints

Hint 1 is locked until requested. Additional hints follow a new attempt and a stated gap.

## DSA-FND-070-P05 — What must be returned?

### Task

A service chooses exactly `k` positions out of `n` distinguishable positions. Compare three
output contracts: only the number of valid selections; every selection as a fresh list of its
chosen indices; and every selection as a fresh length-`n` list of zero/one membership entries.
For `n=5,k=2`, draw one representative output for each contract and count all required output
slots without writing every list. Then derive general output-size and unavoidable-write bounds.

### Constraints and expected behavior

- `0 <= k <= n <= 60`; explicitly materializing examples is restricted to `n <= 8`.
- Indices in each chosen-index list are increasing; lists are distinct owned outputs, not views.
- Output: a count and a representation-cost comparison, including per-list container overhead.
- Performance target: compute the number without enumerating selections. For explicit output,
  justify what work cannot be avoided; do not claim that a quick counting expression writes lists.
- Variation: a caller consumes one selection at a time instead of retaining all of them.

### Required edge cases

- `n=0,k=0`, `k=0`, and `k=n`; an empty output list can still have a container cost.
- Equal values stored at different positions; this task still selects positions.

### Before running

Define output equality, the number of containers, the number of element slots, and the input
size of the returned count itself. Separate output storage from auxiliary generation state.

### Acceptance criteria

- [ ] Every representation has a clear contract and a justified general size expression.
- [ ] Empty selections and per-container overhead are not lost.
- [ ] Integer bit costs and enumeration costs are distinguished.
- [ ] Streaming's effect on retained space and total work is explained separately.

### Progressive hints

Hint 1 is locked until requested. No representation formulas or generation code have been supplied
for this exercise; further hints require a revised attempt.

## DSA-FND-070-P06 — Packet A

### Task

A record has `n` positions. Each position stores exactly one of the symbols `0`, `1`, or `2`.
A record is valid when neighboring positions never hold the same symbol. Different complete
symbol sequences are different records. Given `n`, return the number of valid records. There is
one empty record. Explain your approach and produce a small case that can independently check
the result. Preserve the first attempt before seeking feedback.

### Constraints and expected behavior

- Input: an integer `0 <= n <= 200`.
- Output: the exact nonnegative number of valid records; no rounding or remainder operation.
- Select and justify your own method and resource bounds. No target complexity or structure
  is supplied before the attempt.
- After closing the first attempt, consider requiring the first position to contain `0` when
  `n > 0`. Keep the empty-record convention unchanged.

### Required edge cases

- `n=0`, `n=1`, and records with two positions.
- An input large enough that listing all records would be impractical.

### Acceptance criteria

- [ ] The contract, original attempt, and independently checked small case are preserved.
- [ ] Correctness, termination, time, auxiliary/output/stack space, and numeric representation
  are explained using the chosen method.
- [ ] Any hint is recorded; intended structure and postmortem are revealed only after closure.

### Progressive hints

All hints are locked. Request one after recording an attempt; no pre-attempt method is supplied.

## DSA-FND-070-P07 — Packet B

### Task

A worker receives integers `n` and `budget`. On each run it draws one integer `r` uniformly
from `1..n`, then visits exactly `r` cells. Each visit costs one work unit; this model counts no
other work. Report the largest possible work, the average work over this declared random choice,
and the chance that a run exceeds `budget`. A teammate says the average is enough to guarantee
the budget for every run. Assess that claim and explain what the caller can actually rely on.

### Constraints and expected behavior

- `1 <= n <= 10^9`, `0 <= budget <= n`; strict exceedance means work greater than `budget`.
- Output: exact quantities plus a concise explanation. Start with `(n,budget)=(7,4)`.
- Timebox: 20 minutes, including clarifying questions, an independent small check, and explanation.
- Choose and defend your method and complexity. No target complexity, invariant, or intended
  structure is supplied before the attempt.
- Follow-up after closure: two workers reuse the same drawn `r`. Which requested quantities
  would need reconsidering if their combined work is measured?

### Required edge cases

- `n=1`, zero budget, and budget equal to `n`.
- Explain whether a fractional average implies that a run visits a fractional cell.

### Acceptance criteria

- [ ] The first explanation and every clarification/hint are recorded.
- [ ] All requested quantities use the given experiment and strict budget comparison.
- [ ] The guarantee claim is assessed with a legal case and a justified general statement.
- [ ] Time, auxiliary/output/stack space, and exact numeric output costs are defended.

### Progressive hints

All hints are locked. The interviewer gives only one requested hint at a time after an attempt.

## Review record

No learner evidence exists yet. After an attempt, record its date and local artifact path, the
original reasoning, what was correct, the first missing step, a smallest counterexample, hint
level, actual commands and observations, remaining weakness, and next review date. Preserve
corrections alongside the original attempt. Use [REVIEW.md](../REVIEW.md) for state decisions.

Passing supplied tests or reading recorded experiment output does not satisfy the practice,
recall, or mixed-transfer evidence gates.
