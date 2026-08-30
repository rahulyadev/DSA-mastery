# Review Record — DSA-FND-060 Recursion, call stacks, and recursive complexity

| Field | Value |
|---|---|
| Unit note | [DSA-FND-060](README.md) |
| Progress | [PROGRESS.md](../../../PROGRESS.md) |
| Artifact state | Draft |
| Learning state | Not started |
| Last evidence | — |
| Next review | 1 day after first study, then adapt |
| Mastery badge | No |
| Strongest area | Not evaluated yet |
| Weakest area | Not evaluated yet |

Ask one question at a time. Record the original response and hint level before offering a
correction. Dates are anchored to actual study and retrieval, not the date the pack was created.

## Closed-book reconstruction questions

1. What does one recursive call promise, and what information must its caller retain?
2. Can you draw every call and return for a prefix total on `[4, -1, 6]`, with no notes?
3. What is the entry invariant, and what is the return contract in that trace?
4. Which base cases follow from allowing an empty input?
5. What strictly decreases, and why must every branch decrease rather than only the first?
6. How does a smaller correct answer prove the current result without circular reasoning?
7. What work does taking a new tail slice add beyond the arithmetic?
8. How do time, non-stack auxiliary, output, and recursion-stack space differ?
9. Why can equal-sized child calls be distinct invocations with distinct local state?
10. What would make iteration or an explicit stack preferable?
11. What is the difference between an execution tree and one active stack snapshot?
12. Why does a finite mathematical recurrence not establish safe execution at arbitrary depth?

## Delayed-recall questions

These are prompts, not completed evidence. Use new tiny values when repeating a question.
Shorten the interval after a hint, boundary error, proof gap, or unsupported cost claim.

### 1-day recall

1. Can you reconstruct the notebook core and a four-event call/return trace without notes?
2. What happens if a nonbase function body computes a child's answer but does not return it?
3. Can you explain why empty input must be considered before indexing?

### 3-day recall

1. Can you recover a precise return contract and termination measure for one of your own attempts?
2. How many calls and active frames occur when both halves of an eight-item input are processed?
3. What changes if each internal call also scans its entire subinput?

### 7-day recall

1. A synthetic routine makes three calls of size `n-1`, with a base at zero. How would you
   derive total work and maximum active depth without guessing from its name?
2. Can you reconstruct one implementation from its contract without consulting the old attempt?
3. Why might remembering repeated pure subproblems reduce calls but retain extra memory?

### 14-day recall

1. A previously shallow input can now contain hundreds of thousands of nested parts.
   What constraints must you re-evaluate before coding?
2. Can you explain the necessary pending state without using the words “recursion” or “stack”
   for the first minute?
3. If every child returns a large list, what storage might remain alive during the next child?

### 30-day recall

1. A new routine divides its input into unequal parts. What measurements and proof obligations
   would you establish before writing a recurrence or claiming logarithmic depth?
2. Can you teach the difference between total allocated storage and peak live storage using
   an original tiny example?
3. What do the two experiments show directly, what can be inferred from their counts, and what
   can their traced byte measurements not establish?

| Planned interval | Actual date | Closed book? | Hint level | Evidence link | Result / next interval |
|---|---|---|---|---|---|
| 1 day after first study | — | Not attempted | — | — | Not evaluated |
| 3 days | — | Not attempted | — | — | Not evaluated |
| 7 days | — | Not attempted | — | — | Not evaluated |
| 14 days | — | Not attempted | — | — | Not evaluated |
| 30 days | — | Not attempted | — | — | Not evaluated |

## Interview retrieval

1. What constraint makes a smaller-instance decomposition meaningful?
2. What is a simplest correct baseline, and which repeated operation is its bottleneck?
3. What invariant or return contract is sufficient to justify each combination step?
4. Why is the coverage complete, and what positions or states can this call safely ignore?
5. How do you derive time from local work and child calls, rather than source-code length?
6. What are maximum active depth, retained-data space, and output space for your implementation?
7. Which Python operation could change your recurrence even when the call structure stays the same?
8. What would you change for deep inputs, one-pass input, or large returned outputs?
9. Why is raising the recursion limit not a general resource-safety argument?
10. What does Python 3.14's internal tail-call interpreter actually imply for a Python recursive function?

## One-question-at-a-time evidence record

### Question 1

For a list total on `[4, -1, 6]`, what does the call for the first two elements promise,
and exactly what must its caller do after that answer returns?

**Rahul's answer:** Not attempted yet.

**Correct reasoning:** Record only after Rahul answers.

**First missing step:** Record only after Rahul answers.

**Smallest recovery hint:** Give only if requested or needed during an agreed review.

**Attempt date and elapsed time:** Not recorded.

**Confidence before feedback:** Not recorded.

## Evidence

| Link | Result | What it proves | Remaining limitation |
|---|---|---|---|
| — | Not attempted | No learning evidence yet | Initialization and maintenance runs do not prove learning |

For each later entry, link the preserved attempt or trace, give the actual date and result,
state whether notes were closed, record hints, and name the exact capability demonstrated.
Do not turn a test run or an Accepted submission into a unit state automatically.

## Error log update

| Category | Exact failure | Corrective drill | Review interval |
|---|---|---|---|
| — | Not evaluated | Complete the first closed-book trace and record the first gap | 1 day after first study |

Useful categories include input interpretation, base cases, decreasing measure, return meaning,
coverage/proof, total-work analysis, active-depth analysis, retained data, Python behavior, and
communication. Add a category only when there is evidence of that failure.

## State decision

Recommended state: **Not started**.

The initialized Draft pack provides material and unsolved exercises. Rahul has not yet recorded
a prediction, implementation attempt, explanation, or delayed retrieval. Publication does not
change that fact.

Later decisions must follow the [tracker's evidence gates](../../../PROGRESS.md#evidence-gates):
engagement for Learning; required attempts and explanations for Practiced; successful closed-book
retrieval after at least one day for Recalled; an unseen variation for Demonstrated; repeated
later retrieval for Retained. A failed review may justify lowering a state. No badge is assumed.
