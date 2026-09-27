# Science Evidence Ledger

Updated: 2026-09-22

This ledger records which scientific observations are being converted into project
hypotheses, what is actually established, and what experiment is required before
an engineering claim is made.

| Finding | Evidence status | Project use | Required validation |
|---|---|---|---|
| Fly whole-brain network has rich-club structure, reciprocal/recurrent motifs and strong global connectivity despite sparsity | Established in whole-brain FlyWire analysis | hubs, reciprocity, motifs | degree-preserving and threshold-matched nulls |
| Human cortical hierarchy reorganizes with brain state | 2026 empirical/modeling study | structural hierarchy + dynamic effective hierarchy | M6 state-dependent flow experiment |
| Human white-matter tracts cross hierarchy and bridge distinct biological systems | 2026 human connectome study | typed hierarchy-crossing long-range edges | compare within-level vs cross-level edges |
| Multiscale structural eigenmodes constrain functional dynamics | 2026 human study | multiscale topology-to-dynamics interface | held-out activity reconstruction |
| Human spatially diffuse control can reduce control energy and input count | 2026 network-control study | spatial influence/control model | compare point vs diffuse control under equal resources |
| Mammalian connectomes combine modular cooperation with diffuse long-range competition | 2026 cross-species study | inhibitory/competitive long-range channel | topology-matched cooperation-only ablation |
| Hierarchical modular reservoirs can improve memory/multitasking and brain-like timescales | 2026 neuromorphic study | hierarchy as computational hypothesis | random, flat-modular and hierarchy controls |
| Unified fly brain-and-cord connectome shows local feedback loops linked by long-range ascending/descending circuits | 2026 Nature study | distributed embodied control | local-loop vs centralized-control ablation |
| Fly anatomical connectome alone does not reproduce resting dynamics without learned weights | 2026 whole-brain spiking study | separate structure from learned dynamics | fixed-weight vs trained-weight comparison |
| Fly optic-lobe models show energy-information trade-offs and statistical regularity | 2026 study | explicit resource objective | task/information per energy proxy |
| Event-driven hardware co-design remains constrained by memory and communication | recent neuromorphic literature | M10 hardware/resource layer | memory traffic, events, latency, energy |
| Fly whole-brain dynamics model identifies a compact core containing sparse inhibitory hubs with reciprocal excitatory partners as a mechanism sustaining resting dynamics | Promising (2026 preprint; not yet peer reviewed) | candidate control-backbone primitive; typed reciprocal E-I motifs | fixed-weight vs learned-weight; hub ablation; matched-degree null |
| Human rich-club regions can be important for controlling transitions between cognitive states, with higher control energy when rich-club nodes are excluded | Promising (2026 human network-control study) | test whether a small expensive backbone can provide integration/control | size-matched peripheral controls; equal-resource comparisons |
| Combined mammalian evidence links modular cooperation with diffuse long-range competition and hierarchical/synergistic dynamics | Promising / cross-species | local cooperative modules + sparse long-range competitive channel | cooperation-only, competition-only and sign-shuffled controls |
| Spatial + topological maximum-entropy models predict additional connectome properties beyond their fitted constraints | Established across fly, mouse and human datasets | fit topology and geometry jointly rather than as independent heuristics | held-out graphlets, weights and wiring-cost prediction |
| Mesoscale participation and hierarchy-crossing connectivity provide measurable separation between local specialists and cross-module integrators | Established network-science measures; biological interpretation remains model-dependent | M5 validation metrics for local/global organization | degree-preserving, module-preserving and spatial nulls |
| Fly visual pathways are shallow and parallel, while fine spatial sampling persists into central brain regions | Promising/established for the studied visual pathways (Cell 2026) | avoid assuming deep serial hierarchy; allow parallel feature pathways with spatial maps | deep-serial hierarchy and spatially shuffled controls |
| Fly brain-and-cord control is distributed and embodied, with local body-part feedback loops linked by long-range ascending/descending circuits | Established (Nature 2026) | distributed local controllers + sparse coordination layer | centralized-controller ablation |

| Quantum entanglement has multipartite shareability/monogamy constraints | Established quantum-information result | investigate bounded high-value relational capacity rather than unlimited strong cross-module coupling | equal-edge-count strength-distribution controls |
| 2025-2026 quantum-network studies show entanglement routing is constrained by fidelity, coherence, memory, errors and bottlenecks | Established engineering/physics evidence | treat interface/routing capacity as dynamic stateful resources | shortest-path, unrestricted-bandwidth and static-routing controls |
| Tensor networks provide structured multiscale representations of high-dimensional states | Established computational method | compact effective module states and scale-dependent interfaces | raw-state vs pooled vs learned compressed state |
| Holographic tensor-network models connect boundary representations, entanglement and quantum-error-correction properties | Established within theoretical models | test constrained boundary/interface representations and structured redundancy | full-state access and uniform-redundancy controls |
| Emergent-geometry interpretations from entanglement/tensor networks | Theoretical framework / promising cross-domain abstraction | test whether effective communication geometry predicts dynamics beyond raw Euclidean distance | Euclidean-only and graph-distance controls |

## Evidence classes

- **Established:** repeatedly measured or strongly supported in the cited literature.
- **Promising:** recent result that should influence experiments but needs replication or broader testing.
- **Hypothesis:** project-specific engineering interpretation.
- **Novelty candidate:** only after exact prior-art search and reproducible controls.

## Scientific rule

A literature result is never copied into the architecture as an unquestioned truth.
The project records the observation, the proposed abstraction, its falsifiable prediction,
and the control required to separate the biological effect from generic graph effects.


| 2026 neuromorphic hierarchical-reservoir study finds performance gains saturate after limited hierarchy depth in its tested tasks | Established for the studied reservoir experiments | test shallow hierarchy and parallel pathways rather than assuming deep fractal scaling | flat-modular, random and deeper-hierarchy controls with matched density/degree |
| 2026 community-aware sparse SNN topology work reinforces that sparse topology can be designed jointly with communities for efficient spiking computation | Promising engineering evidence | preserve community structure while minimizing active communication | degree/density-matched random sparse topology |
| 2026 cortical microcircuit generative-model work learns compressed latent structure and links generated circuits to reservoir tasks | Promising cross-domain prior art | treat compressed generative representations as a possible M5/M6 interface | explicit parameter-count and held-out-structure controls |


| 2025 Nature Communications modular-resource study reports that structural modularity does not generally guarantee functional specialization and that narrow bottlenecks can increase specialization in the studied toy networks | Established for the studied model; not a general brain law | Q1 effective-state/interface experiment | dense communication, shared-readout and randomized-interface controls |
| 2026 Conditional Rate–Utility communication-edge inference explicitly optimizes task utility against communication rate with adaptive bottlenecks | Established engineering prior art | interface bandwidth should be measured as a first-class resource | fixed/unrestricted bandwidth controls |
| 2026 tensor-network bottleneck compression demonstrates compact MPO representations of classical neural bottlenecks in hybrid quantum-classical experiments | Established computational prior art | compact effective-state interfaces are clearly not novel in isolation | dense parameterization and equal-resource compression controls |
| 2026 hyperbolic temporal graph learning demonstrates scalable hierarchical/dynamic graph representations in hyperbolic space | Established ML prior art | effective geometry remains an optional controlled branch, not a biological assumption | Euclidean and graph-distance controls |
| 2026 selective redundancy work shows targeted fault-tolerance can reduce resource overhead relative to uniform replication in its FPGA setting | Promising engineering evidence | Q3 targeted redundancy benchmark | no-redundancy and uniform-redundancy controls |

| 2026 higher-order brain interaction analysis finds redundancy, synergy and topological scaffold measures reveal collective structure beyond pairwise connectivity and align with cortical hierarchy | Established for the studied HCP datasets/methods | test bounded higher-order module coordination as a separate M6 branch | pairwise-only and matched-resource controls |
| 2026 naturalistic human connectome study reports a conserved degree-based backbone with context-flexible rich-club recruitment | Promising/established for the studied naturalistic datasets | distinguish stable infrastructure from state-dependent hub/routing selection | static hub set, degree-matched and context-shuffled controls |
| 2025 neural-module resource study shows specialization varies dynamically with information-flow timing and bandwidth | Established for its controlled model | make interface bandwidth a dynamic experimental variable, not only a static topology property | high-bandwidth, low-bandwidth and timing-shuffled controls |


| Cosmic web is a multiscale network of nodes, filaments, sheets and voids generated by gravitational structure formation | Established cosmological evidence | add a field-mediated relational layer as an independent cross-domain abstraction | explicit-edge, latent-field and hybrid field+backbone controls under matched communication budgets |
| Cosmic connectivity and filament connectivity can be quantified and depend on scale/environment | Established in cosmological network studies | motivate explicit measurement of connectivity/corridor structure | scale, distance and mass/environment matched nulls |
| 2026 cosmic-web force analysis finds filaments can dominate local gravitational/tidal influence in several web environments | Recent simulation evidence | motivate low-dimensional influence-field abstraction | filament-only, node-only and full-field controls |


## 2026-09-24 literature refresh — spatial/topological controls and connectome-constrained dynamics

### EVIDENCE — EDR is now a required spatial null candidate
**Source:** Péntek & Ercsey-Ravasz, *Network Neuroscience* 9(3), 869–895 (2025), DOI 10.1162/netn_a_00455.

The study uses FAFB v783 and reports that an exponential-distance-rule (EDR) model explains numerous binary and weighted properties of the Drosophila neuropil projectome. It explicitly presents EDR as a useful null model for identifying properties not explained by geometric constraints, including asymmetric connection weights. This strengthens the project's planned spatial/distance Gate C: a generic spatial null is not sufficient; the EDR formulation should be considered as a literature-backed candidate control.

**Evidence class:** OBSERVED / NULL-CONTROLLED in the cited study.  
**Project consequence:** add EDR-based null to Gate C design; do not implement until neuron/neuropil distance semantics are fixed.

### EVIDENCE — topology + spatial constraints should be tested jointly
**Source:** *Combined topological and spatial constraints are required to capture the structure of neural connectomes* (2025).

Across fly, mouse and human connectomes, the study reports that spatial constraints alone do not reproduce broad degree structure and degree sequence alone does not reproduce spatial structure. It therefore motivates combined maximum-entropy models incorporating both classes of constraints.

**Evidence class:** NULL-CONTROLLED / CROSS-SPECIES.  
**Project consequence:** Gate C should retain separate spatial and topology controls and include a combined constraint condition where computationally feasible.

### EVIDENCE — recent whole-brain modeling links wiring to activity only through an explicit generative model
**Source:** Li et al., bioRxiv 2026, *Connectome-constrained modeling identifies neurons and synapses that sustain spontaneous activity in Drosophila*.

The work fits a whole-brain dynamical model to spontaneous calcium activity while constraining the model by the FlyWire connectome, then uses perturbations to identify a compact neuropil core and sparse inhibitory hub ensemble associated with resting-state dynamics. The authors emphasize that connectome wiring alone does not specify activity; the bridge is a fitted generative dynamical model validated against independent observations.

**Evidence class:** HYPOTHESIS / MODEL-CONSTRAINED, preprint.  
**Project consequence:** reinforces the project's rule that structural findings and functional findings must remain separate until a validated dynamical model/benchmark connects them.

### EVIDENCE — current FlyWire literature is expanding from topology to pathway-level and behavioral organization
FlyWire's current publication index includes 2026 work on visual pathways, behavioral control, modular presynaptic organization, and whole-brain/nerve-cord connectomes. The September 2026 Cell paper on visual pathways reports shallow hierarchical organization, feature-biased pathway classes, broad spread with focal convergence, and preservation of fine spatial sampling into the central brain.

**Evidence class:** OBSERVED / ANALYSIS.  
**Project consequence:** pathway hierarchy and spatial sampling are relevant future observables, but they are not specifications for the computational architecture and should not be promoted to architecture claims without controlled abstraction experiments.

### REVIEW NOTE — rich-club interpretation remains conservative
The 2024 Lin et al. rich-club result remains the primary direct prior-art anchor for Gate A/B. The 2025–2026 literature above does not invalidate the project's CFG→NPC-like→spatial control hierarchy; instead it strengthens the need to test geometry and activity separately.

## 2026-09-27 literature refresh

| Finding | Evidence status | Project use | Required validation |
|---|---|---|---|
| Combined spatial and topological constraints improve prediction of connectome structure across fly, mouse and human | Established in the cited 2025 study | Gate C combined null design | observed vs CFG vs spatial vs combined; held-out structural metrics |
| EDR explains numerous binary/weighted properties of the Drosophila neuropil projectome and is proposed as a null model | Established in the cited 2025 study | candidate spatial Gate C null | verify distance semantics and neuron-level applicability before implementation |
| Fly connectome-constrained whole-brain dynamics can identify candidate cells/synapses associated with spontaneous activity when fitted to recordings | Promising; 2026 preprint | future structure-to-dynamics bridge | independent activity validation and perturbation/ablation |
| Simplified dynamics on real Drosophila network structure can reproduce studied activation patterns, with network distance differing from physical distance | Established for the cited model | keep graph-distance and physical-distance controls conceptually separate | matched dynamical models and controlled rewiring |
| Full/partial Drosophila connectomes have already been used in reservoir computing, fixed recurrent processing units and neuromorphic hardware | Established prior art | prevents overclaiming computational novelty | targeted prior-art search before architecture/IP claims |
| Recent fly-connectome reviews emphasize linking wiring to activity and behavior through explicit models | Review/context | reinforces evidence ladder | structural null -> dynamics -> task validation |

**Decision:** these literature updates sharpen but do not reorder the current
project. Gate B remains the immediate unfinished scientific gate.


## 2026-09-27 targeted literature refresh — new practical evidence

| Finding | Evidence status | Project use | Required validation |
|---|---|---|---|
| A 2026 Nature study analyzes distributed control circuits across a fly brain-and-cord connectome, extending connectome organization beyond isolated brain topology | Established for the cited dataset/analysis | keep distributed control and pathway-level organization as future observables; do not equate distributed control with a computational primitive | brain-only vs brain-and-cord matched analyses if the project later expands scope |
| A 2026 connectome-constrained whole-brain model fitted to spontaneous calcium recordings identifies a compact neuropil core and sparse inhibitory hub ensemble sustaining modeled resting-state dynamics | Promising model-constrained evidence; preprint | strengthens the requirement for an explicit structure-to-dynamics bridge after structural null controls | independent activity validation, perturbation and matched structural controls |
| A 2025 peer-reviewed reservoir study finds Drosophila connectome topology and synaptic weights can improve overfitting resilience in studied time-series tasks, with hybrid topology/weight controls | Established for the studied reservoir benchmark | confirms that topology/weights-to-task mapping is already prior art; useful as a future baseline for any computational primitive | matched-resource baselines, topology-only, weight-only and randomized controls |
| 2024–2025 rich-club work remains the direct prior-art anchor for CFG/NPC interpretation | Established | preserves the current Gate A→B→C control order | complete NPC ensemble before changing gate state |

**Current decision:** no reordering of the scientific pipeline. The immediate blocker remains completion and inspection of the NPC 100-null ensemble.


## 2026-09-27 Gate C literature/preflight checkpoint

### EVIDENCE — neuron-level spatial data are available for FAFB v783
Codex documents a downloadable Marked Neuron Coordinates product for FAFB v783.
The current public snapshot is v783 with 139,255 neurons and 3,732,460 connections.
The coordinate product is a separate input from the connection table and must be
version-pinned and checksummed before use.

**Project use:** use the coordinate product only for a first node-position spatial
null. Do not call the coordinate position an axon length, arbor length, or
synapse coordinate.

### EVIDENCE — distance-only is insufficient as the sole biological control
Salova & Kovács (2025) show across fly, mouse and human connectomes that spatial
constraints alone do not reproduce broad topology such as the degree sequence,
while degree alone does not reproduce spatial structure. Their combined
maximum-entropy models use both topology and spatial constraints.

**Project use:** Gate C requires a degree+spatial control after the spatial
inventory. A distance-only model is a sensitivity control, not the final
degree-sensitive test.

### EVIDENCE — EDR is useful but has a level mismatch
Péntek & Ercsey-Ravasz (2025) show that an exponential distance rule can explain
many properties of the Drosophila projectome and explicitly use EDR as a null for
geometry-driven effects.

**Project use:** include EDR as a projectome/neuropil sensitivity control. Do not
replace the neuron-level NPC rich-club null with EDR without demonstrating the
level conversion.

### Gate C decision
The repository now contains:
- docs/GATE-C-SPATIAL-DESIGN.md;
- scripts/run_fafb_spatial_preflight.py;
- .github/workflows/m2-fafb-spatial-preflight.yml.

The preflight must report coordinate coverage, schema, anisotropic voxel scaling,
checksums, sampled edge/non-edge distances, and missing-coordinate policy before
any spatial randomization. It is explicitly non-conclusive.
