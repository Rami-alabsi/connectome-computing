# C2 Runtime Anomaly and Checkpoint Hardening — 2026-09-29

## Purpose

Record the cancelled artifact-complete C2 rerun, identify the execution cause, and document the infrastructure hardening applied before the next scientific C2 realization.

## Event

The artifact-complete C2 rerun was workflow run `36523442690`.

The run used the same C2 sampler implementation and fixed seed as C2 full-null #1, but was cancelled after reaching the workflow job timeout.

The workflow itself contained:

```yaml
timeout-minutes: 180
```

This is a workflow-level timeout. The run therefore cannot be interpreted as a scientific failure of the C2 sampler or constraint surface.

## Important implementation finding

The previous `--checkpoint-every` mechanism did not create a resumable checkpoint. It only appended diagnostic dictionaries to an in-memory `checkpoints` list. The final JSON artifact was written only after the sampling loop completed.

Therefore, when a job was terminated before normal completion, no final artifact and no resumable sampler state were preserved.

This is an infrastructure/provenance defect, not a biological or statistical result.

## Hardening applied

The C2 workflow and sampler were updated to:

1. Increase the workflow timeout from 180 to 350 minutes.
2. Persist a compressed checkpoint state containing:
   - current edge list
   - distance-bin assignments
   - accepted/rejected counters
   - attempt count
   - Python RNG state
   - checkpoint history
   - seed/version marker
3. Write checkpoints atomically through a temporary file followed by replacement.
4. Validate resumed state before continuing:
   - seed consistency
   - edge count and uniqueness
   - degree maps
   - block-pair counts
   - distance-bin histogram
5. Add workflow inputs for a previous run ID and checkpoint artifact name.
6. Download an optional checkpoint artifact and resume from it when supplied.
7. Upload the result/checkpoint artifact with `if: always()` as a best-effort failure/cancellation preservation mechanism.

## Scientific interpretation

The cancelled run contributes **no C2 rich-club result** and is not a replicate.

C2 full-null #1 remains the previously completed feasibility realization with exact invariants, but its original artifact did not contain the final graph and therefore cannot be used for the intended observed-vs-C2 rich-club comparison.

The next C2 scientific realization must be run only after the hardened workflow passes its software tests and a short operational calibration confirms expected throughput.

## Decision

Do not aggregate the cancelled run with C2 nulls.

Do not change the C2 constraint surface because of this event.

Do not interpret runtime variation as biological or sampler evidence.

## Next action

1. Verify CI tests for the checkpoint/resume changes.
2. Run a short operational calibration.
3. If calibration is healthy, run the artifact-complete C2 realization.
4. Preserve the final graph/state and rich-club observable in the artifact.
5. Only then proceed to independent C2 seeds and Gate C evaluation.


## 2026-09-29 follow-up hardening

After the initial checkpoint hardening, the sampler was audited again.

- Checkpoints are now triggered at completed attempt boundaries, including rejected proposals; they are not restricted to accepted swaps.
- Resume state is bound to the SHA-256 hash of `scripts/run_fafb_npc_spatial_feasibility.py`, rather than the full repository commit, so workflow-only changes do not invalidate an otherwise identical sampler state.
- The repository test workflow passed after the checkpoint-boundary change: GitHub Actions run `36551224898`, conclusion `success`, head commit `6d14564872f4e0139b16021149df7589c6120f2c`.
- The sampler source was then updated to use the source-file hash as `--code-version`; this operational change does not alter the proposal kernel or scientific constraint surface.

Decision: do not launch the artifact-complete C2 scientific run until the hardened path is exercised by an operational calibration/resume check. The cancelled run `36523442690` remains a runtime/infrastructure anomaly and is not a scientific replicate.
