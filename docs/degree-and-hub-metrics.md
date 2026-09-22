# Degree and Hub Metrics

Updated: 2026-09-22

## Why this is now a first-class constraint

Recent connectome generative-model work shows that distance alone does not reproduce
the broad degree distributions and hubs observed in fly, mouse, and human connectomes.
Conversely, degree sequence alone does not reproduce spatial structure. The generator
must therefore not treat density as a sufficient description of a biological network.

## Metrics

For both in-degree and out-degree we record:

- mean
- median
- 90th percentile
- 99th percentile
- maximum
- coefficient of variation
- fraction of nodes above a configurable hub threshold

We also record the Pearson correlation between each node's in-degree and out-degree.

The default hub threshold is 5 × mean degree. This is a reporting convention only,
not a biological definition.

## Validation sequence

1. Match total nodes and directed edges.
2. Compare density.
3. Compare in/out degree distributions.
4. Compare hub fractions and maximum degree.
5. Add modularity and short/long-range structure.
6. Add spatial/contact constraints.
7. Evaluate all synthetic networks with metrics not directly used during fitting.

## Scientific caution

A generator can match degree statistics while placing hubs in the wrong anatomical or
spatial locations. Recent work reports that long-range connectivity and hub topography
can remain poorly captured even when conventional topology metrics look similar.
Therefore hub location and long-range edge structure will become explicit validation
targets once spatial data are available.

## Reference

Salova & Kovács, Network Neuroscience (2025), "Combined topological and spatial
constraints are required to capture the structure of neural connectomes."
