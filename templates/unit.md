<!--
Copy to units/{{DOMAIN_SLUG}}/{{UNIT_ID}}-{{UNIT_SLUG}}/README.md.
Initialization must replace every placeholder with complete unit-specific content.
Do not leave template instructions, empty sections, filler, or premature exercise solutions.
The initialized pack must also contain practice/README.md and REVIEW.md.
-->

# {{UNIT_ID}} — {{UNIT_TITLE}}

## Physical Notebook Core

Keep this section compact enough to reconstruct by hand.

### Problem shape or pressure

{{WHAT_REPEATED_WORK_STATE_OR_CONSTRAINT_CREATES_THE_NEED}}

### One-sentence mental model

> {{ONE_SENTENCE_MODEL}}

### Essential visual

```text
{{TINY_RECONSTRUCTABLE_TRACE}}
```

#### How to read this visual

{{READING_ORDER_AND_STATE}}

#### Key insight

{{ONE_CONCLUSION}}

#### Simplification or limitation

{{WHAT_THE_VISUAL_OMITS_OR_ASSUMES}}

### Governing invariant or rules

1. {{INVARIANT_OR_RULE_1}}
2. {{INVARIANT_OR_RULE_2}}
3. {{PROGRESS_OR_TERMINATION_RULE}}

### Minimal pseudocode or Python skeleton

```python
{{MINIMAL_SKELETON_WITHOUT_SOLVING_SEPARATE_PRACTICE}}
```

### Complexity

- Input variables: {{VARIABLES}}
- Time: {{TIME_WITH_REASON}}
- Auxiliary space: {{AUXILIARY_SPACE}}
- Output space: {{OUTPUT_SPACE_IF_RELEVANT}}
- Recursion stack: {{STACK_SPACE_IF_RELEVANT}}
- Important Python cost: {{PYTHON_COST}}

### Recognition cues and anti-cues

- Signal: {{SIGNAL}}
- Constraint signal: {{CONSTRAINT_SIGNAL}}
- Anti-signal: {{WHEN_THIS_PATTERN_IS_WRONG}}

### Important comparison

{{PATTERN_A}} versus {{PATTERN_B}}: {{SELECTION_RULE}}

### Common failure

{{BUG_OR_REASONING_FAILURE_AND_CORRECTION}}

### Recall prompts

1. {{RECALL_1}}
2. {{RECALL_2}}
3. {{RECALL_3}}

| Field | Value |
|---|---|
| Domain | {{DOMAIN_TITLE}} |
| Curriculum | [CURRICULUM.md](../../../CURRICULUM.md#{{UNIT_ANCHOR}}) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Pattern index | [PATTERN_INDEX.md](../../../PATTERN_INDEX.md) |
| Problem bank | [PROBLEM_BANK.md](../../../PROBLEM_BANK.md) |
| Primary outcome | {{OBSERVABLE_OUTCOME}} |
| Hard prerequisites | {{FULL_IDS_OR_NONE}} |
| Soft prerequisites | {{FULL_IDS_OR_NONE}} |
| Priority | Core / Professional / Advanced / Reference |
| Interview frequency | High / Medium / Low |
| Practical relevance | High / Medium / Low |
| Python relevance | High / Medium / Low |
| Difficulty | 1 / 2 / 3 / 4 / 5 |
| Depth | D1 / D2 / D3 / D4 |
| Scope | {{SCOPES}} |
| Size | S / M / L / XL |
| Evidence | E / T / I / P / D / X / (X) / R / M |
| Artifact state | Draft |
| Canonical Python | 3.14 |
| Interview compatibility | 3.11 |

## 1. Learning outcomes and evidence

After this unit Rahul should be able to:

1. {{CAPABILITY_1}}
2. {{CAPABILITY_2}}
3. {{CAPABILITY_3}}

Required evidence:

- {{TRACE_OR_EXPLANATION_EVIDENCE}}
- {{IMPLEMENTATION_OR_DEBUG_EVIDENCE}}
- {{PROOF_COMPLEXITY_RECALL_OR_TRANSFER_EVIDENCE}}

## 2. Prerequisite bridge

Remove this section when no bridge is required. Otherwise state the missing unit and only the smallest correct model needed to proceed.

| Type | Unit | Why it matters | Minimum bridge |
|---|---|---|---|
| Hard / Soft | `{{PREREQUISITE_ID}}` | {{REASON}} | {{MINIMUM_CORRECT_MODEL}} |

A bridge does not replace full study.

## 3. Intuition and problem shape

{{SIMPLE_EXPLANATION_CONNECTED_TO_CONSTRAINTS_AND_REPEATED_WORK}}

## 4. Brute force and bottleneck

### Simplest correct baseline

```python
{{SMALL_BRUTE_FORCE_EXAMPLE}}
```

### Exact bottleneck

{{DOMINANT_REPEATED_OPERATION_AND_COST}}

## 5. Derivation and invariant

{{DERIVATION_FROM_BOTTLENECK_TO_STATE_AND_INVARIANT}}

## 6. Detailed visual trace

### {{VISUAL_TITLE}}

```text
{{T0_TO_TN_TRACE}}
```

#### How to read this visual

{{READING_GUIDE}}

#### Key insight

{{KEY_INSIGHT}}

#### Simplification or limitation

{{LIMITATION}}

## 7. Mechanics and state variables

| State variable | Meaning | Update rule | Why it is sufficient |
|---|---|---|---|
| `{{NAME}}` | {{MEANING}} | {{UPDATE}} | {{JUSTIFICATION}} |

## 8. Correctness reasoning

- **Initialization:** {{WHY_TRUE_BEFORE_WORK}}
- **Preservation:** {{WHY_EACH_STEP_MAINTAINS_INVARIANT}}
- **Progress and termination:** {{WHY_IT_FINISHES}}
- **Completeness:** {{WHY_ALL_NECESSARY_CANDIDATES_ARE_COVERED}}
- **Safe exclusion:** {{WHY_OTHERS_CAN_BE_IGNORED}}
- **Final-state argument:** {{WHY_THE_RESULT_FOLLOWS}}

## 9. Complexity derivation

{{INPUT_VARIABLES_DOMINANT_OPERATIONS_TIME_AUXILIARY_OUTPUT_STACK_AND_PYTHON_COSTS}}

## 10. Implementations

### Generic pseudocode

```text
{{PSEUDOCODE}}
```

### Idiomatic Python

```python
{{CLEAR_INTERVIEW_COMPATIBLE_IMPLEMENTATION_OR_TRACE_HELPER}}
```

### Python 3.11 compatibility

{{DIFFERENCE_OR_NOT_APPLICABLE}}

### First-principles versus standard-library choice

{{EDUCATIONAL_IMPLEMENTATION_AND_NORMAL_INTERVIEW_CHOICE}}

## 11. Edge-case matrix

| Dimension | Minimal adversarial case | Expected behavior | Invariant risk |
|---|---|---|---|
| {{DIMENSION}} | {{CASE}} | {{EXPECTED}} | {{RISK}} |

## 12. Comparisons and anti-signals

| Candidate | Use when | Reject when | Evidence in the problem |
|---|---|---|---|
| {{PATTERN}} | {{USE}} | {{REJECT}} | {{SIGNAL}} |

## 13. Common bugs and debugging

| Failure | Symptom | Smallest counterexample | Correction |
|---|---|---|---|
| {{FAILURE}} | {{SYMPTOM}} | {{CASE}} | {{FIX}} |

## 14. Practice ladder

1. concept micro-drill;
2. hand-worked trace;
3. guided problem;
4. labeled independent problem;
5. changed-constraint variation;
6. confused-pattern comparison;
7. mixed unlabeled problem;
8. timed interview problem;
9. delayed re-solve;
10. unseen transfer problem.

Link only canonical or intentional secondary problems. Keep mixed/mock labels hidden before the attempt.

## 15. Interview questions, traps, and follow-ups

### Recognition and approach questions

1. {{SCENARIO_RECOGNITION_QUESTION}}
2. {{BRUTE_FORCE_AND_BOTTLENECK_QUESTION}}

### Invariant and correctness questions

1. {{INVARIANT_QUESTION}}
2. {{CORRECTNESS_OR_TERMINATION_QUESTION}}

### Complexity questions

1. {{TIME_COMPLEXITY_QUESTION}}
2. {{SPACE_OR_PYTHON_COST_QUESTION}}

### Changed-constraint follow-ups

1. {{CHANGED_CONSTRAINT_QUESTION}}
2. {{STREAMING_MEMORY_DUPLICATE_OR_DYNAMIC_UPDATE_QUESTION}}

### Common traps and weak-answer repairs

- Trap: {{COMMON_INTERVIEW_TRAP_AND_WHY_IT_FAILS}}
- Weak answer: {{WEAK_ANSWER}} — repair it by explaining {{MISSING_REASONING}}.

## 16. Explanation exercises

1. Explain the approach in under two minutes without naming the pattern first.
2. Defend the invariant using one minimal counterexample.
3. Explain why a plausible alternative is rejected.
4. Recalculate complexity after {{REQUIREMENT_CHANGE}}.

## 17. Experiment decision

Decision: {{CREATED_WITH_RELATIVE_LINK_OR_NOT_CREATED_WITH_SPECIFIC_REASON}}

An `X` unit requires a real experiment. For `(X)`, explain specifically why observation adds value now or why it is deferred.

## 18. Vocabulary and professional English

Select two to five genuinely useful words only.

### {{WORD}}

| Item | Content |
|---|---|
| Pronunciation | {{PRONUNCIATION}} |
| Simple English meaning | {{PLAIN_MEANING}} |
| Hindi cue | {{OPTIONAL_HINDI_CUE_OR_DASH}} |
| Meaning here | {{DSA_CONTEXT}} |

Examples:

1. {{GENERAL_EXAMPLE_1}}
2. {{GENERAL_EXAMPLE_2}}
3. {{GENERAL_EXAMPLE_3}}
4. **Interview:** {{INTERVIEW_EXAMPLE}}
5. **Engineering discussion:** {{ENGINEERING_EXAMPLE}}

## 19. Python Mastery references

Use exact absolute links from `PYTHON_REFERENCES.md`; do not duplicate full Python lessons.

## 20. Authoritative sources

Keep citations near subtle claims and list only sources actually read. Do not copy statements, editorials, or textbook prose.

## 21. Open uncertainties

Record genuine uncertainty, changing platform metadata, or an unresolved source conflict. Remove when empty.
