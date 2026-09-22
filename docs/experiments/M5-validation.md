# M5 Real FAFB Validation

## Objective

Test whether a synthetic graph can reproduce a selected set of measurable
structural properties of the real FAFB connectome, then progressively add
higher-order constraints.

## Reproducible sequence

1. Download the official FAFB v783 analysis resource using `src/ingestion/download_fafb.py`.
2. Build a streaming profile with `scripts/build_profile.py`.
3. Calibrate the first-order generator from the observed density.
4. Generate a synthetic graph at the same node/edge scale for a tractable baseline.
5. Measure the synthetic graph independently.
6. Compare observed vs synthetic with `src/generator/validation.py`.
7. Add degree-distribution, hub, modularity and motif constraints one at a time.
8. Repeat with ablations so each biological constraint can be tested independently.

## Important interpretation rule

A close structural match is not evidence of computational superiority.
A computational advantage is not evidence that the network is biologically faithful.
These claims must be tested separately.

## Current status

The pipeline code is prepared, but **no real FAFB result is recorded here yet**.
The dataset must be executed in an environment with network access and the official
Codex resource. Results must include dataset/version, resource name, seed, generator
configuration and comparison metrics.

## Novelty checkpoint

A potentially novel method/result may only be raised after a targeted prior-art
search against the exact method and after reproducible experiments with controls
and ablations. See `docs/novelty-tracker.md`.
