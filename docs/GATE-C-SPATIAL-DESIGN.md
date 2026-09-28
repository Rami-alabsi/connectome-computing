# Gate C — Spatial / Distance-Control Design

Updated: 2026-09-27

## Purpose

Gate C asks whether the residual rich-club structure left after the defined
degree-preserving CFG control and the NPC-like neuropil-constrained control
survives a genuine spatial/distance constraint.

This is a design/preflight record. It does not report a Gate C result.

## Current evidence

FAFB v783 has a public coordinates.csv.gz product containing neuron coordinates
(root_id, position, supervoxel_id). Codex currently describes FAFB v783 as
139,255 neurons and 3,732,460 connections. The repository's existing connection
table remains the authoritative graph input for rich-club analysis.

The repository spatial profile is descriptive only: its neuropil field identifies
synapse location and is not a complete neuron-level spatial model.

## Literature constraints

### Salova & Kovács 2025

Their fly/mouse/human analysis shows that spatial constraints matter, but spatial
constraints alone do not reproduce broad topology such as the degree sequence;
degree alone does not reproduce spatial structure. Their maximum-entropy models
combine topological and spatial constraints and can predict additional graph
properties beyond the fitted constraints.

Project use: Gate C should not use a distance-only null as the sole primary test
of a degree-sensitive rich-club effect. A degree+distance control is required
for a clean continuation of the CFG/NPC hierarchy.

### Péntek & Ercsey-Ravasz 2025

Their EDR model is a useful null for Drosophila projectome/neuropil networks and
is explicitly intended to separate geometry-driven structure from additional
organization.

Project limitation: this is a projectome/neuropil-level model. It should be
used
as a sensitivity analysis or cross-level control, not silently treated as the
neuron-level equivalent of the NPC rich-club null.

## Spatial coordinate semantics

Before any null is executed, record:
- coordinate file SHA-256;
- number of coordinate rows;
- number of unique root IDs;
- fraction of graph nodes with coordinates;
- units and voxel scaling;
- whether the coordinate is soma/marked-neuron position or another point;
- duplicate-root handling rule.

The first Gate C preflight used the documented coordinate product as a node-position
proxy, but its raw table contains multiple positions per root_id. The corrected
preflight therefore collapses all positions per root_id by component-wise median
for diagnostics only. This is reproducible, but it is not yet the preferred
biological distance definition for the primary C0/C1 analysis.

The preferred next C0 distance definition is an arbor-aware source/target
definition if the v783 synapse-coordinate product can support it: outgoing
synapse centroid for the presynaptic neuron and incoming synapse centroid for
the postsynaptic neuron. This follows the relevant whole-brain Drosophila
prior-art approach more closely than a generic neuron-position proxy. It must
still be labeled as a synapse-derived arbor proxy, not axon length.

The existing node-position proxy must not be described as axon length, arbor
distance, or synapse-to-synapse physical distance.

For coordinates [x,y,z] in FAFB voxel units, preserve the anisotropic voxel
scale (4, 4, 40 nm) when calculating Euclidean distances. Do not calculate
ordinary Euclidean distance on raw voxel indices without correcting the z-axis
scale.

## Candidate null hierarchy

### C0 — Spatial inventory / empirical distance law

No randomization.

Measure:
- observed edge-length distribution;
- controlled sampled non-edge distance distribution;
- connection probability by distance bin;
- rich-club edge-length profile.

Purpose: establish whether a distance-dependent null is supported by the
available node coordinates.

### C1 — Degree-preserving spatial rewiring

Primary candidate.

Constraints:
- same unique directed edge count;
- exact in-degree sequence;
- exact out-degree sequence;
- no self-loops;
- no duplicate directed pairs.

Spatial condition:
- accepted rewiring should preserve or match a pre-registered distance
  distribution/conditional distance law rather than simply minimizing total
  length.

The implementation must not silently alter degree sequences while fitting
distance.

### C2 — NPC + spatial sensitivity

If C1 is validated and computationally tractable:
- preserve in/out degree;
- preserve source-neuropil→target-neuropil block counts;
- add a spatial constraint/target.

This is the closest continuation of the Gate B hierarchy, but it may have a
substantially lower swap acceptance rate. Failure to reach the target must be
reported, not hidden.

### C3 — EDR sensitivity

Fit/construct the EDR-style control at the appropriate level and compare its
ability to reproduce the observed rich-club profile.

This is not a substitute for C1/C2 because of the projectome-versus-neuron
resolution difference.

## Distance definition decision

The first implementation should distinguish:
1. soma/marked-neuron Euclidean distance — available from the coordinates
   product and suitable for a reproducible first spatial null;
2. axon/arbor distance — biologically richer but requires skeleton/morphology
   data and a much heavier computation;
3. synapse physical distance — requires synapse-coordinate data and is a
   different question from neuron-level rich-club wiring.

Only (1) is in scope for the first Gate C preflight.

## Required preflight artifact

Before any large null ensemble, produce a JSON artifact containing:
- dataset/version;
- coordinate source and checksum;
- coordinate schema;
- unit conversion;
- node coverage;
- duplicate policy;
- missing-coordinate policy;
- sampled observed edge-distance statistics;
- sampled non-edge distance statistics;
- distance bins;
- empirical distance-law diagnostics;
- proposed null constraints;
- proposed swap acceptance diagnostics;
- explicit statement that no Gate C scientific conclusion is being made.

## Statistical discipline

phi_norm > 1.01 remains descriptive only.

Gate C should preserve the existing 20–120 degree sweep so CFG, NPC-like and
spatial curves remain directly comparable. Formal inference, if later added,
must use the pre-registered null ensemble and account for the threshold sweep
rather than treating 101 thresholds as independent tests.

## Decision rule

- If the spatial preflight shows insufficient coordinate coverage or ambiguous
  semantics, stop and resolve the data issue before null generation.
- If C1 cannot preserve both degree sequences and the declared spatial law,
  stop; do not weaken invariants to make the algorithm run.
- If C1 is valid, execute the pre-registered ensemble.
- Only after C1 is validated should C2 be considered.
- No computational architecture claim is permitted from Gate C alone.

## Provenance

Primary dataset: FlyWire FAFB v783.

Primary literature:
- Lin et al., Nature 634, 153–165 (2024), DOI 10.1038/s41586-024-07968-y.
- Salova & Kovács, Network Neuroscience 9(1), 181–206 (2025),
  DOI 10.1162/netn_a_00428.
- Péntek & Ercsey-Ravasz, Network Neuroscience 9(3), 869–895 (2025),
  DOI 10.1162/netn_a_00455.

Data-access note: Codex exposes marked neuron coordinates as a downloadable
FAFB v783 product. The underlying FlyWire data remain subject to their own
licensing terms.


## Gate C0 product audit — authoritative source

The project tested two FAFB v783 spatial products. The primary source is the full
Princeton synapse table `fafb_v783_princeton_synapse_table.csv.gz` (~2.7 GB compressed):
80,215,790 rows, separate pre/post coordinates, and 100% graph-node arbor-centroid
coverage. The lighter `synapse_coordinates.csv.gz` product remains a secondary
sensitivity comparison and produced 86.86% both-centroid coverage.

Authoritative C0:
- workflow run `36315995364`;
- artifact `10930278435`;
- synapse-table SHA-256 `780a0ebd9320847b9fce2b05056b3d57a56da097549dae7847b8e55c488f1e29`;
- connection-table SHA-256 `445f996bf6c4b1803b9ba186189138a3061ff8623aa94c0abcf38af30a5bd48b`.

The later C1 feasibility run consumed the lighter C0 centroid artifact and is explicitly
superseded for the primary path. The C1 workflow has been redirected to consume the
Princeton C0 artifact.

## Gate C0 final result — 2026-09-27

The arbor-aware C0 preflight was executed against the FAFB v783 Princeton synapse table, not the lighter `synapse_coordinates.csv.gz` product. The full Princeton table contains 80,215,790 rows and exposes separate pre-site and post-site coordinates plus the root-ID suffix fields `pre_root_id_720575940` and `post_root_id_720575940`. Root IDs were normalized to canonical 64-bit strings by restoring the `720575940` prefix.

The resulting source/target proxies are:
- outgoing centroid = mean of all outgoing synapse pre-site coordinates for the neuron;
- incoming centroid = mean of all incoming synapse post-site coordinates for the neuron;
- distance = anisotropic Euclidean distance using FAFB voxel scaling 4,4,40 nm.

Execution checks:
- graph nodes: 138,584;
- unique directed pairs after the existing pair aggregation + 5-synapse threshold: 3,732,460;
- outgoing centroid coverage: 100%;
- incoming centroid coverage: 100%;
- both-centroid coverage: 100%;
- malformed synapse rows: 0;
- edge distance sample: 100,000 unique graph edges;
- nonedge distance sample: 100,000 unique nonedges;
- observed edge distance median: 481,001 nm (~481 µm);
- sampled nonedge distance median: 2,282,542 nm (~2.28 mm).

This closes the **data-definition/coverage portion of C0**. It does not establish a spatial null result and does not by itself alter the CFG/NPC rich-club conclusions.

### C1 pre-registration direction

The primary C1 candidate will preserve the full directed in-degree and out-degree sequence while imposing a spatial constraint at the level of the validated arbor-aware distance. A benchmark must first establish whether a hard distance-binned edge-swap ensemble is computationally reachable without materially distorting the degree sequence or failing to produce enough accepted swaps. The proposed hard constraint preserves the multiset of coarse distance bins across each accepted two-edge swap; this is deliberately stronger than an unconstrained CFG and is intended as a sensitivity/control, not as a claim about the biological generative mechanism.

The distance bins will be fixed before the C1 benchmark and reported with the exact swap acceptance/failure diagnostics. No rich-club interpretation will be published from C1 unless the ensemble passes its pre-registered invariants and reaches the requested null count.

Lin et al. (2024) provide the direct biological precedent for defining pairwise distance from outgoing and incoming synapse-derived arbor proxies; their NND analysis also shows that spatial information changes network null expectations. Salova & Kovács (2025) provide independent support for treating topology and spatial constraints jointly rather than treating either degree or distance alone as sufficient.


## 2026-09-28 — Authoritative C1 feasibility result

The Princeton arbor-distance path passed the feasibility gate.

**Provenance**
- C0: Run `36318477728`, artifact `10931780910`, SHA-256 `7265e20db3721f6b438a93227180eb0d0b8d3ad3fd9894bcbbe4a14a81dd5f36`.
- C1: Run `36320329317`, artifact `10932471526`, SHA-256 `efa3b9837ece2920e37fde31383ea0e40f4787d5d1da6da61fc897850882ea45`.
- Commit: `ad1005f4974048957b05e8eb21697fd495816fac`.
- Graph: 3,732,460 directed pairs at min_synapses=5.
- Coverage: 100% nodes and 100% edges.
- Attempts: 100,000; accepted: 4,156; acceptance rate 4.156%.
- Exact preservation: edge count, in-degree, out-degree, coarse arbor-distance-bin histogram.
- Rich-edge drop: zero at degree thresholds 37, 75, 93 and 120.

**Decision:** the hard-binned arbor-distance swap is computationally feasible on the complete authoritative graph. It is still a project-defined spatial sensitivity null, not an exact implementation of Lin et al.'s NND model and not the Salova & Kovács maximum-entropy model.

**Next:** run four independent spatial rich-club nulls (seeds 20260927–20260930), each targeting one successful swap per edge, then aggregate only if all four pass invariants and full target completion.


## 2026-09-28 — First spatial ensemble result and next control

The authoritative Princeton C0 and C1 feasibility path has produced the first validated spatial rich-club ensemble.

Run 36381489805 used four independent seeds (20260927–20260930), one successful swap per directed edge, 20–120 degree sweep, and exact preservation of edge count, in-degree, out-degree and the coarse arbor-distance-bin histogram. All four nulls reached the full 3,732,460-swap target.

Result: descriptive phi_norm > 1.01 from degree 51 through 71; peak at degree 62 with phi_norm 1.0121585.

This is a project-defined hard-binned spatial sensitivity control. It is not exact Lin NND, not a maximum-entropy spatial model, and not evidence that spatial distance is the biological mechanism.

The next planned step is an 8-null stability expansion. Expected wall-clock time is approximately 40–45 minutes with four-way parallelism, based on the completed 4-null run (~21 minutes). If stability is adequate, proceed to a 100,000-attempt C2 NPC+spatial feasibility pilot before any full combined ensemble.

The C2 pilot must preserve:
- exact in-degree;
- exact out-degree;
- source-neuropil → target-neuropil block counts;
- declared arbor-distance constraint;
- no self-loops or duplicate directed pairs.

The pilot reports acceptance and invariant status only; it must not be interpreted as a rich-club result.
