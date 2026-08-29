# Curated Problem Bank

`data/problems.json` is the machine-readable source of truth. This file is the human index. Problems support units; they do not define curriculum boundaries.

## Counts

| Measure | Count |
|---|---:|
| Unique problems | 121 |
| Mandatory core | 71 |
| Optional expansion and reserve | 41 |
| Hard stretch/mock | 9 |
| Free | 121 |
| Premium | 0 |
| Easy | 24 |
| Medium | 78 |
| Hard | 19 |
| Renewable unlabeled Easy/Medium reserve | 30 |
| Separate Hard stretch/mock pool | 9 |

The mandatory core is finite. The Easy/Medium reserve supports repeated unlabeled readiness sets; Hard problems are kept in a separate stretch/mock pool. No mandatory route depends on Premium access.

## Distribution by owning domain

| Owning domain | Problems |
|---|---:|
| Problem-solving foundations | 0 |
| Python mechanics for DSA | 0 |
| Arrays, strings, and sequence patterns | 27 |
| Searching, ordering, and selection | 9 |
| Linked structures | 9 |
| Stacks, queues, intervals, and heaps | 13 |
| Recursion and backtracking | 6 |
| Trees and tries | 12 |
| Graphs and disjoint sets | 15 |
| Greedy algorithms | 4 |
| Dynamic programming | 12 |
| Bits, mathematics, and string algorithms | 7 |
| Advanced structures and techniques | 1 |
| Composite designs and interview synthesis | 6 |

## Mandatory teaching core

| Problem | Difficulty | Access | Canonical owner | Primary learning purpose | First-attempt timebox |
|---|---|---|---|---|---:|
| <a id="lc-0001"></a>[1 — Two Sum](https://leetcode.com/problems/two-sum/) | Easy | Free | [DSA-SEQ-020](CURRICULUM.md#dsa-seq-020) | complement lookup | 20 min |
| <a id="lc-0003"></a>[3 — Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | Free | [DSA-SEQ-060](CURRICULUM.md#dsa-seq-060) | variable sliding window | 35 min |
| <a id="lc-0011"></a>[11 — Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | Free | [DSA-SEQ-040](CURRICULUM.md#dsa-seq-040) | two-pointer greedy elimination | 35 min |
| <a id="lc-0015"></a>[15 — 3Sum](https://leetcode.com/problems/3sum/) | Medium | Free | [DSA-SEQ-040](CURRICULUM.md#dsa-seq-040) | sorting plus two pointers | 35 min |
| <a id="lc-0019"></a>[19 — Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Medium | Free | [DSA-LNK-030](CURRICULUM.md#dsa-lnk-030) | fixed-gap pointers | 35 min |
| <a id="lc-0020"></a>[20 — Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Easy | Free | [DSA-SQH-020](CURRICULUM.md#dsa-sqh-020) | matching stack | 20 min |
| <a id="lc-0021"></a>[21 — Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Easy | Free | [DSA-LNK-040](CURRICULUM.md#dsa-lnk-040) | sentinel merge | 20 min |
| <a id="lc-0023"></a>[23 — Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Hard | Free | [DSA-SQH-090](CURRICULUM.md#dsa-sqh-090) | K-way merge | 50 min |
| <a id="lc-0033"></a>[33 — Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | Free | [DSA-ORD-030](CURRICULUM.md#dsa-ord-030) | rotated binary search | 35 min |
| <a id="lc-0034"></a>[34 — Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | Free | [DSA-ORD-020](CURRICULUM.md#dsa-ord-020) | lower and upper bounds | 35 min |
| <a id="lc-0039"></a>[39 — Combination Sum](https://leetcode.com/problems/combination-sum/) | Medium | Free | [DSA-REC-040](CURRICULUM.md#dsa-rec-040) | pruned combination search | 35 min |
| <a id="lc-0046"></a>[46 — Permutations](https://leetcode.com/problems/permutations/) | Medium | Free | [DSA-REC-030](CURRICULUM.md#dsa-rec-030) | used-set permutation search | 35 min |
| <a id="lc-0053"></a>[53 — Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | Free | [DSA-SEQ-100](CURRICULUM.md#dsa-seq-100) | Kadane-style running optimum | 35 min |
| <a id="lc-0054"></a>[54 — Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | Medium | Free | [DSA-SEQ-120](CURRICULUM.md#dsa-seq-120) | boundary simulation | 35 min |
| <a id="lc-0055"></a>[55 — Jump Game](https://leetcode.com/problems/jump-game/) | Medium | Free | [DSA-GRD-010](CURRICULUM.md#dsa-grd-010) | greedy reachability | 35 min |
| <a id="lc-0056"></a>[56 — Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Medium | Free | [DSA-SQH-050](CURRICULUM.md#dsa-sqh-050) | sort and merge intervals | 35 min |
| <a id="lc-0057"></a>[57 — Insert Interval](https://leetcode.com/problems/insert-interval/) | Medium | Free | [DSA-SQH-050](CURRICULUM.md#dsa-sqh-050) | three-phase interval scan | 35 min |
| <a id="lc-0062"></a>[62 — Unique Paths](https://leetcode.com/problems/unique-paths/) | Medium | Free | [DSA-DP-040](CURRICULUM.md#dsa-dp-040) | grid DP | 35 min |
| <a id="lc-0070"></a>[70 — Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Easy | Free | [DSA-DP-030](CURRICULUM.md#dsa-dp-030) | one-dimensional DP | 20 min |
| <a id="lc-0073"></a>[73 — Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/) | Medium | Free | [DSA-SEQ-120](CURRICULUM.md#dsa-seq-120) | matrix markers | 35 min |
| <a id="lc-0078"></a>[78 — Subsets](https://leetcode.com/problems/subsets/) | Medium | Free | [DSA-REC-020](CURRICULUM.md#dsa-rec-020) | choose or skip | 35 min |
| <a id="lc-0079"></a>[79 — Word Search](https://leetcode.com/problems/word-search/) | Medium | Free | [DSA-REC-050](CURRICULUM.md#dsa-rec-050) | grid backtracking | 35 min |
| <a id="lc-0098"></a>[98 — Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Medium | Free | [DSA-TRE-060](CURRICULUM.md#dsa-tre-060) | BST bounds | 35 min |
| <a id="lc-0102"></a>[102 — Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | Medium | Free | [DSA-TRE-030](CURRICULUM.md#dsa-tre-030) | level-order BFS | 35 min |
| <a id="lc-0104"></a>[104 — Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | Free | [DSA-TRE-050](CURRICULUM.md#dsa-tre-050) | subtree aggregation | 20 min |
| <a id="lc-0121"></a>[121 — Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Free | [DSA-SEQ-100](CURRICULUM.md#dsa-seq-100) | running optimum | 20 min |
| <a id="lc-0125"></a>[125 — Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | Free | [DSA-SEQ-040](CURRICULUM.md#dsa-seq-040) | opposite two pointers | 20 min |
| <a id="lc-0133"></a>[133 — Clone Graph](https://leetcode.com/problems/clone-graph/) | Medium | Free | [DSA-GRA-030](CURRICULUM.md#dsa-gra-030) | DFS or BFS graph cloning | 35 min |
| <a id="lc-0136"></a>[136 — Single Number](https://leetcode.com/problems/single-number/) | Easy | Free | [DSA-BMS-020](CURRICULUM.md#dsa-bms-020) | XOR cancellation | 20 min |
| <a id="lc-0139"></a>[139 — Word Break](https://leetcode.com/problems/word-break/) | Medium | Free | [DSA-DP-090](CURRICULUM.md#dsa-dp-090) | string segmentation DP | 35 min |
| <a id="lc-0141"></a>[141 — Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | Free | [DSA-LNK-030](CURRICULUM.md#dsa-lnk-030) | fast and slow pointers | 20 min |
| <a id="lc-0143"></a>[143 — Reorder List](https://leetcode.com/problems/reorder-list/) | Medium | Free | [DSA-LNK-050](CURRICULUM.md#dsa-lnk-050) | split, reverse, merge | 35 min |
| <a id="lc-0146"></a>[146 — LRU Cache](https://leetcode.com/problems/lru-cache/) | Medium | Free | [DSA-SYN-010](CURRICULUM.md#dsa-syn-010) | hash map plus doubly linked list | 35 min |
| <a id="lc-0155"></a>[155 — Min Stack](https://leetcode.com/problems/min-stack/) | Easy | Free | [DSA-SYN-020](CURRICULUM.md#dsa-syn-020) | auxiliary minimum state | 20 min |
| <a id="lc-0167"></a>[167 — Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | Free | [DSA-SEQ-040](CURRICULUM.md#dsa-seq-040) | opposite two pointers | 35 min |
| <a id="lc-0191"></a>[191 — Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/) | Easy | Free | [DSA-BMS-010](CURRICULUM.md#dsa-bms-010) | bit clearing | 20 min |
| <a id="lc-0198"></a>[198 — House Robber](https://leetcode.com/problems/house-robber/) | Medium | Free | [DSA-DP-030](CURRICULUM.md#dsa-dp-030) | take-or-skip DP | 35 min |
| <a id="lc-0200"></a>[200 — Number of Islands](https://leetcode.com/problems/number-of-islands/) | Medium | Free | [DSA-GRA-040](CURRICULUM.md#dsa-gra-040) | grid connected components | 35 min |
| <a id="lc-0204"></a>[204 — Count Primes](https://leetcode.com/problems/count-primes/) | Medium | Free | [DSA-BMS-050](CURRICULUM.md#dsa-bms-050) | sieve | 35 min |
| <a id="lc-0206"></a>[206 — Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | Free | [DSA-LNK-020](CURRICULUM.md#dsa-lnk-020) | pointer reversal | 20 min |
| <a id="lc-0207"></a>[207 — Course Schedule](https://leetcode.com/problems/course-schedule/) | Medium | Free | [DSA-GRA-080](CURRICULUM.md#dsa-gra-080) | cycle detection or topological sort | 35 min |
| <a id="lc-0208"></a>[208 — Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) | Medium | Free | [DSA-TRE-090](CURRICULUM.md#dsa-tre-090) | trie | 35 min |
| <a id="lc-0210"></a>[210 — Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Medium | Free | [DSA-GRA-080](CURRICULUM.md#dsa-gra-080) | topological sort | 35 min |
| <a id="lc-0215"></a>[215 — Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Medium | Free | [DSA-ORD-060](CURRICULUM.md#dsa-ord-060) | quickselect or bounded heap | 35 min |
| <a id="lc-0217"></a>[217 — Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | Free | [DSA-SEQ-020](CURRICULUM.md#dsa-seq-020) | membership set | 20 min |
| <a id="lc-0226"></a>[226 — Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | Free | [DSA-TRE-020](CURRICULUM.md#dsa-tre-020) | tree DFS | 20 min |
| <a id="lc-0235"></a>[235 — Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/) | Medium | Free | [DSA-TRE-070](CURRICULUM.md#dsa-tre-070) | BST ancestry | 35 min |
| <a id="lc-0238"></a>[238 — Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | Free | [DSA-SEQ-080](CURRICULUM.md#dsa-seq-080) | prefix and suffix aggregates | 35 min |
| <a id="lc-0300"></a>[300 — Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Medium | Free | [DSA-DP-080](CURRICULUM.md#dsa-dp-080) | LIS DP and tails | 35 min |
| <a id="lc-0309"></a>[309 — Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | Medium | Free | [DSA-DP-110](CURRICULUM.md#dsa-dp-110) | state-machine dynamic programming | 35 min |
| <a id="lc-0322"></a>[322 — Coin Change](https://leetcode.com/problems/coin-change/) | Medium | Free | [DSA-DP-060](CURRICULUM.md#dsa-dp-060) | unbounded minimum DP | 35 min |
| <a id="lc-0347"></a>[347 — Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | Free | [DSA-SQH-080](CURRICULUM.md#dsa-sqh-080) | frequency plus heap or buckets | 35 min |
| <a id="lc-0380"></a>[380 — Insert Delete GetRandom O(1)](https://leetcode.com/problems/insert-delete-getrandom-o1/) | Medium | Free | [DSA-SYN-020](CURRICULUM.md#dsa-syn-020) | array plus index map | 35 min |
| <a id="lc-0416"></a>[416 — Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) | Medium | Free | [DSA-DP-050](CURRICULUM.md#dsa-dp-050) | 0/1 subset-sum DP | 35 min |
| <a id="lc-0424"></a>[424 — Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Medium | Free | [DSA-SEQ-060](CURRICULUM.md#dsa-seq-060) | variable sliding window | 35 min |
| <a id="lc-0435"></a>[435 — Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/) | Medium | Free | [DSA-GRD-030](CURRICULUM.md#dsa-grd-030) | interval scheduling | 35 min |
| <a id="lc-0543"></a>[543 — Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) | Easy | Free | [DSA-TRE-050](CURRICULUM.md#dsa-tre-050) | local return plus global optimum | 20 min |
| <a id="lc-0560"></a>[560 — Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | Free | [DSA-SEQ-070](CURRICULUM.md#dsa-seq-070) | prefix sum plus frequency map | 35 min |
| <a id="lc-0567"></a>[567 — Permutation in String](https://leetcode.com/problems/permutation-in-string/) | Medium | Free | [DSA-SEQ-050](CURRICULUM.md#dsa-seq-050) | fixed sliding window | 35 min |
| <a id="lc-0621"></a>[621 — Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Medium | Free | [DSA-SYN-050](CURRICULUM.md#dsa-syn-050) | frequency-driven scheduling | 35 min |
| <a id="lc-0684"></a>[684 — Redundant Connection](https://leetcode.com/problems/redundant-connection/) | Medium | Free | [DSA-GRA-090](CURRICULUM.md#dsa-gra-090) | disjoint-set union | 35 min |
| <a id="lc-0703"></a>[703 — Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Easy | Free | [DSA-SQH-080](CURRICULUM.md#dsa-sqh-080) | bounded min-heap | 20 min |
| <a id="lc-0704"></a>[704 — Binary Search](https://leetcode.com/problems/binary-search/) | Easy | Free | [DSA-ORD-010](CURRICULUM.md#dsa-ord-010) | exact binary search | 20 min |
| <a id="lc-0739"></a>[739 — Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Medium | Free | [DSA-SQH-030](CURRICULUM.md#dsa-sqh-030) | monotonic stack | 35 min |
| <a id="lc-0743"></a>[743 — Network Delay Time](https://leetcode.com/problems/network-delay-time/) | Medium | Free | [DSA-GRA-110](CURRICULUM.md#dsa-gra-110) | Dijkstra | 35 min |
| <a id="lc-0875"></a>[875 — Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/) | Medium | Free | [DSA-ORD-040](CURRICULUM.md#dsa-ord-040) | binary search on answer | 35 min |
| <a id="lc-0981"></a>[981 — Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | Medium | Free | [DSA-SYN-030](CURRICULUM.md#dsa-syn-030) | per-key ordered history plus boundary search | 35 min |
| <a id="lc-0994"></a>[994 — Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Medium | Free | [DSA-GRA-050](CURRICULUM.md#dsa-gra-050) | multi-source BFS | 35 min |
| <a id="lc-1071"></a>[1071 — Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/) | Easy | Free | [DSA-BMS-040](CURRICULUM.md#dsa-bms-040) | Euclidean structure on repeated strings | 20 min |
| <a id="lc-1143"></a>[1143 — Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/) | Medium | Free | [DSA-DP-070](CURRICULUM.md#dsa-dp-070) | two-sequence DP | 35 min |
| <a id="lc-1584"></a>[1584 — Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/) | Medium | Free | [DSA-GRA-130](CURRICULUM.md#dsa-gra-130) | minimum spanning tree | 35 min |

## Optional labeled expansion

| Problem | Difficulty | Access | Canonical owner | Primary learning purpose | First-attempt timebox |
|---|---|---|---|---|---:|
| <a id="lc-0041"></a>[41 — First Missing Positive](https://leetcode.com/problems/first-missing-positive/) | Hard | Free | [DSA-SEQ-110](CURRICULUM.md#dsa-seq-110) | index placement | 50 min |
| <a id="lc-0042"></a>[42 — Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Hard | Free | [DSA-SEQ-040](CURRICULUM.md#dsa-seq-040) | two pointers or monotonic stack | 50 min |
| <a id="lc-0051"></a>[51 — N-Queens](https://leetcode.com/problems/n-queens/) | Hard | Free | [DSA-REC-040](CURRICULUM.md#dsa-rec-040) | constraint backtracking | 50 min |
| <a id="lc-0076"></a>[76 — Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Hard | Free | [DSA-SEQ-060](CURRICULUM.md#dsa-seq-060) | minimum valid sliding window | 50 min |
| <a id="lc-0084"></a>[84 — Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | Hard | Free | [DSA-SQH-030](CURRICULUM.md#dsa-sqh-030) | monotonic stack | 50 min |
| <a id="lc-0124"></a>[124 — Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Hard | Free | [DSA-TRE-050](CURRICULUM.md#dsa-tre-050) | tree aggregation | 50 min |
| <a id="lc-0239"></a>[239 — Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Hard | Free | [DSA-SQH-040](CURRICULUM.md#dsa-sqh-040) | monotonic deque | 50 min |
| <a id="lc-0295"></a>[295 — Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/) | Hard | Free | [DSA-SQH-100](CURRICULUM.md#dsa-sqh-100) | two heaps | 50 min |
| <a id="lc-0297"></a>[297 — Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Hard | Free | [DSA-TRE-080](CURRICULUM.md#dsa-tre-080) | tree serialization | 50 min |
| <a id="lc-0974"></a>[974 — Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/) | Medium | Free | [DSA-BMS-060](CURRICULUM.md#dsa-bms-060) | prefix remainder frequency | 35 min |
| <a id="lc-1268"></a>[1268 — Search Suggestions System](https://leetcode.com/problems/search-suggestions-system/) | Medium | Free | [DSA-SYN-040](CURRICULUM.md#dsa-syn-040) | prefix index with bounded ranked results | 35 min |

## Renewable Easy/Medium unlabeled reserve

These problems are held back for mixed transfer. Before an attempt, do not reveal the owner, pattern, intended structure, target complexity, invariant, or metadata stored in `data/problems.json`.

| Problem | Difficulty | Access | First-attempt timebox | Reserve use |
|---|---|---|---:|---|
| <a id="lc-0049"></a>[49 — Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0075"></a>[75 — Sort Colors](https://leetcode.com/problems/sort-colors/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0090"></a>[90 — Subsets II](https://leetcode.com/problems/subsets-ii/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0092"></a>[92 — Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0105"></a>[105 — Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0128"></a>[128 — Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0138"></a>[138 — Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0142"></a>[142 — Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0150"></a>[150 — Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0153"></a>[153 — Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0169"></a>[169 — Majority Element](https://leetcode.com/problems/majority-element/) | Easy | Free | 20 min | Unlabeled mixed set |
| <a id="lc-0236"></a>[236 — Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0242"></a>[242 — Valid Anagram](https://leetcode.com/problems/valid-anagram/) | Easy | Free | 20 min | Unlabeled mixed set |
| <a id="lc-0268"></a>[268 — Missing Number](https://leetcode.com/problems/missing-number/) | Easy | Free | 20 min | Unlabeled mixed set |
| <a id="lc-0283"></a>[283 — Move Zeroes](https://leetcode.com/problems/move-zeroes/) | Easy | Free | 20 min | Unlabeled mixed set |
| <a id="lc-0304"></a>[304 — Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0307"></a>[307 — Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0392"></a>[392 — Is Subsequence](https://leetcode.com/problems/is-subsequence/) | Easy | Free | 20 min | Unlabeled mixed set |
| <a id="lc-0406"></a>[406 — Queue Reconstruction by Height](https://leetcode.com/problems/queue-reconstruction-by-height/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0417"></a>[417 — Pacific Atlantic Water Flow](https://leetcode.com/problems/pacific-atlantic-water-flow/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0525"></a>[525 — Contiguous Array](https://leetcode.com/problems/contiguous-array/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0547"></a>[547 — Number of Provinces](https://leetcode.com/problems/number-of-provinces/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0647"></a>[647 — Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0733"></a>[733 — Flood Fill](https://leetcode.com/problems/flood-fill/) | Easy | Free | 20 min | Unlabeled mixed set |
| <a id="lc-0785"></a>[785 — Is Graph Bipartite?](https://leetcode.com/problems/is-graph-bipartite/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0912"></a>[912 — Sort an Array](https://leetcode.com/problems/sort-an-array/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-0973"></a>[973 — K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-1011"></a>[1011 — Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-1094"></a>[1094 — Car Pooling](https://leetcode.com/problems/car-pooling/) | Medium | Free | 35 min | Unlabeled mixed set |
| <a id="lc-2406"></a>[2406 — Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/) | Medium | Free | 35 min | Unlabeled mixed set |

## Separate Hard stretch and mock pool

Hard problems do not count toward the ten-problem Easy/Medium readiness benchmark. They are optional stretch or advanced mock material.

| Problem | Difficulty | Access | First-attempt timebox | Use |
|---|---|---|---:|---|
| <a id="lc-0025"></a>[25 — Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Hard | Free | 50 min | Mixed |
| <a id="lc-0127"></a>[127 — Word Ladder](https://leetcode.com/problems/word-ladder/) | Hard | Free | 50 min | Mock |
| <a id="lc-0212"></a>[212 — Word Search II](https://leetcode.com/problems/word-search-ii/) | Hard | Free | 50 min | Mixed |
| <a id="lc-0218"></a>[218 — The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) | Hard | Free | 50 min | Mixed |
| <a id="lc-0312"></a>[312 — Burst Balloons](https://leetcode.com/problems/burst-balloons/) | Hard | Free | 50 min | Mock |
| <a id="lc-0847"></a>[847 — Shortest Path Visiting All Nodes](https://leetcode.com/problems/shortest-path-visiting-all-nodes/) | Hard | Free | 50 min | Mock |
| <a id="lc-1192"></a>[1192 — Critical Connections in a Network](https://leetcode.com/problems/critical-connections-in-a-network/) | Hard | Free | 50 min | Mixed |
| <a id="lc-1368"></a>[1368 — Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/) | Hard | Free | 50 min | Mixed |
| <a id="lc-1392"></a>[1392 — Longest Happy Prefix](https://leetcode.com/problems/longest-happy-prefix/) | Hard | Free | 50 min | Mixed |

## Practice-coverage audit

Every Core or Professional algorithmic unit has a canonical/secondary problem reference or an explicit original runnable micro-lab. This table is generated from the `practice_coverage` section of `data/problems.json`.

| Unit | Practice evidence |
|---|---|
| [DSA-SEQ-010](CURRICULUM.md#dsa-seq-010) | [LC 121](#lc-0121), [LC 169](#lc-0169) |
| [DSA-SEQ-020](CURRICULUM.md#dsa-seq-020) | [LC 1](#lc-0001), [LC 49](#lc-0049), [LC 128](#lc-0128), [LC 217](#lc-0217), [LC 242](#lc-0242) |
| [DSA-SEQ-030](CURRICULUM.md#dsa-seq-030) | [LC 75](#lc-0075), [LC 283](#lc-0283) |
| [DSA-SEQ-040](CURRICULUM.md#dsa-seq-040) | [LC 11](#lc-0011), [LC 15](#lc-0015), [LC 42](#lc-0042), [LC 125](#lc-0125), [LC 167](#lc-0167), [LC 392](#lc-0392) |
| [DSA-SEQ-050](CURRICULUM.md#dsa-seq-050) | [LC 567](#lc-0567) |
| [DSA-SEQ-060](CURRICULUM.md#dsa-seq-060) | [LC 3](#lc-0003), [LC 76](#lc-0076), [LC 424](#lc-0424) |
| [DSA-SEQ-070](CURRICULUM.md#dsa-seq-070) | [LC 304](#lc-0304), [LC 525](#lc-0525), [LC 560](#lc-0560) |
| [DSA-SEQ-080](CURRICULUM.md#dsa-seq-080) | [LC 238](#lc-0238) |
| [DSA-SEQ-090](CURRICULUM.md#dsa-seq-090) | [LC 1094](#lc-1094) |
| [DSA-SEQ-100](CURRICULUM.md#dsa-seq-100) | [LC 53](#lc-0053), [LC 121](#lc-0121) |
| [DSA-SEQ-110](CURRICULUM.md#dsa-seq-110) | [LC 41](#lc-0041) |
| [DSA-SEQ-120](CURRICULUM.md#dsa-seq-120) | [LC 54](#lc-0054), [LC 73](#lc-0073) |
| [DSA-ORD-010](CURRICULUM.md#dsa-ord-010) | [LC 704](#lc-0704) |
| [DSA-ORD-020](CURRICULUM.md#dsa-ord-020) | [LC 34](#lc-0034) |
| [DSA-ORD-030](CURRICULUM.md#dsa-ord-030) | [LC 33](#lc-0033), [LC 153](#lc-0153) |
| [DSA-ORD-040](CURRICULUM.md#dsa-ord-040) | [LC 875](#lc-0875), [LC 1011](#lc-1011) |
| [DSA-ORD-050](CURRICULUM.md#dsa-ord-050) | [LC 912](#lc-0912) |
| [DSA-ORD-060](CURRICULUM.md#dsa-ord-060) | [LC 215](#lc-0215), [LC 973](#lc-0973) |
| [DSA-ORD-070](CURRICULUM.md#dsa-ord-070) | [LC 347](#lc-0347) |
| [DSA-LNK-010](CURRICULUM.md#dsa-lnk-010) | [LC 21](#lc-0021) |
| [DSA-LNK-020](CURRICULUM.md#dsa-lnk-020) | [LC 206](#lc-0206) |
| [DSA-LNK-030](CURRICULUM.md#dsa-lnk-030) | [LC 19](#lc-0019), [LC 141](#lc-0141), [LC 142](#lc-0142) |
| [DSA-LNK-040](CURRICULUM.md#dsa-lnk-040) | [LC 21](#lc-0021), [LC 138](#lc-0138) |
| [DSA-LNK-050](CURRICULUM.md#dsa-lnk-050) | [LC 25](#lc-0025), [LC 92](#lc-0092), [LC 143](#lc-0143) |
| [DSA-LNK-060](CURRICULUM.md#dsa-lnk-060) | [LC 146](#lc-0146) |
| [DSA-SQH-010](CURRICULUM.md#dsa-sqh-010) | [LC 20](#lc-0020), [LC 155](#lc-0155) |
| [DSA-SQH-020](CURRICULUM.md#dsa-sqh-020) | [LC 20](#lc-0020), [LC 150](#lc-0150) |
| [DSA-SQH-030](CURRICULUM.md#dsa-sqh-030) | [LC 84](#lc-0084), [LC 739](#lc-0739) |
| [DSA-SQH-040](CURRICULUM.md#dsa-sqh-040) | [LC 239](#lc-0239) |
| [DSA-SQH-050](CURRICULUM.md#dsa-sqh-050) | [LC 56](#lc-0056), [LC 57](#lc-0057) |
| [DSA-SQH-060](CURRICULUM.md#dsa-sqh-060) | [LC 218](#lc-0218), [LC 2406](#lc-2406) |
| [DSA-SQH-070](CURRICULUM.md#dsa-sqh-070) | [LC 215](#lc-0215), [LC 703](#lc-0703) |
| [DSA-SQH-080](CURRICULUM.md#dsa-sqh-080) | [LC 215](#lc-0215), [LC 347](#lc-0347), [LC 703](#lc-0703) |
| [DSA-SQH-090](CURRICULUM.md#dsa-sqh-090) | [LC 23](#lc-0023) |
| [DSA-SQH-100](CURRICULUM.md#dsa-sqh-100) | [LC 295](#lc-0295) |
| [DSA-REC-010](CURRICULUM.md#dsa-rec-010) | [LC 46](#lc-0046), [LC 78](#lc-0078) |
| [DSA-REC-020](CURRICULUM.md#dsa-rec-020) | [LC 78](#lc-0078), [LC 90](#lc-0090) |
| [DSA-REC-030](CURRICULUM.md#dsa-rec-030) | [LC 46](#lc-0046) |
| [DSA-REC-040](CURRICULUM.md#dsa-rec-040) | [LC 39](#lc-0039), [LC 51](#lc-0051) |
| [DSA-REC-050](CURRICULUM.md#dsa-rec-050) | [LC 79](#lc-0079) |
| [DSA-REC-060](CURRICULUM.md#dsa-rec-060) | [LC 39](#lc-0039), [LC 51](#lc-0051) |
| [DSA-REC-070](CURRICULUM.md#dsa-rec-070) | [LC 139](#lc-0139), [LC 416](#lc-0416) |
| [DSA-TRE-010](CURRICULUM.md#dsa-tre-010) | [LC 102](#lc-0102), [LC 226](#lc-0226) |
| [DSA-TRE-020](CURRICULUM.md#dsa-tre-020) | [LC 226](#lc-0226) |
| [DSA-TRE-030](CURRICULUM.md#dsa-tre-030) | [LC 102](#lc-0102) |
| [DSA-TRE-040](CURRICULUM.md#dsa-tre-040) | [LC 104](#lc-0104), [LC 124](#lc-0124) |
| [DSA-TRE-050](CURRICULUM.md#dsa-tre-050) | [LC 104](#lc-0104), [LC 124](#lc-0124), [LC 543](#lc-0543) |
| [DSA-TRE-060](CURRICULUM.md#dsa-tre-060) | [LC 98](#lc-0098) |
| [DSA-TRE-070](CURRICULUM.md#dsa-tre-070) | [LC 235](#lc-0235), [LC 236](#lc-0236) |
| [DSA-TRE-080](CURRICULUM.md#dsa-tre-080) | [LC 105](#lc-0105), [LC 297](#lc-0297) |
| [DSA-TRE-090](CURRICULUM.md#dsa-tre-090) | [LC 208](#lc-0208), [LC 212](#lc-0212) |
| [DSA-TRE-100](CURRICULUM.md#dsa-tre-100) | [LC 124](#lc-0124), [LC 543](#lc-0543) |
| [DSA-GRA-010](CURRICULUM.md#dsa-gra-010) | [LC 133](#lc-0133), [LC 200](#lc-0200) |
| [DSA-GRA-020](CURRICULUM.md#dsa-gra-020) | [LC 127](#lc-0127) |
| [DSA-GRA-030](CURRICULUM.md#dsa-gra-030) | [LC 133](#lc-0133) |
| [DSA-GRA-040](CURRICULUM.md#dsa-gra-040) | [LC 200](#lc-0200), [LC 417](#lc-0417), [LC 547](#lc-0547), [LC 733](#lc-0733) |
| [DSA-GRA-050](CURRICULUM.md#dsa-gra-050) | [LC 994](#lc-0994) |
| [DSA-GRA-060](CURRICULUM.md#dsa-gra-060) | [LC 785](#lc-0785) |
| [DSA-GRA-070](CURRICULUM.md#dsa-gra-070) | [LC 207](#lc-0207), [LC 684](#lc-0684) |
| [DSA-GRA-080](CURRICULUM.md#dsa-gra-080) | [LC 207](#lc-0207), [LC 210](#lc-0210) |
| [DSA-GRA-090](CURRICULUM.md#dsa-gra-090) | [LC 684](#lc-0684) |
| [DSA-GRA-100](CURRICULUM.md#dsa-gra-100) | [LC 127](#lc-0127), [LC 743](#lc-0743), [LC 1368](#lc-1368) |
| [DSA-GRA-110](CURRICULUM.md#dsa-gra-110) | [LC 743](#lc-0743) |
| [DSA-GRA-130](CURRICULUM.md#dsa-gra-130) | [LC 1584](#lc-1584) |
| [DSA-GRD-010](CURRICULUM.md#dsa-grd-010) | [LC 55](#lc-0055), [LC 169](#lc-0169) |
| [DSA-GRD-020](CURRICULUM.md#dsa-grd-020) | [LC 55](#lc-0055), [LC 435](#lc-0435) |
| [DSA-GRD-030](CURRICULUM.md#dsa-grd-030) | [LC 435](#lc-0435) |
| [DSA-GRD-040](CURRICULUM.md#dsa-grd-040) | [LC 406](#lc-0406), [LC 435](#lc-0435) |
| [DSA-GRD-050](CURRICULUM.md#dsa-grd-050) | [LC 55](#lc-0055), [LC 198](#lc-0198) |
| [DSA-DP-010](CURRICULUM.md#dsa-dp-010) | [LC 70](#lc-0070), [LC 198](#lc-0198) |
| [DSA-DP-020](CURRICULUM.md#dsa-dp-020) | [LC 62](#lc-0062), [LC 70](#lc-0070), [LC 1143](#lc-1143) |
| [DSA-DP-030](CURRICULUM.md#dsa-dp-030) | [LC 70](#lc-0070), [LC 198](#lc-0198) |
| [DSA-DP-040](CURRICULUM.md#dsa-dp-040) | [LC 62](#lc-0062) |
| [DSA-DP-050](CURRICULUM.md#dsa-dp-050) | [LC 416](#lc-0416) |
| [DSA-DP-060](CURRICULUM.md#dsa-dp-060) | [LC 322](#lc-0322) |
| [DSA-DP-070](CURRICULUM.md#dsa-dp-070) | [LC 1143](#lc-1143) |
| [DSA-DP-080](CURRICULUM.md#dsa-dp-080) | [LC 300](#lc-0300) |
| [DSA-DP-090](CURRICULUM.md#dsa-dp-090) | [LC 139](#lc-0139), [LC 647](#lc-0647) |
| [DSA-DP-110](CURRICULUM.md#dsa-dp-110) | [LC 121](#lc-0121), [LC 309](#lc-0309) |
| [DSA-DP-120](CURRICULUM.md#dsa-dp-120) | [LC 124](#lc-0124), [LC 543](#lc-0543) |
| [DSA-BMS-010](CURRICULUM.md#dsa-bms-010) | [LC 191](#lc-0191) |
| [DSA-BMS-020](CURRICULUM.md#dsa-bms-020) | [LC 136](#lc-0136), [LC 268](#lc-0268) |
| [DSA-BMS-030](CURRICULUM.md#dsa-bms-030) | [LC 78](#lc-0078) |
| [DSA-BMS-040](CURRICULUM.md#dsa-bms-040) | [LC 1071](#lc-1071) |
| [DSA-BMS-050](CURRICULUM.md#dsa-bms-050) | [LC 204](#lc-0204) |
| [DSA-BMS-060](CURRICULUM.md#dsa-bms-060) | [LC 974](#lc-0974) |
| [DSA-SYN-010](CURRICULUM.md#dsa-syn-010) | [LC 146](#lc-0146) |
| [DSA-SYN-020](CURRICULUM.md#dsa-syn-020) | [LC 155](#lc-0155), [LC 380](#lc-0380) |
| [DSA-SYN-030](CURRICULUM.md#dsa-syn-030) | [LC 295](#lc-0295), [LC 981](#lc-0981) |
| [DSA-SYN-040](CURRICULUM.md#dsa-syn-040) | [LC 208](#lc-0208), [LC 1268](#lc-1268) |
| [DSA-SYN-050](CURRICULUM.md#dsa-syn-050) | [LC 621](#lc-0621), [LC 2406](#lc-2406) |
| [DSA-SYN-060](CURRICULUM.md#dsa-syn-060) | Original micro-lab — Build a hidden-label mixed-set selector, run tiny unlabeled cases, and compare the chosen approach with the postmortem owner unit. Reason: A platform problem would reveal its own tag; an original lab is required to test pattern selection without labels. |
| [DSA-SYN-070](CURRICULUM.md#dsa-syn-070) | Original micro-lab — Build a deterministic mock-interview scorer and review scheduler from fixed rubric and hint-ledger fixtures. Reason: This unit assesses interview evidence and scheduling behavior rather than one canonical algorithmic answer. |

## Mixed/mock label protection

Reserve tables intentionally hide canonical owner and primary pattern. Full metadata remains in `data/problems.json` for postmortem and validation only.

## Review rule

“Accepted” is one event, not mastery. Record hints, explanation quality, missed edge cases, delayed re-solve results, and transfer performance using [`templates/problem_attempt.md`](templates/problem_attempt.md).
