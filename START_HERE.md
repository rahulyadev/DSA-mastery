# Start Here

This repository has a one-time setup workflow, then a simple daily DSA workflow.

## One-time bootstrap: use Local

1. Extract `dsa-mastery-bootstrap.zip` directly into the cloned repository root.
2. Open the first Codex chat using the **Local** checkout.
3. Paste:

```text
Initialize the DSA Mastery repository bootstrap locally.

Read AGENTS.md and START_HERE.md. Inspect Git status and verify that the extracted curriculum, pattern index, problem bank, learning paths, Python references, progress tracker, projects, templates, configuration, links, and Git workflow are valid.

Create or resume the local branch setup/dsa-mastery-bootstrap, run python scripts/validate_repo.py, commit only the validated bootstrap files, and report the validation results and commit.

Do not push, open a pull request, merge, initialize a unit, or initialize a project. Give me the exact publication prompt when the local bootstrap is ready.
```

4. Review locally, then publish only with:

```text
Publish the validated DSA Mastery bootstrap.

Push setup/dsa-mastery-bootstrap, create a pull request into main, run validation, merge after checks pass, preferably using a squash merge, and synchronize local main.

Never force-push or bypass failed checks. Stop if authentication, conflicts, branch protection, or unrelated changes require my action.
```

Do not initialize units or projects until the validated baseline is on `main`.

## Daily learning: one pinned Worktree per unit

1. Choose a route in [LEARNING_PATHS.md](LEARNING_PATHS.md).
2. Use the permanent helper chat to find the exact unit.
3. Open a new Codex **Worktree** chat for a new unit.
4. Say only:

```text
Initialize <UNIT-ID>.
```

Example:

```text
Initialize DSA-SEQ-060.
```

A new clean Worktree may start at detached `HEAD`; that is normal. Codex refreshes `origin/main` and creates the exact new branch from it when the selected commit can safely fast-forward. It does not need to rewrite or switch local `main`.

When this same chat already owns exactly `topic/<UNIT-ID>`, rerun the same command to resume or repair it even if `main` has advanced. Do not open another Worktree for the same branch. If this Worktree owns another topic or project, use its original pinned chat or open a new Worktree for the new ID.

A complete initialization creates:

- a substantive `README.md` with the full teaching pack and visual trace;
- concrete unsolved exercises in `practice/README.md`;
- `REVIEW.md` with closed-book and delayed-recall questions;
- a runnable micro-lab or trace exercise for every Core or Professional unit;
- starter code and separated scaffold/challenge tests when implementation is required;
- a focused experiment when required or genuinely useful.

Codex runs live-repository validation, relevant code, and the appropriate tests, commits, and safely pushes only the current initialization or repair commit. It never opens a pull request or merges during initialization. Rerunning initialization preserves learner work and makes no commit when the pack is already complete.

Continue naturally:

```text
Teach me the next concept visually.
Trace this using a tiny example.
Give me one problem without revealing the pattern.
Give me the smallest hint.
Review my approach before I code.
Find the exact invariant I am missing.
Review my complexity analysis.
Test my solution against adversarial cases.
Make me explain this like an interview.
Give me a variation that breaks my current approach.
Schedule this for recall.
```

Later learning changes stay local until completion.

Keep them local:

```text
I completed <UNIT-ID>. Keep any new changes local and do not push or merge.
```

Or publish and merge:

```text
I completed <UNIT-ID>. Finalize it, push the latest changes, and merge the topic branch into main.
```

## Projects

Open a new project Worktree and say:

```text
Initialize project <PROJECT-ID>.
```

If the same pinned Worktree already owns the exact project branch, rerunning the command resumes or repairs it. A Worktree occupied by another unit or project must not be repurposed.

Complete locally:

```text
I completed project <PROJECT-ID>. Keep any new changes local and do not push or merge.
```

Publish and merge:

```text
I completed project <PROJECT-ID>. Finalize it, push the latest changes, and merge the project branch into main.
```

If completion omits the choice, Codex asks only:

```text
Should I keep the latest changes local, or push them and merge the branch into main?
```

## Validation commands

Ordinary repository validation uses the Python standard library and does not require pytest. It auto-detects an installed/live repository when `units/` or `projects/` exists:

```bash
python scripts/validate_repo.py
```

In a normal Local checkout, working validation ignores the repository-root `.git/` directory. In a linked Worktree, it ignores the repository-root `.git` file. Bootstrap and live profiles also prune the narrow local-development allowlist: root `.venv/`, `venv/`, `env/`, or `ENV/`; `__pycache__/`; `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.hypothesis/`, `htmlcov/`; bytecode; and ordinary coverage output. These paths are neither scanned nor counted. `.env` files, credentials, secrets, `private/`, `tokens/`, and arbitrary hidden files are not ignored. Archive validation remains strict and rejects Git metadata, local development artifacts, generated units/projects/attempts/solutions, and private content.

Extended validator tests and full final-report verification rerun pytest-backed fixtures. Install the locked development group first:

```bash
uv sync --group dev
uv run --group dev python scripts/validate_repo.py --self-test
```

Full report verification compares the saved mutation and fixture tests:

```bash
uv run --group dev python scripts/validate_repo.py \
  --verify-report <report.json> \
  --archive dsa-mastery-bootstrap.zip
```

A deliberate hash/content/statistics-only verification that does not rerun those pytest-backed tests is available as:

```bash
python scripts/validate_repo.py \
  --verify-report <report.json> \
  --archive <downloaded-copy.zip> \
  --skip-self-test-comparison
```

See [docs/WORKFLOW.md](docs/WORKFLOW.md) for the full branch matrix, validation profiles, idempotent repair rules, test separation, and publication safety.
