# Connectome Data Model

## Current reference dataset

The first ingestion target is **FlyWire FAFB v783**. Codex provides static downloadable
snapshots intended for bulk analysis. The connection data is modeled as a directed graph:
neurons are nodes and synaptic connections are directed edges.

A connection export may contain multiple rows for the same presynaptic/postsynaptic pair
when synapses occur in different brain regions. We therefore distinguish:

- **edge rows** — rows in the downloaded connection table;
- **unique directed pairs** — unique (pre, post) neuron pairs;
- **synapse weight** — the synapse count associated with a row when supplied.

We will not silently collapse regional rows during ingestion. Aggregation is an explicit
analysis step so regional organization remains available for later motif and architecture analysis.

## Research measurements

The first graph-analysis layer will measure degree distributions, sparse connectivity,
reciprocity, regional/module structure, hub/rich-club structure, feed-forward and recurrent
motifs, and edge-weight distributions. Dynamic activity models come later.

This separation keeps the biological evidence layer distinct from the computational abstraction layer.
