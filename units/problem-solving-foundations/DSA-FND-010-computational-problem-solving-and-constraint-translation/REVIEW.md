# Review Record — DSA-FND-010 Computational problem solving and constraint translation

| Field | Value |
|---|---|
| Unit note | [DSA-FND-010](README.md) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Artifact state | Draft |
| Learning state | Not started |
| Last evidence | — |
| Next review | 1 day after first study, then adapt |
| Mastery badge | No |
| Strongest area | Not evaluated yet |
| Weakest area | Not evaluated yet |

## Closed-book reconstruction questions

1. What are the seven lines of a constraint ledger, and why does output come before candidate pattern?
2. Reconstruct the distinct-pair teaching predicate using values, target, n, i, and j.
3. Draw the prompt → contract → examples → baseline → count → feasible-envelope trace.
4. What contract invariant must remain true while a candidate is optimized?
5. Why are [4] and [4, 4] together stronger than either example alone?
6. Derive the exact number of unordered pairs for n items without reading the formula.
7. Why can early return not improve the required worst-case count for a Boolean existence query?
8. What separate roles do n, q, and r play?
9. Distinguish input, auxiliary, output, and recursion-stack space.
10. Give one anti-signal that should stop a pattern-first guess.
11. Which Python expressions can hide a traversal or allocation even when written on one line?
12. What is the smallest clarification question when a tie-breaking rule is absent?

## Delayed-recall questions

### 1-day recall

1. Without opening the note, write the one-sentence mental model and the constraint ledger.
2. Recompute the work for n=10 unordered pairs, then explain the singleton boundary.
3. Which assumption did you most recently add without evidence?

### 3-day recall

1. Recover the contract invariant and apply it to “return any” versus “return all.”
2. For n items and q full-scan queries, derive time and space using independent variables.
3. Explain why a deterministic operation count and a benchmark answer different questions.

### 7-day recall

1. Translate this unseen variation: return the first duplicate in arrival order from a replayable list while preserving the list.
2. Which tempting alternative becomes invalid if that same input changes to a one-pass stream?
3. Construct a minimal example that separates value identity from position identity.

### 14-day recall

1. Change the booking exercise from half-open to closed intervals. Which predicate and edge case change?
2. Explain the complete feasibility derivation without using any pattern label.
3. If a result contains r items, why must the complexity statement mention r?

### 30-day recall

1. Given an unfamiliar prompt with n records, q updates, and r reported matches, produce the ledger, one baseline, one adversarial case, and a feasible envelope.
2. Teach back the difference among a computational problem, an algorithm, a candidate state, and an implementation.
3. Name one limitation of abstract operation counts and one limitation of raw wall-clock timing.

## Invariant and correctness recovery

1. State the contract invariant in one sentence.
2. How do initialization, preservation, progress, completeness, safe exclusion, and final state apply to constraint translation?
3. Prove that the nested pair baseline visits every legal pair exactly once.
4. Give a counterexample to the claim that passing the samples proves the general interpretation.
5. When is it safe to exclude a candidate family before a replacement algorithm is known?

## Complexity explanation

1. What is the dominant operation in the all-pairs baseline?
2. Derive n(n−1)/2 from a sum and then state its growth.
3. Why can a nested loop be linear, and why can a one-line expression be linear or worse?
4. How would you report preprocessing P(n) and per-query Q(n) across q queries?
5. What space categories must be named for an iterative function that copies input and returns r outputs?
6. Which claim requires an experiment: asymptotic operation growth or elapsed time on a stated workload?

## Changed constraints

1. What changes when a Boolean result becomes every valid witness?
2. What changes when mutation is allowed but original indices must still be returned?
3. What changes when one target becomes q targets against stable data?
4. What changes when a reusable sequence becomes a one-pass stream?
5. What changes when an exact result may become approximate?
6. What changes when the numeric domain is bounded to only 1,000 possible values?

## Interview retrieval

1. How would you recognize this unit's problem shape from constraints alone?
2. What is the simplest correct brute force and its exact bottleneck?
3. Which contract invariant makes the derivation safe?
4. Why is the baseline complete, and what can it safely ignore?
5. What are time, auxiliary, output, and recursion-stack costs?
6. Which Python operation could silently change the complexity?
7. What tempting interpretation fails, and on what smallest case?
8. How does the solution contract change when one Boolean becomes every witness?
9. Which clarification would you ask before discussing a pattern?
10. Can you explain the feasible envelope in under two minutes without promising a final algorithm?

## One-question-at-a-time evidence record

### Question 1

Without opening the unit note, translate this statement: “Given n integers, return whether two distinct positions contain equal values; n may be zero, input order must not change, and n ≤ 200,000.” State the predicate, three edge cases, the simplest baseline, its dominant count, and the required feasible envelope.

**Rahul's answer:** Not attempted yet.

**Correct reasoning:** Add after Rahul answers.

**First missing step:** Add after Rahul answers.

**Smallest recovery hint:** Give only when needed.

## Evidence

| Date | Link | Result | What it proves | Remaining limitation |
|---|---|---|---|---|
| — | — | Not attempted | Initialization alone provides no learning evidence | Closed-book work, practice, and delayed recall remain |

## Error log update

| Category | Exact failure | Smallest counterexample or corrective drill | Review interval |
|---|---|---|---|
| — | Not evaluated | Complete Question 1 without opening the note | 1 day after first study |

Use one of these categories when evidence exists: interpretation, constraints, variables, quantifier, invariant, proof, complexity, space, Python cost, edge cases, communication, or time management.

## State decision

Recommended state: **Not started**

Reason tied to the evidence gate: the Draft learning pack exists, but Rahul has not yet produced a prediction, explanation, practice attempt, or delayed-recall evidence.

Do not advance the learning state because files were generated or tests passed. Reassess after evidence, and lower the state if a later review exposes a material gap.
