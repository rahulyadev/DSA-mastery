<!--
Create at units/{{DOMAIN_SLUG}}/{{UNIT_ID}}-{{UNIT_SLUG}}/experiments/{{EXPERIMENT_ID}}-{{SLUG}}/README.md when X is required, (X) materially helps, or runtime observation is central.
Replace every placeholder. Never invent observed output.
-->

# {{EXPERIMENT_ID}} — {{TITLE}}

| Field | Value |
|---|---|
| Owning unit | [{{UNIT_ID}}](../../README.md) |
| Curriculum | [CURRICULUM.md](../../../../../CURRICULUM.md#{{UNIT_ANCHOR}}) |
| Question | {{PRECISE_QUESTION}} |
| Scope | Algorithm / Python / CPython / Platform / Benchmark |
| Runnable script | `experiment.py` |
| Status | Planned / Run / Interpreted / Reproduced |

## Why observation is necessary

{{WHAT_PROSE_OR_A_STATIC_EXAMPLE_CANNOT_REVEAL_RELIABLY}}

## Hypothesis

> {{EXPECTED_RESULT_AND_REASON}}

## Environment

```text
Date:
Operating system:
Architecture:
Python version:
Implementation:
Dependencies:
Input distribution:
Trial count if benchmark:
```

## Controls and measured variables

- Controlled: {{CONTROLLED_FACTORS}}
- Changed: {{INDEPENDENT_VARIABLE}}
- Measured: {{OBSERVABLE_RESULT}}

## Reproduction command

```bash
{{COMMAND}}
```

## Predicted output

```text
{{PREDICTION_WRITTEN_BEFORE_EXECUTION}}
```

## Observed output

Add only after execution. Until then write `Not run yet`; do not fabricate output.

```text
{{ACTUAL_OUTPUT_OR_NOT_RUN_YET}}
```

## Visual interpretation

```text
{{TRACE_OR_TABLE}}
```

### How to read this visual

{{GUIDE}}

### Key insight

{{INSIGHT}}

### Simplification or limitation

{{LIMITATION}}

## Interpretation

1. What the output directly shows: {{DIRECT_OBSERVATION}}
2. What can reasonably be inferred: {{SUPPORTED_INFERENCE}}
3. What cannot be inferred: {{UNSUPPORTED_CONCLUSION}}

## Threats to validity

- {{THREAT_1}}
- {{THREAT_2}}

## Sources

List only sources actually read.
