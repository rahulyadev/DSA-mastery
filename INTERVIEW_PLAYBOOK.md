# Interview Playbook

This playbook teaches a natural reasoning conversation, not a script to memorize.

## Universal flow

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

## Questions to answer before coding

1. What exactly is being asked?
2. Which input variables and constraints matter?
3. What is the simplest correct brute-force solution?
4. Which operation makes it too slow?
5. What information is repeatedly recomputed?
6. Which structure or monotonic property can remove that work?
7. What invariant must remain true?
8. Why are all necessary candidates considered?
9. Why can other candidates be discarded?
10. What are the real time, auxiliary, output, and recursion-stack costs?
11. Which minimal adversarial examples could break the implementation?
12. Which changed requirement would invalidate the approach?

## Complexity explanation contract

Always name input variables and dominant operations. Separate auxiliary, output, and recursion-stack space. State whether a hash-table bound is average-case, whether sorting or heap construction is included, and whether slicing or string concatenation adds hidden cost.

## Natural answer outlines

### “Why is this correct?”

State the invariant, show initialization, show that each update preserves it, explain progress/termination, and connect the final state to the required answer.

### “Why not sort?”

Compare time, memory, order destruction, streaming constraints, and whether complete ordering provides value beyond the requested output.

### “Why is this loop still linear?”

Count total pointer movement or total pushes/pops across the full execution rather than multiplying syntactically nested loops.

### “Can you reduce memory?”

Name what information is retained, whether it is needed for future transitions or reconstruction, and what is lost by compression.

### “What changes for streaming input?”

Identify whether the algorithm needs future values, random access, multiple passes, or full ordering; then choose bounded state or admit the limitation.

### “What if duplicates are allowed?”

Revisit key identity, multiplicity, pointer movement, deduplication, and strict versus non-strict comparisons.

### “What if the data does not fit in memory?”

Separate one-pass streaming, external sorting, chunking, bounded heaps, sketches, and system-design concerns.

### “How would you test this?”

Derive tests from constraints, representation, boundaries, invariant, and transitions; include a tiny oracle or property where useful.

## Mock-interview behavior

- Ask one question at a time.
- Do not reveal the pattern, target complexity, invariant, or intended data structure.
- Wait for Rahul’s reasoning.
- Identify the exact missing reasoning step.
- Give the smallest next hint.
- Let Rahul recover.
- Add follow-ups that change constraints after a correct solution.

## Scoring rubric

Score each dimension independently from 0 to 4:

| Dimension | Evidence |
|---|---|
| Understanding | Restates the task and clarifies ambiguity. |
| Constraint analysis | Connects input size to feasible approaches. |
| Algorithm choice | Derives a viable approach without a label. |
| Correctness | States a useful invariant and justifies candidate coverage. |
| Complexity | Gives accurate time and all relevant space costs. |
| Implementation | Writes clear, idiomatic, explainable Python. |
| Testing | Derives adversarial boundaries and dry-runs accurately. |
| Communication | Narrates decisions and responds to follow-ups. |

## Renewable unseen reserve

The problem bank holds 30 Easy/Medium problems in a hidden-label reserve. It can supply three non-overlapping ten-problem readiness sets before recycling. Hard stretch/mock problems are stored separately and do not count toward the Easy/Medium gate. Before an attempt, do not reveal the owner unit, pattern, intended data structure, target complexity, or invariant.

## Readiness gates

Preparedness is supported—not guaranteed—when Rahul can repeatedly:

- solve at least 70% of a recent set of 10 unseen mixed Easy/Medium problems within 25/40-minute timeboxes without a pattern hint;
- produce a viable approach on at least 3 of 4 realistic mocks;
- state a useful invariant before or during implementation on at least 80% of core problems;
- give correct complexity, including Python costs, on at least 85% of reviewed attempts;
- identify and test boundary cases without prompting on at least 80% of attempts;
- explain a rejected alternative and handle one changed constraint in each mock;
- re-solve representative weak problems after 7–30 days without copying.

Thresholds guide revision. They do not guarantee a hiring outcome.
