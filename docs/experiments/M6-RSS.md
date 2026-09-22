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

All conditions expose the same configured active-relation budget and
bytes-per-relation. The current benchmark uses the active route endpoints as
the only source states available to the receiver.

## Tasks

- **global** — target depends on an aggregate over all modules. A condition
  receives only the subset of source states represented by its active routes.
- **pair** — target depends on a specific ordered module pair. The prediction is
  exact only when both target endpoints are transmitted.
- **context** — target depends on the currently selected overlapping group.
- **temporal** — target changes with the context sequence and tests whether the
  active relational structure follows that sequence.

The target is computed from the full hidden fixture state only for evaluation.
The prediction path is restricted to transmitted source states.

## Metrics

- absolute task error;
- active relation count;
- transmitted bytes;
- routing churn between successive contexts;
- explicit higher-order relation activation.

The benchmark deliberately does not collapse these into a single score.

## Information-flow integrity gate

The earlier prototype allowed some global predictions to read the complete
fixture state directly. That was an implementation shortcut, not a valid
communication experiment. It has now been removed.

The current benchmark enforces:

**hidden source states → selected communication routes → visible source subset → prediction**

Therefore a condition cannot obtain a zero-error result by reading states that
its routing policy did not transmit.

The pair task also explicitly requires both target endpoints, preventing the
benchmark from treating an unrelated route as successful pairwise information
transfer.

## Controls and interpretation

A result is not evidence for an architectural advantage merely because dynamic
routing reduces error. The effect must survive matched active-relation,
parameter, interface-state and byte budgets.

Required controls:

- fixed overlapping groups;
- random context-dependent routing with the same active-route budget;
- parameter/interface-dimension matching;
- matched active-relation count;
- shuffled higher-order relation null;
- stable-core + flexible-periphery ablation;
- sparse brokerage ablation.

The benchmark is therefore a **mechanism test**, not a novelty test.

## Prior-art boundary

Dynamic routing is established: learned dynamically routed neural networks have
been systematically studied for years, and network-routing literature includes
candidate-path, multipath and opportunistic routing. Recent 2026 work also
explicitly evaluates dynamic multi-path candidate decoding. These establish that
multiple candidate routes and state-dependent route selection are not novel by
themselves. citeturn0search14turn0search8turn0search15turn0search0

The research question here is narrower: whether a **resource-bounded,
overlapping, higher-order relational state space with controlled information
interfaces** provides an independent engineering benefit, and later whether a
bounded delayed-commitment/potential-path mechanism adds benefit beyond ordinary
dynamic routing. That remains unproven.

## Current execution status

The information-flow semantics have now been corrected in code and protected by
unit tests. GitHub Actions must be inspected after the new commits complete,
including the uploaded CSV artifact. No scientific result is claimed until the
artifact and matched controls have been evaluated.
