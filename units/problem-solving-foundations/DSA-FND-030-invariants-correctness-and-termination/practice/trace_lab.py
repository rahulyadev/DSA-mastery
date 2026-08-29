"""Deterministic proof-state trace for DSA-FND-030.

The lab makes one loop's invariant, guard, exit reason, and ranking measure
observable on tiny inputs. Prefix checks and snapshots are instrumentation;
they are deliberately not part of the constant-space production algorithm.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LoopHead:
    """Observable state immediately before one guard evaluation."""

    step: int
    index: int
    processed_prefix: tuple[int, ...]
    current: int | None
    invariant_holds: bool
    guard_holds: bool
    variant: int
    action: str


@dataclass(frozen=True)
class TraceReport:
    """Complete trace plus the conclusion reached at the false guard."""

    values: tuple[int, ...]
    threshold: int
    rows: tuple[LoopHead, ...]
    result: int | None
    exit_reason: str


@dataclass(frozen=True)
class TransitionAudit:
    """Proof obligations for one proposed continuing transition."""

    index: int
    next_index: int
    invariant_before: bool
    guard_before: bool
    invariant_after: bool
    variant_before: int
    variant_after: int
    preserves_invariant: bool
    makes_strict_progress: bool


def loop_head_invariant(
    values: tuple[int, ...], threshold: int, index: int
) -> bool:
    """Check bounds and failed-prefix meaning at a teaching loop head."""

    return 0 <= index <= len(values) and all(
        values[position] < threshold for position in range(index)
    )


def trace_first_index_at_least(
    values: list[int], threshold: int
) -> TraceReport:
    """Trace the loop-head proof state for a first-valid-index scan."""

    stable_values = tuple(values)
    index = 0
    rows: list[LoopHead] = []

    while True:
        invariant_holds = loop_head_invariant(stable_values, threshold, index)
        if not invariant_holds:
            raise AssertionError("the supplied transition broke the loop invariant")

        in_bounds = index < len(stable_values)
        current = stable_values[index] if in_bounds else None
        guard_holds = in_bounds and current is not None and current < threshold
        variant = len(stable_values) - index

        if guard_holds:
            action = "advance"
        elif in_bounds:
            action = "return index"
        else:
            action = "return None"

        rows.append(
            LoopHead(
                step=len(rows),
                index=index,
                processed_prefix=stable_values[:index],
                current=current,
                invariant_holds=invariant_holds,
                guard_holds=guard_holds,
                variant=variant,
                action=action,
            )
        )

        if not guard_holds:
            if in_bounds:
                return TraceReport(
                    values=stable_values,
                    threshold=threshold,
                    rows=tuple(rows),
                    result=index,
                    exit_reason="current candidate satisfies the predicate",
                )
            return TraceReport(
                values=stable_values,
                threshold=threshold,
                rows=tuple(rows),
                result=None,
                exit_reason="input exhausted after every candidate failed",
            )

        previous_variant = variant
        index += 1
        if len(stable_values) - index >= previous_variant:
            raise AssertionError("the ranking measure did not strictly decrease")


def audit_transition(
    values: list[int],
    threshold: int,
    *,
    index: int,
    next_index: int,
) -> TransitionAudit:
    """Evaluate preservation and progress for one proposed body update."""

    stable_values = tuple(values)
    if not 0 <= index < len(stable_values):
        raise ValueError("index must identify a current input position")
    if not 0 <= next_index <= len(stable_values):
        raise ValueError("next_index must stay within the loop boundary")

    invariant_before = loop_head_invariant(stable_values, threshold, index)
    guard_before = stable_values[index] < threshold
    invariant_after = loop_head_invariant(stable_values, threshold, next_index)
    variant_before = len(stable_values) - index
    variant_after = len(stable_values) - next_index
    continuing_state = invariant_before and guard_before

    return TransitionAudit(
        index=index,
        next_index=next_index,
        invariant_before=invariant_before,
        guard_before=guard_before,
        invariant_after=invariant_after,
        variant_before=variant_before,
        variant_after=variant_after,
        preserves_invariant=continuing_state and invariant_after,
        makes_strict_progress=(
            continuing_state
            and 0 <= variant_after < variant_before
        ),
    )


def render_report(report: TraceReport) -> str:
    """Render one trace without making an elapsed-time claim."""

    header = (
        f"{'head':>4} {'i':>3} {'processed':<16} {'current':>8} "
        f"{'I':>3} {'guard':>6} {'V':>3} action"
    )
    divider = "-" * len(header)
    lines = [
        f"values={list(report.values)} threshold={report.threshold}",
        header,
        divider,
    ]
    for row in report.rows:
        current = "END" if row.current is None else str(row.current)
        lines.append(
            f"{row.step:4d} {row.index:3d} "
            f"{list(row.processed_prefix)!s:<16} {current:>8} "
            f"{'yes' if row.invariant_holds else 'no':>3} "
            f"{'true' if row.guard_holds else 'false':>6} "
            f"{row.variant:3d} {row.action}"
        )
    lines.append(f"result={report.result!r}; exit={report.exit_reason}")
    return "\n".join(lines)


def default_cases() -> tuple[tuple[list[int], int], ...]:
    """Return the fixed cases named in the prediction exercise."""

    return (
        ([2, 5, 1, 7], 6),
        ([6], 6),
        ([1], 6),
        ([], 6),
    )


def main() -> None:
    for case_number, (values, threshold) in enumerate(default_cases(), start=1):
        if case_number > 1:
            print()
        print(f"case {case_number}")
        print(render_report(trace_first_index_at_least(values, threshold)))

    print("\ntransition audits")
    for label, values, threshold, index, next_index in (
        ("correct", [1, 7], 6, 0, 1),
        ("skips candidate", [1, 7], 6, 0, 2),
        ("stutters", [1], 6, 0, 0),
    ):
        audit = audit_transition(
            values,
            threshold,
            index=index,
            next_index=next_index,
        )
        print(
            f"{label:15} preserve={audit.preserves_invariant!s:<5} "
            f"strict_progress={audit.makes_strict_progress!s:<5} "
            f"V:{audit.variant_before}->{audit.variant_after}"
        )

    print("\nTrace snapshots and invariant scans are teaching instrumentation.")


if __name__ == "__main__":
    main()
