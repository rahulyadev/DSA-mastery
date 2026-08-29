<!--
Create at initialization as units/{{DOMAIN_SLUG}}/{{UNIT_ID}}-{{UNIT_SLUG}}/REVIEW.md.
Replace every placeholder with concrete questions, but do not pre-fill Rahul's answers.
-->

# Review Record — {{UNIT_ID}} {{UNIT_TITLE}}

| Field | Value |
|---|---|
| Unit note | [{{UNIT_ID}}](README.md) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Artifact state | Draft / Approved |
| Learning state | Not started / Learning / Practiced / Recalled / Demonstrated / Retained |
| Last evidence | — |
| Next review | 1 day after first study, then adapt |
| Mastery badge | No |
| Strongest area | Not evaluated yet |
| Weakest area | Not evaluated yet |

## Closed-book reconstruction questions

1. {{QUESTION_RECONSTRUCTING_THE_PROBLEM_SHAPE}}
2. {{QUESTION_RECONSTRUCTING_THE_ESSENTIAL_TRACE}}
3. {{QUESTION_STATING_THE_INVARIANT}}
4. {{QUESTION_DERIVING_FROM_BRUTE_FORCE}}
5. {{QUESTION_JUSTIFYING_CORRECTNESS}}
6. {{QUESTION_DERIVING_TIME_AND_SPACE}}
7. {{QUESTION_IDENTIFYING_AN_ANTI_SIGNAL}}
8. {{QUESTION_COMPARING_A_CONFUSED_PATTERN}}

## Delayed-recall questions

### 1-day recall

1. {{SHORT_MODEL_AND_TRACE_QUESTION}}
2. {{BOUNDARY_OR_BUG_QUESTION}}

### 3-day recall

1. {{INVARIANT_RECOVERY_QUESTION}}
2. {{COMPLEXITY_RECOVERY_QUESTION}}

### 7-day recall

1. {{UNSEEN_VARIATION_QUESTION}}
2. {{REJECTED_ALTERNATIVE_QUESTION}}

### 14-day recall

1. {{CHANGED_CONSTRAINT_QUESTION}}
2. {{EXPLANATION_WITHOUT_PATTERN_LABEL_QUESTION}}

### 30-day recall

1. {{TRANSFER_QUESTION}}
2. {{TEACH_BACK_AND_LIMITATION_QUESTION}}

## Interview retrieval

1. How would you recognize this unit's problem shape from constraints alone?
2. What is the simplest correct brute force and its exact bottleneck?
3. Which invariant makes the optimized algorithm safe?
4. Why is the algorithm complete, and what can it safely ignore?
5. What are time, auxiliary, output, and recursion-stack costs?
6. Which Python operation could silently change the complexity?
7. What tempting alternative fails, and on what smallest case?
8. How does the solution change when {{SPECIFIC_REQUIREMENT_CHANGE}}?

## One-question-at-a-time evidence record

### Question 1

{{FIRST_LIVE_REVIEW_QUESTION}}

**Rahul's answer:** Not attempted yet.

**Correct reasoning:** Record only after Rahul answers.

**First missing step:** Record only after Rahul answers.

**Smallest recovery hint:** Give only when needed.

## Evidence

| Link | Result | What it proves | Remaining limitation |
|---|---|---|---|
| — | Not attempted | No learning evidence yet | Initialization alone does not prove learning |

## Error log update

| Category | Exact failure | Corrective drill | Review interval |
|---|---|---|---|
| — | Not evaluated | Complete the first closed-book review | 1 day after first study |

## State decision

Recommended state: **Not started**

Reason tied to the evidence gate: the learning pack exists, but Rahul has not yet produced learning evidence.
