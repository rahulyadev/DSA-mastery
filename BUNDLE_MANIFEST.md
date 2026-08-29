# Bundle Manifest

The ZIP places repository files directly at archive root. It intentionally excludes `.git/`, environments, caches, credentials, transcripts, `LICENSE`, generated `units/`, generated `projects/`, generated `solutions/`, and problem attempts.

## Inventory

| Path | Purpose |
|---|---|
| `.gitignore` | Repository hygiene exclusions |
| `.python-version` | Verified CPython patch pin |
| `AGENTS.md` | Lean durable Codex contract |
| `BUNDLE_MANIFEST.md` | Archive inventory and purpose |
| `CURRICULUM.md` | Canonical unit catalog |
| `INTERVIEW_PLAYBOOK.md` | Reasoning, mocks, scoring, readiness |
| `LEARNING_PATHS.md` | Calculated recommended paths |
| `NOTEBOOKLM.md` | Short NotebookLM pointer |
| `PATTERN_INDEX.md` | Pattern, symptom, and comparison navigation |
| `PROBLEM_BANK.md` | Human problem index |
| `PROGRESS.md` | Evidence and state tracker |
| `PROJECTS.md` | Milestone project catalog |
| `PYTHON_REFERENCES.md` | Python Mastery links |
| `README.md` | Repository overview |
| `START_HERE.md` | Bootstrap and daily use |
| `data/problems.json` | Machine-readable problem metadata |
| `docs/COPYRIGHT_AND_LICENSE.md` | Rights and license decision policy |
| `docs/LEETCODE_REFERENCE_POLICY.md` | Problem metadata and copyright rules |
| `docs/NOTEBOOKLM.md` | NotebookLM workflow |
| `docs/SOURCE_AND_VERSION_POLICY.md` | Source and Python version policy |
| `docs/WORKFLOW.md` | Detailed learning and Git procedures |
| `pyproject.toml` | Tool and dependency configuration |
| `scripts/validate_repo.py` | Repository/archive validator |
| `templates/experiment.md` | Runtime/performance experiment template |
| `templates/mock_interview.md` | Mock record template |
| `templates/practice.md` | Unsolved unit practice template |
| `templates/problem_attempt.md` | Problem-attempt record |
| `templates/project.md` | Project template |
| `templates/review.md` | Closed-book unit review |
| `templates/unit.md` | Integrated unit note |
| `uv.lock` | Locked development dependencies |

## Canonical counts

| Item | Count |
|---|---:|
| Domains | 14 |
| Learning units | 125 |
| Learning paths | 12 |
| Milestone projects | 7 |
| Curated problems | 121 |
| Mandatory / optional / stretch | 71 / 41 / 9 |

Validate with:

```bash
python scripts/validate_repo.py
```
