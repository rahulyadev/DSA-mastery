# Source and Version Policy

## Python baseline

- Canonical teaching baseline: Python 3.14.
- Initially verified runtime: CPython 3.14.7.
- Interview-compatibility baseline: Python 3.11.
- Preview releases are not canonical.

Re-verify the patch baseline from official Python sources before changing `.python-version` or regenerating `uv.lock`.

## Python source order

Prefer:

1. Python Language Reference;
2. Python Standard Library documentation;
3. accepted or final PEPs;
4. the typing specification;
5. Python Developer's Guide;
6. CPython source only when implementation detail materially matters;
7. official third-party-tool documentation.

Label language guarantees, standard-library contracts, CPython details, tooling behavior, and platform-specific behavior separately.

## Algorithm source order

Prefer original papers where practical, established textbooks, credible university course materials, and authoritative library documentation. Use original explanations and examples. Cite rather than reproduce copyrighted prose, diagrams, or exercise sets.

## LeetCode metadata

Store only minimal identifying metadata and original pedagogical notes. Verify number, current title, canonical slug, difficulty, and access status from the official problem page when packaging or materially updating metadata.

An unavailable network check is `Skipped`, never `Passed`. Platform metadata can change; record the verification date and do not convert company tags or popularity labels into hiring statistics.

## Version and interview compatibility

When code uses syntax or behavior newer than Python 3.11:

1. state the first supported version;
2. show the Python 3.14 canonical form;
3. provide a useful Python 3.11-compatible form;
4. distinguish syntax, runtime, typing-only, and CPython-specific differences.

Prefer readable interview code over version-specific cleverness.

## Complexity and benchmark claims

Algorithmic complexity requires explicit input variables and a derivation. Benchmark claims require an actual recorded run with Python version, machine, workload, warm-up, trial count, measurements, and limitations. Never invent a runtime or memory result.

## Experiments

Every experiment records its question, hypothesis, environment, command, actual output, interpretation, scope classification, and limitations. Do not present conceptual diagrams as literal CPython layouts.

## Release audit

When adopting a new stable Python feature release:

1. verify it through official sources;
2. update this policy and `.python-version`;
3. regenerate `uv.lock`;
4. run repository validation and all current unit/project tests;
5. audit recursion, integer, sorting, heap, typing, and performance notes;
6. add version callouts rather than rewriting history.
