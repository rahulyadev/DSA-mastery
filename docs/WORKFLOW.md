# DSA Mastery Workflow

This document owns the detailed learner, Git, Worktree, initialization, repair, practice, review, validation, and publication procedures.

## 1. Daily operating model

- One permanent curriculum-helper chat finds the correct unit.
- One dedicated Codex Worktree chat owns one learning unit or one project.
- A chat retains its associated Worktree; do not treat a later chat as if it owns an earlier Worktree.
- One Worktree is never created for a single LeetCode problem.
- Unit, project, attempt, visualization, and experiment artifacts are created only when needed.
- After initialization Rahul asks ordinary follow-up questions without selecting a mode.
- Only a validated initialization or repair-initialization commit may push automatically.
- Later learning work stays local until an explicit completion choice.

A focused daily session normally contains:

1. short closed-book recall;
2. one visual reconstruction;
3. one focused problem or micro-lab;
4. one mixed or delayed-review problem;
5. verbal explanation;
6. error-log update;
7. next-review scheduling.

## 2. Permanent curriculum-helper chat

Use:

```text
Find the best DSA curriculum unit for <problem symptom, concept, or confusion>. Return the canonical unit ID, exact title, short reason, prerequisites, commonly confused units, relevant problem references, Python Mastery references, whether the folder exists, and the exact initialization prompt. Do not initialize it unless I ask.
```

The helper may answer natural questions such as:

```text
Which unit teaches sliding window?
When should I use sliding window instead of prefix sum?
What should I study before graph shortest paths?
I keep failing array edge cases. What should I revise?
```

It may inspect repository folders but must not claim to know whether another ChatGPT or Codex conversation exists.

## 3. One-time bootstrap

Use the Local checkout once.

The exact setup branch is:

```text
setup/dsa-mastery-bootstrap
```

The bootstrap-local operation may:

1. read `AGENTS.md` and `START_HERE.md`;
2. inspect Git status safely;
3. create or resume the exact setup branch;
4. run `python scripts/validate_repo.py --profile bootstrap`;
5. review the diff for unexpected, copied, or private content;
6. commit only validated bootstrap files locally.

It never authorizes push, pull request, merge, unit initialization, or project initialization. The separate bootstrap-publication prompt authorizes publication after local review.

Do not initialize a unit or project until the validated bootstrap is merged into `main`.

## 4. Codex Worktrees and initial detached HEAD

Official Codex Worktree use assumes one chat remains associated with its selected Worktree. A newly created Worktree may begin at detached `HEAD`; this is normal. Git itself permits one branch to be checked out in only one Worktree.

Inspect the selected Worktree:

```bash
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git branch --show-current
git worktree list --porcelain
```

Refresh only the local observation of remote `main`:

```bash
git fetch --no-tags origin \
  +refs/heads/main:refs/remotes/origin/main
```

The leading `+` only permits the named remote-tracking ref to reflect rewritten remote history. It does not push, rewrite a remote branch, move local `main`, move the selected branch, or authorize force-push.

## 5. Exact branch names and remote inspection

Unit branch:

```text
topic/<UNIT-ID>
```

Project branch:

```text
project/<PROJECT-ID>
```

Never create lowercase, shortened, suffixed, duplicate, `-2`, or `-new` variants.

Inspect an exact unit branch remotely:

```bash
git ls-remote --exit-code --heads origin refs/heads/topic/<UNIT-ID>

git fetch --no-tags origin \
  +refs/heads/topic/<UNIT-ID>:refs/remotes/origin/topic/<UNIT-ID>
```

Inspect an exact project branch remotely:

```bash
git ls-remote --exit-code --heads origin refs/heads/project/<PROJECT-ID>

git fetch --no-tags origin \
  +refs/heads/project/<PROJECT-ID>:refs/remotes/origin/project/<PROJECT-ID>
```

A missing exact remote branch is normal. It is never permission to invent another branch name.

## 6. Branch routing rules

### 6.1 The current Worktree already owns the exact branch

If `git branch --show-current` returns exactly `topic/<UNIT-ID>` for unit initialization, resume that branch regardless of whether `origin/main` has advanced.

The same rule applies to `project/<PROJECT-ID>`.

Do not require an existing exact topic or project branch to equal local `main` or `origin/main`. The branch contains its own learning history and is expected to differ after initialization.

Refresh and compare its exact remote branch. Stop only for dirty work, branch divergence, unsafe local-only commits, or another explicit blocker.

### 6.2 The current Worktree owns a different topic or project

If the current branch is another `topic/...` or `project/...`, stop.

Tell Rahul to either:

- return to the original pinned chat and Worktree for that branch; or
- open a new Worktree for the new unit or project.

Never switch an occupied learning Worktree to a different topic or project.

### 6.3 The exact branch is checked out in another Worktree

Inspect `git worktree list --porcelain`. If another Worktree owns the exact branch, stop and direct Rahul to the original pinned chat and Worktree.

Git cannot check out one branch in two Worktrees simultaneously. Never work around this by inventing a duplicate branch.

### 6.4 Neither exact local nor remote branch exists

A clean detached Worktree or clean Worktree selected from `main` may create the exact new branch at refreshed `origin/main` when the selected commit is an ancestor of `origin/main` and therefore can safely fast-forward.

Check the ancestry without moving local `main`:

```bash
git merge-base --is-ancestor HEAD refs/remotes/origin/main
```

When it succeeds, create the exact branch directly at the refreshed remote-tracking commit:

```bash
git switch -c topic/<UNIT-ID> refs/remotes/origin/main
```

Use the equivalent project branch command.

This does not require checking out, resetting, or synchronizing local `main`. It does not discard a clean newly created Worktree. If the selected commit is not an ancestor of `origin/main`, stop because moving to the remote baseline is not a simple safe fast-forward.

### 6.5 Exact branch exists locally but is not checked out

If it is not owned by another Worktree, attach this clean Worktree to the exact local branch. Fetch its exact remote observation when present, compare histories, and follow the matrix below.

### 6.6 Exact branch exists only remotely

Fetch the exact ref and create the exact local tracking branch at that commit. Do not recreate it from `main`.

## 7. Complete branch-state decision matrix

When both exact local and remote refs exist, compare them.

For a unit:

```bash
git rev-list --left-right --count \
  refs/heads/topic/<UNIT-ID>...refs/remotes/origin/topic/<UNIT-ID>
```

For a project:

```bash
git rev-list --left-right --count \
  refs/heads/project/<PROJECT-ID>...refs/remotes/origin/project/<PROJECT-ID>
```

The first number is local-only commits; the second is remote-only commits.

| Branch state | Required safe action | Automatic initialization push |
|---|---|---|
| Neither local nor remote exists | From a clean detached/selected-main Worktree whose selected commit is an ancestor of refreshed `origin/main`, create the exact branch at `origin/main`. | Allowed only for commits created during this initialization. |
| Remote only | Fetch the exact ref and create the exact tracking branch at that commit. | No push when the validated initialization is already remote; otherwise only current-operation commits may push. |
| Local only | Resume or attach the exact local branch only when no other Worktree owns it. Preserve every commit. | Stop if a first push would publish any older local-only commit. |
| Local and remote are identical | Resume the exact branch, regardless of later changes on `main`. | No redundant push when the complete initialization is already remote. |
| Local is ahead | Enumerate every local-only commit. | Allowed only when every ahead commit was created after this operation’s `INIT_START`. |
| Remote is ahead | With a clean exact-branch Worktree and zero local-only commits, fast-forward the exact local branch to its remote branch and re-evaluate. | A later current-operation repair commit may push normally. |
| Histories diverged | Stop and request the smallest explicit reconciliation decision. | Never. |
| Exact branch is owned by another Worktree | Stop and direct Rahul to the original pinned chat and Worktree. | Never from the new Worktree. |
| Current Worktree owns another topic/project | Stop and use a new Worktree for the requested ID. | Never. |

Never reset, force, silently rebase, auto-merge divergence, choose one side, or create an alternate branch.

## 8. Clean-Worktree gate

Before recording initialization start, require:

```bash
git status --porcelain=v1 --untracked-files=all
```

It must produce no output.

Any output means pre-existing tracked, staged, or untracked work exists. Stop and ask for an explicit decision. Never include, stash, discard, reset, overwrite, amend, or rewrite that work during initialization.

Only after the exact branch is selected and the Worktree is clean, record:

```bash
git rev-parse HEAD
```

Call the result `INIT_START`.

## 9. Current-operation-only push proof

Before an existing unit-branch push, enumerate local-only commits:

```bash
git log --format='%H %s' --reverse \
  refs/remotes/origin/topic/<UNIT-ID>..refs/heads/topic/<UNIT-ID>
```

For a new unit branch without a remote branch:

```bash
git log --format='%H %s' --reverse \
  refs/remotes/origin/main..refs/heads/topic/<UNIT-ID>
```

Enumerate commits created in this operation:

```bash
git log --format='%H %s' --reverse INIT_START..HEAD
```

Use equivalent project refs.

Automatic push is permitted only when the local-only commit list equals the current-operation commit list exactly. If an older local-only commit would be published, stop and ask for explicit publication authorization.

If the complete validated initialization is already remote and this operation made no repair, report:

```text
no push required
```

First unit push:

```bash
git push --set-upstream origin \
  refs/heads/topic/<UNIT-ID>:refs/heads/topic/<UNIT-ID>
```

Existing unit upstream:

```bash
git push origin \
  refs/heads/topic/<UNIT-ID>:refs/heads/topic/<UNIT-ID>
```

Use equivalent exact project refspecs. Stop on authentication failure, non-fast-forward rejection, branch protection, or uncertain results.

## 10. Complete unit initialization

The exact command is:

```text
Initialize <UNIT-ID>.
```

It authorizes Codex to:

1. validate the complete ID and exact title in `CURRICULUM.md`;
2. inspect the matching progress row, problem metadata, pattern index, and Python references;
3. route the current Worktree using sections 4–9;
4. explain essential missing prerequisites briefly and provide the smallest correct bridge;
5. inspect any existing unit pack before editing;
6. create or repair the canonical unit directory;
7. produce the complete initialized learning pack defined below;
8. update only the matching tracker row and valid links;
9. set Artifact state to `Draft` without advancing Unit learning state;
10. run live validation, code, and appropriate tests;
11. commit only when initialization or repair changed files;
12. prove the publication boundary;
13. normally push only the safe initialization or repair commit;
14. report branch, commit or no-op, files, validation, tests, and push result.

Initialization never creates a pull request, merges, modifies remote `main`, force-pushes, bypasses a failure, or edits another unit.

## 11. Required initialized learning pack

Every initialized unit receives:

```text
units/<domain-slug>/<UNIT-ID>-<unit-slug>/
├── README.md
├── REVIEW.md
└── practice/
    └── README.md
```

### 11.1 `README.md`

It contains complete teaching material rather than template instructions:

- `Physical Notebook Core`;
- simple intuition and problem shape;
- brute force and exact bottleneck;
- invariant and derivation;
- at least one complete visual trace;
- state-variable mechanics;
- correctness reasoning;
- honest complexity derivation;
- generic pseudocode and idiomatic Python where useful;
- Python 3.11 compatibility;
- edge-case matrix;
- comparisons and anti-signals;
- common bugs and counterexamples;
- practice ladder;
- concrete interview questions, traps, follow-ups, complexity questions, changed-constraint questions, and explanation exercises;
- experiment decision;
- Python Mastery references and sources.

### 11.2 `practice/README.md`

It contains at least two concrete unsolved tasks. A task must describe the actual input, required output or observation, constraints, performance target, edge cases, reasoning to record, and acceptance criteria. Exercise titles alone are not practice.

Hints begin locked. Add one hint only after Rahul requests it.

### 11.3 `REVIEW.md`

It exists from initialization and contains concrete questions for:

- closed-book reconstruction;
- delayed recall at 1, 3, 7, 14, and 30 days;
- invariant and correctness recovery;
- complexity explanation;
- changed constraints;
- interview communication;
- error-log and state decision.

Do not pre-fill Rahul’s answers.

### 11.4 Core and Professional micro-lab

Every Core or Professional unit includes a runnable file such as:

```text
practice/micro_lab.py
```

It must reveal the unit’s state or trace and include a runnable `__main__` entry point.

### 11.5 Implementation evidence

When the unit evidence contains `I`, initialize:

```text
practice/starter.py
practice/test_examples.py
practice/test_challenge.py
```

- `starter.py` remains unsolved and may raise `NotImplementedError` at the intended learner boundary.
- `test_examples.py` tests only provided trace/scaffold behavior and must pass.
- `test_challenge.py` defines the unsolved learner contract. Validate its syntax and pytest collection separately; do not run it as a passing initialization check.

Use commands equivalent to:

```bash
uv run --group dev python -m compileall -q <unit-directory>
uv run --group dev python practice/micro_lab.py
uv run --group dev python -m pytest -q practice/test_examples.py
uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py
```

Never claim the intentionally incomplete challenge tests passed.

### 11.6 Experiments

Create an experiment when:

- the evidence includes `X`;
- `(X)` materially adds value;
- runtime observation is central to the unit.

A required experiment contains a precise question, hypothesis, runnable script, command, predicted output, observation section, interpretation, limitations, and source classification.

For `(X)` units without an experiment, `README.md` must contain a specific `Experiment decision` explaining why observation would not add enough value now. Generic “not needed” text is insufficient.

## 12. Idempotent repair initialization

Rerunning `Initialize <UNIT-ID>.` on the exact owning branch must first inspect the existing pack.

Classify each requirement as:

- complete;
- missing;
- present but incomplete;
- learner-authored or evidence-bearing and therefore protected.

Repair rules:

1. Preserve existing notes, examples, attempts, experiments, review evidence, and learner files byte-for-byte unless Rahul explicitly asks for an edit.
2. Create a missing file from its template with complete unit-specific content.
3. For an incomplete canonical file, append or locally insert only the smallest missing required section; do not replace the file.
4. Never replace a learner attempt with an ideal answer.
5. Never delete an experiment because a newer explanation exists.
6. Never reveal a complete exercise solution while repairing scaffolding.
7. Revalidate the whole live repository after repair.
8. If everything was already complete, make no file change, commit, or push.
9. If repair changed files, create a distinct repair-initialization commit.
10. Push that repair commit automatically only when no older local-only commit would also be published.

The same preservation and no-op rules apply to project initialization.

## 13. Practice and solution separation

Use:

```text
predict → trace → implement → run → observe → explain → optimize → vary → recall
```

Never place a complete solution in:

- `practice/README.md` before closure;
- `starter.py`;
- `test_examples.py`;
- comments, filenames, or fixtures that reveal the algorithm.

A later comparison solution may be added only after Rahul closes the exercise and must remain clearly separate from the preserved original attempt.

## 14. Project initialization

The exact command is:

```text
Initialize project <PROJECT-ID>.
```

Validate the ID only in `PROJECTS.md`. Never treat it as a curriculum unit ID.

Apply the same Worktree routing, clean-state, branch matrix, repair, commit-boundary, live-validation, test, and safe-push rules using `project/<PROJECT-ID>`.

Create `projects/<PROJECT-ID>-<project-slug>/README.md` from `templates/project.md`, add only useful starter files, and change only the matching project row from `Planned` to `Active`. Project initialization or completion never automatically changes a unit learning state.

## 15. Later learning and completion

Only the validated initialization or repair-initialization commit pushes automatically.

Later notes, questions, attempts, hints, visualizations, experiments, reviews, recall records, and corrections may be committed locally but must not push automatically.

The remote branch retains the initialized version while newer work may remain in the pinned Worktree.

If Rahul states completion without a publication choice, ask only:

```text
Should I keep the latest changes local, or push them and merge the branch into main?
```

Keep a Worktree pinned while it has unpushed or unmerged work. Archive it only after merge verification and confirmation that no local work remains. Prefer squash merge unless repository policy says otherwise.

## 16. Universal teaching flow

For substantial problems use:

```text
understand constraints
→ construct examples
→ derive brute force
→ identify the bottleneck
→ recognize candidate patterns
→ state the invariant
→ derive the optimized algorithm
→ justify correctness
→ calculate complexity
→ dry-run
→ implement
→ test adversarial cases
→ explain and vary
```

Patterns must arise from constraints, bottlenecks, and invariants rather than memorized labels.

## 17. Review, spacing, and error log

Use the adaptive schedule:

```text
1 day → 3 days → 7 days → 14 days → 30 days
```

Shorten the interval after a pattern hint, invariant gap, repeated boundary error, complexity error, proof gap, or copied implementation structure.

Track error categories such as interpretation, constraints, pattern recognition, invariant, proof, complexity, implementation, edge cases, Python behavior, communication, and time management.

## 18. Validation profiles

The ordinary command auto-detects the profile:

```bash
python scripts/validate_repo.py
```

- With no `units/` or `projects/`, it uses the bootstrap profile.
- With installed `units/` or `projects/`, it uses the live profile.

Explicit commands are:

```bash
python scripts/validate_repo.py --profile bootstrap
python scripts/validate_repo.py --profile live
```

Working bootstrap validation permits and completely ignores the repository-root Git metadata used by a real checkout:

- a normal clone's root `.git/` directory;
- a linked Worktree's root `.git` file.

The validator must prune that directory or skip that file before content scanning. Git internals must not affect Markdown, link, fence, ID, cache, sensitive-file, or other repository statistics. This exception applies only to the root Git metadata in working `bootstrap` and `live` profiles.

Working profiles also ignore and prune only these ordinary local artifacts:

- root project environments: `.venv/`, `venv/`, `env/`, and `ENV/`;
- `__pycache__/` at any depth;
- `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.hypothesis/`, and `htmlcov/`;
- `.pyc` and `.pyo` bytecode;
- `.coverage`, `.coverage.*`, `coverage.xml`, `coverage.json`, and `lcov.info`.

These paths must not be traversed and must not affect Markdown, links, fences, IDs, privacy checks, or statistics. This is a narrow allowlist: `.env` files, credentials, secrets, `private/`, `tokens/`, arbitrary hidden files, and private data are still inspected and rejected when appropriate. Archive validation rejects all working-only artifacts.

Live validation additionally permits and validates installed `units/` and `projects/`. For every Draft or Approved unit it checks directory/tracker parity, exact ID/title, required sections, concrete practice, `REVIEW.md`, interview coverage, micro-labs/experiments, starter/tests where required, placeholders, links, and premature solution leakage. Root `attempts/` and `solutions/` remain forbidden.

Archive validation is deliberately different. It forbids every `.git` file or directory entry and also forbids generated `units/`, `projects/`, `attempts/`, and `solutions/`. Archive packaging must use the archive profile.

Ordinary repository validation is implemented with the Python standard library and does not require pytest:

```bash
python scripts/validate_repo.py
```

The extended mutation/fixture suite and full validation-report comparison rerun pytest-backed fixture collection. Install the locked development group before either operation:

```bash
uv sync --group dev
uv run --group dev python scripts/validate_repo.py --self-test
```

If pytest is unavailable because the command was not run through the locked project environment, these extended operations fail with `[EXTENDED_TEST_PREREQUISITE_MISSING]` or `REPORT_EXTENDED_TEST_PREREQUISITE_MISSING`. Run `uv sync --group dev`, then retry through `uv run --group dev`; never classify this as an ordinary fixture failure.

## 19. Downloaded ZIP and report verification

Canonical final-report verification checks the recorded archive filename, content, extracted statistics, and all saved mutation/fixture-test summaries. It requires the development group:

```bash
uv sync --group dev
uv run --group dev python scripts/validate_repo.py \
  --verify-report <report.json> \
  --archive dsa-mastery-bootstrap.zip
```

A deliberately renamed downloaded copy may be verified with the same full comparison while accepting only the filename difference:

```bash
uv run --group dev python scripts/validate_repo.py \
  --verify-report <report.json> \
  --archive <renamed-copy.zip> \
  --allow-renamed-archive
```

When pytest-backed fixture/self-test comparison is deliberately unavailable, use content/statistics-only verification explicitly:

```bash
python scripts/validate_repo.py \
  --verify-report <report.json> \
  --archive <downloaded-copy.zip> \
  --skip-self-test-comparison
```

Combine `--allow-renamed-archive` with `--skip-self-test-comparison` when both conditions apply. Skipping self-test comparison does not weaken SHA-256, byte-size, entry-count, ZIP-integrity, required-file, forbidden-path, extracted-statistics, errors, or warnings checks. Canonical final packaging must still use full comparison through `uv run --group dev` after `uv sync --group dev`.

## 20. Publication

Final publication requires the exact completion prompt, live validation, relevant tests, a normal push, checked pull request, safe merge, synchronized local `main`, and a report of branch, commits, changed files, checks, pull request, and merge result.

Never force-push, bypass failed checks, discard unrelated work, or silently resolve a conflict.
