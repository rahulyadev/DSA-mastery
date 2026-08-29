# DSA-FND-030 — Invariants, correctness, and termination

## Physical Notebook Core

Use this page when an algorithm looks plausible but you still need to explain why it is safe,
complete, and guaranteed to finish.

### Problem shape or pressure

A loop repeatedly changes state. Examples may show what happened on a few inputs, but an
interviewer can still ask whether an index ever leaves bounds, whether a candidate is skipped,
whether the returned result follows from the final state, or whether the loop can run forever.

### One-sentence mental model

> An invariant says what remains true at a chosen state boundary; initialization and preservation
> keep it true, the false guard turns it into the postcondition, and a bounded decreasing measure
> proves termination.

### Essential visual

```text
find the first index whose value is at least 6
values = [2, 5, 1, 7]

loop-head invariant I(i):
  0 <= i <= 4
  every index j in [0, i) has values[j] < 6

state boundary       known excluded prefix       guard                     V = 4-i
i = 0                []                          0<4 and 2<6 -> true            4
  update i <- 1             I preserved; V strictly decreases
i = 1                [2]                         1<4 and 5<6 -> true            3
  update i <- 2             I preserved; V strictly decreases
i = 2                [2,5]                       2<4 and 1<6 -> true            2
  update i <- 3             I preserved; V strictly decreases
i = 3                [2,5,1]                     3<4 and 7<6 -> false           1

exit knowledge = I(3) and not guard
               = every earlier value is < 6, while values[3] >= 6
               => index 3 is the first valid index
```

#### How to read this visual

Read only at loop heads: before the first guard test, after every completed update, and once more
when the guard is false. The processed prefix is half-open, `[0, i)`. The invariant explains what
that prefix means; `V = n - i` is a separate termination measure. At exit, combine the invariant
with the reason the guard is false.

#### Key insight

The invariant is not the whole proof. It provides persistent knowledge. The negated guard supplies
new exit knowledge, and the decreasing non-negative measure rules out an infinite sequence of
iterations.

#### Simplification or limitation

This visual uses a finite, unchanged list with constant-time indexing and integer comparisons. It
does not prove algorithms over a mutating collection, an unbounded stream, floating-point values
with special cases, or a loop whose comparison has side effects. Those contracts need different
state claims and sometimes a different termination argument.

### Governing invariant or rules

1. Choose one precise boundary and state a useful claim there, including bounds and the semantic
   meaning of processed or remaining state.
2. Prove initialization, preservation under every branch, and `invariant and not guard` implies the
   required postcondition.
3. Prove progress separately with a well-founded measure that strictly decreases or increases
   toward a finite bound on every continuing transition.

### Minimal proof skeleton

```text
write precondition and postcondition
choose the loop-head state boundary
state I using exact indices, ranges, and result meaning
initialization: precondition => I
preservation: I and guard and one body step => I again
exit: I and not guard => postcondition
choose a natural-number measure V
show I and guard => V >= 0
show every continuing body step makes V strictly smaller
state time, auxiliary/output/stack space, and hidden Python costs
```

### Complexity

- Input variables: `n` list elements and `c` worst-case cost of one threshold comparison.
- Time: best case `Theta(c)` and worst case `Theta(nc)`; under the usual constant-cost integer
  comparison model this is `Theta(1)` best case and `Theta(n)` worst case.
- Auxiliary space: `Theta(1)` for `i`, `n`, and scalar control state.
- Output space: `Theta(1)` for one index or `None`.
- Recursion stack: zero; the teaching scan is iterative.
- Important Python cost: recomputing `all(values[j] < threshold for j in range(i))` at every loop
  head makes an executable invariant check quadratic across a full scan. `values[:i]` also allocates
  a slice. A proof assertion and the algorithm's required work must be counted separately.

### Recognition cues and anti-cues

- Signal: the explanation contains “so far,” “remaining candidates,” “already processed,” “valid
  region,” or “this pointer never moves backward.”
- Constraint signal: a loop has multiple branches, mutations, early exits, or boundary-sensitive
  updates whose safety cannot be defended by examples alone.
- Anti-signal: a statement is true but does not connect the loop state to the postcondition, such as
  “the input length stays `n`.” That can be invariant and still be useless.

### Important comparison

Partial correctness versus total correctness: partial correctness says that if the algorithm
terminates, its answer satisfies the contract; total correctness also proves that termination must
occur for every allowed input.

### Common failure

Saying “`i` increases, so the loop terminates” is incomplete. If `i` can skip the stopping state, is
unbounded, or fails to increase on one branch, the conclusion does not follow. Name a bounded
measure and prove strict progress on every path that returns to the guard.

### Recall prompts

1. At exactly which program boundary does your invariant hold?
2. What does `invariant and not guard` tell you that the invariant alone does not?
3. Which non-negative integer changes strictly on every continuing iteration?

| Field | Value |
|---|---|
| Domain | Problem-solving foundations |
| Curriculum | [CURRICULUM.md](../../../CURRICULUM.md#dsa-fnd-030) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Pattern index | [PATTERN_INDEX.md](../../../PATTERN_INDEX.md) |
| Problem bank | [PROBLEM_BANK.md](../../../PROBLEM_BANK.md) |
| Primary outcome | State useful loop or state invariants and use them to justify safety, progress, completeness, and termination at interview depth. |
| Hard prerequisites | DSA-FND-010, DSA-FND-020 |
| Soft prerequisites | None |
| Priority | Core |
| Interview frequency | High |
| Practical relevance | High |
| Python relevance | High |
| Difficulty | 3 |
| Depth | D2 |
| Scope | Foundations, Proof, Interview |
| Size | L |
| Evidence | E+T+P+D+R+M |
| Artifact state | Draft |
| Canonical Python | 3.14 |
| Interview compatibility | 3.11 |

## 1. Learning outcomes and evidence

After this unit Rahul should be able to:

1. translate a result contract into a useful loop-head invariant rather than a vague comment;
2. identify the exact boundary at which an invariant is claimed;
3. prove initialization and preservation for every branch that returns to the loop guard;
4. derive the postcondition from the invariant together with the false guard;
5. separate safety, partial correctness, progress, completeness, and termination obligations;
6. select and defend a well-founded ranking measure for a finite-state process;
7. debug off-by-one, skipped-state, stale-summary, unsafe-guard, and non-progress defects using the
   first broken proof obligation;
8. explain time plus auxiliary, output, and recursion-stack space without hiding instrumentation
   costs;
9. communicate a compact correctness argument and adapt it when the contract changes.

Required evidence:

- Predict and reconcile a complete loop-head trace with invariant and ranking values.
- Produce an initialization, preservation, exit, and termination argument without reading the note.
- Debug multiple faulty loops by naming the first failed proof obligation and a smallest
  counterexample.
- Complete a changed-constraint proof and an unlabeled mixed transfer without being given the
  intended invariant or target complexity.
- Reconstruct the reasoning after delay and record the exact weakness exposed by recall.

## 2. Prerequisite bridge

`DSA-FND-010` and `DSA-FND-020` are hard prerequisites. Their tracker rows currently contain no
learner-produced evidence, so use only this minimum bridge before entering the unit:

| Unit | Why it matters | Minimum bridge |
|---|---|---|
| `DSA-FND-010` | A proof needs an exact input contract, output predicate, identity rule, and mutation permission. | Write allowed inputs, required result, edge semantics, and pre/postconditions before reasoning about the loop. |
| `DSA-FND-020` | Completeness and safe exclusion depend on knowing the legal candidate space. | State the simplest correct enumeration, what has been processed, what remains, and the exact bottleneck before claiming candidates can be skipped. |

These bridges make the proof vocabulary usable, but they do not replace closed-book evidence for
either prerequisite.

## 3. Intuition and problem shape

An algorithm is a sequence of state transitions. A proof does not need to narrate every possible
execution. It needs a compact statement that survives each transition and contains enough
information to derive the result when execution stops.

For a loop, distinguish six pieces:

| Piece | Question it answers |
|---|---|
| Precondition | What may be assumed about every allowed input? |
| Postcondition | What must be true of the returned result and final state? |
| Guard | Under which current states does another iteration run? |
| Invariant | What is true at the chosen boundary before and after every iteration? |
| Transition | How does one body execution change state while preserving the invariant? |
| Ranking measure | Why can continuing transitions not occur forever? |

An invariant is often easiest to derive by finishing this sentence:

> At the start of the next iteration, the state summarizes exactly ______ about the processed
> region, and every answer not yet decided remains represented by ______.

Useful invariants commonly combine more than one clause:

- **bounds:** indices and sizes remain legal;
- **representation:** data structures encode the intended abstract state;
- **processed-state meaning:** a summary is exact for a prefix, suffix, window, or visited set;
- **candidate retention:** every answer not yet ruled out remains in an active region;
- **result relation:** a running answer is optimal or valid among work already processed.

“The array is still an array” may be true at every iteration, but it cannot usually establish the
postcondition. A useful invariant is strong enough to finish the proof and weak enough to establish
initially and preserve under every branch.

### Safety, correctness, completeness, and termination are related but distinct

- **Safety:** no illegal operation or state is reached, such as out-of-range indexing.
- **Soundness:** any answer returned satisfies the required predicate.
- **Completeness:** no required valid answer is missed; for a first-answer contract, no earlier valid
  answer was skipped.
- **Partial correctness:** if execution terminates, the postcondition holds.
- **Progress:** one transition moves toward a stopping state.
- **Termination:** an infinite sequence of continuing transitions is impossible.
- **Total correctness:** partial correctness plus termination.

Passing examples supplies evidence about executions, not a universal argument over all allowed
states. Conversely, a proof of a misstated contract can be internally valid and still solve the wrong
problem. Contract work and proof work must agree.

## 4. Brute force and bottleneck

### Simplest correct baseline

For “return the first index whose value is at least `threshold`, or `None`,” a deliberately literal
baseline can collect every matching index and then choose the first:

```python
def first_index_at_least_baseline(
    values: list[int], threshold: int
) -> int | None:
    matches: list[int] = []
    for index, value in enumerate(values):
        if value >= threshold:
            matches.append(index)
    return min(matches) if matches else None
```

This baseline is easy to relate to the output predicate: the returned value is the minimum of all
valid indices. It still needs a coverage argument for the enumeration, but it does not rely on an
early-exit claim.

### Exact bottleneck

The baseline always performs `n` threshold comparisons and can store up to `n` matching indices,
even though the contract needs at most one index. The repeated work after the first match cannot
change which match is first.

An early-exit scan does not improve the worst-case `Theta(n)` bound, because a no-match input must
still inspect all `n` positions. It improves best-case work and removes the avoidable `Theta(n)`
match list. The proof obligation created by the optimization is exact:

> At index `i`, why is it safe to return now, and why can no earlier index be a valid answer?

The processed-prefix invariant answers that question.

## 5. Derivation and invariant

Start from the postcondition rather than guessing a slogan.

For result `r`:

```text
r is None
    exactly when no index j in [0,n) has values[j] >= threshold

or

r is an integer in [0,n)
    values[r] >= threshold
    every earlier j in [0,r) has values[j] < threshold
```

At a candidate index `i`, the only history needed to justify “first” is that every earlier index has
failed. This gives the loop-head invariant:

```text
I(i): 0 <= i <= n
      and for every j in [0,i), values[j] < threshold
```

The loop should continue exactly while `i` is in bounds and the current value also fails. Advancing
`i` then extends the proven-failing prefix by one position. The ranking measure is:

```text
V(i) = n - i
```

Under the invariant and guard, `V` is a positive integer. After `i <- i + 1`, it decreases by one.

### Derivation checklist

1. Write the postcondition with exact quantifiers and interval conventions.
2. Ask what historical fact would make an early return safe.
3. Express that fact over the already processed region.
4. Add bounds needed to evaluate the guard safely.
5. Choose initialization that makes every invariant clause true, including empty regions.
6. Design the body so one new item joins the processed region without falsifying its meaning.
7. Negate the full guard and combine it with the invariant.
8. Choose a measure over a well-founded set and prove strict progress on every continuing branch.

### Assertion versus invariant

An invariant is a mathematical claim about reachable states. An `assert` is one possible runtime
check for selected executions. Python can omit assertion code when optimization is requested, so an
assertion must not validate untrusted input or provide required control flow. A prefix-scanning
assertion can also change the debug build's complexity. Use assertions as diagnostics, not as the
proof itself.

## 6. Detailed visual trace

### First valid index: proof state at every loop head

```text
input: values = [2, 5, 1, 7], threshold = 6, n = 4

I(i) = 0 <= i <= n and all values[0:i] are below 6
V(i) = n - i

head  i  processed [0:i)  current  I?   guard?  V  transition / conclusion
----  -  ---------------  -------  ---  ------  -  -----------------------
  0   0  []                  2      yes   true   4  current fails; i <- 1
  1   1  [2]                 5      yes   true   3  current fails; i <- 2
  2   2  [2,5]               1      yes   true   2  current fails; i <- 3
  3   3  [2,5,1]             7      yes   false  1  return 3

preservation at head 2 -> head 3:
  old I says positions 0 and 1 fail
  old guard says position 2 also fails
  after i <- 3, positions [0,3) all fail, so new I holds

exit split:
  i == n                 -> every position is in the failed prefix -> return None
  i < n and guard false  -> values[i] >= threshold, earlier values fail -> return i
```

#### How to read this visual

The `I?` column is evaluated at one consistent boundary, before the guard. Each true guard supplies
the fact needed to enlarge the processed prefix. The `V` column is not the result summary; it is the
remaining number of candidate positions. The two exit cases come from negating the short-circuit
guard without performing an unsafe access.

#### Key insight

The body does not need to rescan the prefix. The invariant carries its logical meaning from one
iteration to the next, while the current guard contributes exactly one new failed position.

#### Simplification or limitation

The trace prints prefix values for readability. Materializing those prefixes in production would add
copying and storage that the algorithm does not require. The proof assumes `values` is not mutated
while scanning and that each comparison returns consistently.

### Boundary trace: no match

```text
values = [1], threshold = 6

head i=0: I true, i<n true, values[0]<6 true, V=1
update i=1
head i=1: I true, i<n false, second guard operand is not evaluated, V=0
exit: i==n, so every legal position failed; return None
```

This trace exposes why `i < n` must be evaluated before `values[i] < threshold` in Python's
left-to-right short-circuit `and` expression.

## 7. Mechanics and state variables

| State variable or predicate | Meaning | Update rule | Why it is sufficient |
|---|---|---|---|
| `values` | finite input sequence whose order and contents remain fixed | no mutation | stabilizes the domain over which the invariant quantifies |
| `n` | number of legal positions | fixed as `len(values)` | supplies the safety bound and termination limit |
| `threshold` | predicate parameter | fixed | keeps “valid candidate” meaning stable |
| `i` | first not-yet-proven-failing position | start at `0`; increment by one only after current failure | partitions processed `[0,i)` from remaining `[i,n)` |
| `I(i)` | bounds plus “all earlier positions fail” | re-established after every continuing transition | supports safety, completeness, and first-index minimality |
| guard | `i < n and values[i] < threshold` | re-evaluated at each loop head | decides whether the current candidate joins the failed prefix |
| `V = n - i` | remaining candidate positions | decreases by exactly one | proves the loop cannot continue indefinitely |
| result | `i` when in bounds, otherwise `None` | produced only after guard is false | follows from the exit split |

State variables should earn their place. If a fact can be derived cheaply from existing state, storing
another mutable copy can create a stale-summary invariant that is harder to preserve.

## 8. Correctness reasoning

### Preconditions and postcondition

Assume `values` is a finite list of integers, neither `values` nor `threshold` changes during the
function, and integer comparison behaves normally. The required postcondition is: return `None`
exactly when no value reaches the threshold; otherwise return the smallest valid index.

### Safety and partial correctness

- **Initialization:** `i = 0`, so `0 <= i <= n`. The prefix `[0,0)` is empty, making “every earlier
  value is below the threshold” vacuously true.
- **Safe guard evaluation:** Python evaluates `and` left to right and stops after a false operand.
  Therefore `values[i]` is evaluated only when `i < n`; the invariant also supplies `i >= 0`.
- **Preservation:** assume the invariant and guard. The old prefix fails by the invariant, and the
  current position `i` fails by the guard. After incrementing `i`, the enlarged prefix fails. Bounds
  remain valid because the old guard supplied `i < n`.
- **Exit and soundness:** if the loop exits with `i < n`, the bounds check is true but the complete
  guard is false, so `values[i] >= threshold`. Returning `i` is valid.
- **Completeness and minimality:** the invariant says every earlier position fails. Therefore no valid
  index was skipped, and an in-bounds returned `i` is the first one.
- **No-match case:** if the loop exits with `i == n`, the invariant covers `[0,n)`, so every legal
  position fails and `None` is correct.

These steps prove partial correctness: whenever the loop exits, the returned value satisfies the
contract.

### Progress and termination

While the guard is true, `0 <= i < n`, so `V = n - i` is a positive integer. The only continuing
transition changes `i` to `i + 1`, hence changes `V` to `V - 1`. A positive integer cannot decrease
strictly forever. The loop must eventually reach a false guard. Partial correctness plus this
termination argument establishes total correctness for the stated input domain.

### Proof obligations for branching loops

If a loop body has several paths, prove preservation and progress for every path that can return to
the guard. `continue` deserves special attention because it skips later statements in the body. A
branch that preserves the invariant but leaves the ranking measure unchanged can still cause
nontermination; a branch that decreases the measure but corrupts the invariant can terminate with a
wrong answer.

## 9. Complexity derivation

Let `n = len(values)` and let `c` be the maximum cost of one `value < threshold` comparison under
the chosen numeric model.

- The loop inspects at most `n` values. Each completed iteration permanently moves one position from
  the remaining region into the processed prefix.
- Best-case time is `Theta(c)` when position zero is already valid.
- Worst-case time is `Theta(nc)` when no value is valid or only the last value is valid.
- Under the standard fixed-width or bounded-integer comparison model, report `Theta(1)` best case
  and `Theta(n)` worst case.
- Auxiliary space is `Theta(1)`: the proof's quantified prefix is logical and is not materialized.
- Output space is `Theta(1)` for the scalar result.
- Recursion-stack space is zero.

### Instrumentation can change the measured program

Suppose debug code executes this at every head:

```python
assert all(values[j] < threshold for j in range(i))
```

On a full scan it performs `0 + 1 + ... + (n - 1) = Theta(n^2)` additional comparisons. Replacing
the generator with `values[:i]` also allocates a growing slice each time. That instrumentation may be
useful in a tiny trace lab, but its cost is not part of the constant-space production algorithm and
must not be hidden in a complexity claim.

Python integers are arbitrary precision, so comparison cost can depend on integer magnitude in a
bit-cost model. At this unit's interview depth, state the standard constant-cost assumption unless
the prompt makes magnitude a meaningful input variable.

## 10. Implementations

### Generic pseudocode

```text
i <- 0
while i < n and candidate i fails:
    # invariant: [0,i) contains only failed candidates
    i <- i + 1

if i == n:
    return NO_RESULT
return i
```

### Idiomatic Python

```python
def first_index_at_least(values: list[int], threshold: int) -> int | None:
    index = 0
    while index < len(values) and values[index] < threshold:
        index += 1
    return None if index == len(values) else index
```

This spelling mirrors the proof state directly. An equally valid interview implementation can use
`enumerate` and return from the first successful comparison; then the finite iterator supplies the
progress structure, while the processed-prefix meaning remains the correctness invariant.

The runnable [micro-lab](practice/trace_lab.py) exposes loop-head state, preservation, exit reason,
and ranking decrease without creating a learner implementation answer.

### Python 3.11 compatibility

The code uses union syntax and built-ins available in Python 3.11. No Python 3.14-only behavior is
required. Python's `while`, short-circuit Boolean evaluation, and `assert` caveat used here are part
of the language documentation; implementation-specific bytecode is irrelevant to the proof.

### First-principles versus standard-library choice

Use the explicit `while` loop when teaching or defending the boundary and ranking measure. Use
`enumerate` in normal Python when it makes the same state transition clearer. Neither spelling
eliminates the need to explain why an early return is safe or why the no-match path is complete.

## 11. Edge-case matrix

| Dimension | Minimal adversarial case | Expected behavior | Invariant or termination risk |
|---|---|---|---|
| Empty input | `[]`, threshold `6` | return `None` without indexing | guard operands in unsafe order |
| First position valid | `[6]`, threshold `6` | return `0` with zero body iterations | treating initialization as requiring one iteration |
| Equality boundary | `[5, 6]`, threshold `6` | return `1` | using `>` instead of `>=` in the result contract |
| No match | `[1]`, threshold `6` | return `None` after reaching `i == n` | out-of-bounds access at exit |
| Last position valid | `[1, 6]`, threshold `6` | return `1` | stopping one position early |
| Skipped update | `[1, 6]` with `i += 2` | defect must be exposed | processed-prefix invariant is not established for skipped index |
| Stuttering update | `[1]` with no effective increment | loop must not be trusted | ranking measure fails to decrease |
| Mutating input | append while iterating | outside stated contract | `n`, domain, or iterator-exhaustion argument becomes stale |
| Side-effecting comparison | custom objects changing state | outside stated contract | repeated predicates need not have stable truth values |
| Runtime assertions | prefix scan at every head | correct result but extra work | proof instrumentation inflates time to quadratic |
| Early `continue` | progress update placed afterward | possible infinite loop | one branch returns to guard without progress |
| Floating-point `NaN` | comparison contract not specified | clarify semantics first | ordinary trichotomy assumptions fail |

## 12. Comparisons and anti-signals

| Candidate reasoning tool | Use when | Reject or revise when | Evidence required |
|---|---|---|---|
| Loop invariant | a repeated transition must preserve a state relation | the statement is true but cannot imply the postcondition | initialization, every-branch preservation, exit implication |
| Ranking measure | termination depends on monotone progress | it can stay equal, increase, or leave its lower-bounded domain | strict change on every continuing path plus a bound |
| Example trace | discovering state, boundaries, and counterexamples | presented as proof for all inputs | representative and adversarial states, followed by general reasoning |
| Runtime assertion | exposing a violated claim during development | required for input validation or correctness control flow | assertion cost and `-O` behavior acknowledged |
| Test suite | detecting concrete failures and regressions | used as a universal completeness argument | selected cases plus separate proof obligations |
| Postcondition only | specifying the desired final result | it gives no guidance for intermediate state | derive a preservable summary from it |
| Stronger invariant | weaker claim cannot establish the result | it cannot be initialized or maintained | show every added clause earns its proof cost |
| `for` loop | a finite iterable naturally controls progress | the iterable can grow or fail to exhaust | iterator/domain contract remains stable |

Anti-signals include “it obviously works,” “the pointer always moves” without checking every branch,
an invariant stated only after the loop, and a termination claim based on typical inputs rather than
all allowed inputs.

## 13. Common bugs and debugging

| Failure | Symptom | Smallest counterexample | Correction |
|---|---|---|---|
| Guard operands reversed | `IndexError` on a no-match input | `[]` or `[1]` | prove bounds before indexing; place `i < n` first |
| Weak invariant | proof reaches exit but cannot show “first” | `[7, 6]`, threshold `6` | include that every earlier position fails |
| Over-strong invariant | initialization or preservation is impossible | claim “current item is valid” at `i = 0` | keep only facts true at every chosen boundary |
| Wrong boundary | proof alternates between before and after update | `[1, 7]` | name the loop head and use half-open `[0,i)` consistently |
| Update skips state | valid candidate is missed | `[1, 7]` with `i += 2` | show exactly one newly processed state per transition |
| Progress on only one branch | one case loops forever | a `continue` before increment | prove ranking decrease for every returning branch |
| Non-strict measure | measure never increases but may stay equal | `i += 0` | require strict progress, not merely non-regression |
| Exit implication missing | invariant holds but return rule is guessed | empty or no-match case | combine invariant with the negated full guard |
| Assertions treated as validation | invalid input accepted under `python -O` | any assertion-only precondition | raise an explicit exception for required validation |
| Instrumentation cost ignored | trace version appears slower or changes bound | long no-match input | separate diagnostic traversal from algorithm work |
| Mutation breaks domain | newly appended items alter exhaustion | append during list iteration | forbid mutation or restate state/domain invariant |
| Proof of wrong contract | elegant proof returns any match, prompt asks first | `[7, 6]` | restate exact postcondition before choosing invariant |

Debug from the proof structure: find the earliest failed obligation—contract, initialization, safe
guard, preservation, progress, exit implication, soundness, or completeness. That produces a smaller
and more actionable diagnosis than “the loop is wrong.”

## 14. Practice ladder

1. Rewrite vague loop comments as boundary-specific predicates.
2. Predict the supplied micro-lab trace before running it.
3. Mark initialization, preservation, false-guard, and ranking facts on one hand trace.
4. Diagnose an unsafe guard using the smallest empty or no-match input.
5. Diagnose a skipped candidate using a two-element counterexample.
6. Diagnose a non-progress branch without executing an infinite loop.
7. Prove a changed output contract with a revised invariant.
8. Complete the mixed unlabeled state-transition task without receiving a pattern or target bound.
9. Deliver a two-minute interview proof with explicit complexity categories.
10. Reconstruct the proof after 1, 3, 7, 14, and 30 days.

The concrete unsolved tasks are in [practice/README.md](practice/README.md). The current canonical
problem metadata has no owner or intentional secondary problem for `DSA-FND-030`, so this pack uses
original drills rather than relabeling another unit's problem evidence.

## 15. Interview questions, traps, and follow-ups

### Recognition and approach questions

1. When a loop returns the first valid position, what historical fact must its state retain?
2. Starting from the exact postcondition, how would you derive a candidate loop invariant?
3. What is the simplest correct full-enumeration baseline, and which work can an early exit avoid?

### Invariant and correctness questions

1. At what exact program point does your invariant hold?
2. Why is the invariant true before the first iteration, including for empty input?
3. How does each branch preserve every clause of the invariant?
4. What does the invariant combined with the false guard imply at exit?
5. Why is the returned index sound, complete, and minimal?
6. What useful fact is missing from the tempting invariant `0 <= i <= n`?

### Termination and safety questions

1. Which ranking measure proves termination, what bounds it, and why does every continuing branch
   change it strictly?
2. Why does “the index usually increases” fail as a termination proof?
3. Which guard order prevents an out-of-bounds read on the no-match path?

### Complexity questions

1. What are the best- and worst-case time bounds, with `n` and comparison cost stated explicitly?
2. What are the auxiliary, output, and recursion-stack space costs?
3. How can an executable prefix assertion silently change the complexity from linear to quadratic?
4. Why does early exit improve some executions without improving the no-match worst case?

### Changed-constraint follow-ups

1. How must the invariant and output space change if the contract returns every valid index?
2. What changes if the contract asks for the last valid index rather than the first?
3. What changes if values arrive as a one-pass stream and the numeric index is still required?
4. What changes if another thread or callback may mutate the collection during the scan?
5. How would you explain correctness if the loop may stop early after a caller-supplied budget?

### Common traps and weak-answer repairs

- Trap: “The invariant is that `i` increases.” That is an update fact, not the semantic claim that
  connects state to the result; it also does not prove bounds or strict progress on every branch.
- Trap: “The tests pass, therefore the algorithm is correct.” Tests can reveal counterexamples but
  do not quantify over every allowed state.
- Weak answer: “It is `O(n)` because there is one loop.” Repair it by naming `n`, counting at most
  `n` comparisons, separating best and worst cases, and reporting auxiliary/output/stack space.
- Weak answer: “It terminates when the condition becomes false.” Repair it by proving why a
  well-founded measure must force that condition to become false.

## 16. Explanation exercises

1. Explain the scan in under two minutes using contract, invariant, exit implication, ranking
   measure, and complexity—without reciting code line by line.
2. Explain why `0 <= i <= n` is necessary for safety but insufficient for minimality.
3. Defend the half-open prefix `[0,i)` using the empty initial state and one preservation step.
4. Give the smallest counterexample for each defective update in the practice task and name the
   first failed proof obligation.
5. Recalculate proof and complexity when the output changes from one index to all valid indices.
6. Explain why a finite trace can falsify a claimed invariant but cannot prove it for every input.

## 17. Experiment decision

Decision: no separate experiment is created. `DSA-FND-030` has no `X` or `(X)` evidence marker,
elapsed runtime is not central, and observing finitely many successful runs cannot establish a
universal invariant or termination claim. The deterministic [micro-lab](practice/trace_lab.py)
already provides the useful observation: loop-head state, guard outcome, invariant checks, and
ranking decrease on small cases. A benchmark would add noise without satisfying the missing proof
obligations.

## 18. Vocabulary and professional English

### Invariant

| Item | Content |
|---|---|
| Pronunciation | in-VAIR-ee-uhnt |
| Simple English meaning | a fact that remains true through specified changes |
| Hindi cue | badlav ke dauran sthir satya |
| Meaning here | a state predicate true at the selected loop boundary before and after every iteration |

Examples:

1. The total quantity is invariant under the exchange.
2. Ownership is an invariant of this state transition.
3. The invariant describes the processed prefix, not the next element.
4. **Interview:** “My loop invariant is that every index before `i` has already failed the predicate.”
5. **Engineering discussion:** “This refactor preserves the cache-coherence invariant on every
   update path.”

### Preserve

| Item | Content |
|---|---|
| Pronunciation | pri-ZURV |
| Simple English meaning | keep something true or unchanged through an action |
| Hindi cue | banaye rakhna |
| Meaning here | show that one legal transition re-establishes the invariant |

Examples:

1. The container preserves insertion order.
2. The migration preserves existing identifiers.
3. Incrementing by one preserves the meaning of the processed prefix.
4. **Interview:** “Assuming the invariant at the loop head, this branch preserves both bounds and
   candidate coverage.”
5. **Engineering discussion:** “The retry must preserve idempotency even after a timeout.”

### Terminate

| Item | Content |
|---|---|
| Pronunciation | TUR-muh-nayt |
| Simple English meaning | come to a definite end |
| Hindi cue | samapt hona |
| Meaning here | reach a state where no further loop transition occurs for every allowed input |

Examples:

1. The agreement terminates at the end of the month.
2. The worker terminates after receiving the shutdown signal.
3. A non-negative ranking value that strictly decreases supports a termination proof.
4. **Interview:** “The loop terminates because `n - i` decreases by one and cannot become negative.”
5. **Engineering discussion:** “A retry loop needs an explicit bound or cancellation rule to
   terminate under persistent failure.”

## 19. Python Mastery references

These are supporting references, not additional curriculum prerequisites:

- [PY-BLT-040 — Lists, tuples, ranges, and sequence behaviour](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-blt-040) — indexing, half-open ranges, and sequence mutation assumptions.
- [PY-TST-020 — Pytest fundamentals and fixtures](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-tst-020) — running the deterministic micro-lab tests.
- [PY-TST-050 — Property-based testing, coverage, and mutation concepts](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-tst-050) — later testing evidence that complements but does not replace proof.
- [PY-MPR-070 — Algorithmic and memory complexity](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mpr-070) — explicit input variables and separate space categories.

The minimum Python bridge is: list indices are `0` through `n - 1`; `range(i)` represents the
half-open integers `[0,i)`; Boolean `and` short-circuits left to right; and required input validation
must not depend on `assert`.

## 20. Authoritative sources

- [Cornell CS 2112 — Loop invariants](https://www.cs.cornell.edu/courses/cs2112/2012fa/lectures/lec20.html) — consulted for the initialization, maintenance, postcondition, and termination proof structure and the distinction between partial and total correctness.
- [MIT OpenCourseWare 6.042J — State Machines: Invariants and Termination](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/9ecca71877aba37f609292c8ff94d44e_ln7.pdf) — consulted for invariant-based partial correctness and natural-number decreasing measures for termination.
- [Python 3.14 language reference — Compound statements](https://docs.python.org/3.14/reference/compound_stmts.html#the-while-statement) — consulted for `while` repetition, `for` exhaustion, `break`, and `continue` semantics.
- [Python 3.14 language reference — The `assert` statement](https://docs.python.org/3.14/reference/simple_stmts.html#the-assert-statement) — consulted for assertion semantics and the fact that assertion code can be omitted under optimization.

All explanations, traces, exercises, and code in this unit are original repository material. No
problem statement, editorial, textbook proof, or proprietary interview content is reproduced.
