# Practice — DSA-FND-050 Amortized, aggregate, output-sensitive, and query analysis

| Field | Value |
|---|---|
| Unit note | [DSA-FND-050](../README.md) |
| Curriculum | [CURRICULUM.md](../../../../CURRICULUM.md#dsa-fnd-050) |
| Problem bank | [PROBLEM_BANK.md](../../../../PROBLEM_BANK.md) |
| Evidence target | E+T+P+D+R+M |
| Attempt required before solution | Yes |
| Status | Not attempted |
| Passing teaching checks | From this unit directory: `uv run --group dev python -m pytest -q .` |
| Challenge validation | Not applicable: this reasoning unit has no implementation challenge tests |

## Learning questions

1. Which expensive events can repeat, and which operation pays for each occurrence?
2. What changes when the query count, initial state, required output, or retention policy changes?
3. Which claimed costs describe the algorithm, and which describe the observation script?

## Cycle

```text
predict → trace → implement → run → observe → explain → optimize → vary → recall
```

For a reasoning task, “implement” can mean writing an explicit counting rule or a small
independent checker after the hand derivation. Runnable code is supplementary here, not a
new canonical `I` requirement. Never replace the initial argument with a polished answer.

## File and test separation

- [micro_lab.py](micro_lab.py) is a worked model for two teaching policies. Its output is not
  evidence that a new policy in P01 has been understood.
- [test_amortized_trace.py](test_amortized_trace.py) checks only the teaching counter.
- The two [experiments](../README.md#17-experiment-decision) contain worked observations and
  explicit limitations. Predict a fresh run before consulting its recorded output.
- There is no `starter.py` or `test_challenge.py` because this unit requires explanation,
  trace, proof, debugging, recall, and transfer rather than an unsolved implementation.
- Passing these supplied tests proves nothing about the learner's answers to P01–P05.
- Save each original attempt in a separate local note such as `P01-attempt.md`, with date,
  prediction, reasoning, hint history, actual commands, and any later corrections appended.

## Exercise index

| Exercise ID | Type | Difficulty | Objective | Status |
|---|---|---:|---|---|
| DSA-FND-050-P01 | Trace / Prove | 3 | Compare two specified storage policies from their transitions | Not attempted |
| DSA-FND-050-P02 | Debug / Explain | 3 | Audit a teammate's cost claim against the actual program | Not attempted |
| DSA-FND-050-P03 | Compare / Vary | 3 | Choose a service plan under explicit work and memory budgets | Not attempted |
| DSA-FND-050-P04 | Analyze / Explain | 3 | Audit a report's representation and input-preservation contract | Not attempted |
| DSA-FND-050-P05 | Mixed / Timed | 3 | Solve Request R from its contract | Not attempted |

<a id="dsa-fnd-050-p01"></a>

## DSA-FND-050-P01 — Two storage policies

### Task

A buffer begins empty with three already allocated slots. One append writes one new reference.
When full, it first copies every existing reference into a newly allocated buffer. Policy A
triples the old capacity; policy B adds three slots. Derive a complete transition table for
eleven appends under each policy, then justify the total work for arbitrary non-negative `m`.
Do not assume that the worked lab's constants or doubling boundaries still apply.

### Constraints and expected behavior

- Input: `m` appends of existing references; no deletes, hidden resets, or failures.
- Initial state: size zero, capacity three. Initial allocation is outside this counter.
- Cost: one unit per copied old reference and per newly written reference. Allocation and
  slot initialization are excluded explicitly; discuss them separately afterward.
- Output: columns for append number, size before, capacity before/after, copies, actual cost,
  cumulative cost, and your justified per-operation charge if you choose one.
- Performance target: derive a tight aggregate bound and a worst individual bound for each
  policy. Your proof must cover every prefix, not just a completed growth cycle.
- Small traces may use `m <= 30`; do not run a huge simulation as a substitute for a proof.

### Required edge cases

- `m = 0`: no appends and no division by an operation count.
- `m = 3` and `m = 4`: stop on either side of the first growth boundary.
- `m = 9` and `m = 10`: check the two policies separately rather than sharing a trace.
- Start instead with the original three slots already full: explain which setup term changes.

### Before running

Draw the eleven-row traces and write your sum before modifying or extending any teaching code.
Explain the invariant that connects size, capacity, and which references must be copied.
If you use prepaid charges, identify the first prefix on which the proposed charge could fail.

### Acceptance criteria

- [ ] Both transition tables cover all eleven appends, not just resize steps.
- [ ] A general sum or charging proof accompanies the finite examples.
- [ ] The initial-state term and individual spikes are separated from the aggregate result.
- [ ] Auxiliary resizing storage, retained buffer storage, and trace-output storage are named.
- [ ] Any executed checker is recorded after the original prediction, with discrepancies kept.
- [ ] The proof is reconstructed aloud without reopening the lab.

### Progressive hints

Hint 1: Locked until Rahul requests it.

Hint 2: Locked until Rahul has made another attempt.

Hint 3: Locked until Rahul has explained the remaining gap.

<a id="dsa-fnd-050-p02"></a>

## DSA-FND-050-P02 — A cost claim under review

### Task

Review the supplied program and the claim below. Its contract is to return the number of
reviews performed when each newly admitted token causes every currently pending token to be
reviewed once. The counter represents real required review events, even though the example
does not perform a useful business action for each event. Find the first incorrect step in
the claim, give a smallest informative trace, and replace it with a justified analysis.

```python
def review_count(n: int) -> int:
    pending = []
    checks = 0
    for token in range(n):
        pending.append(token)
        for _ in pending:
            checks += 1
    return checks
```

Claim to audit: “Every token is appended once, and append is amortized constant, so the whole
function is linear. The inner loop doesn't change that.” This is a review specimen, not a
solution or a recommended implementation.

### Constraints and expected behavior

- Input: integer `n` with `0 <= n <= 10^6`; use `n <= 8` for any literal execution.
- Required output: a hand trace for `n = 4`, an exact review count in terms of `n`, a tight
  time bound for this program, and auxiliary/output/stack space.
- Performance target: a proof that explains all review iterations and append work. Code
  optimization is not needed to close this reasoning task.
- Count reviews as bounded-cost events. State how large integer counters would change the
  machine-word simplification when the input restriction is removed.

### Required edge cases

- No admitted tokens.
- Exactly one admitted token.
- The earliest token after several later admissions: record how often it is reviewed.
- A proposed change deletes each token after its first review: determine whether it preserves
  the original contract before discussing speed.

### Before running

Write what the claim counts and what it omits. Predict `checks` after every outer iteration,
then decide whether a local invariant says anything about all future visits to the same token.
Do not accept a changed algorithm that returns a different required review count.

### Acceptance criteria

- [ ] The original claim is preserved and its first unsupported inference is identified.
- [ ] The sum counts the supplied loop, not a different desired program.
- [ ] The trace and general proof agree, including the empty input.
- [ ] A semantic change is distinguished from a semantics-preserving optimization.
- [ ] The repair includes explicit input variables and Python append/counter assumptions.
- [ ] The explanation can be delivered in under 90 seconds.

### Progressive hints

Hint 1: Locked until Rahul requests it.

Hint 2: Locked until Rahul has made another attempt.

Hint 3: Locked until Rahul has explained the remaining gap.

<a id="dsa-fnd-050-p03"></a>

## DSA-FND-050-P03 — A catalog service budget

### Task

An unchanged catalog of `n` entries serves `q` scalar subtotal requests. Two correct service
plans have the exact artificial work costs specified below. Recommend a plan for each workload,
show the arithmetic, and explain what operational facts your recommendation relies on. The
costs are given measurements in a logical work model, not promises of Python execution time.

Plan A has no preprocessing and costs `3n` work units per request. Plan B eagerly builds an
index for `8n` units and answers each request for five units. Both return one bounded-size
integer per request. Plan B retains `n+1` extra words; plan A uses constant working words.

### Constraints and expected behavior

- Inputs: first use `n = 64` and `q` in `{0, 1, 2, 3, 16}`; then derive a symbolic decision rule
  for arbitrary positive `n` and non-negative `q` without subtracting big-O notation.
- Output: a comparison table of total work, retained index, retained responses, selected plan,
  and the reason for any tie or rejection.
- Performance target: choose the lower modeled total among feasible plans, including build
  cost. Do not claim a precise wall-clock crossover.
- First compare an index budget of 128 words, then 32 words, excluding input and response
  storage. Input already exists; both plans must keep it unchanged.
- All given request costs exclude storing the returned integers. Report the common response
  cost separately if the caller collects all `q` answers.

### Required edge cases

- Zero requests with an eager build; then consider a caller allowed to avoid construction.
- One request and a request count near the point where the decision changes.
- A memory budget too small for an otherwise attractive plan.
- Every request is preceded by a value update that invalidates Plan B's entire index. Rebuild
  costs `8n` each time; input-update cost is one additional unit under either plan.
- Plan A requests instead touch only width `w_i` at cost `3w_i`; explain why `q` alone no
  longer determines your recommendation.

### Before running

Write both full-workload expressions and state which quantities you hold fixed. Explain what
you would need to measure before transferring the artificial-cost decision to production.
The teaching query experiment uses different counters and does not supply this task's table.

### Acceptance criteria

- [ ] Every finite workload has an arithmetic comparison and a feasibility check.
- [ ] The symbolic rule handles ties and cases where one plan has no cheaper query cost.
- [ ] Updates, eager construction, and empty workloads are accounted for explicitly.
- [ ] Index memory is not conflated with retained response memory.
- [ ] One rejected plan is defended aloud under each memory budget.
- [ ] The changed-width and changed-update scenarios are reanalyzed without guessing.

### Progressive hints

Hint 1: Locked until Rahul requests it.

Hint 2: Locked until Rahul has made another attempt.

Hint 3: Locked until Rahul has explained the remaining gap.

<a id="dsa-fnd-050-p04"></a>

## DSA-FND-050-P04 — Report format and space contract

### Task

A reporting endpoint takes an ordered list and must describe every nonempty prefix in original
order. Format A returns `(start, stop)` descriptors referring to an unchanged input snapshot.
Format B returns an independent list copy of each prefix. Compare the actual result volume,
construction work, and peak storage for both formats. There are no filtering or sorting
requirements. A teammate proposes sorting the input first and claims both formats use linear
space because both return the same number of rows. Audit both parts of that proposal.

### Constraints and expected behavior

- Input: `n` bounded-size values; trace `[8, -3, 4, 8]`, retaining duplicate positions and order.
- Output: enumerate both representations for the four-item trace, count rows and stored
  references/endpoint words separately, and derive the general bounds in your own notation.
- Descriptors use half-open boundaries, not copies. They are useful only while the referenced
  snapshot remains valid; include its retention requirement in the system-level memory account.
- Format B snapshots must not alias a changing temporary list. The original input must remain
  unchanged under both formats.
- Performance target: derive tight construction and peak-space bounds in terms of input and
  emitted data, with auxiliary, output, and recursion-stack space separated. No code is required.

### Required edge cases

- Empty input and a single-element input.
- Duplicate or negative values that must not be sorted or deduplicated.
- A consumer that immediately releases each copied prefix versus one that collects all copies.
- A descriptor consumer that still needs the snapshot after the producer finishes.
- A recursive version with one active frame per input position, even if it makes no slices.

### Before running

Draw the objects that remain live, not only the local variable names. Distinguish count of
records from the total size of their contents. Predict the largest simultaneously live output
for each consumer policy before trying any memory tool.

### Acceptance criteria

- [ ] Row count and emitted data volume are derived independently.
- [ ] The input-order and snapshot-lifetime contracts are preserved.
- [ ] The teammate's claim is repaired with a concrete example and general bound.
- [ ] Peak live memory is distinguished from cumulative allocation over time.
- [ ] The streaming variation includes the size of the currently emitted prefix.
- [ ] Any memory observation is labeled shallow/deep or traced-allocation scope accurately.

### Progressive hints

Hint 1: Locked until Rahul requests it.

Hint 2: Locked until Rahul has made another attempt.

Hint 3: Locked until Rahul has explained the remaining gap.

<a id="dsa-fnd-050-p05"></a>

## DSA-FND-050-P05 — Request R

### Task

Design a component that accepts the commands below in order, starting with no visible entries.
`add(value)` adds the value after all currently visible entries. `undo(r)` removes up to `r`
most recently added entries that are still visible. `read()` returns an independent snapshot
of all visible values in their current order. Later commands must not change an earlier
snapshot. Explain your proposal, walk through the supplied commands, and defend its resource
costs from the input and output contract.

```text
add(5), add(-1), read(), undo(1), read(), add(7), read(), undo(10), read()
```

### Constraints and expected behavior

- Input: at most `10^5` commands; values are bounded-size signed integers; `0 <= r <= 10^5`.
- Required output: every `read()` snapshot, plus a clear proposed interface, state description,
  correctness argument, adversarial tests, and resource analysis. Pseudocode is sufficient.
- Commands arrive online and cannot be rearranged. No previously returned snapshot may change.
- Performance target: intentionally not supplied for this mixed task. Derive and defend a
  bound, introducing any additional size variables you need. No intended structure is named.
- Timebox: 20 minutes for the first explanation, trace, and complexity argument. Record elapsed
  time and any hint request honestly rather than calling an unfinished attempt complete.

### Required edge cases

- No commands, or a `read()` before any `add()`.
- `undo(0)` and an undo larger than the visible entry count.
- Repeated reads without intervening commands.
- Repeated equal values whose positions are still distinct entries.
- Changes after earlier snapshots have already been returned to a caller.

### Before running

Close the unit note and experiments. Save your first reasoning and predicted snapshots before
asking for feedback. State uncertainties and rejected alternatives in your own words. If you
choose to implement, keep that original attempt even after later corrections.

### Acceptance criteria

- [ ] The trace satisfies every command and preserves earlier snapshots.
- [ ] The proposal includes a correctness argument and termination explanation.
- [ ] Resource bounds account for the whole command sequence and all retained results.
- [ ] The listed boundary cases are checked without relying only on the supplied trace.
- [ ] A two-minute explanation is recorded before any feedback supplies an approach.
- [ ] After closing the first attempt, reassess a changed `read()` contract that returns only
  the latest visible value, or `None` when empty.

### Progressive hints

Hint 1: Locked until Rahul requests it.

Hint 2: Locked until Rahul has made another attempt.

Hint 3: Locked until Rahul has explained the remaining gap.

## Review record

No learner attempt has been evaluated. For each future attempt record its date and file link,
the exact claim being assessed, what was correct, the first missing reasoning step, a smallest
counterexample, hint level, actual commands/results, and the next recall date.

Practice status and unit learning state remain unchanged until evidence is assessed using
[REVIEW.md](../REVIEW.md). A comparison answer may be added only after Rahul closes the
exercise, and must remain separate from the original reasoning.
