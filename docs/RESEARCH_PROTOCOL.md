# Connectome Computing — Research Protocol and AI Handoff

## Purpose
This is the primary operational handoff document for future human or AI contributors. Read it before changing the research pipeline. It records the scientific question, provenance, current stage, evidence rules, replication gates, and non-negotiable interpretation constraints.

## Scientific question
Can measurable organizational principles in a biological connectome be separated from generic consequences of degree, sparsity, and mesoscale anatomy, and then translated into computational abstractions that can be benchmarked?

Required chain:
biological observation → controlled null model → surviving structural constraint → computational abstraction → benchmark

Connectivity alone is not treated as proof of function.

## Current stage — 2026-10-07
C2 three-seed replication is complete and the non-invasive stability audit has passed as a reproducibility/control check. Formal mixing/convergence remains OPEN. Gate C remains OPEN. C3 is currently a prior-art/design and synthetic-validation gate only; no full FAFB C3 run is authorized yet.

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
12. For every substantive stage, perform a targeted literature refresh and record only findings that change, constrain, validate, or explicitly rule out a project decision.
8. Separate published facts from project measurements.
9. Never claim an artifact was inspected unless it was actually retrieved.
10. Never call a newer-snapshot extension an exact replication.
11. Continue from the first unfinished gate rather than jumping to M6.

## Current blocking gate
The immediate scientific boundary is **formal C2 mixing/convergence assessment + validated C3 sensitivity design**. Runs #45–#47 are complete and artifact-backed; their full rich-club curves are highly reproducible, but the artifacts do not establish formal Markov-chain mixing or convergence.

C2 three-seed audit:
- #45: seed 20260935; max phi_norm 1.0076221 at degree 51; overlap 47.9138%.
- #46: seed 20261001; max phi_norm 1.0076660 at degree 50; overlap 47.9129%.
- #47: seed 20261002; max phi_norm 1.0077486 at degree 51; overlap 47.9273%.
- Full-curve Pearson correlations: 0.9999321–0.9999503.
- Maximum pointwise spread: 0.0006645.
- No realization has phi_norm > 1.01.
- Formal ESS/autocorrelation/convergence diagnostics: not established.

C3 guardrail:
- C2 definition and kernel remain unchanged.
- Salova & Kovács (2025) makes generic canonical spatial maximum-entropy connectome modeling prior art, not novelty.
- C3-A is a separate canonical sensitivity ensemble.
- Synthetic exact-vs-canonical validation and support/scalability audit must precede FAFB.
- Any support restriction is a model change and must be scientifically justified.
- No structure→function, RSS, architecture, benchmark, scaling, or commercialization claim before Gate C closure.

### Gate B closure record — 2026-09-27
The completed 100-null NPC-like ensemble (workflow 36295429519, artifact 10925776875) used FAFB v783, 3,732,460 unique directed pairs, a 5-synapse pair-level threshold, 100 deterministic nulls, exact in/out-degree preservation, exact source-neuropil→target-neuropil block-count preservation, and full swap realization. The descriptive phi_norm > 1.01 span was degrees 41–69 with peak 1.015171 at degree 57. This closes only the defined v783 NPC-like benchmark.

### Gate C pre-registration principle
Gate C is not one null. It is a hierarchy:
1. Spatial-only sensitivity: estimate how much of the observed wiring/rich-club profile is explained by distance alone.
2. Degree + spatial control: preserve the directed in/out degree sequences while imposing the empirical spatial wiring constraint.
3. NPC + spatial control, if computationally feasible: retain the Gate B source-block→target-block constraints while adding spatial conditioning.
4. EDR/projectome sensitivity: use the published EDR formulation only as a sensitivity/control at its appropriate projectome/neuropil level, not as a direct neuron-level replacement for the NPC model.

The primary Gate C comparison must be selected before execution and must specify the distance definition, spatial coordinate source, edge threshold, constraints, randomization algorithm, invariants, number of nulls, seed policy, and failure criteria.

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

## 2026-09-28 research-continuity rule
The project now has two parallel but explicitly separated tracks:
1. Confirmatory spine: close the predeclared biological null hierarchy before making structural claims.
2. Discovery watch: preserve and escalate unexpected observations only through artifact verification, independent rerun, stronger nulls, alternative explanations, locked follow-up, and held-out or external validation.

The existence of an anomaly never authorizes a post-hoc threshold, mechanism claim, or novelty claim.
