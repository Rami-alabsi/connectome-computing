# Novelty Tracker

This document records what the project can currently distinguish as established
prior art, open research territory, or a potentially novel combination. It is
not a novelty or patentability opinion.

## Current assessment — 2026-09-22

The broad idea of using biological connectomes to derive computational models or
architectures is not new.

Documented prior art includes:

- Connectome-constrained neural models of Drosophila circuits and whole-brain dynamics.
- Generative models that learn or reconstruct network-generating rules from biological networks, including Drosophila brain networks.
- Connectomics-derived motifs used to constrain neural architecture search.
- Neuromorphic implementations of large fly-connectome-derived networks.
- Connectome-constrained models that connect structural wiring to measured neural activity.

## What we must not claim as new

We must not claim novelty merely because this repository:

1. uses FlyWire/FAFB data;
2. extracts graph statistics or motifs;
3. generates synthetic modular graphs;
4. maps biological motifs to computational primitives;
5. benchmarks a connectome-derived network;
6. mentions scaling toward human-brain reference constraints.

Each has substantial precedent in adjacent or directly related work.

## Potential research gap to test

The project may become distinctive if experiments demonstrate a reproducible pipeline
that jointly:

1. extracts multiple biological constraints from a real connectome;
2. generates larger synthetic computational networks while preserving a selected vector of structural and dynamical constraints;
3. separates biological constraints from generic graph priors;
4. uses controlled ablations to identify which constraints actually improve a computational workload;
5. demonstrates a scaling law or resource-efficiency advantage that survives comparisons against strong non-biological graph baselines.

This is currently a research hypothesis, not a novelty claim.

## Novelty gate

We will only mark a result as potentially new when all of the following are true:

- a targeted literature search finds no close prior method;
- the exact method is clearly specified;
- the experiment is reproducible;
- controls and ablations are included;
- the result is experimentally supported;
- the claim is narrowed to exactly what the evidence supports.

When such a point is reached, update this file and docs/PROJECT-STATUS.md with
the evidence, date, and relevant references before describing it as novel.

## Research alert rule

Whenever the project reaches a result that appears to satisfy the novelty gate,
report it explicitly to the project owner as:

NOVELTY ALERT: This specific method or result appears not to have been identified
in the targeted literature search. Evidence and limitations: ...

Do not convert "we did not find it" into "nobody has done it."
