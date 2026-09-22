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

## Evidence classes

- **Established:** repeatedly measured or strongly supported in the cited literature.
- **Promising:** recent result that should influence experiments but needs replication or broader testing.
- **Hypothesis:** project-specific engineering interpretation.
- **Novelty candidate:** only after exact prior-art search and reproducible controls.

## Scientific rule

A literature result is never copied into the architecture as an unquestioned truth.
The project records the observation, the proposed abstraction, its falsifiable prediction,
and the control required to separate the biological effect from generic graph effects.
