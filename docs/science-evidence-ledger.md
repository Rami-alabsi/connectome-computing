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
