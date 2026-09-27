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

The first Gate C implementation should use the documented neuron coordinate
product as a node-position distance. It must not be described as axon length,
arbor distance, or synapse-to-synapse physical distance.

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
- Salova & Kovács, Network Neuroscience 9(1), 181–206 (2025),
  DOI 10.1162/netn_a_00428.
- Péntek & Ercsey-Ravasz, Network Neuroscience 9(3), 869–895 (2025),
  DOI 10.1162/netn_a_00455.

Data-access note: Codex exposes marked neuron coordinates as a downloadable
FAFB v783 product. The underlying FlyWire data remain subject to their own
licensing terms.
