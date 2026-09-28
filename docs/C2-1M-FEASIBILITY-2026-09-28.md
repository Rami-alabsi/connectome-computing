# C2 1M Feasibility Benchmark — 2026-09-28

## Purpose

Calibrate the corrected joint C2 sampler before committing to a full null ensemble.

C2 constraint surface:

- exact directed edge count;
- exact in-degree;
- exact out-degree;
- exact source-block → target-block edge counts for edges with complete dominant NPC-like block assignment;
- exact global arbor-distance-bin histogram;
- no self-loops;
- no duplicate directed edges;
- edges lacking complete dominant block assignment remain frozen.

## Provenance

- Dataset: FAFB v783
- Authoritative C0 source run: `36318477728`
- Authoritative C0 artifact: `10931780910`
- Workflow: `m2-fafb-c2-feasibility.yml`
- Workflow run: `36412132062`
- Run number: 13
- Commit: `ef6784d3d0c81fb5deff92b8cf0abca4f985c2bc`
- Seed: `20260935`
- Attempts: `1,000,000`
- Minimum synapses: `5`
- Checkpoint interval requested: `100,000`
- Proposal kernel: block-pair-stratified degree-preserving swap proposal with exact distance-bin acceptance check.

## Results

- Unique directed pairs: **3,732,460**
- Accepted swaps: **94,751**
- Acceptance rate: **9.4751%**
- Invalid/duplicate/self-loop proposals: **38,055**
- Block rejections: **0**
- Distance-bin rejections: **867,194**
- Block-pair classes: **3,648**
- Eligible pair choices: **213,055,629,164**
- Frozen edges without complete block assignment: **9,869**
- All invariants preserved: **true**

Preservation checks:

- same edge count: true
- same in-degree: true
- same out-degree: true
- same source-block → target-block counts: true
- same distance-bin histogram: true
- no self-loops: true
- no duplicate edges: true

Artifact:

- ID: `10964334557`
- name: `fafb-v783-c2-feasibility-1000000`
- uploaded ZIP SHA-256: `59542077648956b8922746e10c585d7ed46aa554beed8ed5a44f419e5da4c15d`

## Runtime

The GitHub Actions log places the sampler invocation from approximately 10:51:17.10 UTC to 10:52:47.96 UTC, giving a wall-clock interval of approximately **90.86 s**.

The emitted JSON contains an instrumentation anomaly: it reports only one checkpoint at 400,000 attempts despite `checkpoint_every=100000`, with 3.86 s elapsed. This checkpoint timing is inconsistent with the final wall-clock interval and is therefore not used for runtime inference.

A simple linear calculation from the final 1M pilot gives:

- provisional accepted-swap rate: 9.4751%;
- approximately 39.4M attempts for 3,732,460 successful swaps if the rate remained constant;
- approximately 1 hour of sampler time at the observed wall-clock throughput.

This is a **calibration estimate only**. Acceptance can change as the chain moves, so the estimate is not a guarantee for a full null.

## Scientific interpretation

This is a **feasibility/runtime benchmark only**.

It does not provide:

- a rich-club curve;
- a null ensemble;
- a p-value or formal significance test;
- a mechanism claim;
- a computational-architecture claim.

The result establishes that the corrected C2 move set can execute at million-attempt scale while preserving the declared joint constraints exactly.

## Decision

The previous ~6 h/null runtime estimate from the 100k benchmark is superseded as the current calibration point.

Do not weaken the NPC-like block constraint or arbor-distance-bin constraint.

Next experiment:

1. execute one full C2 null to **3,732,460 successful swaps**;
2. verify exact invariants and record realized attempts/runtime;
3. if the full null reaches target cleanly, proceed to multiple independent seeds for the joint-control ensemble;
4. keep stronger spatial/max-entropy sensitivity as a separate downstream control.

No rich-club interpretation is permitted until the full null artifact exists and is aggregated against the observed graph.
