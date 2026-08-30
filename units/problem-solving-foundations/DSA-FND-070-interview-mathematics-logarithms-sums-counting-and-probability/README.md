# DSA-FND-070 — Interview mathematics: logarithms, sums, counting, and probability

## Physical Notebook Core

**Pressure:** a loop shrinks, a level expands, choices combine, or a random event changes the
work. Before choosing a formula, name exactly what one step, choice, or outcome means.

> Count the right objects, keep the endpoints, and state the assumptions beside the formula.

```text
Integer halving:       13 -> 6 -> 3 -> 1          3 divisions
Capacity doubling:     1 -> 2 -> 4 -> 8 -> 16     4 doublings to cover 13
Work at four levels:   1 +  2 +  4 +  8 = 15     4 levels, 15 work units
Two fair coins:       HH  HT  TH  TT              each outcome has mass 1/4
Number of heads:       2   1   1   0              expected count = 1
At least one head:     1   1   1   0              probability = 3/4
```

#### How to read this visual

Read each line separately. Arrows count transitions; the addition line counts work within
levels. The last two rows use the same four equally likely outcomes but measure different things.

#### Key insight

A logarithm can count levels without counting all work. An expected count can differ from the
probability that the count is positive. The contract determines both quantities.

#### Simplification or limitation

The arrows use positive integers and base two. Coin outcomes are fair and mutually independent.
Work units ignore the growing bit cost of Python integers; this is not a timing measurement.

**Rules to reconstruct:** `log_b(n)` solves `b^x = n`; `sum(1..n) = n(n+1)/2`;
`1+2+...+2^h = 2^(h+1)-1`; `H_n = sum(1/i)` grows as `Theta(log n)` for `n >= 2`;
an unordered pair of distinct positions has two ordered representations;
`E[sum(X_i)] = sum(E[X_i])` without requiring independence.

```text
describe one counted object and its legal range
write the first few states or list a tiny outcome space
partition without overlap, or account for a fixed duplication factor
derive an exact expression or a justified bound
check the empty case, boundaries, output size, and arithmetic model
```

- Inputs: name `n` as a size or numeric magnitude, `h` levels, `k` choices, and `B` integer bits.
- Time: halving has `Theta(log n)` steps; inspecting every distinct pair has `Theta(n^2)` visits.
- Auxiliary space: a scalar counting loop uses a constant number of integers, not constant bits.
- Output space: count-only and an explicit list of all choices have different costs.
- Recursion stack: these examples are iterative; stack depth is constant.
- Python cost: use integer boundaries for exact answers; integer multiplication and `comb` are
  not constant-time operations on unbounded inputs.
- Cue: repeated multiplication/division, regular work schedules, choice counts, declared randomness.
- Anti-cue: a formula cannot replace inspecting arbitrary pair values when the answer depends on them.
- Comparison: multiply choices along a construction; add counts of disjoint alternatives.
- Failure: “there are two loops, so quadratic” without counting each inner range.

Recall: What is being counted? Why is nothing missed or counted twice? Is this an exact count,
a growth bound, an expectation, or an observed frequency?

| Field | Value |
|---|---|
| Domain | Problem-solving foundations |
| Curriculum | [CURRICULUM.md](../../../CURRICULUM.md#dsa-fnd-070) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Pattern index | [PATTERN_INDEX.md](../../../PATTERN_INDEX.md) |
| Problem bank | [PROBLEM_BANK.md](../../../PROBLEM_BANK.md) |
| Primary outcome | Use the small set of logarithmic, summation, counting, combinatorial, and probability tools that recur in interview algorithms. |
| Hard prerequisites | DSA-FND-040 |
| Soft prerequisites | None |
| Priority | Professional |
| Interview frequency | Medium |
| Practical relevance | Medium |
| Python relevance | Low |
| Difficulty | 3 |
| Depth | D2 |
| Scope | Foundations, Mathematics |
| Size | L |
| First understanding | 4–7 h |
| Hands-on practice | 8–14 h |
| Evidence | E+T+P+R+M |
| Artifact state | Draft |
| Canonical Python | 3.14 |
| Interview compatibility | 3.11 |

## 1. Learning outcomes and evidence

After study, Rahul should be able to:

1. derive logarithmic step counts from inequalities, including floor and ceiling boundaries;
2. derive arithmetic and geometric sums and bound a harmonic sum without memorizing a table;
3. distinguish counting a state space from enumerating and materializing its members;
4. decide whether order, replacement, and duplicate values change a count;
5. define a sample space, conditional probability, and the independence assumptions actually used;
6. use indicator variables for an expected count and separate expectation from worst-case cost;
7. defend an answer, reject a tempting formula, and adapt to a changed constraint.

Required evidence is **E** explanation, **T** trace, **P** proof, **R** delayed recall, and **M**
mixed transfer. Use [practice](practice/README.md) and [REVIEW.md](REVIEW.md). This curriculum
row has no `I` or `X`: the micro-lab and two supplementary experiments support those evidence
goals, without adding mandatory implementation challenges or extra learning states.

No problem-bank entry is owned by this unit. The registered LC 1071 reference lists this unit
as a prerequisite but belongs to [DSA-BMS-040](../../../CURRICULUM.md#dsa-bms-040); it is not
silently reassigned here. All local exercises are original, with mixed/mock reserve pools untouched.

## 2. Prerequisite bridge

The tracker records [DSA-FND-040 — Asymptotic notation and input-variable modeling](../../../CURRICULUM.md#dsa-fnd-040)
as `Not started`. Preparation can proceed, but prerequisite mastery is not assumed. Recover
four facts before studying: define independent input sizes; name the dominant operation; add
successive phases and sum repeated costs; distinguish an upper bound from a tight bound.

For example, `n` stored records and an integer whose value is `n` are different input models.
The latter needs about `log2(n)` bits. Python bridge: `//` floors a quotient, `range` excludes its
stop, `**` computes powers, and Python `int` retains exact integer values as their size grows.
A bridge does not advance this unit or its prerequisite in [PROGRESS.md](../../../PROGRESS.md).

## 3. Intuition and problem shape

Imagine arranging chairs in rows. “How many rows?” and “How many chairs?” are different
questions. Doubling a row's length gives few rows but many chairs. Now imagine choosing two
chairs: selecting left then right counts the same unordered pair twice. Finally, imagine choosing
chairs randomly: not every description of an outcome necessarily has the same probability.

Translate constraints before calculating:

| Question | Contract to establish first |
|---|---|
| How many reductions? | Initial value, update rule, rounding, and exact stopping test |
| How much total work? | Per-stage cost and both summation endpoints |
| How many legal objects? | Distinguishable positions, order, replacement, and restrictions |
| How likely, or how much on average? | Sample space, event/count, and probability distribution |

Use tiny examples to discover the structure, then prove it for the stated domain. These tools
support later algorithms; advanced counting, randomized selection, and number theory retain
their separate curriculum owners.

## 4. Brute force and bottleneck

To count distinct unordered pairs of `n` positions, a transparent baseline is:

```text
count = 0
for i from 0 through n-1:
    for j from i+1 through n-1:
        count += 1
```

For four positions the candidates are `(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)`.
Row lengths are `3, 2, 1, 0`. The baseline spends one increment per pair even when only the
count is requested. The bottleneck is visiting a predictable set of candidates individually.
Summing row sizes, then deriving a formula, removes that enumeration from the count-only task.
If instead every pair's values must be checked, its count alone cannot decide the result.

A probability baseline similarly enumerates a tiny sample space and adds the weights of matching
outcomes. For `m` binary choices there are `2^m` sequences. This is useful for checking a small
derivation, but a full enumeration becomes expensive quickly. Symmetry, complements, or an
expected-count decomposition can sometimes avoid visiting every sequence; their assumptions
must be established first.

## 5. Derivation and invariant

### Logarithms are inverse questions

`log_b(n) = x` means `b^x = n`, with `n > 0` and fixed `b > 1`. For positive integer `n`,
the loop `x = n; while x > 1: x //= 2` preserves `x = floor(n / 2^t)` after `t` divisions.
It stops at `x = 1`, so `2^t <= n < 2^(t+1)`: `t = floor(log2(n))`.

For capacity starting at one and doubled while below `n`, the final exponent is the least
integer `t` with `2^t >= n`: `ceil(log2(n))`. At `n = 1`, both counts are zero. For integer
base `b > 2`, repeated floor division with guard `x >= b` stops in `1..b-1` and gives
`floor(log_b(n))`; changing that guard to `x > 1` changes the problem.

For positive `x,y`, `log_b(xy) = log_b(x) + log_b(y)` and `log_b(x^c) = c log_b(x)`.
Changing a fixed logarithm base changes a constant factor. If the base varies with the input,
that factor cannot automatically be discarded. There is no corresponding rule that splits
`log_b(x+y)` into the sum of two logarithms.

### Add the actual work

For `S = 1+2+...+n`, pair the forward list with its reversal. Each of the `n` columns adds
to `n+1`, so `2S = n(n+1)`. Pair enumeration instead uses `0+1+...+(n-1) = n(n-1)/2`.

For `G = 1+r+...+r^h`, multiply by `r` and subtract: `(r-1)G = r^(h+1)-1` for `r != 1`.
When `r = 1`, there are `h+1` ones. A growing geometric sum with fixed `r > 1` has the order
of its largest term. A constant amount of work per level has the order of the number of levels.

For `H_n = 1+1/2+...+1/n`, group denominators as `1`, `2..3`, `4..7`, `8..15`, and so on.
Every complete block contributes more than `1/2` and at most `1`. There are logarithmically
many blocks; the partial last block cannot add more than one. Thus `H_n = Theta(log n)` for
`n >= 2`. Smaller terms alone do not imply a bounded sum. These identities and harmonic
bounds are standard; see [MIT's sums notes](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/0287cc25b80969d0e83c5ea3e854c227_ln8.pdf).

### Count constructions without changing the objects

Multiply the number of legal choices at each stage when that stage has the same branching
count for every legal preceding choice. This does not require probabilistic independence.
If different prefixes have different counts, separate them into cases or sum over prefixes.
Add case counts only when the cases are disjoint, or explicitly correct their overlap.

| Objects from `n` distinguishable items | Count | Reason |
|---|---|---|
| Length-`k` sequences, repetition allowed | `n^k` | `n` choices at each position |
| Ordered selections, no replacement | `n!/(n-k)!` for `0 <= k <= n` | Available choices decrease |
| Unordered selections, no replacement | `C(n,k)` | Each chosen set has `k!` orderings |
| All subsets | `2^n` | Include/exclude for each position |
| All arrangements using every item | `n!` | Ordered selection of length `n` |

The division by `k!` needs a uniform duplication factor. Equal displayed values can hide
distinct positions, so first define equality of outputs. The empty selection has one construction;
`0! = 1`, and `C(n,k) = 0` for `k > n`. The counting and division rules are supported by
[MIT's counting notes](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/5f8110ee5b0df0da6173de66ff35c7b0_ln9.pdf).

### Probability needs a model

A sample space contains complete outcomes. An event is a subset of those outcomes. Compute
its probability by adding their weights. “Favorable divided by total” is valid only when those
elementary outcomes are equally likely. The complement rule is `P(not A) = 1-P(A)`.

When `P(A) > 0`, `P(A and B) = P(A) P(B given A)`. Replace the conditional term by `P(B)`
only when independence is justified. Sampling distinct items without replacement generally
changes later conditional probabilities. Disjoint events cannot occur together; two disjoint
events of positive probability are not independent. See [MIT's probability notes](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/56a41986aa7ab49261e3ff80017e8cf4_ln12.pdf).

For a count `X`, its expectation is the probability-weighted sum of its values. Write
`X = I_1 + ... + I_m`, where each indicator is one exactly when its event occurs. Then
`E[X] = P(event_1) + ... + P(event_m)`. For a finite sample space, distribute the sum inside
`sum_outcome P(outcome) X(outcome)`; independence is not needed. This is the linearity rule
in [MIT's expectation treatment, section 18.3](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/93cad640cf3ed0b23ef70688f452d4d5_MIT6_042JF10_notes.pdf).

For mutually independent trials with the same success probability `p`, the chance of at least
one success in `m` trials is `1-(1-p)^m`. With dependent events, multiplying failure
probabilities is unjustified. The bound `P(any event) <= min(1, sum P(event_i))` still holds:
the indicator of any event never exceeds the sum of their indicators.

An expected runtime averages over a declared input distribution or random algorithm choices.
It does not promise the same runtime for every execution. Amortized analysis instead bounds a
whole operation sequence, without requiring randomness; revisit [DSA-FND-050](../../../CURRICULUM.md#dsa-fnd-050)
if those claims feel interchangeable.

## 6. Detailed visual trace

### A. An exact stopping boundary

```text
t    remaining=floor(13/2^t)    guard remaining>1    action
0              13                    true           divide
1               6                    true           divide
2               3                    true           divide
3               1                    false          stop
Final boundary: 2^3 <= 13 < 2^4.
```

#### How to read this visual

Each row is the state before the next guard check. The initial row is not a division.

#### Key insight

There are four recorded states but three transitions. The stopping inequality fixes the rounding.

#### Simplification or limitation

This exact floor-division loop is not a complete binary-search algorithm; inclusive/exclusive
search intervals require their own invariant.

### B. The upper triangle counts each pair once

```text
           j=0  1  2  3       row size     cumulative
i=0         .  x  x  x            3             3
i=1         .  .  x  x            2             5
i=2         .  .  .  x            1             6
i=3         .  .  .  .            0             6
```

#### How to read this visual

An `x` is a legal pair `i < j`. Dots are excluded coordinates, not candidate comparisons.

#### Key insight

Every unordered pair has one smaller index and appears in exactly one row.

#### Simplification or limitation

Positions are distinct even if their stored values are equal. The micro-lab computes each row's
size directly; it does not actually perform the six candidate visits drawn here.

### C. Geometric and harmonic prefixes

```text
term k       1       2        3        4
2^(k-1)      1       2        4        8
prefix G     1       3        7       15
added to H   1      1/2      1/3      1/4
prefix H     1      3/2     11/6     25/12
```

#### How to read this visual

Move left to right; add the current term to the previous prefix. Each column represents one update.

#### Key insight

`G` grows with the last power; `H` grows slowly without a fixed upper bound as more terms arrive.

#### Simplification or limitation

Four columns illustrate the rules, not an asymptotic proof. Exact fractions are teaching aids,
and their numerator/denominator arithmetic is not free.

### D. One sample space, two different measurements

```text
outcome       probability     heads X     indicator I(X>0)
HH                1/4           2               1
HT                1/4           1               1
TH                1/4           1               1
TT                1/4           0               0
weighted sum       1            1              3/4
```

#### How to read this visual

Multiply each measurement by the probability in its row, then add down its column.

#### Key insight

The row `HH` contributes two heads but only one occurrence of “any heads.”

#### Simplification or limitation

Equal row weights depend on fair independent coins. Collapsing `HT` and `TH` into one description
would give unequal weights to the three head-count categories.

## 7. Mechanics and state variables

| State | Meaning | Update | Why sufficient |
|---|---|---|---|
| `remaining`, `steps` | Current quotient and completed halvings | Floor-divide, increment | Recovers the exact quotient invariant |
| `i`, `row_size`, `cumulative` | Current row and counted pairs so far | Add the next disjoint row | No earlier row needs revisiting |
| `power`, `geometric` | Current geometric term and prefix | Add, then double | Consecutive terms have fixed ratio |
| `term`, `harmonic` | Denominator and exact reciprocal prefix | Add `Fraction(1, term)` | Retains an exact small reference value |
| Outcome and measurement | Complete result and its event/count value | Multiply by weight, add | Keeps the probability space unchanged |

These are teaching state variables, not a universal solution template for every math problem.

## 8. Correctness reasoning

For halving, initialization gives `remaining = floor(n/1)`. Floor-dividing a nonnegative integer
quotient by two preserves `remaining = floor(n/2^t)` at the next step. When the guard is true,
the positive value strictly decreases; eventually it is one. The invariant and exit condition
give both sides of `2^t <= n < 2^(t+1)`, establishing the exact answer, not just an upper bound.

For pair counting, row `i` contains precisely indices `i+1..n-1`. Rows cannot share a pair
because its smaller index is unique. Every legal pair has such an index, so the rows are complete.
Their lengths sum to the answer; the arithmetic identity changes only how that sum is evaluated.
Self-pairs and reversed duplicates are safely excluded by the stated unordered-distinct contract.

For probability, assign nonnegative masses summing to one before evaluating an event. Adding
the masses of its outcomes neither misses an outcome nor counts it twice. An expected count
weights the count, not merely a boolean event. The indicator proof in section 5 applies to
dependent events too; multiplying their probabilities requires a separate independence argument.

## 9. Complexity derivation

Always distinguish a workload from a script that merely summarizes its count. Let `n` be the
positive magnitude being halved, `N` the number of distinct positions, `h` the number of series
terms, `m` the number of sampled items, `b` the bucket count, `T` sampled trials, `B` the maximum
bit length of an arithmetic value, and `L` the number of materialized output slots.

| Operation or representation | Dominant work and time model | Auxiliary / output / stack space |
|---|---|---|
| Halving count, without a trace list | `floor(log2 n)` divisions; `Theta(log n)` for unit-cost integers | Constant integer count / one count / constant stack |
| `halving_trace` | Same divisions, plus one record per state | Constant live state / `Theta(log n)` integer records / constant stack |
| Visit every distinct pair | `N(N-1)/2` visits; `Theta(N^2)` for `N >= 2` | Constant loop state / scalar count or `Theta(N^2)` pair records / constant stack |
| `pair_trace` | `N` arithmetic row summaries; `Theta(N)` in a word model | Constant live state / `Theta(N)` records / constant stack |
| Formula `N(N-1)//2` | Constant arithmetic operations, with bit-dependent costs | Arithmetic workspace / `O(log(N+1))` result bits / constant stack |
| `series_trace(h)` | `h` integer and rational updates, including rational reduction | Arithmetic workspace / `h` records with growing numbers / constant stack |
| Explicit lists for every subset | `2^N` lists; across them `N*2^(N-1)` selected-item slots for `N >= 1` | Generation state depends on method / `Theta(N 2^N)` slots / method-dependent stack |
| Tiny exact collision experiment | `b^m` assignments, all `C(m,2)` comparisons per assignment | `O(b+m)` iterator/work items / scalar aggregates / constant stack |
| Sampled collision experiment | `T` trials, `m` draws and `C(m,2)` comparisons each | `O(m)` work items plus generator state / scalar aggregates / constant stack |

The pair formula computes a count; it cannot materialize `L` outputs in fewer than `Omega(L)`
writes. Likewise, `math.comb` returns a potentially huge integer, not a list of selections.

For unbounded Python integers, add bit costs to the word model. A `B`-bit operand takes
`Theta(B)` storage; integer addition and division by a small fixed integer can take `O(B)` bit
work, and multiplication is not a unit operation. The halving trace uses `O(B^2)` bit work
and stored value bits across its decreasing operands. Omitting the trace leaves `O(B)` live
value storage. No portable constant-time guarantee is made for `bit_length` or `math.comb`.

For exact rational traces, let `C(B)` bound one update including reduction, and `W(B)` its
workspace. The trace needs `O(h C(B))` arithmetic time, `O(B + W(B))` auxiliary bits, and
`O(h B)` output bits. This deliberately does not disguise a growing numerator/denominator as
a fixed-size float. The experiment notes specify their own finite workloads and cost assumptions.

## 10. Implementations

### Generic pseudocode

```text
remaining = positive input n
steps = 0
record initial state
while remaining > 1:
    remaining = floor(remaining / 2)
    steps += 1
    record state and check remaining = floor(n / 2^steps)
return recorded states
```

### Idiomatic Python

The complete [micro-lab](practice/micro_lab.py) implements the four teaching traces above.
Read its small loops after making a prediction. Exact library tools can then check a derivation:

```python
from fractions import Fraction
from math import comb

n = 13  # Positive integer; these are exact base-two boundaries.
floor_exponent = n.bit_length() - 1
ceiling_exponent = (n - 1).bit_length()
unordered_selections = comb(6, 2)
exact_weight = Fraction(2, 7)
```

The integer identities follow from the documented [`int.bit_length` contract](https://docs.python.org/3.14/library/stdtypes.html#int.bit_length).
[`math.comb`](https://docs.python.org/3.14/library/math.html#math.comb) counts unordered selections
without replacement; invalid negative arguments are errors. [`Fraction`](https://docs.python.org/3.14/library/fractions.html)
constructed from integer numerator/denominator preserves an exact ratio. Constructing it from
an already rounded float preserves that float's value, not the intended decimal fraction.

### Python 3.11 compatibility

All scripts use syntax and standard-library interfaces available in Python 3.11. Fraction output
uses `str` or an explicit conversion to `float`; it does not need newer Fraction formatting APIs.
Canonical runs use the repository's Python 3.14 environment. On 2026-08-30 the micro-lab and
both experiment scripts also ran successfully under CPython 3.11.16 on Linux x86_64, and all
unit Python files compiled there. The 36 pytest scaffold checks ran under CPython 3.14.7;
this does not claim a separate pytest run under Python 3.11.

### First-principles versus standard-library choice

Derive the counted objects and boundaries first, then use the library. Reimplementing factorials
does not fix an incorrect selection model. A floating [`log2`](https://docs.python.org/3.14/library/math.html#math.log2)
is useful numerically but cannot be assumed to decide exact integer thresholds near a power.

From this unit directory, run:

```bash
uv run --group dev python practice/micro_lab.py
uv run --group dev python -m pytest -q practice/test_math_traces.py experiments
```

If a sandbox makes the default uv cache read-only, prefix a command with
`env UV_CACHE_DIR=/tmp/dsa-fnd-070-uv-cache`; do not change repository pins to solve a cache issue.

## 11. Edge-case matrix

| Dimension | Minimal adversarial case | Required behavior or question | Risk |
|---|---|---|---|
| Log domain | `n=0`, `n<0`, or base one | Reject or specify a different contract | Undefined logarithm or no progress |
| No transition | `n=1` | Zero halving/covering steps | Counting initial state as work |
| Boundary | `2^k-1`, `2^k`, `2^k+1` | Apply exact floor/ceiling inequalities | Float rounding or wrong guard |
| Empty sum / product | Zero terms / zero choices | Sum zero; empty product one | Treating “nothing selected” as no construction |
| No legal pair | `N=0` or `N=1` | Count zero | Negative range or accidental self-pair |
| Impossible selection | `k>N`, no replacement | Count zero | Applying factorials to negative values |
| Duplicates | Two positions both store `5` | State position-based or value-based equality | Incorrect duplication factor |
| Conditional probability | Conditioning event has mass zero | Ordinary ratio is undefined | Division by zero |
| Certain/impossible event | Probability one or zero | Respect range `[0,1]` | Invalid complement or denominator |
| Random count | More than one success possible | Expectation may exceed one | Confusing count with event probability |
| Large output / integer | All subsets or a huge count | Account for output slots / integer bits | Calling one expression constant-time |

## 12. Comparisons and anti-signals

| Tempting alternatives | Decision rule |
|---|---|
| Floor versus ceiling logarithm | Derive the terminal inequality, including strictness |
| Geometric versus harmonic sum | Constant ratio versus reciprocal index; both require correct endpoints |
| Sum versus product of counts | Disjoint cases versus sequential choices with known branching counts |
| Permutation versus combination | Does exchanging the selected positions change the output? |
| Count versus enumeration | Is a number enough, or must every object be produced/inspected? |
| Expected count versus event probability | Is the measured variable a count or a zero/one indicator? |
| Expected versus amortized bound | Declared randomness versus a bound over an operation sequence |
| Simulation versus proof | A run measures a model; it cannot establish an identity for every input |

Do not infer an algorithm solely from a familiar formula. A triangular number does not imply
that arbitrary pairwise data can be processed without inspection. A small mean does not establish
a hard latency limit. Pairwise independence alone does not justify a product across many events.

## 13. Common bugs and debugging

| Failure | Small counterexample or symptom | Repair |
|---|---|---|
| Count states as transitions | `8 -> 4 -> 2 -> 1` has four states | Count the three arrows |
| Use floor for covering capacity | Capacity eight cannot cover nine | Check the terminal inequality |
| Divide a factor too early | `4*((4-1)//2)` gives four pairs | Preserve exact divisibility of the whole product |
| Treat every shrinking sum as constant | Harmonic prefixes keep growing | Bound blocks, not just individual terms |
| Divide by symmetry with unequal multiplicities | Repeated values identify some constructions differently | Define outputs and prove the duplication factor |
| Assume head-count categories are equally likely | Two coins have three counts but four elementary outcomes | Keep weights when merging descriptions |
| Multiply dependent event probabilities | Removing an item changes the next draw | Use conditional probabilities |
| Read expectation as a guarantee | Two fair coins can produce zero or two heads | Describe the distribution and worst case separately |
| Demand every larger sample be closer | Fixed-seed prefixes can move away from the mean | Record observations without a monotonicity claim |

## 14. Practice ladder

The [practice file](practice/README.md) owns the full unsolved contracts. Hints stay locked.

1. Concept micro-drill: explain the two stopping tests in `DSA-FND-070-P01` aloud.
2. Hand-worked trace: fill the supplied `DSA-FND-070-P01` inputs before using Python.
3. Guided observation: predict the micro-lab, then use it to check state meanings in `DSA-FND-070-P02`.
4. Labeled independent reasoning: complete `DSA-FND-070-P03` without reading any comparison answer.
5. Changed-constraint variation: complete both sampling contracts in `DSA-FND-070-P04`.
6. Confused-model comparison: defend the output representations in `DSA-FND-070-P05`.
7. Mixed unlabeled work: open only `DSA-FND-070-P06` (Packet A) during its attempt.
8. Timed interview: use `DSA-FND-070-P07` (Packet B), preserving the first explanation.
9. Delayed re-solve: use the 1/3/7/14/30-day prompts in [REVIEW.md](REVIEW.md).
10. Unseen transfer: ask for a fresh unlabeled task only after closing the current packets;
    neither generated material nor a previously seen example is unseen-transfer evidence.

## 15. Interview questions, traps, and follow-ups

### Recognition and approach questions

1. What exact inequality does “enough capacity” require, and which tiny boundary checks it?
2. Can you explain what is counted before naming a logarithm, sum, or combination?
3. What is the brute-force enumeration, and which work does the proposed formula remove?

### Invariant and correctness questions

1. What invariant relates the remaining value to the number of completed floor divisions?
2. Why does every unordered pair appear in exactly one row of the triangle?
3. What proves that the factor you divide by counts every output equally many times?
4. Which probability calculation needs independence, and which expectation calculation does not?

### Complexity questions

1. If there are logarithmically many levels, when is the total work nevertheless linear?
2. What is the difference between computing `2^N` and returning every selected-item list?
3. Which input variable measures a Python integer's representation, and how can it change complexity?
4. Does the trace helper perform the represented work or only summarize it?

### Changed-constraint follow-ups

1. What changes if the loop rounds up instead of down, or the comparison becomes strict?
2. What changes if selected items can repeat or their order now matters?
3. What changes if the draws are weighted, or one draw removes an item?
4. What additional argument is needed when a caller requires a worst-case latency bound?

### Common traps and weak-answer repairs

- Trap: “Average means half the worst case.” What distribution or calculation would justify that?
- Trap: “All events are pairwise independent, so I can multiply all probabilities.” What stronger
  condition would that multiplication need?
- Weak answer: “Use `comb`.” Repair it by naming the objects, roles, replacement policy, and
  the exact symmetry being removed before quoting a library result.

## 16. Explanation exercises

1. In 90 seconds, explain why the two arrow traces in the notebook core have different lengths.
   Use inequalities and one boundary example without relying on floating-point output.
2. Derive a sum using a drawing, then explain why the drawing is complete for every legal input.
3. In two minutes, distinguish expected count, event probability, and observed frequency using
   one sample space. State exactly where independence enters.
4. Give a count-only explanation, then revise its time and memory claims when all objects must
   be returned as lists. Include Python integer and output-representation costs.

## 17. Experiment decision

Created two supplementary experiments because these misconceptions benefit from actual observation:

- [DSA-FND-070-X01 — Integer logarithm boundaries](experiments/DSA-FND-070-X01-integer-log-boundaries/README.md)
  compares exact integer inequalities with floating logarithms around powers of two.
- [DSA-FND-070-X02 — Expectation and observed frequency](experiments/DSA-FND-070-X02-expectation-and-frequency/README.md)
  separates the exact mean number of matching pairs from the probability of any match, then
  measures finite samples under an explicit uniform independent model.

These are bounded demonstrations, not benchmarks or extra curriculum requirements. Recorded
initialization runs establish that the artifacts execute, not that Rahul has completed an experiment.

## 18. Vocabulary and professional English

| Word | Pronunciation | Simple meaning | Meaning here |
|---|---|---|---|
| Multiplicity | mul-tih-PLISS-ih-tee | How many times something occurs | How many constructions represent one output |
| Expectation | ek-spek-TAY-shun | An anticipated amount | The probability-weighted mean of a random variable |

Multiplicity examples: a file can occur twice in a list; an order can contain three identical
items; repeated invitations can represent one guest. **Interview:** “I divide only after proving
the same multiplicity for each result.” **Engineering:** “Deduplication changes whether we count
events or distinct identifiers.”

Expectation examples: an estimate need not match every observation; a small average can coexist
with a large outlier; repeated trials can help estimate a mean. **Interview:** “This expectation
uses the stated uniform distribution.” **Engineering:** “An expected cost does not replace a
worst-case latency requirement.”

## 19. Python Mastery references

Exact links come from [PYTHON_REFERENCES.md](../../../PYTHON_REFERENCES.md):

- [PY-MPR-070 — Algorithmic and memory complexity](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mpr-070): explicit input variables and bit/output costs.
- [PY-BLT-040 — Lists, tuples, ranges, and sequence behaviour](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-blt-040): half-open ranges and trace storage.
- [PY-TST-020 — Pytest fundamentals and fixtures](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-tst-020): running the supplied scaffold checks.
- [PY-TST-030 — Parametrization, marks, monkeypatching, and fixture composition](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-tst-030): concise checks around boundary families.

## 20. Authoritative sources

Read on 2026-08-30. Explanations, diagrams, examples, exercises, and code here are original.

| Source | Use and classification |
|---|---|
| [MIT 6.042J, sums, products, and asymptotics](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/0287cc25b80969d0e83c5ea3e854c227_ln8.pdf) | Mathematical identities and harmonic bounds |
| [MIT 6.042J, counting](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/5f8110ee5b0df0da6173de66ff35c7b0_ln9.pdf) | Product and division rules |
| [MIT 6.042J, probability](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2005/56a41986aa7ab49261e3ff80017e8cf4_ln12.pdf) | Conditional probability; pairwise versus mutual independence |
| [MIT 6.042J course notes, section 18.3](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-fall-2010/93cad640cf3ed0b23ef70688f452d4d5_MIT6_042JF10_notes.pdf) | Linearity and indicator expectations |
| [Python integer types](https://docs.python.org/3.14/library/stdtypes.html#int.bit_length) | Language/type behavior; exact bit-length contract |
| [Python math library](https://docs.python.org/3.14/library/math.html) | Standard-library contracts, not universal timing guarantees |
| [Python fractions](https://docs.python.org/3.14/library/fractions.html) | Exact rational construction and float caveats |
| [Python random](https://docs.python.org/3.14/library/random.html#notes-on-reproducibility) | Seeded observations, reproducibility limits, and non-security use |
