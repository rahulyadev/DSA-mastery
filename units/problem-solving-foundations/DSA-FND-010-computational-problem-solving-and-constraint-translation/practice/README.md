# Practice — DSA-FND-010 Computational problem solving and constraint translation

| Field | Value |
|---|---|
| Unit note | [DSA-FND-010](../README.md) |
| Curriculum | [CURRICULUM.md](../../../../CURRICULUM.md#dsa-fnd-010) |
| Problem bank | [PROBLEM_BANK.md](../../../../PROBLEM_BANK.md) |
| Evidence target | E+T+P+D+R+M |
| Attempt required before comparison | Yes |
| Passing scaffold command | uv run --group dev python -m pytest -q practice/test_micro_lab.py |
| Learner implementation contract | Not applicable; this unit's evidence profile excludes I |
| Status | Not attempted |

## Learning questions

1. Can you convert prose into a stable input/output predicate before an algorithm name appears?
2. Can you use independent variables and exact operation counts to reject a candidate without inventing a universal timing rule?
3. Can you recognize when a specification is ambiguous or impossible instead of coding through the contradiction?

## Cycle

~~~text
predict → trace → run → observe → explain → vary → recall
~~~

## File and test separation

- [micro_lab.py](micro_lab.py) is a runnable deterministic operation-budget trace. It reveals reasoning state without solving the written exercises.
- [test_micro_lab.py](test_micro_lab.py) checks only the provided lab formulas and boundary behavior.
- No starter or challenge test is created because DSA-FND-010 requires explanation, trace, proof, debugging, recall, and mixed transfer—not implementation evidence.
- Preserve every written attempt and hint level in the review record.

## Exercise index

| Exercise ID | Type | Difficulty | Objective | Files | Status |
|---|---|---:|---|---|---|
| DSA-FND-010-P01 | Predict / Trace | 1 | Predict exact work counts and budget decisions before running the lab | micro_lab.py | Not attempted |
| DSA-FND-010-P02 | Translate / Defend | 2 | Build a complete constraint ledger for an interval prompt without receiving a pattern | This file | Not attempted |
| DSA-FND-010-P03 | Debug / Changed constraint | 2 | Detect and repair an impossible exact-streaming contract | This file | Not attempted |

## DSA-FND-010-P01 — Predict the budget trace

### Task

Without opening or running micro_lab.py, calculate the dominant-operation count and within-budget decision for every default scenario listed below. Record the formula first, substitute the values second, and mark the first scenario where intuition based only on “large n” would give an incomplete explanation. Then run the lab and reconcile every difference.

### Constraints and expected behavior

- Input scenarios:
  - shape single_scan with n=12, q=1, r=1, budget=100;
  - shape all_unordered_pairs with n=6, q=1, r=1, budget=14;
  - shape all_unordered_pairs with n=200,000, q=1, r=1, budget=3,000,000;
  - shape scan_per_query with n=200,000, q=100,000, r=100,000, budget=3,000,000;
  - shape build_once_then_one_per_query with n=200,000, q=100,000, r=100,000, budget=3,000,000;
  - shape output_lower_bound with n=10, q=1, r=5,000,000, budget=3,000,000.
- Required observation or output: a written seven-row prediction including the automatically added empty-input boundary row, followed by the program's deterministic table and a discrepancy note.
- Performance target: exact integer arithmetic only; this exercise models abstract dominant operations and makes no seconds-based claim.

### Required edge cases

- For n=0, all_unordered_pairs must produce zero rather than a negative count.
- A candidate whose work equals its budget is within budget; only work greater than the budget is rejected.
- Output pressure is controlled by r even when n is small.

### Before running

Record for each row: independent variables, formula, exact count, decision, and one sentence explaining which contract fact makes that shape relevant.

### Acceptance criteria

- [ ] Every prediction is timestamped or otherwise clearly recorded before execution.
- [ ] n, q, and r are kept independent.
- [ ] The unordered-pair count is derived rather than guessed from loop shape.
- [ ] Equality at the budget boundary is handled correctly.
- [ ] Actual command and observed output are recorded without converting the result into a hardware-speed claim.
- [ ] Each discrepancy names the first mistaken reasoning step.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## DSA-FND-010-P02 — Translate the booking-overlap contract

### Task

Translate the prompt below into a seven-line constraint ledger, three additional adversarial examples, a simplest correct baseline described in plain language, and a feasible time/space envelope. Do not name or implement a final algorithm. Propose two candidate work families, derive each dominant count, and reject a family only with a concrete correctness or resource conflict.

> Given a list of half-open booking intervals (start, end), return whether any two bookings overlap. There are n intervals, 0 ≤ n ≤ 150,000. Every endpoint is an integer with 0 ≤ start < end ≤ 10^9. Intervals that only touch, such as (1, 3) and (3, 5), do not overlap. The original list and its interval objects must remain unchanged. A separate copy is allowed. Use at most O(n) auxiliary space and at most 4,000,000 abstract endpoint comparisons in the worst case.

### Constraints and expected behavior

- Input contract: one reusable list of n valid integer pairs representing half-open intervals.
- Output contract: one Boolean; True exactly when at least two distinct interval positions share a point.
- Required supplied examples: [] gives False; [(1, 3), (3, 5)] gives False; [(5, 8), (2, 6)] gives True.
- Performance target: at most 4,000,000 endpoint comparisons in the worst case and O(n) auxiliary space; no wall-clock prediction is requested.

### Required edge cases

- A singleton interval list returns False because two distinct positions are required.
- Duplicate non-empty intervals overlap even though their values are equal.
- Touching endpoints do not overlap under half-open semantics.
- Input order may be meaningful to the caller even though the output itself is Boolean, so the original representation cannot be reordered in place.

### Before writing candidate families

- Inputs and size variables:
- Exact output predicate:
- Quantifier and identity rules:
- Bounds and representation:
- Mutation/order permissions:
- Normal, boundary, and adversarial examples:
- Unresolved ambiguity:
- Simplest correct baseline:
- Dominant operation and exact count:
- Required feasible envelope:

### Acceptance criteria

- [ ] The predicate defines overlap using the half-open endpoint rule.
- [ ] Every example is checked against the same predicate.
- [ ] The baseline is argued correct before it is assessed for feasibility.
- [ ] Two candidate work families have symbolic counts in n.
- [ ] At least one rejection cites an exact worst-case count or a contract violation.
- [ ] Time, auxiliary space, output space, recursion stack, and any Python copy/sort cost are stated separately.
- [ ] No pattern label substitutes for the derivation.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## DSA-FND-010-P03 — Repair an impossible streaming contract

### Task

Act as the engineer reviewing the following requirement before implementation. Produce the exact input/output contract, identify whether all requirements can hold simultaneously, construct the smallest persuasive failure family, and write the clarification you would ask. Then propose two revised contracts—each changing exactly one requirement—and explain what new feasible envelope each revision creates. Do not provide algorithm code.

> Device identifiers arrive as a one-pass stream of arbitrary strings. The stream length and number of distinct identifiers are unbounded. Return the first identifier whose second occurrence arrives, or None if no identifier repeats. The result must be exact. The stream cannot be replayed, and the process may retain at most 100 distinct identifiers.

### Constraints and expected behavior

- Input contract: a one-pass, finite but unbounded-length stream of arbitrary strings; the number of distinct strings is not bounded.
- Output contract: the earliest-by-arrival identifier at its second occurrence, otherwise None at end of stream; approximation is forbidden.
- Retained-state contract: at most 100 distinct identifiers may be remembered and no replay is available.
- Performance target: one pass; state must respect the fixed distinct-identifier limit.

### Required edge cases

- The first repeated identifier may occur immediately, as in A, A.
- A duplicate may arrive only after more than 100 different identifiers have appeared.
- The entire stream may contain no duplicate.
- Two identifiers may both receive a second occurrence at adjacent positions; “first” is determined by arrival order.

### Before proposing a repair

- Which requirement supplies information?
- Which requirement discards or forbids information?
- What two input prefixes are indistinguishable to any state obeying the limit?
- Which exact-output obligation can those prefixes force to differ on a later item?
- What is the smallest clarification question that would unblock design?

### Acceptance criteria

- [ ] The response does not pretend that a data-structure name resolves the contradiction.
- [ ] The failure argument uses an input family rather than one unexplained assertion.
- [ ] The roles of exactness, replay, domain cardinality, and retained state are separated.
- [ ] Each revised contract changes exactly one of those four facts.
- [ ] Each revision states its new time, auxiliary-space, output-space, and stack-space envelope.
- [ ] The reasoning is explained in interview-ready language without revealing a memorized pattern label.

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
