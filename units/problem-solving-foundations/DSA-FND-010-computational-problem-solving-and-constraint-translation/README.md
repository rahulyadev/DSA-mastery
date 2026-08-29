# DSA-FND-010 — Computational problem solving and constraint translation

## Physical Notebook Core

Keep this page in the notebook: it is the translation checkpoint to use before choosing an algorithm.

### Problem shape or pressure

A prompt mixes story, data, limits, required behavior, and freedoms. The danger is solving a familiar-looking problem while silently changing one of those facts.

### One-sentence mental model

> Turn prose into a testable contract, turn limits into an operation budget, and only then search for an algorithm.

### Essential visual

```text
Prompt: distinct positions whose values sum to target
                    |
                    v
+---------------- CONTRACT ----------------+
| inputs: values[0:n], target               |
| output: one Boolean                       |
| rule: exists i < j with values[i]+values[j]=target
| n: 0..200,000; negatives and duplicates allowed
| original order/data must not be changed   |
+-------------------------------------------+
                    |
                    v
all unordered pairs = n(n-1)/2
at n = 200,000      = 19,999,900,000 checks
                    |
                    v
Required search shape: avoid examining every pair;
retain only state justified by the contract.
```

#### How to read this visual

Read downward. First name the objects and the exact output. Next translate words such as “distinct” and “exists” into predicates. Then attach every limit and permission to that contract. Only after the contract is stable should a candidate's dominant work be counted in terms of the input variables.

#### Key insight

Constraints do not identify one algorithm, but they can reject whole families of algorithms. The result of translation is a feasible envelope plus a correctness contract—not a guessed pattern name.

#### Simplification or limitation

The operation count is an abstract model, not a prediction of seconds on every machine. It also does not select the eventual data structure or prove that a faster solution is correct.

### Governing invariant or rules

1. Every example, candidate, and test uses the same input/output contract.
2. No candidate may assume a permission the statement did not grant, such as mutation, reordering, random access, or approximate output.
3. Reject a candidate only through an explicit conflict: incorrect behavior, too much dominant work, too much space, or failure to emit the required output.

### Minimal reasoning skeleton

~~~text
write inputs and independent size variables
write the exact output predicate
translate semantic words: any/all, distinct, contiguous, stable, online
list bounds, allowed mutations, ordering, and memory
construct normal, boundary, and adversarial examples
state the simplest correct baseline
count its dominant operation
compare the count with the stated budget
record the required time/space/output envelope
only then propose candidate state or a pattern
~~~

### Complexity

- Input variables: n items, q queries or operations, r returned items, and sometimes V vertices plus E edges.
- Time: count dominant work symbolically; for example, all unordered pairs require n(n−1)/2 checks, while q independent full scans require nq visits.
- Auxiliary space: state used beyond the input and required output; name whether it grows with n, q, or another variable.
- Output space: at least proportional to r when r items must be materialized.
- Recursion stack: zero for the iterative examples in this unit.
- Important Python cost: range(n) is lazy, while list(range(n)) materializes n references; a hidden copy or repeated membership scan can change the budget.

### Recognition cues and anti-cues

- Signal: the statement contains large limits, multiple size variables, many queries, streaming language, or strict mutation/order rules.
- Constraint signal: substituting the maximum values makes a baseline operation count obviously exceed the supplied abstract budget.
- Anti-signal: choosing a named pattern from one familiar word before writing the output predicate and constraints.

### Important comparison

Constraint translation versus pattern recognition: translation defines what every valid answer must do and what resources it may use; pattern recognition proposes one way to meet that contract.

### Common failure

“Duplicates are allowed” is not enough. If two equal values may be used, the contract must still require distinct positions. The one-element input [4] with target 8 catches an implementation that reuses one position.

### Recall prompts

1. Which nouns become inputs, and which quantities need independent variables?
2. Which word in the output sentence carries the quantifier: any, every, first, minimum, or all?
3. What exact count rules out the simplest candidate at the maximum constraints?

| Field | Value |
|---|---|
| Domain | Problem-solving foundations |
| Curriculum | [CURRICULUM.md](../../../CURRICULUM.md#dsa-fnd-010) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Pattern index | [PATTERN_INDEX.md](../../../PATTERN_INDEX.md) |
| Problem bank | [PROBLEM_BANK.md](../../../PROBLEM_BANK.md) |
| Primary outcome | Translate a problem statement and constraints into explicit inputs, outputs, candidate state, and feasible complexity budgets. |
| Hard prerequisites | None |
| Soft prerequisites | None |
| Priority | Core |
| Interview frequency | High |
| Practical relevance | High |
| Python relevance | High |
| Difficulty | 1 |
| Depth | D1 |
| Scope | Foundations, Interview |
| Size | M |
| Evidence | E+T+P+D+R+M |
| Artifact state | Draft |
| Canonical Python | 3.14 |
| Interview compatibility | 3.11 |

## 1. Learning outcomes and evidence

After this unit Rahul should be able to:

1. rewrite an unfamiliar prompt as an explicit input contract, output predicate, and list of permitted operations;
2. name independent input variables and convert maximum constraints into candidate operation and space counts;
3. construct boundary and adversarial examples that expose ambiguity or an invalid assumption;
4. reject an infeasible candidate without pretending that a wall-clock rule is universal;
5. communicate the remaining feasible envelope before choosing a data structure or algorithm.

Required evidence:

- Explain and trace a complete constraint ledger from memory for an unseen prompt.
- Prove or disprove that a proposed interpretation covers the required cases, and debug one deliberately inconsistent specification.
- Derive dominant-operation, auxiliary-space, output-space, and Python-cost consequences for at least two candidate shapes.
- Complete delayed recall and an unlabeled transfer task without being given a pattern or target algorithm.

## 3. Intuition and problem shape

An algorithm problem has two layers:

1. **Specification:** which inputs are valid, which outputs are correct, and what restrictions apply.
2. **Construction:** a procedure that returns a correct output within the allowed resources.

Weak starts jump to construction. Strong starts compress the specification into a **constraint ledger**:

| Ledger line | Question | Example translation |
|---|---|---|
| Inputs | What objects arrive, in what representation? | A finite list of integers and one integer target |
| Size variables | Which quantities vary independently? | n list items; q queries if queries exist |
| Output | What exact object or predicate is required? | Boolean existence, not the pair itself |
| Semantics | What do distinct, contiguous, stable, online, or optimal mean? | Distinct positions means i is not j |
| Bounds | What are the minima and maxima? | 0 ≤ n ≤ 200,000 |
| Permissions | May the input be mutated, reordered, copied, or reread? | Input must remain unchanged |
| Resources | What time, memory, or output limits matter? | Avoid work proportional to all pairs |

The ledger is deliberately boring. That is its strength: each later idea is checked against the same facts.

### Translate verbs and quantifiers

- **Return whether** usually asks for a Boolean.
- **Return one** permits early termination once a witness is proven.
- **Return the first** requires an ordering definition.
- **Return all** introduces an output variable r and an unavoidable output cost.
- **For each query** introduces q; a cost paid once and a cost paid q times must be separated.
- **Online** means a decision is needed as input arrives and may forbid revisiting earlier items.

### Separate requirements from examples

Examples demonstrate selected instances; they do not replace the general contract. If examples contain only positive integers, negative values remain possible unless the statement rules them out. If one valid output is shown, do not infer it is the only valid output unless tie-breaking is specified.

## 4. Brute force and bottleneck

### Simplest correct baseline

For the teaching example, the most direct interpretation checks every unordered pair of distinct positions:

~~~python
def has_distinct_pair_sum(values: list[int], target: int) -> bool:
    for left in range(len(values)):
        for right in range(left + 1, len(values)):
            if values[left] + values[right] == target:
                return True
    return False
~~~

This baseline is useful because its coverage is easy to audit. It is not presented as the final method.

### Exact bottleneck

For n items, the inner comparison runs

~~~text
(n - 1) + (n - 2) + ... + 1 = n(n - 1) / 2
~~~

times in the no-witness case. At n = 200,000 that is 19,999,900,000 pair checks. The bottleneck is not “two loops”; it is explicitly enumerating every unordered pair. Early return improves some instances but not the required worst case.

## 5. Derivation and invariant

Use this derivation chain:

~~~text
maximum constraints
→ simplest correct baseline
→ exact repeated operation
→ symbolic count
→ worst-case substitution
→ reject or retain candidate family
→ required complexity envelope
→ state that could avoid repeated work
~~~

The governing **contract invariant** is:

> At every derivation step, the accepted examples, rejected examples, output predicate, permissions, and resource limits still describe the original statement.

This prevents a common false optimization: making the code faster by solving an easier problem. For example, replacing “return all pairs” with “return whether a pair exists” may reduce output and permit early return, but it violates the contract.

A candidate state is not yet a data structure. Describe information before implementation: “information from the processed prefix needed to decide whether the current item can complete a witness.” Later units decide how to represent that information.

## 6. Detailed visual trace

### Statement-to-budget trace

~~~text
T0  prose
    "Given n integer readings and target t, return whether two
     distinct positions sum to t. n ≤ 200,000. Do not mutate input."

T1  objects
    values: sequence[int]     t: int

T2  sizes
    n = len(values)           only one independent collection size

T3  output predicate
    True  iff  exists indices i,j with 0 ≤ i < j < n
               and values[i] + values[j] = t

T4  semantic edges
    [] -> False
    [4], t=8 -> False         one position cannot be reused
    [4,4], t=8 -> True        equal values at distinct positions are valid
    [-3,7], t=4 -> True       signed values remain allowed

T5  baseline work
    candidates = every i<j
    worst-case checks = n(n-1)/2

T6  feasibility conclusion
    pair enumeration conflicts with the large-n envelope
    seek a method with about one or a few n-sized passes
    any extra state must respect "do not mutate input"
~~~

#### How to read this visual

Follow T0 through T6 without skipping T3. T3 is the executable meaning of the prose. T4 tries to falsify that meaning. T5 counts the baseline's dominant operation. T6 rejects only the work shape; it does not claim that any unproved faster idea is correct.

#### Key insight

The tiny cases [4] and [4, 4] carry more semantic information than a large random example: together they separate value equality from position identity.

#### Simplification or limitation

This trace assumes exact integer arithmetic, a materialized reusable sequence, and a Boolean result. A stream, approximate answer, multiple targets, or requirement to return every witness changes the ledger.

## 7. Mechanics and state variables

| State variable | Meaning | Update rule | Why it is sufficient |
|---|---|---|---|
| n | Number of primary items | Obtain from the input contract | Scales scans and pair counts |
| q | Number of independent queries/updates | Set to 1 when no query batch exists | Separates one-time work from repeated work |
| r | Number of returned items | Derive from the produced result | Makes output-sensitive lower bounds visible |
| candidate_work | Dominant operation count | Write a formula before substituting maxima | Compares families without machine-specific seconds |
| candidate_space | Extra retained state | Count objects/references by input variable | Prevents “fast” from hiding excessive memory |
| mutation_allowed | Whether input may change | Copy the statement's rule exactly | Rejects in-place transformations when forbidden |
| ordering_required | Whether original or tie order matters | Record the specified order and tie-break | Detects invalid reordering |
| unresolved | Missing semantic facts | Remove only after a justified assumption or clarification | Prevents ambiguity from becoming silent code |

State variables describe the reasoning process. An eventual algorithm will introduce its own loop or structure invariant.

## 8. Correctness reasoning

### Translation correctness

- **Initialization:** every named input and output noun is entered in the ledger before a candidate is considered.
- **Preservation:** an assumption is added only if it is stated, logically implied, or explicitly marked for clarification.
- **Progress and termination:** each pass resolves one category—objects, semantics, limits, permissions, examples, and budget—so the finite checklist ends.
- **Completeness:** normal, minimum, maximum-shape, and adversarial examples exercise the stated predicate and its boundaries.
- **Safe exclusion:** a candidate is discarded only when a concrete input breaks correctness or a derived resource count breaks a limit.
- **Final-state argument:** when no ledger line is unresolved, candidate evaluation refers to the same input/output relation as the prompt.

### Teaching-baseline correctness

The nested loops visit each pair of indices with left < right exactly once. If they return True, those distinct positions satisfy the target equation, so the answer is sound. If a valid pair exists, it has one smaller and one larger index, so that iteration is visited and returns True; therefore the scan is complete. If no iteration matches, no valid unordered pair exists.

## 9. Complexity derivation

Always state variables before bounds:

| Candidate work shape | Dominant count | Time model | Typical pressure |
|---|---:|---:|---|
| One visit per item | n | Θ(n) | Primary input |
| Every unordered pair | n(n−1)/2 | Θ(n²) | Pair relationships |
| Full scan for every query | nq | Θ(nq) | Repeated queries |
| One build plus per-query work | P(n) + qQ(n) | Depends on P and Q | Preprocessing trade-off |
| Emit r items | at least r writes | Ω(r) | Output size |
| Graph adjacency traversal | V + E visits | Θ(V+E) in the standard model | Two independent graph dimensions |

Use the exact expression before simplifying. n(n−1)/2 explains why a pair baseline is quadratic; merely seeing nested syntax does not. A nested loop can still total linear work if its pointer advances only n times globally, and a one-line Python expression can still consume an entire input.

### Feasibility is a bound, not folklore

Do not memorize a universal “operations per second” cutoff. A judge, Python version, operation mix, input distribution, and hardware all matter. Instead:

1. compare growth families at maximum inputs;
2. identify enormous separations, such as 200,000 versus 19,999,900,000;
3. honor explicit time and memory limits;
4. benchmark only when a runtime claim is actually needed and can be reproduced.

### Space accounting

- **Input space** belongs to the caller unless the algorithm copies it.
- **Auxiliary space** is additional working state.
- **Output space** is separated when the caller requires r produced items.
- **Recursion stack** is separate even when no explicit container appears.
- “In place” is not the same as O(1) total memory; it normally describes auxiliary mutation of the supplied representation.

### Python costs to surface

- The Python tutorial documents that range produces values lazily rather than building a list; wrapping it in list changes space usage.
- A list display or comprehension constructs a new list.
- Membership has container-dependent mechanics; on a general sequence it may compare successive elements, so writing “in” does not prove constant time.
- Repeated slicing, concatenation, sorting, conversion, or copying must be counted even when each appears on one source line.

## 10. Implementations

### Generic pseudocode

~~~text
function build_constraint_ledger(statement):
    inputs      = extract objects, types, representation
    variables   = assign independent sizes
    output      = write exact predicate and tie rules
    semantics   = translate quantifiers and identity rules
    limits      = record minima, maxima, time, space
    permissions = record mutation, ordering, streaming, approximation
    examples    = create normal, boundary, adversarial cases
    unresolved  = list facts still ambiguous
    return all fields without choosing an algorithm

function assess(candidate, ledger):
    prove candidate returns ledger.output for all valid ledger.inputs
    derive dominant work from ledger.variables
    derive auxiliary, output, and stack space
    reject on one concrete correctness or resource conflict
~~~

### Idiomatic Python

This helper exposes operation counts without pretending to benchmark wall-clock time:

~~~python
def operation_ledger(n: int, q: int = 1, output_items: int = 1) -> dict[str, int]:
    if min(n, q, output_items) < 0:
        raise ValueError("sizes must be non-negative")
    return {
        "single_scan": n,
        "all_unordered_pairs": n * (n - 1) // 2,
        "scan_per_query": n * q,
        "build_once_then_one_per_query": n + q,
        "output_lower_bound": output_items,
    }
~~~

The runnable [micro-lab](practice/micro_lab.py) adds named scenarios, budget decisions, and a trace.

### Python 3.11 compatibility

The examples use syntax and standard-library behavior available in Python 3.11. The repository's canonical teaching runtime is Python 3.14, but no version-specific shortcut is needed here.

### First-principles versus standard-library choice

Write the formulas by hand first so the dominant work is inspectable. In normal code, use clear built-ins such as len, enumerate, and range when their semantics match the contract; a shorter spelling never removes the need to account for the work it performs.

## 11. Edge-case matrix

| Dimension | Minimal adversarial case | Expected behavior | Invariant risk |
|---|---|---|---|
| Empty input | [], target 0 | False for the pair predicate | Assuming at least one item |
| Singleton identity | [4], target 8 | False | Reusing one position |
| Duplicate values | [4, 4], target 8 | True | Deduplicating values too early |
| Signed values | [-3, 7], target 4 | True | Inventing a positivity constraint |
| Quantifier | Return all pairs, not any pair | Output may contain many pairs | Early return violates output |
| Tie rule | Two equally valid first results | Follow the stated ordering or flag ambiguity | Accidental iteration order |
| Mutation | Input must remain unchanged | Any reordering occurs on permitted state only | Hidden in-place sort |
| Multiple sizes | n items and q queries | Model n and q independently | Collapsing both to n |
| Output size | r can exceed n | Account for Ω(r) output work | Claiming sub-output time |
| Stream | Values cannot be reread | State must be sufficient online | Assuming random access |

## 12. Comparisons and anti-signals

| Candidate | Use when | Reject when | Evidence in the problem |
|---|---|---|---|
| Contract-first translation | Every unfamiliar or changed prompt | Never skip it; shorten only when the contract is already explicit | Inputs, output, limits, permissions |
| Direct exhaustive baseline | A simple method is needed as a correctness oracle | Its derived worst-case work violates the budget | Candidate count at maximum inputs |
| Reordering | Order is irrelevant or a copy is permitted | Original order, stability, streaming, or mutation rules forbid it | “Preserve order,” “online,” “in place” |
| Preprocessing | Many queries reuse the same stable input | Only one query exists or updates invalidate the state | Large q, repeated access, update rules |
| Extra retained state | Memory is allowed and it removes repeated work | The memory limit or stream cardinality forbids it | Explicit memory bound |
| Pattern-first guess | Only as a private hypothesis after translation | A keyword is the only evidence | Changed constraints break the familiar contract |

Anti-signals include deriving complexity from line count, treating sample values as constraints, using only average-case intuition when worst case is required, and optimizing before the output is defined.

## 13. Common bugs and debugging

| Failure | Symptom | Smallest counterexample | Correction |
|---|---|---|---|
| Value confused with position | One element pairs with itself | [4], target 8 | Write i < j in the predicate |
| Example promoted to rule | Negatives fail unexpectedly | [-3, 7], target 4 | Take domains from constraints, not samples |
| Quantifier weakened | Only one witness is returned when all are required | [1, 1, 1], target 2 | Write output cardinality and tie rules |
| Variables collapsed | Cost is reported as O(n²) for n items and q queries | n=2, q=1,000,000 | Keep n and q independent |
| Average hides worst case | Early return is called constant time | No witness exists | Analyze the required worst case |
| Hidden copy ignored | “Constant-space” code slices the entire list | values[:] | Count copied references as auxiliary space |
| Illegal reordering | Correct values but wrong original positions | [9, 1, 8] | Record mutation and order permissions |
| Contradiction ignored | Exact online duplicate detection with bounded state is promised for an unbounded domain | More distinct values than retained slots | Flag infeasibility and ask for a revised contract |

Debug the ledger before debugging code: find the first sentence, example, or derived count that no longer matches.

## 14. Practice ladder

1. Reconstruct the seven-line constraint ledger from memory.
2. Predict the [operation-budget micro-lab](practice/README.md#dsa-fnd-010-p01-predict-the-budget-trace) before running it.
3. Translate a fully specified interval prompt without choosing a pattern.
4. Find the contradiction in an exact streaming requirement.
5. Change “return any” to “return all” and introduce r.
6. Change one query to q queries and separate build from query cost.
7. Compare mutation allowed versus original order preserved.
8. Complete a mixed prompt whose familiar keyword points toward an invalid method.
9. Give a two-minute interview clarification and feasibility summary.
10. Repeat an unseen translation after the scheduled delay in [REVIEW.md](REVIEW.md).

No canonical LeetCode problem owns this unit. The initialized tasks are original specification and reasoning drills; later pattern units own platform problems.

## 15. Interview questions, traps, and follow-ups

### Recognition and approach questions

1. Before naming an algorithm, what are the exact inputs, independent size variables, and required output?
2. Which words in the statement define identity, order, contiguity, or a quantifier?
3. What is the simplest correct baseline, and what exact operation does it repeat?

### Invariant and correctness questions

1. What contract invariant must remain true while you optimize the approach?
2. How would you prove that your interpretation handles duplicates without reusing one position?
3. Which adversarial example distinguishes your interpretation from the nearest plausible alternative?

### Complexity questions

1. Why is n(n−1)/2 the relevant count here rather than simply saying “nested loops”?
2. If there are n stored items, q queries, and r reported matches, what time, auxiliary-space, output-space, and stack-space variables will you state?
3. Which Python operation in your sketch may hide a traversal or allocation, and how will you count it?

### Changed-constraint follow-ups

1. How does the contract change if the interviewer asks for every witness rather than a Boolean?
2. What changes if the input is a one-pass stream and cannot be replayed?
3. What changes if q target queries reuse the same immutable input?
4. If only approximate answers are acceptable, which previously mandatory correctness condition can be renegotiated?

### Common traps and weak-answer repairs

- **Trap:** “n is large, so I will use hashing.” This names a representation without defining the output or proving that its equality, memory, and ordering behavior fit.
- **Trap:** treating a time limit as a universal operations-per-second conversion.
- **Weak answer:** “This is O(n) because there is one loop.” Repair it by naming n, the dominant operation, the number of executions, hidden calls, auxiliary state, output, and stack.
- **Weak answer:** “The samples pass, so the interpretation is correct.” Repair it by explaining the general predicate and one boundary plus one adversarial case.

## 16. Explanation exercises

1. Explain the pair example in under two minutes without naming a final pattern.
2. Defend the distinct-position predicate using [4] and [4, 4].
3. Explain why an all-pairs baseline is correct yet infeasible at n = 200,000.
4. Recalculate the budget when one target becomes q independent targets.
5. Explain why returning r items prevents a time claim smaller than the work needed to emit r items.
6. Give the clarification question you would ask when exact output conflicts with bounded streaming memory.

## 17. Experiment decision

Decision: no runtime experiment is created for this unit. Its evidence profile does not contain X, and machine timing would encourage a false universal cutoff before formal complexity modeling. The runnable micro-lab instead counts deterministic abstract operations. Reproducible benchmarking belongs after the workload, runtime, trials, and limitations can be controlled, as developed in PY-MPR-080 and later complexity work.

## 18. Vocabulary and professional English

### Constraint

| Item | Content |
|---|---|
| Pronunciation | kuhn-STRAYNT |
| Simple English meaning | A rule or limit that narrows what is allowed |
| Hindi cue | सीमा / शर्त |
| Meaning here | A bound or semantic requirement every valid solution must respect |

Examples:

1. The room size is a physical constraint.
2. The deadline constrains the plan.
3. Privacy rules constrain data retention.
4. **Interview:** “The no-mutation constraint rules out sorting the input in place.”
5. **Engineering discussion:** “The latency constraint applies to each query, not only to preprocessing.”

### Feasible

| Item | Content |
|---|---|
| Pronunciation | FEE-zuh-buhl |
| Simple English meaning | Possible within the stated limits |
| Hindi cue | संभव / व्यावहारिक |
| Meaning here | Correct and within the derived time, space, and output envelope |

Examples:

1. The route is feasible before sunset.
2. The proposal is feasible within the budget.
3. Both designs are technically feasible.
4. **Interview:** “Pair enumeration is correct, but not feasible for the maximum n.”
5. **Engineering discussion:** “The design becomes feasible if preprocessing may be shared across queries.”

### Ambiguity

| Item | Content |
|---|---|
| Pronunciation | am-bih-GYOO-uh-tee |
| Simple English meaning | More than one reasonable interpretation |
| Hindi cue | अस्पष्टता |
| Meaning here | A missing rule that could change correctness or algorithm choice |

Examples:

1. The pronoun creates ambiguity.
2. The contract has ambiguity around refunds.
3. A tie needs a rule to remove ambiguity.
4. **Interview:** “There is ambiguity about whether equal endpoints overlap.”
5. **Engineering discussion:** “Before implementation, let us resolve the ambiguity around duplicate events.”

## 19. Python Mastery references

- [PY-BLT-040 — Lists, tuples, ranges, and sequence behaviour](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-blt-040): optional bridge for sequence representation, indexing, ranges, and copying.
- [PY-BLT-090 — Protocol-facing built-in functions and container complexity](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-blt-090): bridge for work hidden behind concise built-ins.
- [PY-MPR-070 — Algorithmic and memory complexity](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mpr-070): deeper Python-side complexity accounting.
- [PY-MPR-080 — Responsible benchmarking](https://github.com/rahulyadev/python-mastery/blob/main/CURRICULUM.md#py-mpr-080): use when an empirical performance claim is actually required.

These are supporting references, not hard prerequisites for DSA-FND-010.

## 20. Authoritative sources

- [MIT 6.006 Spring 2020, Lecture 1: Introduction](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/477c78e0af2df61fa205bcc6cb613ceb_MIT6_006S20_lec1.pdf) — defines a computational problem through inputs and correct outputs, separates correctness from efficiency, and motivates counting operations against input size.
- [MIT 6.006 Fall 2011 syllabus](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/syllabus/) — supports the communication contract of description, worked example, correctness reasoning, and complexity analysis.
- [Python 3.14 tutorial: More Control Flow Tools](https://docs.python.org/3.14/tutorial/controlflow.html#the-range-function) — documents that range is iterable and does not materialize a list of all values.
- [Python 3.14 language reference: Expressions](https://docs.python.org/3.14/reference/expressions.html#membership-test-operations) — documents membership semantics and why the container protocol must be known before assigning a cost.

All explanations, examples, exercises, and diagrams in this unit are original; the sources above were consulted for definitions and language behavior.
