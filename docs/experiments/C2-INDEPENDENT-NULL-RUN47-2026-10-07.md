# C2 INDEPENDENT NULL — RUN #47 — 2026-10-07

## Purpose

Third artifact-complete realization of the fixed C2 joint NPC-like + arbor-distance-bin null, using an independent RNG seed.

## Provenance

- Workflow run: **37617681244** (Run #47)
- Job: **112779897382**
- Head commit: **62d5f9fd0700eca281f4067bb0bf7c5fab922e87**
- Seed: **20261002**
- C0 source run: **36318477728**
- Artifact ID: **11481125143**
- Artifact SHA-256: **4850e27dcb285dcfa258a594241bb5c843d9bf295f65d807a77c55a51c47ce64**
- Artifact contains final JSON + checkpoint state.
- No resume checkpoint from another seed was used.

## Execution

- target accepted swaps: **3,732,460**
- final attempts: **55,264,717**
- accepted swaps: **3,732,460**
- target reached: **true**
- acceptance rate: **6.7537846977%**
- frozen edges without complete block assignment: **9,869**
- block-pair classes: **3,648**

## Exact invariants

All seven declared invariants passed:

- same edge count: true
- same in-degree: true
- same out-degree: true
- same source-block → target-block counts: true
- same global distance-bin histogram: true
- no self-loops: true
- no duplicate directed edges: true
- all invariants preserved: **true**

## Rich-club result

Full descriptive curve: thresholds 20–120.

- maximum phi_norm: **1.0077486180432564**
- peak threshold: **51**
- no threshold exceeded **1.01**
- onset above 1.01: none
- offset above 1.01: none
- null_count: **1**
- interpretation: descriptive single-null comparison; not a significance test
- original-edge overlap fraction: **0.4792729192007416** (~47.9273%)

## Three-seed comparison

| Metric | Run #45 | Run #46 | Run #47 |
|---|---:|---:|---:|
| Seed | 20260935 | 20261001 | **20261002** |
| Attempts | 55,361,441 | 55,237,500 | **55,264,717** |
| Acceptance | 6.7419849% | 6.7571125% | **6.7537847%** |
| Max phi_norm | 1.0076221 | 1.0076660 | **1.0077486** |
| Peak threshold | 51 | 50 | **51** |
| Any >1.01 | No | No | **No** |
| Edge overlap | 47.913762% | 47.912878% | **47.927292%** |
| Frozen edges | 9,869 | 9,869 | 9,869 |
| Block-pair classes | 3,648 | 3,648 | 3,648 |

Across all three independent realizations, the same qualitative result is reproduced: the descriptive >1.01 rich-club region is absent under the joint NPC-like + spatial C2 constraint surface.

The three maxima are tightly clustered around **1.00762–1.00775**, with peak thresholds **50–51**.

## Scientific interpretation boundary

Run #47 completes the planned three-seed replication set. This materially strengthens the C2 structural-control observation.

The evidence now supports the bounded descriptive statement:

> Across three independent C2 realizations using the same dataset, constraint surface, proposal kernel, and target, the descriptive rich-club residual remains below phi_norm = 1.01, with maxima tightly clustered near 1.0077.

This is still not:

- a formal statistical significance test;
- proof of Markov-chain mixing/convergence;
- proof that the joint constraints are the unique explanation;
- a biological mechanism;
- evidence of computational advantage.

The next scientific gate is therefore the planned **three-seed stability/mixing audit**, followed by the stronger spatial/max-entropy sensitivity family before a Gate-C decision.

## Decision

- C2 artifact-complete realization #3: **CLOSED**.
- Three-seed C2 replication set: **COMPLETE**.
- C2 ensemble/mixing audit: **OPEN**.
- Gate C: **OPEN pending stability/mixing + sensitivity checks**.
- Structure→function: **BLOCKED until Gate C is resolved**.

Unexpected or anomalous behavior in the three full curves must be retained as a possible discovery/control signal rather than discarded.
