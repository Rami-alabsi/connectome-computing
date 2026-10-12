# C2 Run #56 — 128E Continuation Partial Audit
## Audit date: 2026-10-12

### Status and scope
- Workflow run: [#56 / 38204750622](https://github.com/Rami-alabsi/connectome-computing/actions/runs/38204750622)
- Job: 114665646123
- Commit: `c06ef737a5a45d41dbfd062e54ed9f1fe9d75ab7`
- Terminal status: **cancelled**, not successful.
- Sampling step was cancelled; the following artifact-upload step completed successfully.
- This is a **partial checkpoint audit**, not a completed 128E realization. No final result JSON was produced in the artifact, so no final rich-club curve, overlap, or seven-invariant result can be attributed to Run #56.

### Artifact verification
- Artifact name: `fafb-v783-c2-feasibility-9000000000`
- Artifact ID: `11740612480`
- Size: 46,268,143 bytes
- GitHub-reported ZIP SHA-256: `def6b8161ee641e7a1db122029b2123f06afe98fbf83c1dc76da333d421b7e6c`
- Independently downloaded ZIP SHA-256: **matches exactly**.
- ZIP contents: one file only, `c2-state.pkl.gz` (46,259,342 bytes); expected result file `c2-feasibility-9000000000.json` is absent.
- Checkpoint SHA-256: `5a1b7942b2ee18cee387a25f36c4d7ea8bfe2df3fecea8a31a982f48eb449b49`
- Artifact expiration reported by GitHub: 2027-01-10T04:40:37Z.

### Checkpoint contents verified locally
The checkpoint pickle was inspected after confirming it contains no GLOBAL/STACK_GLOBAL or object-construction opcodes. Parsed metadata:
- format version: 2
- seed: `20261002`
- attempt: `6,200,000,000`
- accepted swaps: `358,099,863`
- acceptance rate at checkpoint: `5.7758042%`
- code version: `890a73d18a8e3d4e006233b45d9dd2c5771fa849f69dc3d462ed7588af6ef076`
- constraint fingerprint: `b330c16977c084434c129086112cf75710f95b8c39af7fd4df57ab16a87d76e3`
- edge list length: 3,732,460
- unique edge count: 3,732,460
- edge-bin array length: 3,732,460
- self-loops in saved edge list: 0
- RNG state present; 1,248 checkpoint records present.
- Saved distance-bin counts: bin 0: 15,340; 1: 53,700; 2: 180,439; 3: 465,059; 4: 1,212,172; 5: 1,052,594; 6: 622,653; 7: 130,303; 8: 200.

A second independent comparison loaded the Run #55 checkpoint from its own artifact and compared its saved edge state to Run #56's saved checkpoint. Both carry the same seed and constraint fingerprint. The 3,732,460-edge count and uniqueness match; there are no self-loops; in-degree maps and out-degree maps are exactly equal; and the distance-bin histogram is exactly equal. Edge-set overlap between the saved 64E state and the partial Run #56 state is **20.8697%** (this is inter-state overlap, not overlap with the original observed graph). The Run #55 result JSON itself reports all seven invariants true. The final Run #56 block-pair counts were not independently recomputed because the artifact does not contain the authoritative block mapping/graph; do not describe all seven final invariants as independently revalidated.

The workflow log also shows that Run #56 successfully loaded the Run #55 state at attempt 4,128,211,946 / 238,877,440 accepted, and passed the runner's resume validation (edge count/uniqueness, distance-bin histogram, degree maps, block-pair counts) before entering the sampling loop.

### Last log line versus saved checkpoint
- Last supplied/logged probe: attempt 6,202,800,000; accepted 358,260,480.
- Saved checkpoint: attempt 6,200,000,000; accepted 358,099,863.
- Gap after checkpoint: 2,800,000 attempts and 160,617 accepted swaps.
- Target: 477,754,880 accepted swaps (128E).
- Remaining from checkpoint: 119,655,017 accepted swaps.
- Remaining from last log probe: 119,494,400 accepted swaps.

The artifact's checkpoint is the correct safe resume point visible in the saved state. Do not claim the later log counters were checkpointed. The cancelled run did not reach its 128E target.

### Interpretation and next action
1. Preserve Run #56 as a cancelled, partial same-chain continuation; do not mark 128E complete.
2. Before any continuation, verify available Actions quota and choose a bounded continuation plan. Resume from this artifact only after rechecking code/input/constraint fingerprints and the workflow's resume-validation behavior.
3. If resumed, ensure the workflow checkpoints often enough and uploads the checkpoint on cancellation; ideally improve result finalization so partial progress counters and checkpoint metadata are emitted even when the target is not reached.
4. Do not launch PR #7 sensitivity runs or parallel long C2 jobs before the run audit and compute-budget decision.
5. Formal mixing/convergence remains open. The saved checkpoint alone cannot support a rich-club conclusion or convergence claim.

### Evidence links
- Run #56: https://github.com/Rami-alabsi/connectome-computing/actions/runs/38204750622
- Artifact: https://github.com/Rami-alabsi/connectome-computing/actions/runs/38204750622/artifacts/11740612480
- Run #55 source checkpoint audit: `docs/experiments/C2-RUN-55-64E-COMPLETION-AUDIT-2026-10-11.md`
