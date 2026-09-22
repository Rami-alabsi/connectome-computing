# M6-RSS — Dynamic Relational State Space benchmark

## Purpose

This experiment operationalizes the **Relational State Space (RSS)** hypothesis:
hierarchy is treated as one relational coordinate, alongside overlapping layers,
context, temporal activation, and bounded higher-order group relations.

This is a classical engineering benchmark. It is not a model of human social
behavior, brain physics, quantum gravity, or a literal fourth spatial dimension.

## Conditions

| Condition | Representation | Dynamic routing | Higher-order |
|---|---|---:|---:|
| A | flat pairwise | state-ranked | no |
| B | fixed hierarchy | no | no |
| C | overlapping context layers | yes | no |
| D | overlapping context layers | yes | bounded |

All conditions expose the same active-relation budget and bytes-per-relation in
the benchmark configuration.

## Tasks

- **global** — target depends on an aggregate over all modules.
- **pair** — target depends on a specific ordered module pair.
- **context** — target depends on the currently selected overlapping group.
- **temporal** — target changes with the context sequence and tests whether the
  active relational structure follows that sequence.

## Metrics

- absolute task error;
- active relation count;
- transmitted bytes;
- routing churn between successive contexts;
- explicit higher-order relation activation.

The benchmark deliberately does not collapse these into a single score.

## Controls and interpretation

A result is not evidence for an architectural advantage merely because dynamic
routing reduces error. The effect must survive matched active-relation,
parameter, interface-state and byte budgets. A random context-dependent routing
control and a fixed-overlap control are planned next.

The benchmark is therefore a **mechanism test**, not a novelty test.

## Prior-art boundary

Multilayer, temporal and higher-order networks are established research areas.
A 2026 review explicitly treats their integration as an active network-science
direction, while a 2026 Nature Reviews Physics review documents collective
dynamics from interactions involving more than two nodes. Recent brain work also
shows higher-order metrics can reveal information beyond pairwise connectivity.
These sources justify the experimental variables but do not establish the
specific Connectome Computing combination as novel.

## Current execution status

Implementation and deterministic unit tests have been committed. GitHub Actions
has been triggered on the current main commit. Results must be read from the
uploaded CSV artifact after the run completes; no scientific result is claimed
from code existence or CI success alone.
