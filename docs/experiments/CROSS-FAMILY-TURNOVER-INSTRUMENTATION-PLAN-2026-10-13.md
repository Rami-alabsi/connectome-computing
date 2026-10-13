# Cross-family turnover instrumentation — code audit and next implementation gate

**Date:** 2026-10-13  
**Status:** static code audit complete; implementation and prospective measurements remain OPEN.  
**Purpose:** make the CFG → NPC-like → spatial → C2 comparison auditable without changing any null-family constraints or interpreting missing historical data as known.

## What was checked

The current main versions of these runners were inspected:

| Family | Runner | Current observed-edge overlap / final edge-state accounting |
|---|---|---|
| CFG / degree-preserving | `scripts/run_fafb_rich_club.py` | The runner computes a null graph and degree-preservation reports, but its JSON output does not report original-edge overlap, a canonical final-edge fingerprint, or the final edge set. |
| NPC-like / block-preserving | `scripts/run_fafb_npc_rich_club.py` | The runner constructs edge lists and reports degree/block preservation, but the current output does not report original-edge overlap, a canonical final-edge fingerprint, or the final edge set. |
| Spatial / distance-bin preserving | `scripts/run_fafb_spatial_rich_club.py` | The runner constructs `edge_list` and `edge_set` and checks constraints, but the current result does not report original-edge overlap or a canonical final-edge fingerprint. |
| C2 / NPC-like + spatial | `scripts/run_fafb_npc_spatial_feasibility.py` | Already reports `original_edge_overlap_fraction`, input and constraint fingerprints, milestone observables, and the seven declared invariants. Its result/checkpoint path is materially more auditable than the three historical aggregate families. |

This is a **code-level inspection**, not a new experiment. No historical overlap values are inferred or backfilled. Existing CFG/NPC-like/spatial aggregate artifacts still lack the final edge sets needed to reconstruct the missing quantities.

## Required instrumentation contract

For each future representative null, report all of the following in its own result JSON:

1. **Provenance:** dataset/version, minimum-synapse threshold, seed, runner/code version, input fingerprint, explicit constraint fingerprint, and run/artifact IDs in the external experiment record.
2. **Observed-edge overlap:** intersection(original edge set, final edge set) divided by the original edge-set size; also report intersection count, original/final edge counts, and changed-edge count. Define changed-edge count explicitly and consistently (recommended: number of original edges absent from the final state; do not label it as symmetric difference).
3. **Final-state identity:** deterministic SHA-256 over a documented canonical serialization of sorted directed edge pairs. The same graph must hash identically regardless of in-memory set iteration order.
4. **Effort and kernel:** attempts, accepted swaps, acceptance rate, rejection counters where available, and accepted swaps per original edge.
5. **Constraint audit:** all family-specific invariants, explicit booleans, and fail-closed behavior if any invariant fails.
6. **Retention:** keep final edge-state evidence for the bounded diagnostic in an artifact when size/retention permits; at minimum retain canonical fingerprint and overlap metrics. Do not silently change the null distribution merely to facilitate logging.

## Validation before any expensive workflow

- Add small synthetic-graph tests for overlap = 1.0 when unchanged, 0.0 for disjoint same-sized directed edge sets, and a known partial overlap.
- Add a determinism test proving edge-state fingerprints do not depend on set/list order.
- Test that a deliberately broken invariant fails the run rather than emitting a success-shaped result.
- Run syntax/pytest and targeted tests on the modified runners before dispatching any full-data workflow.
- Use one bounded representative run per family first: short CFG diagnostic; NPC-like and spatial capped at approximately 20–25 minutes each, subject to the available budget.
- Compare families at both accepted-swaps-per-edge and matched observed-edge-overlap levels where attainable. Preserve the complete rich-club curves and all constraint fingerprints.

## Interpretation boundary

Observed-edge overlap is a **state-memory/turnover descriptor**, not a convergence statistic. Accepted swaps per edge is an exposure normalization, not matched turnover. Neither quantity alone establishes stationarity, mixing, statistical significance, or causal effects of individual constraints. Because the proposal kernels and constraint surfaces differ, any cross-family comparison must state those differences and retain the full trajectory/curve evidence.

**Next authorized action:** implement and test this instrumentation without changing CFG, NPC-like, spatial, or C2 scientific constraints; then run bounded prospective diagnostics. Do not launch another long C2 continuation or full C3-A run as a substitute for this evidence gap.
