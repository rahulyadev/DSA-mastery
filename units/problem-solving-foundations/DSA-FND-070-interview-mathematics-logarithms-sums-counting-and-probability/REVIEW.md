# Review Record — DSA-FND-070 Interview mathematics: logarithms, sums, counting, and probability

| Field | Value |
|---|---|
| Unit note | [DSA-FND-070](README.md) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Practice | [Unsolved tasks](practice/README.md) |
| Artifact state | Draft |
| Learning state | Not started |
| Last evidence | — |
| Next review | 1 day after first study, then adapt |
| Mastery badge | No |
| Strongest area | Not evaluated yet |
| Weakest area | Not evaluated yet |

Initialization, publication, supplied test results, and maintainer experiment runs are artifact
evidence. None is Rahul's learning evidence. Dates below are relative to the first real study
session, not to file creation; record actual dates only when that session occurs.

## Closed-book reconstruction questions

1. What question does a logarithm answer, and which domain restrictions apply?
2. Starting at 29, reconstruct floor division by three while the current value is at least three.
   What exact invariant and terminal inequality justify the update count?
3. How would you reconstruct an arithmetic sum by pairing, without quoting its formula first?
4. Why can a fixed-ratio geometric workload have much more work than its number of levels?
5. How do groups of reciprocal terms establish an unbounded but slowly growing harmonic sum?
6. What distinguishes a permutation, a combination, and a selection where repetition is allowed?
7. Before dividing a count to remove duplicates, what must be proved about multiplicity?
8. What are an elementary outcome, an event, an indicator, and an expectation?
9. Why does expectation add across dependent indicators, while event probabilities cannot
   generally be multiplied without checking independence?
10. What is an anti-signal for using a formula to replace data inspection?
11. How do time, auxiliary space, output space, recursion stack, and Python integer costs differ
    for a count and a materialized collection?
12. What makes expected cost different from both worst-case and amortized cost?

## Delayed-recall questions

### 1-day recall

1. Can you redraw the halving/covering traces for an input just above a power of two and explain
   the different endpoints without using a floating logarithm?
2. What is the smallest case that distinguishes states from transitions or ordered from unordered pairs?

### 3-day recall

1. Can you recover the quotient invariant and both sides of its final inequality?
2. Can you derive one arithmetic and one geometric sum, then explain the computational cost
   of evaluating a formula versus enumerating its counted objects?

### 7-day recall

1. Can you bound a new schedule of work after writing its actual per-stage contributions?
2. Can you explain why expectation can add when two events are dependent, and reject a
   tempting product of their probabilities using a small outcome space?

Use a fresh problem supplied after the current practice closes. A prompt already printed in the
pack is a recall exercise, not evidence of an unseen transfer.

### 14-day recall

1. What changes in a count when roles become distinguishable, repeated selections become legal,
   or equal displayed values stop representing distinct outputs?
2. Can you explain a new counting or sampling contract in two minutes without naming a formula
   first, while stating its limitations and Python costs?

### 30-day recall

1. Can you derive a fresh problem's count or bound from constraints, check it on a tiny case,
   and defend the result after an interviewer changes the output representation?
2. Can you teach why more sampled trials do not guarantee a closer estimate at every prefix,
   and why one successful run is neither a proof nor a worst-case guarantee?

## Interview retrieval

1. What input, output, equality rule, and random mechanism need clarification before calculation?
2. What is the simplest correct enumeration, and what precise bottleneck could be removed?
3. Which invariant or counting correspondence makes the shortcut correct?
4. Why is the approach complete, and why can excluded or duplicate constructions be ignored?
5. What are time, auxiliary, output, and recursion-stack costs under the chosen input model?
6. Which Python operation or returned integer changes a constant-word claim into a bit-cost claim?
7. What tempting formula fails, and on what smallest legal case?
8. If a random draw removes an item instead of returning it, which probabilities change and why?
9. If the caller wants a hard deadline, what is missing from an expected-runtime statement?
10. If a summary script prints a quadratic count quickly, what has it actually measured?

## One-question-at-a-time evidence record

### Question 1

A positive integer is repeatedly floor-divided by two while greater than one. Without code or
notes, trace the input 17. State the invariant, justify the exact stopping count, and explain how
the answer changes when the process instead doubles capacity from one until it covers 17.

**Rahul's answer:** Not attempted yet.

**Correct reasoning:** Record only after Rahul answers.

**First missing step:** Record only after Rahul answers.

**Smallest recovery hint:** Give one only when needed or requested; record the hint used.

**Retry and delayed check:** Not scheduled until the first answer exists.

Ask the next question only after reviewing this answer. Preserve the initial answer and the
specific correction; do not substitute a polished model explanation for the learner's evidence.

## Evidence

| Date / link | Result | What it proves | Remaining limitation |
|---|---|---|---|
| — | Not attempted | No learning evidence yet | Artifact creation and publication do not demonstrate knowledge |

Future entries need a dated attempt or recall artifact, hint level, exact conclusion, and limits.
A successful familiar trace is not automatically a successful unseen or delayed reconstruction.

## Error log update

| Category | Exact failure | Corrective drill | Review interval |
|---|---|---|---|
| — | Not evaluated | Begin the first closed-book question | 1 day after first study |

After an actual error, choose a precise category such as stopping boundary, sum endpoints,
duplicate construction, sample-space weighting, independence, guarantee, or representation
cost. Record the smallest counterexample and one recovery drill. Do not pre-assign a weakness.

## State decision

Recommended state: **Not started**.

Reason: the learning pack exists, but Rahul has not yet produced a prediction, attempt, proof,
or delayed recall. Artifact state remains **Draft**, regardless of branch publication.

Later use the gates in [PROGRESS.md](../../../PROGRESS.md): Learning needs engagement evidence;
Practiced needs required attempts and explained reasoning; Recalled needs successful closed-book
reconstruction after at least one day; Demonstrated needs unseen transfer and a defended argument;
Retained needs later repeated retrieval. An unsuccessful review may justify lowering a state.
Record the exact evidence supporting any change; do not advance problem or project state here.
