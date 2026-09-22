# Atomic-Structure Analogy for Connectome Architecture

## Status
**Hypothesis / cross-domain design analogy — not a biological claim and not evidence that neural systems obey atomic rules.**

The atomic analogy is useful because an atom is not an undifferentiated set of particles. Its structure emerges from discrete levels and sublevels, bounded occupancy, energy ordering, filling of available states, and interactions among occupied states.

Electron configurations follow the Aufbau principle: available subshells are filled in increasing energy order subject to quantum-number and Pauli constraints. A shell with principal quantum number n has maximum capacity 2n^2; subshell capacities are s=2, p=6, d=10, f=14. These are physical constraints, not an architectural recipe.

## Architectural hypothesis
Test whether scalable computation benefits from a related **bounded-capacity hierarchy**:

```
local processing unit
    |
    | capacity / state-space budget
    v
module
    |
    | interface capacity / communication budget
    v
higher-order module
    |
    | sparse coordination
    v
global integration layer
```

The transferable abstraction is not neuron=electron. It is: a scalable system may benefit when each level has bounded local capacity and structured interfaces, while additional complexity is accommodated by higher-order organization rather than arbitrary densification.

## Candidate computational rules

### R1 — Bounded local occupancy
Each module has explicit limits on node count, active recurrent edges, event rate, state dimension, and inter-module communication.

### R2 — Saturation-triggered expansion
When a module approaches a defined capacity threshold, new computation preferentially activates a peer module, creates a higher-order module, or uses sparse cross-module routing rather than densifying all local connections.

### R3 — Energy/cost ordering
Candidate routes or hierarchy levels receive computational/resource costs. Lower-cost local routes are preferred until capacity or performance saturates; higher-cost long-range routes are then recruited.

### R4 — Interface/valence constraint
A module can have many internal connections but a limited number of high-value external interfaces. Test dense local processing + sparse external interfaces against uniformly distributed connectivity under equal budgets.

### R5 — Discrete hierarchy levels
Use discrete levels L0 -> L1 -> L2 -> L3 and measure where additional levels stop improving memory, multitasking, temporal diversity, robustness, or communication efficiency.

## Proposed experiment
Generate families with matched node count, directed edge count, degree distribution, approximate modularity, and wiring-cost budget.

- **A Uniform-density:** connectivity spread without capacity-triggered hierarchy.
- **B Hierarchical-capacity:** modules have bounded local capacity; saturation introduces peers/higher levels.
- **C Hierarchical-capacity + sparse backbone:** B plus a small coordination backbone.
- **D Random hierarchy control:** same levels and approximate edge counts, but hierarchy assignment randomized.

Measure task performance, memory capacity, timescale diversity, motifs, rich-club structure, participation coefficient, hierarchy crossing, long-range fraction, wiring cost, communication/event cost, fault tolerance, and parameter count.

## Falsification
The analogy is not useful if bounded-capacity hierarchy provides no measurable benefit after matching density, degree, edge count, spatial cost, parameter count, and compute/event budget. If deeper hierarchy always wins, that also weakens the specific saturation hypothesis.

## Important distinction
Atomic shell filling has exact physical rules from quantum mechanics. Our architecture has no reason to inherit the exact values 2n^2 or 2/6/10/14. We should test the abstraction **bounded capacity -> saturation -> structured expansion -> sparse interfaces**, not copy atomic numbers into the neural generator.

## Relation to current project
This extends **Parallel Hierarchical Distributed Control** with a possible capacity law:

```
parallel modules
      ↓
bounded local capacity
      ↓
local saturation
      ↓
new peer / higher-order module
      ↓
sparse coordination
      ↓
global integration
```

No novelty claim is made. Exact prior-art search is required once the mechanism is implemented as a precise generator and benchmark.
