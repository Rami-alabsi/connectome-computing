# C2 Checkpoint Performance Audit — 2026-09-29

## Status

**Performance gate: corrected; full C2 scientific run remains blocked until the new checkpoint path is validated on scale.**

This audit records a performance issue discovered after the resumable C2 checkpoint implementation was made correct.

## Finding

The resumable checkpoint serializes the complete C2 state, including:

- `edge_list`
- `edge_bins`
- counters
- checkpoint history
- `rng_state`

At the real graph scale (3,732,460 directed pairs), gzip level 9 made checkpoint writes disproportionately expensive.

Project scale test measurements:

| Checkpoint encoding | Measured write time |
| --- | ---: |
| gzip default / level 9 | ~26.0 s |
| gzip level 1 | ~2.3 s |
| uncompressed | ~1.1 s |

These measurements are implementation-performance evidence, not scientific C2 results.

With the previous workflow setting `--checkpoint-every 100000`, checkpoint I/O could dominate sampler runtime because the sampler processes roughly 100,000 attempts on the order of one second under the previously observed environment.

## Correction

Commit `ab78ff247840a8650ead340997b0f6383b85fcc7` changed:

```python
gzip.open(tmp_path, "wb")
```

to an explicit low-overhead checkpoint setting:

```python
gzip.open(tmp_path, "wb", compresslevel=1)
```

The rationale is that checkpoint files are recovery artifacts, not archival artifacts. The existing atomic temporary-file replacement is retained.

Commit `958df2d115da46d47cbc95fa186697be904791f8` changed the C2 workflow checkpoint interval from:

```
100000
```

to:

```
5000000
```

At the previously observed ~85k–95k attempts/s, five million attempts represents roughly 53–59 seconds of sampler work between checkpoints. With the measured level-1 checkpoint write time of ~2.3 s, the expected checkpoint I/O fraction is only a few percent rather than dominating execution.

This is an estimate, not yet a new full-run measurement.

## Test coverage

Commit `8bc84eb74a19c22c1f462122a6630c2f44ffb356` adds:

1. A regression test asserting the default `save_c2_state(..., compresslevel=...)` is level 1.
2. An opt-in real-scale checkpoint benchmark using 373,246 edges (approximately one tenth of the 3,732,460-edge C2 graph).

The scale benchmark is intentionally disabled in ordinary CI and runs only with:

```
RUN_C2_PERF_TESTS=1
```

The ordinary CI run for this commit reached successful pytest execution; the workflow was still finalizing at the time of this audit.

## Scientific interpretation

This performance issue does **not** change:

- the C2 constraint surface,
- the proposal kernel,
- the seed,
- the accepted-swap target,
- any graph invariant,
- or the scientific interpretation of the completed C2 feasibility realization.

It only affects execution/recovery infrastructure.

The previous completed C2 #1 realization remains a valid feasibility result. It still lacks a final graph artifact because its original implementation did not persist the final edge list. Therefore it must not be retroactively treated as a C2 rich-club comparison.

The cancelled artifact-complete rerun remains a cancelled execution, not a scientific null.

## Next gate

Before launching the full 3,732,460-accepted-swap C2 null:

1. Run the opt-in checkpoint performance benchmark on CI or equivalent environment.
2. Confirm the new level-1 checkpoint write time and checkpoint file size are acceptable.
3. Confirm the five-million-attempt interval is operationally safe.
4. Then run C2 with the fixed seed `20260935`, target `3,732,460`, and the current exact constraint fingerprint.
5. Preserve the resulting final JSON **and** final checkpoint artifact.
6. Only after a completed graph artifact exists, compute and audit the C2 rich-club comparison.

No C2 scientific conclusion should be advanced from checkpoint-performance measurements.
