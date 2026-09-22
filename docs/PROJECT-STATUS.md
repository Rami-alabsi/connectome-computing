# Project Status

## Current position

**Stage: M6 — resource-constrained multiscale simulator + real-data validation**

Experimental spine:

**biological evidence → structural abstraction → bounded resources → effective state → relational coordination → dynamics → benchmark → ablation → scaling**

Biological structure is evidence used to generate falsifiable computational
abstractions, not a specification to copy literally.

### Completed

- [x] M0 Research foundation
- [x] M1 FlyWire/Codex ingestion layer
- [x] M2 structural graph analysis
- [x] M2b motif/null-model foundation
- [x] M3 biological annotation layer
- [x] M4 architecture primitives
- [x] M5 modular/sparse/hierarchical/spatial generators and validation
- [x] M5 capacity-triggered hierarchy prototype
- [x] M6 effective-state interface and communication accounting
- [x] M6 bounded higher-order coordination primitive
- [x] M6 stateful local-plus-interface simulator
- [x] M6 state-dependent routing primitive
- [x] M6 dynamic relational layering primitive
- [x] M6 field-mediated relational layer prototype
- [x] M6 controlled RSS benchmark implementation
- [x] M6 RSS information-flow semantics corrected + unit tests strengthened
- [x] M6 RSS matched-control matrix + multi-seed/multi-budget runner

## Active workstreams

### 1. Real biological anchor

Run FAFB v783 through a streaming profile pipeline and measure directed degree,
reciprocity, hubs/rich-club, motifs, hierarchy/modularity, spatial/contact
constraints, long-range structure and multi-constraint interactions.

Current public Codex identifies FAFB v783 as 139,255 neurons and 3,732,460
directed connection pairs; BANC v888 is a newer 2026 brain-and-nerve-cord
snapshot. citeturn0search0turn0search1

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
- G: stable core + flexible periphery.

The benchmark enforces:

**hidden source states → selected routes → visible source subset → prediction**

The runner now sweeps seeds 0–4 and active-relation budgets 2/4/6/8 with matched
module count, state dimension, bytes per relation, contexts and sequence length.

D is explicitly documented as a bounded collective-pooling surrogate, not a
general nonlinear higher-order interaction model.

### 4. Required next controls

Still required before scientific interpretation:

- parameter/interface-dimension matching;
- shuffled collective-relation null;
- sparse brokerage ablation;
- explicit stable-core removal;
- candidate-topology matching where appropriate.

### 5. Potential-path branch

Future classical hypothesis:

**candidate paths → state/context evolution → selective activation/suppression → delayed commitment**

Dynamic routing, candidate-path and multipath mechanisms already have substantial
prior art. Therefore no novelty is assumed. The branch remains blocked until RSS
controls and artifacts are validated.

### 6. M6-COSMIC and multiscale branches

Re-run M6-COSMIC after the bounded-state correction before interpreting scaling.
Do not interpret hierarchy depth until parent grouping is genuinely multilevel.

## Scientific status

**No benchmark advantage or novelty claim yet.**

CI success is implementation evidence only. Scientific claims require executed
artifacts, matched-resource controls, ablations, multiple seeds and reproducible
analysis.

## Immediate sequence

1. Inspect the new RSS CI run and CSV artifact.
2. Fix any remaining semantic/test issues.
3. Add the remaining null/ablation controls.
4. Analyze the 5-seed × 4-budget matrix without a single aggregate score.
5. Re-run M6-COSMIC.
6. Complete FAFB v783 profiling.
7. Reassess the potential-path branch using narrow prior-art search.
8. Scale only after mechanisms survive controls.

## Cross-domain rule

Quantum information, holography, cosmic web and social-network analogies are
hypothesis generators only. They never substitute for connectome evidence or
matched non-biological controls.

## Compass

**evidence → abstraction → falsifiable prediction → matched control → implementation → execution → ablation → scaling → prior-art recheck**
