# DSA-FND-020 — Brute-force enumeration and bottleneck discovery

## Physical Notebook Core

Use this page when the optimized idea is not obvious. A trustworthy exhaustive baseline is a map of the candidate space and a measuring instrument for the work.

### Problem shape or pressure

A problem asks whether, which, or how many candidates satisfy a condition. The direct method can generate every legal candidate and test it. That is often the easiest method to prove correct, but the maximum constraints may make its repeated candidate generation or evaluation infeasible.

### One-sentence mental model

> Enumerate every legal candidate exactly once, measure the work inside each check, and optimize the named repetition rather than the visible loop syntax.

### Essential visual

```text
values = [4, 1, 7, 4], target = 8
legal candidates are index pairs i < j

candidate space                 predicate
(0,1) -> 4+1 = 5              no
(0,2) -> 4+7 = 11             no
(0,3) -> 4+4 = 8              yes
(1,2) -> 1+7 = 8              yes
(1,3) -> 1+4 = 5              no
(2,3) -> 7+4 = 11             no

rows checked = 3 + 2 + 1 = 6 = 4(4-1)/2
                       |
                       v
exact bottleneck: one explicit predicate check per unordered pair
optimization contract: avoid generating or evaluating most pairs explicitly
```

#### How to read this visual

Read the index rule before the values. `i < j` excludes self-pairs and prevents the ordered duplicates `(i, j)` and `(j, i)`. Then read each row as one candidate-generation event followed by one predicate evaluation. The triangular row lengths produce the exact count.

#### Key insight

Brute force is not synonymous with careless code. Its value comes from a precise candidate definition, complete coverage, no duplicates, and an auditable predicate. The bottleneck is the repeated operation multiplied by the number of candidates—not the phrase “nested loops.”

#### Simplification or limitation

This trace uses a small materialized sequence, constant-time integer operations in the teaching model, and a request to find all matching index pairs. Large Python integers have size-dependent arithmetic costs, and returning only one witness may allow early exit on some inputs but not improve the no-match worst case.

### Governing invariant or rules

1. Before candidate `(i, j)` is checked, every legal pair earlier in lexicographic order has been checked exactly once and no illegal pair has been checked.
2. The recorded matches are exactly the checked candidates that satisfy the predicate.
3. Each transition advances to the next legal candidate; when no candidate remains, coverage is complete and enumeration terminates.

### Minimal reasoning skeleton

~~~text
write the exact candidate object and legality rule
construct the simplest generator for every legal candidate
state why there are no omissions and no duplicates
write the predicate evaluated for one candidate
count legal candidates exactly when practical
count the dominant work inside one evaluation
multiply or sum to obtain total worst-case work
name the repeated information or operation
state what an optimization must avoid, reuse, or exclude
only then choose a faster representation or pattern
~~~

### Complexity

- Input variables: `n` input items, `c(n)` legal candidates, `e(n)` work per candidate, and `r` emitted matches.
- Time: `Theta(c(n) * e(n))` when each candidate has the same evaluation cost; use a sum when costs differ. Pair enumeration with constant-time checks is `Theta(n^2)` because `c(n) = n(n-1)/2`.
- Auxiliary space: `Theta(1)` for loop indices and a few scalar values when candidates are streamed; `Theta(c(n))` if all candidates are materialized first.
- Output space: `Theta(r)` when every match must be returned; this is separate from auxiliary space.
- Recursion stack: zero for the iterative examples here.
- Important Python cost: `sum(values[left:right + 1])` first creates a slice and then traverses it; placing it inside candidate loops makes evaluation cost grow with interval length. A generator can avoid materializing all candidates, but it does not reduce how many are consumed.

### Recognition cues and anti-cues

- Signal: small constraints, a finite candidate space, a need for a correctness oracle, or an optimization that has not yet been derived.
- Constraint signal: substituting maximum `n` into the exact candidate count makes explicit enumeration too large.
- Anti-signal: calling an approach “brute force” without defining candidates, or rejecting it only because the code contains two loops.

### Important comparison

Candidate count versus evaluation cost: enumerating `Theta(n^2)` intervals and evaluating each in `Theta(1)` is `Theta(n^2)`; enumerating the same intervals and re-summing each in up to `Theta(n)` work is `Theta(n^3)` total.

### Common failure

Using `for i in range(n)` and `for j in range(n)` for unordered distinct pairs checks self-pairs and both orders. At `n = 4` it performs 16 iterations for only 6 legal candidates, and an implementation can accidentally reuse one position.

### Recall prompts

1. What is the candidate object, and what rule makes it legal?
2. What exact operation repeats, and how many times does it run in the worst case?
3. Does the proposed optimization reduce candidate count, evaluation cost, or both?

| Field | Value |
|---|---|
| Domain | Problem-solving foundations |
| Curriculum | [CURRICULUM.md](../../../CURRICULUM.md#dsa-fnd-020) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Pattern index | [PATTERN_INDEX.md](../../../PATTERN_INDEX.md) |
| Problem bank | [PROBLEM_BANK.md](../../../PROBLEM_BANK.md) |
| Primary outcome | Construct the simplest correct exhaustive solution, identify repeated work, and name the exact bottleneck that an optimization must remove. |
| Hard prerequisites | DSA-FND-010 |
| Soft prerequisites | None |
| Priority | Core |
| Interview frequency | High |
| Practical relevance | High |
| Python relevance | High |
| Difficulty | 2 |
| Depth | D2 |
| Scope | Foundations, Algorithms, Interview |
| Size | M |
| Evidence | E+T+I+P+D+R+M |
| Artifact state | Draft |
| Canonical Python | 3.14 |
| Interview compatibility | 3.11 |

## 1. Learning outcomes and evidence

After this unit Rahul should be able to:

1. define the legal candidate space for pairs, triples, subsets, intervals, assignments, or paths without omissions or duplicates;
2. implement a simple exhaustive baseline whose coverage and termination can be defended;
3. derive total work from candidate count and per-candidate evaluation cost rather than from source-code shape;
4. locate the first repeated operation or information and state a precise optimization contract;
5. use a small exhaustive implementation as an oracle or diagnostic tool without mistaking it for a scalable final method;
6. communicate the baseline, bottleneck, and required improvement before naming a pattern.

Required evidence:

- Explain and hand-trace a legal candidate space, including the coverage invariant and exact check count.
- Implement the separate triple-enumeration challenge after a genuine attempt, while preserving distinct indices and deterministic output order.
- Prove soundness, completeness, no duplication, progress, and termination for an exhaustive baseline.
- Debug a candidate generator that includes illegal or duplicate states, and derive the corrected complexity.
- Complete delayed recall and an unlabeled transfer in which neither the intended pattern nor target complexity is disclosed.

## 2. Prerequisite bridge

`DSA-FND-010` is the hard prerequisite. Its tracker currently contains no learner-produced evidence, so use this minimum bridge before starting the exercises:

| Unit | Why it matters | Minimum bridge |
|---|---|---|
| `DSA-FND-010` | Enumeration is only meaningful after inputs, output predicate, identity rules, constraints, and allowed mutation are explicit. | Write the candidate object, its legality predicate, maximum input variables, required output cardinality, and mutation/order permissions before writing loops. |

This bridge is enough to enter the unit, but it does not replace a closed-book review of `DSA-FND-010`.

## 3. Intuition and problem shape

When the clever method is missing, start with a method that is easy to trust. Exhaustive enumeration separates three questions:

1. **What could the answer be?** This defines the candidate space.
2. **Which candidates are legal?** This removes self-use, duplicates, invalid boundaries, and broken constraints.
3. **Does this legal candidate satisfy the output predicate?** This is the evaluator.

For an input of length `n`, common candidate spaces include:

| Candidate object | Canonical index rule | Exact candidate count |
|---|---|---:|
| one item | `0 <= i < n` | `n` |
| unordered pair of distinct positions | `0 <= i < j < n` | `n(n-1)/2` |
| ordered pair of distinct positions | `0 <= i != j < n` | `n(n-1)` |
| contiguous non-empty interval | `0 <= left <= right < n` | `n(n+1)/2` |
| unordered triple of distinct positions | `0 <= i < j < k < n` | `n(n-1)(n-2)/6` |
| binary include/exclude choices | one choice per item | `2^n` |

The table is a starting vocabulary, not permission to quote a formula without deriving the legal states for the actual contract.

### Why a baseline is useful even when it is slow

- It gives a correctness reference for tiny inputs.
- It reveals whether duplicate states are being generated.
- It exposes the dominant repeated work.
- It helps construct adversarial tests for a later optimized method.
- It makes the optimization claim falsifiable: the new method must return the same result while removing a named cost.

“Brute force” is therefore a design stage and an evidence tool, not an insult.

## 4. Brute force and bottleneck

### Simplest correct baseline

This teaching helper returns every matching unordered index pair:

~~~python
def matching_index_pairs(values: list[int], target: int) -> list[tuple[int, int]]:
    matches: list[tuple[int, int]] = []
    for left in range(len(values)):
        for right in range(left + 1, len(values)):
            if values[left] + values[right] == target:
                matches.append((left, right))
    return matches
~~~

The goal here is not to pre-empt later hash-table or two-pointer units. It is to make candidate coverage, distinct-position semantics, output cardinality, and exact repeated work visible.

### Exact bottleneck

The inner predicate executes

~~~text
(n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2
~~~

times, regardless of how many matches are appended, because the contract returns every matching index pair. With `n = 100,000`, that is `4,999,950,000` candidate checks. The exact bottleneck is explicit evaluation of the sum predicate for every unordered pair.

For a different baseline, the candidate count may not be the only cost. This interval code enumerates `n(n+1)/2` intervals but repeatedly rebuilds and sums slices:

~~~python
def all_interval_totals_recomputed(values: list[int]) -> list[int]:
    totals: list[int] = []
    for left in range(len(values)):
        for right in range(left, len(values)):
            totals.append(sum(values[left:right + 1]))
    return totals
~~~

Across all intervals, the number of element contributions is

~~~text
sum over lengths L of L(n-L+1)
= n(n+1)(n+2)/6
~~~

and slicing also allocates those elements before `sum` consumes them. Here the bottleneck is repeated reconstruction and aggregation of overlapping interval contents, not merely interval enumeration.

## 5. Derivation and invariant

Use this derivation chain:

~~~text
contract
→ candidate object
→ legality rule
→ exhaustive generator
→ coverage/no-duplicate invariant
→ predicate for one candidate
→ exact candidate count
→ cost of one evaluation
→ total worst-case work
→ repeated operation or information
→ optimization contract
~~~

For unordered pairs, derive loop bounds from the legality predicate `i < j`:

- `i` can start at zero and stop before `n`;
- once `i` is fixed, `j` starts at `i + 1` so self-pairs and earlier reversed pairs cannot appear;
- `j` stops before `n` so each candidate stays in bounds.

The **enumeration invariant** is:

> Before the next `(i, j)` is evaluated, every legal pair earlier in the loop order has been evaluated exactly once, no later legal pair has been evaluated, and the result contains exactly the matches among the evaluated pairs.

This invariant supports two kinds of optimization question:

1. **Reduce candidates:** prove that many candidates can be excluded without evaluation.
2. **Reduce evaluation cost:** retain a summary so repeated information is not reconstructed.

A proposed method is not an optimization merely because it has fewer visible lines. It must reduce one of those costs while preserving the original predicate.

## 6. Detailed visual trace

### From candidate grid to legal triangle

~~~text
n = 4 positions: 0 1 2 3

full ordered grid                    keep only i < j

        j=0  j=1  j=2  j=3              j=0  j=1  j=2  j=3
i=0      X    A    B    C          i=0        A    B    C
i=1      a    X    D    E          i=1             D    E
i=2      b    d    X    F          i=2                  F
i=3      c    e    f    X          i=3

X = illegal self-pair
lowercase = reverse duplicate of the uppercase pair
uppercase triangle = six legal unordered candidates

loop state for values [4,1,7,4], target 8

step  candidate  total  match  completed legal prefix
 1      (0,1)      5     no    A
 2      (0,2)     11     no    A B
 3      (0,3)      8     yes   A B C
 4      (1,2)      8     yes   A B C D
 5      (1,3)      5     no    A B C D E
 6      (2,3)     11     no    A B C D E F

final matches = [(0,3), (1,2)]
~~~

#### How to read this visual

First compare the square grid with the upper triangle. Every removed diagonal cell violates distinct-position identity; every removed lowercase cell duplicates an uppercase unordered pair. Then read the step table downward. After each row, the completed prefix grows by one legal candidate, and the result changes only when the predicate is true.

#### Key insight

Loop bounds are a compact encoding of the candidate-set proof. `right = left + 1` is not a style preference; it enforces legality and uniqueness.

#### Simplification or limitation

The visual materializes all six conceptual candidates. A real generator may yield them one at a time. Lazy generation lowers storage, but consuming the entire generator still performs six checks and, generally, `n(n-1)/2` checks.

## 7. Mechanics and state variables

| State variable | Meaning | Update rule | Why it is sufficient |
|---|---|---|---|
| `left` | first index of the current candidate row | advance after all larger `right` values are exhausted | partitions the legal triangle into disjoint rows |
| `right` | second index, always greater than `left` | starts at `left + 1`, then increments | enforces distinctness, bounds, and no reverse duplicates |
| `checks` | number of legal candidates evaluated | increment exactly once before or with each predicate test | exposes the dominant work and catches missing/duplicate states |
| `matches` | satisfying candidates among the checked prefix | append only when the predicate is true | is exactly the required output accumulated so far |
| `candidate_count` | number of legal states implied by the contract | derive symbolically before substituting `n` | separates input size from search-space size |
| `evaluation_cost` | work to test one candidate | count traversal, copying, hashing, comparison, or aggregation inside the check | prevents hidden work from disappearing behind a function call |
| `r` | number of emitted matches | increases on a match | keeps output cost separate from work state |

## 8. Correctness reasoning

### Pair baseline

- **Initialization:** before `left = 0, right = 1`, no legal pair has been checked and `matches` is empty, so the invariant holds.
- **Preservation:** one iteration evaluates the next legal pair. It appends that pair exactly when the predicate is true, so the result remains exact for the enlarged checked prefix.
- **Progress and termination:** `right` increases within a finite row; then `left` increases. Both are bounded by `n`, so the nested loops terminate.
- **Completeness:** every legal pair has a unique smaller index `i` and larger index `j`; the iteration with `left = i` and `right = j` visits it.
- **No duplication:** a pair appears only in the row of its smaller index. The reverse order cannot appear because `right > left` always holds.
- **Safe exclusion:** diagonal cells reuse a position and lower-triangle cells are reverse representations of already covered unordered pairs, so neither belongs to the legal candidate set.
- **Final-state argument:** after the final row, every legal pair has been checked exactly once; therefore `matches` contains all and only satisfying pairs.

### What an optimized method must prove

A faster method inherits the same soundness and completeness obligations. It must additionally justify every candidate it does not explicitly check. “I stored earlier values” or “I moved a pointer” is not enough; the retained state or elimination rule must prove that skipped candidates cannot change the answer.

## 9. Complexity derivation

### Candidate count times evaluation cost

Let `C(n)` be the legal candidate count and `E(candidate)` the evaluator work:

~~~text
total work = candidate-generation work
           + sum over legal candidates of E(candidate)
           + output writes
~~~

When `E` is constant, `Theta(C(n))` usually dominates. When `E` depends on the candidate, keep the summation until the dependence is counted.

| Baseline | Candidates | Evaluation work | Total time | Auxiliary space | Output space |
|---|---:|---:|---:|---:|---:|
| every item | `n` | `Theta(1)` | `Theta(n)` | `Theta(1)` | contract-dependent |
| unordered pairs | `n(n-1)/2` | `Theta(1)` | `Theta(n^2)` | `Theta(1)` streamed | `Theta(r)` |
| unordered triples | `n(n-1)(n-2)/6` | `Theta(1)` | `Theta(n^3)` | `Theta(1)` streamed | `Theta(r)` |
| all intervals with carried running total | `n(n+1)/2` | `Theta(1)` per extension | `Theta(n^2)` | `Theta(1)` beyond output | `Theta(n^2)` if all totals returned |
| all intervals with slicing and `sum` | `n(n+1)/2` | proportional to interval length | `Theta(n^3)` | transient slice proportional to interval length | `Theta(n^2)` if all totals returned |
| all include/exclude assignments | `2^n` | at least `Theta(1)` | at least `Theta(2^n)` | representation-dependent | `Theta(r)` |

### Early exit

If the contract asks for one witness, a match may end enumeration early. State three bounds honestly:

- best case: the first candidate matches;
- worst case: no candidate matches or the only match is last;
- required guarantee: normally the worst case unless the problem states a distribution or expected-case model.

Early exit does not convert the worst-case pair search to constant time.

### Python accounting

- A list comprehension materializes every produced item; a generator expression evaluates most of its body lazily as items are requested.
- `itertools.combinations(values, r)` is an iterator and expresses positional combinations clearly, but consuming all of it still emits `math.comb(n, r)` tuples. It may also first pool the input, so do not call its auxiliary space constant for an arbitrary iterable.
- A slice such as `values[left:right + 1]` creates a new list for list input. Count copied references and the later traversal performed by `sum`.
- Appending `r` matches requires output storage proportional to `r`; this is not a flaw if the contract requires all matches.
- Python's arbitrary-precision integers mean arithmetic is not literally constant for unbounded integer magnitude. The unit's formulas use the standard word-operation teaching model unless magnitude is an explicit input variable.

## 10. Implementations

### Generic pseudocode

~~~text
result <- empty
checks <- 0
for each legal candidate in canonical order:
    checks <- checks + 1
    if candidate satisfies the output predicate:
        record candidate in result
return result and checks
~~~

For unordered triples, the legality rule becomes `i < j < k`; each inner bound starts one position after its enclosing index.

### Idiomatic Python trace helper

~~~python
from collections.abc import Iterator


def unordered_index_pairs(n: int) -> Iterator[tuple[int, int]]:
    if n < 0:
        raise ValueError("n must be non-negative")
    for left in range(n):
        for right in range(left + 1, n):
            yield left, right
~~~

The runnable [micro-lab](practice/micro_lab.py) uses this generator to expose candidate shape, predicate results, and exact checks. The learner implementation boundary remains unsolved in [starter.py](practice/starter.py).

### Python 3.11 compatibility

All unit code uses syntax and standard-library APIs available in Python 3.11. The canonical repository runtime is Python 3.14, but the enumeration mechanics do not require newer behavior.

### First-principles versus standard-library choice

Write at least one nested-loop enumerator to make bounds and the coverage proof visible. In production or an interview, `itertools.combinations` can communicate the same positional candidate space succinctly when materialization, ordering, and input-pooling behavior fit the contract. The standard-library spelling changes representation details, not the number of emitted candidates.

## 11. Edge-case matrix

| Dimension | Minimal adversarial case | Expected behavior | Invariant risk |
|---|---|---|---|
| Empty candidate space | `n = 0` | zero candidates and empty output | assuming a first index exists |
| Too few items | `n = 1` for pairs; `n = 2` for triples | zero legal candidates | negative or bogus combination count |
| Self-use | `[4]`, target `8` | no pair | allowing `i == j` |
| Equal values, distinct positions | `[4, 4]`, target `8` | pair `(0, 1)` is legal | deduplicating values instead of positions |
| Reverse duplicates | positions `0` and `1` | emit one unordered pair, not two | generating the full ordered grid |
| All matches | `[0, 0, 0, 0]`, target `0` for triples | emit all four index triples | early return violates output cardinality |
| No matches | large input with impossible target | check the entire legal space | best-case analysis presented as worst case |
| Signed values | `[-3, 1, 2]`, target `0` | valid triple is retained | inventing positivity assumptions |
| Expensive evaluator | all intervals with slicing and `sum` | count candidate length and allocation | assuming one function call is constant |
| Required output size | every matching pair | allocate `Theta(r)` output | calling required output “extra” memory |
| Input mutation | caller requires original order | preserve input unchanged | sorting to simplify enumeration illegally |

## 12. Comparisons and anti-signals

| Candidate | Use when | Reject or revise when | Evidence in the problem |
|---|---|---|---|
| Direct enumeration | constraints are small, a baseline is needed, or a tiny-input oracle is useful | derived worst-case work exceeds the envelope | finite explicit candidate space |
| Ordered Cartesian product | candidate order matters and `(a,b)` differs from `(b,a)` | pairs are unordered or self-use is illegal | direction/role semantics |
| Combinations | positions are chosen without order and without replacement | order matters or reuse is allowed | `i < j < ...` legality |
| Permutations | order matters and positions cannot repeat | order is irrelevant | role assigned to each selected item |
| Materialized candidate list | candidates must be revisited many times and memory permits | one pass is sufficient or candidate count is large | reuse requirement |
| Lazy generator | one-pass consumption can avoid storing candidates | consumers require random access or multiple passes | streaming candidate consumption |
| Memoized/reused evaluation state | many candidates share the same subcomputation | candidates have unrelated evaluation work | overlapping information |
| Candidate elimination | a proof excludes a whole region | exclusion rests only on intuition or samples | monotonicity, ordering, bounds, dominance |

Anti-signals include optimizing before the baseline is correct, citing `O(n^2)` without naming `n`, using wall-clock timing to prove asymptotic growth, and selecting a data structure before stating which repeated operation it removes.

## 13. Common bugs and debugging

| Failure | Symptom | Smallest counterexample | Correction |
|---|---|---|---|
| Full square for unordered pairs | self-pairs and reverse duplicates appear | `n = 2` generates four cells for one legal pair | encode `right > left` in the loop bound |
| Adjacent-only enumeration | non-adjacent candidates are missed | `[4, 0, 4]`, target `8` | generate every `i < j`, not only `j = i + 1` |
| Value deduplication | distinct equal-valued positions disappear | `[4, 4]`, target `8` | define candidates by index identity |
| Wrong upper bound | last index never appears | `[0, 0]`, target `0` | trace half-open ranges on `n = 2` |
| Early return for all-output contract | only the first match is emitted | `[0, 0, 0]` pair target `0` | align termination with output cardinality |
| Candidate count only | interval method is called quadratic despite repeated `sum` | `[1, 2, 3]` | count evaluator traversal and slice allocation |
| Materialize before checking | memory grows with all candidates | generate all triples for large `n` | stream candidates unless replay is required |
| Hidden mutation | later index evidence is invalid | sort input in place | preserve input or retain original positions under permission |
| Formula copied without boundary check | nonsensical result for `r > n` | triples with `n = 2` | derive from the generator and define zero candidates |

Debug candidate generators on `n = 0, 1, 2, 3, 4`. Small spaces can be listed completely, making the first omission or duplicate visible.

## 14. Practice ladder

1. Reconstruct the notebook core and legal-pair triangle from memory.
2. Predict every row from the [pair-space micro-lab](practice/README.md#dsa-fnd-020-p01-audit-the-unordered-pair-space) before running it.
3. Repair an ordered-grid explanation into a unique unordered candidate generator.
4. Implement the protected [triple-enumeration challenge](practice/README.md#dsa-fnd-020-p02-enumerate-target-triples) after writing its coverage invariant.
5. Predict and run the [repeated-interval-work experiment](experiments/DSA-FND-020-X01-repeated-interval-work/README.md).
6. Change an “all matches” contract to “one witness” and separate best from worst case.
7. Compare reducing candidate count with reducing per-candidate evaluation cost.
8. Use a tiny exhaustive baseline as an oracle for a later optimized attempt.
9. Explain baseline and bottleneck in two minutes before proposing a representation.
10. Complete a mixed unlabeled transfer and delayed reconstruction in [REVIEW.md](REVIEW.md).

The problem bank's Two Sum entry belongs canonically to `DSA-SEQ-020`; it is intentionally not reassigned here. This unit uses original candidate-space drills so later pattern evidence remains separate.

## 15. Interview questions, traps, and follow-ups

### Recognition and approach questions

1. What exactly is one candidate, and which index or state rule makes it legal?
2. What is the simplest brute force, and why is it correct before efficiency is discussed?
3. Does the output require any witness, the first witness, the best witness, a count, or every witness?

### Invariant and correctness questions

1. State the enumeration invariant immediately before candidate `(i, j)` is evaluated.
2. Why does `j` starting at `i + 1` prove both distinctness and no reverse duplicates?
3. How do you prove completeness for triples with `i < j < k`?
4. What safe-exclusion proof will the optimized method owe for candidates it never checks?

### Complexity questions

1. Derive the unordered-pair count from row lengths instead of quoting `O(n^2)`.
2. If there are `C(n)` candidates and candidate `x` costs `E(x)` to evaluate, how will you state total work?
3. Why can enumerating all intervals be quadratic in one implementation and cubic in another?
4. Which Python expression in the baseline allocates or traverses data, and how does that change auxiliary space or time?

### Changed-constraint follow-ups

1. How do best- and worst-case costs change if one witness is enough instead of all witnesses?
2. What changes if ordered pairs are distinct outputs, so `(i, j)` and `(j, i)` both matter?
3. What changes if equal values may be reused but the same position may not?
4. What changes if the input is a one-pass iterable rather than a reusable sequence?
5. What changes if candidates must be produced lazily and the consumer may stop early?

### Explanation and communication questions

1. Explain the brute force and exact bottleneck in under two minutes without naming a faster pattern.
2. Explain whether your proposed optimization reduces the candidate space, evaluator cost, or both.

### Common traps and weak-answer repairs

- **Trap:** “Two loops means `O(n^2)`.” A nested evaluator may add another factor, while two monotone loops in another problem may total only linear work.
- **Trap:** “A generator makes it efficient.” Laziness changes materialization and can enable early stopping, but consuming every candidate preserves the enumeration count.
- **Trap:** optimizing a faulty baseline whose candidate space omits equal-valued positions or includes self-use.
- **Weak answer:** “The bottleneck is brute force.” Repair it by naming the exact repeated operation, its count, the input variables, and what must be reused or excluded.
- **Weak answer:** “Hashing is faster.” Repair it by postponing the structure name until the retained information and correctness obligation are explicit.

## 16. Explanation exercises

1. Explain why the six upper-triangle cells are exactly the legal pairs for `n = 4`.
2. Derive `n(n-1)/2` from the row lengths without using a memorized combination formula.
3. Defend the pair-enumeration invariant using the transition from `(0, 3)` to `(1, 2)`.
4. Explain the difference between candidate-generation cost, predicate-evaluation cost, auxiliary space, and output space.
5. Recalculate work when a Boolean pair query changes to returning every matching pair.
6. Explain why a generator can reduce storage without reducing worst-case checks.
7. Use the interval example to explain repeated information without naming a later prefix-sum pattern.
8. Give a small counterexample to an adjacent-only or value-deduplicating baseline.

## 17. Experiment decision

Decision: created and run [DSA-FND-020-X01 — Repeated interval work](experiments/DSA-FND-020-X01-repeated-interval-work/README.md). Although the curriculum evidence does not require `X`, instrumented execution materially reinforces this unit: it separates a fixed interval candidate count from the much larger number of additions caused by rebuilding every interval. The experiment uses deterministic counts rather than presenting machine timing as a universal threshold.

## 18. Vocabulary and professional English

### Exhaustive

| Item | Content |
|---|---|
| Pronunciation | ig-ZAWS-tiv |
| Simple English meaning | Covering every relevant possibility |
| Hindi cue | सम्पूर्ण / सभी संभावनाओं को जाँचने वाला |
| Meaning here | Generating every legal candidate required by the contract |

Examples:

1. The audit was exhaustive.
2. We made an exhaustive list of failure modes.
3. Exhaustive testing is possible only for a small finite state space.
4. **Interview:** “I will begin with an exhaustive pair enumeration whose coverage is easy to prove.”
5. **Engineering discussion:** “The small-input exhaustive checker is our differential oracle.”

### Bottleneck

| Item | Content |
|---|---|
| Pronunciation | BOT-uhl-nek |
| Simple English meaning | The part that most limits progress or performance |
| Hindi cue | मुख्य बाधा |
| Meaning here | The dominant repeated operation that a useful optimization must remove or reduce |

Examples:

1. Approval became the bottleneck in the process.
2. Network latency is the current bottleneck.
3. Adding workers will not help if storage is the bottleneck.
4. **Interview:** “The bottleneck is re-summing every overlapping interval, not generating the interval boundaries.”
5. **Engineering discussion:** “Profile data confirms serialization, rather than database lookup, is the bottleneck.”

### Candidate

| Item | Content |
|---|---|
| Pronunciation | KAN-di-dayt |
| Simple English meaning | One possibility being considered |
| Hindi cue | संभावित विकल्प |
| Meaning here | A legal state or object that may satisfy the output predicate |

Examples:

1. Three candidates reached the final interview.
2. This material is a candidate for replacement.
3. Each route is a candidate plan.
4. **Interview:** “An unordered pair of distinct indices is one candidate.”
5. **Engineering discussion:** “We reduced the candidate set before running the expensive validator.”

## 19. Python Mastery references

- [PY-BLT-040 — Lists, tuples, ranges, and sequence behaviour](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-blt-040): bridge for half-open ranges, indexing, slicing, and materialization.
- [PY-BLT-090 — Protocol-facing built-in functions and container complexity](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-blt-090): bridge for work hidden by `sum`, membership, and other concise built-ins.
- [PY-FIT-080 — Generators, yield, and delegation](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-fit-080): optional support for lazy candidate generation.
- [PY-MPR-070 — Algorithmic and memory complexity](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mpr-070): deeper Python-side accounting for time, auxiliary space, output, and integer costs.
- [PY-MPR-080 — Responsible benchmarking](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mpr-080): use before turning deterministic work counts into empirical timing claims.

These are supporting references rather than additional hard prerequisites for this unit.

## 20. Authoritative sources

- [MIT 6.006 Spring 2020, Lecture 1: Introduction](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/477c78e0af2df61fa205bcc6cb613ceb_MIT6_006S20_lec1.pdf) — supports separating a problem's correct-output predicate from an algorithm, proving correctness for general inputs, and analyzing efficiency by counting modeled operations. Its birthday-matching example also contrasts a quadratic scan with retained search state.
- [MIT 6.006 Spring 2020, Lecture 20: Course Review](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/aa4f264093faf990054cc4820553bb46_MIT6_006S20_lec20.pdf) — classifies brute force as an algorithm-design approach and keeps correctness, efficiency, and communication as separate obligations.
- [Python 3.14 documentation: `itertools`](https://docs.python.org/3.14/library/itertools.html#itertools.combinations) — documents positional combinations, their `math.comb(n, r)` output count, lexicographic emission order, and iterator behavior.
- [Python 3.14 language reference: generator expressions](https://docs.python.org/3.14/reference/expressions.html#generator-expressions) — documents generator creation and lazy evaluation behavior used in the materialization comparison.

All diagrams, examples, exercises, lab code, and experiment design in this unit are original. No LeetCode statement or editorial is reproduced.
