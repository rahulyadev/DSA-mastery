<!--
Create for every initialized unit at:
units/{{DOMAIN_SLUG}}/{{UNIT_ID}}-{{UNIT_SLUG}}/practice/README.md
Replace every placeholder with concrete unsolved work.
Provide at least two substantive exercises; titles alone are invalid.
Do not include a complete solution or reveal all hints.
-->

# Practice — {{UNIT_ID}} {{UNIT_TITLE}}

| Field | Value |
|---|---|
| Unit note | [{{UNIT_ID}}](../README.md) |
| Curriculum | [CURRICULUM.md](../../../../CURRICULUM.md#{{UNIT_ANCHOR}}) |
| Problem bank | [PROBLEM_BANK.md](../../../../PROBLEM_BANK.md) |
| Evidence target | E / T / I / P / D / X / R / M |
| Attempt required before solution | Yes |
| Passing scaffold command | `uv run --group dev python -m pytest -q practice/test_examples.py` or unit-specific equivalent |
| Challenge validation command | `uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py` |
| Status | Not attempted |

## Learning questions

1. {{QUESTION_REVEALED_BY_TRACE_OR_MICRO_LAB}}
2. {{QUESTION_REVEALED_BY_IMPLEMENTATION_OR_DEBUGGING}}

## Cycle

```text
predict → trace → implement → run → observe → explain → optimize → vary → recall
```

## File and test separation

- `micro_lab.py` or `trace_lab.py` is runnable and reveals state without solving the learner challenge.
- `starter.py` remains intentionally incomplete when implementation evidence is required.
- `test_examples.py` covers only provided trace/scaffold behavior and must pass.
- `test_challenge.py` specifies the learner contract. During initialization validate syntax and collection only; do not claim it passes.
- Do not create `solution.py`, `answer.py`, or a complete solution section before Rahul closes the exercise.

## Exercise index

| Exercise ID | Type | Difficulty | Objective | Files | Status |
|---|---|---:|---|---|---|
| `{{UNIT_ID}}-P01` | Trace / Debug | 1–5 | {{CONCRETE_OBJECTIVE_1}} | `micro_lab.py` | Not attempted |
| `{{UNIT_ID}}-P02` | Implement / Compare / Optimize | 1–5 | {{CONCRETE_OBJECTIVE_2}} | `starter.py`, `test_challenge.py` | Not attempted |

## {{UNIT_ID}}-P01 — {{TRACE_OR_DEBUG_TITLE}}

### Task

{{CONCRETE_TASK_DESCRIPTION_WITH_INPUT_STATE_STEPS_AND_REQUIRED_OUTPUT_OR_EXPLANATION}}

### Constraints and expected behavior

- Input or initial state: {{EXACT_SMALL_INPUT_OR_STATE}}
- Required observation or output: {{EXACT_OBSERVABLE_RESULT}}
- Performance target: {{TARGET_OR_NOT_APPLICABLE_WITH_REASON}}

### Required edge cases

- {{EDGE_CASE_1_AND_EXPECTED_BEHAVIOR}}
- {{EDGE_CASE_2_AND_EXPECTED_BEHAVIOR}}

### Before running

Record the predicted state at each step, the invariant, the first point where a faulty implementation diverges, and the expected complexity.

### Acceptance criteria

- [ ] The trace is predicted before execution.
- [ ] Every state variable is explained.
- [ ] The invariant is checked at each transition.
- [ ] The smallest failing case is identified.
- [ ] Complexity and Python-specific costs are stated.

### Progressive hints

#### Hint 1

Locked until Rahul requests it.

#### Hint 2

Locked until Rahul has made another attempt.

#### Hint 3

Locked until Rahul has explained the remaining gap.

## {{UNIT_ID}}-P02 — {{IMPLEMENT_COMPARE_OR_OPTIMIZE_TITLE}}

### Task

{{CONCRETE_UNSOLVED_IMPLEMENTATION_OR_REFACTORING_TASK_WITHOUT_THE_KEY_SOLUTION_STEP}}

### Constraints and expected behavior

- Input contract: {{EXACT_INPUT_CONTRACT}}
- Output contract: {{EXACT_OUTPUT_CONTRACT}}
- Performance target: {{REQUIRED_TIME_AND_SPACE_BOUND}}

### Required edge cases

- {{EDGE_CASE_3_AND_EXPECTED_BEHAVIOR}}
- {{EDGE_CASE_4_AND_EXPECTED_BEHAVIOR}}

### Before coding

- Brute force:
- Exact bottleneck:
- Candidate patterns:
- Rejected alternatives:
- Invariant:
- Planned time and auxiliary/output/stack space:
- One adversarial dry-run:

### Acceptance criteria

- [ ] The original attempt is preserved.
- [ ] Passing scaffold/example tests remain green.
- [ ] Challenge tests collect before implementation.
- [ ] The learner implementation satisfies the challenge after a genuine attempt.
- [ ] Correctness, complexity, and edge cases are explained.
- [ ] A changed-constraint variation is addressed.

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

A comparison solution may be added only after Rahul explicitly closes the exercise, and it must not replace the preserved attempt.
