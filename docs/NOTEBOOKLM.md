# NotebookLM Handoff

NotebookLM supports retrieval and comparison; it does not own progress or prove correctness.

## Upload

Upload approved unit `README.md` files, the relevant learning-path section, selected `PATTERN_INDEX.md` comparisons, and compact parts of `INTERVIEW_PLAYBOOK.md`.

Do not upload raw attempts, hidden/comparison solutions, generated test output, caches, profiler files, full problem-bank JSON, or noisy source trees by default.

## Useful notebook groups

- foundations and complexity;
- arrays, strings, and sequence patterns;
- linked structures, stacks, intervals, and heaps;
- trees and graphs;
- greedy and dynamic programming;
- bits, mathematics, and string algorithms;
- mixed mocks and interview communication.

## Flashcards

Generate cards primarily from `Physical Notebook Core`: problem shape, invariant, essential trace, complexity, anti-signal, comparison, and common failure. Avoid trivia and copied sentences.

## Quizzes

Ask for trace-based, complexity, invariant, comparison, and adversarial-case questions. For mixed quizzes, instruct NotebookLM not to reveal the pattern label, target complexity, or intended data structure before Rahul answers.

## Interview practice

Request one question at a time, changed-constraint follow-ups, and separate feedback on approach, correctness, proof, complexity, testing, code, and communication.

## Return weaknesses to Codex

Bring the exact unit ID, question, Rahul's answer, correction, cited note section, and remaining confusion to the existing unit chat. Update `REVIEW.md`; edit canonical notes only when the clarification is generally useful.

NotebookLM output is neither authoritative evidence nor an automatic progress transition. Verify technical claims and implementations in the repository workflow.
