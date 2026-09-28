# Project Map — Master Compass

Updated: 2026-09-27

## Purpose

This file is the short, durable map for human and AI handoff. It does not replace
the detailed experiment records. It answers one question first:

> Where are we, what has been proven, what is still open, and what must happen next?

For operational rules, read `docs/RESEARCH_PROTOCOL.md` first.
For milestone truth, read `docs/PROJECT-STATUS.md`.
For historical decisions, use Git history and the experiment documents.

---

## 1. Project thesis

The project asks whether measurable organizational principles in biological
connectomes can be separated from generic graph consequences and then converted
into computational abstractions that provide measurable engineering value.

Required chain:

**biological observation -> controlled null -> surviving structural constraint
-> computational abstraction -> benchmark -> ablation -> scaling**

Biology is evidence, not a specification.

The project is NOT trying to:
- claim that a fly brain is a scaled human brain;
- claim that connectivity alone proves function;
- copy the connectome literally into a computer and call it intelligence;
- claim novelty because the project uses FlyWire;
- announce a computational advantage before controlled benchmarks.

---

## 2. Current scientific state

### Gate A — CFG / degree-preserving rich-club

**CLOSED** for the defined FAFB v783 method-aligned path.

Evidence:
- FAFB v783;
- pair-level synapse aggregation before thresholding;
- 5-synapse minimum connection threshold;
- total degree = in-degree + out-degree;
- 100 deterministic CFG nulls;
- 3,732,460 requested and successful swaps per null;
- exact edge-count, in-degree and out-degree preservation;
- descriptive phi_norm > 1.01 continuously from degree 27 through 120;
- peak phi_norm = 1.057835 at degree 96.

Interpretation:
This is a stable CFG-controlled v783 result. It is a method-aligned
replication/extension, NOT an exact reproduction of Lin et al. 2024, whose
analysis used v630 and its own null-generation implementation.

### Gate B — NPC-like / neuropil-constrained rich-club

**CLOSED** for the defined 100-null FAFB v783 NPC-like benchmark.

- workflow run: `36295429519`;
- artifact: `10925776875`;
- 100/100 nulls completed;
- 3,732,460 pairs;
- exact edge count, in-degree, out-degree and source-block→target-block preservation;
- all requested swaps reached;
- descriptive `phi_norm > 1.01` spans degrees 41–69;
- peak `phi_norm = 1.015171` at degree 57.

This is a matched-null benchmark, not a formal significance test or a claim of a
distinct biological mechanism. It is an NPC-like v783 extension, not an exact
v630 reproduction.

### Gate C — spatial/distance-constrained null

**C0 CLOSED for data-definition/coverage; C1 OPEN.**

The authoritative C0 uses the full FAFB v783 Princeton synapse table
`fafb_v783_princeton_synapse_table.csv.gz` (~2.7 GB compressed).

Authoritative C0:
- workflow run: `36315995364`;
- artifact: `10930278435`;
- synapse-table rows: 80,215,790;
- graph: 138,584 nodes / 3,732,460 unique directed pairs;
- malformed rows: 0;
- outgoing and incoming arbor-centroid coverage: 100%;
- 100,000 observed-edge and 100,000 non-edge distance samples;
- observed-edge median: 481,001 nm;
- non-edge median: 2,281,970 nm;
- distance = anisotropic Euclidean source-outgoing-centroid → target-incoming-centroid using 4/4/40 nm voxel scaling.

A secondary lightweight C0 from `synapse_coordinates.csv.gz` is retained only as a
sensitivity/data-product comparison; it had 86.86% both-centroid node coverage and an
observed-edge median of 464,205 nm.

The first C1 feasibility run (`36317314664`, artifact `10930429115`) consumed that
secondary lightweight C0 artifact, not the authoritative Princeton C0. It is therefore
**SUPERSEDED for the primary C1 decision**. Its covered-subgraph invariants are retained
as historical execution evidence only.

The next C1 run must consume the Princeton C0 centroid artifact and establish full
covered-edge feasibility before any spatial rich-club ensemble.

## 3. Critical ingestion rule

FAFB connection tables can contain multiple region-split rows for the same
directed neuron pair.

Therefore:

1. aggregate synapse counts across all rows for a directed pair;
2. then apply the 5-synapse threshold;
3. then construct the unique directed graph.

This rule is centralized in:
`src/graph/connections.py::aggregate_pair_synapses`.

CFG, NPC and motif loaders now reuse this boundary. A regression test explicitly
checks that e.g. 3 + 3 synapses across two regions is retained at threshold 5.

This refactor was important because the same class of data-handling bug had
appeared independently in the NPC path.

---

## 4. What has actually been built

### Research infrastructure
- evidence-first research protocol;
- project status and handoff rules;
- prior-art log;
- novelty tracker;
- science evidence ledger;
- literature-to-design-rules mapping;
- provenance/checksum-oriented workflows;
- GitHub Actions execution and artifact capture.

### Biological analysis
- FAFB v783 ingestion;
- graph profile;
- reciprocity;
- spatial/neuropil inventory;
- CFG rich-club null;
- 100-null CFG ensemble;
- NPC-like rich-club null;
- NPC 8-null benchmark;
- NPC 100-null ensemble;
- conditional directed-triad sampler.

Important: the motif artifact is a conditional triad-signature sample, not a
general unrestricted triad census.

### Computational / M6 work
The repository contains RSS/effective-state, routing, bounded collective,
dynamic-layer and related prototype components. These remain research branches,
not validated architecture claims.

The RSS results generated before the semantic correction are explicitly marked
invalid for scientific interpretation.

The correct order is to finish the biological control spine before turning a
surviving pattern into a computational primitive.

---

## 5. Current map of the whole project

**M0 foundation**
  -> scientific guardrails / provenance / prior art

**M1 ingestion**
  -> FlyWire/FAFB data path

**M2 structural validation**
  -> degree / hubs / rich-club / reciprocity / motifs / spatial inventory

**Gate A**
  -> CFG rich-club
  -> CLOSED

**Gate B**
  -> NPC-like neuropil constraint
  -> CLOSED for the defined 100-null v783 benchmark

**Gate C**
  -> genuine spatial/distance null
  -> OPEN

**Surviving biological constraint**
  -> only if a structural effect survives the relevant null hierarchy

**Computational abstraction**
  -> define a minimal primitive that expresses that constraint

**Benchmark**
  -> compare against strong conventional, random and matched-resource baselines

**Ablation**
  -> identify which constraint actually causes any measured benefit

**Scaling**
  -> 10K -> 100K -> 1M -> ... only after the primitive has earned the right
     to scale

**Product/IP**
  -> only after measurable technical value and a clean IP/data path exist

---

## 6. What is NOT currently established

The project has NOT established:
- a new computational architecture;
- a benchmark advantage over conventional ML;
- energy efficiency advantage;
- a scaling law;
- biological universality;
- human-brain equivalence;
- patentable novelty;
- commercial product-market fit.

These are future questions.

---

## 7. Documentation rule from this point forward

Every substantive step must leave an audit trail containing, when applicable:

- date;
- purpose/question;
- hypothesis or decision being tested;
- exact dataset/version;
- exact input product;
- code commit SHA;
- workflow run ID;
- parameters;
- random seeds;
- null model and invariants;
- runtime/memory when available;
- artifact ID and checksum;
- result;
- interpretation;
- limitations;
- decision: continue / modify / close gate / reject branch.

Failed runs are part of the history and must remain documented with their cause.

Never overwrite a scientific conclusion silently when a new run changes it.
Record the new evidence and explicitly update the gate decision.

---

## 8. AI handoff rule

A new AI agent should read, in order:

1. `docs/RESEARCH_PROTOCOL.md`
2. `docs/PROJECT-MAP.md`
3. `docs/PROJECT-STATUS.md`
4. latest active experiment document
5. latest commits
6. current code
7. current workflow status
8. final artifacts before interpreting results

The agent must continue from the first unfinished gate.

It must not invent a result from an in-progress workflow, and it must not
restart an already-closed gate unless a reproducibility discrepancy is found.

---

## 9. Commercialization track

Commercial value is a possible downstream outcome, not a current scientific
conclusion.

The project becomes commercially interesting if it can demonstrate something
specific that customers value, for example:
- a measurable compute/resource advantage on a useful workload;
- a scalable connectome-derived architecture or compiler/runtime;
- a reusable generator/benchmarking platform;
- a defensible algorithmic method;
- a licensed software/IP component;
- a research or engineering platform that materially reduces architecture
  exploration cost.

The commercial path should therefore remain downstream of scientific validation.

### Critical IP/data constraint

FAFB v783 public data are released by FlyWire under CC BY-NC 4.0. This means
we must not assume that a commercial product can simply package or redistribute
the underlying FlyWire-derived data. Commercialization must separate:
- our original software/algorithms;
- derived results that can legally be distributed;
- third-party biological data and their licenses;
- any future proprietary training/data products.

Before commercial launch, licensing and IP ownership need explicit legal review.

---

## 10. Current decision

**The project is on the correct path.**

The next scientific decision is not “invent the architecture”.

It is:

**Does the residual structure survive a genuine spatial/distance-constrained
control while retaining the appropriate topological constraints?**

Gate C must first establish the available neuron-level spatial data, define the
distance semantics, and pre-register the null hierarchy before large execution.
Only a residual effect that survives the relevant spatial controls can become a
candidate computational constraint.

This ordering is the project's compass.


## 2026-09-28 — Gate C1 feasibility checkpoint

**Gate C1 feasibility: CLOSED for the authoritative Princeton path. Gate C remains ACTIVE pending the spatial null ensemble.**

Authoritative chain:
`C0 Run 36318477728 → artifact 10931780910 → C1 Run 36320329317 → artifact 10932471526`.

C1 measured 100% graph/node coverage, 4,156 accepted swaps in 100,000 attempts, exact edge/in/out-degree preservation, and exact coarse arbor-distance-bin preservation. Rich-edge coverage at thresholds 37/75/93/120 was 100%.

The next controlled experiment is the four-null spatial rich-club ensemble. Do not interpret the C1 feasibility benchmark itself as a rich-club result.


## 2026-09-28 — Gate C first spatial ensemble checkpoint

The authoritative spatial path has now progressed beyond C1 feasibility.

**Gate C state:** C0 CLOSED → C1 feasibility CLOSED → first 4-null spatial rich-club ensemble VALIDATED → Gate C overall remains OPEN for ensemble stability and stronger spatial-model comparison.

Cross-null audit:
- CFG 100-null: peak phi_norm 1.057835 at degree 96; descriptive >1.01 span 27–120.
- NPC-like 100-null: peak 1.015171 at degree 57; descriptive >1.01 span 41–69.
- Spatial 4-null: peak 1.012159 at degree 62; descriptive >1.01 span 51–71.
- The observed curve is identical across the three aggregates, so the attenuation comes from the null constraints.

The spatial result is a project-defined hard-binned arbor-distance sensitivity null, not an exact Lin NND reproduction and not a Salova & Kovács maximum-entropy model.

**Compass now:** Gate A CLOSED → Gate B CLOSED → authoritative C0 CLOSED → C1 feasibility CLOSED → spatial 4-null validated → 8-null stability → C2 feasibility pilot → possible NPC+spatial ensemble → functional validation → computational abstraction.

See docs/GATE-C-COMPARISON-2026-09-28.md for the complete audit, runtime estimates, terminology and literature checkpoint.


## 2026-09-28 — Spatial stability closed as a sub-gate

Spatial 8-null stability is now validated:
- >1.01 interval remains 51–71.
- peak remains degree 62.
- peak phi_norm = 1.0120821 versus 1.0121585 in the 4-null ensemble.
- all 8 nulls preserve edge count, in-degree, out-degree and distance-bin histogram.

This closes the **spatial ensemble stability sub-gate**, but not Gate C overall.

C2 feasibility is active: NPC-like block-pair preservation + coarse arbor-distance-bin preservation. The pilot is 100,000 attempts and is feasibility-only.

**Updated compass:** Gate A CLOSED → Gate B CLOSED → C0 CLOSED → C1 feasibility CLOSED → spatial stability CLOSED → C2 feasibility RUNNING → possible C2 ensemble → stronger spatial model / maximum-entropy sensitivity → functional validation → computational abstraction.
