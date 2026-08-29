# Review Record — DSA-FND-020 Brute-force enumeration and bottleneck discovery

| Field | Value |
|---|---|
| Unit note | [DSA-FND-020](README.md) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Artifact state | Draft |
| Learning state | Not started |
| Last evidence | — |
| Next review | 1 day after first study, then adapt |
| Mastery badge | No |
| Strongest area | Not evaluated yet |
| Weakest area | Not evaluated yet |

## Closed-book reconstruction questions

1. Define brute-force enumeration without using the words “slow” or “nested loops.”
2. Reconstruct the candidate object, legality rule, and six-cell upper triangle for unordered pairs when `n = 4`.
3. State the enumeration invariant immediately before one pair is checked.
4. Derive `n(n-1)/2` from row lengths rather than quoting a formula.
5. Why does `right` starting at `left + 1` establish both distinctness and no reverse duplicates?
6. Prove soundness and completeness for the all-matching-pairs baseline.
7. Distinguish candidate-generation work from predicate-evaluation work using the interval example.
8. Why can all-interval enumeration be quadratic while an implementation that slices and sums every interval is cubic?
9. State time, auxiliary space, output space, and recursion-stack space for streamed pair enumeration returning `r` matches.
10. What does a generator change, and what does it not change?
11. Give the smallest example that separates equal values from identical positions.
12. What exact sentence should replace the vague claim “brute force is the bottleneck”?

## Delayed-recall questions

### 1-day recall

1. Draw the legal-pair triangle and recover the one-sentence mental model without opening the note.
2. For `[4, 1, 7, 4]` and target `8`, list every candidate and match in canonical order.
3. Which bug appears if both loops run from zero to `n - 1`?

### 3-day recall

1. Recover the coverage/no-duplicate invariant and apply it to triples `i < j < k`.
2. Derive the exact triple count for `n = 5` from loop row sizes or a counting argument.
3. Explain why early return changes some instances but not the no-witness worst case.

### 7-day recall

1. Given all contiguous intervals, separate boundary-candidate count from total re-summing work.
2. Design a tiny exhaustive oracle for a later optimized method without materializing every candidate.
3. Which tempting candidate generator fails when equal values occupy different positions?

### 14-day recall

1. Change unordered pairs to ordered pairs. Which legality rule, count, loop bounds, and output order change?
2. Explain the baseline and bottleneck in under two minutes without naming any faster pattern.
3. If the input becomes a one-pass iterable, which assumptions in the index-based baseline fail?

### 30-day recall

1. For an unseen finite search problem, define candidates, legality, evaluator, invariant, count, bottleneck, and optimization contract before proposing a data structure.
2. Teach back the difference between reducing the candidate space and reducing evaluation cost.
3. Name one limitation of abstract operation counts and one limitation of raw timing measurements.

## Invariant and correctness recovery

1. State the pair-enumeration invariant precisely enough to identify checked and unchecked candidates.
2. How do initialization and preservation apply when moving within one `left` row?
3. Why is the transition from the last `right` of one row to the first `right` of the next row safe?
4. Prove that each legal unordered pair appears in exactly one row.
5. Why may self-pairs and reverse duplicates be safely excluded?
6. What additional proof must an optimized method give for candidates it skips?
7. What termination measure works for the nested loops?
8. How would the proof change if only the first lexicographic match were required?

## Complexity explanation

1. What are `n`, `C(n)`, `E(candidate)`, and `r`?
2. Write the total-work summation when candidate evaluation costs differ.
3. Derive pair and triple candidate counts without hiding constants before the count is understood.
4. Why does an all-output contract require `Theta(r)` output space?
5. What transient allocation occurs in `values[left:right + 1]` for list input?
6. Why does lazy generation not make consuming all combinations subquadratic?
7. How do best case, worst case, and expected case differ for early-exit enumeration?
8. When must integer magnitude become an input variable in Python cost analysis?

## Changed constraints

1. What changes when one witness is enough instead of every witness?
2. What changes when pair order matters?
3. What changes when using the same position twice becomes legal?
4. What changes when the original input may be reordered?
5. What changes when only the count of matches is required rather than the matches themselves?
6. What changes when candidates must be yielded lazily to a consumer?
7. What changes when the input cannot be replayed or indexed?
8. What changes when candidate evaluation itself scans a length-`m` object?

## Interview retrieval

1. How would you recognize that a trustworthy exhaustive baseline is useful here?
2. What is one legal candidate and the simplest correct brute force?
3. What exact bottleneck does that baseline expose?
4. Which invariant proves coverage and prevents duplicate candidates?
5. Why is the baseline sound, complete, and terminating?
6. What are time, auxiliary, output, and recursion-stack costs?
7. Which Python operation could silently add traversal or allocation work?
8. What tempting generator fails, and on what smallest case?
9. Does the next idea reduce candidate count, evaluation cost, or both?
10. How does the approach change when the output contract changes from all matches to one witness?

## One-question-at-a-time evidence record

### Question 1

Without opening the unit note, solve this reasoning task: for `n` positions, define and enumerate every unordered triple of distinct positions. State canonical loop bounds, derive the exact candidate count, give a coverage/no-duplicate invariant, prove termination, and explain time plus auxiliary/output/stack space when `r` triples are returned.

**Rahul's answer:** Not attempted yet.

**Correct reasoning:** Add after Rahul answers.

**First missing step:** Add after Rahul answers.

**Smallest recovery hint:** Give only when needed.

## Evidence

| Date | Link | Result | What it proves | Remaining limitation |
|---|---|---|---|---|
| — | — | Not attempted | Initialization and passing scaffold checks provide no learner evidence | Prediction, implementation, proof, transfer, and delayed recall remain |

## Error log update

| Category | Exact failure | Smallest counterexample or corrective drill | Review interval |
|---|---|---|---|
| — | Not evaluated | Reconstruct Question 1 without opening the note | 1 day after first study |

Use one of these categories when evidence exists: candidate definition, legality, bounds, coverage, duplication, invariant, proof, complexity, hidden Python cost, output space, edge case, optimization contract, or communication.

## State decision

Recommended state: **Not started**

Reason tied to the evidence gate: the Draft pack exists, but Rahul has not yet produced a prediction, trace, implementation attempt, correctness explanation, mixed transfer, or delayed-recall evidence.

Do not advance the learning state because files were generated, scaffold tests passed, or the topic branch was merged. Reassess after learner evidence, and lower a later state if recall exposes a material gap.
