# DSA Milestone Projects and Assessment Labs

Projects integrate multiple units but are not curriculum units. Create a project folder only when initialized with `Initialize project <PROJECT-ID>`. Project completion never automatically advances a unit learning state.

## Overview

| Project ID | Purpose | Size |
|---|---|:---:|
| [DSA-PRJ-010 — Core data-structure invariant laboratory](#dsa-prj-010) | Implement selected structures from first principles and prove that every mutation preserves their representation invariants. | `L` |
| [DSA-PRJ-020 — Brute-force oracle and differential-testing laboratory](#dsa-prj-020) | Use obviously correct small-input algorithms as oracles to discover defects in optimized solutions and shrinking assumptions. | `L` |
| [DSA-PRJ-030 — Array and string pattern visualizer](#dsa-prj-030) | Render faithful state transitions for pointer, window, prefix, partition, monotonic, and matrix algorithms on tiny inputs. | `L` |
| [DSA-PRJ-040 — Tree and graph traversal explorer](#dsa-prj-040) | Compare recursive and iterative traversals, frontier behavior, component discovery, cycle state, and topological processing. | `L` |
| [DSA-PRJ-050 — Shortest-path and routing laboratory](#dsa-prj-050) | Select, implement, compare, and falsify shortest-path algorithms across different edge-weight domains and query shapes. | `XL` |
| [DSA-PRJ-060 — Dynamic-programming state-modeling explorer](#dsa-prj-060) | Derive dynamic programs from recursive choices and make state, transition, evaluation order, reconstruction, and space optimization visible. | `XL` |
| [DSA-PRJ-070 — Mixed interview simulator and error-analysis dashboard](#dsa-prj-070) | Run renewable unlabeled interviews, preserve hint and reasoning evidence, and turn delayed outcomes into a focused revision queue. | `XL` |

<a id="dsa-prj-010"></a>
## `DSA-PRJ-010` — Core data-structure invariant laboratory

**Purpose:** Implement selected structures from first principles and prove that every mutation preserves their representation invariants.

**Required prerequisites:** `DSA-FND-030`, `DSA-FND-040`, `DSA-PY-080`, `DSA-LNK-010`, `DSA-SQH-010`, `DSA-SQH-070`, `DSA-TRE-010`, `DSA-GRA-010`

**Recommended prerequisites:** `DSA-FND-050`, `DSA-GRA-090`

**Integrated structures and algorithms:** dynamic array, sentinel linked list, stack/deque, binary heap, tree representation, disjoint-set union

### Staged change pressure

1. Implement a small dynamic array with explicit size and capacity; add growth and shrink requirements.
2. Implement a doubly linked list with sentinels, then expose insertion, deletion, and iteration.
3. Implement a binary min-heap, then add key updates or indexed deletion.
4. Implement DSU with union by size and path compression; compare against a naive parent forest.

### Core invariants

- `0 <= size <= capacity` and logical elements occupy exactly the active prefix.
- Every list node has mutually consistent `prev` and `next` links; sentinels are never exposed as data.
- Every heap parent is no greater than its children.
- Every DSU parent chain terminates at a root, and component sizes live only at roots.

### Seeded defects

- A resize copies `capacity` slots instead of `size` elements.
- Deleting the final real list node leaves one sentinel pointing at a detached node.
- Heap sift-down chooses the left child without comparing the right child.
- Path compression updates parents but component-size accounting is read from a non-root.

### Adversarial tests and oracle

Compare public behavior with Python `list`, `collections.deque`, `heapq`, and a tiny connectivity oracle that recomputes components by DFS.

### Required visual traces

- capacity-and-active-prefix frames before and after resize
- four-node pointer rewiring frames
- heap array/tree views after every swap
- DSU forest before and after union/compression

### Refactoring checkpoint

Extract invariant-checking helpers used only by tests; defend why production methods should not repeatedly perform O(n) full-structure validation.

### Rejected alternatives

- Using only standard-library structures would hide representation invariants.
- A single generic `Node` abstraction for lists, trees, and heaps would couple unrelated invariants.

### Complexity analysis

Derive per-operation worst-case and amortized costs, including resize copies, heap height, and inverse-Ackermann DSU operations.

### Senior interview walkthrough

- Explain which invariants are local and which require whole-structure reasoning.
- Diagnose one seeded corruption from a failing minimal test.
- Discuss which implementation should be used in production Python and why the from-scratch version remains educational.

### Definition of done

- [ ] All four staged structures have deterministic tests and invariant-focused property tests.
- [ ] Every seeded defect is reproduced by a minimal counterexample and repaired.
- [ ] At least one operation has an amortized proof rather than only a claimed complexity.
- [ ] Visual traces and the production-versus-educational trade-off are documented.
- [ ] Tests and commands actually run are recorded without fabricated results.
- [ ] Evidence is linked in `PROGRESS.md` without automatic unit-state inflation.


<a id="dsa-prj-020"></a>
## `DSA-PRJ-020` — Brute-force oracle and differential-testing laboratory

**Purpose:** Use obviously correct small-input algorithms as oracles to discover defects in optimized solutions and shrinking assumptions.

**Required prerequisites:** `DSA-FND-020`, `DSA-FND-080`, `DSA-FND-090`, `DSA-PY-080`

**Recommended prerequisites:** `DSA-SEQ-060`, `DSA-ORD-040`, `DSA-DP-020`

**Integrated structures and algorithms:** exhaustive enumeration, randomized generation, Hypothesis strategies, differential testing, shrinking, complexity boundaries

### Staged change pressure

1. Build a cubic or quadratic oracle for a sequence problem and an optimized window/prefix implementation.
2. Add a monotonic-answer problem with a linear feasibility oracle and a binary-search implementation.
3. Add a small DP problem with an exponential recursive oracle and memoized/tabulated implementations.
4. Introduce input-size guards so oracles never escape their trusted small domain.

### Core invariants

- The oracle and optimized version receive equivalent immutable inputs.
- Generated examples satisfy the original problem constraints.
- A mismatch records the seed, minimized input, both outputs, and the claimed invariant.
- Performance assertions never replace correctness assertions.

### Seeded defects

- The oracle mutates a list that is then reused by the optimized version.
- A generated test silently excludes empty and duplicate-heavy inputs.
- The binary-search predicate is monotonic only under an omitted positivity constraint.
- A DP oracle shares a memo between independent test cases.

### Adversarial tests and oracle

The project itself establishes one independent oracle per algorithm family; for tiny domains, also enumerate all possible inputs to verify the generator did not miss a class.

### Required visual traces

- oracle-versus-optimized call flow
- shrinking sequence from failing input to minimal counterexample
- feasibility predicate table across an answer range
- recursion tree collapsed into a state graph

### Refactoring checkpoint

Separate generators, oracles, optimized implementations, and comparison harnesses so a defect in one layer cannot mask another.

### Rejected alternatives

- Golden expected-output files alone do not explore enough input variation.
- Benchmark-only comparisons can make two equally wrong implementations appear successful.

### Complexity analysis

State the safe oracle input bound, optimized complexity, generation cost, and total test-suite cost.

### Senior interview walkthrough

- Explain when a brute-force implementation is trustworthy enough to be an oracle.
- Show how the smallest counterexample reveals the exact broken invariant.
- Defend which properties belong in Hypothesis and which require hand-selected adversarial tests.

### Definition of done

- [ ] Three distinct algorithm families have independent oracles and optimized implementations.
- [ ] At least six seeded bugs are found automatically, including one mutation bug and one invalid monotonicity assumption.
- [ ] Every failure is reproducible from a stored seed or minimized input.
- [ ] The test harness records complexity boundaries and never claims benchmarks that were not run.
- [ ] Tests and commands actually run are recorded without fabricated results.
- [ ] Evidence is linked in `PROGRESS.md` without automatic unit-state inflation.


<a id="dsa-prj-030"></a>
## `DSA-PRJ-030` — Array and string pattern visualizer

**Purpose:** Render faithful state transitions for pointer, window, prefix, partition, monotonic, and matrix algorithms on tiny inputs.

**Required prerequisites:** `DSA-SEQ-030`, `DSA-SEQ-040`, `DSA-SEQ-050`, `DSA-SEQ-060`, `DSA-SEQ-070`, `DSA-SEQ-120`

**Recommended prerequisites:** `DSA-SQH-030`, `DSA-SQH-040`

**Integrated structures and algorithms:** read/write pointers, opposite pointers, sliding windows, prefix state, partitioning, monotonic structures, matrix boundaries

### Staged change pressure

1. Define a common immutable trace-event schema without forcing every algorithm into identical state fields.
2. Add read/write and opposite-pointer traces, including before/after mutation frames.
3. Add fixed and variable windows with explicit validity and contraction events.
4. Add prefix-state, monotonic-stack, and spiral-matrix traces; export notebook-friendly text.

### Core invariants

- A trace frame represents state either immediately before or immediately after one documented transition, never ambiguously both.
- Tracing does not change algorithm behavior or asymptotic complexity beyond emitted-output cost.
- Window validity and pointer domains are visible in every relevant frame.
- Mutation traces retain the original value needed to explain an overwrite.

### Seeded defects

- A frame is captured after both pointers move, hiding the elimination decision.
- A variable window records its answer before restoring validity.
- Equal values use inconsistent monotonic-stack pop rules between code and trace.
- Spiral boundaries emit a duplicate row after top crosses bottom.

### Adversarial tests and oracle

For tiny inputs, compare final outputs with simple brute-force implementations and verify trace-derived outputs equal implementation outputs.

### Required visual traces

- indexed pointer frames
- window expansion/contraction timeline
- prefix-frequency table
- monotonic stack content per index
- matrix boundary rectangle per step

### Refactoring checkpoint

Replace one giant event dictionary with small typed event records while preserving a shared renderer boundary.

### Rejected alternatives

- Animation or web UI would turn the project into frontend work.
- Printing arbitrary local variables would expose noise instead of the governing invariant.

### Complexity analysis

Account for algorithm cost separately from trace-output size; state when retaining every frame changes space from O(1) to O(n).

### Senior interview walkthrough

- Use one trace to derive rather than merely illustrate an invariant.
- Explain why a tempting alternative pattern is wrong for the same input.
- Modify a requirement and identify which trace fields must change.

### Definition of done

- [ ] At least six algorithm families produce deterministic notebook-friendly traces.
- [ ] Every renderer includes how-to-read, key-insight, and limitation text.
- [ ] Seeded timing and boundary defects are exposed by trace assertions.
- [ ] The trace layer can be disabled without changing algorithm results.
- [ ] Tests and commands actually run are recorded without fabricated results.
- [ ] Evidence is linked in `PROGRESS.md` without automatic unit-state inflation.


<a id="dsa-prj-040"></a>
## `DSA-PRJ-040` — Tree and graph traversal explorer

**Purpose:** Compare recursive and iterative traversals, frontier behavior, component discovery, cycle state, and topological processing.

**Required prerequisites:** `DSA-TRE-020`, `DSA-TRE-030`, `DSA-GRA-020`, `DSA-GRA-030`, `DSA-GRA-040`

**Recommended prerequisites:** `DSA-GRA-050`, `DSA-GRA-080`, `DSA-PY-060`

**Integrated structures and algorithms:** tree DFS/BFS, graph DFS/BFS, components, cycle detection, topological sort, recursion safety

### Staged change pressure

1. Implement recursive and iterative tree traversals with matching visit-order contracts.
2. Generalize to graph traversal with explicit visited timing and disconnected components.
3. Add directed-cycle state and Kahn topological processing.
4. Add deep/skewed inputs and switch safely between recursion and explicit stacks.

### Core invariants

- A vertex is scheduled according to one stated visited policy and processed at most once.
- The frontier contains exactly discovered but not yet processed states.
- DFS color state distinguishes unseen, active, and finished vertices in directed cycle detection.
- Kahn output length equals vertex count exactly when the graph is acyclic.

### Seeded defects

- Visited is marked on dequeue, causing duplicate frontier entries.
- An iterative DFS pushes neighbors in natural order but claims to match recursive order.
- A global visited set is reused across independent test graphs.
- Topological indegrees are decremented twice for one edge.

### Adversarial tests and oracle

For small graphs, compare reachable sets and component partitions with exhaustive adjacency-matrix traversal; validate topological orders against every edge.

### Required visual traces

- BFS frontier layers
- recursive call-stack versus explicit-stack snapshots
- DFS discovery/finish colors
- indegree table after each removal

### Refactoring checkpoint

Unify neighbor access and event emission while keeping traversal strategy explicit rather than hidden behind inheritance.

### Rejected alternatives

- One generic traversal function with many boolean flags obscures ordering and visited semantics.
- Recursion-only code is unsafe for deliberately deep inputs.

### Complexity analysis

Derive O(V+E) with representation-specific qualifications and include frontier, visited, recursion-stack, and output space.

### Senior interview walkthrough

- Explain why BFS and DFS may both solve reachability but expose different evidence.
- Diagnose a duplicate-enqueue defect from the frontier trace.
- Choose a traversal after a constraint change and defend the decision.

### Definition of done

- [ ] Recursive/iterative tree traversal and graph BFS/DFS have cross-checked outputs.
- [ ] Components, cycle detection, and topological sorting include adversarial directed and disconnected cases.
- [ ] A deep input demonstrates the recursion-risk policy.
- [ ] All order-sensitive claims have deterministic test contracts.
- [ ] Tests and commands actually run are recorded without fabricated results.
- [ ] Evidence is linked in `PROGRESS.md` without automatic unit-state inflation.


<a id="dsa-prj-050"></a>
## `DSA-PRJ-050` — Shortest-path and routing laboratory

**Purpose:** Select, implement, compare, and falsify shortest-path algorithms across different edge-weight domains and query shapes.

**Required prerequisites:** `DSA-GRA-100`, `DSA-GRA-110`, `DSA-GRA-120`, `DSA-GRA-140`

**Recommended prerequisites:** `DSA-GRA-130`, `DSA-SQH-070`

**Integrated structures and algorithms:** BFS, 0-1 BFS, Dijkstra, Bellman-Ford, Floyd-Warshall, path reconstruction, algorithm selection

### Staged change pressure

1. Implement unweighted BFS with path reconstruction.
2. Introduce weights in {0,1} and add 0-1 BFS.
3. Introduce arbitrary non-negative weights and Dijkstra with stale-entry handling.
4. Introduce negative edges, negative cycles, and all-pairs queries using Bellman-Ford and Floyd-Warshall.

### Core invariants

- A settled Dijkstra distance is final only under non-negative edge weights.
- A relaxation changes a distance only when a strictly better known path is found.
- 0-1 BFS deque placement reflects whether the new edge adds zero or one.
- Path parents correspond to the distance value that survived final relaxation.

### Seeded defects

- Dijkstra is selected despite a negative edge.
- A stale heap entry overwrites a newer parent.
- Infinity arithmetic creates a false Bellman-Ford relaxation from an unreachable vertex.
- Floyd-Warshall loop order is permuted so intermediate-vertex meaning is lost.

### Adversarial tests and oracle

Use Floyd-Warshall on tiny graphs as an all-pairs oracle; compare single-source outputs with Bellman-Ford where its preconditions hold.

### Required visual traces

- frontier/deque/heap snapshots
- edge-relaxation table
- distance and parent arrays after each phase
- algorithm-selection decision table by weight domain

### Refactoring checkpoint

Create a small graph/input boundary and separate algorithm selection from each algorithm; reject an abstract class hierarchy that adds no useful contract.

### Rejected alternatives

- Always using Dijkstra is incorrect with negative edges and wasteful for unweighted graphs.
- Always using Floyd-Warshall ignores sparse-graph and single-source constraints.

### Complexity analysis

Derive costs using V and E for each representation; include heap duplicates, all-pairs matrix space, and reconstruction output.

### Senior interview walkthrough

- Given only constraints, choose the algorithm and state why each alternative is invalid or excessive.
- Prove the key finalization or relaxation invariant.
- Respond to online updates and explain why the static algorithms no longer answer cheaply.

### Definition of done

- [ ] All five algorithm families pass shared tiny-graph differential tests where domains overlap.
- [ ] Negative-cycle and unreachable-state behavior is explicit.
- [ ] At least five seeded algorithm-selection or relaxation defects are diagnosed.
- [ ] The final report contains a precise selection matrix and path-reconstruction trade-offs.
- [ ] Tests and commands actually run are recorded without fabricated results.
- [ ] Evidence is linked in `PROGRESS.md` without automatic unit-state inflation.


<a id="dsa-prj-060"></a>
## `DSA-PRJ-060` — Dynamic-programming state-modeling explorer

**Purpose:** Derive dynamic programs from recursive choices and make state, transition, evaluation order, reconstruction, and space optimization visible.

**Required prerequisites:** `DSA-DP-010`, `DSA-DP-020`, `DSA-DP-030`, `DSA-DP-040`, `DSA-DP-050`, `DSA-DP-070`

**Recommended prerequisites:** `DSA-DP-100`, `DSA-DP-110`, `DSA-DP-120`

**Integrated structures and algorithms:** recursive oracle, memoization, tabulation, grid/knapsack/string DP, reconstruction, space optimization

### Staged change pressure

1. Start with an exponential recurrence and enumerate its decision tree.
2. Memoize the exact state, then tabulate in a justified dependency order.
3. Add reconstruction of one optimal decision sequence.
4. Optimize space and demonstrate which dependencies make an in-place update safe or unsafe.

### Core invariants

- A state contains all information the future needs and no history that cannot affect the answer.
- Every transition points to a strictly smaller or previously evaluated state.
- Base cases cover the boundary of the state space, not merely sample inputs.
- Space optimization preserves every dependency needed before overwrite.

### Seeded defects

- Memoization key omits a state dimension.
- A tabulation loop evaluates consumers before dependencies.
- Forward iteration accidentally turns 0/1 knapsack into unbounded knapsack.
- Reconstruction reads a compressed row that no longer retains parent decisions.

### Adversarial tests and oracle

Use exhaustive recursive enumeration on tiny inputs and compare memoized, tabulated, and optimized forms; enumerate all decisions when the output includes a reconstruction.

### Required visual traces

- recursion tree to DAG collapse
- state and transition table
- evaluation-order arrows
- before/after row-compression dependency diagram

### Refactoring checkpoint

Separate problem-specific transition logic from trace/reporting utilities without inventing a universal DP framework.

### Rejected alternatives

- Memorizing recurrence templates hides state derivation.
- A generic multidimensional memo wrapper cannot decide the correct state or evaluation order.

### Complexity analysis

Use state-count × transition-cost, then account separately for reconstruction, memo keys, recursion stack, and compressed storage.

### Senior interview walkthrough

- Derive a state live from a changed requirement.
- Explain why greedy or backtracking alone is insufficient.
- Identify which state dimension can and cannot be removed.

### Definition of done

- [ ] At least four DP families progress from brute force through memoization and tabulation.
- [ ] Each family includes one wrong-state or wrong-order seeded defect.
- [ ] One reconstruction and two space optimizations are verified against the oracle.
- [ ] Rahul can derive rather than recite the state and transition in the final walkthrough.
- [ ] Tests and commands actually run are recorded without fabricated results.
- [ ] Evidence is linked in `PROGRESS.md` without automatic unit-state inflation.


<a id="dsa-prj-070"></a>
## `DSA-PRJ-070` — Mixed interview simulator and error-analysis dashboard

**Purpose:** Run renewable unlabeled interviews, preserve hint and reasoning evidence, and turn delayed outcomes into a focused revision queue.

**Required prerequisites:** `DSA-SYN-060`, `DSA-SYN-070`, `DSA-FND-090`, `DSA-FND-100`

**Recommended prerequisites:** `DSA-PRJ-020`

**Integrated structures and algorithms:** unlabeled reserve selection, mock timing, scoring, hint ledger, error taxonomy, spaced review, readiness trends

### Staged change pressure

1. Select non-overlapping Easy/Medium reserve sets without exposing owner, pattern, invariant, or target complexity.
2. Record problem restatement, brute force, bottleneck, invariant, code, tests, hints, and rubric dimensions independently.
3. Add changed-constraint follow-ups and a delayed re-solve scheduler.
4. Produce readiness summaries that preserve raw evidence instead of converting one Accepted result into mastery.

### Core invariants

- A learner-facing mock record never reveals hidden pattern metadata before postmortem.
- Every hint has a timestamp, level, and effect on the next review interval.
- A problem attempt and a unit learning state remain separate records.
- A readiness aggregate is reproducible from underlying scored attempts and never claims hiring certainty.

### Seeded defects

- The reserve selector repeats a recently used problem while claiming a fresh set.
- A pattern label leaks through a filename or report field.
- An Accepted submission automatically marks the owning unit Demonstrated.
- Review scheduling ignores repeated invariant or boundary failures.

### Adversarial tests and oracle

Use deterministic seeded selection and hand-computed rubric fixtures; cross-check aggregate metrics against raw attempt records rather than an algorithmic answer oracle.

### Required visual traces

- interview timeline with hint events
- error-category heat map
- review queue by due date
- readiness trend with sample size and uncertainty

### Refactoring checkpoint

Separate hidden metadata, learner-facing prompt data, scoring evidence, and reports so presentation cannot accidentally leak answers.

### Rejected alternatives

- A single total score hides whether the weakness is algorithm choice, proof, code, or communication.
- Company-tag frequency and a large solved count are not reliable readiness measures.

### Complexity analysis

Account for reserve filtering, scheduling, report aggregation, and storage growth; do not optimize before correctness and privacy boundaries.

### Senior interview walkthrough

- Conduct one full unlabeled mock and explain the smallest hint policy.
- Defend why an Accepted result does not imply retention.
- Interpret a readiness trend without overstating confidence or guaranteeing outcomes.

### Definition of done

- [ ] The selector can produce at least three non-overlapping 10-problem Easy/Medium sets before recycling.
- [ ] Pattern metadata is absent from all learner-facing pre-attempt output.
- [ ] Hint use, error categories, changed constraints, and delayed outcomes affect review scheduling.
- [ ] The dashboard can reconstruct every aggregate from evidence and contains no employment-guarantee language.
- [ ] Tests and commands actually run are recorded without fabricated results.
- [ ] Evidence is linked in `PROGRESS.md` without automatic unit-state inflation.
