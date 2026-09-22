# Literature Review Checkpoint — 2026-09-22

## Purpose

This project treats current neuroscience as a moving scientific constraint set. Every
major architecture rule is checked against recent work before it is promoted from
hypothesis to implementation requirement.

## New 2026 evidence reviewed

### Human hierarchy is state-dependent

Oh et al., *Nature Neuroscience* (1 Sep 2026), reports a data-driven framework for
human cortical signal-flow hierarchy. Integrated effective connectivity recovered
directionality consistent with histological feedforward/feedback organization, with
a hierarchy spanning sensorimotor, association and paralimbic areas.

**Design implication:** hierarchy cannot be represented only as a static community tree.
M5 should preserve a structural hierarchy, while M6 should allow direction, state and
dynamics to modify effective information flow.

### White-matter tracts cross hierarchical levels

Bagautdinova et al., *Nature Human Behaviour* (31 Aug 2026), found that white-matter
tract placement across the cortical hierarchy relates to cognitive diversity:
within-level tracts connect biologically similar regions, while hierarchy-spanning
tracts bridge distinct biological milieus.

**Design implication:** long-range edges need at least two classes in experiments:
within-level reinforcement and cross-level integration. A single undifferentiated
shortcut parameter is too coarse for the human reference model.

### Multiscale structure constrains dynamics

Xia et al., *Communications Biology* (25 Jun 2026), found that multiscale structural
connectome eigenmodes captured spontaneous and task-evoked functional activity better
than conventional structural approximations in the studied human datasets.

**Design implication:** M6 should keep topology and dynamics separate, but the interface
must support multiscale operators/eigenmodes rather than only node-local recurrence.

### Rich-club structure has measurable control consequences

Podschun et al., *Human Brain Mapping* (Mar 2026), used network-control analysis and
reported higher control energy and lower state stability when rich-club regions were
prevented from controlling dynamics compared with size-matched peripheral regions.

**Design implication:** rich-club nodes should be treated as an explicit architectural
resource candidate. We must measure whether they improve communication/control per unit
of cost rather than assume they do.

### Spatially distributed control matters

Betzel et al., *Communications Biology* (28 Feb 2026), extended network control to
spatially diffuse inputs whose influence decays with distance and reported lower energy
requirements and fewer input sites in the studied human connectome models.

**Design implication:** spatial coupling should not be reduced to a wiring-cost penalty.
The architecture layer should eventually model spatially distributed influence and
control radius.

### Fly dynamics are becoming experimentally observable at higher temporal resolution

Gauthey et al., *Nature Communications* (28 Apr 2026; version of record 3 Jul 2026)
demonstrated whole-brain Drosophila calcium imaging at 28 volumes/s and up to 60 volumes/s
for the central brain, revealing fast auditory responses that standard volumetric
imaging can miss.

**Design implication:** activity-derived constraints are becoming more informative.
M6 validation should eventually use temporal statistics, not only static graph metrics.

### Fly connectome topology alone is not enough to reproduce resting dynamics

A 2026 *Nature Communications* study using a whole-brain FlyWire-constrained spiking
model reported that directly implementing anatomical connectivity did not reproduce
resting activity and cross-neuropil correlations accurately; training synaptic weights
was required in that model.

**Design implication:** anatomical topology is a constraint, not a complete specification
of dynamics. This directly supports separating fixed structure from learnable dynamics.

### Energy-information trade-offs are being measured directly in fly circuits

Dhiman & Panwar, *Scientific Reports* (19 May 2026), combined Drosophila optic-lobe
connectome structure, connectome-constrained dynamics and an explicit energy proxy to
study energy-information trade-offs.

**Design implication:** resource cost must enter our benchmark suite. A graph that matches
biology but requires disproportionate communication or memory traffic is not an
engineering success.

### Algorithm-hardware co-design is now using explicit fast/slow memory pathways

Sun et al., *Nature Machine Intelligence* (16 Jun 2026), reported a spiking architecture
with a compact slow memory pathway alongside event-driven spiking, with hardware
co-design targeting sparse communication and memory constraints.

**Design implication:** M10 should not map only neurons to cores. It should model
communication, state storage and memory locality as first-class constraints.

## Stable earlier evidence

- Whole-brain Drosophila network statistics establish the need for network-level
  validation beyond density and edge count.
- Connectome-constrained fly visual models show that topology can constrain task models
  while remaining synapse/neuron parameters are optimized.
- Cross-species spatial + topological generative models motivate combining distance/contact
  and degree/topology constraints.
- FlyWire-scale neuromorphic mapping demonstrates the relevance of sparse irregular
  recurrent communication to hardware resource limits.

## Current synthesis

The strongest current architecture hypothesis is therefore not “copy the brain”.
It is:

**hierarchy + modular local computation + sparse cross-module integration + expensive
connector/rich-club resources + spatially constrained wiring + recurrent state + explicit
resource budgets.**

Each term remains a hypothesis until it survives controlled comparison with non-biological
baselines.

## Scientific status

No claim of novelty or engineering superiority is made here. Exact prior art must be
checked again when the combined generator, dynamics model and benchmark protocol are fixed.
