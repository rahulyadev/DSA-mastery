# Review Record — DSA-FND-040 Asymptotic notation and input-variable modeling

| Field | Value |
|---|---|
| Unit note | [DSA-FND-040](README.md) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Practice | [Unsolved exercises](practice/README.md) |
| Artifact state | Draft |
| Learning state | Not started |
| Last evidence | — |
| Next review | 1 day after first study, then adapt to observed recall |
| Mastery badge | No |
| Strongest area | Not evaluated yet |
| Weakest area | Not evaluated yet |

## Closed-book reconstruction questions

1. What must your model sentence specify before the symbol `n` becomes meaningful?
2. Can you redraw a three-by-two body-visit trace and explain what its marks omit?
3. What counting invariant holds after `r` complete rows of a rectangle?
4. How would you derive the triangular count without guessing from two nested loops?
5. What constants and threshold establish a tight bound for `4*n + 9`?
6. How can a valid upper bound be correct yet less informative than a tight bound?
7. How do best, worst, and expected costs differ from upper, lower, and tight bounds?
8. How many body transitions occur when a positive cursor doubles until it reaches at least 33?
9. Why can a zero inner dimension leave a growing total runtime?
10. Which Python costs can be hidden by a slice, membership test, or user-defined comparison?
11. What changes between retaining every trace row and returning only a final scalar?
12. Why is a bound on one implementation not automatically a lower bound on the problem itself?

Reconstruct answers from memory first. Use the note only after marking where recall stopped.

## Delayed-recall questions

Intervals begin with actual study evidence, not the date this file was initialized. Do not assign
successful recall dates in advance. Ask one question, listen, then choose the smallest next probe.

### 1-day recall

1. Can you explain `O`, `Omega`, and `Theta` with one function and actual constants?
2. For a four-row, zero-column loop, which operations still occur?
3. What is the first question you ask when someone says “the input size is `n`”?

### 3-day recall

1. Can you recover the triangular prefix-count invariant and justify its preservation?
2. What family disproves dropping an independent `m` term from `n + m`?
3. If the doubling guard changes from `<` to `<=`, where do boundary counts change?

### 7-day recall

1. A data source changes from a rectangular grid to rows of unequal lengths, including empties.
   What quantities would you name before deriving traversal work?
2. Why can repeated temporary copying have a different peak-space class from retained copying?
3. Can you derive a fresh stepped-loop count chosen by the reviewer without seeing its label?

### 14-day recall

1. How does your analysis change when equality compares variable-length records?
2. Can a search's expected cost stay small under one distribution while its worst case grows?
3. Without naming a growth class first, explain how to analyze a loop over an integer's value
   when the input is encoded in binary?

### 30-day recall

1. Can you analyze an unseen two-input program, including empty cases, without renaming both sizes `n`?
2. Can you teach the difference between a measured timing ratio and a mathematical tight bound?
3. Which exact assumption from your original analysis would fail under a changed representation?

## Interview retrieval

1. How would you clarify the input representation and relevant size variables in thirty seconds?
2. What is the simplest exhaustive baseline, and which event measures its bottleneck?
3. Which invariant ensures that your count covers every required event exactly once?
4. Why does reducing a pair enumeration by roughly half not necessarily change its growth class?
5. What supports the upper bound, and what feasible input family supports the lower bound?
6. Where could Python do more work than the visible number of loop iterations suggests?
7. How do you report auxiliary, output, and stack space without hiding instrumentation?
8. What changes if one input dimension is fixed while the other can grow?
9. Which claim would you withdraw if only a few benchmark samples supported it?
10. Can you complete a fresh unlabeled contract within twenty minutes and defend your decisions?

For mixed/mock retrieval, show only the new contract and constraints. Do not supply a pattern,
target complexity, invariant, or intended data structure before the attempt.

## One-question-at-a-time evidence record

### Question 1

Two unchanged lists have independently chosen lengths. What do you need to know about the work
performed before you can distinguish an additive count from a pairwise count?

**Rahul's answer:** Not attempted yet.

**Correct reasoning:** Record only after Rahul answers.

**First missing step:** Not evaluated.

**Smallest recovery hint:** Locked until needed; provide one hint at a time.

**Follow-up and counterexample:** Choose after the answer reveals a specific gap.

**Date and recall interval:** Not recorded.

Append later questions with the original answer, exact correction, hint level, and the next
retrieval date. A polished replacement answer must not erase how it was obtained.

## Evidence

| Link | Result | What it proves | Remaining limitation |
|---|---|---|---|
| — | Not attempted | No learner evidence yet | A generated pack and passing scaffold tests do not demonstrate learning |

The supplementary [experiment](experiments/DSA-FND-040-X01-counts-and-clock-time/README.md)
records an initialization run separately. It is a reproducibility check, not Rahul's prediction,
interpretation, proof, or delayed recall. A merge likewise changes publication state, not knowledge.

## Error log update

| Category | Exact failure | Corrective drill | Review interval |
|---|---|---|---|
| — | Not evaluated | First answer followed by the smallest relevant counterexample | 1 day after first study |

When an error occurs, name it precisely: an omitted variable, invalid witness constant, wrong input
case, unjustified lower bound, hidden primitive cost, lost empty-case overhead, or incorrect memory
lifetime. Pick a corrective drill only after observing the error; do not invent a weakness now.

## State decision

Recommended state: **Not started**.

Reason tied to the evidence gate: initialization creates a Draft pack but supplies no learner
prediction, attempt, or retrieval. No last-evidence date, next-review date in the tracker, weakest
point, or mastery badge is earned by publication.

Advance only on recorded evidence using [PROGRESS.md](../../../PROGRESS.md). A later failed review
may justify lowering a state. Do not mark this unit learned merely to begin
[DSA-FND-050](../../../CURRICULUM.md#dsa-fnd-050); that next unit depends on the reasoning here.
