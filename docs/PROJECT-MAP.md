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

**OPEN.**

The complete 100-null ensemble was executed and inspected. An 8-null benchmark preceded it and showed a much smaller residual than CFG:
- 3,732,460 pairs;
- exact degree preservation;
- exact source-neuropil -> target-neuropil block-count preservation;
- all requested swaps reached;
- phi_norm > 1.01 only over an intermediate range in the 8-null benchmark;
- peak approximately 1.0152 at degree 58;
- high-degree values fell below 1.

This is directional benchmark evidence only. It does NOT close Gate B.

The final 100-null ensemble:
- workflow run: 36295429519;
- source commit: bbd0fa1ea2b5c4ef06788808e20597bebb0483bf;
- 100/100 null jobs succeeded;
- aggregate artifact: fafb-v783-rich-club-npc-100null, artifact 10925776875;
- exact degree and source-block -> target-block preservation passed;
- all requested swaps were reached.

Descriptive >1.01 enrichment spans degrees 41–69 and peaks at degree 57 with
phi_norm = 1.015171, versus CFG peak 1.057835 at degree 96. This is a matched-null
comparison, not a formal significance test and not evidence by itself for a distinct
biological mechanism.

### Gate C — spatial/distance-constrained null

**NOT STARTED / OPEN.**

Gate C must use an actual spatial/distance model. Neuropil labels alone are not
a distance null. The current literature review points to EDR and combined
topology+spatial constraints as important candidate controls.

Do not jump to Gate C before Gate B is resolved unless an implementation
dependency requires preparatory work.

---

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
