# Practice — DSA-FND-060 Recursion, call stacks, and recursive complexity

| Field | Value |
|---|---|
| Unit note | [DSA-FND-060](../README.md) |
| Curriculum | [CURRICULUM.md](../../../../CURRICULUM.md#dsa-fnd-060) |
| Problem bank | [PROBLEM_BANK.md](../../../../PROBLEM_BANK.md) |
| Evidence target | E+T+I+P+D+R+M |
| Attempt required before solution | Yes |
| Passing scaffold command | `uv run --group dev python -m pytest -q practice/test_examples.py experiments` |
| Challenge validation command | `uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py` |
| Status | Not attempted |

Commands in this page run from the unit directory. Start from the repository root with:

```bash
uv sync --group dev --locked
cd units/problem-solving-foundations/DSA-FND-060-recursion-call-stacks-and-recursive-complexity
```

## Learning questions

1. What does the current call promise, and what does each waiting caller still need?
2. How do total invocations, maximum active depth, and retained data differ?
3. Which boundaries follow from the contract, rather than from a remembered code template?
4. When does a working small recursive implementation become an unsuitable large-input design?

## Cycle

```text
predict → trace → implement → run → observe → explain → optimize → vary → recall
```

## File and test separation

- [micro_lab.py](micro_lab.py) is a completed teaching trace of a list total. It does not
  implement either learner function.
- [starter.py](starter.py) holds two intentionally incomplete functions.
- [test_examples.py](test_examples.py) verifies only provided trace behavior.
- [test_challenge.py](test_challenge.py) defines the unsolved contracts. Initialization checks
  syntax and collection only; the challenge tests are **not passing implementation evidence**.
- Experiment tests check the measurement scripts, not Rahul's mastery.
- Keep the first attempt and later corrections distinguishable. Record the first failure and
  hints before revising. Do not add a comparison implementation until the exercise is closed.

Run the challenge tests only after recording an implementation attempt:

```bash
uv run --group dev python -m pytest -q practice/test_challenge.py
```

The tests are a finite set of observations. A reviewer must also check complexity, recursive
structure, copying, mutation, and the explanation; passing examples alone cannot prove those.

## Exercise index

| Exercise ID | Type | Difficulty | Objective | Files | Status |
|---|---|---:|---|---|---|
| DSA-FND-060-P01 | Predict / Trace / Debug | 2 | Recover call order, returns, and pending work | `micro_lab.py`; notebook | Not attempted |
| DSA-FND-060-P02 | Implement / Prove | 2 | Decide whether a bounded interval reads the same in both directions | `starter.py`, `test_challenge.py` | Not attempted |
| DSA-FND-060-P03 | Implement / Explain | 3 | Summarize a nested packet with an exact return contract | `starter.py`, `test_challenge.py` | Not attempted |
| DSA-FND-060-P04 | Analyze / Debug | 3 | Audit two unsupported cost claims | Notebook | Not attempted |
| DSA-FND-060-P05 | Mixed / Timed | 3 | Produce the requested episode report | A preserved independent attempt | Not attempted |

Difficulty is local conceptual difficulty, not a platform problem rating.

## DSA-FND-060-P01 — Predict the returning subtotals

### Task

Use the teaching function on `[3, 0, -5, 8]`. Before running it, write every call and return
in chronological order, the active prefix sizes at each event, each returned subtotal, and the
work still pending in each caller. Mark the maximum-depth instant. Then compare with execution
and identify the first discrepancy in your prediction, rather than only checking the final sum.

Also inspect this deliberately faulty example without repairing it first:

```python
def faulty_total(values: list[int], size: int) -> int:
    if size == 0:
        return 0
    faulty_total(values, size - 1) + values[size - 1]
```

Explain the actual behavior for an empty input, a singleton, and a two-element input. Write the
smallest correction only after recording what each caller receives.

### Constraints and expected behavior

- Input: lists of integers, at most 32 elements; the initial size is their full length.
- Required output: a complete trace and a reasoned bug diagnosis. The correct main example's
  total is `6`; the intermediate trace is yours to reconstruct.
- The trace records a returning frame before removing it.
- Performance target: no elapsed-time target for this small trace. Account separately for
  calls, maximum active depth, snapshot construction, and stored trace output.
- Explain every variable and distinguish a returned zero from no returned value.

### Required edge cases

- Empty input has a directly answerable result and still invokes the base case.
- `[0]` distinguishes a valid zero answer from a missing return.
- `[-5]` tests signed values without a second nonbase frame.
- Repeated values must not cause two different invocations to be merged in your trace.

### Before running

Record the predicted events, the return contract, the decreasing measure, the first point where
the faulty example diverges, and expected time/auxiliary/output/stack costs.

To observe your fresh input from the unit directory:

```bash
uv run --group dev python -c 'import sys; sys.path.insert(0, "practice"); from micro_lab import trace_prefix_sum; print(trace_prefix_sum([3, 0, -5, 8]))'
```

### Acceptance criteria

- [ ] Prediction exists before output is viewed.
- [ ] Every invocation is paired with its own return.
- [ ] Active-frame snapshots and local bindings are explained.
- [ ] The faulty example is diagnosed on the smallest useful input, including missing-return behavior.
- [ ] Algorithm costs are separated from the trace's added costs.
- [ ] The final explanation can be spoken in 90 seconds without the code.

### Progressive hints

Hint 1 is locked until Rahul requests it. Hint 2 is locked until a further attempt.
Hint 3 is locked until Rahul explains the remaining gap. No hint has been given.

## DSA-FND-060-P02 — Mirror interval

### Task

Implement `is_mirror(values, lo, hi)` in the starter. Return whether the selected half-open
interval reads identically in either direction. For example, the selected interval in
`values=[90, -2, 0, -2, 91], lo=1, hi=4` qualifies, even though the entire list does not.
Before coding, state the exact promise of a recursive call and justify all stopping conditions.

### Constraints and expected behavior

- `values` is a list of integers, `0 <= len(values) <= 64`, with magnitudes at most
  `10^6`. Bounds are integers; type validation is not part of this exercise.
- Valid bounds satisfy `0 <= lo <= hi <= len(values)`. Raise `ValueError` for invalid bounds.
- `hi` is exclusive. Empty and one-element intervals both return `True`.
- Return a Boolean and preserve the original list.
- Use recursion for the substantive decision. Do not use slicing, reversed copies, list
  construction, string conversion, or mutation to obtain the answer.
- Let `k=hi-lo`. Target `O(k+1)` worst-case time, `O(k+1)` stack words, and
  `O(1)` non-stack auxiliary words. Output is one Boolean.
- Avoid further substantive work once the answer is already determined.

### Required edge cases

- Empty list with `(0, 0)`; empty interval at the end of a nonempty list.
- One element; equal and unequal adjacent elements.
- Odd and even interval lengths.
- Matching exterior values with a disagreement inside.
- A qualifying subinterval inside a nonqualifying full list.
- Negative, reversed, and too-large bounds; an equal pair of bounds beyond the list is invalid.

### Before coding

Write the simplest baseline, its representation costs, the return contract, a decreasing
measure, and one adversarial dry-run. State why each excluded position is irrelevant.
Do not begin with a memorized code skeleton.

### Acceptance criteria

- [ ] First attempt and later edits remain distinguishable.
- [ ] Invalid-bound behavior and all valid stopping cases are justified.
- [ ] The implementation uses recursion without copies or input changes.
- [ ] Relevant challenge tests pass only after a recorded attempt.
- [ ] Correctness and worst-case time, non-stack auxiliary, output, and stack space are defended.
- [ ] Explain a new design choice if the list limit changes from 64 to 200,000; do not run
  an unsafe deep recursive call merely to demonstrate failure.

### Progressive hints

Hint 1 is locked until requested. Hint 2 requires another attempt.
Hint 3 requires an explanation of the remaining difficulty. No solution or hint is included.

## DSA-FND-060-P03 — Nested packet summary

### Task

Implement `summarize_packet(packet)`. A packet is either an integer or a tuple containing
zero or more packets. Return `(total, nesting)`: the sum of every integer occurrence and the
maximum number of tuple containers on any path through the packet. The contract must handle
empty containers, branching, reused subtuples, and independent successive calls.

### Constraints and expected behavior

- Input contains only integers and tuples; Boolean values and other Python types are outside
  the contract. Inputs are finite and acyclic.
- Integer magnitudes are at most `10^6`; maximum tuple nesting is 40.
- Let `v` count all integer and tuple occurrences in the fully expanded input, including
  the root; `v <= 10,000`. A reused subtuple counts again for each occurrence.
- An integer has nesting zero. An empty tuple has nesting one and contributes zero to the sum.
- Examples: `7 -> (7, 0)`; `() -> (0, 1)`;
  `(2, (6, ()), -3) -> (5, 3)`.
- Return a pair of integers without modifying the input or retaining state across calls.
- Use recursive calls to express the nested packet contract.
- Target `Theta(v)` time under bounded-word arithmetic. Let `h` be the maximum active
  path in packet occurrences; target `O(h)` auxiliary space including the call stack,
  and `O(1)` returned output words. Avoid flattening or copying the expanded packet.

### Required edge cases

- A scalar with no container; a negative scalar; an empty tuple.
- Tuples containing only other empty tuples.
- A broad tuple with many elements but shallow nesting.
- A narrow packet nested 40 levels deep.
- A shallow large value next to a deeper smaller value: structural nesting is not numeric magnitude.
- The same subtuple used twice; successive unrelated calls after a nonzero result.

### Before coding

Define the result of one recursive call in your own words. Explain what counts as an occurrence
and how the input-size definition treats reuse. Draw one branching input, label the expected
return of each part, and state which information must remain in a waiting caller.

### Acceptance criteria

- [ ] The first implementation attempt is preserved.
- [ ] Depth conventions are consistent for scalars, empty tuples, and nested tuples.
- [ ] Tests cover both width and depth, not just one long nested example.
- [ ] Reused subtuples obey occurrence semantics; a previous call cannot contaminate a result.
- [ ] Explain termination, coverage, and correctness using the return contract.
- [ ] Count time over all occurrences and memory over simultaneous live state.
- [ ] Discuss how the contract and approach would change if shared objects should be counted
  only once or mutable containers could form cycles; do not silently add those requirements.

### Progressive hints

Hint 1 is locked until Rahul asks. Hint 2 is locked until another attempt.
Hint 3 is locked until the specific unresolved reasoning step is stated.

## DSA-FND-060-P04 — Audit the analysis cards

### Task

For each synthetic routine below, replace the analyst's claim with a justified result. Record
the size variable, base cases, work recurrence, a small call tree, maximum active depth, total
work, and any additional storage assumptions. These routines measure execution shapes; they do
not stand for a named algorithm or promise a useful numeric output.

**Card A:** size is a nonnegative integer. At sizes zero and one, return immediately. At any
larger size, execute two independent calls of size `n-2`, one after another, with constant
local work. The analyst says, “Every path gets shorter, so the total work is linear.”

**Card B:** size is a nonnegative integer. At sizes zero and one, return immediately. At any
larger size, execute one call of size `floor(n/3)`, then do `n` constant-cost local operations.
It retains no size-dependent buffer. The analyst says, “The size is divided by three, so
the total work is logarithmic.”

### Constraints and expected behavior

- Use paper traces for sizes `0, 1, 2, 3, 6, 7`; you do not need to execute large inputs.
- Required output is a corrected analysis, not an implementation.
- Performance target: derive a tight bound for each routine instead of accepting a supplied
  target. Treat local primitive operations and frame fields as bounded words.
- Account for all executed siblings while remembering that they execute sequentially.
- Include scalar output space and the maximum active stack; state what is excluded.

### Required edge cases

- Both allowed base sizes.
- Odd and even sizes on Card A.
- Sizes just above powers of three on Card B.
- A counterfactual where Card B keeps a newly allocated `n`-element buffer alive during
  its child: revisit memory separately from the original time claim.

### Before checking

Write your prediction before using the notes or experiments. Name the first unsupported step
in each analyst's argument. If you later write a simulator, keep its output-storage cost out of
the modeled routine's cost.

### Acceptance criteria

- [ ] Recurrences count local operations separately from recursive work.
- [ ] Base, rounding, and odd/even behavior are checked.
- [ ] Tight time and maximum-depth claims follow from a derivation.
- [ ] The memory counterfactual accounts for simultaneously retained buffers.
- [ ] Explain each correction in under two minutes without quoting a theorem name.

### Progressive hints

Hint 1 is locked until requested. A second hint requires a new derivation attempt.
The final hint stays locked until the remaining gap is identified.

## DSA-FND-060-P05 — Episode report

### Task

An ordered log contains integer status readings. An episode is a nonempty contiguous section
whose readings are all equal. Return `(start, length)` for a longest episode. If several are
equally long, return the earliest start. If the log is empty, return `(-1, 0)`.
Explain your choices, implement an independent attempt, and design adversarial examples.

### Constraints and expected behavior

- Input is a list of at most 200,000 integers with magnitudes at most `10^9`.
- Return the specified integer pair; do not alter the supplied readings.
- Examples: `[6, 6, 1, 1, 1, 6] -> (2, 3)`;
  `[8, 8, 4, 4] -> (0, 2)`.
- Choose and justify resource use from the constraints. The reviewer target is withheld
  until the postmortem.
- Timebox: 25 minutes including clarification, implementation, tests, and spoken explanation.

### Required edge cases

- Empty and one-reading logs.
- All readings equal; every neighboring reading different.
- Several equally long episodes.
- The selected episode at the start, in the middle, or reaching the last reading.
- Negative readings and zero.

### Before coding

Clarify the output and tie rule, construct your own examples, record an initial approach, and
explain what would make it unsuitable. No approach is prescribed by this exercise's location.

### Acceptance criteria

- [ ] Attempt begins without reading method-specific guidance.
- [ ] Returned position, length, empty behavior, and tie handling satisfy the contract.
- [ ] Tests include a final-reading boundary and a tie.
- [ ] Justify correctness and resource use for the full input constraints.
- [ ] Record whether any hint was used, and review the approach only after the attempt.

### Progressive hints

All hints are locked. Any requested hint is supplied individually and recorded after the
first approach is preserved. Method and evaluation details are reserved for the postmortem.

## Review record

| Item | Learner record |
|---|---|
| Attempt date and exercise | Not attempted |
| Original reasoning and file | Not recorded |
| First failing example | Not evaluated |
| What was correct | Not evaluated |
| First missing reasoning step | Not evaluated |
| Hint history | None given |
| Commands and actual results | No learner run yet |
| Revised explanation | Not attempted |
| Remaining weakness | Not evaluated |
| Next review | One day after first study, then adapt |

Use [REVIEW.md](../REVIEW.md) for dated learning evidence. Generated notes, maintenance test
results, and a merged branch do not advance the learning state.
