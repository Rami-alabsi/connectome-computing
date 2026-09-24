# Connectome Computing

**From Biological Neural Networks to Scalable Computational Architectures**

Connectome Computing is an open research project investigating whether structural and dynamical principles found in biological neural connectomes can be transformed into scalable computational architectures.

## Vision

Instead of asking how to simulate a biological brain exactly, we ask: **Which organizational principles of biological neural networks can be abstracted into computational primitives and architectures that remain useful as they scale?**

Pipeline: Biological connectome → network principles → computational primitives → scalable architecture → benchmarked computing system.

## Starting Point

The project starts with the Drosophila melanogaster whole-brain connectome as a tractable, high-resolution biological reference. Human-brain neuroscience and connectomics are used as a higher-scale scientific reference and constraint source, not as a target obtained by simply scaling a fly brain.

Published FlyWire work reports a whole-brain reconstruction of 139,255 neurons and 54.5 million synapses, with extensive annotations and programmatic access. Network analysis has identified recurrent motifs, sparsity, strong interconnectivity and rich-club organization.

## Research Questions

1. Which structural properties of biological connectomes are stable, measurable and computationally relevant?
2. Which motifs, modules, hubs and feedback patterns can become reusable computational primitives?
3. Can a synthetic network generator reproduce important connectome statistics while scaling beyond the biological network?
4. Do connectome-derived architectures provide measurable benefits in sparsity, parallelism, robustness, latency, memory traffic or energy efficiency?
5. Which properties are fly-specific and which may represent broader principles of biological neural computation?
6. How should human-brain evidence constrain or guide scaling?
7. Which workloads reveal strengths or weaknesses of the architecture?

## Project Phases

1. Fly connectome ingestion and validation.
2. Graph, motif, module and hub analysis.
3. Dynamic modeling.
4. Computational abstraction.
5. First connectome-derived software architecture.
6. Benchmarking against conventional and random baselines.
7. Scalable network generation.
8. Human-brain-informed constraints.
9. Optional neuromorphic/hardware mapping.

## Core Abstractions

- Neuron/node → stateful processing node.
- Synapse → weighted communication edge.
- Microcircuit → processing unit.
- Module → functional or structural subsystem.
- Hub/rich-club node → integration or routing resource.
- Feedback loop → recurrent state mechanism.
- Sparse communication → event-driven data movement.

These are engineering abstractions, not claims that a biological neuron is literally equivalent to a CPU transistor.

## Scaling Strategy

Rather than copying a 139K-neuron graph into a larger graph, we investigate: observed biological rules → generative model → larger synthetic architecture.

Candidate preservation targets include degree distributions, motif frequencies, modularity, sparsity, hub structure, recurrent connectivity, path lengths and validated activity statistics.

Experimental scales may include 10K → 100K → 1M → 10M → 100M → 1B processing units. These are research targets, not claims of automatic biological intelligence.

## Prior Art

The broad idea of using a fly connectome for computation is not claimed as novel. Existing work includes FlyWire whole-brain analysis, Biological Processing Units derived from insect connectomes, and full FlyWire connectome execution on Loihi 2.

The working research hypothesis here is narrower: a systematic pipeline of biological design-rule extraction → computational primitives → scalable generation → controlled ablation → cross-scale benchmarking may provide a reusable methodology for connectome-derived computing architectures.

Novelty will be assessed continuously through the prior-art log.

## Baselines

Where appropriate, compare against MLP, CNN, GNN, recurrent networks, SNNs, Transformer-style models, random graphs, degree-preserving controls and motif-preserving controls.

## Scientific Principles

1. No overclaiming: connectivity does not by itself prove function.
2. Biology is evidence, not a specification.
3. Fly and human brains are not simple scaled copies.
4. Architectural claims require measurable experiments.
5. Random and conventional baselines are required.
6. Structural preservation and functional performance must be evaluated separately.
7. Data provenance and licensing must be respected.

## Repository Structure

connectome-computing/
  README.md
  ROADMAP.md
  LICENSE
  CITATION.cff
  CONTRIBUTING.md
  docs/
  data/
  src/
  experiments/
  notebooks/
  tests/
  configs/
  results/

## Status

**Stage: M5 → M6 — synthetic connectome validation + real-data biological gate closure**

Current blocking gate: **FAFB v783 biological Gate A (CFG/rich-club) is open.** The combined real-data anchor Run `35984738032` has now completed successfully and all five artifacts have been inspected. The 2-null rich-club benchmark reached the full requested swap target with exact degree/edge-count preservation, but it is still not a publication-grade 100-null replication. The next checkpoint is the controlled 100-null CFG decision/run.

Operational status and scientific decisions are maintained in `docs/PROJECT-STATUS.md`; the research protocol and AI handoff rules are in `docs/RESEARCH_PROTOCOL.md`.

## References

- Dorkenwald et al., Neuronal wiring diagram of an adult brain, Nature (2024).
- Schlegel et al., Whole-brain annotation and multi-connectome cell typing of Drosophila, Nature (2024).
- Lin et al., Network statistics of the whole-brain connectome of Drosophila, Nature (2024).
- Yu et al., Biological Processing Units: Leveraging an Insect Connectome to Pioneer Biofidelic Neural Architectures (2025).
- Wang et al., Neuromorphic Simulation of Drosophila Melanogaster Brain Connectome on Loihi 2 (2025).

See docs/prior-art.md for links and detailed notes.

## License

Software in this repository is released under the repository license. Biological datasets and external resources remain subject to their own licenses and terms.