<!-- Create only at projects/{{PROJECT_ID}}-{{PROJECT_SLUG}}/README.md after `Initialize project {{PROJECT_ID}}.` -->

# {{PROJECT_ID}} — {{PROJECT_TITLE}}

| Field | Value |
|---|---|
| Project catalog | [PROJECTS.md](../../PROJECTS.md#{{PROJECT_ANCHOR}}) |
| Progress | [PROGRESS.md](../../PROGRESS.md) |
| Required prerequisites | {{FULL_UNIT_IDS}} |
| Recommended prerequisites | {{FULL_UNIT_IDS_OR_NONE}} |
| Structures and algorithms | {{INTEGRATION}} |
| Python baseline | 3.14; maintain 3.11 interview compatibility |
| Project state | Active |

## Purpose and interview value

{{PURPOSE}}

## Scope

### Included

- {{ITEM}}

### Excluded

- web UI and framework curriculum;
- production cloud or distributed-system expansion;
- unrelated architecture work;
- copied platform statements or solutions.

## Architecture or state-flow visual

```text
{{COMPONENT_OR_STATE_FLOW}}
```

### How to read this visual

{{GUIDE}}

### Key insight

{{INSIGHT}}

### Simplification or limitation

{{LIMITATION}}

## Staged requirements

1. Build the smallest correct baseline.
2. Add a requirement that exposes an invariant or complexity pressure.
3. Add at least two tiny visual traces.
4. Seed and repair at least two defects.
5. Compare and reject an alternative.
6. Add adversarial/property-based tests where useful.
7. Complete a senior interview walkthrough.

## Complexity targets

| Operation or stage | Input variables | Target time | Target auxiliary space | Reason |
|---|---|---:|---:|---|
| {{OPERATION}} | {{VARIABLES}} | {{TIME}} | {{SPACE}} | {{REASON}} |

## Tests and oracles

- deterministic unit tests;
- integration tests for staged workflows;
- brute-force reference or differential testing when feasible;
- seeded-regression tests;
- properties and generated adversarial cases where useful.

## Correctness questions

1. What representation invariant must always hold?
2. Why does each update preserve it?
3. Which candidates are considered or discarded safely?
4. What changed constraint invalidates the design?

## Definition of done

- [ ] Required behavior and stages are complete.
- [ ] Tests pass and actual commands are recorded.
- [ ] Seeded bugs and corrections are explained.
- [ ] Invariants and complexity are justified.
- [ ] Visuals are reconstructable by hand.
- [ ] Rejected alternatives are defended.
- [ ] Final walkthrough handles a changed constraint.
- [ ] Project evidence is linked without automatically changing unit states.
