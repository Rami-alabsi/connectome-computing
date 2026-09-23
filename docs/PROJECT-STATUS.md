# Project Status

## Current position

**Stage: M6 — resource-constrained multiscale simulator + real-data validation**

**Prototype-phase note:** the current implementation phase was built in a single intensive session. Treat the repository as a research prototype scaffold until real-data execution, matched controls, ablations and reproducible artifacts have been completed.

Experimental spine:

**biological evidence → structural abstraction → bounded resources → effective state → relational coordination → dynamics → benchmark → ablation → scaling**

Biological structure is evidence used to generate falsifiable computational abstractions, not a specification to copy literally.

## Evidence state

- Software scaffolding and unit tests exist for M1–M6 components.
- Real FAFB v783 data have **not yet been executed through the ingestion/profile pipeline in this checkpoint**.
- Therefore M1/M2 biological completion marks are implementation readiness, not validated connectome results.
- No RSS performance result is currently accepted as scientific evidence.

## Implemented prototype components

- [x] M0 research foundation and scientific guardrails
- [x] M1 FlyWire/Codex ingestion code
- [x] M2 graph-analysis code
- [x] M2b motif/null-model code
- [x] M3 biological annotation code
- [x] M4 architecture primitives
- [x] M5 modular/sparse/hierarchical/spatial generators and validation code
- [x] M5 capacity-triggered hierarchy prototype
- [x] M6 effective-state interface and communication accounting
- [x] M6 bounded higher-order coordination primitive
- [x] M6 stateful local-plus-interface simulator
- [x] M6 state-dependent routing primitive
- [x] M6 dynamic relational layering primitive
- [x] M6 field-mediated relational layer prototype
- [x] M6 controlled RSS benchmark implementation
- [x] M6 RSS information-flow semantics correction
- [x] M6 RSS matched-control runner
- [x] M6 shuffled-context null implementation
- [x] M6 shuffled-collective null implementation

## Active workstreams

### 1. Real biological anchor

Run FAFB v783 through a streaming profile pipeline and measure directed degree,
reciprocity, hubs/rich-club, motifs, hierarchy/modularity, spatial/contact
constraints, long-range structure and multi-constraint interactions.

Current public Codex identifies FAFB v783 as 139,255 neurons and 3,732,460
directed connection pairs; BANC v888 is a newer 2026 brain-and-nerve-cord
snapshot. These published counts are reference checks, not yet a result from our
local ingestion pipeline.

This remains the main biological gate.

### 2. Dynamic Relational State Space (RSS)

**local state → effective module state → overlapping relational layers → selective direct routes → bounded collective relations**

A relation may carry endpoint pair, layer/type, context, order, strength/priority,
activation and cost. This is not a literal fourth spatial dimension.

### 3. M6-RSS benchmark

Current conditions:

- A: flat pairwise;
- B: fixed hierarchy;
- C: dynamic overlapping context layers;
- D: dynamic layers + bounded collective pooling;
- E: fixed overlap;
- F: random context-matched routing;
- G: stable core + flexible periphery;
- H: shuffled-context null;
- I: shuffled-collective null.

### 4. RSS semantic correction — critical

The earlier C/D implementation gave the correct context group as the candidate
pool. At budgets that covered that group, low error could arise from candidate
coverage rather than context-aware routing.

C/D now rank the **full candidate pool** under the same active-route budget,
with the current context group receiving priority. H uses a deterministic
same-cardinality shuffled priority group. This isolates contextual priority
from simple group coverage.

**All previous 6,720-row RSS results generated before this correction are
invalid for scientific interpretation and must not be reused as evidence.**

The runner is configured for seeds 0–4 and budgets 2/4/6/8 with matched module
count, state dimension, bytes per relation, contexts and sequence length.

D remains a bounded collective-pooling surrogate, not a general nonlinear
higher-order interaction model.

## Required controls before interpretation

- shuffled-context null — **implemented**;
- parameter/interface-dimension matching;
- shuffled collective-relation null — **implemented**;
- sparse brokerage ablation;
- explicit stable-core removal;
- candidate-topology matching where appropriate.

## Potential-path branch

Future classical hypothesis:

**candidate paths → state/context evolution → selective activation/suppression → delayed commitment**

Dynamic routing, candidate-path and multipath mechanisms already have substantial
prior art. Therefore no novelty is assumed. The branch remains blocked until RSS
controls and artifacts are validated.

## M6-COSMIC and multiscale branches

Re-run M6-COSMIC after the bounded-state correction before interpreting scaling.
Do not interpret hierarchy depth until parent grouping is genuinely multilevel.

## Scientific status

**No benchmark advantage or novelty claim yet.**

CI success is implementation evidence only. Scientific claims require executed
artifacts, matched-resource controls, ablations, multiple seeds and reproducible
analysis.

## Immediate sequence

1. Execute the corrected RSS matrix and inspect the CSV artifact.
2. Determine whether C/D retain any advantage against H/F and whether D retains any advantage against I at matched budgets.
3. Verify fixed-control regressions, then add parameter/interface matching and the remaining ablations.
4. Execute the real FAFB v783 ingestion/profile pipeline and compare its counts with the published reference counts.
5. Re-run M6-COSMIC after the bounded-state correction.
6. Only then reassess the potential-path branch.
7. Scale only after mechanisms survive controls.

## Cross-domain rule

Quantum information, holography, cosmic web and social-network analogies are hypothesis generators only. They never substitute for connectome evidence or matched non-biological controls.

## Compass

**evidence → abstraction → falsifiable prediction → matched control → implementation → execution → ablation → scaling → prior-art recheck**
