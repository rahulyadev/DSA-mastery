# Review Record — DSA-FND-030 Invariants, correctness, and termination

| Field | Value |
|---|---|
| Unit note | [DSA-FND-030](README.md) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Artifact state | Draft |
| Learning state | Not started |
| Last evidence | — |
| Next review | 1 day after first study, then adapt |
| Mastery badge | No |
| Strongest area | Not evaluated yet |
| Weakest area | Not evaluated yet |

## Closed-book reconstruction questions

1. Define precondition, postcondition, guard, invariant, transition, and ranking measure in your own
   words.
2. Draw the loop-head proof cycle from initialization through preservation to exit.
3. Reconstruct the first-index visual for `values=[2,5,1,7]` and `threshold=6`.
4. State the exact half-open processed-prefix invariant, including its bounds clause.
5. Why is an empty processed prefix useful during initialization?
6. Prove one preservation step using old index `i` and new index `i'`.
7. Derive both postcondition cases from the invariant and the false guard.
8. Which statement establishes soundness, and which establishes completeness or minimality?
9. Distinguish partial correctness, progress, termination, and total correctness.
10. State the ranking measure, its domain, and its strict-change argument.
11. Why is “the input length stays fixed” an invariant but usually not a useful one?
12. Why can `0 <= i <= n` prove safety yet fail to prove the returned index is first?
13. Which guard order is safe on empty input, and which Python evaluation rule supports it?
14. How can an invariant-checking assertion change runtime complexity?
15. Why may required input validation not rely on Python `assert`?
16. Give one anti-signal that should make you reject a proposed invariant.

## Delayed-recall questions

### 1-day recall

1. Without opening the note, write the one-sentence mental model and four proof obligations.
2. Trace the first-index scan on `[]`, `[6]`, and `[1]` with threshold `6`.
3. What is the first mistake you made when separating invariant from termination?

### 3-day recall

1. Recover the invariant and ranking measure for the scan without reading code.
2. Explain why invariant plus false guard—not invariant alone—implies the result.
3. Construct the smallest counterexample for an update that advances by two positions.
4. Derive best/worst time and all space categories, including trace-only cost.

### 7-day recall

1. Given a loop with two branches and one `continue`, list every preservation and progress case you
   must inspect.
2. Derive a useful state claim for the dispatch-ledger practice task without naming a pattern.
3. Give a true but useless invariant, then strengthen it only enough to derive the postcondition.
4. Explain why finite tests can refute a universal claim but cannot establish it by themselves.

### 14-day recall

1. Change “first value at least threshold” to “last value at least threshold.” Which state meaning,
   exit reasoning, and result update must change?
2. Change the input from a fixed list to a one-pass stream. Which safety and termination facts remain,
   and which representation facts must be restated?
3. Present a two-minute proof without reading code or using “obviously.”

### 30-day recall

1. For an unseen state-transition problem, derive a contract, useful invariant, exit implication,
   ranking measure, and complexity from scratch.
2. Teach back the difference between an invariant, an assertion, a test property, and a postcondition.
3. Recover from a deliberately planted non-progress branch using the smallest counterexample and a
   corrected proof obligation.
4. Name one limitation of a trace and one limitation of a formal proof built over the wrong contract.

## Invariant and correctness recovery

1. At which exact boundary is the first-index invariant claimed?
2. What facts must the precondition supply for initialization and stable comparisons?
3. How do bounds and semantic clauses work together in one invariant?
4. For each continuing branch, what are the assumptions and the resulting new state?
5. Which old-state fact and guard fact establish preservation of the enlarged prefix?
6. Negate `i < n and values[i] < threshold` without making an unsafe access.
7. Why does the in-bounds exit return a valid index?
8. Why can no earlier index be valid?
9. Why is `None` correct at the exhausted exit?
10. What additional obligation is needed if the input can mutate during execution?
11. What changes when a loop is allowed to return early from inside its body?
12. Can a loop preserve its invariant and still fail to terminate? Give a minimal state transition.

## Complexity explanation

1. Define `n` and comparison cost `c` before stating a bound.
2. Derive best-case and worst-case comparison counts for the teaching scan.
3. Why does early exit not improve the no-match worst case?
4. Why is the quantified processed prefix logical rather than stored auxiliary space?
5. What are auxiliary, output, and recursion-stack space for the scalar-return scan?
6. Derive the total debug work if a length-`i` prefix is rechecked at every loop head.
7. What allocation is introduced by `values[:i]`?
8. When should Python integer magnitude become an explicit input variable?
9. How should complexity change if every matching index must be returned?
10. Why is “one loop means O(n)” weaker than counting dominant operations?

## Changed constraints

1. What changes if equality no longer satisfies the threshold predicate?
2. What changes if the output must contain every valid index in increasing order?
3. What changes if the output is the last valid index?
4. What changes if the caller allows input mutation but still requires original indices?
5. What changes if comparisons can raise an exception?
6. What changes if another actor can append to the list during iteration?
7. What changes if a caller-supplied step budget may stop the search before exhaustion?
8. What changes if the collection is infinite and a valid item may never arrive?
9. What changes if values are floating-point and may include `NaN`?
10. What changes if one comparison costs `Theta(b)` for `b`-bit values?

## Interview retrieval

1. How would you recognize that correctness—not pattern recognition—is the main pressure?
2. What is the simplest correct baseline and its exact bottleneck?
3. Which loop invariant captures the processed state, and where does it hold?
4. Why is the invariant initialized and preserved on every branch?
5. How do invariant and false guard imply the postcondition?
6. Why is the algorithm safe, sound, and complete?
7. What measure proves progress and termination?
8. What are best/worst time and auxiliary/output/stack space?
9. Which Python operation or assertion could silently change complexity or behavior?
10. What tempting proof statement is too weak, and on what smallest case?
11. How would you adapt the proof when the interviewer changes “first” to “all”?
12. Can you explain the proof naturally in under two minutes without narrating every line?

## One-question-at-a-time evidence record

### Question 1

Without opening the unit note, analyze this loop for a finite unchanged list:

```text
i <- 0
while i < n and item i is not valid:
    i <- i + 1
return NO_RESULT if i == n else i
```

State the exact postcondition, loop-head invariant, initialization argument, preservation argument,
two exit cases, safety argument, ranking measure, termination proof, and best/worst time plus
auxiliary/output/stack space. Then give the smallest defect that would break each of guard safety,
preservation, and progress.

**Rahul's answer:** Not attempted yet.

**Correct reasoning:** Record only after Rahul answers.

**First missing step:** Record only after Rahul answers.

**Smallest recovery hint:** Give only when needed.

## Evidence

| Date | Link | Result | What it proves | Remaining limitation |
|---|---|---|---|---|
| — | — | Not attempted | Initialization and scaffold checks provide no learner evidence | Prediction, proof, debugging, transfer, and delayed recall remain |

## Error log update

| Category | Exact failure | Smallest counterexample or corrective drill | Review interval |
|---|---|---|---|
| — | Not evaluated | Complete Question 1 without opening the note | 1 day after first study |

Use one of these categories when evidence exists: contract, boundary, bounds, invariant strength,
initialization, preservation, guard safety, exit implication, soundness, completeness, ranking
measure, termination, complexity, Python assertion cost, edge case, or communication.

## State decision

Recommended state: **Not started**

Reason tied to the evidence gate: the Draft pack exists, but Rahul has not yet produced a prediction,
trace, proof, debugging diagnosis, mixed transfer, interview explanation, or delayed-recall evidence.

Do not advance the learning state because files were generated, the scaffold passed, or the topic
branch was merged. Reassess after learner evidence, and lower a later state if recall exposes a
material gap.
