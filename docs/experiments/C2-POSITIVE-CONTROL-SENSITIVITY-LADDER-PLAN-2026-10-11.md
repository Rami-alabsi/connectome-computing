# C2 Positive-Control Sensitivity Ladder — Preregistered Plan (2026-10-11)

## Status and scope

**Status: PLAN ONLY — not executed.** This document specifies an independent synthetic sensitivity experiment. It does not alter the C2 kernel, its seven hard constraints, any FAFB artifact, or the active C2 64E continuation. No result or power claim is made until an execution artifact is inspected.

The existing positive control showed that the unchanged C2 constraint geometry can erase a deliberately planted large fixed-club signal (36 to 86 internal edges) while preserving all seven C2 statistics. That is a useful positive control, but it does not quantify sensitivity to smaller signals. This plan addresses that gap.

## Questions

1. What is the smallest planted fixed-club excess that the current C2-constrained null pipeline can reliably distinguish in this synthetic setup?
2. Does the answer vary across independently generated base graphs?
3. Does the analysis maintain a calibrated false-positive rate when no signal is planted?

This is a synthetic method-validation experiment only. It cannot establish a biological effect in FAFB, C2 convergence, or Gate C closure.

## Frozen constraints and construction

Use the same conceptual C2 constraints and acceptance rules as the existing positive-control execution:

1. exact directed edge count;
2. exact in-degree sequence;
3. exact out-degree sequence;
4. exact source-block → target-block counts;
5. exact global distance-bin histogram;
6. no self-loops;
7. no duplicate directed edges.

Retain the existing synthetic scale and heterogeneous constraint geometry as the initial reference: N=80, two source/target blocks, three distance bins, fixed club size 12. The fixed club membership is defined once from each base graph's total-degree ranking before planting and is held fixed for every observed/null curve for that replicate. Use the existing C2-valid swap construction; do not relax constraints to reach a target.

Before the full ladder, confirm that the existing large-effect case reproduces its prior invariant checks and that the zero-effect path leaves the base graph unchanged. If the implementation cannot add the requested number of fixed-club internal edges exactly while preserving all constraints, record that as a construction limitation rather than silently substituting a different effect.

## Preregistered effect ladder

Define effect size as the **absolute increase in directed edges internal to the fixed club**, relative to the same base graph:

| Condition | Target fixed-club edge change | Purpose |
|---|---:|---|
| Negative control | 0 | False-positive/calibration check |
| Small 1 | +1 edge | Near-minimal detectable change |
| Small 2 | +2 edges | Small-effect sensitivity |
| Small 5 | +5 edges | Intermediate sensitivity |
| Small 10 | +10 edges | Stronger, but below the existing +50 case |
| Historical positive control | +50 edges | Large-effect implementation anchor |

These are absolute edge increments, not percentages of all graph edges. Report the baseline fixed-club edge count for each base graph so relative effect sizes remain transparent. The historical +50 condition is an anchor and must not be used to tune the smaller-effect thresholds after outcomes are seen.

## Replication and null procedure

- Use 20 predeclared independent synthetic base-graph seeds. Record the seed list before generating or inspecting outcomes.
- For each base graph, run all six conditions using the same graph, fixed club, block labels, distance-bin assignments, and C2 kernel.
- For each condition, generate 19 independently seeded C2-constrained null realizations. Keep the null-seed derivation deterministic and recorded.
- Use the same proposal-attempt budget for nulls within this synthetic experiment, and record accepted swaps, attempts, acceptance rate, and whether the budget was reached. Do not compare acceptance rate as a mixing-speed estimator.
- First benchmark one complete base-graph replicate. If runtime or construction failures require changing the plan, stop and version a revised protocol before inspecting sensitivity outcomes.

The 20 × 6 × 19 design is a proposed replication target, not an assertion that these runs have occurred. Any reduction must be documented as a protocol deviation before result inspection.

## Primary outcomes

For each base graph and condition, archive:

- baseline and planted fixed-club internal-edge counts;
- complete fixed-membership rich-club curves for the planted graph and every null;
- all seven invariant checks for base, planted, and null graphs;
- accepted swaps, proposal attempts, acceptance rate, seed, and target/budget status;
- the distribution of null fixed-club edge counts and the observed planted value;
- the predeclared descriptive phi_norm curve and its maximum, with no reliance on the maximum alone;
- exact software/code version and artifact digest.

Primary sensitivity summaries:

1. fraction of independent base graphs for which the planted fixed-club edge count exceeds the 95th percentile of its 19-null distribution;
2. corresponding false-positive fraction for the zero-effect negative control;
3. the complete effect-versus-detection curve, with uncertainty across base graphs;
4. full-curve separation summaries, reported alongside—not replaced by—the fixed-club edge-count outcome.

With 19 nulls, the empirical tail resolution is coarse. State that limitation explicitly; do not report a precise p-value unsupported by the finite null count. The percentile-based fraction is a pilot sensitivity summary, not a universal guarantee of statistical power.

## Acceptance and interpretation rules

- **Implementation validity:** all seven C2 invariants pass for every accepted base/planted/null graph; the fixed club is unchanged within a replicate; the requested effect is achieved exactly or the replicate is marked a construction failure.
- **Negative control:** report its false-positive fraction as observed, even if it is inconvenient. Do not tune the detector or thresholds after seeing it.
- **Sensitivity:** report the observed detection fraction separately at +1, +2, +5, +10, and +50 edges. Do not collapse them into a single PASS/FAIL label.
- **Calibration warning:** if the negative-control false-positive fraction is high, smaller-effect detection estimates are not interpretable as clean power.
- **Failure is a result:** inability to plant tiny increments under the constraints, or failure to recover them, identifies a limit of this synthetic construction or observable. Do not silently increase effect size and retain the original label.
- **No biological inference:** even excellent synthetic sensitivity does not establish that the FAFB residual is meaningful, that C2 has mixed, or that Gate C is closed.

## Relationship to current C2 64E run

The active C2 extended chain remains the priority execution and must not be modified or cancelled for this plan. This sensitivity ladder is a separate future synthetic workflow. It should be dispatched only after reviewing the 64E outcome and checking available Actions capacity; if it competes with the long-running job, defer execution and keep this document as a preregistration.

## Required report

The result record must distinguish:
- protocol compliance;
- construction success/failure;
- exact invariant validation;
- sensitivity by effect size;
- negative-control calibration;
- runtime and acceptance diagnostics;
- scientific interpretation and explicit non-claims.

Update docs/PROJECT-STATUS.md and the relevant evidence ledger only after the execution artifact has been inspected. Until then, this file is a plan, not evidence.
