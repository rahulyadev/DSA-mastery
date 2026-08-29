<!-- Create a mock record only when a mock starts. Do not expose hidden labels before the postmortem. -->

# Mock Interview — {{YYYY_MM_DD}}

| Field | Value |
|---|---|
| Duration | {{MINUTES}} minutes |
| Problem reference | {{REFERENCE_OR_ORIGINAL_PROMPT}} |
| Pattern hidden before attempt | Yes |
| Target complexity hidden before attempt | Yes |
| Hints used | {{COUNT_AND_TEXT}} |
| Result | Incomplete / Recovered / Correct / Strong |

## Interview record

Ask one question at a time and wait.

1. Restatement and clarifications:
2. Constraints and example:
3. Brute force and bottleneck:
4. Candidate approaches and rejected alternatives:
5. Invariant and correctness:
6. Complexity:
7. Code plan and implementation:
8. Dry-run and adversarial tests:
9. Changed-constraint follow-up:

## Scoring

Score each dimension separately from 0 to 4.

| Dimension | Score | Evidence | Exact next improvement |
|---|---:|---|---|
| Understanding |  |  |  |
| Approach selection |  |  |  |
| Correctness reasoning |  |  |  |
| Complexity |  |  |  |
| Code quality |  |  |  |
| Testing |  |  |  |
| Communication |  |  |  |
| Changed-constraint response |  |  |  |

## Postmortem

Reveal the canonical pattern, target complexity, invariant, and intended structure only here.

- First missing reasoning step:
- Smallest useful hint:
- Recovery quality:
- Error-log categories:
- Next review:
