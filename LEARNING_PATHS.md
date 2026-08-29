# DSA Mastery Learning Paths

[Back to the curriculum](CURRICULUM.md)

## Choose a path

[1. Absolute DSA foundations](#absolute-dsa-foundations) | [2. Emergency interview revision](#emergency-interview-revision) | [3. 7-day interview refresher](#seven-day-interview-refresher) | [4. 14-day interview preparation](#fourteen-day-interview-preparation) | [5. 30-day core interview foundation](#thirty-day-core-interview-foundation) | [6. 90-day comprehensive interview preparation](#ninety-day-comprehensive-interview) | [7. Complete DSA mastery](#complete-dsa-mastery) | [8. Arrays and strings repair path](#arrays-strings-repair) | [9. Trees and graphs repair path](#trees-graphs-repair) | [10. Dynamic-programming repair path](#dynamic-programming-repair) | [11. Senior Python/backend coding-interview path](#senior-python-backend-interview) | [12. Mixed mocks and final revision](#mixed-mocks-final-revision)

Paths are recommendations, not gates. Any unit may be initialized earlier. Codex warns about hard prerequisites, gives the smallest correct bridge, and continues unless proceeding would be materially misleading.

## Two study-depth contracts

### Rapid interview pass

A rapid unit pass includes:

- `Physical Notebook Core`;
- one tiny worked trace or micro-drill inside the unit-time estimate;
- recognition and anti-recognition cues;
- one commonly confused comparison;
- complexity derivation;
- interview traps and focused recall questions.

A **complete first attempt at a selected LeetCode problem is not included in unit time**. Every selected problem is counted exactly once under the separate problem-attempt component. The rapid unit pass does not require every implementation, lab, proof variation, experiment, delayed review, or transfer item.

### Full mastery pass

A full unit pass includes the complete note, first-principles implementation, correctness reasoning, all required labs, labeled and mixed practice, variations, debugging, delayed recall, verbal explanation, and unseen transfer evidence.

Neither contract guarantees employment or a particular interview result.

<a id="absolute-dsa-foundations"></a>
## 1. Absolute DSA foundations

<!-- PATH_META {"id":"absolute-dsa-foundations","title":"Absolute DSA foundations","unit_count":40,"problem_count":15,"concept_minutes":[1685,2445],"problem_minutes":345,"activities":{"Recall and visual reconstruction":[300,420],"Mixed review and postmortem":[180,240],"Checkpoint":[90,120]},"activity_minutes":[570,780],"rapid_total_minutes":[2600,3570],"full_unit_hours":[435,774],"assumed_or_bridge_prerequisites":[],"project_count":2} -->

**Who it is for:** Rahul or any experienced programmer rebuilding DSA from first principles before pattern-heavy practice.

**Time assumption:** 60–120 minutes per day; the calculated rapid pass is 43 h 20 min–59 h 30 min and normally spans several weeks.

**Prerequisite policy:** No DSA knowledge is assumed beyond basic Python syntax. Python gaps receive a bridge or a Python Mastery link.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 28 h 5 min–40 h 45 min |
| Complete first attempts for 15 selected problems | 5 h 45 min |
| Recall and visual reconstruction | 5 h–7 h |
| Mixed review and postmortem | 3 h–4 h |
| Checkpoint | 1 h 30 min–2 h |
| **Required activities subtotal** | **9 h 30 min–13 h** |
| **Rapid path total** | **43 h 20 min–59 h 30 min** |
| **Full mastery of included units** | **435–774 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (40 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-FND-080 — Testing algorithms with examples, oracles, and properties](CURRICULUM.md#dsa-fnd-080)
8. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
9. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
10. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
11. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
12. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
13. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
14. [DSA-PY-080 — pytest, Hypothesis, brute-force oracles, and differential testing](CURRICULUM.md#dsa-py-080)
15. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
16. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
17. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
18. [DSA-SEQ-040 — Opposite-direction two pointers](CURRICULUM.md#dsa-seq-040)
19. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
20. [DSA-SEQ-100 — Running optima and Kadane-style reasoning](CURRICULUM.md#dsa-seq-100)
21. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
22. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
23. [DSA-LNK-010 — Linked-list representation, sentinels, and ownership](CURRICULUM.md#dsa-lnk-010)
24. [DSA-LNK-020 — Reversal and safe pointer rewiring](CURRICULUM.md#dsa-lnk-020)
25. [DSA-LNK-040 — Merging, intersection, and reference preservation](CURRICULUM.md#dsa-lnk-040)
26. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
27. [DSA-SQH-020 — Matching, nesting, and expression evaluation](CURRICULUM.md#dsa-sqh-020)
28. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
29. [DSA-SQH-080 — Top-K and streaming selection](CURRICULUM.md#dsa-sqh-080)
30. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
31. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
32. [DSA-TRE-030 — Breadth-first and level-order traversal](CURRICULUM.md#dsa-tre-030)
33. [DSA-TRE-050 — Subtree aggregation and divide-and-conquer](CURRICULUM.md#dsa-tre-050)
34. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
35. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
36. [DSA-GRA-030 — Depth-first search](CURRICULUM.md#dsa-gra-030)
37. [DSA-GRA-040 — Connected components and grid-as-graph reasoning](CURRICULUM.md#dsa-gra-040)
38. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
39. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
40. [DSA-DP-030 — One-dimensional sequence DP](CURRICULUM.md#dsa-dp-030)

### Selected problem attempts (15)

1. [LC 217 — Contains Duplicate](PROBLEM_BANK.md#lc-0217) — Easy, 20 min
2. [LC 121 — Best Time to Buy and Sell Stock](PROBLEM_BANK.md#lc-0121) — Easy, 20 min
3. [LC 125 — Valid Palindrome](PROBLEM_BANK.md#lc-0125) — Easy, 20 min
4. [LC 1 — Two Sum](PROBLEM_BANK.md#lc-0001) — Easy, 20 min
5. [LC 704 — Binary Search](PROBLEM_BANK.md#lc-0704) — Easy, 20 min
6. [LC 206 — Reverse Linked List](PROBLEM_BANK.md#lc-0206) — Easy, 20 min
7. [LC 21 — Merge Two Sorted Lists](PROBLEM_BANK.md#lc-0021) — Easy, 20 min
8. [LC 20 — Valid Parentheses](PROBLEM_BANK.md#lc-0020) — Easy, 20 min
9. [LC 703 — Kth Largest Element in a Stream](PROBLEM_BANK.md#lc-0703) — Easy, 20 min
10. [LC 226 — Invert Binary Tree](PROBLEM_BANK.md#lc-0226) — Easy, 20 min
11. [LC 104 — Maximum Depth of Binary Tree](PROBLEM_BANK.md#lc-0104) — Easy, 20 min
12. [LC 102 — Binary Tree Level Order Traversal](PROBLEM_BANK.md#lc-0102) — Medium, 35 min
13. [LC 200 — Number of Islands](PROBLEM_BANK.md#lc-0200) — Medium, 35 min
14. [LC 133 — Clone Graph](PROBLEM_BANK.md#lc-0133) — Medium, 35 min
15. [LC 70 — Climbing Stairs](PROBLEM_BANK.md#lc-0070) — Easy, 20 min

### Milestone callouts

- [DSA-PRJ-010 — Core data-structure invariant laboratory](PROJECTS.md#dsa-prj-010)
- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)

### Intentionally deferred

Advanced graphs, DP families, string matching, range-query structures, and timed mocks.


<a id="emergency-interview-revision"></a>
## 2. Emergency interview revision

<!-- PATH_META {"id":"emergency-interview-revision","title":"Emergency interview revision","unit_count":35,"problem_count":10,"concept_minutes":[1535,2215],"problem_minutes":290,"activities":{"Closed-book recall":[60,60],"Comparison drill and postmortem":[45,60],"Mock framing and feedback beyond coding time":[45,45],"Checkpoint and error log":[30,45]},"activity_minutes":[180,210],"rapid_total_minutes":[2005,2715],"full_unit_hours":[408,723],"assumed_or_bridge_prerequisites":[],"project_count":1} -->

**Who it is for:** A learner with prior exposure who needs a compact refresher before an imminent interview.

**Time assumption:** Approximately four to six full-time days; budget 33 h 25 min–45 h 15 min. Prior exposure is required.

**Prerequisite policy:** Assumed prior exposure. Every omitted hard prerequisite requires the smallest correct bridge; this path is not a beginner transformation.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 25 h 35 min–36 h 55 min |
| Complete first attempts for 10 selected problems | 4 h 50 min |
| Closed-book recall | 1 h |
| Comparison drill and postmortem | 45 min–1 h |
| Mock framing and feedback beyond coding time | 45 min |
| Checkpoint and error log | 30 min–45 min |
| **Required activities subtotal** | **3 h–3 h 30 min** |
| **Rapid path total** | **33 h 25 min–45 h 15 min** |
| **Full mastery of included units** | **408–723 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (35 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
8. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
9. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
10. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
11. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
12. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
13. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
14. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
15. [DSA-SEQ-040 — Opposite-direction two pointers](CURRICULUM.md#dsa-seq-040)
16. [DSA-SEQ-050 — Fixed-size sliding windows](CURRICULUM.md#dsa-seq-050)
17. [DSA-SEQ-060 — Variable-size sliding windows](CURRICULUM.md#dsa-seq-060)
18. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
19. [DSA-SEQ-100 — Running optima and Kadane-style reasoning](CURRICULUM.md#dsa-seq-100)
20. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
21. [DSA-ORD-020 — Lower bound, upper bound, and first/last true](CURRICULUM.md#dsa-ord-020)
22. [DSA-ORD-040 — Binary search on a monotonic answer space](CURRICULUM.md#dsa-ord-040)
23. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
24. [DSA-SQH-030 — Monotonic stacks and next-element reasoning](CURRICULUM.md#dsa-sqh-030)
25. [DSA-SQH-050 — Interval sorting, merging, and coverage](CURRICULUM.md#dsa-sqh-050)
26. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
27. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
28. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
29. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
30. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
31. [DSA-GRA-100 — Shortest-path algorithm selection](CURRICULUM.md#dsa-gra-100)
32. [DSA-GRA-110 — Dijkstra and non-negative weighted paths](CURRICULUM.md#dsa-gra-110)
33. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
34. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
35. [DSA-DP-030 — One-dimensional sequence DP](CURRICULUM.md#dsa-dp-030)

### Selected problem attempts (10)

1. [LC 1 — Two Sum](PROBLEM_BANK.md#lc-0001) — Easy, 20 min
2. [LC 121 — Best Time to Buy and Sell Stock](PROBLEM_BANK.md#lc-0121) — Easy, 20 min
3. [LC 3 — Longest Substring Without Repeating Characters](PROBLEM_BANK.md#lc-0003) — Medium, 35 min
4. [LC 560 — Subarray Sum Equals K](PROBLEM_BANK.md#lc-0560) — Medium, 35 min
5. [LC 704 — Binary Search](PROBLEM_BANK.md#lc-0704) — Easy, 20 min
6. [LC 875 — Koko Eating Bananas](PROBLEM_BANK.md#lc-0875) — Medium, 35 min
7. [LC 739 — Daily Temperatures](PROBLEM_BANK.md#lc-0739) — Medium, 35 min
8. [LC 56 — Merge Intervals](PROBLEM_BANK.md#lc-0056) — Medium, 35 min
9. [LC 743 — Network Delay Time](PROBLEM_BANK.md#lc-0743) — Medium, 35 min
10. [LC 70 — Climbing Stairs](PROBLEM_BANK.md#lc-0070) — Easy, 20 min

### Milestone callouts

- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)

### Intentionally deferred

Full labs, most linked-list variations, advanced graphs, most DP families, advanced math/string algorithms, and delayed retention evidence.


<a id="seven-day-interview-refresher"></a>
## 3. 7-day interview refresher

<!-- PATH_META {"id":"seven-day-interview-refresher","title":"7-day interview refresher","unit_count":60,"problem_count":28,"concept_minutes":[2655,3830],"problem_minutes":845,"activities":{"Daily recall":[140,175],"Comparison and postmortem sessions":[120,180],"Mock framing and feedback beyond coding time":[90,90],"Checkpoint and error log":[60,90]},"activity_minutes":[410,535],"rapid_total_minutes":[3910,5210],"full_unit_hours":[708,1251],"assumed_or_bridge_prerequisites":[],"project_count":2} -->

**Who it is for:** An experienced programmer refreshing the most common interview structures and patterns.

**Time assumption:** 7 days at approximately 9 h 19 min–12 h 25 min per day for the calculated rapid route.

**Prerequisite policy:** Basic programming and prior DSA exposure are assumed; missing specialized prerequisites receive bridges.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 44 h 15 min–63 h 50 min |
| Complete first attempts for 28 selected problems | 14 h 5 min |
| Daily recall | 2 h 20 min–2 h 55 min |
| Comparison and postmortem sessions | 2 h–3 h |
| Mock framing and feedback beyond coding time | 1 h 30 min |
| Checkpoint and error log | 1 h–1 h 30 min |
| **Required activities subtotal** | **6 h 50 min–8 h 55 min** |
| **Rapid path total** | **65 h 10 min–86 h 50 min** |
| **Full mastery of included units** | **708–1251 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (60 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
8. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
9. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
10. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
11. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
12. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
13. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
14. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
15. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
16. [DSA-SEQ-040 — Opposite-direction two pointers](CURRICULUM.md#dsa-seq-040)
17. [DSA-SEQ-050 — Fixed-size sliding windows](CURRICULUM.md#dsa-seq-050)
18. [DSA-SEQ-060 — Variable-size sliding windows](CURRICULUM.md#dsa-seq-060)
19. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
20. [DSA-SEQ-080 — Suffix aggregates and bidirectional precomputation](CURRICULUM.md#dsa-seq-080)
21. [DSA-SEQ-100 — Running optima and Kadane-style reasoning](CURRICULUM.md#dsa-seq-100)
22. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
23. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
24. [DSA-ORD-020 — Lower bound, upper bound, and first/last true](CURRICULUM.md#dsa-ord-020)
25. [DSA-ORD-040 — Binary search on a monotonic answer space](CURRICULUM.md#dsa-ord-040)
26. [DSA-LNK-010 — Linked-list representation, sentinels, and ownership](CURRICULUM.md#dsa-lnk-010)
27. [DSA-LNK-020 — Reversal and safe pointer rewiring](CURRICULUM.md#dsa-lnk-020)
28. [DSA-LNK-030 — Fast/slow pointers and cycle detection](CURRICULUM.md#dsa-lnk-030)
29. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
30. [DSA-SQH-020 — Matching, nesting, and expression evaluation](CURRICULUM.md#dsa-sqh-020)
31. [DSA-SQH-030 — Monotonic stacks and next-element reasoning](CURRICULUM.md#dsa-sqh-030)
32. [DSA-SQH-050 — Interval sorting, merging, and coverage](CURRICULUM.md#dsa-sqh-050)
33. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
34. [DSA-SQH-080 — Top-K and streaming selection](CURRICULUM.md#dsa-sqh-080)
35. [DSA-REC-010 — Recursive decomposition and decision trees](CURRICULUM.md#dsa-rec-010)
36. [DSA-REC-020 — Subsets and combinations](CURRICULUM.md#dsa-rec-020)
37. [DSA-REC-040 — Constraint propagation and pruning](CURRICULUM.md#dsa-rec-040)
38. [DSA-REC-070 — Backtracking versus dynamic programming](CURRICULUM.md#dsa-rec-070)
39. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
40. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
41. [DSA-TRE-030 — Breadth-first and level-order traversal](CURRICULUM.md#dsa-tre-030)
42. [DSA-TRE-060 — Binary-search-tree invariants, search, update, and validation](CURRICULUM.md#dsa-tre-060)
43. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
44. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
45. [DSA-GRA-030 — Depth-first search](CURRICULUM.md#dsa-gra-030)
46. [DSA-GRA-040 — Connected components and grid-as-graph reasoning](CURRICULUM.md#dsa-gra-040)
47. [DSA-GRA-050 — Multi-source BFS](CURRICULUM.md#dsa-gra-050)
48. [DSA-GRA-070 — Cycle detection in directed and undirected graphs](CURRICULUM.md#dsa-gra-070)
49. [DSA-GRA-080 — Topological sorting and dependency order](CURRICULUM.md#dsa-gra-080)
50. [DSA-GRA-100 — Shortest-path algorithm selection](CURRICULUM.md#dsa-gra-100)
51. [DSA-GRA-110 — Dijkstra and non-negative weighted paths](CURRICULUM.md#dsa-gra-110)
52. [DSA-GRD-010 — Greedy-choice recognition and counterexamples](CURRICULUM.md#dsa-grd-010)
53. [DSA-GRD-020 — Exchange arguments and stays-ahead proofs](CURRICULUM.md#dsa-grd-020)
54. [DSA-GRD-030 — Interval scheduling and resource allocation](CURRICULUM.md#dsa-grd-030)
55. [DSA-GRD-050 — Greedy versus dynamic programming](CURRICULUM.md#dsa-grd-050)
56. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
57. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
58. [DSA-DP-030 — One-dimensional sequence DP](CURRICULUM.md#dsa-dp-030)
59. [DSA-DP-050 — Knapsack and subset-sum families](CURRICULUM.md#dsa-dp-050)
60. [DSA-SYN-060 — Mixed unlabeled problem solving](CURRICULUM.md#dsa-syn-060)

### Selected problem attempts (28)

1. [LC 1 — Two Sum](PROBLEM_BANK.md#lc-0001) — Easy, 20 min
2. [LC 121 — Best Time to Buy and Sell Stock](PROBLEM_BANK.md#lc-0121) — Easy, 20 min
3. [LC 238 — Product of Array Except Self](PROBLEM_BANK.md#lc-0238) — Medium, 35 min
4. [LC 125 — Valid Palindrome](PROBLEM_BANK.md#lc-0125) — Easy, 20 min
5. [LC 167 — Two Sum II - Input Array Is Sorted](PROBLEM_BANK.md#lc-0167) — Medium, 35 min
6. [LC 3 — Longest Substring Without Repeating Characters](PROBLEM_BANK.md#lc-0003) — Medium, 35 min
7. [LC 560 — Subarray Sum Equals K](PROBLEM_BANK.md#lc-0560) — Medium, 35 min
8. [LC 704 — Binary Search](PROBLEM_BANK.md#lc-0704) — Easy, 20 min
9. [LC 34 — Find First and Last Position of Element in Sorted Array](PROBLEM_BANK.md#lc-0034) — Medium, 35 min
10. [LC 875 — Koko Eating Bananas](PROBLEM_BANK.md#lc-0875) — Medium, 35 min
11. [LC 206 — Reverse Linked List](PROBLEM_BANK.md#lc-0206) — Easy, 20 min
12. [LC 141 — Linked List Cycle](PROBLEM_BANK.md#lc-0141) — Easy, 20 min
13. [LC 20 — Valid Parentheses](PROBLEM_BANK.md#lc-0020) — Easy, 20 min
14. [LC 739 — Daily Temperatures](PROBLEM_BANK.md#lc-0739) — Medium, 35 min
15. [LC 56 — Merge Intervals](PROBLEM_BANK.md#lc-0056) — Medium, 35 min
16. [LC 347 — Top K Frequent Elements](PROBLEM_BANK.md#lc-0347) — Medium, 35 min
17. [LC 78 — Subsets](PROBLEM_BANK.md#lc-0078) — Medium, 35 min
18. [LC 39 — Combination Sum](PROBLEM_BANK.md#lc-0039) — Medium, 35 min
19. [LC 226 — Invert Binary Tree](PROBLEM_BANK.md#lc-0226) — Easy, 20 min
20. [LC 102 — Binary Tree Level Order Traversal](PROBLEM_BANK.md#lc-0102) — Medium, 35 min
21. [LC 98 — Validate Binary Search Tree](PROBLEM_BANK.md#lc-0098) — Medium, 35 min
22. [LC 200 — Number of Islands](PROBLEM_BANK.md#lc-0200) — Medium, 35 min
23. [LC 994 — Rotting Oranges](PROBLEM_BANK.md#lc-0994) — Medium, 35 min
24. [LC 207 — Course Schedule](PROBLEM_BANK.md#lc-0207) — Medium, 35 min
25. [LC 55 — Jump Game](PROBLEM_BANK.md#lc-0055) — Medium, 35 min
26. [LC 435 — Non-overlapping Intervals](PROBLEM_BANK.md#lc-0435) — Medium, 35 min
27. [LC 70 — Climbing Stairs](PROBLEM_BANK.md#lc-0070) — Easy, 20 min
28. [LC 198 — House Robber](PROBLEM_BANK.md#lc-0198) — Medium, 35 min

### Milestone callouts

- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)
- [DSA-PRJ-030 — Array and string pattern visualizer](PROJECTS.md#dsa-prj-030)

### Intentionally deferred

Rare graph algorithms, advanced DP, string matching, and range-query structures.


<a id="fourteen-day-interview-preparation"></a>
## 4. 14-day interview preparation

<!-- PATH_META {"id":"fourteen-day-interview-preparation","title":"14-day interview preparation","unit_count":79,"problem_count":50,"concept_minutes":[3540,5100],"problem_minutes":1570,"activities":{"Daily recall":[280,350],"Comparison and postmortem sessions":[240,360],"Mock framing and feedback beyond coding time":[135,135],"Checkpoint and error log":[90,120]},"activity_minutes":[745,965],"rapid_total_minutes":[5855,7635],"full_unit_hours":[951,1677],"assumed_or_bridge_prerequisites":[],"project_count":3} -->

**Who it is for:** A learner who needs broad interview coverage with derivation, practice, recall, and two mocks.

**Time assumption:** 14 days at approximately 6 h 59 min–9 h 6 min per day for the calculated rapid route.

**Prerequisite policy:** Basic Python is assumed. All included unit prerequisites are present; any external Python gaps use PYTHON_REFERENCES.md.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 59 h–85 h |
| Complete first attempts for 50 selected problems | 26 h 10 min |
| Daily recall | 4 h 40 min–5 h 50 min |
| Comparison and postmortem sessions | 4 h–6 h |
| Mock framing and feedback beyond coding time | 2 h 15 min |
| Checkpoint and error log | 1 h 30 min–2 h |
| **Required activities subtotal** | **12 h 25 min–16 h 5 min** |
| **Rapid path total** | **97 h 35 min–127 h 15 min** |
| **Full mastery of included units** | **951–1677 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (79 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-FND-070 — Interview mathematics: logarithms, sums, counting, and probability](CURRICULUM.md#dsa-fnd-070)
8. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
9. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
10. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
11. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
12. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
13. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
14. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
15. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
16. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
17. [DSA-SEQ-040 — Opposite-direction two pointers](CURRICULUM.md#dsa-seq-040)
18. [DSA-SEQ-050 — Fixed-size sliding windows](CURRICULUM.md#dsa-seq-050)
19. [DSA-SEQ-060 — Variable-size sliding windows](CURRICULUM.md#dsa-seq-060)
20. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
21. [DSA-SEQ-080 — Suffix aggregates and bidirectional precomputation](CURRICULUM.md#dsa-seq-080)
22. [DSA-SEQ-100 — Running optima and Kadane-style reasoning](CURRICULUM.md#dsa-seq-100)
23. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
24. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
25. [DSA-ORD-020 — Lower bound, upper bound, and first/last true](CURRICULUM.md#dsa-ord-020)
26. [DSA-ORD-030 — Rotated and partially ordered search](CURRICULUM.md#dsa-ord-030)
27. [DSA-ORD-040 — Binary search on a monotonic answer space](CURRICULUM.md#dsa-ord-040)
28. [DSA-ORD-060 — Partitioning, quicksort concepts, and quickselect](CURRICULUM.md#dsa-ord-060)
29. [DSA-LNK-010 — Linked-list representation, sentinels, and ownership](CURRICULUM.md#dsa-lnk-010)
30. [DSA-LNK-020 — Reversal and safe pointer rewiring](CURRICULUM.md#dsa-lnk-020)
31. [DSA-LNK-030 — Fast/slow pointers and cycle detection](CURRICULUM.md#dsa-lnk-030)
32. [DSA-LNK-040 — Merging, intersection, and reference preservation](CURRICULUM.md#dsa-lnk-040)
33. [DSA-LNK-050 — Sublist reversal, reordering, and k-group transformations](CURRICULUM.md#dsa-lnk-050)
34. [DSA-LNK-060 — Linked composite structures and cache design](CURRICULUM.md#dsa-lnk-060)
35. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
36. [DSA-SQH-020 — Matching, nesting, and expression evaluation](CURRICULUM.md#dsa-sqh-020)
37. [DSA-SQH-030 — Monotonic stacks and next-element reasoning](CURRICULUM.md#dsa-sqh-030)
38. [DSA-SQH-050 — Interval sorting, merging, and coverage](CURRICULUM.md#dsa-sqh-050)
39. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
40. [DSA-SQH-080 — Top-K and streaming selection](CURRICULUM.md#dsa-sqh-080)
41. [DSA-SQH-090 — K-way merge and frontier heaps](CURRICULUM.md#dsa-sqh-090)
42. [DSA-REC-010 — Recursive decomposition and decision trees](CURRICULUM.md#dsa-rec-010)
43. [DSA-REC-020 — Subsets and combinations](CURRICULUM.md#dsa-rec-020)
44. [DSA-REC-030 — Permutations and duplicate handling](CURRICULUM.md#dsa-rec-030)
45. [DSA-REC-040 — Constraint propagation and pruning](CURRICULUM.md#dsa-rec-040)
46. [DSA-REC-050 — Grid and path backtracking](CURRICULUM.md#dsa-rec-050)
47. [DSA-REC-070 — Backtracking versus dynamic programming](CURRICULUM.md#dsa-rec-070)
48. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
49. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
50. [DSA-TRE-030 — Breadth-first and level-order traversal](CURRICULUM.md#dsa-tre-030)
51. [DSA-TRE-040 — Path state and root-to-leaf reasoning](CURRICULUM.md#dsa-tre-040)
52. [DSA-TRE-050 — Subtree aggregation and divide-and-conquer](CURRICULUM.md#dsa-tre-050)
53. [DSA-TRE-060 — Binary-search-tree invariants, search, update, and validation](CURRICULUM.md#dsa-tre-060)
54. [DSA-TRE-070 — Lowest common ancestor and ancestry reasoning](CURRICULUM.md#dsa-tre-070)
55. [DSA-TRE-090 — Tries and prefix search](CURRICULUM.md#dsa-tre-090)
56. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
57. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
58. [DSA-GRA-030 — Depth-first search](CURRICULUM.md#dsa-gra-030)
59. [DSA-GRA-040 — Connected components and grid-as-graph reasoning](CURRICULUM.md#dsa-gra-040)
60. [DSA-GRA-050 — Multi-source BFS](CURRICULUM.md#dsa-gra-050)
61. [DSA-GRA-070 — Cycle detection in directed and undirected graphs](CURRICULUM.md#dsa-gra-070)
62. [DSA-GRA-080 — Topological sorting and dependency order](CURRICULUM.md#dsa-gra-080)
63. [DSA-GRA-090 — Disjoint-set union](CURRICULUM.md#dsa-gra-090)
64. [DSA-GRA-100 — Shortest-path algorithm selection](CURRICULUM.md#dsa-gra-100)
65. [DSA-GRA-110 — Dijkstra and non-negative weighted paths](CURRICULUM.md#dsa-gra-110)
66. [DSA-GRA-130 — Minimum spanning trees](CURRICULUM.md#dsa-gra-130)
67. [DSA-GRD-010 — Greedy-choice recognition and counterexamples](CURRICULUM.md#dsa-grd-010)
68. [DSA-GRD-020 — Exchange arguments and stays-ahead proofs](CURRICULUM.md#dsa-grd-020)
69. [DSA-GRD-040 — Sorting-based greedy and local choices](CURRICULUM.md#dsa-grd-040)
70. [DSA-GRD-050 — Greedy versus dynamic programming](CURRICULUM.md#dsa-grd-050)
71. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
72. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
73. [DSA-DP-030 — One-dimensional sequence DP](CURRICULUM.md#dsa-dp-030)
74. [DSA-DP-080 — Longest increasing subsequence](CURRICULUM.md#dsa-dp-080)
75. [DSA-DP-090 — String dynamic programming](CURRICULUM.md#dsa-dp-090)
76. [DSA-BMS-010 — Bit operations and masks](CURRICULUM.md#dsa-bms-010)
77. [DSA-BMS-020 — XOR invariants and parity reasoning](CURRICULUM.md#dsa-bms-020)
78. [DSA-SYN-010 — LRU cache composite design](CURRICULUM.md#dsa-syn-010)
79. [DSA-SYN-060 — Mixed unlabeled problem solving](CURRICULUM.md#dsa-syn-060)

### Selected problem attempts (50)

1. [LC 1 — Two Sum](PROBLEM_BANK.md#lc-0001) — Easy, 20 min
2. [LC 217 — Contains Duplicate](PROBLEM_BANK.md#lc-0217) — Easy, 20 min
3. [LC 121 — Best Time to Buy and Sell Stock](PROBLEM_BANK.md#lc-0121) — Easy, 20 min
4. [LC 238 — Product of Array Except Self](PROBLEM_BANK.md#lc-0238) — Medium, 35 min
5. [LC 53 — Maximum Subarray](PROBLEM_BANK.md#lc-0053) — Medium, 35 min
6. [LC 125 — Valid Palindrome](PROBLEM_BANK.md#lc-0125) — Easy, 20 min
7. [LC 167 — Two Sum II - Input Array Is Sorted](PROBLEM_BANK.md#lc-0167) — Medium, 35 min
8. [LC 15 — 3Sum](PROBLEM_BANK.md#lc-0015) — Medium, 35 min
9. [LC 11 — Container With Most Water](PROBLEM_BANK.md#lc-0011) — Medium, 35 min
10. [LC 3 — Longest Substring Without Repeating Characters](PROBLEM_BANK.md#lc-0003) — Medium, 35 min
11. [LC 424 — Longest Repeating Character Replacement](PROBLEM_BANK.md#lc-0424) — Medium, 35 min
12. [LC 567 — Permutation in String](PROBLEM_BANK.md#lc-0567) — Medium, 35 min
13. [LC 560 — Subarray Sum Equals K](PROBLEM_BANK.md#lc-0560) — Medium, 35 min
14. [LC 73 — Set Matrix Zeroes](PROBLEM_BANK.md#lc-0073) — Medium, 35 min
15. [LC 54 — Spiral Matrix](PROBLEM_BANK.md#lc-0054) — Medium, 35 min
16. [LC 704 — Binary Search](PROBLEM_BANK.md#lc-0704) — Easy, 20 min
17. [LC 34 — Find First and Last Position of Element in Sorted Array](PROBLEM_BANK.md#lc-0034) — Medium, 35 min
18. [LC 33 — Search in Rotated Sorted Array](PROBLEM_BANK.md#lc-0033) — Medium, 35 min
19. [LC 875 — Koko Eating Bananas](PROBLEM_BANK.md#lc-0875) — Medium, 35 min
20. [LC 215 — Kth Largest Element in an Array](PROBLEM_BANK.md#lc-0215) — Medium, 35 min
21. [LC 206 — Reverse Linked List](PROBLEM_BANK.md#lc-0206) — Easy, 20 min
22. [LC 21 — Merge Two Sorted Lists](PROBLEM_BANK.md#lc-0021) — Easy, 20 min
23. [LC 141 — Linked List Cycle](PROBLEM_BANK.md#lc-0141) — Easy, 20 min
24. [LC 19 — Remove Nth Node From End of List](PROBLEM_BANK.md#lc-0019) — Medium, 35 min
25. [LC 143 — Reorder List](PROBLEM_BANK.md#lc-0143) — Medium, 35 min
26. [LC 20 — Valid Parentheses](PROBLEM_BANK.md#lc-0020) — Easy, 20 min
27. [LC 739 — Daily Temperatures](PROBLEM_BANK.md#lc-0739) — Medium, 35 min
28. [LC 56 — Merge Intervals](PROBLEM_BANK.md#lc-0056) — Medium, 35 min
29. [LC 57 — Insert Interval](PROBLEM_BANK.md#lc-0057) — Medium, 35 min
30. [LC 703 — Kth Largest Element in a Stream](PROBLEM_BANK.md#lc-0703) — Easy, 20 min
31. [LC 347 — Top K Frequent Elements](PROBLEM_BANK.md#lc-0347) — Medium, 35 min
32. [LC 23 — Merge k Sorted Lists](PROBLEM_BANK.md#lc-0023) — Hard, 50 min
33. [LC 78 — Subsets](PROBLEM_BANK.md#lc-0078) — Medium, 35 min
34. [LC 46 — Permutations](PROBLEM_BANK.md#lc-0046) — Medium, 35 min
35. [LC 39 — Combination Sum](PROBLEM_BANK.md#lc-0039) — Medium, 35 min
36. [LC 79 — Word Search](PROBLEM_BANK.md#lc-0079) — Medium, 35 min
37. [LC 226 — Invert Binary Tree](PROBLEM_BANK.md#lc-0226) — Easy, 20 min
38. [LC 104 — Maximum Depth of Binary Tree](PROBLEM_BANK.md#lc-0104) — Easy, 20 min
39. [LC 102 — Binary Tree Level Order Traversal](PROBLEM_BANK.md#lc-0102) — Medium, 35 min
40. [LC 543 — Diameter of Binary Tree](PROBLEM_BANK.md#lc-0543) — Easy, 20 min
41. [LC 98 — Validate Binary Search Tree](PROBLEM_BANK.md#lc-0098) — Medium, 35 min
42. [LC 235 — Lowest Common Ancestor of a Binary Search Tree](PROBLEM_BANK.md#lc-0235) — Medium, 35 min
43. [LC 208 — Implement Trie (Prefix Tree)](PROBLEM_BANK.md#lc-0208) — Medium, 35 min
44. [LC 200 — Number of Islands](PROBLEM_BANK.md#lc-0200) — Medium, 35 min
45. [LC 133 — Clone Graph](PROBLEM_BANK.md#lc-0133) — Medium, 35 min
46. [LC 994 — Rotting Oranges](PROBLEM_BANK.md#lc-0994) — Medium, 35 min
47. [LC 207 — Course Schedule](PROBLEM_BANK.md#lc-0207) — Medium, 35 min
48. [LC 210 — Course Schedule II](PROBLEM_BANK.md#lc-0210) — Medium, 35 min
49. [LC 684 — Redundant Connection](PROBLEM_BANK.md#lc-0684) — Medium, 35 min
50. [LC 743 — Network Delay Time](PROBLEM_BANK.md#lc-0743) — Medium, 35 min

### Milestone callouts

- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)
- [DSA-PRJ-030 — Array and string pattern visualizer](PROJECTS.md#dsa-prj-030)
- [DSA-PRJ-040 — Tree and graph traversal explorer](PROJECTS.md#dsa-prj-040)

### Intentionally deferred

Advanced/reference algorithms, most hard stretch problems, and long projects.


<a id="thirty-day-core-interview-foundation"></a>
## 5. 30-day core interview foundation

<!-- PATH_META {"id":"thirty-day-core-interview-foundation","title":"30-day core interview foundation","unit_count":97,"problem_count":73,"concept_minutes":[4425,6360],"problem_minutes":2300,"activities":{"Daily recall and review scheduling":[600,750],"Comparison, complexity, and postmortem sessions":[480,720],"Mock framing and feedback beyond coding time":[180,225],"Project checkpoints":[240,360]},"activity_minutes":[1500,2055],"rapid_total_minutes":[8225,10715],"full_unit_hours":[1203,2118],"assumed_or_bridge_prerequisites":[],"project_count":4} -->

**Who it is for:** A learner rebuilding a strong, prerequisite-safe interview core rather than only refreshing labels.

**Time assumption:** 30 days at approximately 4 h 35 min–5 h 58 min per day for the calculated rapid route.

**Prerequisite policy:** Basic Python is assumed. The selected curriculum is prerequisite-closed.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 73 h 45 min–106 h |
| Complete first attempts for 73 selected problems | 38 h 20 min |
| Daily recall and review scheduling | 10 h–12 h 30 min |
| Comparison, complexity, and postmortem sessions | 8 h–12 h |
| Mock framing and feedback beyond coding time | 3 h–3 h 45 min |
| Project checkpoints | 4 h–6 h |
| **Required activities subtotal** | **25 h–34 h 15 min** |
| **Rapid path total** | **137 h 5 min–178 h 35 min** |
| **Full mastery of included units** | **1203–2118 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (97 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-FND-070 — Interview mathematics: logarithms, sums, counting, and probability](CURRICULUM.md#dsa-fnd-070)
8. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
9. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
10. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
11. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
12. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
13. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
14. [DSA-PY-060 — Recursion limits, integers, and Python performance traps](CURRICULUM.md#dsa-py-060)
15. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
16. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
17. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
18. [DSA-SEQ-040 — Opposite-direction two pointers](CURRICULUM.md#dsa-seq-040)
19. [DSA-SEQ-050 — Fixed-size sliding windows](CURRICULUM.md#dsa-seq-050)
20. [DSA-SEQ-060 — Variable-size sliding windows](CURRICULUM.md#dsa-seq-060)
21. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
22. [DSA-SEQ-080 — Suffix aggregates and bidirectional precomputation](CURRICULUM.md#dsa-seq-080)
23. [DSA-SEQ-100 — Running optima and Kadane-style reasoning](CURRICULUM.md#dsa-seq-100)
24. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
25. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
26. [DSA-ORD-020 — Lower bound, upper bound, and first/last true](CURRICULUM.md#dsa-ord-020)
27. [DSA-ORD-030 — Rotated and partially ordered search](CURRICULUM.md#dsa-ord-030)
28. [DSA-ORD-040 — Binary search on a monotonic answer space](CURRICULUM.md#dsa-ord-040)
29. [DSA-ORD-060 — Partitioning, quicksort concepts, and quickselect](CURRICULUM.md#dsa-ord-060)
30. [DSA-ORD-070 — Counting, bucket, and constraint-driven ordering](CURRICULUM.md#dsa-ord-070)
31. [DSA-LNK-010 — Linked-list representation, sentinels, and ownership](CURRICULUM.md#dsa-lnk-010)
32. [DSA-LNK-020 — Reversal and safe pointer rewiring](CURRICULUM.md#dsa-lnk-020)
33. [DSA-LNK-030 — Fast/slow pointers and cycle detection](CURRICULUM.md#dsa-lnk-030)
34. [DSA-LNK-040 — Merging, intersection, and reference preservation](CURRICULUM.md#dsa-lnk-040)
35. [DSA-LNK-050 — Sublist reversal, reordering, and k-group transformations](CURRICULUM.md#dsa-lnk-050)
36. [DSA-LNK-060 — Linked composite structures and cache design](CURRICULUM.md#dsa-lnk-060)
37. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
38. [DSA-SQH-020 — Matching, nesting, and expression evaluation](CURRICULUM.md#dsa-sqh-020)
39. [DSA-SQH-030 — Monotonic stacks and next-element reasoning](CURRICULUM.md#dsa-sqh-030)
40. [DSA-SQH-050 — Interval sorting, merging, and coverage](CURRICULUM.md#dsa-sqh-050)
41. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
42. [DSA-SQH-080 — Top-K and streaming selection](CURRICULUM.md#dsa-sqh-080)
43. [DSA-SQH-090 — K-way merge and frontier heaps](CURRICULUM.md#dsa-sqh-090)
44. [DSA-SQH-100 — Two-heaps median, lazy deletion, and dynamic priorities](CURRICULUM.md#dsa-sqh-100)
45. [DSA-REC-010 — Recursive decomposition and decision trees](CURRICULUM.md#dsa-rec-010)
46. [DSA-REC-020 — Subsets and combinations](CURRICULUM.md#dsa-rec-020)
47. [DSA-REC-030 — Permutations and duplicate handling](CURRICULUM.md#dsa-rec-030)
48. [DSA-REC-040 — Constraint propagation and pruning](CURRICULUM.md#dsa-rec-040)
49. [DSA-REC-050 — Grid and path backtracking](CURRICULUM.md#dsa-rec-050)
50. [DSA-REC-070 — Backtracking versus dynamic programming](CURRICULUM.md#dsa-rec-070)
51. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
52. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
53. [DSA-TRE-030 — Breadth-first and level-order traversal](CURRICULUM.md#dsa-tre-030)
54. [DSA-TRE-040 — Path state and root-to-leaf reasoning](CURRICULUM.md#dsa-tre-040)
55. [DSA-TRE-050 — Subtree aggregation and divide-and-conquer](CURRICULUM.md#dsa-tre-050)
56. [DSA-TRE-060 — Binary-search-tree invariants, search, update, and validation](CURRICULUM.md#dsa-tre-060)
57. [DSA-TRE-070 — Lowest common ancestor and ancestry reasoning](CURRICULUM.md#dsa-tre-070)
58. [DSA-TRE-090 — Tries and prefix search](CURRICULUM.md#dsa-tre-090)
59. [DSA-TRE-100 — Tree dynamic programming and recursion-depth safety](CURRICULUM.md#dsa-tre-100)
60. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
61. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
62. [DSA-GRA-030 — Depth-first search](CURRICULUM.md#dsa-gra-030)
63. [DSA-GRA-040 — Connected components and grid-as-graph reasoning](CURRICULUM.md#dsa-gra-040)
64. [DSA-GRA-050 — Multi-source BFS](CURRICULUM.md#dsa-gra-050)
65. [DSA-GRA-070 — Cycle detection in directed and undirected graphs](CURRICULUM.md#dsa-gra-070)
66. [DSA-GRA-080 — Topological sorting and dependency order](CURRICULUM.md#dsa-gra-080)
67. [DSA-GRA-090 — Disjoint-set union](CURRICULUM.md#dsa-gra-090)
68. [DSA-GRA-100 — Shortest-path algorithm selection](CURRICULUM.md#dsa-gra-100)
69. [DSA-GRA-110 — Dijkstra and non-negative weighted paths](CURRICULUM.md#dsa-gra-110)
70. [DSA-GRA-130 — Minimum spanning trees](CURRICULUM.md#dsa-gra-130)
71. [DSA-GRD-010 — Greedy-choice recognition and counterexamples](CURRICULUM.md#dsa-grd-010)
72. [DSA-GRD-020 — Exchange arguments and stays-ahead proofs](CURRICULUM.md#dsa-grd-020)
73. [DSA-GRD-030 — Interval scheduling and resource allocation](CURRICULUM.md#dsa-grd-030)
74. [DSA-GRD-040 — Sorting-based greedy and local choices](CURRICULUM.md#dsa-grd-040)
75. [DSA-GRD-050 — Greedy versus dynamic programming](CURRICULUM.md#dsa-grd-050)
76. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
77. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
78. [DSA-DP-030 — One-dimensional sequence DP](CURRICULUM.md#dsa-dp-030)
79. [DSA-DP-040 — Grid and path DP](CURRICULUM.md#dsa-dp-040)
80. [DSA-DP-050 — Knapsack and subset-sum families](CURRICULUM.md#dsa-dp-050)
81. [DSA-DP-060 — Coin change and unbounded-choice DP](CURRICULUM.md#dsa-dp-060)
82. [DSA-DP-070 — Subsequence and sequence-alignment DP](CURRICULUM.md#dsa-dp-070)
83. [DSA-DP-080 — Longest increasing subsequence](CURRICULUM.md#dsa-dp-080)
84. [DSA-DP-090 — String dynamic programming](CURRICULUM.md#dsa-dp-090)
85. [DSA-DP-110 — State-machine dynamic programming](CURRICULUM.md#dsa-dp-110)
86. [DSA-DP-120 — Tree dynamic programming](CURRICULUM.md#dsa-dp-120)
87. [DSA-BMS-010 — Bit operations and masks](CURRICULUM.md#dsa-bms-010)
88. [DSA-BMS-020 — XOR invariants and parity reasoning](CURRICULUM.md#dsa-bms-020)
89. [DSA-BMS-040 — GCD, divisibility, and Euclidean reasoning](CURRICULUM.md#dsa-bms-040)
90. [DSA-BMS-050 — Primes and sieve techniques](CURRICULUM.md#dsa-bms-050)
91. [DSA-BMS-060 — Modular arithmetic and fixed-width translation](CURRICULUM.md#dsa-bms-060)
92. [DSA-SYN-010 — LRU cache composite design](CURRICULUM.md#dsa-syn-010)
93. [DSA-SYN-020 — Min stack and randomized-set API invariants](CURRICULUM.md#dsa-syn-020)
94. [DSA-SYN-030 — Median stream and time-based key-value storage](CURRICULUM.md#dsa-syn-030)
95. [DSA-SYN-040 — Autocomplete and in-memory indexes](CURRICULUM.md#dsa-syn-040)
96. [DSA-SYN-050 — Task scheduling and composite constraint modeling](CURRICULUM.md#dsa-syn-050)
97. [DSA-SYN-060 — Mixed unlabeled problem solving](CURRICULUM.md#dsa-syn-060)

### Selected problem attempts (73)

1. [LC 1 — Two Sum](PROBLEM_BANK.md#lc-0001) — Easy, 20 min
2. [LC 217 — Contains Duplicate](PROBLEM_BANK.md#lc-0217) — Easy, 20 min
3. [LC 121 — Best Time to Buy and Sell Stock](PROBLEM_BANK.md#lc-0121) — Easy, 20 min
4. [LC 238 — Product of Array Except Self](PROBLEM_BANK.md#lc-0238) — Medium, 35 min
5. [LC 53 — Maximum Subarray](PROBLEM_BANK.md#lc-0053) — Medium, 35 min
6. [LC 125 — Valid Palindrome](PROBLEM_BANK.md#lc-0125) — Easy, 20 min
7. [LC 167 — Two Sum II - Input Array Is Sorted](PROBLEM_BANK.md#lc-0167) — Medium, 35 min
8. [LC 15 — 3Sum](PROBLEM_BANK.md#lc-0015) — Medium, 35 min
9. [LC 11 — Container With Most Water](PROBLEM_BANK.md#lc-0011) — Medium, 35 min
10. [LC 3 — Longest Substring Without Repeating Characters](PROBLEM_BANK.md#lc-0003) — Medium, 35 min
11. [LC 424 — Longest Repeating Character Replacement](PROBLEM_BANK.md#lc-0424) — Medium, 35 min
12. [LC 567 — Permutation in String](PROBLEM_BANK.md#lc-0567) — Medium, 35 min
13. [LC 560 — Subarray Sum Equals K](PROBLEM_BANK.md#lc-0560) — Medium, 35 min
14. [LC 73 — Set Matrix Zeroes](PROBLEM_BANK.md#lc-0073) — Medium, 35 min
15. [LC 54 — Spiral Matrix](PROBLEM_BANK.md#lc-0054) — Medium, 35 min
16. [LC 704 — Binary Search](PROBLEM_BANK.md#lc-0704) — Easy, 20 min
17. [LC 34 — Find First and Last Position of Element in Sorted Array](PROBLEM_BANK.md#lc-0034) — Medium, 35 min
18. [LC 33 — Search in Rotated Sorted Array](PROBLEM_BANK.md#lc-0033) — Medium, 35 min
19. [LC 875 — Koko Eating Bananas](PROBLEM_BANK.md#lc-0875) — Medium, 35 min
20. [LC 215 — Kth Largest Element in an Array](PROBLEM_BANK.md#lc-0215) — Medium, 35 min
21. [LC 206 — Reverse Linked List](PROBLEM_BANK.md#lc-0206) — Easy, 20 min
22. [LC 21 — Merge Two Sorted Lists](PROBLEM_BANK.md#lc-0021) — Easy, 20 min
23. [LC 141 — Linked List Cycle](PROBLEM_BANK.md#lc-0141) — Easy, 20 min
24. [LC 19 — Remove Nth Node From End of List](PROBLEM_BANK.md#lc-0019) — Medium, 35 min
25. [LC 143 — Reorder List](PROBLEM_BANK.md#lc-0143) — Medium, 35 min
26. [LC 20 — Valid Parentheses](PROBLEM_BANK.md#lc-0020) — Easy, 20 min
27. [LC 739 — Daily Temperatures](PROBLEM_BANK.md#lc-0739) — Medium, 35 min
28. [LC 56 — Merge Intervals](PROBLEM_BANK.md#lc-0056) — Medium, 35 min
29. [LC 57 — Insert Interval](PROBLEM_BANK.md#lc-0057) — Medium, 35 min
30. [LC 703 — Kth Largest Element in a Stream](PROBLEM_BANK.md#lc-0703) — Easy, 20 min
31. [LC 347 — Top K Frequent Elements](PROBLEM_BANK.md#lc-0347) — Medium, 35 min
32. [LC 23 — Merge k Sorted Lists](PROBLEM_BANK.md#lc-0023) — Hard, 50 min
33. [LC 78 — Subsets](PROBLEM_BANK.md#lc-0078) — Medium, 35 min
34. [LC 46 — Permutations](PROBLEM_BANK.md#lc-0046) — Medium, 35 min
35. [LC 39 — Combination Sum](PROBLEM_BANK.md#lc-0039) — Medium, 35 min
36. [LC 79 — Word Search](PROBLEM_BANK.md#lc-0079) — Medium, 35 min
37. [LC 226 — Invert Binary Tree](PROBLEM_BANK.md#lc-0226) — Easy, 20 min
38. [LC 104 — Maximum Depth of Binary Tree](PROBLEM_BANK.md#lc-0104) — Easy, 20 min
39. [LC 102 — Binary Tree Level Order Traversal](PROBLEM_BANK.md#lc-0102) — Medium, 35 min
40. [LC 543 — Diameter of Binary Tree](PROBLEM_BANK.md#lc-0543) — Easy, 20 min
41. [LC 98 — Validate Binary Search Tree](PROBLEM_BANK.md#lc-0098) — Medium, 35 min
42. [LC 235 — Lowest Common Ancestor of a Binary Search Tree](PROBLEM_BANK.md#lc-0235) — Medium, 35 min
43. [LC 208 — Implement Trie (Prefix Tree)](PROBLEM_BANK.md#lc-0208) — Medium, 35 min
44. [LC 200 — Number of Islands](PROBLEM_BANK.md#lc-0200) — Medium, 35 min
45. [LC 133 — Clone Graph](PROBLEM_BANK.md#lc-0133) — Medium, 35 min
46. [LC 994 — Rotting Oranges](PROBLEM_BANK.md#lc-0994) — Medium, 35 min
47. [LC 207 — Course Schedule](PROBLEM_BANK.md#lc-0207) — Medium, 35 min
48. [LC 210 — Course Schedule II](PROBLEM_BANK.md#lc-0210) — Medium, 35 min
49. [LC 684 — Redundant Connection](PROBLEM_BANK.md#lc-0684) — Medium, 35 min
50. [LC 743 — Network Delay Time](PROBLEM_BANK.md#lc-0743) — Medium, 35 min
51. [LC 1584 — Min Cost to Connect All Points](PROBLEM_BANK.md#lc-1584) — Medium, 35 min
52. [LC 55 — Jump Game](PROBLEM_BANK.md#lc-0055) — Medium, 35 min
53. [LC 435 — Non-overlapping Intervals](PROBLEM_BANK.md#lc-0435) — Medium, 35 min
54. [LC 70 — Climbing Stairs](PROBLEM_BANK.md#lc-0070) — Easy, 20 min
55. [LC 198 — House Robber](PROBLEM_BANK.md#lc-0198) — Medium, 35 min
56. [LC 322 — Coin Change](PROBLEM_BANK.md#lc-0322) — Medium, 35 min
57. [LC 416 — Partition Equal Subset Sum](PROBLEM_BANK.md#lc-0416) — Medium, 35 min
58. [LC 62 — Unique Paths](PROBLEM_BANK.md#lc-0062) — Medium, 35 min
59. [LC 300 — Longest Increasing Subsequence](PROBLEM_BANK.md#lc-0300) — Medium, 35 min
60. [LC 1143 — Longest Common Subsequence](PROBLEM_BANK.md#lc-1143) — Medium, 35 min
61. [LC 139 — Word Break](PROBLEM_BANK.md#lc-0139) — Medium, 35 min
62. [LC 136 — Single Number](PROBLEM_BANK.md#lc-0136) — Easy, 20 min
63. [LC 191 — Number of 1 Bits](PROBLEM_BANK.md#lc-0191) — Easy, 20 min
64. [LC 204 — Count Primes](PROBLEM_BANK.md#lc-0204) — Medium, 35 min
65. [LC 146 — LRU Cache](PROBLEM_BANK.md#lc-0146) — Medium, 35 min
66. [LC 155 — Min Stack](PROBLEM_BANK.md#lc-0155) — Easy, 20 min
67. [LC 380 — Insert Delete GetRandom O(1)](PROBLEM_BANK.md#lc-0380) — Medium, 35 min
68. [LC 981 — Time Based Key-Value Store](PROBLEM_BANK.md#lc-0981) — Medium, 35 min
69. [LC 1268 — Search Suggestions System](PROBLEM_BANK.md#lc-1268) — Medium, 35 min
70. [LC 621 — Task Scheduler](PROBLEM_BANK.md#lc-0621) — Medium, 35 min
71. [LC 1071 — Greatest Common Divisor of Strings](PROBLEM_BANK.md#lc-1071) — Easy, 20 min
72. [LC 974 — Subarray Sums Divisible by K](PROBLEM_BANK.md#lc-0974) — Medium, 35 min
73. [LC 309 — Best Time to Buy and Sell Stock with Cooldown](PROBLEM_BANK.md#lc-0309) — Medium, 35 min

### Milestone callouts

- [DSA-PRJ-010 — Core data-structure invariant laboratory](PROJECTS.md#dsa-prj-010)
- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)
- [DSA-PRJ-030 — Array and string pattern visualizer](PROJECTS.md#dsa-prj-030)
- [DSA-PRJ-040 — Tree and graph traversal explorer](PROJECTS.md#dsa-prj-040)

### Intentionally deferred

SCC, digit DP, rolling hash/KMP/Z, advanced range structures, and some stretch mocks.


<a id="ninety-day-comprehensive-interview"></a>
## 6. 90-day comprehensive interview preparation

<!-- PATH_META {"id":"ninety-day-comprehensive-interview","title":"90-day comprehensive interview preparation","unit_count":122,"problem_count":106,"concept_minutes":[5675,8135],"problem_minutes":3575,"activities":{"Spaced recall and delayed re-solves":[1800,2400],"Comparison, proof, and postmortem sessions":[1200,1800],"Mock framing and feedback beyond coding time":[360,540],"Project checkpoints":[600,900]},"activity_minutes":[3960,5640],"rapid_total_minutes":[13210,17350],"full_unit_hours":[1563,2748],"assumed_or_bridge_prerequisites":[],"project_count":7} -->

**Who it is for:** A learner seeking broad product-company readiness with mixed practice, advanced comparisons, and projects.

**Time assumption:** 90 days at approximately 2 h 27 min–3 h 13 min per day for the calculated rapid route.

**Prerequisite policy:** Basic Python is assumed; this is a sustained preparation plan, not a guarantee of interview outcomes.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 94 h 35 min–135 h 35 min |
| Complete first attempts for 106 selected problems | 59 h 35 min |
| Spaced recall and delayed re-solves | 30 h–40 h |
| Comparison, proof, and postmortem sessions | 20 h–30 h |
| Mock framing and feedback beyond coding time | 6 h–9 h |
| Project checkpoints | 10 h–15 h |
| **Required activities subtotal** | **66 h–94 h** |
| **Rapid path total** | **220 h 10 min–289 h 10 min** |
| **Full mastery of included units** | **1563–2748 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (122 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-FND-070 — Interview mathematics: logarithms, sums, counting, and probability](CURRICULUM.md#dsa-fnd-070)
8. [DSA-FND-080 — Testing algorithms with examples, oracles, and properties](CURRICULUM.md#dsa-fnd-080)
9. [DSA-FND-090 — Debugging wrong answers, time limits, and memory failures](CURRICULUM.md#dsa-fnd-090)
10. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
11. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
12. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
13. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
14. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
15. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
16. [DSA-PY-060 — Recursion limits, integers, and Python performance traps](CURRICULUM.md#dsa-py-060)
17. [DSA-PY-070 — Iterators, generators, and streaming inputs](CURRICULUM.md#dsa-py-070)
18. [DSA-PY-080 — pytest, Hypothesis, brute-force oracles, and differential testing](CURRICULUM.md#dsa-py-080)
19. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
20. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
21. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
22. [DSA-SEQ-040 — Opposite-direction two pointers](CURRICULUM.md#dsa-seq-040)
23. [DSA-SEQ-050 — Fixed-size sliding windows](CURRICULUM.md#dsa-seq-050)
24. [DSA-SEQ-060 — Variable-size sliding windows](CURRICULUM.md#dsa-seq-060)
25. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
26. [DSA-SEQ-080 — Suffix aggregates and bidirectional precomputation](CURRICULUM.md#dsa-seq-080)
27. [DSA-SEQ-090 — Difference arrays and range updates](CURRICULUM.md#dsa-seq-090)
28. [DSA-SEQ-100 — Running optima and Kadane-style reasoning](CURRICULUM.md#dsa-seq-100)
29. [DSA-SEQ-110 — Index placement and cyclic-position techniques](CURRICULUM.md#dsa-seq-110)
30. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
31. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
32. [DSA-ORD-020 — Lower bound, upper bound, and first/last true](CURRICULUM.md#dsa-ord-020)
33. [DSA-ORD-030 — Rotated and partially ordered search](CURRICULUM.md#dsa-ord-030)
34. [DSA-ORD-040 — Binary search on a monotonic answer space](CURRICULUM.md#dsa-ord-040)
35. [DSA-ORD-050 — Merge sort, stable merging, and inversion counting](CURRICULUM.md#dsa-ord-050)
36. [DSA-ORD-060 — Partitioning, quicksort concepts, and quickselect](CURRICULUM.md#dsa-ord-060)
37. [DSA-ORD-070 — Counting, bucket, and constraint-driven ordering](CURRICULUM.md#dsa-ord-070)
38. [DSA-LNK-010 — Linked-list representation, sentinels, and ownership](CURRICULUM.md#dsa-lnk-010)
39. [DSA-LNK-020 — Reversal and safe pointer rewiring](CURRICULUM.md#dsa-lnk-020)
40. [DSA-LNK-030 — Fast/slow pointers and cycle detection](CURRICULUM.md#dsa-lnk-030)
41. [DSA-LNK-040 — Merging, intersection, and reference preservation](CURRICULUM.md#dsa-lnk-040)
42. [DSA-LNK-050 — Sublist reversal, reordering, and k-group transformations](CURRICULUM.md#dsa-lnk-050)
43. [DSA-LNK-060 — Linked composite structures and cache design](CURRICULUM.md#dsa-lnk-060)
44. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
45. [DSA-SQH-020 — Matching, nesting, and expression evaluation](CURRICULUM.md#dsa-sqh-020)
46. [DSA-SQH-030 — Monotonic stacks and next-element reasoning](CURRICULUM.md#dsa-sqh-030)
47. [DSA-SQH-040 — Monotonic deques and window extrema](CURRICULUM.md#dsa-sqh-040)
48. [DSA-SQH-050 — Interval sorting, merging, and coverage](CURRICULUM.md#dsa-sqh-050)
49. [DSA-SQH-060 — Sweep-line events and scheduling conflicts](CURRICULUM.md#dsa-sqh-060)
50. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
51. [DSA-SQH-080 — Top-K and streaming selection](CURRICULUM.md#dsa-sqh-080)
52. [DSA-SQH-090 — K-way merge and frontier heaps](CURRICULUM.md#dsa-sqh-090)
53. [DSA-SQH-100 — Two-heaps median, lazy deletion, and dynamic priorities](CURRICULUM.md#dsa-sqh-100)
54. [DSA-REC-010 — Recursive decomposition and decision trees](CURRICULUM.md#dsa-rec-010)
55. [DSA-REC-020 — Subsets and combinations](CURRICULUM.md#dsa-rec-020)
56. [DSA-REC-030 — Permutations and duplicate handling](CURRICULUM.md#dsa-rec-030)
57. [DSA-REC-040 — Constraint propagation and pruning](CURRICULUM.md#dsa-rec-040)
58. [DSA-REC-050 — Grid and path backtracking](CURRICULUM.md#dsa-rec-050)
59. [DSA-REC-060 — Branch ordering and backtracking complexity](CURRICULUM.md#dsa-rec-060)
60. [DSA-REC-070 — Backtracking versus dynamic programming](CURRICULUM.md#dsa-rec-070)
61. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
62. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
63. [DSA-TRE-030 — Breadth-first and level-order traversal](CURRICULUM.md#dsa-tre-030)
64. [DSA-TRE-040 — Path state and root-to-leaf reasoning](CURRICULUM.md#dsa-tre-040)
65. [DSA-TRE-050 — Subtree aggregation and divide-and-conquer](CURRICULUM.md#dsa-tre-050)
66. [DSA-TRE-060 — Binary-search-tree invariants, search, update, and validation](CURRICULUM.md#dsa-tre-060)
67. [DSA-TRE-070 — Lowest common ancestor and ancestry reasoning](CURRICULUM.md#dsa-tre-070)
68. [DSA-TRE-080 — Tree construction and serialization concepts](CURRICULUM.md#dsa-tre-080)
69. [DSA-TRE-090 — Tries and prefix search](CURRICULUM.md#dsa-tre-090)
70. [DSA-TRE-100 — Tree dynamic programming and recursion-depth safety](CURRICULUM.md#dsa-tre-100)
71. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
72. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
73. [DSA-GRA-030 — Depth-first search](CURRICULUM.md#dsa-gra-030)
74. [DSA-GRA-040 — Connected components and grid-as-graph reasoning](CURRICULUM.md#dsa-gra-040)
75. [DSA-GRA-050 — Multi-source BFS](CURRICULUM.md#dsa-gra-050)
76. [DSA-GRA-060 — Bipartite testing](CURRICULUM.md#dsa-gra-060)
77. [DSA-GRA-070 — Cycle detection in directed and undirected graphs](CURRICULUM.md#dsa-gra-070)
78. [DSA-GRA-080 — Topological sorting and dependency order](CURRICULUM.md#dsa-gra-080)
79. [DSA-GRA-090 — Disjoint-set union](CURRICULUM.md#dsa-gra-090)
80. [DSA-GRA-100 — Shortest-path algorithm selection](CURRICULUM.md#dsa-gra-100)
81. [DSA-GRA-110 — Dijkstra and non-negative weighted paths](CURRICULUM.md#dsa-gra-110)
82. [DSA-GRA-120 — Bellman-Ford and all-pairs shortest paths](CURRICULUM.md#dsa-gra-120)
83. [DSA-GRA-130 — Minimum spanning trees](CURRICULUM.md#dsa-gra-130)
84. [DSA-GRA-140 — Zero-one BFS](CURRICULUM.md#dsa-gra-140)
85. [DSA-GRA-150 — Low-link DFS: bridges, articulation points, and strongly connected components](CURRICULUM.md#dsa-gra-150)
86. [DSA-GRD-010 — Greedy-choice recognition and counterexamples](CURRICULUM.md#dsa-grd-010)
87. [DSA-GRD-020 — Exchange arguments and stays-ahead proofs](CURRICULUM.md#dsa-grd-020)
88. [DSA-GRD-030 — Interval scheduling and resource allocation](CURRICULUM.md#dsa-grd-030)
89. [DSA-GRD-040 — Sorting-based greedy and local choices](CURRICULUM.md#dsa-grd-040)
90. [DSA-GRD-050 — Greedy versus dynamic programming](CURRICULUM.md#dsa-grd-050)
91. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
92. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
93. [DSA-DP-030 — One-dimensional sequence DP](CURRICULUM.md#dsa-dp-030)
94. [DSA-DP-040 — Grid and path DP](CURRICULUM.md#dsa-dp-040)
95. [DSA-DP-050 — Knapsack and subset-sum families](CURRICULUM.md#dsa-dp-050)
96. [DSA-DP-060 — Coin change and unbounded-choice DP](CURRICULUM.md#dsa-dp-060)
97. [DSA-DP-070 — Subsequence and sequence-alignment DP](CURRICULUM.md#dsa-dp-070)
98. [DSA-DP-080 — Longest increasing subsequence](CURRICULUM.md#dsa-dp-080)
99. [DSA-DP-090 — String dynamic programming](CURRICULUM.md#dsa-dp-090)
100. [DSA-DP-100 — Interval dynamic programming](CURRICULUM.md#dsa-dp-100)
101. [DSA-DP-110 — State-machine dynamic programming](CURRICULUM.md#dsa-dp-110)
102. [DSA-DP-120 — Tree dynamic programming](CURRICULUM.md#dsa-dp-120)
103. [DSA-DP-130 — Bitmask dynamic programming](CURRICULUM.md#dsa-dp-130)
104. [DSA-BMS-010 — Bit operations and masks](CURRICULUM.md#dsa-bms-010)
105. [DSA-BMS-020 — XOR invariants and parity reasoning](CURRICULUM.md#dsa-bms-020)
106. [DSA-BMS-030 — Subset enumeration with bitmasks](CURRICULUM.md#dsa-bms-030)
107. [DSA-BMS-040 — GCD, divisibility, and Euclidean reasoning](CURRICULUM.md#dsa-bms-040)
108. [DSA-BMS-050 — Primes and sieve techniques](CURRICULUM.md#dsa-bms-050)
109. [DSA-BMS-060 — Modular arithmetic and fixed-width translation](CURRICULUM.md#dsa-bms-060)
110. [DSA-BMS-070 — Combinatorics and interview probability](CURRICULUM.md#dsa-bms-070)
111. [DSA-BMS-080 — Rolling hash and collision reasoning](CURRICULUM.md#dsa-bms-080)
112. [DSA-BMS-090 — KMP and prefix-function string matching](CURRICULUM.md#dsa-bms-090)
113. [DSA-ADV-010 — Fenwick trees](CURRICULUM.md#dsa-adv-010)
114. [DSA-ADV-020 — Segment trees and lazy propagation concepts](CURRICULUM.md#dsa-adv-020)
115. [DSA-ADV-040 — Reservoir sampling, randomized selection, and streaming algorithms](CURRICULUM.md#dsa-adv-040)
116. [DSA-SYN-010 — LRU cache composite design](CURRICULUM.md#dsa-syn-010)
117. [DSA-SYN-020 — Min stack and randomized-set API invariants](CURRICULUM.md#dsa-syn-020)
118. [DSA-SYN-030 — Median stream and time-based key-value storage](CURRICULUM.md#dsa-syn-030)
119. [DSA-SYN-040 — Autocomplete and in-memory indexes](CURRICULUM.md#dsa-syn-040)
120. [DSA-SYN-050 — Task scheduling and composite constraint modeling](CURRICULUM.md#dsa-syn-050)
121. [DSA-SYN-060 — Mixed unlabeled problem solving](CURRICULUM.md#dsa-syn-060)
122. [DSA-SYN-070 — Mock interviews, readiness gates, and error analysis](CURRICULUM.md#dsa-syn-070)

### Selected problem attempts (106)

1. [LC 1 — Two Sum](PROBLEM_BANK.md#lc-0001) — Easy, 20 min
2. [LC 3 — Longest Substring Without Repeating Characters](PROBLEM_BANK.md#lc-0003) — Medium, 35 min
3. [LC 11 — Container With Most Water](PROBLEM_BANK.md#lc-0011) — Medium, 35 min
4. [LC 15 — 3Sum](PROBLEM_BANK.md#lc-0015) — Medium, 35 min
5. [LC 19 — Remove Nth Node From End of List](PROBLEM_BANK.md#lc-0019) — Medium, 35 min
6. [LC 20 — Valid Parentheses](PROBLEM_BANK.md#lc-0020) — Easy, 20 min
7. [LC 21 — Merge Two Sorted Lists](PROBLEM_BANK.md#lc-0021) — Easy, 20 min
8. [LC 23 — Merge k Sorted Lists](PROBLEM_BANK.md#lc-0023) — Hard, 50 min
9. [LC 33 — Search in Rotated Sorted Array](PROBLEM_BANK.md#lc-0033) — Medium, 35 min
10. [LC 34 — Find First and Last Position of Element in Sorted Array](PROBLEM_BANK.md#lc-0034) — Medium, 35 min
11. [LC 39 — Combination Sum](PROBLEM_BANK.md#lc-0039) — Medium, 35 min
12. [LC 46 — Permutations](PROBLEM_BANK.md#lc-0046) — Medium, 35 min
13. [LC 53 — Maximum Subarray](PROBLEM_BANK.md#lc-0053) — Medium, 35 min
14. [LC 54 — Spiral Matrix](PROBLEM_BANK.md#lc-0054) — Medium, 35 min
15. [LC 55 — Jump Game](PROBLEM_BANK.md#lc-0055) — Medium, 35 min
16. [LC 56 — Merge Intervals](PROBLEM_BANK.md#lc-0056) — Medium, 35 min
17. [LC 57 — Insert Interval](PROBLEM_BANK.md#lc-0057) — Medium, 35 min
18. [LC 62 — Unique Paths](PROBLEM_BANK.md#lc-0062) — Medium, 35 min
19. [LC 70 — Climbing Stairs](PROBLEM_BANK.md#lc-0070) — Easy, 20 min
20. [LC 73 — Set Matrix Zeroes](PROBLEM_BANK.md#lc-0073) — Medium, 35 min
21. [LC 78 — Subsets](PROBLEM_BANK.md#lc-0078) — Medium, 35 min
22. [LC 79 — Word Search](PROBLEM_BANK.md#lc-0079) — Medium, 35 min
23. [LC 98 — Validate Binary Search Tree](PROBLEM_BANK.md#lc-0098) — Medium, 35 min
24. [LC 102 — Binary Tree Level Order Traversal](PROBLEM_BANK.md#lc-0102) — Medium, 35 min
25. [LC 104 — Maximum Depth of Binary Tree](PROBLEM_BANK.md#lc-0104) — Easy, 20 min
26. [LC 121 — Best Time to Buy and Sell Stock](PROBLEM_BANK.md#lc-0121) — Easy, 20 min
27. [LC 125 — Valid Palindrome](PROBLEM_BANK.md#lc-0125) — Easy, 20 min
28. [LC 133 — Clone Graph](PROBLEM_BANK.md#lc-0133) — Medium, 35 min
29. [LC 136 — Single Number](PROBLEM_BANK.md#lc-0136) — Easy, 20 min
30. [LC 139 — Word Break](PROBLEM_BANK.md#lc-0139) — Medium, 35 min
31. [LC 141 — Linked List Cycle](PROBLEM_BANK.md#lc-0141) — Easy, 20 min
32. [LC 143 — Reorder List](PROBLEM_BANK.md#lc-0143) — Medium, 35 min
33. [LC 146 — LRU Cache](PROBLEM_BANK.md#lc-0146) — Medium, 35 min
34. [LC 155 — Min Stack](PROBLEM_BANK.md#lc-0155) — Easy, 20 min
35. [LC 167 — Two Sum II - Input Array Is Sorted](PROBLEM_BANK.md#lc-0167) — Medium, 35 min
36. [LC 191 — Number of 1 Bits](PROBLEM_BANK.md#lc-0191) — Easy, 20 min
37. [LC 198 — House Robber](PROBLEM_BANK.md#lc-0198) — Medium, 35 min
38. [LC 200 — Number of Islands](PROBLEM_BANK.md#lc-0200) — Medium, 35 min
39. [LC 204 — Count Primes](PROBLEM_BANK.md#lc-0204) — Medium, 35 min
40. [LC 206 — Reverse Linked List](PROBLEM_BANK.md#lc-0206) — Easy, 20 min
41. [LC 207 — Course Schedule](PROBLEM_BANK.md#lc-0207) — Medium, 35 min
42. [LC 208 — Implement Trie (Prefix Tree)](PROBLEM_BANK.md#lc-0208) — Medium, 35 min
43. [LC 210 — Course Schedule II](PROBLEM_BANK.md#lc-0210) — Medium, 35 min
44. [LC 215 — Kth Largest Element in an Array](PROBLEM_BANK.md#lc-0215) — Medium, 35 min
45. [LC 217 — Contains Duplicate](PROBLEM_BANK.md#lc-0217) — Easy, 20 min
46. [LC 226 — Invert Binary Tree](PROBLEM_BANK.md#lc-0226) — Easy, 20 min
47. [LC 235 — Lowest Common Ancestor of a Binary Search Tree](PROBLEM_BANK.md#lc-0235) — Medium, 35 min
48. [LC 238 — Product of Array Except Self](PROBLEM_BANK.md#lc-0238) — Medium, 35 min
49. [LC 300 — Longest Increasing Subsequence](PROBLEM_BANK.md#lc-0300) — Medium, 35 min
50. [LC 309 — Best Time to Buy and Sell Stock with Cooldown](PROBLEM_BANK.md#lc-0309) — Medium, 35 min
51. [LC 322 — Coin Change](PROBLEM_BANK.md#lc-0322) — Medium, 35 min
52. [LC 347 — Top K Frequent Elements](PROBLEM_BANK.md#lc-0347) — Medium, 35 min
53. [LC 380 — Insert Delete GetRandom O(1)](PROBLEM_BANK.md#lc-0380) — Medium, 35 min
54. [LC 416 — Partition Equal Subset Sum](PROBLEM_BANK.md#lc-0416) — Medium, 35 min
55. [LC 424 — Longest Repeating Character Replacement](PROBLEM_BANK.md#lc-0424) — Medium, 35 min
56. [LC 435 — Non-overlapping Intervals](PROBLEM_BANK.md#lc-0435) — Medium, 35 min
57. [LC 543 — Diameter of Binary Tree](PROBLEM_BANK.md#lc-0543) — Easy, 20 min
58. [LC 560 — Subarray Sum Equals K](PROBLEM_BANK.md#lc-0560) — Medium, 35 min
59. [LC 567 — Permutation in String](PROBLEM_BANK.md#lc-0567) — Medium, 35 min
60. [LC 621 — Task Scheduler](PROBLEM_BANK.md#lc-0621) — Medium, 35 min
61. [LC 684 — Redundant Connection](PROBLEM_BANK.md#lc-0684) — Medium, 35 min
62. [LC 703 — Kth Largest Element in a Stream](PROBLEM_BANK.md#lc-0703) — Easy, 20 min
63. [LC 704 — Binary Search](PROBLEM_BANK.md#lc-0704) — Easy, 20 min
64. [LC 739 — Daily Temperatures](PROBLEM_BANK.md#lc-0739) — Medium, 35 min
65. [LC 743 — Network Delay Time](PROBLEM_BANK.md#lc-0743) — Medium, 35 min
66. [LC 875 — Koko Eating Bananas](PROBLEM_BANK.md#lc-0875) — Medium, 35 min
67. [LC 981 — Time Based Key-Value Store](PROBLEM_BANK.md#lc-0981) — Medium, 35 min
68. [LC 994 — Rotting Oranges](PROBLEM_BANK.md#lc-0994) — Medium, 35 min
69. [LC 1071 — Greatest Common Divisor of Strings](PROBLEM_BANK.md#lc-1071) — Easy, 20 min
70. [LC 1143 — Longest Common Subsequence](PROBLEM_BANK.md#lc-1143) — Medium, 35 min
71. [LC 1584 — Min Cost to Connect All Points](PROBLEM_BANK.md#lc-1584) — Medium, 35 min
72. [LC 41 — First Missing Positive](PROBLEM_BANK.md#lc-0041) — Hard, 50 min
73. [LC 42 — Trapping Rain Water](PROBLEM_BANK.md#lc-0042) — Hard, 50 min
74. [LC 51 — N-Queens](PROBLEM_BANK.md#lc-0051) — Hard, 50 min
75. [LC 76 — Minimum Window Substring](PROBLEM_BANK.md#lc-0076) — Hard, 50 min
76. [LC 84 — Largest Rectangle in Histogram](PROBLEM_BANK.md#lc-0084) — Hard, 50 min
77. [LC 124 — Binary Tree Maximum Path Sum](PROBLEM_BANK.md#lc-0124) — Hard, 50 min
78. [LC 239 — Sliding Window Maximum](PROBLEM_BANK.md#lc-0239) — Hard, 50 min
79. [LC 295 — Find Median from Data Stream](PROBLEM_BANK.md#lc-0295) — Hard, 50 min
80. [LC 297 — Serialize and Deserialize Binary Tree](PROBLEM_BANK.md#lc-0297) — Hard, 50 min
81. [LC 974 — Subarray Sums Divisible by K](PROBLEM_BANK.md#lc-0974) — Medium, 35 min
82. [LC 1268 — Search Suggestions System](PROBLEM_BANK.md#lc-1268) — Medium, 35 min
83. [LC 49 — Group Anagrams](PROBLEM_BANK.md#lc-0049) — Medium, 35 min
84. [LC 75 — Sort Colors](PROBLEM_BANK.md#lc-0075) — Medium, 35 min
85. [LC 90 — Subsets II](PROBLEM_BANK.md#lc-0090) — Medium, 35 min
86. [LC 92 — Reverse Linked List II](PROBLEM_BANK.md#lc-0092) — Medium, 35 min
87. [LC 105 — Construct Binary Tree from Preorder and Inorder Traversal](PROBLEM_BANK.md#lc-0105) — Medium, 35 min
88. [LC 128 — Longest Consecutive Sequence](PROBLEM_BANK.md#lc-0128) — Medium, 35 min
89. [LC 138 — Copy List with Random Pointer](PROBLEM_BANK.md#lc-0138) — Medium, 35 min
90. [LC 142 — Linked List Cycle II](PROBLEM_BANK.md#lc-0142) — Medium, 35 min
91. [LC 150 — Evaluate Reverse Polish Notation](PROBLEM_BANK.md#lc-0150) — Medium, 35 min
92. [LC 153 — Find Minimum in Rotated Sorted Array](PROBLEM_BANK.md#lc-0153) — Medium, 35 min
93. [LC 169 — Majority Element](PROBLEM_BANK.md#lc-0169) — Easy, 20 min
94. [LC 236 — Lowest Common Ancestor of a Binary Tree](PROBLEM_BANK.md#lc-0236) — Medium, 35 min
95. [LC 242 — Valid Anagram](PROBLEM_BANK.md#lc-0242) — Easy, 20 min
96. [LC 268 — Missing Number](PROBLEM_BANK.md#lc-0268) — Easy, 20 min
97. [LC 283 — Move Zeroes](PROBLEM_BANK.md#lc-0283) — Easy, 20 min
98. [LC 304 — Range Sum Query 2D - Immutable](PROBLEM_BANK.md#lc-0304) — Medium, 35 min
99. [LC 307 — Range Sum Query - Mutable](PROBLEM_BANK.md#lc-0307) — Medium, 35 min
100. [LC 392 — Is Subsequence](PROBLEM_BANK.md#lc-0392) — Easy, 20 min
101. [LC 406 — Queue Reconstruction by Height](PROBLEM_BANK.md#lc-0406) — Medium, 35 min
102. [LC 417 — Pacific Atlantic Water Flow](PROBLEM_BANK.md#lc-0417) — Medium, 35 min
103. [LC 25 — Reverse Nodes in k-Group](PROBLEM_BANK.md#lc-0025) — Hard, 50 min
104. [LC 127 — Word Ladder](PROBLEM_BANK.md#lc-0127) — Hard, 50 min
105. [LC 312 — Burst Balloons](PROBLEM_BANK.md#lc-0312) — Hard, 50 min
106. [LC 1192 — Critical Connections in a Network](PROBLEM_BANK.md#lc-1192) — Hard, 50 min

### Milestone callouts

- [DSA-PRJ-010 — Core data-structure invariant laboratory](PROJECTS.md#dsa-prj-010)
- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)
- [DSA-PRJ-030 — Array and string pattern visualizer](PROJECTS.md#dsa-prj-030)
- [DSA-PRJ-040 — Tree and graph traversal explorer](PROJECTS.md#dsa-prj-040)
- [DSA-PRJ-050 — Shortest-path and routing laboratory](PROJECTS.md#dsa-prj-050)
- [DSA-PRJ-060 — Dynamic-programming state-modeling explorer](PROJECTS.md#dsa-prj-060)
- [DSA-PRJ-070 — Mixed interview simulator and error-analysis dashboard](PROJECTS.md#dsa-prj-070)

### Intentionally deferred

Reference-only digit DP, suffix structures, and sparse-table depth unless role-specific.


<a id="complete-dsa-mastery"></a>
## 7. Complete DSA mastery

<!-- PATH_META {"id":"complete-dsa-mastery","title":"Complete DSA mastery","unit_count":125,"problem_count":121,"concept_minutes":[5850,8380],"problem_minutes":4160,"activities":{"Initial spaced-review program":[2400,3600],"Mixed transfer postmortems and delayed re-solves":[1800,3000],"Mock framing and feedback beyond coding time":[600,900]},"activity_minutes":[4800,7500],"rapid_total_minutes":[14810,20040],"full_unit_hours":[1617,2841],"assumed_or_bridge_prerequisites":[],"project_count":7} -->

**Who it is for:** Long-term mastery across all canonical units, curated problems, evidence, and advanced/reference topics.

**Time assumption:** Long-term mastery; the first rapid survey is 246 h 50 min–334 h, before full labs, projects, and spaced retention.

**Prerequisite policy:** No unit is skipped; projects and later retention cycles remain additional to the unit totals.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 97 h 30 min–139 h 40 min |
| Complete first attempts for 121 selected problems | 69 h 20 min |
| Initial spaced-review program | 40 h–60 h |
| Mixed transfer postmortems and delayed re-solves | 30 h–50 h |
| Mock framing and feedback beyond coding time | 10 h–15 h |
| **Required activities subtotal** | **80 h–125 h** |
| **Rapid path total** | **246 h 50 min–334 h** |
| **Full mastery of included units** | **1617–2841 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (125 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-FND-070 — Interview mathematics: logarithms, sums, counting, and probability](CURRICULUM.md#dsa-fnd-070)
8. [DSA-FND-080 — Testing algorithms with examples, oracles, and properties](CURRICULUM.md#dsa-fnd-080)
9. [DSA-FND-090 — Debugging wrong answers, time limits, and memory failures](CURRICULUM.md#dsa-fnd-090)
10. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
11. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
12. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
13. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
14. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
15. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
16. [DSA-PY-060 — Recursion limits, integers, and Python performance traps](CURRICULUM.md#dsa-py-060)
17. [DSA-PY-070 — Iterators, generators, and streaming inputs](CURRICULUM.md#dsa-py-070)
18. [DSA-PY-080 — pytest, Hypothesis, brute-force oracles, and differential testing](CURRICULUM.md#dsa-py-080)
19. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
20. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
21. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
22. [DSA-SEQ-040 — Opposite-direction two pointers](CURRICULUM.md#dsa-seq-040)
23. [DSA-SEQ-050 — Fixed-size sliding windows](CURRICULUM.md#dsa-seq-050)
24. [DSA-SEQ-060 — Variable-size sliding windows](CURRICULUM.md#dsa-seq-060)
25. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
26. [DSA-SEQ-080 — Suffix aggregates and bidirectional precomputation](CURRICULUM.md#dsa-seq-080)
27. [DSA-SEQ-090 — Difference arrays and range updates](CURRICULUM.md#dsa-seq-090)
28. [DSA-SEQ-100 — Running optima and Kadane-style reasoning](CURRICULUM.md#dsa-seq-100)
29. [DSA-SEQ-110 — Index placement and cyclic-position techniques](CURRICULUM.md#dsa-seq-110)
30. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
31. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
32. [DSA-ORD-020 — Lower bound, upper bound, and first/last true](CURRICULUM.md#dsa-ord-020)
33. [DSA-ORD-030 — Rotated and partially ordered search](CURRICULUM.md#dsa-ord-030)
34. [DSA-ORD-040 — Binary search on a monotonic answer space](CURRICULUM.md#dsa-ord-040)
35. [DSA-ORD-050 — Merge sort, stable merging, and inversion counting](CURRICULUM.md#dsa-ord-050)
36. [DSA-ORD-060 — Partitioning, quicksort concepts, and quickselect](CURRICULUM.md#dsa-ord-060)
37. [DSA-ORD-070 — Counting, bucket, and constraint-driven ordering](CURRICULUM.md#dsa-ord-070)
38. [DSA-LNK-010 — Linked-list representation, sentinels, and ownership](CURRICULUM.md#dsa-lnk-010)
39. [DSA-LNK-020 — Reversal and safe pointer rewiring](CURRICULUM.md#dsa-lnk-020)
40. [DSA-LNK-030 — Fast/slow pointers and cycle detection](CURRICULUM.md#dsa-lnk-030)
41. [DSA-LNK-040 — Merging, intersection, and reference preservation](CURRICULUM.md#dsa-lnk-040)
42. [DSA-LNK-050 — Sublist reversal, reordering, and k-group transformations](CURRICULUM.md#dsa-lnk-050)
43. [DSA-LNK-060 — Linked composite structures and cache design](CURRICULUM.md#dsa-lnk-060)
44. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
45. [DSA-SQH-020 — Matching, nesting, and expression evaluation](CURRICULUM.md#dsa-sqh-020)
46. [DSA-SQH-030 — Monotonic stacks and next-element reasoning](CURRICULUM.md#dsa-sqh-030)
47. [DSA-SQH-040 — Monotonic deques and window extrema](CURRICULUM.md#dsa-sqh-040)
48. [DSA-SQH-050 — Interval sorting, merging, and coverage](CURRICULUM.md#dsa-sqh-050)
49. [DSA-SQH-060 — Sweep-line events and scheduling conflicts](CURRICULUM.md#dsa-sqh-060)
50. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
51. [DSA-SQH-080 — Top-K and streaming selection](CURRICULUM.md#dsa-sqh-080)
52. [DSA-SQH-090 — K-way merge and frontier heaps](CURRICULUM.md#dsa-sqh-090)
53. [DSA-SQH-100 — Two-heaps median, lazy deletion, and dynamic priorities](CURRICULUM.md#dsa-sqh-100)
54. [DSA-REC-010 — Recursive decomposition and decision trees](CURRICULUM.md#dsa-rec-010)
55. [DSA-REC-020 — Subsets and combinations](CURRICULUM.md#dsa-rec-020)
56. [DSA-REC-030 — Permutations and duplicate handling](CURRICULUM.md#dsa-rec-030)
57. [DSA-REC-040 — Constraint propagation and pruning](CURRICULUM.md#dsa-rec-040)
58. [DSA-REC-050 — Grid and path backtracking](CURRICULUM.md#dsa-rec-050)
59. [DSA-REC-060 — Branch ordering and backtracking complexity](CURRICULUM.md#dsa-rec-060)
60. [DSA-REC-070 — Backtracking versus dynamic programming](CURRICULUM.md#dsa-rec-070)
61. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
62. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
63. [DSA-TRE-030 — Breadth-first and level-order traversal](CURRICULUM.md#dsa-tre-030)
64. [DSA-TRE-040 — Path state and root-to-leaf reasoning](CURRICULUM.md#dsa-tre-040)
65. [DSA-TRE-050 — Subtree aggregation and divide-and-conquer](CURRICULUM.md#dsa-tre-050)
66. [DSA-TRE-060 — Binary-search-tree invariants, search, update, and validation](CURRICULUM.md#dsa-tre-060)
67. [DSA-TRE-070 — Lowest common ancestor and ancestry reasoning](CURRICULUM.md#dsa-tre-070)
68. [DSA-TRE-080 — Tree construction and serialization concepts](CURRICULUM.md#dsa-tre-080)
69. [DSA-TRE-090 — Tries and prefix search](CURRICULUM.md#dsa-tre-090)
70. [DSA-TRE-100 — Tree dynamic programming and recursion-depth safety](CURRICULUM.md#dsa-tre-100)
71. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
72. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
73. [DSA-GRA-030 — Depth-first search](CURRICULUM.md#dsa-gra-030)
74. [DSA-GRA-040 — Connected components and grid-as-graph reasoning](CURRICULUM.md#dsa-gra-040)
75. [DSA-GRA-050 — Multi-source BFS](CURRICULUM.md#dsa-gra-050)
76. [DSA-GRA-060 — Bipartite testing](CURRICULUM.md#dsa-gra-060)
77. [DSA-GRA-070 — Cycle detection in directed and undirected graphs](CURRICULUM.md#dsa-gra-070)
78. [DSA-GRA-080 — Topological sorting and dependency order](CURRICULUM.md#dsa-gra-080)
79. [DSA-GRA-090 — Disjoint-set union](CURRICULUM.md#dsa-gra-090)
80. [DSA-GRA-100 — Shortest-path algorithm selection](CURRICULUM.md#dsa-gra-100)
81. [DSA-GRA-110 — Dijkstra and non-negative weighted paths](CURRICULUM.md#dsa-gra-110)
82. [DSA-GRA-120 — Bellman-Ford and all-pairs shortest paths](CURRICULUM.md#dsa-gra-120)
83. [DSA-GRA-130 — Minimum spanning trees](CURRICULUM.md#dsa-gra-130)
84. [DSA-GRA-140 — Zero-one BFS](CURRICULUM.md#dsa-gra-140)
85. [DSA-GRA-150 — Low-link DFS: bridges, articulation points, and strongly connected components](CURRICULUM.md#dsa-gra-150)
86. [DSA-GRD-010 — Greedy-choice recognition and counterexamples](CURRICULUM.md#dsa-grd-010)
87. [DSA-GRD-020 — Exchange arguments and stays-ahead proofs](CURRICULUM.md#dsa-grd-020)
88. [DSA-GRD-030 — Interval scheduling and resource allocation](CURRICULUM.md#dsa-grd-030)
89. [DSA-GRD-040 — Sorting-based greedy and local choices](CURRICULUM.md#dsa-grd-040)
90. [DSA-GRD-050 — Greedy versus dynamic programming](CURRICULUM.md#dsa-grd-050)
91. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
92. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
93. [DSA-DP-030 — One-dimensional sequence DP](CURRICULUM.md#dsa-dp-030)
94. [DSA-DP-040 — Grid and path DP](CURRICULUM.md#dsa-dp-040)
95. [DSA-DP-050 — Knapsack and subset-sum families](CURRICULUM.md#dsa-dp-050)
96. [DSA-DP-060 — Coin change and unbounded-choice DP](CURRICULUM.md#dsa-dp-060)
97. [DSA-DP-070 — Subsequence and sequence-alignment DP](CURRICULUM.md#dsa-dp-070)
98. [DSA-DP-080 — Longest increasing subsequence](CURRICULUM.md#dsa-dp-080)
99. [DSA-DP-090 — String dynamic programming](CURRICULUM.md#dsa-dp-090)
100. [DSA-DP-100 — Interval dynamic programming](CURRICULUM.md#dsa-dp-100)
101. [DSA-DP-110 — State-machine dynamic programming](CURRICULUM.md#dsa-dp-110)
102. [DSA-DP-120 — Tree dynamic programming](CURRICULUM.md#dsa-dp-120)
103. [DSA-DP-130 — Bitmask dynamic programming](CURRICULUM.md#dsa-dp-130)
104. [DSA-DP-140 — Digit DP and advanced state compression](CURRICULUM.md#dsa-dp-140)
105. [DSA-BMS-010 — Bit operations and masks](CURRICULUM.md#dsa-bms-010)
106. [DSA-BMS-020 — XOR invariants and parity reasoning](CURRICULUM.md#dsa-bms-020)
107. [DSA-BMS-030 — Subset enumeration with bitmasks](CURRICULUM.md#dsa-bms-030)
108. [DSA-BMS-040 — GCD, divisibility, and Euclidean reasoning](CURRICULUM.md#dsa-bms-040)
109. [DSA-BMS-050 — Primes and sieve techniques](CURRICULUM.md#dsa-bms-050)
110. [DSA-BMS-060 — Modular arithmetic and fixed-width translation](CURRICULUM.md#dsa-bms-060)
111. [DSA-BMS-070 — Combinatorics and interview probability](CURRICULUM.md#dsa-bms-070)
112. [DSA-BMS-080 — Rolling hash and collision reasoning](CURRICULUM.md#dsa-bms-080)
113. [DSA-BMS-090 — KMP and prefix-function string matching](CURRICULUM.md#dsa-bms-090)
114. [DSA-BMS-100 — Z algorithm and advanced suffix structures](CURRICULUM.md#dsa-bms-100)
115. [DSA-ADV-010 — Fenwick trees](CURRICULUM.md#dsa-adv-010)
116. [DSA-ADV-020 — Segment trees and lazy propagation concepts](CURRICULUM.md#dsa-adv-020)
117. [DSA-ADV-030 — Sparse tables and static range-query trade-offs](CURRICULUM.md#dsa-adv-030)
118. [DSA-ADV-040 — Reservoir sampling, randomized selection, and streaming algorithms](CURRICULUM.md#dsa-adv-040)
119. [DSA-SYN-010 — LRU cache composite design](CURRICULUM.md#dsa-syn-010)
120. [DSA-SYN-020 — Min stack and randomized-set API invariants](CURRICULUM.md#dsa-syn-020)
121. [DSA-SYN-030 — Median stream and time-based key-value storage](CURRICULUM.md#dsa-syn-030)
122. [DSA-SYN-040 — Autocomplete and in-memory indexes](CURRICULUM.md#dsa-syn-040)
123. [DSA-SYN-050 — Task scheduling and composite constraint modeling](CURRICULUM.md#dsa-syn-050)
124. [DSA-SYN-060 — Mixed unlabeled problem solving](CURRICULUM.md#dsa-syn-060)
125. [DSA-SYN-070 — Mock interviews, readiness gates, and error analysis](CURRICULUM.md#dsa-syn-070)

### Selected problem attempts (121)

1. [LC 1 — Two Sum](PROBLEM_BANK.md#lc-0001) — Easy, 20 min
2. [LC 3 — Longest Substring Without Repeating Characters](PROBLEM_BANK.md#lc-0003) — Medium, 35 min
3. [LC 11 — Container With Most Water](PROBLEM_BANK.md#lc-0011) — Medium, 35 min
4. [LC 15 — 3Sum](PROBLEM_BANK.md#lc-0015) — Medium, 35 min
5. [LC 19 — Remove Nth Node From End of List](PROBLEM_BANK.md#lc-0019) — Medium, 35 min
6. [LC 20 — Valid Parentheses](PROBLEM_BANK.md#lc-0020) — Easy, 20 min
7. [LC 21 — Merge Two Sorted Lists](PROBLEM_BANK.md#lc-0021) — Easy, 20 min
8. [LC 23 — Merge k Sorted Lists](PROBLEM_BANK.md#lc-0023) — Hard, 50 min
9. [LC 33 — Search in Rotated Sorted Array](PROBLEM_BANK.md#lc-0033) — Medium, 35 min
10. [LC 34 — Find First and Last Position of Element in Sorted Array](PROBLEM_BANK.md#lc-0034) — Medium, 35 min
11. [LC 39 — Combination Sum](PROBLEM_BANK.md#lc-0039) — Medium, 35 min
12. [LC 46 — Permutations](PROBLEM_BANK.md#lc-0046) — Medium, 35 min
13. [LC 53 — Maximum Subarray](PROBLEM_BANK.md#lc-0053) — Medium, 35 min
14. [LC 54 — Spiral Matrix](PROBLEM_BANK.md#lc-0054) — Medium, 35 min
15. [LC 55 — Jump Game](PROBLEM_BANK.md#lc-0055) — Medium, 35 min
16. [LC 56 — Merge Intervals](PROBLEM_BANK.md#lc-0056) — Medium, 35 min
17. [LC 57 — Insert Interval](PROBLEM_BANK.md#lc-0057) — Medium, 35 min
18. [LC 62 — Unique Paths](PROBLEM_BANK.md#lc-0062) — Medium, 35 min
19. [LC 70 — Climbing Stairs](PROBLEM_BANK.md#lc-0070) — Easy, 20 min
20. [LC 73 — Set Matrix Zeroes](PROBLEM_BANK.md#lc-0073) — Medium, 35 min
21. [LC 78 — Subsets](PROBLEM_BANK.md#lc-0078) — Medium, 35 min
22. [LC 79 — Word Search](PROBLEM_BANK.md#lc-0079) — Medium, 35 min
23. [LC 98 — Validate Binary Search Tree](PROBLEM_BANK.md#lc-0098) — Medium, 35 min
24. [LC 102 — Binary Tree Level Order Traversal](PROBLEM_BANK.md#lc-0102) — Medium, 35 min
25. [LC 104 — Maximum Depth of Binary Tree](PROBLEM_BANK.md#lc-0104) — Easy, 20 min
26. [LC 121 — Best Time to Buy and Sell Stock](PROBLEM_BANK.md#lc-0121) — Easy, 20 min
27. [LC 125 — Valid Palindrome](PROBLEM_BANK.md#lc-0125) — Easy, 20 min
28. [LC 133 — Clone Graph](PROBLEM_BANK.md#lc-0133) — Medium, 35 min
29. [LC 136 — Single Number](PROBLEM_BANK.md#lc-0136) — Easy, 20 min
30. [LC 139 — Word Break](PROBLEM_BANK.md#lc-0139) — Medium, 35 min
31. [LC 141 — Linked List Cycle](PROBLEM_BANK.md#lc-0141) — Easy, 20 min
32. [LC 143 — Reorder List](PROBLEM_BANK.md#lc-0143) — Medium, 35 min
33. [LC 146 — LRU Cache](PROBLEM_BANK.md#lc-0146) — Medium, 35 min
34. [LC 155 — Min Stack](PROBLEM_BANK.md#lc-0155) — Easy, 20 min
35. [LC 167 — Two Sum II - Input Array Is Sorted](PROBLEM_BANK.md#lc-0167) — Medium, 35 min
36. [LC 191 — Number of 1 Bits](PROBLEM_BANK.md#lc-0191) — Easy, 20 min
37. [LC 198 — House Robber](PROBLEM_BANK.md#lc-0198) — Medium, 35 min
38. [LC 200 — Number of Islands](PROBLEM_BANK.md#lc-0200) — Medium, 35 min
39. [LC 204 — Count Primes](PROBLEM_BANK.md#lc-0204) — Medium, 35 min
40. [LC 206 — Reverse Linked List](PROBLEM_BANK.md#lc-0206) — Easy, 20 min
41. [LC 207 — Course Schedule](PROBLEM_BANK.md#lc-0207) — Medium, 35 min
42. [LC 208 — Implement Trie (Prefix Tree)](PROBLEM_BANK.md#lc-0208) — Medium, 35 min
43. [LC 210 — Course Schedule II](PROBLEM_BANK.md#lc-0210) — Medium, 35 min
44. [LC 215 — Kth Largest Element in an Array](PROBLEM_BANK.md#lc-0215) — Medium, 35 min
45. [LC 217 — Contains Duplicate](PROBLEM_BANK.md#lc-0217) — Easy, 20 min
46. [LC 226 — Invert Binary Tree](PROBLEM_BANK.md#lc-0226) — Easy, 20 min
47. [LC 235 — Lowest Common Ancestor of a Binary Search Tree](PROBLEM_BANK.md#lc-0235) — Medium, 35 min
48. [LC 238 — Product of Array Except Self](PROBLEM_BANK.md#lc-0238) — Medium, 35 min
49. [LC 300 — Longest Increasing Subsequence](PROBLEM_BANK.md#lc-0300) — Medium, 35 min
50. [LC 309 — Best Time to Buy and Sell Stock with Cooldown](PROBLEM_BANK.md#lc-0309) — Medium, 35 min
51. [LC 322 — Coin Change](PROBLEM_BANK.md#lc-0322) — Medium, 35 min
52. [LC 347 — Top K Frequent Elements](PROBLEM_BANK.md#lc-0347) — Medium, 35 min
53. [LC 380 — Insert Delete GetRandom O(1)](PROBLEM_BANK.md#lc-0380) — Medium, 35 min
54. [LC 416 — Partition Equal Subset Sum](PROBLEM_BANK.md#lc-0416) — Medium, 35 min
55. [LC 424 — Longest Repeating Character Replacement](PROBLEM_BANK.md#lc-0424) — Medium, 35 min
56. [LC 435 — Non-overlapping Intervals](PROBLEM_BANK.md#lc-0435) — Medium, 35 min
57. [LC 543 — Diameter of Binary Tree](PROBLEM_BANK.md#lc-0543) — Easy, 20 min
58. [LC 560 — Subarray Sum Equals K](PROBLEM_BANK.md#lc-0560) — Medium, 35 min
59. [LC 567 — Permutation in String](PROBLEM_BANK.md#lc-0567) — Medium, 35 min
60. [LC 621 — Task Scheduler](PROBLEM_BANK.md#lc-0621) — Medium, 35 min
61. [LC 684 — Redundant Connection](PROBLEM_BANK.md#lc-0684) — Medium, 35 min
62. [LC 703 — Kth Largest Element in a Stream](PROBLEM_BANK.md#lc-0703) — Easy, 20 min
63. [LC 704 — Binary Search](PROBLEM_BANK.md#lc-0704) — Easy, 20 min
64. [LC 739 — Daily Temperatures](PROBLEM_BANK.md#lc-0739) — Medium, 35 min
65. [LC 743 — Network Delay Time](PROBLEM_BANK.md#lc-0743) — Medium, 35 min
66. [LC 875 — Koko Eating Bananas](PROBLEM_BANK.md#lc-0875) — Medium, 35 min
67. [LC 981 — Time Based Key-Value Store](PROBLEM_BANK.md#lc-0981) — Medium, 35 min
68. [LC 994 — Rotting Oranges](PROBLEM_BANK.md#lc-0994) — Medium, 35 min
69. [LC 1071 — Greatest Common Divisor of Strings](PROBLEM_BANK.md#lc-1071) — Easy, 20 min
70. [LC 1143 — Longest Common Subsequence](PROBLEM_BANK.md#lc-1143) — Medium, 35 min
71. [LC 1584 — Min Cost to Connect All Points](PROBLEM_BANK.md#lc-1584) — Medium, 35 min
72. [LC 41 — First Missing Positive](PROBLEM_BANK.md#lc-0041) — Hard, 50 min
73. [LC 42 — Trapping Rain Water](PROBLEM_BANK.md#lc-0042) — Hard, 50 min
74. [LC 49 — Group Anagrams](PROBLEM_BANK.md#lc-0049) — Medium, 35 min
75. [LC 51 — N-Queens](PROBLEM_BANK.md#lc-0051) — Hard, 50 min
76. [LC 75 — Sort Colors](PROBLEM_BANK.md#lc-0075) — Medium, 35 min
77. [LC 76 — Minimum Window Substring](PROBLEM_BANK.md#lc-0076) — Hard, 50 min
78. [LC 84 — Largest Rectangle in Histogram](PROBLEM_BANK.md#lc-0084) — Hard, 50 min
79. [LC 90 — Subsets II](PROBLEM_BANK.md#lc-0090) — Medium, 35 min
80. [LC 92 — Reverse Linked List II](PROBLEM_BANK.md#lc-0092) — Medium, 35 min
81. [LC 105 — Construct Binary Tree from Preorder and Inorder Traversal](PROBLEM_BANK.md#lc-0105) — Medium, 35 min
82. [LC 124 — Binary Tree Maximum Path Sum](PROBLEM_BANK.md#lc-0124) — Hard, 50 min
83. [LC 128 — Longest Consecutive Sequence](PROBLEM_BANK.md#lc-0128) — Medium, 35 min
84. [LC 138 — Copy List with Random Pointer](PROBLEM_BANK.md#lc-0138) — Medium, 35 min
85. [LC 142 — Linked List Cycle II](PROBLEM_BANK.md#lc-0142) — Medium, 35 min
86. [LC 150 — Evaluate Reverse Polish Notation](PROBLEM_BANK.md#lc-0150) — Medium, 35 min
87. [LC 153 — Find Minimum in Rotated Sorted Array](PROBLEM_BANK.md#lc-0153) — Medium, 35 min
88. [LC 169 — Majority Element](PROBLEM_BANK.md#lc-0169) — Easy, 20 min
89. [LC 236 — Lowest Common Ancestor of a Binary Tree](PROBLEM_BANK.md#lc-0236) — Medium, 35 min
90. [LC 239 — Sliding Window Maximum](PROBLEM_BANK.md#lc-0239) — Hard, 50 min
91. [LC 242 — Valid Anagram](PROBLEM_BANK.md#lc-0242) — Easy, 20 min
92. [LC 268 — Missing Number](PROBLEM_BANK.md#lc-0268) — Easy, 20 min
93. [LC 283 — Move Zeroes](PROBLEM_BANK.md#lc-0283) — Easy, 20 min
94. [LC 295 — Find Median from Data Stream](PROBLEM_BANK.md#lc-0295) — Hard, 50 min
95. [LC 297 — Serialize and Deserialize Binary Tree](PROBLEM_BANK.md#lc-0297) — Hard, 50 min
96. [LC 304 — Range Sum Query 2D - Immutable](PROBLEM_BANK.md#lc-0304) — Medium, 35 min
97. [LC 307 — Range Sum Query - Mutable](PROBLEM_BANK.md#lc-0307) — Medium, 35 min
98. [LC 392 — Is Subsequence](PROBLEM_BANK.md#lc-0392) — Easy, 20 min
99. [LC 406 — Queue Reconstruction by Height](PROBLEM_BANK.md#lc-0406) — Medium, 35 min
100. [LC 417 — Pacific Atlantic Water Flow](PROBLEM_BANK.md#lc-0417) — Medium, 35 min
101. [LC 525 — Contiguous Array](PROBLEM_BANK.md#lc-0525) — Medium, 35 min
102. [LC 547 — Number of Provinces](PROBLEM_BANK.md#lc-0547) — Medium, 35 min
103. [LC 647 — Palindromic Substrings](PROBLEM_BANK.md#lc-0647) — Medium, 35 min
104. [LC 733 — Flood Fill](PROBLEM_BANK.md#lc-0733) — Easy, 20 min
105. [LC 785 — Is Graph Bipartite?](PROBLEM_BANK.md#lc-0785) — Medium, 35 min
106. [LC 912 — Sort an Array](PROBLEM_BANK.md#lc-0912) — Medium, 35 min
107. [LC 973 — K Closest Points to Origin](PROBLEM_BANK.md#lc-0973) — Medium, 35 min
108. [LC 974 — Subarray Sums Divisible by K](PROBLEM_BANK.md#lc-0974) — Medium, 35 min
109. [LC 1011 — Capacity To Ship Packages Within D Days](PROBLEM_BANK.md#lc-1011) — Medium, 35 min
110. [LC 1094 — Car Pooling](PROBLEM_BANK.md#lc-1094) — Medium, 35 min
111. [LC 1268 — Search Suggestions System](PROBLEM_BANK.md#lc-1268) — Medium, 35 min
112. [LC 2406 — Divide Intervals Into Minimum Number of Groups](PROBLEM_BANK.md#lc-2406) — Medium, 35 min
113. [LC 25 — Reverse Nodes in k-Group](PROBLEM_BANK.md#lc-0025) — Hard, 50 min
114. [LC 127 — Word Ladder](PROBLEM_BANK.md#lc-0127) — Hard, 50 min
115. [LC 212 — Word Search II](PROBLEM_BANK.md#lc-0212) — Hard, 50 min
116. [LC 218 — The Skyline Problem](PROBLEM_BANK.md#lc-0218) — Hard, 50 min
117. [LC 312 — Burst Balloons](PROBLEM_BANK.md#lc-0312) — Hard, 50 min
118. [LC 847 — Shortest Path Visiting All Nodes](PROBLEM_BANK.md#lc-0847) — Hard, 50 min
119. [LC 1192 — Critical Connections in a Network](PROBLEM_BANK.md#lc-1192) — Hard, 50 min
120. [LC 1368 — Minimum Cost to Make at Least One Valid Path in a Grid](PROBLEM_BANK.md#lc-1368) — Hard, 50 min
121. [LC 1392 — Longest Happy Prefix](PROBLEM_BANK.md#lc-1392) — Hard, 50 min

### Milestone callouts

- [DSA-PRJ-010 — Core data-structure invariant laboratory](PROJECTS.md#dsa-prj-010)
- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)
- [DSA-PRJ-030 — Array and string pattern visualizer](PROJECTS.md#dsa-prj-030)
- [DSA-PRJ-040 — Tree and graph traversal explorer](PROJECTS.md#dsa-prj-040)
- [DSA-PRJ-050 — Shortest-path and routing laboratory](PROJECTS.md#dsa-prj-050)
- [DSA-PRJ-060 — Dynamic-programming state-modeling explorer](PROJECTS.md#dsa-prj-060)
- [DSA-PRJ-070 — Mixed interview simulator and error-analysis dashboard](PROJECTS.md#dsa-prj-070)

### Intentionally deferred

Nothing canonical. External competitive-programming topics remain outside this repository unless later justified.


<a id="arrays-strings-repair"></a>
## 8. Arrays and strings repair path

<!-- PATH_META {"id":"arrays-strings-repair","title":"Arrays and strings repair path","unit_count":44,"problem_count":23,"concept_minutes":[1880,2720],"problem_minutes":775,"activities":{"Closed-book traces":[300,420],"Pattern comparisons and postmortems":[240,360],"Mock framing and feedback beyond coding time":[45,90],"Visualizer checkpoint":[120,180]},"activity_minutes":[705,1050],"rapid_total_minutes":[3360,4545],"full_unit_hours":[492,876],"assumed_or_bridge_prerequisites":[],"project_count":2} -->

**Who it is for:** Rahul when array boundaries, hashing, windows, prefixes, mutation, or string costs remain unreliable.

**Time assumption:** Focused repair path; budget the calculated 56 h–75 h 45 min rather than forcing an arbitrary calendar.

**Prerequisite policy:** Tree, graph, and DP units are not required. BMS string units require bridges when selected before their prerequisites.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 31 h 20 min–45 h 20 min |
| Complete first attempts for 23 selected problems | 12 h 55 min |
| Closed-book traces | 5 h–7 h |
| Pattern comparisons and postmortems | 4 h–6 h |
| Mock framing and feedback beyond coding time | 45 min–1 h 30 min |
| Visualizer checkpoint | 2 h–3 h |
| **Required activities subtotal** | **11 h 45 min–17 h 30 min** |
| **Rapid path total** | **56 h–75 h 45 min** |
| **Full mastery of included units** | **492–876 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (44 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-FND-070 — Interview mathematics: logarithms, sums, counting, and probability](CURRICULUM.md#dsa-fnd-070)
8. [DSA-FND-080 — Testing algorithms with examples, oracles, and properties](CURRICULUM.md#dsa-fnd-080)
9. [DSA-FND-090 — Debugging wrong answers, time limits, and memory failures](CURRICULUM.md#dsa-fnd-090)
10. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
11. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
12. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
13. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
14. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
15. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
16. [DSA-PY-060 — Recursion limits, integers, and Python performance traps](CURRICULUM.md#dsa-py-060)
17. [DSA-PY-070 — Iterators, generators, and streaming inputs](CURRICULUM.md#dsa-py-070)
18. [DSA-PY-080 — pytest, Hypothesis, brute-force oracles, and differential testing](CURRICULUM.md#dsa-py-080)
19. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
20. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
21. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
22. [DSA-SEQ-040 — Opposite-direction two pointers](CURRICULUM.md#dsa-seq-040)
23. [DSA-SEQ-050 — Fixed-size sliding windows](CURRICULUM.md#dsa-seq-050)
24. [DSA-SEQ-060 — Variable-size sliding windows](CURRICULUM.md#dsa-seq-060)
25. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
26. [DSA-SEQ-080 — Suffix aggregates and bidirectional precomputation](CURRICULUM.md#dsa-seq-080)
27. [DSA-SEQ-090 — Difference arrays and range updates](CURRICULUM.md#dsa-seq-090)
28. [DSA-SEQ-100 — Running optima and Kadane-style reasoning](CURRICULUM.md#dsa-seq-100)
29. [DSA-SEQ-110 — Index placement and cyclic-position techniques](CURRICULUM.md#dsa-seq-110)
30. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
31. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
32. [DSA-ORD-020 — Lower bound, upper bound, and first/last true](CURRICULUM.md#dsa-ord-020)
33. [DSA-ORD-030 — Rotated and partially ordered search](CURRICULUM.md#dsa-ord-030)
34. [DSA-ORD-040 — Binary search on a monotonic answer space](CURRICULUM.md#dsa-ord-040)
35. [DSA-ORD-050 — Merge sort, stable merging, and inversion counting](CURRICULUM.md#dsa-ord-050)
36. [DSA-ORD-060 — Partitioning, quicksort concepts, and quickselect](CURRICULUM.md#dsa-ord-060)
37. [DSA-ORD-070 — Counting, bucket, and constraint-driven ordering](CURRICULUM.md#dsa-ord-070)
38. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
39. [DSA-SQH-030 — Monotonic stacks and next-element reasoning](CURRICULUM.md#dsa-sqh-030)
40. [DSA-SQH-040 — Monotonic deques and window extrema](CURRICULUM.md#dsa-sqh-040)
41. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
42. [DSA-BMS-060 — Modular arithmetic and fixed-width translation](CURRICULUM.md#dsa-bms-060)
43. [DSA-BMS-080 — Rolling hash and collision reasoning](CURRICULUM.md#dsa-bms-080)
44. [DSA-BMS-090 — KMP and prefix-function string matching](CURRICULUM.md#dsa-bms-090)

### Selected problem attempts (23)

1. [LC 1 — Two Sum](PROBLEM_BANK.md#lc-0001) — Easy, 20 min
2. [LC 217 — Contains Duplicate](PROBLEM_BANK.md#lc-0217) — Easy, 20 min
3. [LC 121 — Best Time to Buy and Sell Stock](PROBLEM_BANK.md#lc-0121) — Easy, 20 min
4. [LC 238 — Product of Array Except Self](PROBLEM_BANK.md#lc-0238) — Medium, 35 min
5. [LC 53 — Maximum Subarray](PROBLEM_BANK.md#lc-0053) — Medium, 35 min
6. [LC 125 — Valid Palindrome](PROBLEM_BANK.md#lc-0125) — Easy, 20 min
7. [LC 167 — Two Sum II - Input Array Is Sorted](PROBLEM_BANK.md#lc-0167) — Medium, 35 min
8. [LC 15 — 3Sum](PROBLEM_BANK.md#lc-0015) — Medium, 35 min
9. [LC 11 — Container With Most Water](PROBLEM_BANK.md#lc-0011) — Medium, 35 min
10. [LC 3 — Longest Substring Without Repeating Characters](PROBLEM_BANK.md#lc-0003) — Medium, 35 min
11. [LC 424 — Longest Repeating Character Replacement](PROBLEM_BANK.md#lc-0424) — Medium, 35 min
12. [LC 567 — Permutation in String](PROBLEM_BANK.md#lc-0567) — Medium, 35 min
13. [LC 560 — Subarray Sum Equals K](PROBLEM_BANK.md#lc-0560) — Medium, 35 min
14. [LC 73 — Set Matrix Zeroes](PROBLEM_BANK.md#lc-0073) — Medium, 35 min
15. [LC 54 — Spiral Matrix](PROBLEM_BANK.md#lc-0054) — Medium, 35 min
16. [LC 704 — Binary Search](PROBLEM_BANK.md#lc-0704) — Easy, 20 min
17. [LC 34 — Find First and Last Position of Element in Sorted Array](PROBLEM_BANK.md#lc-0034) — Medium, 35 min
18. [LC 33 — Search in Rotated Sorted Array](PROBLEM_BANK.md#lc-0033) — Medium, 35 min
19. [LC 875 — Koko Eating Bananas](PROBLEM_BANK.md#lc-0875) — Medium, 35 min
20. [LC 215 — Kth Largest Element in an Array](PROBLEM_BANK.md#lc-0215) — Medium, 35 min
21. [LC 41 — First Missing Positive](PROBLEM_BANK.md#lc-0041) — Hard, 50 min
22. [LC 42 — Trapping Rain Water](PROBLEM_BANK.md#lc-0042) — Hard, 50 min
23. [LC 76 — Minimum Window Substring](PROBLEM_BANK.md#lc-0076) — Hard, 50 min

### Milestone callouts

- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)
- [DSA-PRJ-030 — Array and string pattern visualizer](PROJECTS.md#dsa-prj-030)

### Intentionally deferred

Non-sequence domains except supporting complexity, Python, monotonic, and string-matching concepts.


<a id="trees-graphs-repair"></a>
## 9. Trees and graphs repair path

<!-- PATH_META {"id":"trees-graphs-repair","title":"Trees and graphs repair path","unit_count":47,"problem_count":17,"concept_minutes":[2050,2960],"problem_minutes":580,"activities":{"Visual reconstruction":[360,480],"Algorithm-selection comparisons and postmortems":[300,420],"Mock framing and feedback beyond coding time":[90,135],"Explorer checkpoint":[180,300]},"activity_minutes":[930,1335],"rapid_total_minutes":[3560,4875],"full_unit_hours":[543,963],"assumed_or_bridge_prerequisites":[],"project_count":2} -->

**Who it is for:** A learner who loses traversal state, mishandles visited sets, or cannot choose BFS, DFS, DSU, or shortest paths.

**Time assumption:** Focused repair path; budget the calculated 59 h 20 min–81 h 15 min rather than forcing an arbitrary calendar.

**Prerequisite policy:** Core recursion, stacks, queues, hashing, heaps, and complexity prerequisites are included through closure.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 34 h 10 min–49 h 20 min |
| Complete first attempts for 17 selected problems | 9 h 40 min |
| Visual reconstruction | 6 h–8 h |
| Algorithm-selection comparisons and postmortems | 5 h–7 h |
| Mock framing and feedback beyond coding time | 1 h 30 min–2 h 15 min |
| Explorer checkpoint | 3 h–5 h |
| **Required activities subtotal** | **15 h 30 min–22 h 15 min** |
| **Rapid path total** | **59 h 20 min–81 h 15 min** |
| **Full mastery of included units** | **543–963 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (47 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
8. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
9. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
10. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
11. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
12. [DSA-PY-060 — Recursion limits, integers, and Python performance traps](CURRICULUM.md#dsa-py-060)
13. [DSA-PY-070 — Iterators, generators, and streaming inputs](CURRICULUM.md#dsa-py-070)
14. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
15. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
16. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
17. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
18. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
19. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
20. [DSA-REC-010 — Recursive decomposition and decision trees](CURRICULUM.md#dsa-rec-010)
21. [DSA-REC-040 — Constraint propagation and pruning](CURRICULUM.md#dsa-rec-040)
22. [DSA-REC-070 — Backtracking versus dynamic programming](CURRICULUM.md#dsa-rec-070)
23. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
24. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
25. [DSA-TRE-030 — Breadth-first and level-order traversal](CURRICULUM.md#dsa-tre-030)
26. [DSA-TRE-040 — Path state and root-to-leaf reasoning](CURRICULUM.md#dsa-tre-040)
27. [DSA-TRE-050 — Subtree aggregation and divide-and-conquer](CURRICULUM.md#dsa-tre-050)
28. [DSA-TRE-060 — Binary-search-tree invariants, search, update, and validation](CURRICULUM.md#dsa-tre-060)
29. [DSA-TRE-070 — Lowest common ancestor and ancestry reasoning](CURRICULUM.md#dsa-tre-070)
30. [DSA-TRE-080 — Tree construction and serialization concepts](CURRICULUM.md#dsa-tre-080)
31. [DSA-TRE-090 — Tries and prefix search](CURRICULUM.md#dsa-tre-090)
32. [DSA-TRE-100 — Tree dynamic programming and recursion-depth safety](CURRICULUM.md#dsa-tre-100)
33. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
34. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
35. [DSA-GRA-030 — Depth-first search](CURRICULUM.md#dsa-gra-030)
36. [DSA-GRA-040 — Connected components and grid-as-graph reasoning](CURRICULUM.md#dsa-gra-040)
37. [DSA-GRA-050 — Multi-source BFS](CURRICULUM.md#dsa-gra-050)
38. [DSA-GRA-060 — Bipartite testing](CURRICULUM.md#dsa-gra-060)
39. [DSA-GRA-070 — Cycle detection in directed and undirected graphs](CURRICULUM.md#dsa-gra-070)
40. [DSA-GRA-080 — Topological sorting and dependency order](CURRICULUM.md#dsa-gra-080)
41. [DSA-GRA-090 — Disjoint-set union](CURRICULUM.md#dsa-gra-090)
42. [DSA-GRA-100 — Shortest-path algorithm selection](CURRICULUM.md#dsa-gra-100)
43. [DSA-GRA-110 — Dijkstra and non-negative weighted paths](CURRICULUM.md#dsa-gra-110)
44. [DSA-GRA-120 — Bellman-Ford and all-pairs shortest paths](CURRICULUM.md#dsa-gra-120)
45. [DSA-GRA-130 — Minimum spanning trees](CURRICULUM.md#dsa-gra-130)
46. [DSA-GRA-140 — Zero-one BFS](CURRICULUM.md#dsa-gra-140)
47. [DSA-GRA-150 — Low-link DFS: bridges, articulation points, and strongly connected components](CURRICULUM.md#dsa-gra-150)

### Selected problem attempts (17)

1. [LC 226 — Invert Binary Tree](PROBLEM_BANK.md#lc-0226) — Easy, 20 min
2. [LC 104 — Maximum Depth of Binary Tree](PROBLEM_BANK.md#lc-0104) — Easy, 20 min
3. [LC 102 — Binary Tree Level Order Traversal](PROBLEM_BANK.md#lc-0102) — Medium, 35 min
4. [LC 543 — Diameter of Binary Tree](PROBLEM_BANK.md#lc-0543) — Easy, 20 min
5. [LC 98 — Validate Binary Search Tree](PROBLEM_BANK.md#lc-0098) — Medium, 35 min
6. [LC 235 — Lowest Common Ancestor of a Binary Search Tree](PROBLEM_BANK.md#lc-0235) — Medium, 35 min
7. [LC 208 — Implement Trie (Prefix Tree)](PROBLEM_BANK.md#lc-0208) — Medium, 35 min
8. [LC 200 — Number of Islands](PROBLEM_BANK.md#lc-0200) — Medium, 35 min
9. [LC 133 — Clone Graph](PROBLEM_BANK.md#lc-0133) — Medium, 35 min
10. [LC 994 — Rotting Oranges](PROBLEM_BANK.md#lc-0994) — Medium, 35 min
11. [LC 207 — Course Schedule](PROBLEM_BANK.md#lc-0207) — Medium, 35 min
12. [LC 210 — Course Schedule II](PROBLEM_BANK.md#lc-0210) — Medium, 35 min
13. [LC 684 — Redundant Connection](PROBLEM_BANK.md#lc-0684) — Medium, 35 min
14. [LC 743 — Network Delay Time](PROBLEM_BANK.md#lc-0743) — Medium, 35 min
15. [LC 1584 — Min Cost to Connect All Points](PROBLEM_BANK.md#lc-1584) — Medium, 35 min
16. [LC 124 — Binary Tree Maximum Path Sum](PROBLEM_BANK.md#lc-0124) — Hard, 50 min
17. [LC 297 — Serialize and Deserialize Binary Tree](PROBLEM_BANK.md#lc-0297) — Hard, 50 min

### Milestone callouts

- [DSA-PRJ-040 — Tree and graph traversal explorer](PROJECTS.md#dsa-prj-040)
- [DSA-PRJ-050 — Shortest-path and routing laboratory](PROJECTS.md#dsa-prj-050)

### Intentionally deferred

Unrelated sequence, interval, math, and DP families except tree DP.


<a id="dynamic-programming-repair"></a>
## 10. Dynamic-programming repair path

<!-- PATH_META {"id":"dynamic-programming-repair","title":"Dynamic-programming repair path","unit_count":37,"problem_count":9,"concept_minutes":[1735,2485],"problem_minutes":300,"activities":{"State-definition drills":[360,540],"Memoization/tabulation comparisons and postmortems":[240,360],"Mock framing and feedback beyond coding time":[45,90],"DP explorer checkpoint":[180,300]},"activity_minutes":[825,1290],"rapid_total_minutes":[2860,4075],"full_unit_hours":[480,843],"assumed_or_bridge_prerequisites":[],"project_count":2} -->

**Who it is for:** A learner who memorizes recurrences but cannot define state, transition, order, or correctness.

**Time assumption:** Focused repair path; budget the calculated 47 h 40 min–67 h 55 min rather than forcing an arbitrary calendar.

**Prerequisite policy:** Core recursion, complexity, arrays, trees, and bit prerequisites are included through closure.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 28 h 55 min–41 h 25 min |
| Complete first attempts for 9 selected problems | 5 h |
| State-definition drills | 6 h–9 h |
| Memoization/tabulation comparisons and postmortems | 4 h–6 h |
| Mock framing and feedback beyond coding time | 45 min–1 h 30 min |
| DP explorer checkpoint | 3 h–5 h |
| **Required activities subtotal** | **13 h 45 min–21 h 30 min** |
| **Rapid path total** | **47 h 40 min–67 h 55 min** |
| **Full mastery of included units** | **480–843 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (37 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
6. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
7. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
8. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
9. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
10. [DSA-PY-060 — Recursion limits, integers, and Python performance traps](CURRICULUM.md#dsa-py-060)
11. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
12. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
13. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
14. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
15. [DSA-ORD-020 — Lower bound, upper bound, and first/last true](CURRICULUM.md#dsa-ord-020)
16. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
17. [DSA-REC-010 — Recursive decomposition and decision trees](CURRICULUM.md#dsa-rec-010)
18. [DSA-REC-040 — Constraint propagation and pruning](CURRICULUM.md#dsa-rec-040)
19. [DSA-REC-070 — Backtracking versus dynamic programming](CURRICULUM.md#dsa-rec-070)
20. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
21. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
22. [DSA-TRE-050 — Subtree aggregation and divide-and-conquer](CURRICULUM.md#dsa-tre-050)
23. [DSA-TRE-100 — Tree dynamic programming and recursion-depth safety](CURRICULUM.md#dsa-tre-100)
24. [DSA-GRD-010 — Greedy-choice recognition and counterexamples](CURRICULUM.md#dsa-grd-010)
25. [DSA-GRD-050 — Greedy versus dynamic programming](CURRICULUM.md#dsa-grd-050)
26. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
27. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
28. [DSA-DP-030 — One-dimensional sequence DP](CURRICULUM.md#dsa-dp-030)
29. [DSA-DP-040 — Grid and path DP](CURRICULUM.md#dsa-dp-040)
30. [DSA-DP-050 — Knapsack and subset-sum families](CURRICULUM.md#dsa-dp-050)
31. [DSA-DP-060 — Coin change and unbounded-choice DP](CURRICULUM.md#dsa-dp-060)
32. [DSA-DP-070 — Subsequence and sequence-alignment DP](CURRICULUM.md#dsa-dp-070)
33. [DSA-DP-080 — Longest increasing subsequence](CURRICULUM.md#dsa-dp-080)
34. [DSA-DP-090 — String dynamic programming](CURRICULUM.md#dsa-dp-090)
35. [DSA-DP-110 — State-machine dynamic programming](CURRICULUM.md#dsa-dp-110)
36. [DSA-DP-120 — Tree dynamic programming](CURRICULUM.md#dsa-dp-120)
37. [DSA-DP-130 — Bitmask dynamic programming](CURRICULUM.md#dsa-dp-130)

### Selected problem attempts (9)

1. [LC 70 — Climbing Stairs](PROBLEM_BANK.md#lc-0070) — Easy, 20 min
2. [LC 198 — House Robber](PROBLEM_BANK.md#lc-0198) — Medium, 35 min
3. [LC 322 — Coin Change](PROBLEM_BANK.md#lc-0322) — Medium, 35 min
4. [LC 416 — Partition Equal Subset Sum](PROBLEM_BANK.md#lc-0416) — Medium, 35 min
5. [LC 62 — Unique Paths](PROBLEM_BANK.md#lc-0062) — Medium, 35 min
6. [LC 300 — Longest Increasing Subsequence](PROBLEM_BANK.md#lc-0300) — Medium, 35 min
7. [LC 1143 — Longest Common Subsequence](PROBLEM_BANK.md#lc-1143) — Medium, 35 min
8. [LC 139 — Word Break](PROBLEM_BANK.md#lc-0139) — Medium, 35 min
9. [LC 309 — Best Time to Buy and Sell Stock with Cooldown](PROBLEM_BANK.md#lc-0309) — Medium, 35 min

### Milestone callouts

- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)
- [DSA-PRJ-060 — Dynamic-programming state-modeling explorer](PROJECTS.md#dsa-prj-060)

### Intentionally deferred

Digit DP unless role-specific; advanced optimization techniques outside the canonical catalog.


<a id="senior-python-backend-interview"></a>
## 11. Senior Python/backend coding-interview path

<!-- PATH_META {"id":"senior-python-backend-interview","title":"Senior Python/backend coding-interview path","unit_count":69,"problem_count":23,"concept_minutes":[3175,4560],"problem_minutes":805,"activities":{"Python-cost drills":[180,240],"Design comparisons and postmortems":[240,360],"Mock framing and feedback beyond coding time":[135,180],"Error-log update":[90,120]},"activity_minutes":[645,900],"rapid_total_minutes":[4625,6265],"full_unit_hours":[867,1524],"assumed_or_bridge_prerequisites":[],"project_count":2} -->

**Who it is for:** An experienced Python backend engineer preparing for coding rounds that emphasize implementation judgment and Python costs.

**Time assumption:** Focused repair path; budget the calculated 77 h 5 min–104 h 25 min rather than forcing an arbitrary calendar.

**Prerequisite policy:** Professional Python experience is assumed; algorithmic prerequisites are included through closure.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 52 h 55 min–76 h |
| Complete first attempts for 23 selected problems | 13 h 25 min |
| Python-cost drills | 3 h–4 h |
| Design comparisons and postmortems | 4 h–6 h |
| Mock framing and feedback beyond coding time | 2 h 15 min–3 h |
| Error-log update | 1 h 30 min–2 h |
| **Required activities subtotal** | **10 h 45 min–15 h** |
| **Rapid path total** | **77 h 5 min–104 h 25 min** |
| **Full mastery of included units** | **867–1524 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (69 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-050 — Amortized, aggregate, output-sensitive, and query analysis](CURRICULUM.md#dsa-fnd-050)
6. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
7. [DSA-FND-080 — Testing algorithms with examples, oracles, and properties](CURRICULUM.md#dsa-fnd-080)
8. [DSA-FND-090 — Debugging wrong answers, time limits, and memory failures](CURRICULUM.md#dsa-fnd-090)
9. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
10. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
11. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
12. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
13. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
14. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
15. [DSA-PY-080 — pytest, Hypothesis, brute-force oracles, and differential testing](CURRICULUM.md#dsa-py-080)
16. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
17. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
18. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
19. [DSA-SEQ-050 — Fixed-size sliding windows](CURRICULUM.md#dsa-seq-050)
20. [DSA-SEQ-060 — Variable-size sliding windows](CURRICULUM.md#dsa-seq-060)
21. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
22. [DSA-SEQ-080 — Suffix aggregates and bidirectional precomputation](CURRICULUM.md#dsa-seq-080)
23. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
24. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
25. [DSA-ORD-020 — Lower bound, upper bound, and first/last true](CURRICULUM.md#dsa-ord-020)
26. [DSA-ORD-040 — Binary search on a monotonic answer space](CURRICULUM.md#dsa-ord-040)
27. [DSA-LNK-010 — Linked-list representation, sentinels, and ownership](CURRICULUM.md#dsa-lnk-010)
28. [DSA-LNK-020 — Reversal and safe pointer rewiring](CURRICULUM.md#dsa-lnk-020)
29. [DSA-LNK-040 — Merging, intersection, and reference preservation](CURRICULUM.md#dsa-lnk-040)
30. [DSA-LNK-060 — Linked composite structures and cache design](CURRICULUM.md#dsa-lnk-060)
31. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
32. [DSA-SQH-030 — Monotonic stacks and next-element reasoning](CURRICULUM.md#dsa-sqh-030)
33. [DSA-SQH-050 — Interval sorting, merging, and coverage](CURRICULUM.md#dsa-sqh-050)
34. [DSA-SQH-070 — Heap and priority-queue fundamentals](CURRICULUM.md#dsa-sqh-070)
35. [DSA-SQH-080 — Top-K and streaming selection](CURRICULUM.md#dsa-sqh-080)
36. [DSA-SQH-090 — K-way merge and frontier heaps](CURRICULUM.md#dsa-sqh-090)
37. [DSA-SQH-100 — Two-heaps median, lazy deletion, and dynamic priorities](CURRICULUM.md#dsa-sqh-100)
38. [DSA-REC-010 — Recursive decomposition and decision trees](CURRICULUM.md#dsa-rec-010)
39. [DSA-REC-040 — Constraint propagation and pruning](CURRICULUM.md#dsa-rec-040)
40. [DSA-REC-070 — Backtracking versus dynamic programming](CURRICULUM.md#dsa-rec-070)
41. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
42. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
43. [DSA-TRE-090 — Tries and prefix search](CURRICULUM.md#dsa-tre-090)
44. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
45. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
46. [DSA-GRA-030 — Depth-first search](CURRICULUM.md#dsa-gra-030)
47. [DSA-GRA-040 — Connected components and grid-as-graph reasoning](CURRICULUM.md#dsa-gra-040)
48. [DSA-GRA-070 — Cycle detection in directed and undirected graphs](CURRICULUM.md#dsa-gra-070)
49. [DSA-GRA-080 — Topological sorting and dependency order](CURRICULUM.md#dsa-gra-080)
50. [DSA-GRA-090 — Disjoint-set union](CURRICULUM.md#dsa-gra-090)
51. [DSA-GRA-100 — Shortest-path algorithm selection](CURRICULUM.md#dsa-gra-100)
52. [DSA-GRA-110 — Dijkstra and non-negative weighted paths](CURRICULUM.md#dsa-gra-110)
53. [DSA-GRA-130 — Minimum spanning trees](CURRICULUM.md#dsa-gra-130)
54. [DSA-GRD-010 — Greedy-choice recognition and counterexamples](CURRICULUM.md#dsa-grd-010)
55. [DSA-GRD-020 — Exchange arguments and stays-ahead proofs](CURRICULUM.md#dsa-grd-020)
56. [DSA-GRD-040 — Sorting-based greedy and local choices](CURRICULUM.md#dsa-grd-040)
57. [DSA-GRD-050 — Greedy versus dynamic programming](CURRICULUM.md#dsa-grd-050)
58. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
59. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
60. [DSA-DP-030 — One-dimensional sequence DP](CURRICULUM.md#dsa-dp-030)
61. [DSA-DP-050 — Knapsack and subset-sum families](CURRICULUM.md#dsa-dp-050)
62. [DSA-DP-080 — Longest increasing subsequence](CURRICULUM.md#dsa-dp-080)
63. [DSA-SYN-010 — LRU cache composite design](CURRICULUM.md#dsa-syn-010)
64. [DSA-SYN-020 — Min stack and randomized-set API invariants](CURRICULUM.md#dsa-syn-020)
65. [DSA-SYN-030 — Median stream and time-based key-value storage](CURRICULUM.md#dsa-syn-030)
66. [DSA-SYN-040 — Autocomplete and in-memory indexes](CURRICULUM.md#dsa-syn-040)
67. [DSA-SYN-050 — Task scheduling and composite constraint modeling](CURRICULUM.md#dsa-syn-050)
68. [DSA-SYN-060 — Mixed unlabeled problem solving](CURRICULUM.md#dsa-syn-060)
69. [DSA-SYN-070 — Mock interviews, readiness gates, and error analysis](CURRICULUM.md#dsa-syn-070)

### Selected problem attempts (23)

1. [LC 1 — Two Sum](PROBLEM_BANK.md#lc-0001) — Easy, 20 min
2. [LC 238 — Product of Array Except Self](PROBLEM_BANK.md#lc-0238) — Medium, 35 min
3. [LC 3 — Longest Substring Without Repeating Characters](PROBLEM_BANK.md#lc-0003) — Medium, 35 min
4. [LC 560 — Subarray Sum Equals K](PROBLEM_BANK.md#lc-0560) — Medium, 35 min
5. [LC 875 — Koko Eating Bananas](PROBLEM_BANK.md#lc-0875) — Medium, 35 min
6. [LC 146 — LRU Cache](PROBLEM_BANK.md#lc-0146) — Medium, 35 min
7. [LC 739 — Daily Temperatures](PROBLEM_BANK.md#lc-0739) — Medium, 35 min
8. [LC 56 — Merge Intervals](PROBLEM_BANK.md#lc-0056) — Medium, 35 min
9. [LC 347 — Top K Frequent Elements](PROBLEM_BANK.md#lc-0347) — Medium, 35 min
10. [LC 23 — Merge k Sorted Lists](PROBLEM_BANK.md#lc-0023) — Hard, 50 min
11. [LC 295 — Find Median from Data Stream](PROBLEM_BANK.md#lc-0295) — Hard, 50 min
12. [LC 208 — Implement Trie (Prefix Tree)](PROBLEM_BANK.md#lc-0208) — Medium, 35 min
13. [LC 200 — Number of Islands](PROBLEM_BANK.md#lc-0200) — Medium, 35 min
14. [LC 207 — Course Schedule](PROBLEM_BANK.md#lc-0207) — Medium, 35 min
15. [LC 743 — Network Delay Time](PROBLEM_BANK.md#lc-0743) — Medium, 35 min
16. [LC 1584 — Min Cost to Connect All Points](PROBLEM_BANK.md#lc-1584) — Medium, 35 min
17. [LC 416 — Partition Equal Subset Sum](PROBLEM_BANK.md#lc-0416) — Medium, 35 min
18. [LC 300 — Longest Increasing Subsequence](PROBLEM_BANK.md#lc-0300) — Medium, 35 min
19. [LC 155 — Min Stack](PROBLEM_BANK.md#lc-0155) — Easy, 20 min
20. [LC 380 — Insert Delete GetRandom O(1)](PROBLEM_BANK.md#lc-0380) — Medium, 35 min
21. [LC 981 — Time Based Key-Value Store](PROBLEM_BANK.md#lc-0981) — Medium, 35 min
22. [LC 1268 — Search Suggestions System](PROBLEM_BANK.md#lc-1268) — Medium, 35 min
23. [LC 621 — Task Scheduler](PROBLEM_BANK.md#lc-0621) — Medium, 35 min

### Milestone callouts

- [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](PROJECTS.md#dsa-prj-020)
- [DSA-PRJ-070 — Mixed interview simulator and error-analysis dashboard](PROJECTS.md#dsa-prj-070)

### Intentionally deferred

Most reference-only competitive algorithms.


<a id="mixed-mocks-final-revision"></a>
## 12. Mixed mocks and final revision

<!-- PATH_META {"id":"mixed-mocks-final-revision","title":"Mixed mocks and final revision","unit_count":54,"problem_count":14,"concept_minutes":[2430,3500],"problem_minutes":520,"activities":{"Closed-book recall":[240,360],"Reserve-set selection and anonymization":[30,45],"Four mock framing and feedback sessions beyond coding time":[120,180],"Postmortems and delayed re-solves":[300,480]},"activity_minutes":[690,1065],"rapid_total_minutes":[3640,5085],"full_unit_hours":[654,1152],"assumed_or_bridge_prerequisites":[],"project_count":1} -->

**Who it is for:** A learner who has covered core material and now needs unlabeled transfer, timing, communication, and recovery practice.

**Time assumption:** One to two focused weeks; the calculated route is 60 h 40 min–84 h 45 min.

**Prerequisite policy:** Core interview units are assumed retained; this path does not teach missing foundations from scratch.

**Assumed prior knowledge or bridge required:** None; selected units are prerequisite-closed.

### Calculated timing

| Component | Time |
|---|---:|
| Rapid unit study — notebook core plus tiny trace/micro-drill only | 40 h 30 min–58 h 20 min |
| Complete first attempts for 14 selected problems | 8 h 40 min |
| Closed-book recall | 4 h–6 h |
| Reserve-set selection and anonymization | 30 min–45 min |
| Four mock framing and feedback sessions beyond coding time | 2 h–3 h |
| Postmortems and delayed re-solves | 5 h–8 h |
| **Required activities subtotal** | **11 h 30 min–17 h 45 min** |
| **Rapid path total** | **60 h 40 min–84 h 45 min** |
| **Full mastery of included units** | **654–1152 h** |

Selected problem first attempts are counted once, only in the problem-attempt row. The full-mastery total excludes milestone projects and later spaced-review cycles.

### Recommended unit sequence (54 units)

1. [DSA-FND-010 — Computational problem solving and constraint translation](CURRICULUM.md#dsa-fnd-010)
2. [DSA-FND-020 — Brute-force enumeration and bottleneck discovery](CURRICULUM.md#dsa-fnd-020)
3. [DSA-FND-030 — Invariants, correctness, and termination](CURRICULUM.md#dsa-fnd-030)
4. [DSA-FND-040 — Asymptotic notation and input-variable modeling](CURRICULUM.md#dsa-fnd-040)
5. [DSA-FND-060 — Recursion, call stacks, and recursive complexity](CURRICULUM.md#dsa-fnd-060)
6. [DSA-FND-080 — Testing algorithms with examples, oracles, and properties](CURRICULUM.md#dsa-fnd-080)
7. [DSA-FND-090 — Debugging wrong answers, time limits, and memory failures](CURRICULUM.md#dsa-fnd-090)
8. [DSA-FND-100 — Interview communication, dry-runs, and changing constraints](CURRICULUM.md#dsa-fnd-100)
9. [DSA-PY-010 — Python sequence mechanics for DSA](CURRICULUM.md#dsa-py-010)
10. [DSA-PY-020 — Hashing, equality, dictionaries, and sets](CURRICULUM.md#dsa-py-020)
11. [DSA-PY-030 — Counter, defaultdict, deque, and queue-safe Python](CURRICULUM.md#dsa-py-030)
12. [DSA-PY-040 — heapq, bisect, sorting, and comparable entries](CURRICULUM.md#dsa-py-040)
13. [DSA-PY-050 — Mutation, copying, aliasing, and string construction](CURRICULUM.md#dsa-py-050)
14. [DSA-SEQ-010 — Linear scans, aggregation, and minimal state](CURRICULUM.md#dsa-seq-010)
15. [DSA-SEQ-020 — Frequency maps, membership, and complement lookup](CURRICULUM.md#dsa-seq-020)
16. [DSA-SEQ-030 — In-place read/write pointers and stable compaction](CURRICULUM.md#dsa-seq-030)
17. [DSA-SEQ-040 — Opposite-direction two pointers](CURRICULUM.md#dsa-seq-040)
18. [DSA-SEQ-070 — Prefix sums and prefix-state transforms](CURRICULUM.md#dsa-seq-070)
19. [DSA-SEQ-120 — Matrices, grids, rotation, and boundary simulation](CURRICULUM.md#dsa-seq-120)
20. [DSA-ORD-010 — Binary search fundamentals and loop invariants](CURRICULUM.md#dsa-ord-010)
21. [DSA-ORD-030 — Rotated and partially ordered search](CURRICULUM.md#dsa-ord-030)
22. [DSA-LNK-010 — Linked-list representation, sentinels, and ownership](CURRICULUM.md#dsa-lnk-010)
23. [DSA-LNK-020 — Reversal and safe pointer rewiring](CURRICULUM.md#dsa-lnk-020)
24. [DSA-LNK-030 — Fast/slow pointers and cycle detection](CURRICULUM.md#dsa-lnk-030)
25. [DSA-LNK-040 — Merging, intersection, and reference preservation](CURRICULUM.md#dsa-lnk-040)
26. [DSA-LNK-050 — Sublist reversal, reordering, and k-group transformations](CURRICULUM.md#dsa-lnk-050)
27. [DSA-SQH-010 — Stack, queue, and deque invariants](CURRICULUM.md#dsa-sqh-010)
28. [DSA-SQH-020 — Matching, nesting, and expression evaluation](CURRICULUM.md#dsa-sqh-020)
29. [DSA-REC-010 — Recursive decomposition and decision trees](CURRICULUM.md#dsa-rec-010)
30. [DSA-REC-020 — Subsets and combinations](CURRICULUM.md#dsa-rec-020)
31. [DSA-REC-040 — Constraint propagation and pruning](CURRICULUM.md#dsa-rec-040)
32. [DSA-REC-070 — Backtracking versus dynamic programming](CURRICULUM.md#dsa-rec-070)
33. [DSA-TRE-010 — Binary-tree representation and traversal invariants](CURRICULUM.md#dsa-tre-010)
34. [DSA-TRE-020 — Depth-first traversal: recursive and iterative](CURRICULUM.md#dsa-tre-020)
35. [DSA-TRE-040 — Path state and root-to-leaf reasoning](CURRICULUM.md#dsa-tre-040)
36. [DSA-TRE-050 — Subtree aggregation and divide-and-conquer](CURRICULUM.md#dsa-tre-050)
37. [DSA-TRE-070 — Lowest common ancestor and ancestry reasoning](CURRICULUM.md#dsa-tre-070)
38. [DSA-GRA-010 — Graph representations and state-space modeling](CURRICULUM.md#dsa-gra-010)
39. [DSA-GRA-020 — Breadth-first search](CURRICULUM.md#dsa-gra-020)
40. [DSA-GRA-030 — Depth-first search](CURRICULUM.md#dsa-gra-030)
41. [DSA-GRA-040 — Connected components and grid-as-graph reasoning](CURRICULUM.md#dsa-gra-040)
42. [DSA-GRA-070 — Cycle detection in directed and undirected graphs](CURRICULUM.md#dsa-gra-070)
43. [DSA-GRA-080 — Topological sorting and dependency order](CURRICULUM.md#dsa-gra-080)
44. [DSA-GRA-100 — Shortest-path algorithm selection](CURRICULUM.md#dsa-gra-100)
45. [DSA-GRA-150 — Low-link DFS: bridges, articulation points, and strongly connected components](CURRICULUM.md#dsa-gra-150)
46. [DSA-GRD-010 — Greedy-choice recognition and counterexamples](CURRICULUM.md#dsa-grd-010)
47. [DSA-GRD-020 — Exchange arguments and stays-ahead proofs](CURRICULUM.md#dsa-grd-020)
48. [DSA-GRD-040 — Sorting-based greedy and local choices](CURRICULUM.md#dsa-grd-040)
49. [DSA-GRD-050 — Greedy versus dynamic programming](CURRICULUM.md#dsa-grd-050)
50. [DSA-DP-010 — Dynamic-programming recognition and state modeling](CURRICULUM.md#dsa-dp-010)
51. [DSA-DP-020 — Memoization, tabulation, and evaluation order](CURRICULUM.md#dsa-dp-020)
52. [DSA-DP-100 — Interval dynamic programming](CURRICULUM.md#dsa-dp-100)
53. [DSA-SYN-060 — Mixed unlabeled problem solving](CURRICULUM.md#dsa-syn-060)
54. [DSA-SYN-070 — Mock interviews, readiness gates, and error analysis](CURRICULUM.md#dsa-syn-070)

### Selected problem attempts (14)

1. [LC 242 — Valid Anagram](PROBLEM_BANK.md#lc-0242) — Easy, 20 min
2. [LC 392 — Is Subsequence](PROBLEM_BANK.md#lc-0392) — Easy, 20 min
3. [LC 525 — Contiguous Array](PROBLEM_BANK.md#lc-0525) — Medium, 35 min
4. [LC 153 — Find Minimum in Rotated Sorted Array](PROBLEM_BANK.md#lc-0153) — Medium, 35 min
5. [LC 142 — Linked List Cycle II](PROBLEM_BANK.md#lc-0142) — Medium, 35 min
6. [LC 150 — Evaluate Reverse Polish Notation](PROBLEM_BANK.md#lc-0150) — Medium, 35 min
7. [LC 90 — Subsets II](PROBLEM_BANK.md#lc-0090) — Medium, 35 min
8. [LC 236 — Lowest Common Ancestor of a Binary Tree](PROBLEM_BANK.md#lc-0236) — Medium, 35 min
9. [LC 547 — Number of Provinces](PROBLEM_BANK.md#lc-0547) — Medium, 35 min
10. [LC 406 — Queue Reconstruction by Height](PROBLEM_BANK.md#lc-0406) — Medium, 35 min
11. [LC 25 — Reverse Nodes in k-Group](PROBLEM_BANK.md#lc-0025) — Hard, 50 min
12. [LC 127 — Word Ladder](PROBLEM_BANK.md#lc-0127) — Hard, 50 min
13. [LC 312 — Burst Balloons](PROBLEM_BANK.md#lc-0312) — Hard, 50 min
14. [LC 1192 — Critical Connections in a Network](PROBLEM_BANK.md#lc-1192) — Hard, 50 min

### Milestone callouts

- [DSA-PRJ-070 — Mixed interview simulator and error-analysis dashboard](PROJECTS.md#dsa-prj-070)

### Intentionally deferred

New content. The purpose is evidence and repair.
