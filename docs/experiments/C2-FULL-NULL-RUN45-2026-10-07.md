# C2 FULL NULL — RUN #45 — 2026-10-07

## Purpose

Generate the first artifact-complete realization under the declared joint C2 constraint surface:

1. exact directed edge count;
2. exact in-degree sequence;
3. exact out-degree sequence;
4. exact source-block → target-block edge counts for edges with complete dominant block assignment;
5. exact global arbor-distance-bin histogram;
6. no self-loops;
7. no duplicate directed edges.

Edges without complete block assignment are frozen rather than removed.

## Provenance

- Repository: Rami-alabsi/connectome-computing
- Workflow run: 37573133004
- Job: 112636019092
- Commit: 59db12b97023e4e8258b4a9948e810ac0895c66c
- Seed: 20260935
- C0 source run: 36318477728
- Artifact ID: 11461697865
- Artifact SHA-256: cb185da57f64467ecb1197f77062c510fd6f3e0c94a6c8e46689090709b9c97a

## Execution

The realization resumed from the validated 55.3M checkpoint:

- start: 55,300,000 attempts
- accepted at resume: 3,728,657
- final attempts: 55,361,441
- final accepted swaps: 3,732,460
- target reached: true
- final acceptance rate: 6.7419849%

No sampler or null-definition change was made for this completion.

## Invariants

All declared C2 invariants passed:

- same edge count: true
- same in-degree: true
- same out-degree: true
- same source-block → target-block counts: true
- same global distance-bin histogram: true
- no self-loops: true
- no duplicate edges: true
- all invariants preserved: true
- frozen incomplete-block edges: 9,869
- block-pair classes: 3,648

## Artifact-complete rich-club result

Thresholds: 20 through 120.

- maximum phi_norm: 1.0076220771931181
- maximum threshold: 51
- no threshold exceeded phi_norm > 1.01
- onset above 1.01: none
- offset above 1.01: none
- original-edge overlap fraction: 0.47913761969317825
- null_count: 1

The artifact explicitly labels the comparison as descriptive single-null comparison and not a significance test.

## Interpretation boundary

The first complete C2 realization shows that, for this realized null, the joint NPC-like + spatial constraints remove the >1.01 descriptive rich-club region. The maximum normalized residual is approximately 0.762%.

This is a structural-control signal, not a mechanism claim, p-value, convergence claim, or computational-advantage claim.

The result must be replicated with independent seeds. The ensemble variance and mixing behavior remain unresolved.

## Decision

- C2 artifact-complete realization #1: CLOSED as an artifact/provenance milestone.
- C2 ensemble/mixing: OPEN.
- Gate C: OPEN.
- Structure → function: BLOCKED.

## Next experiment

Run at least two independent C2 seeds with the identical dataset, constraint surface, proposal kernel, and target. Record:

- full rich-club curve;
- maximum phi_norm and threshold;
- acceptance trajectory;
- edge overlap/turnover;
- non-invasive mixing diagnostics;
- exact invariants;
- artifact digest and provenance.

Do not modify the C2 constraint surface to improve runtime.

Unexpected outcomes are discovery candidates only after artifact verification and independent replication.
