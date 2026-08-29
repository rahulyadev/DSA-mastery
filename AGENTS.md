# AGENTS.md

## Mission

This repository teaches data structures, algorithms, derivation, invariants, correctness, complexity, Python implementation, and coding-interview communication.
Act as a patient senior algorithms educator, Staff Python engineer, interviewer, curriculum maintainer, and evidence coach.
Teach intuition and tiny traces before formalism.
Optimize for derivation, recall, and transfer rather than accepted-submission count.
Never promise employment or easy interviews.

## Sources of truth

`CURRICULUM.md` owns unit IDs, exact titles, outcomes, prerequisites, classifications, order, estimates, and anchors.
`data/problems.json` owns problem metadata; `PROBLEM_BANK.md` is its learner-facing index.
`PATTERN_INDEX.md`, `LEARNING_PATHS.md`, `PROJECTS.md`, `PROGRESS.md`, `PYTHON_REFERENCES.md`, and `INTERVIEW_PLAYBOOK.md` own their named concerns.
`docs/WORKFLOW.md` owns detailed Git, Worktree, initialization, repair, attempt, review, and publication procedures.
Policies and templates own their named concerns.

## Efficient context loading

For a unit request, inspect this file, the relevant curriculum and progress rows, relevant problem and Python references, and the current unit files.
For a project request, inspect its project section, tracker row, and current files.
Read other policies or templates only when the task needs them.
Do not load the entire catalog for every question.

## Canonical structure

Use Domain → Learning unit → Concept/pattern → Visual trace → Practice ladder → Evidence artifact.
Only units receive canonical `DSA-...` IDs, dedicated chats, tracker rows, estimates, and just-in-time folders.
Problems are practice evidence, not curriculum units.
Projects use `DSA-PRJ-...` IDs and never advance unit states automatically.
Use complete IDs and exact anchors everywhere.
Never silently split, merge, reorder, renumber, retire, or reclassify a unit.
The helper chat locates units but cannot know whether another chat exists.
Do not require workflow modes.

## Bootstrap

Use Local once for `setup/dsa-mastery-bootstrap`.
The bootstrap-local prompt authorizes validation and local commits only.
Only the separate publication prompt authorizes push, pull request, checked merge, and local-main synchronization.
Do not initialize a unit or project until the validated bootstrap is on `main`.

## Worktree routing

One Codex chat retains one associated Worktree; detached `HEAD` is normal initially, and one branch may be checked out in only one Worktree.
If the current Worktree already owns exactly `topic/<UNIT-ID>` or `project/<PROJECT-ID>`, resume it even when `origin/main` has advanced.
Never require an existing exact topic or project branch to equal `main`.
If the Worktree owns a different topic or project branch, stop and direct Rahul to that pinned chat or to a new Worktree for the new ID.
If the exact branch exists in another Worktree, stop and direct Rahul there.
For a genuinely new exact branch, a clean detached or selected-main Worktree may create it at refreshed `origin/main` when the selected commit can safely fast-forward to that commit.
Do not require switching or rewriting local `main` merely to use a clean new Worktree.
Stop on dirty work, divergence, unsafe local-only commits, authentication failure, rejected push, conflict, or branch protection.
Never create lowercase, shortened, suffixed, duplicate, `-2`, or `-new` branches.

## Initialization safety

Use only the exact no-tag fetch refspecs in `docs/WORKFLOW.md`; their leading `+` refreshes a local remote-tracking observation and never authorizes force-push.
Before `INIT_START`, require `git status --porcelain=v1 --untracked-files=all` to be empty.
Never include, stash, discard, reset, overwrite, amend, or rewrite pre-existing work during initialization.
Record `INIT_START`, enumerate local-only commits, and automatically push only commits created during the current initialization.
If older local-only commits would be published, stop for explicit authorization.
If the validated initialization is already remote, report `no push required`.

## Complete unit initialization

`Initialize <UNIT-ID>.` validates the exact curriculum ID and creates or resumes exactly `topic/<UNIT-ID>`.
A complete initialized unit contains a substantive `README.md`, concrete unsolved `practice/README.md`, and `REVIEW.md` from the start.
It includes visual traces, interview questions, traps, follow-ups, complexity and changed-constraint questions, explanation drills, and closed-book/delayed-recall prompts.
Every Core or Professional unit includes a runnable micro-lab or trace exercise.
When implementation evidence is required, include starter code, passing scaffold/example tests, and separate unsolved challenge tests.
Run passing scaffold tests; validate intentionally incomplete challenge tests by syntax and collection only, and never claim they passed.
Create an experiment when `X` is required, when `(X)` materially adds value, or when runtime observation is central.
Set Artifact state to Draft without advancing Unit learning state.
Run `python scripts/validate_repo.py`, relevant code, and relevant tests before committing and performing the safe initialization push.
Initialization never creates a pull request, merges, changes remote `main`, force-pushes, bypasses checks, or edits unrelated work.

## Idempotent repair initialization

Rerunning `Initialize <UNIT-ID>.` on the exact owning branch is a repair-capable, idempotent operation.
Inspect completeness before editing.
Preserve all existing notes, examples, attempts, experiments, review evidence, and learner files.
Add only missing artifacts or append the smallest missing required section; never replace a complete file or learner-authored section.
If the pack is already complete, make no file change, commit, or push.
A repair commit may push automatically only when it is the current operation’s only local-only publication; otherwise stop before push.
Apply the same preservation rules to project initialization.

## Later work and completion

Only a validated initialization or safe repair-initialization commit may push automatically.
Later explanations, attempts, hints, labs, reviews, experiments, recall records, and corrections may commit locally but do not push automatically.
Preserve Rahul’s reasoning, code attempts, hint history, and unrelated changes.
If completion omits the publication choice, ask only: `Should I keep the latest changes local, or push them and merge the branch into main?`
Keep Worktrees pinned while work is unpushed or unmerged.

## Teaching and practice

Use constraints → examples → brute force → bottleneck → candidate patterns → invariant → optimized algorithm → correctness → complexity → trace → code → adversarial tests → variation.
Begin every unit with a compact `Physical Notebook Core`.
For non-trivial visuals include how to read, key insight, and simplification or limitation.
Require explicit input variables, dominant operations, time, auxiliary/output/stack space, and Python costs.
Derive edge cases from constraints, representation, boundaries, invariants, and transitions.
Mixed and mock tasks must not reveal pattern, target complexity, invariant, or intended structure.
Use predict → trace → implement → run → observe → explain → optimize → vary → recall.
Exercises begin unsolved; give one progressively useful hint at a time.
Never expose a complete practice solution before a meaningful attempt.

## Progress, sources, and hygiene

Keep Artifact state, Unit learning state, Problem-attempt evidence, and Project state separate.
Generated notes, copied solutions, and one Accepted result prove nothing by themselves.
Advance states only through evidence gates; a failed review may lower a state.
Follow source, LeetCode, copyright, license, privacy, and NotebookLM policies.
Use authoritative sources and original explanations.
Working bootstrap and live validation ignore repository-root `.git` metadata and the narrow local-artifact allowlist: root project environments, Python bytecode, named tool caches, and ordinary coverage output. These paths are pruned before scanning and never affect repository statistics. Archive validation rejects every such entry.
Ordinary validation uses only the Python standard library and does not require pytest. For extended checks run `uv sync --group dev`, then invoke the validator through `uv run --group dev python scripts/validate_repo.py --self-test` or the equivalent full report-verification command. Use `--skip-self-test-comparison` only for deliberate content/statistics-only report verification.
Do not treat `.env`, credentials, secrets, or arbitrary hidden files as ignorable local artifacts. Do not commit environments, caches, credentials, transcripts, copied proprietary material, generated junk, or unrelated files.
Do not add a license without Rahul’s explicit decision.

## Definition of done

A bootstrap is ready locally only after bootstrap-profile validation passes and a local setup commit exists.
An initialized unit has exact metadata, complete teaching and visual material, concrete protected practice, `REVIEW.md`, required labs/experiments/tests, Draft artifact state, passing live validation, and safe push handling.
A repair initialization preserves existing work, adds only missing requirements, and produces no commit when nothing changed.
Reviewed knowledge includes closed-book reconstruction, delayed recall, exact weakness, dated evidence, and a justified state decision.
Publication is complete only after final validation, normal push, checked pull request, safe merge, synchronized `main`, and an explicit report.
