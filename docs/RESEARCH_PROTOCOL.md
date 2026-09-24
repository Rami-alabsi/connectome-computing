# Connectome Computing — Research Protocol and AI Handoff

## Purpose
This is the primary operational handoff document for future human or AI contributors. Read it before changing the research pipeline. It records the scientific question, provenance, current stage, evidence rules, replication gates, and non-negotiable interpretation constraints.

## Scientific question
Can measurable organizational principles in a biological connectome be separated from generic consequences of degree, sparsity, and mesoscale anatomy, and then translated into computational abstractions that can be benchmarked?

Required chain:
biological observation → controlled null model → surviving structural constraint → computational abstraction → benchmark

Connectivity alone is not treated as proof of function.

## Current stage
M5 → M6: synthetic connectome validation and effective-state interface prototyping.
The immediate blocking gate is closure of the FAFB rich-club replication/validation sequence.

## Dataset provenance
Primary current dataset: FlyWire FAFB, Female Adult Fly Brain, snapshot v783.
Current public Codex description: 139,255 neurons and 3,732,460 connections.
FlyWire states that v783 corresponds to the October 2023 public snapshot.
The repository downloads connections_princeton.csv.gz from the public FlyWire storage path pinned in scripts/download_fafb.py.

### Critical version distinction
Lin et al. performed the network-statistics analyses on v630, not v783. Their v630 snapshot contained 127,978 neurons and 2,613,129 thresholded connections.
Therefore v783 results are not an exact reproduction of the published v630 dataset. They are a method-aligned replication/extension on v783 unless a v630 input is explicitly used.

## Primary publication anchor
Lin, A., Yang, R., Dorkenwald, S. et al. Network statistics of the whole-brain connectome of Drosophila. Nature 634, 153–165 (2024). DOI 10.1038/s41586-024-07968-y.

Relevant published facts:
- directed weighted connectome;
- connection weight is total synapse count between neuron pairs;
- standard analysis threshold is 5 synapses per connection;
- total degree is in-degree plus out-degree;
- Phi(d) = M_d / [N_d (N_d - 1)];
- Phi_norm(d) = Phi(d) / mean(Phi_CFG(d));
- published CFG ensemble uses 100 samples;
- rich-club regime begins around total degree 37;
- very-high-degree regime above approximately 100 is no longer preferentially enriched relative to CFG or NPC;
- NPC comparison also uses 100 null samples.

## Current implementation
scripts/run_fafb_rich_club.py supports minimum-synapse filtering, explicit threshold lists/ranges, directed degree-preserving nulls, preservation reports, normalized rich-club density, and onset/offset/peak summaries.

Important: the repository field above_1pct is a descriptive convenience. It is not the complete statistical thresholding procedure discussed in the publication.

## Null-model hierarchy
### Gate A — CFG / degree-preserving null
Required invariants: edge count, directed in-degree sequence, directed out-degree sequence, no self-loops, and no duplicate directed pairs.
Implementation: src/graph/random_baseline.py.

### Gate B — neuropil-constrained / NPC-like null
The project has a neuropil-constrained null from the M2b work. It preserves degree-related structure plus source-neuropil to target-neuropil block counts.
Use the term NPC-like or neuropil-constrained unless exact equivalence to the publication's DC-SBM sampling procedure has been demonstrated.

### Gate C — spatial null
Not closed. A true distance-constrained null requires reliable neuron/arbour spatial information and an explicitly defined distance-conditioned randomization. Neuropil labels alone are not a distance model.

## Current replication plan
Phase 1: benchmark FAFB v783 with 5-synapse threshold, degree sweep 20–120, small null ensemble, runtime and invariant measurement.
Phase 2: if practical, run 100 CFG nulls and inspect the complete normalized curve.
Phase 3: repeat against the neuropil-constrained null.
Phase 4: establish the available spatial data and design a genuine spatial null.
Phase 5: only surviving structural effects may become candidates for computational primitives.

## Evidence labels
OBSERVED = directly measured in the biological dataset.
NULL-CONTROLLED = compared against a specified null.
REPLICATED = method and data sufficiently matched to the cited study.
EXTENSION = same question tested on a newer/different dataset or implementation.
HYPOTHESIS = proposed interpretation not yet established.
COMPUTATIONAL ABSTRACTION = engineering construct derived from validated structural evidence.
BENCHMARK RESULT = measured behavior of the implementation.

## Reproducibility requirements
Every large analysis artifact should record repository commit SHA, dataset/version, exact input product, filtering, graph representation, degree definition, null model, null count, random seeds, swap target, invariant checks, threshold sweep, software version, runtime, memory when practical, and output path.

## AI handoff protocol
1. Read this document first.
2. Read README.md.
3. Inspect the latest commits.
4. Read the active experiment document.
5. Inspect exact current code before proposing changes.
6. Verify workflow status and artifacts.
7. Search primary literature before modifying a publication-aligned method.
8. Separate published facts from project measurements.
9. Never claim an artifact was inspected unless it was actually retrieved.
10. Never call a newer-snapshot extension an exact replication.
11. Continue from the first unfinished gate rather than jumping to M6.

## Current blocking gate
CFG publication-aligned runtime/replication benchmark.

## Decision log — 2026-09-24
- explicit rich-club threshold controls added;
- publication-aligned documentation added;
- unit tests added for explicit thresholds and minimum-synapse filtering;
- normalized rich-club output fields added;
- publication benchmark workflow added;
- first benchmark workflow failure was a shell/time syntax error; no scientific computation ran;
- workflow was corrected and rerun;
- the corrected run must be inspected before scientific interpretation.

## Primary references
- Nature paper: https://www.nature.com/articles/s41586-024-07968-y
- Codex: https://codex.flywire.ai/
- FlyWire guidelines: https://home.flywire.ai/guidelines

## Non-negotiable rules
- no unsupported functional claims;
- no hidden dataset-version changes;
- no null model without stated invariants;
- no result without provenance;
- no replication label when method or dataset materially differs;
- no architecture claim merely because a biological pattern is visually striking;
- preserve failed runs and explain their cause.