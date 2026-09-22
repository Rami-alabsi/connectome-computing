# Architecture Primitives

This document defines the project's first computational abstraction layer.

The project does **not** assume that a biological structure is automatically useful
for computation. Each primitive is a falsifiable hypothesis. A primitive becomes
an evidence-backed architectural rule only after controlled experiments.

## Abstraction pipeline

```text
Connectome observation
        |
        v
Structural statistic / motif
        |
        v
Biological context
        |
        v
Computational hypothesis
        |
        v
Architecture primitive
        |
        v
Controlled benchmark
        |
        v
Validated design rule
```

## Initial hypotheses

| ID | Primitive | Mechanism | Required evidence |
|---|---|---|---|
| AP-001 | Sparse Event Routing | Event-driven selective communication | Communication/energy advantage |
| AP-002 | Recurrent State Loop | Local persistent state | Temporal-task advantage |
| AP-003 | Modular Processing Unit | Semi-independent modules | Lower cross-module traffic |
| AP-004 | Hub-Mediated Integration | Selective global aggregation | Faster cross-module integration |
| AP-005 | Motif Microcircuit | Reusable local connectivity pattern | Task benefit after controls |

These are hypotheses, not conclusions.

## Experimental rule

Every claimed benefit should have:

1. a biological observation;
2. a null or matched structural control;
3. a defined workload;
4. a measurable metric;
5. an ablation or counterfactual test;
6. reproducible configuration and seed.

## Architecture target

The long-term architecture is not intended to imitate individual neurons.
It should expose a small set of computational primitives that can be composed
into larger systems while retaining measurable properties of the biological
source.
