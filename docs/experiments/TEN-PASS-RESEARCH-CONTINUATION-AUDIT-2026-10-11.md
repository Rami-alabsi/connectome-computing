# Ten-Pass Research Continuation Audit — 2026-10-11

> **Superseding update — 2026-10-11 after Run #55 completed:** the earlier status below was accurate at the time it was written but is now historical. Run #55 / workflow 38122390361 completed successfully, reached cumulative 64E (238,877,440 accepted swaps), and uploaded artifact 11702767144. Full run evidence and the subsequent 8E–64E curve-drift audit are recorded in [C2 Run #55 64E Completion Audit](https://github.com/Rami-alabsi/connectome-computing/blob/c2-run55-64e-completion-audit-2026-10-11/docs/experiments/C2-RUN-55-64E-COMPLETION-AUDIT-2026-10-11.md). The new full-curve comparison shows a systematic upward shift at every threshold from 16E→32E and 32E→64E; formal mixing/convergence and Gate C therefore remain OPEN. This update does not mean the sensitivity ladder was executed.

**Scope:** bounded documentation/review pass during C2 Run #55, without changing the running workflow, C2 kernel, graph, constraints, or scientific thresholds.

**Repository:** `Rami-alabsi/connectome-computing`

**Status at review:** Run #55 (`38122390361`), job `114419636270`, is still reported by GitHub as `in_progress`. The C2 benchmark step is active; the artifact-upload step is pending. No final artifact was listed at the time of this audit. A log-fetch attempt returned GitHub's `BlobNotFound`, so no claim is made about current progress beyond the available step/status data and the user-supplied resume logs.

## Ten review passes

### Pass 1 — Re-anchor the project compass
Reconfirmed the documented order: C2 replication and stability checks are completed as milestones; formal mixing/convergence remains open; C3 design/synthetic validation precedes any FAFB C3 run; Gate C and downstream structure→function, ablation, abstraction, benchmarking, and scaling remain blocked. No status gate was promoted in this review.

### Pass 2 — Verify the reported C2 resume point
The user-supplied run log reports:
- `resumed_from_attempt=2053048908`;
- `accepted_swaps=119438720`;
- edge list, edge set, and distance-bin list each have 3,732,460 entries;
- the bucket builder reports 3,648 block-pair buckets;
- the resumed state was released after load.

These values match the documented end of the 32E checkpoint. This is strong evidence that the running process resumed the intended chain. The GitHub API's completed “Download optional C2 resume checkpoint” step alone would not prove this; the process log values are the stronger evidence.

### Pass 3 — Confirm the 64E target arithmetic
The planned 64E target is 238,877,440 accepted swaps. Starting from 119,438,720 leaves exactly 119,438,720 additional accepted swaps. This is a target count, not a runtime prediction.

### Pass 4 — Audit the early execution telemetry
The supplied sample shows accepted swaps increasing from 119,438,720 to 119,453,244 across the displayed attempts, so the sampling loop had begun making progress. The reported `attempts_per_second` values are inconsistent with the displayed attempt increments and elapsed times; they must not be used to estimate completion time until the instrumentation is audited. RSS maximum around 2,795 MB and current RSS around 2,027 MB are recorded as diagnostics, not proof of a memory fault.

### Pass 5 — Preserve the C2 scientific contract
The seven hard invariants remain frozen: edge count, in-degree sequence, out-degree sequence, source-block→target-block counts, global distance-bin histogram, no self-loops, and no duplicate directed edges. No proposal was made to relax constraints or alter the kernel for speed. Final artifact checks are still required to establish the completed run's invariants and measurements.

### Pass 6 — Review the positive-control evidence boundary
The existing synthetic positive control demonstrates recovery/erasure of a large planted club effect under the C2 constraint geometry. It does not quantify sensitivity to small effects, prove FAFB signal, prove mixing, or close Gate C. The next useful synthetic study is a predeclared effect ladder with a negative control, not a retrospective threshold adjustment.

### Pass 7 — Improve the sensitivity-ladder preregistration
The draft PR #7 plan was tightened before any sensitivity outcomes were generated:
- froze base-graph seeds to 20261011–20261030;
- specified deterministic null-seed derivation;
- set an initial 100,000-proposal budget per null, matching the historical synthetic pilot budget;
- clarified that the design entails 2,280 null realizations;
- replaced vague “95th percentile” wording with an explicit rank rule (observed club edge count strictly greater than all 19 null values);
- warns that 19 nulls provide coarse tail resolution and do not, by themselves, establish a calibrated 5% test.

This is a protocol proposal only. The first complete replicate should be benchmarked before dispatching the full ladder. If code-path compatibility or runtime requires changes, amend the protocol before inspecting sensitivity outcomes.

### Pass 8 — Audit cross-family turnover comparability
The merged cross-family turnover audit documents that CFG, NPC-like, and spatial historical artifacts lack the original-edge-overlap/final-edge-set evidence required for a matched-turnover comparison. Acceptance rates and accepted-swaps-per-edge are not substitutes for matched turnover or a convergence diagnostic. This limitation remains open; no causal attribution of the residual solely to constraint families is warranted yet.

### Pass 9 — Keep C3-A behind its validation gates
C3-A remains a candidate, not a validated FAFB result. The next permitted work is code/protocol review, synthetic checks, and external reproduction of a published spatial/max-entropy baseline. Do not launch a full FAFB C3 run before those gates are documented as passed.

### Pass 10 — Execution decision and next actions
1. Leave Run #55 untouched while it is active.
2. Re-poll the run and job after a meaningful interval; retrieve the artifact when available.
3. Audit final accepted swaps, attempts, target status, all seven invariants, overlap, full `phi_norm` curve, artifact checksum, seed, code version, and constraint/input fingerprints.
4. Do not treat 64E completion alone as proof of convergence.
5. After the C2 artifact audit, decide whether the synthetic sensitivity pilot can run without competing for Actions capacity.
6. Keep PR #7 in draft until the protocol and implementation are reviewed; do not merge it as executed evidence.

## Current decisions

- **Run #55:** active in the last API snapshot; final artifact unavailable at this audit.
- **C2 64E:** target defined; formal convergence remains open.
- **Sensitivity ladder:** preregistration refined; not executed.
- **Cross-family matched-turnover audit:** still blocked by missing historical edge-overlap/final-edge-set data.
- **C3-A:** synthetic/external validation remains ahead of any FAFB run.
- **Gate C and downstream architecture claims:** open/blocked.

## Provenance and non-claims

This note is a review log, not a scientific result. It does not claim that ten experiments ran; it records ten bounded review passes over current state, telemetry, protocol design, and next-step controls. No new biological measurement, null realization, p-value, or convergence result was generated by these passes.
