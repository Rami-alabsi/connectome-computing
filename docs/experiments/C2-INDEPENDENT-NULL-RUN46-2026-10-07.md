# C2 INDEPENDENT NULL — RUN #46 — 2026-10-07

## Purpose

Independent replication of the artifact-complete C2 joint NPC-like + arbor-distance-bin null using a fresh RNG seed, with the same dataset, constraints, proposal kernel, and target as Run #45.

This is an independent C2 realization, not a new null definition.

## Provenance

- Workflow: FAFB v783 C2 NPC-spatial feasibility benchmark
- Workflow run: `37582335296` (Run #46)
- Job: `112664615048`
- Head commit: `e22a13c41b7a25191b8bbecce700acc00e22efd7`
- Seed: `20261001`
- C0 source run: `36318477728`
- Artifact ID: `11466140681`
- Artifact name: `fafb-v783-c2-feasibility-60000000`
- Artifact SHA-256: `d19aa6383818d30c4cd40d01e1cbc00db8d42af028c021052a5111d2edaec213`
- Artifact size: 46,217,738 bytes
- Resume checkpoint: none; independent run started from the observed graph with a fresh seed.

## Execution

- target accepted swaps: **3,732,460**
- final attempts: **55,237,500**
- accepted swaps: **3,732,460**
- target reached: **true**
- final acceptance rate: **6.757112468884363%**
- frozen edges without complete block assignment: **9,869**
- block-pair classes: **3,648**

The full run completed successfully and finalization completed without the Run #44 O(E²) membership problem.

## Exact invariants

All declared C2 invariants passed:

- same edge count: true
- same in-degree: true
- same out-degree: true
- same source-block → target-block counts: true
- same global distance-bin histogram: true
- no self-loops: true
- no duplicate directed edges: true
- all invariants preserved: **true**

## Rich-club result

The final artifact contains the full descriptive rich-club curve for thresholds 20–120.

- maximum `phi_norm`: **1.0076660261640915**
- peak threshold: **50**
- no threshold exceeded `phi_norm > 1.01`
- onset above 1.01: none
- offset above 1.01: none
- null_count: 1
- interpretation: descriptive single-null comparison; not a significance test

Original-edge overlap fraction:

- **0.47912877833921863** (~47.9129%)

## Direct comparison with Run #45

| Metric | Run #45 | Run #46 |
|---|---:|---:|
| Seed | 20260935 | 20261001 |
| Attempts | 55,361,441 | 55,237,500 |
| Acceptance | 6.7419849% | 6.7571125% |
| Peak phi_norm | 1.0076220772 | **1.0076660262** |
| Peak threshold | 51 | **50** |
| Any >1.01 | No | **No** |
| Original-edge overlap | 47.913762% | **47.912878%** |
| Frozen edges | 9,869 | 9,869 |
| Block-pair classes | 3,648 | 3,648 |

The two independent realizations show the same qualitative outcome and very similar quantitative peak behavior. The maximum phi difference is approximately 0.00004395, while the peak shifts by only one threshold.

The overlap fractions are extremely close but **not identical**; they differ by about 0.000884 percentage points. This is consistent with reporting them as close, not as exactly equal.

## Scientific interpretation boundary

Run #46 strengthens the Run #45 observation:

> Under the fixed joint NPC-like + spatial C2 constraint surface, the descriptive >1.01 rich-club region remains absent in an independent realization.

With two independent seeds, this is now stronger than a single-null observation, but it is still **not**:

- a formal significance test;
- a proof of mixing/convergence;
- a biological mechanism;
- evidence that the joint constraints are the unique explanation;
- a computational architecture advantage.

The replication is important because the disappearance of the >1.01 region was not confined to one RNG trajectory.

## Decision

- C2 artifact-complete realization #2: **CLOSED as an artifact/provenance milestone**.
- C2 independent-seed ensemble: **OPEN**.
- Gate C: **OPEN**.
- Structure→function: **BLOCKED downstream**.

## Next authorized experiment

Run the planned independent seed:

**20261002**

Use exactly the same:

- C0 source: 36318477728
- attempts: 60,000,000
- target_accepted: 3,732,460
- min_synapses: 5
- proposal kernel
- C2 constraint surface
- finalization enabled
- no resume from Run #45 or #46

After Run #47, compare all three complete curves and then perform the planned non-invasive mixing/stability audit before any Gate-C decision.

Unexpected persistence, shape shift, reversal, or anomalous turnover must be preserved as a discovery/control signal rather than discarded.
