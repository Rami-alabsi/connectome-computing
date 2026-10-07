# C2 INDEPENDENT SEED ENSEMBLE PLAN — 2026-10-07

## Purpose

Extend the artifact-complete C2 joint NPC-like + arbor-distance-bin null from one realization to an independent seed ensemble without changing the declared null model.

This is the next biological-control experiment after C2 Run #45.

## Current source of record

Primary C2 realization:

- Workflow run: `37573133004`
- Job: `112636019092`
- Commit: `59db12b97023e4e8258b4a9948e810ac0895c66c`
- Seed: `20260935`
- C0 source run: `36318477728`
- Artifact ID: `11461697865`
- Artifact SHA-256: `cb185da57f64467ecb1197f77062c510fd6f3e0c94a6c8e46689090709b9c97a`
- Attempts: 55,361,441
- Accepted swaps: 3,732,460
- Acceptance rate: 6.7419849%
- Maximum phi_norm: 1.0076220771931181 at threshold 51
- No threshold exceeded phi_norm > 1.01
- Original-edge overlap fraction: 0.47913761969317825

Run #45 is artifact-complete realization #1. It is not an ensemble result.

## Fixed C2 definition

All independent seeds MUST use exactly:

- FAFB v783
- authoritative Princeton C0 source
- min_synapses = 5
- unique directed pairs = 3,732,460
- exact edge count
- exact in-degree sequence
- exact out-degree sequence
- exact source-block → target-block counts for edges with complete dominant block assignment
- exact global arbor-distance-bin histogram
- no self-loops
- no duplicate directed edges
- edges without complete dominant block assignment frozen
- current block-pair-stratified proposal kernel
- same target: 3,732,460 accepted swaps

Do NOT strengthen, weaken, or otherwise alter the primary C2 constraint surface for this ensemble.

## Workflow preparation

The C2 workflow was updated so the RNG seed is an explicit manual-dispatch input rather than a hard-coded value:

- workflow commit: `0c8debaf121e1207ee90246b9e674f6d27b7f545`
- default seed remains `20260935` for backward-compatible reproduction of Run #45
- independent runs can now use deterministic seeds `20261001` and `20261002` without changing the sampler or constraint surface
- workflow remains `workflow_dispatch` only; this change does not launch a scientific run by itself.

## Independent seeds

Recommended next realizations:

1. Seed `20261001`
2. Seed `20261002`

The existing realization with seed `20260935` remains the reference realization.

At least two additional independent seeds are preferred before making a Gate-C interpretation. More seeds may be added if the ensemble remains unexpectedly narrow, unstable, or anomalous.

## Required outputs per seed

Each completed realization must retain:

1. final JSON result;
2. resumable C2 state artifact;
3. artifact SHA-256;
4. full rich-club curve, thresholds 20–120;
5. maximum phi_norm and threshold;
6. whether any threshold exceeds 1.01;
7. onset/offset/peak descriptors;
8. acceptance trajectory across checkpoints;
9. final acceptance rate;
10. invalid/duplicate/self-loop count;
11. distance-bin rejection count;
12. block rejection count;
13. frozen-edge count;
14. exact invariant results;
15. original-edge overlap fraction.

## Non-invasive mixing / stability diagnostics

These diagnostics MUST NOT change the C2 sampler or its stationary target.

For each seed, record:

- early/mid/late acceptance trajectory;
- cumulative acceptance-rate change;
- edge turnover relative to the observed graph;
- pairwise edge overlap/Jaccard between completed C2 realizations;
- rich-club curve agreement across seeds;
- maximum-phi variation and peak-threshold variation;
- whether the descriptive >1.01 region appears, disappears, shifts, or reverses.

Where final graphs are available, compare edge sets directly. Do not infer mixing from acceptance rate alone.

A high overlap between independent final graphs is not automatically evidence of poor mixing: the constrained state space itself may be narrow. Conversely, low overlap is not automatically proof of good mixing. Interpret turnover jointly with rich-club stability and constraint geometry.

## Decision rules

### A. Stable C2 ensemble

If independent seeds show similar rich-club curves and similar peak behavior, with meaningful edge turnover and no implementation anomalies:

- C2 becomes a stronger ensemble control.
- Proceed to the stronger spatial/max-entropy sensitivity family.
- Then perform the Gate-C decision.

### B. Persistent disappearance of >1.01

If independent C2 seeds repeatedly show no >1.01 region:

- treat the joint NPC + spatial constraints as a strong candidate explanation for the earlier residual;
- do NOT call it a mechanism;
- do NOT call it statistically significant;
- complete the stronger spatial sensitivity and mixing audit before Gate C closure.

### C. Persistent residual

If independent C2 seeds retain a >1.01 region:

- this becomes a higher-priority structural residual;
- verify independent seeds and invariants;
- compare the full curve against CFG/NPC/spatial controls;
- then move toward matched computational ablations and targeted prior-art review.

### D. Shape shift

If the C2 ensemble changes onset, offset, peak location, or curve shape substantially:

- treat the shape change as a discovery/control signal;
- verify implementation and independent seeds before interpretation.

### E. Reversal or anomalous realization

If a seed produces an unexpected reversal or qualitatively incompatible result:

- preserve the artifact;
- do not discard it;
- audit invariants, provenance, RNG continuity, and rich-club calculation;
- replicate with an independent seed before proposing a biological explanation.

## Gate-C boundary

No Gate-C closure is permitted from Run #45 alone.

The required sequence remains:

**C2 independent seeds → mixing/stability audit → stronger spatial/max-entropy sensitivity → Gate-C decision → only then structure→function.**

## Provenance rule

Every completed seed must receive its own experiment record before its result is used in a scientific conclusion.

Failed, cancelled, diagnostic, or superseded runs remain in the historical record and must not be silently relabeled as scientific nulls.


## Operational checkpoint — 2026-10-07

Repository/workflow audit performed after the ensemble preparation.

- Latest C2 workflow run remains Run #45 (37573133004); no C2 workflow run for seed 20261001 or 20261002 exists yet.
- Latest ordinary repository CI run after the preparation is successful (37579658417).
- The C2 workflow is confirmed workflow_dispatch only; the current GitHub connector exposes no workflow-dispatch action, so no seed run was launched by this audit.
- The current workflow file exposes seed as an explicit required dispatch input and retains the same C2 sampler/constraint definition.

### Dispatch values — Seed 20261001

- c0_run_id = 36318477728
- seed = 20261001
- attempts = 60000000
- target_accepted = 3732460
- resume_run_id = empty
- resume_artifact_name = empty
- trace_attempts = 0
- skip_finalization = false

### Dispatch values — Seed 20261002

Use the same values, changing only seed = 20261002.

Do not reuse Run #45's checkpoint for an independent seed: the independent-seed experiment must start from the observed graph with a fresh RNG seed. Any checkpoint created during a new seed run may be used only to resume that same seed and same constraint fingerprint.

### Audit gate before accepting either seed

A run counts as a scientific C2 realization only if the final artifact contains the final JSON and checkpoint, reaches target_reached=true, preserves every declared invariant, contains the full rich-club curve, records artifact provenance/digest, and has no unresolved execution/finalization anomaly. A cancelled/diagnostic/recovery run remains historical evidence only.


## Run #46 update — seed 20261001 completed

The independent seed phase now has two artifact-complete realizations: Run #45 (20260935) and Run #46 (20261001).

Run #46:
- workflow **37582335296**; job **112664615048**
- artifact **11466140681**; SHA-256 **d19aa6383818d30c4cd40d01e1cbc00db8d42af028c021052a5111d2edaec213**
- attempts **55,237,500**; accepted **3,732,460**; target reached **true**
- acceptance **6.7571125%**
- max phi_norm **1.0076660261640915** at threshold **50**
- no >1.01 region
- overlap **0.47912877833921863**
- all seven invariants preserved; frozen edges 9,869; block-pair classes 3,648.

This independently replicates the qualitative Run #45 outcome. The ensemble is still OPEN because the planned third seed is required before the Gate-C decision.

### Dispatch values — Seed 20261002

- c0_run_id = 36318477728
- seed = 20261002
- attempts = 60000000
- target_accepted = 3732460
- resume_run_id = empty
- resume_artifact_name = empty
- trace_attempts = 0
- skip_finalization = false

Do not reuse a checkpoint from Run #45 or #46. Start from the observed graph with the fresh seed 20261002. After completion, retain the final JSON, checkpoint, artifact digest, full curve, invariants, acceptance trajectory, and overlap.
