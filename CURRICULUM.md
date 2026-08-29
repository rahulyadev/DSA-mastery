# DSA Mastery Curriculum

This is the canonical catalog of **125 independently trackable learning units** across **14 domains**.

- Choose a recommended sequence in [LEARNING_PATHS.md](LEARNING_PATHS.md).
- Browse symptoms and comparisons in [PATTERN_INDEX.md](PATTERN_INDEX.md).
- Problems are evidence and practice, not curriculum units. See [PROBLEM_BANK.md](PROBLEM_BANK.md).
- One dedicated Codex Worktree chat owns one initialized learning unit.
- Unit folders are created only when initialized.

## Hierarchy

```text
Domain
└── Learning unit
    ├── Concept or algorithmic pattern
    ├── Visual trace
    ├── Practice ladder
    └── Evidence artifact
```

## Stable-ID and granularity rules

1. IDs use `DSA-<DOMAIN>-<THREE-DIGIT-SEQUENCE>` with gaps of ten.
2. IDs are immutable and never silently reused.
3. One unit has one observable outcome, one chat, one progress row, one review cycle, and meaningful independent evidence.
4. A LeetCode problem never becomes a unit merely because it has a tag.
5. A concept stays a subtopic when it shares the same invariant, prerequisites, practice, and recall cycle.
6. Splits, merges, reordering, retirement, or reclassification require an explicit curriculum decision.

## Classification legend

`Class` is `Priority / Interview frequency / Practical relevance / Python relevance / Depth`.

| Dimension | Allowed values | Meaning |
|---|---|---|
| Priority | `C`, `P`, `A`, `R` | Core, Professional, Advanced, Reference |
| Interview frequency | `H`, `M`, `L` | Reasoned professional judgment: High, Medium, Low |
| Practical relevance | `H`, `M`, `L` | Usefulness beyond interviews |
| Python relevance | `H`, `M`, `L` | Importance of Python-specific behavior |
| Difficulty | `1`–`5` | Conceptual difficulty, independent of LeetCode labels |
| Depth | `D1`, `D2`, `D3`, `D4` | Practical use, formal mechanics, runtime-aware, unusually deep/source-level |
| Evidence | `E`, `T`, `I`, `P`, `D`, `X`, `(X)`, `R`, `M` | Explain, trace, implement, prove, debug, required/recommended experiment, delayed recall, mixed transfer |

Frequency labels are professional judgments, not measured global hiring statistics.

## Time-size contracts

| Size | First understanding | Hands-on practice | Rapid concept review |
|---|---:|---:|---:|
| `S` | 1–2 h | 2–4 h | 20–30 min |
| `M` | 2–4 h | 4–8 h | 30–45 min |
| `L` | 4–7 h | 8–14 h | 45–65 min |
| `XL` | 7–12 h | 14–24 h | 65–90 min |

Rapid review excludes complete labs, all variations, delayed evidence, and projects. Full mastery includes the complete unit evidence profile. External problem time, spaced reviews, mocks, and projects are calculated separately in learning paths.

## Domain totals

| Domain | Units | First understanding | Hands-on practice |
|---|---:|---:|---:|
| Problem-solving foundations | 10 | 34–61 h | 68–122 h |
| Python mechanics for DSA | 8 | 28–50 h | 56–100 h |
| Arrays, strings, and sequence patterns | 12 | 40–72 h | 80–144 h |
| Searching, ordering, and selection | 7 | 29–51 h | 58–102 h |
| Linked structures | 6 | 25–44 h | 50–88 h |
| Stacks, queues, intervals, and heaps | 10 | 44–77 h | 88–154 h |
| Recursion and backtracking | 7 | 26–46 h | 52–92 h |
| Trees and tries | 10 | 42–74 h | 84–148 h |
| Graphs and disjoint sets | 15 | 63–111 h | 126–222 h |
| Greedy algorithms | 5 | 20–35 h | 40–70 h |
| Dynamic programming | 14 | 83–143 h | 166–286 h |
| Bits, mathematics, and string algorithms | 10 | 43–76 h | 86–152 h |
| Advanced structures and techniques | 4 | 22–38 h | 44–76 h |
| Composite designs and interview synthesis | 7 | 40–69 h | 80–138 h |
| **Total** | **125** | **539–947 h** | **1078–1894 h** |

## Completeness matrix

| Required capability | Canonical owner(s) |
|---|---|
| Universal problem-solving flow | DSA-FND-010, DSA-FND-020, DSA-FND-030, DSA-FND-100 |
| Constraints, brute force, bottlenecks, invariants, correctness, termination | DSA-FND-010–DSA-FND-030 |
| Asymptotic, amortized, recursive, output-sensitive, graph/grid/DP complexity | DSA-FND-040–DSA-FND-070 |
| Testing, debugging wrong answers and time limits | DSA-FND-080, DSA-FND-090, DSA-PY-080 |
| Python list, tuple, str, dict, set, Counter, defaultdict, deque, heapq, bisect, sorting | DSA-PY-010–DSA-PY-040 |
| Copying, mutation, recursion limits, integers, generators, Python performance traps | DSA-PY-050–DSA-PY-080 |
| Linear scans, hashing, two pointers, sliding windows | DSA-SEQ-010–DSA-SEQ-060 |
| Prefix, suffix, difference, running optimum, index placement, matrices | DSA-SEQ-070–DSA-SEQ-120 |
| Binary search, boundary search, answer search, merge/quick/counting sorts | DSA-ORD-010–DSA-ORD-070 |
| Linked-list sentinels, reversal, cycles, merging, intersections, sublists | DSA-LNK-010–DSA-LNK-060 |
| Stacks, queues, monotonic structures, intervals, sweeps, heaps, streaming | DSA-SQH-010–DSA-SQH-100 |
| Recursion, subsets, permutations, pruning, grid backtracking | DSA-REC-010–DSA-REC-070 |
| Tree DFS/BFS, paths, subtree aggregation, BST, LCA, serialization, tries, tree DP | DSA-TRE-010–DSA-TRE-100 |
| Graph BFS/DFS, components, multi-source, bipartite, cycles, topo, DSU | DSA-GRA-010–DSA-GRA-090 |
| Dijkstra, Bellman-Ford, Floyd-Warshall, MST, 0-1 BFS, low-link DFS, and SCC | DSA-GRA-100–DSA-GRA-150 |
| Greedy recognition, proofs, intervals, sorting, greedy-vs-DP | DSA-GRD-010–DSA-GRD-050 |
| DP state modeling, memo/tabulation, 1D, grid, knapsack, sequence/string, interval, state-machine, tree, bitmask, digit | DSA-DP-010–DSA-DP-140 |
| Bits, XOR, masks, GCD, sieve, modular arithmetic, combinatorics, rolling hash, KMP, Z/suffix reference | DSA-BMS-010–DSA-BMS-100 |
| Fenwick, segment tree, sparse table, randomized and streaming algorithms | DSA-ADV-010–DSA-ADV-040 |
| LRU, min stack, median stream, time-key storage, autocomplete, scheduling, mixed mocks | DSA-SYN-010–DSA-SYN-070 |

## Canonical learning units

## Problem-solving foundations

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-fnd-010"></a>`DSA-FND-010` — **Computational problem solving and constraint translation** | Translate a problem statement and constraints into explicit inputs, outputs, candidate state, and feasible complexity budgets. | None | `C/H/H/H/D1` | 1 | `Foundations`, `Interview` | `M` | 2–4 h | 4–8 h | `E+T+P+D+R+M` |
| <a id="dsa-fnd-020"></a>`DSA-FND-020` — **Brute-force enumeration and bottleneck discovery** | Construct the simplest correct exhaustive solution, identify repeated work, and name the exact bottleneck that an optimization must remove. | `DSA-FND-010` | `C/H/H/H/D2` | 2 | `Foundations`, `Algorithms`, `Interview` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-fnd-030"></a>`DSA-FND-030` — **Invariants, correctness, and termination** | State useful loop or state invariants and use them to justify safety, progress, completeness, and termination at interview depth. | `DSA-FND-010`, `DSA-FND-020` | `C/H/H/H/D2` | 3 | `Foundations`, `Proof`, `Interview` | `L` | 4–7 h | 8–14 h | `E+T+P+D+R+M` |
| <a id="dsa-fnd-040"></a>`DSA-FND-040` — **Asymptotic notation and input-variable modeling** | Derive O, Theta, and Omega bounds using explicit input variables rather than guessing from code shape. | `DSA-FND-010` | `C/H/H/H/D2` | 2 | `Foundations`, `Complexity` | `L` | 4–7 h | 8–14 h | `E+T+P+D+R+M` |
| <a id="dsa-fnd-050"></a>`DSA-FND-050` — **Amortized, aggregate, output-sensitive, and query analysis** | Explain aggregate and amortized costs, output-sensitive bounds, preprocessing/query trade-offs, and honest in-place space claims. | `DSA-FND-040` | `C/H/H/H/D2` | 3 | `Foundations`, `Complexity` | `L` | 4–7 h | 8–14 h | `E+T+P+D+R+M` |
| <a id="dsa-fnd-060"></a>`DSA-FND-060` — **Recursion, call stacks, and recursive complexity** | Trace recursive calls, derive base cases and progress, and account for recurrence cost and recursion-stack space. | `DSA-FND-030`, `DSA-FND-040` | `C/H/H/H/D2` | 3 | `Foundations`, `Recursion`, `Complexity` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-fnd-070"></a>`DSA-FND-070` — **Interview mathematics: logarithms, sums, counting, and probability** | Use the small set of logarithmic, summation, counting, combinatorial, and probability tools that recur in interview algorithms. | `DSA-FND-040` | `P/M/M/L/D2` | 3 | `Foundations`, `Mathematics` | `L` | 4–7 h | 8–14 h | `E+T+P+R+M` |
| <a id="dsa-fnd-080"></a>`DSA-FND-080` — **Testing algorithms with examples, oracles, and properties** | Design deterministic cases, brute-force oracles, properties, and differential tests that expose algorithmic defects. | `DSA-FND-020`, `DSA-FND-030` | `C/H/H/H/D2` | 3 | `Foundations`, `Testing` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+X+R+M` |
| <a id="dsa-fnd-090"></a>`DSA-FND-090` — **Debugging wrong answers, time limits, and memory failures** | Classify and diagnose wrong answers, boundary faults, invariant breaks, time-limit failures, and memory-limit failures systematically. | `DSA-FND-030`, `DSA-FND-040`, `DSA-FND-080` | `C/H/H/H/D2` | 2 | `Foundations`, `Debugging`, `Interview` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-fnd-100"></a>`DSA-FND-100` — **Interview communication, dry-runs, and changing constraints** | Explain a solution naturally while deriving it, dry-run accurately, and adapt when an interviewer changes constraints. | `DSA-FND-010`, `DSA-FND-030`, `DSA-FND-040` | `C/H/H/H/D2` | 2 | `Foundations`, `Interview`, `Communication` | `M` | 2–4 h | 4–8 h | `E+T+P+D+R+M` |

## Python mechanics for DSA

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-py-010"></a>`DSA-PY-010` — **Python sequence mechanics for DSA** | Use list, tuple, str, range, indexing, slicing, iteration, and construction with accurate time and space costs. | `DSA-FND-040` | `C/H/H/H/D2` | 2 | `Python`, `Sequences`, `Complexity` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-py-020"></a>`DSA-PY-020` — **Hashing, equality, dictionaries, and sets** | Choose and use dict and set keys correctly while explaining equality, hashability, average-case behavior, and collision caveats. | `DSA-PY-010` | `C/H/H/H/D3` | 3 | `Python`, `Hashing`, `Complexity` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-py-030"></a>`DSA-PY-030` — **Counter, defaultdict, deque, and queue-safe Python** | Use Counter, defaultdict, and deque idiomatically and avoid incorrect or slow queue operations such as list.pop(0). | `DSA-PY-010`, `DSA-PY-020` | `C/H/H/H/D2` | 2 | `Python`, `Standard library`, `Queues` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-py-040"></a>`DSA-PY-040` — **heapq, bisect, sorting, and comparable entries** | Use heapq, bisect, stable sorting, key functions, tie breakers, and comparable heap entries safely. | `DSA-PY-010` | `C/H/H/H/D2` | 3 | `Python`, `Standard library`, `Ordering` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-py-050"></a>`DSA-PY-050` — **Mutation, copying, aliasing, and string construction** | Predict mutation and aliasing effects, choose shallow or deep copies deliberately, and construct strings without hidden quadratic work. | `DSA-PY-010` | `C/H/H/H/D2` | 3 | `Python`, `State`, `Complexity` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-py-060"></a>`DSA-PY-060` — **Recursion limits, integers, and Python performance traps** | Account for Python recursion limits, arbitrary-precision integer costs, object overhead, comprehensions, slicing, and allocation traps. | `DSA-FND-060`, `DSA-PY-010` | `P/M/H/H/D3` | 3 | `Python`, `Runtime`, `Complexity` | `L` | 4–7 h | 8–14 h | `E+T+I+D+(X)+R+M` |
| <a id="dsa-py-070"></a>`DSA-PY-070` — **Iterators, generators, and streaming inputs** | Use iterators and generators to process streaming data while reasoning about one-pass state, exhaustion, and memory. | `DSA-PY-010` | `P/M/H/H/D2` | 3 | `Python`, `Streaming`, `Sequences` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-py-080"></a>`DSA-PY-080` — **pytest, Hypothesis, brute-force oracles, and differential testing** | Build repeatable algorithm tests with pytest and Hypothesis and compare optimized implementations against trusted small-input oracles. | `DSA-FND-080`, `DSA-PY-050` | `P/M/H/H/D2` | 3 | `Python`, `Testing`, `Tooling` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+X+R+M` |

## Arrays, strings, and sequence patterns

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-seq-010"></a>`DSA-SEQ-010` — **Linear scans, aggregation, and minimal state** | Design one-pass scans that maintain only the state needed for counts, extrema, decisions, or output construction. | `DSA-FND-020`, `DSA-FND-030`, `DSA-PY-010` | `C/H/H/H/D2` | 2 | `Arrays`, `Strings`, `Patterns` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-020"></a>`DSA-SEQ-020` — **Frequency maps, membership, and complement lookup** | Replace repeated membership or counting work with a hash-based state whose invariant is explicit. | `DSA-SEQ-010`, `DSA-PY-020` | `C/H/H/H/D2` | 2 | `Arrays`, `Strings`, `Hashing`, `Patterns` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-030"></a>`DSA-SEQ-030` — **In-place read/write pointers and stable compaction** | Mutate a sequence in place using explicit read, write, and partition invariants without losing unread data. | `DSA-SEQ-010`, `DSA-PY-050` | `C/H/H/H/D2` | 3 | `Arrays`, `Two pointers`, `Mutation` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-040"></a>`DSA-SEQ-040` — **Opposite-direction two pointers** | Recognize ordered or monotonic pair-search structure and prove why moving one pointer cannot discard a valid optimum. | `DSA-SEQ-010`, `DSA-FND-030` | `C/H/H/H/D2` | 3 | `Arrays`, `Strings`, `Two pointers` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-050"></a>`DSA-SEQ-050` — **Fixed-size sliding windows** | Maintain an exact fixed-width aggregate incrementally and derive its linear complexity from element entry and exit counts. | `DSA-SEQ-010`, `DSA-FND-030` | `C/H/H/H/D2` | 2 | `Arrays`, `Strings`, `Sliding window` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-060"></a>`DSA-SEQ-060` — **Variable-size sliding windows** | Grow and shrink a window under a monotonic validity rule while stating when the technique is invalid. | `DSA-SEQ-020`, `DSA-SEQ-050` | `C/H/H/H/D2` | 4 | `Arrays`, `Strings`, `Sliding window` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-070"></a>`DSA-SEQ-070` — **Prefix sums and prefix-state transforms** | Turn repeated range or subarray computation into prefix-state lookup, including hashable prefix-state variants. | `DSA-SEQ-010`, `DSA-SEQ-020` | `C/H/H/H/D2` | 3 | `Arrays`, `Prefix sums`, `Hashing` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-080"></a>`DSA-SEQ-080` — **Suffix aggregates and bidirectional precomputation** | Combine left and right summaries without recomputing ranges or accidentally using forbidden output storage. | `DSA-SEQ-070` | `C/H/H/H/D2` | 3 | `Arrays`, `Prefix sums`, `Precomputation` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-090"></a>`DSA-SEQ-090` — **Difference arrays and range updates** | Represent many range updates as boundary events and reconstruct final values with a prefix pass. | `DSA-SEQ-070` | `P/M/H/H/D2` | 3 | `Arrays`, `Difference arrays`, `Sweep line` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-100"></a>`DSA-SEQ-100` — **Running optima and Kadane-style reasoning** | Derive local-versus-global optimum recurrences for contiguous sequences and explain when reset is safe. | `DSA-SEQ-010`, `DSA-FND-030` | `C/H/H/H/D2` | 3 | `Arrays`, `Dynamic programming`, `Greedy` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-110"></a>`DSA-SEQ-110` — **Index placement and cyclic-position techniques** | Use value-to-index constraints to place elements, detect cycles, and avoid duplicate or infinite-swap errors. | `DSA-SEQ-030` | `P/M/H/H/D2` | 4 | `Arrays`, `Index placement`, `Cycles` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-seq-120"></a>`DSA-SEQ-120` — **Matrices, grids, rotation, and boundary simulation** | Traverse and mutate matrices using explicit row, column, layer, direction, and boundary state. | `DSA-SEQ-010`, `DSA-SEQ-030` | `C/H/H/H/D2` | 3 | `Matrices`, `Simulation`, `Arrays` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |

## Searching, ordering, and selection

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-ord-010"></a>`DSA-ORD-010` — **Binary search fundamentals and loop invariants** | Implement exact-value binary search with a deliberate interval convention and prove progress and termination. | `DSA-FND-030`, `DSA-SEQ-010` | `C/H/H/H/D2` | 2 | `Binary search`, `Ordering`, `Proof` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-ord-020"></a>`DSA-ORD-020` — **Lower bound, upper bound, and first/last true** | Search boundaries using monotonic predicates and explain closed versus half-open interval variants. | `DSA-ORD-010` | `C/H/H/H/D2` | 4 | `Binary search`, `Ordering`, `Boundaries` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-ord-030"></a>`DSA-ORD-030` — **Rotated and partially ordered search** | Recover enough local order to discard half of a rotated or piecewise-sorted search space safely. | `DSA-ORD-010` | `C/H/H/H/D2` | 4 | `Binary search`, `Arrays` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-ord-040"></a>`DSA-ORD-040` — **Binary search on a monotonic answer space** | Convert an optimization problem into a monotonic feasibility predicate and search the smallest or largest valid answer. | `DSA-ORD-020`, `DSA-FND-040` | `C/H/H/H/D2` | 4 | `Binary search`, `Optimization`, `Greedy` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-ord-050"></a>`DSA-ORD-050` — **Merge sort, stable merging, and inversion counting** | Implement merge sort and exploit merge structure for counting cross-half relationships. | `DSA-FND-060`, `DSA-SEQ-010` | `C/M/H/H/D2` | 3 | `Sorting`, `Divide and conquer` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-ord-060"></a>`DSA-ORD-060` — **Partitioning, quicksort concepts, and quickselect** | Use partition invariants for selection and explain quicksort and quickselect average and worst cases. | `DSA-SEQ-030`, `DSA-FND-050` | `C/H/H/H/D2` | 4 | `Sorting`, `Selection`, `Randomized` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-ord-070"></a>`DSA-ORD-070` — **Counting, bucket, and constraint-driven ordering** | Choose non-comparison ordering only when the value domain and memory constraints justify it. | `DSA-FND-040`, `DSA-SEQ-020` | `P/M/H/H/D2` | 3 | `Sorting`, `Counting`, `Buckets` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |

## Linked structures

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-lnk-010"></a>`DSA-LNK-010` — **Linked-list representation, sentinels, and ownership** | Draw node ownership and references, use sentinels, and preserve every still-needed node during mutation. | `DSA-FND-030`, `DSA-PY-050` | `C/H/H/H/D2` | 2 | `Linked lists`, `Pointers`, `State` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-lnk-020"></a>`DSA-LNK-020` — **Reversal and safe pointer rewiring** | Reverse links while preserving the unreversed suffix and state the pointer invariant at each step. | `DSA-LNK-010` | `C/H/H/H/D2` | 2 | `Linked lists`, `Pointers` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-lnk-030"></a>`DSA-LNK-030` — **Fast/slow pointers and cycle detection** | Use relative pointer speeds for middle, cycle, entry, and distance reasoning without losing termination guarantees. | `DSA-LNK-010` | `C/H/H/H/D2` | 4 | `Linked lists`, `Two pointers`, `Cycles` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-lnk-040"></a>`DSA-LNK-040` — **Merging, intersection, and reference preservation** | Merge or align linked structures while distinguishing node identity from equal values. | `DSA-LNK-010` | `C/H/H/H/D2` | 2 | `Linked lists`, `Merging`, `Identity` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-lnk-050"></a>`DSA-LNK-050` — **Sublist reversal, reordering, and k-group transformations** | Decompose complex rewiring into boundaries, reversible segments, and reconnection steps. | `DSA-LNK-020`, `DSA-LNK-040` | `C/H/H/H/D2` | 4 | `Linked lists`, `Pointers` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-lnk-060"></a>`DSA-LNK-060` — **Linked composite structures and cache design** | Combine linked order with hash-based lookup while maintaining cross-structure consistency. | `DSA-LNK-020`, `DSA-PY-020` | `P/H/H/H/D2` | 4 | `Linked lists`, `Hashing`, `Composite design` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |

## Stacks, queues, intervals, and heaps

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-sqh-010"></a>`DSA-SQH-010` — **Stack, queue, and deque invariants** | Select LIFO, FIFO, or double-ended state and implement operations with correct complexity. | `DSA-PY-030`, `DSA-FND-030` | `C/H/H/H/D2` | 2 | `Stacks`, `Queues`, `Deque` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-sqh-020"></a>`DSA-SQH-020` — **Matching, nesting, and expression evaluation** | Use a stack to represent unresolved structure and evaluate tokens with explicit operand order. | `DSA-SQH-010` | `C/H/H/H/D2` | 2 | `Stacks`, `Parsing` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-sqh-030"></a>`DSA-SQH-030` — **Monotonic stacks and next-element reasoning** | Maintain unresolved candidates in monotonic order and prove each element is pushed and popped at most once. | `DSA-SQH-010`, `DSA-FND-030` | `C/H/H/H/D2` | 4 | `Stacks`, `Monotonic`, `Arrays` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-sqh-040"></a>`DSA-SQH-040` — **Monotonic deques and window extrema** | Maintain only undominated window candidates with expiry and dominance invariants. | `DSA-SQH-010`, `DSA-SEQ-050` | `C/H/H/H/D2` | 4 | `Deque`, `Monotonic`, `Sliding window` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-sqh-050"></a>`DSA-SQH-050` — **Interval sorting, merging, and coverage** | Normalize interval conventions, sort by a useful key, and maintain a coverage invariant while merging or inserting. | `DSA-FND-030`, `DSA-PY-040` | `C/H/H/H/D2` | 2 | `Intervals`, `Sorting` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-sqh-060"></a>`DSA-SQH-060` — **Sweep-line events and scheduling conflicts** | Convert intervals into ordered events and choose tie rules that preserve the intended boundary semantics. | `DSA-SQH-050` | `P/M/H/H/D2` | 4 | `Intervals`, `Sweep line`, `Scheduling` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-sqh-070"></a>`DSA-SQH-070` — **Heap and priority-queue fundamentals** | Use heap order, push/pop/replace operations, and custom entries while accounting for heap construction and tie safety. | `DSA-PY-040`, `DSA-FND-050` | `C/H/H/H/D2` | 2 | `Heaps`, `Priority queues` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-sqh-080"></a>`DSA-SQH-080` — **Top-K and streaming selection** | Choose heap size and orientation based on which candidates must survive as input streams past. | `DSA-SQH-070` | `C/H/H/H/D2` | 2 | `Heaps`, `Streaming`, `Selection` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-sqh-090"></a>`DSA-SQH-090` — **K-way merge and frontier heaps** | Represent only the next candidate from each sorted source and maintain a heap-backed frontier. | `DSA-SQH-070`, `DSA-LNK-040` | `C/H/H/H/D2` | 4 | `Heaps`, `Merging`, `Streaming` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-sqh-100"></a>`DSA-SQH-100` — **Two-heaps median, lazy deletion, and dynamic priorities** | Maintain partition and balance invariants across two heaps and handle stale entries without corrupting logical state. | `DSA-SQH-070`, `DSA-PY-020` | `P/H/H/H/D3` | 5 | `Heaps`, `Streaming`, `State` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |

## Recursion and backtracking

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-rec-010"></a>`DSA-REC-010` — **Recursive decomposition and decision trees** | Define recursive state, choices, base cases, and progress, and visualize the resulting decision tree. | `DSA-FND-060` | `C/H/H/H/D2` | 2 | `Recursion`, `Backtracking` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-rec-020"></a>`DSA-REC-020` — **Subsets and combinations** | Generate choose/skip or bounded-choice solution spaces without duplicates or missing candidates. | `DSA-REC-010` | `C/H/H/H/D2` | 2 | `Backtracking`, `Combinatorics` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-rec-030"></a>`DSA-REC-030` — **Permutations and duplicate handling** | Track used positions or swap boundaries and eliminate duplicate branches deliberately. | `DSA-REC-010`, `DSA-REC-020` | `C/H/H/H/D2` | 4 | `Backtracking`, `Combinatorics` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-rec-040"></a>`DSA-REC-040` — **Constraint propagation and pruning** | Prune only when a partial state cannot lead to a valid or better solution and justify branch elimination. | `DSA-REC-010`, `DSA-FND-030` | `C/H/H/H/D2` | 4 | `Backtracking`, `Pruning`, `Proof` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-rec-050"></a>`DSA-REC-050` — **Grid and path backtracking** | Manage visited state, restoration, boundaries, and path-local decisions in grid search. | `DSA-REC-040`, `DSA-SEQ-120` | `C/H/H/H/D2` | 4 | `Backtracking`, `Grids` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-rec-060"></a>`DSA-REC-060` — **Branch ordering and backtracking complexity** | Estimate recursion-tree cost and choose branch order that exposes failure or promising candidates earlier. | `DSA-REC-040`, `DSA-FND-040` | `P/M/H/H/D2` | 4 | `Backtracking`, `Complexity` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-rec-070"></a>`DSA-REC-070` — **Backtracking versus dynamic programming** | Decide whether path-specific choices require search or repeated states permit memoized dynamic programming. | `DSA-REC-040` | `C/H/H/H/D2` | 4 | `Backtracking`, `Dynamic programming`, `Comparison` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |

## Trees and tries

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-tre-010"></a>`DSA-TRE-010` — **Binary-tree representation and traversal invariants** | Represent trees, distinguish node identity from value, and state traversal and null-child conventions. | `DSA-FND-060`, `DSA-PY-050` | `C/H/H/H/D2` | 2 | `Trees`, `State` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-tre-020"></a>`DSA-TRE-020` — **Depth-first traversal: recursive and iterative** | Implement preorder, inorder, and postorder DFS recursively and iteratively while preserving visit order. | `DSA-TRE-010`, `DSA-SQH-010` | `C/H/H/H/D2` | 2 | `Trees`, `DFS`, `Stacks` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-tre-030"></a>`DSA-TRE-030` — **Breadth-first and level-order traversal** | Process trees by frontier layers and preserve level boundaries without using slow Python queues. | `DSA-TRE-010`, `DSA-SQH-010` | `C/H/H/H/D2` | 2 | `Trees`, `BFS`, `Queues` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-tre-040"></a>`DSA-TRE-040` — **Path state and root-to-leaf reasoning** | Separate path-local state from global or subtree state and restore mutable path state correctly. | `DSA-TRE-020`, `DSA-FND-030` | `C/H/H/H/D2` | 3 | `Trees`, `DFS`, `Paths` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-tre-050"></a>`DSA-TRE-050` — **Subtree aggregation and divide-and-conquer** | Define what each subtree returns and combine child summaries into local and global answers. | `DSA-TRE-020`, `DSA-FND-030` | `C/H/H/H/D2` | 4 | `Trees`, `Divide and conquer` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-tre-060"></a>`DSA-TRE-060` — **Binary-search-tree invariants, search, update, and validation** | Use ordering bounds rather than only parent comparisons and explain average versus degenerate costs. | `DSA-TRE-020`, `DSA-ORD-010` | `C/H/H/H/D2` | 3 | `Trees`, `BST`, `Ordering` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-tre-070"></a>`DSA-TRE-070` — **Lowest common ancestor and ancestry reasoning** | Derive LCA algorithms from ancestry, search structure, and postorder return semantics. | `DSA-TRE-040`, `DSA-TRE-050` | `C/H/H/H/D2` | 4 | `Trees`, `Ancestry` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-tre-080"></a>`DSA-TRE-080` — **Tree construction and serialization concepts** | Reconstruct or encode trees while preserving boundaries, uniqueness assumptions, and null structure. | `DSA-TRE-020`, `DSA-PY-070` | `C/H/H/H/D2` | 4 | `Trees`, `Serialization`, `Divide and conquer` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-tre-090"></a>`DSA-TRE-090` — **Tries and prefix search** | Represent prefix state, implement insert/search/prefix operations, and compare tries with hash-based indexes. | `DSA-PY-020`, `DSA-TRE-010` | `C/H/H/H/D2` | 3 | `Tries`, `Strings`, `Indexes` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-tre-100"></a>`DSA-TRE-100` — **Tree dynamic programming and recursion-depth safety** | Model include/exclude or multi-state subtree decisions and choose iterative alternatives when depth is unsafe. | `DSA-TRE-050`, `DSA-REC-070`, `DSA-PY-060` | `C/H/H/H/D2` | 5 | `Trees`, `Dynamic programming`, `Runtime` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |

## Graphs and disjoint sets

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-gra-010"></a>`DSA-GRA-010` — **Graph representations and state-space modeling** | Choose adjacency lists, matrices, edge lists, or implicit state transitions and define what a vertex means. | `DSA-PY-020`, `DSA-PY-030`, `DSA-FND-030` | `C/H/H/H/D2` | 2 | `Graphs`, `Modeling` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-020"></a>`DSA-GRA-020` — **Breadth-first search** | Use a FIFO frontier to discover shortest unweighted distance layers and mark visited state at the correct time. | `DSA-GRA-010`, `DSA-SQH-010` | `C/H/H/H/D2` | 2 | `Graphs`, `BFS`, `Shortest paths` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-030"></a>`DSA-GRA-030` — **Depth-first search** | Traverse graph reachability recursively or iteratively while handling cycles and recursion-depth risk. | `DSA-GRA-010`, `DSA-TRE-020` | `C/H/H/H/D2` | 2 | `Graphs`, `DFS` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-040"></a>`DSA-GRA-040` — **Connected components and grid-as-graph reasoning** | Count or label components and translate grid adjacency into graph traversal without duplicating traversal logic. | `DSA-GRA-020`, `DSA-GRA-030`, `DSA-SEQ-120` | `C/H/H/H/D2` | 2 | `Graphs`, `Components`, `Grids` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-050"></a>`DSA-GRA-050` — **Multi-source BFS** | Initialize a frontier with all simultaneous sources and interpret each BFS layer as elapsed distance or time. | `DSA-GRA-020` | `C/H/H/H/D2` | 3 | `Graphs`, `BFS`, `Grids` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-060"></a>`DSA-GRA-060` — **Bipartite testing** | Assign two-color constraints component by component and detect odd-cycle contradictions. | `DSA-GRA-020`, `DSA-GRA-030` | `C/H/H/H/D2` | 3 | `Graphs`, `BFS`, `DFS` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-070"></a>`DSA-GRA-070` — **Cycle detection in directed and undirected graphs** | Distinguish parent edges, active recursion paths, and globally completed nodes when detecting cycles. | `DSA-GRA-030` | `C/H/H/H/D2` | 4 | `Graphs`, `Cycles`, `DFS` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-080"></a>`DSA-GRA-080` — **Topological sorting and dependency order** | Produce or reject a dependency order using indegrees or DFS finishing state and explain uniqueness limitations. | `DSA-GRA-070` | `C/H/H/H/D2` | 4 | `Graphs`, `DAG`, `Topological sort` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-090"></a>`DSA-GRA-090` — **Disjoint-set union** | Maintain component representatives with path compression and union by rank or size, including amortized analysis. | `DSA-FND-050`, `DSA-GRA-010` | `C/H/H/H/D2` | 4 | `Graphs`, `Disjoint set`, `Amortized` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-100"></a>`DSA-GRA-100` — **Shortest-path algorithm selection** | Select BFS, 0-1 BFS, Dijkstra, Bellman-Ford, or all-pairs methods from edge weights, graph size, and query needs. | `DSA-GRA-020`, `DSA-FND-040` | `C/H/H/H/D2` | 4 | `Graphs`, `Shortest paths`, `Comparison` | `L` | 4–7 h | 8–14 h | `E+T+P+D+R+M` |
| <a id="dsa-gra-110"></a>`DSA-GRA-110` — **Dijkstra and non-negative weighted paths** | Maintain tentative distances and a priority frontier while safely ignoring stale heap entries. | `DSA-GRA-100`, `DSA-SQH-070` | `C/H/H/H/D2` | 4 | `Graphs`, `Shortest paths`, `Heaps` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-120"></a>`DSA-GRA-120` — **Bellman-Ford and all-pairs shortest paths** | Use repeated relaxation for negative edges and dynamic-programming closure for dense all-pairs queries. | `DSA-GRA-100` | `A/L/M/M/D3` | 5 | `Graphs`, `Shortest paths`, `Dynamic programming` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-130"></a>`DSA-GRA-130` — **Minimum spanning trees** | Build a minimum-cost connecting structure with Kruskal or Prim and justify the safe-edge choice. | `DSA-GRA-090`, `DSA-SQH-070` | `P/M/H/H/D2` | 4 | `Graphs`, `MST`, `Greedy` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-140"></a>`DSA-GRA-140` — **Zero-one BFS** | Exploit binary edge weights with a deque and explain why front versus back placement preserves distance order. | `DSA-GRA-100`, `DSA-SQH-010` | `A/L/M/H/D2` | 4 | `Graphs`, `Shortest paths`, `Deque` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-gra-150"></a>`DSA-GRA-150` — **Low-link DFS: bridges, articulation points, and strongly connected components** | Compute discovery and low-link values to find bridges and articulation points in undirected graphs, explain SCC algorithms for directed graphs, and distinguish the invariants used by each. | `DSA-GRA-030`, `DSA-GRA-080` | `A/L/M/M/D2` | 5 | `Graphs`, `Low-link DFS`, `Bridges`, `Articulation points`, `SCC` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |

> **`DSA-GRA-150` note contract:** The initialized note must separately trace discovery times and low-link values; derive undirected bridge and articulation-point tests; explain directed SCC algorithms and condensation graphs; and state why undirected bridge detection is not the same algorithm as directed SCC decomposition.

## Greedy algorithms

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-grd-010"></a>`DSA-GRD-010` — **Greedy-choice recognition and counterexamples** | Recognize candidate greedy structure and actively search for counterexamples before trusting a local rule. | `DSA-FND-020`, `DSA-FND-030` | `C/H/H/H/D2` | 2 | `Greedy`, `Proof` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-grd-020"></a>`DSA-GRD-020` — **Exchange arguments and stays-ahead proofs** | Justify a greedy decision using exchange or stays-ahead reasoning instead of intuition alone. | `DSA-GRD-010` | `C/H/H/H/D2` | 4 | `Greedy`, `Proof` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-grd-030"></a>`DSA-GRD-030` — **Interval scheduling and resource allocation** | Choose interval orderings that maximize compatibility or minimize resource conflicts and prove the choice. | `DSA-GRD-020`, `DSA-SQH-050` | `C/H/H/H/D2` | 4 | `Greedy`, `Intervals`, `Scheduling` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-grd-040"></a>`DSA-GRD-040` — **Sorting-based greedy and local choices** | Use sorting to expose a safe local choice and distinguish it from merely trying a sorted heuristic. | `DSA-GRD-020`, `DSA-PY-040` | `C/H/H/H/D2` | 3 | `Greedy`, `Sorting` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-grd-050"></a>`DSA-GRD-050` — **Greedy versus dynamic programming** | Explain why a greedy summary is sufficient or why future-dependent state requires dynamic programming. | `DSA-GRD-010`, `DSA-REC-070` | `C/H/H/H/D2` | 4 | `Greedy`, `Dynamic programming`, `Comparison` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |

## Dynamic programming

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-dp-010"></a>`DSA-DP-010` — **Dynamic-programming recognition and state modeling** | Identify repeated states and optimal substructure, define a minimal state, and write the meaning before the recurrence. | `DSA-FND-020`, `DSA-FND-030`, `DSA-FND-060` | `C/H/H/H/D2` | 4 | `Dynamic programming`, `Modeling` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-020"></a>`DSA-DP-020` — **Memoization, tabulation, and evaluation order** | Convert a recurrence between top-down and bottom-up forms and choose an order that satisfies dependencies. | `DSA-DP-010` | `C/H/H/H/D2` | 4 | `Dynamic programming`, `Recursion`, `Iteration` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-030"></a>`DSA-DP-030` — **One-dimensional sequence DP** | Model prefix or index state for local-choice sequence problems and derive rolling-state optimization. | `DSA-DP-020` | `C/H/H/H/D2` | 2 | `Dynamic programming`, `Sequences` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-040"></a>`DSA-DP-040` — **Grid and path DP** | Define cell state, predecessor transitions, boundaries, obstacles, and row-wise space optimization. | `DSA-DP-020`, `DSA-SEQ-120` | `C/H/H/H/D2` | 3 | `Dynamic programming`, `Grids` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-050"></a>`DSA-DP-050` — **Knapsack and subset-sum families** | Derive capacity and choice states, distinguish 0/1 from repeatable choices, and order loops correctly. | `DSA-DP-020` | `C/H/H/H/D2` | 4 | `Dynamic programming`, `Knapsack` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-060"></a>`DSA-DP-060` — **Coin change and unbounded-choice DP** | Distinguish minimum, count, combination, and permutation objectives in unbounded-choice state transitions. | `DSA-DP-050` | `C/H/H/H/D2` | 4 | `Dynamic programming`, `Knapsack` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-070"></a>`DSA-DP-070` — **Subsequence and sequence-alignment DP** | Model two-prefix states and derive keep, skip, match, or edit transitions. | `DSA-DP-020` | `C/H/H/H/D2` | 4 | `Dynamic programming`, `Sequences`, `Strings` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-080"></a>`DSA-DP-080` — **Longest increasing subsequence** | Derive quadratic DP and the ordered-tail optimization without confusing tail values with a reconstructed solution. | `DSA-DP-030`, `DSA-ORD-020` | `C/H/H/H/D2` | 5 | `Dynamic programming`, `Binary search`, `Sequences` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-090"></a>`DSA-DP-090` — **String dynamic programming** | Model segmentation, palindrome, and decoding states while separating substring and subsequence semantics. | `DSA-DP-020`, `DSA-PY-010` | `C/H/H/H/D2` | 4 | `Dynamic programming`, `Strings` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-100"></a>`DSA-DP-100` — **Interval dynamic programming** | Choose interval boundaries, split points, and evaluation order for problems whose final operation joins subintervals. | `DSA-DP-020` | `A/M/H/H/D2` | 5 | `Dynamic programming`, `Intervals` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-110"></a>`DSA-DP-110` — **State-machine dynamic programming** | Represent legal modes and transitions explicitly for stock, cooldown, transaction, and finite-state problems. | `DSA-DP-030` | `C/H/H/H/D2` | 4 | `Dynamic programming`, `State machine` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-120"></a>`DSA-DP-120` — **Tree dynamic programming** | Define multi-state subtree returns and combine child choices without double-counting or violating adjacency constraints. | `DSA-TRE-100`, `DSA-DP-020` | `C/H/H/H/D2` | 5 | `Dynamic programming`, `Trees` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-130"></a>`DSA-DP-130` — **Bitmask dynamic programming** | Encode small selected sets as bits and reason about state-count times transition-cost. | `DSA-DP-020` | `A/L/L/H/D2` | 5 | `Dynamic programming`, `Bitmasks` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-dp-140"></a>`DSA-DP-140` — **Digit DP and advanced state compression** | Model digit prefixes, tight bounds, leading zeros, and compact state only at advanced/reference depth. | `DSA-DP-020`, `DSA-FND-070` | `R/L/L/M/D3` | 5 | `Dynamic programming`, `Digits`, `Reference` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+(X)+R+M` |

## Bits, mathematics, and string algorithms

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-bms-010"></a>`DSA-BMS-010` — **Bit operations and masks** | Use shifts, masks, set/clear/test operations, signedness awareness, and bit-count identities safely. | `DSA-FND-070` | `C/H/M/H/D2` | 3 | `Bits`, `Mathematics` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-bms-020"></a>`DSA-BMS-020` — **XOR invariants and parity reasoning** | Use cancellation and parity invariants while recognizing when XOR loses information needed by the problem. | `DSA-BMS-010` | `C/H/H/H/D2` | 3 | `Bits`, `Invariants` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-bms-030"></a>`DSA-BMS-030` — **Subset enumeration with bitmasks** | Map positions to bits, enumerate subsets, and derive O(2^n) state costs honestly. | `DSA-BMS-010`, `DSA-FND-070` | `P/M/H/H/D2` | 4 | `Bits`, `Combinatorics` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-bms-040"></a>`DSA-BMS-040` — **GCD, divisibility, and Euclidean reasoning** | Apply Euclid's algorithm and divisibility invariants to simplify number and periodicity problems. | `DSA-FND-070` | `P/M/M/H/D2` | 3 | `Mathematics`, `Number theory` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-bms-050"></a>`DSA-BMS-050` — **Primes and sieve techniques** | Generate and test primes within constraint-driven bounds and derive sieve complexity. | `DSA-FND-040`, `DSA-FND-070` | `P/M/L/H/D2` | 3 | `Mathematics`, `Number theory` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-bms-060"></a>`DSA-BMS-060` — **Modular arithmetic and fixed-width translation** | Use modular identities and translate Python integer solutions safely to fixed-width languages when relevant. | `DSA-FND-070`, `DSA-PY-060` | `P/M/M/H/D2` | 3 | `Mathematics`, `Python` | `M` | 2–4 h | 4–8 h | `E+T+I+P+D+R+M` |
| <a id="dsa-bms-070"></a>`DSA-BMS-070` — **Combinatorics and interview probability** | Count arrangements or outcomes and use probability only where it changes an interview algorithm or randomized design. | `DSA-FND-070` | `A/L/L/L/D2` | 4 | `Mathematics`, `Combinatorics`, `Probability` | `L` | 4–7 h | 8–14 h | `E+T+P+R+M` |
| <a id="dsa-bms-080"></a>`DSA-BMS-080` — **Rolling hash and collision reasoning** | Maintain substring hashes, account for collisions, and choose deterministic alternatives when correctness cannot tolerate them. | `DSA-PY-020`, `DSA-BMS-060` | `A/L/M/H/D2` | 5 | `Strings`, `Hashing` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-bms-090"></a>`DSA-BMS-090` — **KMP and prefix-function string matching** | Derive fallback transitions from proper prefix/suffix structure and prove linear scanning. | `DSA-FND-030`, `DSA-PY-010` | `A/L/M/H/D2` | 5 | `Strings`, `String matching` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-bms-100"></a>`DSA-BMS-100` — **Z algorithm and advanced suffix structures** | Understand Z-box reuse and place suffix arrays or trees at reference depth without bloating the interview core. | `DSA-BMS-090` | `R/L/L/M/D2` | 5 | `Strings`, `String matching`, `Reference` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+(X)+R+M` |

## Advanced structures and techniques

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-adv-010"></a>`DSA-ADV-010` — **Fenwick trees** | Support point updates and prefix queries with binary-index structure and derive the low-bit traversal. | `DSA-SEQ-070`, `DSA-BMS-010` | `A/L/M/H/D2` | 5 | `Advanced structures`, `Range queries` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-adv-020"></a>`DSA-ADV-020` — **Segment trees and lazy propagation concepts** | Represent interval aggregates, combine nodes, update ranges, and compare complexity with simpler alternatives. | `DSA-ADV-010`, `DSA-FND-060` | `A/L/M/H/D2` | 5 | `Advanced structures`, `Range queries`, `Trees` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-adv-030"></a>`DSA-ADV-030` — **Sparse tables and static range-query trade-offs** | Precompute idempotent range answers and compare static-query structures with Fenwick and segment trees. | `DSA-FND-050`, `DSA-BMS-040` | `R/L/L/H/D2` | 5 | `Advanced structures`, `Range queries`, `Reference` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-adv-040"></a>`DSA-ADV-040` — **Reservoir sampling, randomized selection, and streaming algorithms** | Maintain unbiased samples or randomized partitions and state probabilistic guarantees and limitations. | `DSA-FND-070`, `DSA-PY-070`, `DSA-ORD-060` | `A/L/M/H/D2` | 4 | `Advanced techniques`, `Randomized`, `Streaming` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+X+R+M` |

## Composite designs and interview synthesis

| ID | Learning outcome and included scope | Prerequisite IDs | Class | Difficulty | Scope | Size | First understanding | Hands-on practice | Evidence |
|---|---|---|---|---:|---|:---:|---:|---:|---|
| <a id="dsa-syn-010"></a>`DSA-SYN-010` — **LRU cache composite design** | Combine hash lookup and linked recency while maintaining capacity, uniqueness, and cross-structure invariants. | `DSA-LNK-060` | `P/H/H/H/D2` | 2 | `Composite design`, `Caches`, `Interview` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-syn-020"></a>`DSA-SYN-020` — **Min stack and randomized-set API invariants** | Design composite data structures whose auxiliary state remains synchronized across every public operation. | `DSA-SQH-010`, `DSA-PY-020`, `DSA-SEQ-030` | `P/H/H/H/D2` | 4 | `Composite design`, `Stacks`, `Hashing` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-syn-030"></a>`DSA-SYN-030` — **Median stream and time-based key-value storage** | Choose partitioned heaps or sorted per-key histories and defend update/query trade-offs. | `DSA-SQH-100`, `DSA-ORD-020` | `P/H/H/H/D2` | 5 | `Composite design`, `Streaming`, `Indexes` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-syn-040"></a>`DSA-SYN-040` — **Autocomplete and in-memory indexes** | Combine tries, ranking state, and bounded candidate selection while separating algorithmic from production concerns. | `DSA-TRE-090`, `DSA-SQH-080` | `P/M/H/H/D2` | 4 | `Composite design`, `Tries`, `Indexes` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-syn-050"></a>`DSA-SYN-050` — **Task scheduling and composite constraint modeling** | Combine ordering, heaps, queues, counters, and greedy reasoning without forcing one pattern prematurely. | `DSA-GRD-040`, `DSA-SQH-070`, `DSA-SEQ-020` | `C/H/H/H/D2` | 4 | `Composite design`, `Scheduling`, `Greedy` | `L` | 4–7 h | 8–14 h | `E+T+I+P+D+R+M` |
| <a id="dsa-syn-060"></a>`DSA-SYN-060` — **Mixed unlabeled problem solving** | Select and derive approaches from constraints and bottlenecks when no pattern label or target complexity is supplied. | `DSA-FND-100`, `DSA-GRD-050`, `DSA-GRA-100`, `DSA-DP-010` | `C/H/H/H/D2` | 5 | `Synthesis`, `Interview`, `Mixed practice` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
| <a id="dsa-syn-070"></a>`DSA-SYN-070` — **Mock interviews, readiness gates, and error analysis** | Demonstrate repeatable mixed-problem performance and use evidence categories to target the next revision cycle. | `DSA-SYN-060`, `DSA-FND-090` | `P/H/H/H/D2` | 5 | `Synthesis`, `Interview`, `Assessment` | `XL` | 7–12 h | 14–24 h | `E+T+I+P+D+R+M` |
