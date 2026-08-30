# DSA-FND-040 — Asymptotic notation and input-variable modeling

## Physical Notebook Core

**Pressure:** a short loop can hide expensive work, and two nested loops need not use the same
input size. Before naming a bound, say what grows and what you count.

> Complexity is a bound on a named resource function under an explicit input and cost model.

```text
Three rows, two columns; one mark means one body visit.

                 j=0  j=1       visits after this row
i=0               x    x                2
i=1               x    x                4
i=2               x    x                6

n rows, m marks per row -> n*m visits
```

#### How to read this visual

Read across each row, then downward. The two axes are independent input dimensions. Count marks,
not lines of source code.

#### Key insight

The exact body count is `nm`. It becomes a quadratic function of `n` only after a justified
relationship such as `m = n` is supplied.

#### Simplification or limitation

Marks omit loop guards, setup, and Python integer costs. When `m = 0`, there are no marks, but the
outer loop still runs `n` times. Counted events and total runtime are different quantities.

**Rules:** define inputs and representation; choose a resource and case; count work; prove the
bound. `O` is an eventual upper bound, `Omega` a lower bound, and `Theta` both for the same function.
They do not mean worst case, best case, and average case respectively.

```python
visits = 0
for i in range(n):
    for j in range(m):
        visits += 1
```

Invariant: after `r` complete rows, `visits = r*m`; each row adds exactly `m` visits.

- Input variables: non-negative dimensions `n` and `m`; bounded-cost integer operations assumed.
- Time: `Theta(1 + n + nm)` including empty dimensions; `Theta(nm)` when both are positive.
- Auxiliary space: `Theta(1)` words; output: one scalar, `Theta(1)` words; recursion stack: zero.
- Python cost: `range` does not materialize all its values, but a list slice copies references.
- Cue: independent sizes, dependent loop limits, early exits, or hidden operations need modeling.
- Anti-cue: one timing result or a visual count of nested loops is not a derivation.
- Comparison: consecutive phases add their costs; repetition sums the cost of every repetition.
- Common failure: dropping `m` from `n + m` without any relationship between them.

Recall: What grows? Which operation dominates? Which case and bound did I actually establish?

| Field | Value |
|---|---|
| Domain | Problem-solving foundations |
| Curriculum | [CURRICULUM.md](../../../CURRICULUM.md#dsa-fnd-040) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Pattern index | [PATTERN_INDEX.md](../../../PATTERN_INDEX.md) |
| Problem bank | [PROBLEM_BANK.md](../../../PROBLEM_BANK.md) |
| Primary outcome | Derive O, Theta, and Omega bounds using explicit input variables rather than guessing from code shape. |
| Hard prerequisites | DSA-FND-010 |
| Soft prerequisites | None |
| Priority | Core |
| Interview frequency | High |
| Practical relevance | High |
| Python relevance | High |
| Difficulty | 2 |
| Depth | D2 |
| Scope | Foundations, Complexity |
| Size | L |
| First understanding | 4–7 h |
| Hands-on practice | 8–14 h |
| Evidence | E+T+P+D+R+M |
| Artifact state | Draft |
| Canonical Python | 3.14 |
| Interview compatibility | 3.11 |

## 1. Learning outcomes and evidence

After this unit Rahul should be able to:

1. name independent input variables, their relationships, and the representation being analyzed;
2. distinguish exact event counts, elapsed time, asymptotic bounds, and input-case selection;
3. justify an upper, lower, or tight bound with constants or a counting argument;
4. derive costs for separate phases, rectangular and dependent loops, and multiplicative progress;
5. include hidden Python work and separate input, auxiliary, output, and recursion-stack space;
6. repair a complexity claim with a counterexample family rather than one convenient input;
7. explain a bound aloud and revise it when constraints or representation change.

Required evidence is an explanation, a predicted trace, a bound proof, a corrected cost analysis,
an unlabeled transfer attempt, and delayed recall. Use [practice](practice/README.md) and
[REVIEW.md](REVIEW.md). Generated notes, passing teaching tests, and the recorded experiment do
not supply Rahul's learning evidence. `I` and `X` are not required by the canonical evidence
profile; the worked micro-lab and supplementary experiment support the required reasoning.

## 2. Prerequisite bridge

The hard prerequisite is
[DSA-FND-010 — Computational problem solving and constraint translation](../../../CURRICULUM.md#dsa-fnd-010).
At initialization its tracker has no learner evidence. That does not prevent preparing this pack.
Before studying, write a concrete input, required output, smallest valid input, and largest allowed
sizes. Distinguish “there are `n` numbers” from “one number has value `n`.” This is the minimum bridge;
it does not certify completion of the prerequisite.

For Python, know that a list holds references, a half-open range excludes its stop, and `a[:k]`
creates a new list of references. Formal proof vocabulary can be refreshed in
[DSA-FND-030 — Invariants, correctness, and termination](../../../CURRICULUM.md#dsa-fnd-030),
but it is not a new hard prerequisite for this unit.

## 3. Intuition and problem shape

Imagine checking every seat in a hall. Ten rows of four seats require forty seat checks. Adding a
second hall means adding its work. Comparing every attendee from one hall with every attendee from
another means multiplying the group sizes. The question being asked determines which count fits.

Start with a **model sentence**: “The inputs are two unchanged lists of `n` and `m` bounded-size
integers. I count equality comparisons in the worst case, excluding input construction.” A claim
such as `O(nm)` is now interpretable. Without that sentence, `n` might mean one list, both lists,
the number of pairs, or the largest integer value.

Constraints influence the model without changing definitions. If `m` is always at most ten, the
rectangle is linear in the growing variable `n`. If `m` can grow independently, preserve it. If
each comparison examines a large record, give its cost another variable rather than treating the
whole record as a machine integer. No fixed “operations per second” rule follows from big-O.

## 4. Brute force and bottleneck

### Simplest correct baseline

Suppose the teaching question asks how many unordered pairs of distinct positions a list of length
`n` contains. A deliberately literal baseline checks every ordered pair:

```python
def count_position_pairs(n: int) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if j < i:
                count += 1
    return count
```

For `n = 4`, there are sixteen predicate evaluations but six successful increments. Choose which
event you count before making an exact claim. The runtime is `Theta(1 + n*n)` in the unit-cost
model, with constant auxiliary and scalar-output space and no recursion.

### Exact bottleneck

The baseline tests the diagonal and both orientations of every distinct pair. Restricting the
inner range to `range(i)` avoids those rejected candidates. It reduces the body count to
`0 + 1 + ... + (n-1)` without changing the quadratic growth class. A useful constant-factor
improvement is not automatically an asymptotic improvement.

If only the number of position pairs is required, the count can instead be calculated algebraically
as `n*(n-1)//2`. That uses a constant number of arithmetic operations, assuming fixed-cost
arithmetic. If each pair must be inspected for a property of its values, that shortcut no longer
meets the contract. If `n` is an arbitrarily large integer, the arithmetic itself is not constant
in its bit length. Changing either the contract or the cost model changes the conclusion.

## 5. Derivation and invariant

Use the baseline to derive a count, rather than matching its indentation to a memorized label:

1. In the restricted version, row `i` visits exactly `i` earlier positions.
2. After `r` completed rows, the count is `sum(i for i in range(r)) = r(r-1)/2`.
3. The next row adds `r`, producing `r(r+1)/2`, the same formula at `r + 1`.
4. At `r = n`, the exact count is `n(n-1)/2`.
5. For `n >= 2`, this lies between `n*n/4` and `n*n/2`. Both bounds have constants independent
   of `n`, so this count is `Theta(n*n)`.

The invariant accounts for every event once. The inequalities establish the growth class. For a
rectangle, substitute `r*m` for the prefix count; for dependent row widths, retain the sum until
you have justified a simplification. Multiplying the largest observed row width by the number of
rows gives an upper bound, but does not alone establish a matching lower bound.

## 6. Detailed visual trace

### A dependent loop is a sum of different row widths

```text
Teaching specimen: for i in range(4): for j in range(i): count += 1

                    j=0 j=1 j=2 j=3     added     running count
row i=0              .   .   .   .         0            0
row i=1              x   .   .   .         1            1
row i=2              x   x   .   .         2            3
row i=3              x   x   x   .         3            6
exit r=4: every 0 <= j < i < 4 was visited exactly once
```

#### How to read this visual

Each `x` is one execution of the innermost body. Dots are excluded coordinates, not executed
checks. The running count is recorded after a whole row; the first row is deliberately present.

#### Key insight

The inner loop length changes with `i`; add its actual lengths. The triangular region is smaller
than a square but still has a quadratic number of marks as `n` grows.

#### Simplification or limitation

This counts body visits, not bytecode instructions. The real lab also stores summary rows, which
costs memory that the scalar counting algorithm does not need. Four rows illustrate a proof;
four rows alone do not prove an asymptotic statement.

### Multiplicative progress measures levels, not distance

```text
p = 1; limit = 10; repeat while p < limit

step       p before       p after       body visits so far
  0           1              2                  1
  1           2              4                  2
  2           4              8                  3
  3           8             16                  4
exit: 16 < 10 is false

after t steps: p = 2**t; stop at the smallest t with 2**t >= limit
```

#### How to read this visual

Read a row as a body transition. Test the guard again after the last row; there is no body
execution at `p = 16`. Compare a power of two with the next integer above it.

#### Key insight

For integer `limit >= 1`, the body count is `ceil(log2(limit))`. Doubling the limit adds roughly
one iteration; it does not double the iteration count.

#### Simplification or limitation

For `limit` zero or one, there are zero body visits and still constant setup/guard work. A zero
starting value would never grow under multiplication by two. Large Python integers also make the
cost of an individual multiplication depend on representation size.

Run the teaching traces from this unit directory:

```bash
uv run --group dev python practice/micro_lab.py --n 4 --m 3 --limit 10
uv run --group dev python practice/micro_lab.py --n 3 --m 0 --limit 1
```

Predict before running. The CLI limits table sizes so it remains a trace tool, not a benchmark.

## 7. Mechanics and state variables

These are alternative models, not state that every algorithm must store.

| Variable | Meaning | Update or relationship | Why it matters |
|---|---|---|---|
| `n`, `m` | Independent dimensions | Fixed during a run | A bound must remain valid as either grows |
| `i`, `j` | Current coordinates | Follow the actual loop ranges | Determine the number of visits in each row |
| `r` | Completed outer rows | Increases by one | Precise boundary for the counting invariant |
| `visits` | Chosen event count | Increases only at that event | Must not be confused with all runtime work |
| `p`, `t` | Growing cursor and steps | `p *= 2`, `t += 1` | Invariant `p = 2**t` yields the stopping count |
| `b` | Bits in a numeric input | For `N > 0`, `b = floor(log2(N)) + 1` | Separates magnitude from encoded input size |
| `c` | Cost of a primitive comparison | Stated by the representation/model | Prevents hidden work inside a “single” operation |

## 8. Correctness reasoning

For the restricted pair-counting example:

- **Initialization:** before row zero, no allowed coordinate has been visited and the count is zero.
- **Preservation:** row `r` visits each `j` from zero through `r-1` once. These coordinates are new;
  adding `r` preserves the prefix-count invariant.
- **Progress and termination:** both ranges are finite. The outer row count increases to `n`.
- **Completeness:** every allowed coordinate satisfies `j < i` and appears in exactly row `i`.
- **Safe exclusion:** diagonal and reversed pairs are excluded by this position-pair contract.
  Such exclusion would need a new proof for a different contract.
- **Final-state argument:** at exit `r = n`; substituting into the invariant yields the result.

For complexity, also prove that the chosen event covers the dominant work: each visited coordinate
costs a bounded amount, row overhead totals `O(n)`, and no hidden work is omitted. Correct output
does not by itself prove the advertised runtime. An upper bound alone does not prove tightness.

A lower bound on **this implementation's** count is not a lower bound on **every algorithm for the
problem**. The algebraic pair counter is a counterexample to claiming that obtaining only the count
inherently requires enumerating the pairs.

## 9. Complexity derivation

### Bounds on a function

Let `f(n)` be a non-negative resource function and `g(n)` an eventually positive comparison
function. For fixed positive constants and a fixed threshold `n0`:

| Claim | What must hold for every `n >= n0` | What it establishes |
|---|---|---|
| `f in O(g)` | `f(n) <= c*g(n)` | Eventual upper bound |
| `f in Omega(g)` | `c*g(n) <= f(n)` | Eventual lower bound |
| `f in Theta(g)` | `c1*g(n) <= f(n) <= c2*g(n)` | Both bounds for the same function |

The constants cannot depend on the growing input. These are the algorithm-analysis definitions of
[big-O](https://xlinux.nist.gov/dads/HTML/bigOnotation.html),
[Omega](https://xlinux.nist.gov/dads/HTML/omegaCapital.html), and
[Theta](https://xlinux.nist.gov/dads/HTML/theta.html). The common notation `f(n) = O(g(n))` denotes
membership in a class of functions, not ordinary equality of two numeric expressions.

Original witness example: `f(n) = 3n + 2`. For `n >= 1`, `3n <= f(n) <= 5n`, so `f in Theta(n)`.
It is also in `O(n*n)`, since `n <= n*n` there. That looser upper bound is true but hides information.
It is not in `Omega(n*n)`: any proposed positive `c` eventually loses to `f(n)/n**2`, which tends
to zero. “Drop constants” is shorthand after a bound is justified, not the definition.

### Case selection is a separate axis

First define the work on one input, `C(x)`. Among allowed inputs of size `n`, define the smallest
cost, largest cost, or an expectation under a stated distribution. Then bound that function.

A scan for the first matching bounded integer can use one comparison when the first element
matches and `n` when none does. Its best-case runtime is `Theta(1)` and worst-case runtime is
`Theta(n)` for `n >= 1`. Each function has both upper and lower bounds. `Omega` does not select the
best case. If exactly one match has a uniformly distributed position, the expected comparison
count is `(1 + ... + n)/n`; a different distribution requires a different expectation. Without a
distribution or randomized-algorithm model, “average case” has not been defined.

### Add phases; sum repeated work; preserve independent dimensions

| Work shape | Counted body events | Total time under unit-cost assumptions |
|---|---|---|
| Separate scans of lengths `n`, `m` | `n + m` | `Theta(1 + n + m)` |
| `n` rows, each with `m` iterations | `nm` | `Theta(1 + n + nm)` |
| Inner length `i` in row `i`, `0 <= i < n` | `n(n-1)/2` | `Theta(1 + n*n)` |
| `p = 1`, multiply by two while `p < N` | Zero for `N <= 1`; otherwise `ceil(log2(N))` | `Theta(1 + log(max(1, N)))` |

The outer overhead explains the asymmetric `n` term in the rectangle row. With `n = 0`, no
`m`-iteration loop runs. With `m = 0`, every outer iteration still runs. For positive growing
dimensions, the customary abbreviated bounds are sufficient; state that domain.

For multiple variables, one set of constants must work uniformly over the allowed size pairs,
not merely on samples where `m = n`. `n + m` is `Theta(max(n, m))` when the maximum is positive,
but need not be `Theta(n)`. You may replace `m` by a bound only if the constraints justify it.
Likewise, do not erase `m` from `n*n + m` just because the first term has a square.

### Representation chooses useful variables

| Input representation | Useful size variables | Work to account for |
|---|---|---|
| Rectangular grid | Rows `r`, columns `c` | `rc` cells, plus setup where dimensions can be empty |
| Ragged list of lists | Outer rows `r`, total entries `s` | Visiting every row and entry costs `Theta(1 + r + s)` |
| List of words | Word count `w`, total inspected characters `L` | Character processing need not be constant per word |
| Graph adjacency lists | Vertices `V`, stored adjacency entries `A` | Scanning all lists costs `Theta(1 + V + A)`; undirected edges usually occupy two entries |
| Graph adjacency matrix | Vertices `V` | Scanning every slot costs `Theta(1 + V*V)`, even for few actual edges |
| One non-negative integer `N` | Value `N`, encoded bit length `b` | Iterating `N` times is not linear in `b` |

These are traversal models, not claims that every problem on that representation needs a complete
traversal. Define `E` as logical edges if using the conventional `V + E` graph notation; explain
how it relates to stored entries. Later graph units own graph algorithms.

### Logarithms and growth

For multiplication by a fixed factor `a > 1`, after `t` steps the cursor is `a**t`. Solve the exit
inequality for `t`. A fixed change of logarithm base contributes only a constant factor. An input
dependent multiplier, a reset inside another loop, or a linear scan inside each step needs a new
count. Do not infer logarithmic work just because the code contains division.

For orientation as `n` grows, the usual fixed-base classes progress from constant to logarithmic,
linear, `n log n`, quadratic, cubic, exponential, and factorial. This is an eventual growth
comparison, not a universal speed ranking at small inputs. Constants, interpreter overhead,
representation, and the chosen workload can determine the actual crossover.

For a positive integer `N`, `2**(b-1) <= N < 2**b`, where `b` is its bit length. A loop with `N`
body visits therefore has exponential event count in `b`. Arithmetic on growing Python integers
also needs bit-cost analysis; that can change time beyond the event count. This unit introduces
the modeling issue; detailed arithmetic/runtime analysis belongs to
[DSA-PY-060](../../../CURRICULUM.md#dsa-py-060).

### Separate space categories and measure peak live storage

State input storage, auxiliary working space excluding output, output storage, and recursion stack
separately. Say whether a reported auxiliary total includes stack space. None of the teaching
loops recurses: additional recursion stack is zero, and ordinary call depth is constant.

The scalar pair/rectangle counters use constant working words and return one word under the
unit-cost model. The lab intentionally retains a summary row per outer iteration: its rectangle
and triangle reports occupy `Theta(1 + n)` output words, despite constant scalar algorithm state.
The doubling report stores `Theta(1 + log(max(1, N)))` rows. Formatting a report allocates strings
too; it is instrumentation, not part of the scalar algorithm.

Repeatedly allocating and discarding slices may perform quadratic total copying while using only
linear peak temporary storage. A list of all those slices can keep the quadratic storage alive.
Count lifetimes, not just allocations. In a bit model, a counter up to `nm` requires
`O(1 + log(n+1) + log(m+1))` bits, even though it is a constant number of integer variables.

### Python costs belong inside the count

| Operation and assumptions | Cost to include |
|---|---|
| Built-in list `len(a)` or valid indexing | Constant-time CPython access; arbitrary custom containers may differ |
| List membership | Up to `n` equality checks; charge the cost `c` of each check |
| Built-in list slice of length `k` | `Theta(1 + k)` time and new reference storage; no deep copy of the elements |
| Summing `k` bounded integers | `k` additions plus iteration; unbounded intermediate values require another model |
| `range(N)` versus `list(range(N))` | A few endpoints versus storage for every generated value |
| User-defined equality or other protocol calls | No automatic constant-time guarantee; inspect the contract |

The list access, membership, and slicing statements are CPython details inferred from
[`list_length`, `list_item`, `list_contains`, and `list_slice_lock_held` in v3.14.7](https://github.com/python/cpython/blob/v3.14.7/Objects/listobject.c).
The standard type contracts document [range storage](https://docs.python.org/3.14/library/stdtypes.html#ranges)
and [unlimited integer precision](https://docs.python.org/3.14/library/stdtypes.html#numeric-types-int-float-complex).
A fixed number of endpoints is not fixed bit storage when their magnitudes grow. Keep language
semantics, CPython implementation costs, and the simplifying word-cost model distinct.

### A clock is an observation tool

Exact counters can falsify a proposed count on a test input. A finite sequence of counts still
needs a proof to establish asymptotic behavior. Timings add scheduler, allocation, caching, and
interpreter effects. In particular, the minimum measured time in `timeit` is not the mathematical
`Omega` bound. The [experiment](experiments/DSA-FND-040-X01-counts-and-clock-time/README.md)
keeps predicted counts and observed clock measurements separate.

## 10. Implementations

### Generic analysis procedure

```text
write the input contract and representation
name independent size variables and their allowed relationships
choose the resource and case: exact input, best, worst, or a stated expectation
name a primitive operation and its cost
derive visits per phase or outer state; add them
include setup, empty-case overhead, and hidden operations
justify upper and lower bounds separately
account for peak auxiliary, output, and stack space
check boundary inputs; revise when the contract changes
```

### Idiomatic Python teaching specimen

```python
def rectangular_visits(n: int, m: int) -> int:
    """Count body visits for non-negative dimensions, without storing a trace."""
    visits = 0
    for _ in range(n):
        for _ in range(m):
            visits += 1
    return visits
```

This intentionally executes the visits. Replacing its body with multiplication would calculate
the same numeric count but would no longer demonstrate the work being counted. The
[micro-lab](practice/micro_lab.py) also records row summaries and doubling transitions. Its
[passing tests](practice/test_work_counts.py) check those worked specimens, not Rahul's answers.

### Python 3.11 compatibility

The code uses ordinary loops, dataclasses, standard-library timing, and annotations supported in
Python 3.11. No 3.14-only syntax or API is needed. A compatibility syntax check does not replace
execution under that interpreter; record the interpreter actually used in any run.

### First-principles versus standard-library choice

Use visible loops to learn how many events occur. In ordinary code, built-ins may express the
operation more clearly and run with different constants. They do not remove the need to analyze
their contracts. The lab's stored rows and growing lists add instrumentation costs; the usual
amortized list-append accounting is explained in
[DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](../../../CURRICULUM.md#dsa-fnd-050).
Do not claim that this unit has already established those separate results.

## 11. Edge-case matrix

Derive cases from dimensions, representation, boundaries, and transitions rather than guessing
unrelated examples.

| Dimension | Minimal adversarial case | Expected behavior | Reasoning risk |
|---|---|---|---|
| Empty outer dimension | `n=0, m=5` | No row or body visits; constant scalar setup | Charging inner work that never runs |
| Empty inner dimension | `n=3, m=0` | Three outer iterations, zero body visits | Equating zero counted events with zero runtime |
| Strict pair boundary | `n=1` | Zero pairs; one outer row | Including the diagonal |
| Independent dimensions | `n=2, m=1000` and the reverse | Equal pair count but different row overhead | Treating both axes as `n` |
| Logarithmic threshold | `N=8` versus `N=9` | Three versus four doubling transitions | Losing ceiling or using a floating-point guess |
| Starting/exit state | `N=0` or `N=1` with initial `p=1` | No doubling body visits | Evaluating `log(0)` or expecting one visit |
| Early exit | First item matches versus no item matches | One comparison versus a full scan | Calling a best-case example the worst case |
| Record size | Few very long values | Equality may dominate loop control | Omitting the comparison-cost variable |
| Temporary allocation | Repeatedly copy a growing prefix | Peak space differs from total copied volume | Counting cumulative allocation as peak storage |
| Encoding | One large integer instead of a large list | Bit length differs from numeric value | Calling value-linear work input-linear |

## 12. Comparisons and anti-signals

| Candidate claim/model | Use when | Reject or qualify when |
|---|---|---|
| `O(g)` | Only an upper bound has been established | You are trying to claim a tight rate without a lower bound |
| `Theta(g)` | Both bounds hold for the same function and input domain | The evidence is just a maximum row width or a few timings |
| `Omega(g)` | Establishing a lower bound on a named cost function | You mean “best case” or a universal problem lower bound without proof |
| Add phase costs | Phases execute one after another | One phase is actually repeated inside another |
| Multiply sizes | Every outer iteration performs the same amount of inner work | The inner limit varies or shared state changes its total visits |
| Constant primitive cost | Bounded machine-size values and suitable operations | A primitive copies a slice, scans a record, or performs big-integer arithmetic |
| Elapsed-time comparison | Comparing concrete implementations on a controlled workload | Trying to prove an asymptotic class or a platform-independent limit |

Shared monotone state inside nested loops can limit total work across the whole run. Trace state
resets before counting; deeper aggregate and amortized arguments belong to
[DSA-FND-050](../../../CURRICULUM.md#dsa-fnd-050). Recursive calls and stack costs belong to
[DSA-FND-060](../../../CURRICULUM.md#dsa-fnd-060). These are continuation boundaries, not extra
units silently folded into this one.

## 13. Common bugs and debugging

| Failure | Symptom | Counterexample or family | Repair |
|---|---|---|---|
| Count indentation | Every nested loop is called quadratic | Fixed ten inner visits for each growing outer row | Count actual visits and define the growing variables |
| Count only successful branches | Work looks tiny when few matches occur | A full no-match scan still evaluates every predicate | Count failed checks too |
| Lose a variable | `n+m` becomes `n` | Keep `n` fixed while `m` grows | Preserve independent sizes or prove a relationship |
| Upper bound becomes equality | A triangle's largest row is treated as its exact width everywhere | Row zero has no body visits | Write the sum; prove a matching lower bound |
| Ignore stopping values | `log2(10)` is described as an integer number of transitions | The trace reaches 16 on its fourth step | Solve the discrete stopping inequality |
| Use finite samples as proof | A timing ratio becomes a claimed theorem | Constant overhead can dominate small inputs | Separate mathematical derivation from measurements |
| Hide allocation | A one-line slice is called constant-time | Copy a prefix whose length grows with `n` | Charge copied references and peak lifetime |
| Misuse “in place” | No explicitly named buffer is taken to mean no extra space | A slice inside an expression allocates | Inspect operations as well as variable declarations |
| Multiply worst cases blindly | Every comparison is assumed maximally expensive at once | Input constraints may prevent the proposed combination | Give a feasible family attaining the lower bound |

For a false asymptotic claim, one tiny input reveals a likely mistake but may lie below its claimed
threshold. Finish with an unbounded family or a ratio argument showing that no fixed constants
can repair the claim.

## 14. Practice ladder

All tasks are original local exercises. Inspection of `data/problems.json` found no owner,
secondary-unit, or prerequisite mapping to `DSA-FND-040`; no LeetCode metadata or ownership is
invented. The canonical problem bank remains unchanged.

| Stage | Work | Evidence artifact |
|---|---|---|
| Concept micro-drill | [P03: qualify bound claims](practice/README.md#dsa-fnd-040-p03) | Constants, thresholds, or counterexample families |
| Hand trace | [P01: account for skipped coordinates](practice/README.md#dsa-fnd-040-p01) | Predicted rows before execution |
| Guided derivation | [P02: capped dependent work](practice/README.md#dsa-fnd-040-p02) | First derivation; one requested hint at a time |
| Independent analysis | Revisit P02 with two new size relationships | Bound valid beyond square inputs |
| Changed constraints | [P04: audit a report builder](practice/README.md#dsa-fnd-040-p04) | Time and storage lifetimes under both contracts |
| Confused-model comparison | [P05: select the input case](practice/README.md#dsa-fnd-040-p05) | Best, worst, and distribution-specific claims |
| Mixed unlabeled task | [P07: batch acceptance](practice/README.md#dsa-fnd-040-p07) | Independent proposal with labels withheld |
| Timed interview | Attempt P07 unseen in 20 minutes; if already seen, request a fresh contract | Spoken approach, trace, and defended costs |
| Delayed re-solve | [REVIEW.md](REVIEW.md) at 1, 3, 7, 14, and 30 days after study | Dated retrieval, hint history, exact weakness |
| Unseen transfer | [P06: representation change](practice/README.md#dsa-fnd-040-p06), then a fresh coach-supplied variation | New variables and a revised argument |

Keep any later learner files inside this unit's practice directory and link them from the review.
Do not overwrite a prediction after seeing output. Estimates are learning budgets, not deadlines.

## 15. Interview questions, traps, and follow-ups

### Recognition and approach questions

1. A request contains two independently sized lists. What must you define before saying `O(n)`?
2. When do two phases add their work, and when do they multiply it?
3. How would you explain the bottleneck in checking every ordered pair but accepting only `j < i`?

### Invariant and correctness questions

1. What invariant relates completed rows to the count in a rectangular traversal?
2. How does an event-count proof differ from a proof that the returned answer is correct?
3. Why does an upper bound obtained from the longest row not always establish tightness?

### Complexity questions

1. Can a linear function be in `O(n*n)` without being in `Theta(n*n)`?
2. Does a worst-case `Omega(n)` statement imply that every input takes linear time?
3. What distribution would you need before claiming an average-case cost for a search?
4. How do you account for output space, temporary slices, and recursion stack separately?
5. What changes if each equality comparison processes a record rather than one bounded integer?

### Changed-constraint follow-ups

1. If the second list has at most five items, how does your two-variable bound simplify?
2. If the input is a single integer written in binary, is a loop up to that integer linear in input size?
3. If an algorithm must retain every trace row, which space claim changes?
4. If a rectangular grid becomes ragged and may contain empty rows, which variables remain useful?

### Common traps and weak-answer repairs

- Trap: “Big-O is worst case; Omega is best case.” First name the case function, then bound it.
- Trap: “I halved the number of pairs, so the algorithm is linear.” Explain the count as `n` grows.
- Weak answer: “Two loops, so quadratic.” Repair it by stating their limits, reset behavior, and
  body costs. What family would disprove the quadratic claim?
- Weak answer: “It ran twice as fast.” Which input sizes, workload, interpreter, and repeated
  measurements support that observation, and what theorem does it still fail to prove?

## 16. Explanation exercises

1. In ninety seconds, move from the seat-grid visual to a two-variable bound and explain an empty
   inner loop without claiming zero runtime.
2. Explain `O`, `Omega`, and `Theta` using one cost function, actual constants, and one valid but
   loose bound. Keep case selection separate.
3. Reconstruct the triangle invariant on paper, then justify both inequalities needed for a tight
   bound. Do not use “obviously quadratic” as a proof step.
4. Defend a Python cost claim after an interviewer replaces a bounded integer with a long record.
5. Explain why a count prediction can be exact while a corresponding timing prediction is only a
   workload-specific expectation. Say what remains unproved.

## 17. Experiment decision

Decision: Created the supplementary
[DSA-FND-040-X01 — Counts and clock time](experiments/DSA-FND-040-X01-counts-and-clock-time/README.md).
Independent input dimensions are easy to hide by testing only square sizes. The experiment varies
one axis and then both, keeps exact body counts, and optionally measures the same specimens with
`timeit`. The timing run makes noise and instrumentation limits visible. It is not required `X`
evidence, does not change the curriculum classification, and does not advance learning state.

## 18. Vocabulary and professional English

| Term | Pronunciation | Meaning here | Useful sentence |
|---|---|---|---|
| Asymptotic | as-im-TOT-ik | Describes eventual growth as input size increases | “This is an asymptotic bound, not a deadline prediction.” |
| Tight | tyte | A matching upper and lower growth bound | “The count has a tight quadratic bound.” |
| Dominant | DOM-ih-nunt | Controls growth under the stated variable relationships | “Neither independent input size can be dropped without a constraint.” |
| Representation | rep-ri-zen-TAY-shun | How the input is encoded or stored | “The representation determines whether size means elements or bits.” |

Use “under this cost model” and “for all sufficiently large inputs” when those qualifications do
real work. Prefer a precise short sentence over reciting a growth-class name alone.

## 19. Python Mastery references

These are the exact reference links from [PYTHON_REFERENCES.md](../../../PYTHON_REFERENCES.md),
not claims that another repository or its learner evidence was inspected.

- [PY-MPR-070 — Algorithmic and memory complexity](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mpr-070): reinforce resource models and space accounting.
- [PY-BLT-040 — Lists, tuples, ranges, and sequence behaviour](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-blt-040): inspect indexing, ranges, and slices.
- [PY-BLT-090 — Protocol-facing built-in functions and container complexity](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-blt-090): examine work hidden behind a built-in.
- [PY-FND-020 — Objects, names, references, and mutability](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-fnd-020): distinguish a copied container from copied elements.
- [PY-MPR-080 — Responsible benchmarking](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mpr-080): qualify machine observations and avoid timing-as-proof claims.

## 20. Authoritative sources

Read on 2026-08-30. Explanations, examples, exercises, traces, and derivations in this pack are
original; no problem statement, editorial, or external exercise set is reproduced.

| Source | Classification | Used for |
|---|---|---|
| [NIST DADS: big-O](https://xlinux.nist.gov/dads/HTML/bigOnotation.html) | Algorithm terminology | Eventual upper-bound definition and the role of a cost model |
| [NIST DADS: Theta](https://xlinux.nist.gov/dads/HTML/theta.html) | Algorithm terminology | Matching eventual bounds |
| [NIST DADS: capital Omega](https://xlinux.nist.gov/dads/HTML/omegaCapital.html) | Algorithm terminology | Algorithmic lower-bound definition, distinct from lowercase omega |
| [Python 3.14 standard types](https://docs.python.org/3.14/library/stdtypes.html) | Language/standard-type contracts | Integer precision, sequence behavior, and ranges |
| [CPython v3.14.7 list implementation](https://github.com/python/cpython/blob/v3.14.7/Objects/listobject.c) | CPython implementation detail | Access, membership traversal, and shallow slice copying |
| [Python 3.14 timeit](https://docs.python.org/3.14/library/timeit.html) | Standard-library measurement contract | Repetition, clock choice, garbage collection, and timing limitations |
