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

## Evidence classes

- **Established:** repeatedly measured or strongly supported in the cited literature.
- **Promising:** recent result that should influence experiments but needs replication or broader testing.
- **Hypothesis:** project-specific engineering interpretation.
- **Novelty candidate:** only after exact prior-art search and reproducible controls.

## Scientific rule

A literature result is never copied into the architecture as an unquestioned truth.
The project records the observation, the proposed abstraction, its falsifiable prediction,
and the control required to separate the biological effect from generic graph effects.
