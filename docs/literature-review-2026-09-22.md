# Literature Review Checkpoint — 2026-09-22

## Why this exists

The project must use existing scientific work as input rather than rediscovering
known connectome properties and presenting them as new.

## High-value evidence incorporated

### 1. Whole-brain Drosophila network statistics

Eichler et al., *Nature* (2024), "Network statistics of the whole-brain
connectome of Drosophila", provides a direct large-scale network-analysis
reference for the fly connectome.

Implication for this project: our structural validation must go beyond edge
count and density and include network-level organization.

### 2. Connectome-constrained task models

Macke et al., *Nature* (2024), "Connectome-constrained networks predict neural
activity across the fly visual system", demonstrates that experimentally
measured connectivity can constrain a mechanistic model whose remaining
parameters are optimized for a task.

Implication: when we reach M6/M7, topology and learned dynamics must be treated
as separate experimental factors.

### 3. Spatial + topological generative constraints

Recent scalable maximum-entropy work across fly, mouse and human connectomes
shows that combining topological and spatial constraints can capture additional
biological/network properties, including synaptic weights and graphlet
statistics.

Implication: a topology-only generator is insufficient for our long-term target.
Spatial distance/contact constraints must become an explicit branch of M5.

### 4. Fly whole-brain dynamics

A 2026 preprint using FlyWire-constrained whole-brain dynamics reports that a
compact neuropil core containing sparse inhibitory hub neurons and reciprocal
connections can be important for sustaining spontaneous activity.

Implication: our hub analysis should eventually become typed and dynamical,
rather than treating all high-degree nodes as equivalent.

### 5. Neuromorphic implementation

A 2025 Loihi 2 study mapped a FlyWire-scale fly connectome to 12 Loihi 2 chips
and reported strong acceleration relative to conventional numerical simulation,
with advantages increasing for sparser activity.

Implication: sparse event-driven communication and fan-in/fan-out constraints
should be measured explicitly in M10 rather than assumed.

## Current research position

None of these observations is claimed as novel by this project.

The research opportunity remains the experimentally validated combination of:

- multi-constraint biological extraction;
- scalable synthetic expansion;
- explicit ablations separating biological constraints from generic graph priors;
- computational workload evaluation;
- resource/communication measurements;
- scaling behavior.

The exact method must be checked against prior art again when it becomes concrete.
