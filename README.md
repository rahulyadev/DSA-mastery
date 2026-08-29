# DSA Mastery

> **Start here:** [Open `START_HERE.md`](START_HERE.md)

An evidence-based Python repository for deriving data-structure and algorithm solutions, recognizing patterns from constraints, proving correctness, calculating honest complexity, avoiding edge cases, and preparing for coding interviews without memorized templates.

## What is included

- [125 canonical learning units](CURRICULUM.md) across 14 domains
- [A symptom and comparison index](PATTERN_INDEX.md)
- [A curated 121-problem bank](PROBLEM_BANK.md) backed by [`data/problems.json`](data/problems.json)
- [Twelve prerequisite-safe learning paths](LEARNING_PATHS.md)
- [An interview reasoning and mock system](INTERVIEW_PLAYBOOK.md)
- [Exact Python Mastery references](PYTHON_REFERENCES.md)
- [Seven milestone projects](PROJECTS.md)
- Evidence-based [progress, error, and recall tracking](PROGRESS.md)
- Just-in-time unit and project folders
- Protected unsolved practice and progressive hints
- Standard-library-only [repository validation](scripts/validate_repo.py)

## Daily commands

```text
Initialize <UNIT-ID>.
Initialize project <PROJECT-ID>.
```

Only the validated initialization commit pushes automatically. Later work stays local until the explicit completion choice.

Run validation:

```bash
python scripts/validate_repo.py
```

Install locked development tools when runnable artifacts exist, then execute extended checks inside the project environment:

```bash
uv sync --group dev
uv run --group dev python scripts/validate_repo.py --self-test
```

## Core learning rule

```text
constraints → examples → brute force → bottleneck → invariant
→ optimized algorithm → correctness → complexity → trace → code → adversarial tests → variation
```

An Accepted submission, generated note, or completed roadmap is not proof of readiness. See [INTERVIEW_PLAYBOOK.md](INTERVIEW_PLAYBOOK.md) for evidence gates. No roadmap guarantees employment or a particular interview result.

## Repository map

| Path | Purpose |
|---|---|
| [`START_HERE.md`](START_HERE.md) | One-time setup and shortest daily workflow |
| [`CURRICULUM.md`](CURRICULUM.md) | Canonical units, prerequisites, classifications, estimates, and anchors |
| [`PATTERN_INDEX.md`](PATTERN_INDEX.md) | Named patterns, symptoms, constraints, and comparisons |
| [`PROBLEM_BANK.md`](PROBLEM_BANK.md) | Human-readable curated problem index |
| [`data/problems.json`](data/problems.json) | Structured problem metadata source of truth |
| [`LEARNING_PATHS.md`](LEARNING_PATHS.md) | Interview, repair, and mastery routes with calculated timings |
| [`INTERVIEW_PLAYBOOK.md`](INTERVIEW_PLAYBOOK.md) | Natural explanation flow, mocks, scoring, and readiness gates |
| [`PYTHON_REFERENCES.md`](PYTHON_REFERENCES.md) | Exact supporting Python Mastery units |
| [`PROGRESS.md`](PROGRESS.md) | Artifact, unit, project, problem, error, and recall evidence |
| [`PROJECTS.md`](PROJECTS.md) | Seven DSA-focused integration projects |
| [`docs/WORKFLOW.md`](docs/WORKFLOW.md) | Detailed Git, Worktree, learning, attempt, and publication rules |
| [`templates/`](templates/unit.md) | Unit, practice, attempt, review, mock, experiment, and project templates |

No `units/`, `projects/`, or `solutions/` directory exists until corresponding work begins. No license has been selected.
