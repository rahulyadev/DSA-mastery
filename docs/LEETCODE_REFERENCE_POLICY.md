# LeetCode Reference Policy

[`data/problems.json`](../data/problems.json) is the structured source of truth. [`PROBLEM_BANK.md`](../PROBLEM_BANK.md) is its human-readable index.

## Stored metadata

Each entry contains:

- exact problem number and current title;
- canonical official URL and slug;
- difficulty and access status;
- one canonical owning unit;
- primary and secondary concepts;
- prerequisites and learning purpose;
- practice tier and learner-facing visibility;
- first-attempt timebox;
- trap categories and review requirements;
- original follow-up variations;
- a free alternative when a premium item is retained.

## What is not stored

Do not store full problem statements, screenshots, examples copied wholesale, paid editorials, hidden tests, proprietary solutions, leaked company questions, or company tags described as verified frequency.

## Ownership and reuse

A problem has one canonical owning unit. Another unit may link to it without duplicating its metadata. Intentional reuse across learning paths is normal and does not create a second record.

## Access rules

- Mandatory paths must work without LeetCode Premium.
- A premium problem may appear only as an optional extension with an accessible free alternative.
- If access status becomes uncertain, mark the online check `Skipped` or the metadata `needs review`; do not guess.

## Learner-facing labels

Teaching sets may show pattern labels. Mixed and mock lists must not reveal the primary pattern, intended structure, target complexity, or key invariant before the attempt. Reveal those only in the postmortem.

## Metadata verification

Use the official URL form:

```text
https://leetcode.com/problems/<canonical-slug>/
```

When packaging or updating metadata, verify number, title, URL, difficulty, and access from the official page. Record the date. Validation can prove schema and internal parity; only a successful online read can prove current platform metadata.

## Solutions and hints

Exercises begin unsolved. Give one hint at a time. Never place a complete solution in tests, comments, examples, filenames, or learner-facing metadata before a meaningful attempt.
