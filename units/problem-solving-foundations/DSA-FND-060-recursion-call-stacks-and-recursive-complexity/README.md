# DSA-FND-060 — Recursion, call stacks, and recursive complexity

## Physical Notebook Core

**Pressure:** the same question applies to a smaller input, but the caller still has work to
finish when the smaller answer returns.

> Each call keeps its own unfinished work while a strictly smaller call produces an answer.

```text
Shared input: [7, -2, 4]; S(k) means the sum of the first k values.

descent:  S(3) -> S(2) -> S(1) -> S(0)
returns:     9 <-    5 <-    7 <-    0
waiting:   add 4    add -2   add 7    base
```

#### How to read this visual

Follow calls rightward, then returned values leftward. A caller pauses; its local prefix size
does not change when another call receives a different size.

#### Key insight

There are four calls and at most four active calls here. For a branching computation those
counts can differ greatly: **time counts all work; stack space counts simultaneous unfinished work**.

#### Simplification or limitation

The picture shows logical Python calls, not byte addresses or a literal native stack. Integers
are treated as bounded words; it omits tracing output and interpreter overhead.

**Rules:** define what one call returns; handle the smallest valid input before indexing;
make every child strictly smaller; use each returned answer exactly as the contract requires.

```text
S(0) = 0
S(k) = S(k - 1) + values[k - 1], for k > 0
```

- Input: `n` list elements; `h` maximum active calls, including the base call.
- Dominant work: `n` additions and `n+1` calls. Time `Theta(n+1)`.
- Auxiliary space including the stack: `Theta(n+1)`; non-stack bookkeeping `O(1)`.
- Output: one scalar, `O(1)` words. Stack: `h=n+1` constant-size logical frames.
- Python cost: passing the same list shares it; taking a new tail slice copies references.
- Cue: smaller instances have the same contract. Anti-cue: potentially huge depth with a simple loop.
- Comparison: a recursion tree shows all calls; a call-stack snapshot shows one active path.
- Failure: “one recursive line means constant space.” Count the unfinished callers.

Recall: What exactly does a call promise? What decreases? What stays alive while it waits?

| Field | Value |
|---|---|
| Domain | Problem-solving foundations |
| Curriculum | [CURRICULUM.md](../../../CURRICULUM.md#dsa-fnd-060) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Pattern index | [PATTERN_INDEX.md](../../../PATTERN_INDEX.md) |
| Problem bank | [PROBLEM_BANK.md](../../../PROBLEM_BANK.md) |
| Primary outcome | Trace recursive calls, derive base cases and progress, and account for recurrence cost and recursion-stack space. |
| Hard prerequisites | DSA-FND-030, DSA-FND-040 |
| Soft prerequisites | None |
| Priority | Core |
| Interview frequency | High |
| Practical relevance | High |
| Python relevance | High |
| Difficulty | 3 |
| Depth | D2 |
| Scope | Foundations, Recursion, Complexity |
| Size | L |
| First understanding | 4–7 h |
| Hands-on practice | 8–14 h |
| Evidence | E+T+I+P+D+R+M |
| Artifact state | Draft |
| Canonical Python | 3.14 |
| Interview compatibility | 3.11 |

## 1. Learning outcomes and evidence

After study, Rahul should be able to:

1. define a recursive call's input and return meaning before writing its body;
2. derive base cases and a decreasing measure from the input contract;
3. trace descent, suspension, return values, and resumed work without merging different frames;
4. derive work recurrences from the calls actually executed and their local operations;
5. distinguish total calls, maximum active depth, retained buffers, and returned output;
6. implement and test small recursive functions, then explain when iteration is safer;
7. recover a proof, diagnose a recursion bug, and transfer the reasoning after a delay.

| Evidence | Required learner artifact |
|---|---|
| E, T | Predict a complete call/return trace and explain every waiting caller. |
| I | Attempt both protected implementations in [practice](practice/README.md). |
| P, D | Justify termination and correctness; repair a false cost or boundary claim. |
| R | Complete the dated closed-book prompts in [REVIEW.md](REVIEW.md). |
| M | Attempt the unlabeled task without advance method guidance. |

The curriculum does not require `X`, but two supplementary experiments make runtime costs
observable. Their recorded maintenance runs do not count as Rahul's evidence. Initialization
and publication leave the learning state **Not started**.

There are no problem-bank entries owned by or assigned secondarily to this unit. The practice
ladder therefore uses original local tasks. Tree algorithms, backtracking, binary search,
and dynamic programming retain their own later units; this pack does not initialize them.

## 2. Prerequisite bridge

Both hard prerequisites currently have learning state `Not started`; no mastery is assumed.

| Prerequisite | Minimum bridge before the first trace |
|---|---|
| [DSA-FND-030 — Invariants, correctness, and termination](../../../CURRICULUM.md#dsa-fnd-030) | A contract says what a call promises. Prove a smallest case directly, preserve the promise using smaller correct calls, and give a nonnegative measure that strictly decreases. |
| [DSA-FND-040 — Asymptotic notation and input-variable modeling](../../../CURRICULUM.md#dsa-fnd-040) | Name the input size, count dominant operations, add sequential work, and separate upper bounds from tight bounds. Space means maximum simultaneous live storage. |

Python bridge: each invocation has its own parameter bindings; those bindings can refer to the
same list. Returning a value finishes the current invocation. An ordinary function that reaches
its end without a return value produces `None`. A half-open interval includes its left bound
and excludes its right bound. A bridge permits preparation without advancing prerequisite states.

## 3. Intuition and problem shape

Imagine asking someone to total the first two receipts while you keep the third receipt ready.
When they return a subtotal, you add your receipt and hand back the answer. They may do the same
with a still smaller pile. You need a rule for an empty pile so the chain eventually stops.

Start with constraints: a finite list of integers, an exact sum, no input mutation, and shallow
examples for hand tracing. The empty list should total zero. For `[7, -2, 4]`, adding the last
value to the first two values' sum gives nine. This is a useful teaching decomposition, although
a loop or `sum(values)` is usually the simpler real implementation.

Recursion is a way to express dependencies, not an optimization by itself. The questions are:
does the smaller call have the same meaning, does its input shrink, and what does the caller
still need after it returns? Python's execution model describes frames that preserve execution
context; the diagrams here are a conceptual rendering of that model.
[Python execution model](https://docs.python.org/3.14/reference/executionmodel.html#structure-of-a-program)

## 4. Brute force and bottleneck

### Simplest correct baseline

A direct “first item plus the rest” definition can construct a fresh rest-list on every call:

```python
def copied_sum(values: list[int]) -> int:
    if not values:
        return 0
    child_total = copied_sum(values[1:])
    return values[0] + child_total
```

This teaching example is for small inputs. It is not either protected practice task.
The base case answers an empty list directly; each other call delegates a strictly shorter list.

### Exact bottleneck

For length four, slice lengths are `3, 2, 1, 0`. The program adds only four integers, but copies
six references. At length `n`, copies total `(n-1)+(n-2)+...+1 = n(n-1)/2`.
Those shorter lists also remain reachable through waiting callers.

The representation is causing repeated work. Keep the original list and describe the remaining
problem using a bound. This removes slice copies, while recursive callers still consume space.
An iterative accumulation can additionally remove the growing recursion stack.

## 5. Derivation and invariant

Choose `S(k)` to mean **the sum of the first `k` elements of the unchanged original list**,
where `0 <= k <= n). That meaning must remain fixed throughout the trace.

1. For `k=0`, there are no values to add, so the result is zero.
2. For `k>0`, the first `k` elements consist of the first `k-1` plus element `k-1`.
3. Ask the smaller call for exactly its promised subtotal.
4. Add the one element not covered by that subtotal and return the result.

**Entry invariant:** the original list is unchanged and the current bound describes a valid
prefix. **Return contract:** the result equals the sum of that prefix. **Progress measure:**
`k` decreases by one and cannot decrease forever while nonnegative.

The correctness assumption applies only to smaller inputs. “It calls itself, therefore it
works” is circular; “the smaller correct answer plus the missing element gives this answer”
is an inductive argument. For branching calls, establish that the children cover the intended
parts and explain whether those parts are disjoint or deliberately overlap.

## 6. Detailed visual trace

### Descent and unwinding on one shared list

```text
event       active prefix sizes       returned value / unfinished work
call 3      [3]                       wait for S(2), then add values[2]
call 2      [3, 2]                    wait for S(1), then add values[1]
call 1      [3, 2, 1]                 wait for S(0), then add values[0]
call 0      [3, 2, 1, 0]              base case
return 0    [3, 2, 1, 0]              0
return 1    [3, 2, 1]                 0 + 7  = 7
return 2    [3, 2]                    7 + -2 = 5
return 3    [3]                       5 + 4  = 9
finished    []                        answer handed to the outer caller
```

#### How to read this visual

Read downward. The rightmost prefix size is the current call. A return row is recorded before
that frame leaves the stack. The next row resumes its caller, not a fresh call.

#### Key insight

`k=3`, `k=2`, and `k=1` are different local bindings. All refer to the same input list;
none represents an automatic copy of it. The lab emits the eight call/return rows above.

#### Simplification or limitation

Only unit-function invocations are counted. The module, lab wrapper, interpreter, temporary
arithmetic objects, and printing calls are not part of `max_active`.

### A recursion tree is not one stack snapshot

```text
Both halves run, sequentially; stop at size 1.

                    4
                  /   \
                 2     2
                / \   / \
               1   1 1   1

One instant during the leftmost descent: [4, 2, 1]
All invocations over the whole run: 7
Maximum active invocations:         3
```

#### How to read this visual

Each node is a separate invocation, even when labels match. Execute the whole left subtree,
return, and then execute the right subtree. Labels are input sizes, not unique call identifiers.

#### Key insight

Sequential siblings contribute to total work but do not occupy two active recursion paths.
A result returned by the left child may still be retained when the right child runs.

#### Simplification or limitation

The tree assumes constant local work and no stored history or large returned buffers. It is
not automatically a merge-sort time or memory model; merge work would need its own charge.

### Retained data can exceed the frame count

```text
At the deepest point of copied_sum on four values:
original input (borrowed)      4 references
first copied tail             3 references
second copied tail            2 references
third copied tail             1 reference
empty copied tail             0 references

active sum calls: 5       extra copied payload slots: 3 + 2 + 1 = 6
```

#### How to read this visual

Count each distinct list once. The parent reference to a child list and the child's parameter
refer to the same copied list; they do not create two copies of its payload.

#### Key insight

The `n+1` frames are linear, while the simultaneously retained slice payload is quadratic.

#### Simplification or limitation

The count excludes original input, list headers, frame storage, and integer-object sizes.
Slices copy references, not the integer objects. The empty slice still has a list object.

## 7. Mechanics and state variables

| State | Meaning | Lifetime or update | Why needed |
|---|---|---|---|
| `values` | One shared input list | Unchanged for the whole computation | Supplies the values without constructing sublists. |
| `size` | Prefix owned by this call | A new local binding per invocation | Defines both its contract and decreasing measure. |
| `child_total` | Returned result for the smaller prefix | Exists after the child finishes | Connects the child's promise to the parent's result. |
| Resume position | Work to do after the child returns | Retained by the waiting frame | Distinguishes descent from combination. |
| Lab `active` | Explicit list of currently active prefix sizes | Append on entry; pop after the return snapshot | Makes conceptual stack state observable. |
| Lab `events` | Immutable snapshots of the run | Retained for display | Teaching output, not necessary algorithm state. |

In a two-child routine a frame may also retain the first result, which child comes next,
and any buffer being built. Converting such a routine to an explicit stack must preserve this
information; merely pushing input nodes is insufficient for every return-value computation.

## 8. Correctness reasoning

- **Initialization:** the outer call uses the valid full-prefix bound `n`.
- **Base case:** the empty prefix has sum zero; no indexing occurs first.
- **Preservation:** when `k>0`, the child bound `k-1` is valid and the list stays unchanged.
- **Inductive step:** assuming the child returns the first `k-1` elements' sum, adding
  `values[k-1]` yields the first `k` elements' sum.
- **Progress and termination:** the nonnegative integer `k` strictly decreases until zero.
- **Completeness:** the smaller prefix and final element cover every required position once.
- **Safe exclusion:** positions from `k` onward are outside this call's declared prefix.
- **Final-state argument:** at the outer return `k=n`, so the returned scalar answers the
  original contract.

Termination and correctness are separate: a function that always returns zero terminates but
is generally wrong. A mathematically terminating recursive definition may still exceed an
interpreter's supported depth before reaching its base case.

## 9. Complexity derivation

### Name the variables and count local work

Let `n` be the initial problem size, `C(n)` total invocations including base calls, and `h`
maximum simultaneously active invocations. A local cost excludes its children's work.
Under a bounded-word model, indexing, small integer arithmetic, and a fixed amount of frame
bookkeeping take constant time. Then:

```text
total time = sum of local costs over all invocations
peak space = maximum live frame state + distinct live buffers + stored output
```

Read the first line across the entire execution and the second at each instant. The distinction
prevents adding memory from sibling calls that finished at different times. The formulas are
accounting rules, not guarantees that local work or per-frame data is constant.

### Derive representative recurrences

The following bounds use constant-cost base cases; logarithms are base two. The branching
rows run their children sequentially and retain only bounded bookkeeping unless stated otherwise.

| Calls and local work | Time recurrence | Tight time for growing `n` | Active stack |
|---|---|---|---|
| One child smaller by one; constant local work | `T(n)=T(n-1)+Theta(1)` | `Theta(n)` | `Theta(n)` |
| One half-size child; constant local work | `T(n)=T(floor(n/2))+Theta(1)` | `Theta(log n)` | `Theta(log n)` |
| Both disjoint halves; constant local work | `T(n)=T(floor(n/2))+T(ceil(n/2))+Theta(1)` | `Theta(n)` | `Theta(log n)` |
| Both halves; linear local work | `T(n)=2T(n/2)+Theta(n)` for powers of two | `Theta(n log n)` | `Theta(log n)`; buffers require a separate audit |
| Two children each smaller by one; no reuse | `T(n)=2T(n-1)+Theta(1)` | `Theta(2^n)` | `Theta(n)` |
| One child smaller by one; copy the remaining list | `T(n)=T(n-1)+Theta(n)` | `Theta(n^2)` | `Theta(n)`; copied payload also reaches `Theta(n^2)` |

For empty and tiny inputs, use the base cost rather than interpreting `log 0`. Unified chain
bounds are `Theta(n+1)`; unified halving bounds are `Theta(1+log(n+1))`.

Derive these rather than matching code shapes:

1. **Chain:** `n` nonbase calls plus one base call, so `C(n)=n+1`.
2. **One half:** after `j` edges, size is `floor(n/2^j)`. For `n>=1`, stopping at
   size one takes `floor(log2 n)` edges and one more frame than edges.
3. **Both halves:** there are `n` unit-size leaves for `n>=1`. A full binary tree with
   `n` leaves has `n-1` internal nodes, so `C(n)=2n-1`. Its height in active frames is
   `ceil(log2 n)+1`. Constant work per node therefore gives linear total time.
4. **Linear combination at each level:** at depth `j`, `2^j` nodes each do work
   proportional to `n/2^j`. Each nonleaf level costs `Theta(n)`; there are
   `log2 n` such levels, plus linear leaf work.
5. **Repeated decrement:** depth `j` has `2^j` calls. Summing through depth `n`
   gives `2^(n+1)-1` calls, yet only `n+1` are on the deepest active path.

A halved input does not by itself imply logarithmic time. Count how many halved calls execute.
`2 * f(n // 2)` makes one child call; `f(n // 2) + f(n // 2)` makes two without caching.
Memoization can remove repeated states when the contract permits it, but introduces retained
state and does not generally remove the deepest dependency chain. Its full treatment belongs
to [DSA-DP-020](../../../CURRICULUM.md#dsa-dp-020).

### Separate algorithm space from trace output

The unsliced prefix sum uses `Theta(n+1)` stack words, `O(1)` additional non-stack state,
and `O(1)` output words. Reusing an input list does not make the algorithm constant-space.

The micro-lab saves two snapshots at every active depth. Their payload lengths sum to
`2(1+2+...+(n+1))=(n+1)(n+2)` references. Its returned trace therefore adds
`Theta(n^2)` output storage and snapshot-copy time. Do not attribute that tracing cost to
the plain sum.

Likewise, sequential balanced recursion can copy a linear amount at every level and thus
allocate `Theta(n log n)` references over its lifetime while retaining only `Theta(n)`
copied payload at a time. For conventional local half-slices, the simultaneously live lengths
along a descent form a geometric sum. This conclusion depends on releasing completed branches
and not saving their full histories or large intermediate outputs.

### Python costs and runtime limits

List slices are shallow copies. In CPython 3.14.7, the list-slice implementation allocates a
new result and copies each selected reference, supporting `Theta(k)` work and payload for
a slice of length `k`. This is implementation cost evidence, not a byte-size language guarantee.
[Sequence copying](https://docs.python.org/3.14/library/stdtypes.html#mutable-sequence-types),
[CPython list implementation](https://github.com/python/cpython/blob/v3.14.7/Objects/listobject.c)

Python integers have arbitrary precision. If input magnitudes need up to `B` bits, prefix sums
can need `O(B+log(n+1))` bits. The additions alone have an upper bound of
`O(n(B+log(n+1)))` bit work using ordinary linear-cost addition. The word-model time and
space claims above do not promise constant-cost arithmetic or constant-byte integer objects
when magnitudes grow.
[Numeric types](https://docs.python.org/3.14/library/stdtypes.html#numeric-types-int-float-complex)

Read the current recursion limit with `sys.getrecursionlimit()`; do not assume an exact safe
input size from that number. Existing callers and the execution environment matter.
Raising the limit is not a proof of safe resource use, and an excessive value can crash Python.
The provided scripts keep inputs small and never change that setting.
[Recursion-limit API](https://docs.python.org/3.14/library/sys.html#sys.setrecursionlimit)

CPython does not eliminate recursive Python calls merely because they are in tail position.
The optional tail-call interpreter introduced in Python 3.14 concerns internal C functions,
not tail-call optimization of user Python functions.
[Python 3.14 interpreter note](https://docs.python.org/3.14/whatsnew/3.14.html#new-type-of-interpreter)

## 10. Implementations

### Generic pseudocode

```text
solve(state):
    if state is a base case:
        return its directly justified answer
    describe strictly smaller state(s)
    obtain their answer(s)
    finish the caller's remaining work and return its promised result
```

This is a reasoning outline, not an instruction to recurse whenever a loop would suffice.

### Idiomatic Python teaching example

```python
def prefix_total(values: list[int], size: int) -> int:
    """Sum the first size elements; precondition: 0 <= size <= len(values)."""
    if size == 0:
        return 0
    child_total = prefix_total(values, size - 1)
    return child_total + values[size - 1]
```

Use only shallow, valid inputs for this teaching function. In ordinary application code,
`sum(values)` answers the full-list contract without a growing Python recursion stack.
The provided [micro-lab](practice/micro_lab.py) adds bounded, observable call/return events.
The two learner functions in [starter.py](practice/starter.py) remain unsolved.

From the repository root:

```bash
uv sync --group dev --locked
cd units/problem-solving-foundations/DSA-FND-060-recursion-call-stacks-and-recursive-complexity
uv run --group dev python practice/micro_lab.py
uv run --group dev python -m pytest -q practice/test_examples.py experiments
uv run --group dev python -m compileall -q practice experiments
uv run --group dev python -m pytest --collect-only -q practice/test_challenge.py
```

The last command checks collection, **not challenge success**. Do not replace it with a
blanket test run while the learner functions still raise `NotImplementedError`.
If the host restricts the default uv cache, use a writable `UV_CACHE_DIR`; no repository
configuration change is necessary.

### Python 3.11 compatibility

All shipped code uses syntax and standard-library APIs available in Python 3.11. The recursive
`Packet` alias intentionally uses `TypeAlias`, not the Python 3.12 `type` statement.
Canonical execution is verified on CPython 3.14.7; a Python 3.11 grammar check alone does not
establish a Python 3.11 runtime test.

### First-principles versus standard-library choice

Build the trace to understand suspension and returns. Use built-ins or loops for ordinary flat
aggregation when they express the contract clearly. For deeply nested work, an explicit stack
can move pending state into ordinary data structures, but it does not make necessary storage
disappear. An accumulator-style linear traversal may need only constant state; a general
branching traversal may still need a stack and saved partial results.

## 11. Edge-case matrix

| Dimension | Minimal adversarial case | Expected behavior | Risk exposed |
|---|---|---|---|
| Empty input | `[]`, prefix size zero | Return zero before indexing | Base case placed after an invalid access. |
| Smallest nonempty | `[7]` | One addition after the empty-prefix return | Skipping the last real item. |
| Sign and cancellation | `[7, -7]` | Return zero with both items included | Mistaking a zero result for an unvisited state. |
| Repeated values | `[2, 2]` | Count both positions | Treating equal values as identical calls. |
| Valid bounds | Prefix size equals list length | Last access is `size-1` | Using the exclusive bound as an index. |
| Invalid bounds | Negative size or size beyond list length | Reject at an API boundary or state a precondition | A decreasing number alone does not prove it reaches the base. |
| Halving boundary | Sizes zero, one, two, three | Stop before generating a nonshrinking size-one child | Wrong base for floor/ceiling division. |
| Many calls, shallow depth | Both halves on eight items | Count every node but only one active descent | Adding sibling depths as stack space. |
| Few branches, large depth | A long decrementing chain | Assess runtime limits before using recursion | Confusing finite with safely executable. |
| Mutable referenced input | Caller and child share a list | Follow the mutation contract explicitly | Assuming each frame receives a private list. |
| Representation cost | Tail slicing | Charge copied references and retention | Counting only arithmetic and frames. |

## 12. Comparisons and anti-signals

| Candidate | Use when | Reconsider when | Question to ask |
|---|---|---|---|
| Recursive calls | Smaller-instance contracts clarify composition | Depth can be large or a flat loop is clearer | What does the caller still need after the return? |
| A loop with accumulators | State can summarize all prior work | Pending branches or return-dependent work must be remembered | Is the accumulator sufficient to preserve the contract? |
| Explicit stack | Deep pending work must avoid Python call-depth limits | It adds complexity without solving a real constraint | Which locals, return positions, and partial answers must be saved? |
| Memoization | The same pure subproblem is solved repeatedly | States are disjoint or keys omit relevant state | What is reused, and how much memory remains retained? |
| Copied subinputs | Isolation is required by the contract | Bounds can express the same subproblem safely | Are copy costs and ownership intentional? |

Algorithmic recursion is broader than a particular implementation's native stack. Never infer
physical C-stack bytes from the number of Python-level calls in these diagrams.

## 13. Common bugs and debugging

| Failure | Small counterexample or symptom | Repair in the reasoning |
|---|---|---|
| Base only at `size==1` | Empty input keeps decreasing or indexes badly | Cover every smallest valid input. |
| Forget to return the child's answer | A caller receives `None` | Follow the return contract through every control path. |
| Recurse with the same state | `visit(1)` calls `visit(1)` forever | Exhibit a strict decrease on every recursive edge. |
| Read `values[size]` | One-element list raises `IndexError` | Translate the prefix count into its last valid index. |
| Use one global accumulator across runs | A second call includes the first call's total | Specify ownership and lifetime of mutable state. |
| Say “two calls means exponential” | Two disjoint half-size calls | Account for sizes, number of nodes, and local work together. |
| Say “halving means logarithmic” | Both halves execute | Count all branches, not only the longest one. |
| Say “stack equals total calls” | Full tree with seven calls and depth three | Trace one instant of active execution. |
| Ignore slices or saved outputs | Identical call counts, very different allocation peaks | Audit objects retained by each waiting frame. |
| Fix every depth failure by raising a limit | Resource use remains large | Reconsider the algorithm and representation first. |

Debug with the smallest failing case. Write entry state, expected child contract, actual child
return, and the first mismatching combination. Do not begin by printing a huge recursion tree.

## 14. Practice ladder

Use [practice/README.md](practice/README.md) for full contracts and locked hints.

1. Concept micro-drill: separate calls, active frames, and retained input references.
2. Hand trace: predict DSA-FND-060-P01 before running the micro-lab on a fresh tiny input.
3. Guided derivation: state the interval contract for DSA-FND-060-P02; request at most one hint.
4. Independent implementation: attempt DSA-FND-060-P02 and DSA-FND-060-P03 in the starter.
5. Changed constraint: explain how a very large interval changes your implementation choice.
6. Confused-cost comparison: repair the analysis cards in DSA-FND-060-P04.
7. Mixed unlabeled task: attempt DSA-FND-060-P05 without assuming a method from this unit.
8. Timed interview: spend 25 minutes on DSA-FND-060-P05, including explanation and testing.
9. Delayed re-solve: reconstruct a previous attempt from its contract after at least one day.
10. Unseen transfer: use the 7-day and 30-day questions in REVIEW.md.

No algorithm, target bound, intended structure, or invariant is disclosed for the mixed task.
Attempts, hint history, and evidence stay distinct from generated material.

## 15. Interview questions, traps, and follow-ups

### Recognition and approach questions

1. What about a problem's contract makes a smaller instance meaningful?
2. For a flat list total, why might a loop be preferable despite a valid recursive definition?
3. What repeated work does the copied-tail baseline perform beyond its additions?

### Invariant and correctness questions

1. What is the exact invariant or return promise of `prefix_total(values, size)`?
2. Which base cases follow from allowing empty inputs?
3. What measure decreases on every edge, including every branch?
4. How does the smaller correct answer imply the caller's correct answer without circularity?

### Complexity questions

1. How would you derive the complexity of two half-size calls with constant local work?
2. How does linear combination work at every internal node change that derivation?
3. Why can exponential call count coexist with linear recursion-stack space?
4. What Python operation can make one shrinking call per element quadratic?
5. Which previously returned results remain alive during the next child call?

### Changed-constraint follow-ups

1. What would you change if nesting depth could reach hundreds of thousands?
2. What if inputs were a one-pass stream rather than a random-access list?
3. What if each call returned a growing list instead of a scalar?
4. What if repeated references represented one shared object to count once, instead of
   separate occurrences to count repeatedly?

### Common traps and weak-answer repairs

- Trap: “There are two calls, so the time is exponential.” What are their sizes and local costs?
- Trap: “No list is allocated, so space is constant.” Which waiting frames still exist?
- Weak answer: “The base case makes it correct.” Explain both termination and composition.
- Weak answer: “Python 3.14 supports tail calls.” Which interpreter feature is being confused
  with Python-function tail-call elimination?

## 16. Explanation exercises

1. In 90 seconds, explain the receipt subtotal model and hand-trace its returns without
   opening the code. Name exactly what each caller is waiting for.
2. In two minutes, defend a base case and a decreasing measure, then show a terminating but
   incorrect function to separate the two obligations.
3. Explain why the seven-node tree has a maximum of three active calls. Include the lifetime
   of a first child's saved result before discussing memory.
4. Recalculate time, auxiliary, output, and stack space when every call copies a tail list.
5. Explain why the recorded allocation bytes are an observation, while the copy-count formula
   follows from the program's operations.

## 17. Experiment decision

Created two supplementary experiments because call-depth behavior and retained Python objects
are central here, even though the canonical evidence profile has no `X`:

- [DSA-FND-060-X01 — Calls and depth](experiments/DSA-FND-060-X01-calls-and-depth/README.md)
  counts actual invocations for four bounded shapes and reads the runtime's recursion limit.
- [DSA-FND-060-X02 — Slices and retained data](experiments/DSA-FND-060-X02-slices-and-retained-data/README.md)
  holds the result and logical depth constant while changing subinput representation.

The scripts neither search for a crash threshold nor increase the recursion limit. Exact copy
counts are model evidence; traced allocation bytes are environment-specific observations.
Both experiments contain predictions, reproduction commands, maintenance observations, and limits.

## 18. Vocabulary and professional English

**Suspend** (suh-SPEND): pause work while keeping enough information to continue; Hindi cue:
अस्थायी रूप से रोकना. General examples: suspend a meeting, suspend a download, suspend a task
until its input arrives. Interview: “The caller is suspended while the child computes.”
Engineering: “We must preserve the state needed to resume this operation.”

**Unwind** (un-WYND): return through pending layers in reverse order; Hindi cue: परतों से वापस
लौटना. General examples: unwind a cable, unwind a sequence of temporary changes, unwind after
a busy day. Interview: “During unwinding, each caller combines the returned subtotal.”
Engineering: “Normal returns and exceptions both affect which frames remain active.”

## 19. Python Mastery references

These are the exact cross-references recorded in [PYTHON_REFERENCES.md](../../../PYTHON_REFERENCES.md);
the DSA pack works without a local Python Mastery clone.

- [PY-FIT-060 — Recursion and iterative alternatives](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-fit-060):
  function-call mechanics and alternatives.
- [PY-FND-020 — Objects, names, references, and mutability](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-fnd-020):
  shared inputs versus separate local bindings.
- [PY-BLT-040 — Lists, tuples, ranges, and sequence behaviour](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-blt-040):
  sequence bounds and copying.
- [PY-MPR-070 — Algorithmic and memory complexity](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mpr-070):
  explicit cost models and live storage.

## 20. Authoritative sources

Read on 2026-08-30. Explanations, diagrams, exercises, counters, and tests are original.
No external exercise statement, editorial, or solution has been copied.

| Source | Classification and use |
|---|---|
| [Python execution model](https://docs.python.org/3.14/reference/executionmodel.html) | Language model: blocks, frames, and name bindings. Diagrams are conceptual. |
| [Python built-in types](https://docs.python.org/3.14/library/stdtypes.html) | Standard contracts: sequence copies and arbitrary-precision integers. |
| [Python sys documentation](https://docs.python.org/3.14/library/sys.html#sys.getrecursionlimit) | Standard-library API: current recursion limit and the risks of changing it. |
| [Python 3.14 interpreter note](https://docs.python.org/3.14/whatsnew/3.14.html#new-type-of-interpreter) | CPython detail: internal tail calls do not eliminate recursive Python calls. |
| [CPython 3.14.7 list implementation](https://github.com/python/cpython/blob/v3.14.7/Objects/listobject.c) | Implementation evidence: a slice allocates and copies selected references. |
| [Python tracemalloc documentation](https://docs.python.org/3.14/library/tracemalloc.html) | Tool contract: traced-allocation peaks are not complete process-memory measurements. |
