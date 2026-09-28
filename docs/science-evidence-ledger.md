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

**Decision:** these literature updates sharpen but do not reorder the project. Gate B is closed for the defined 100-null NPC-like v783 benchmark; Gate C is the active biological control stage.


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


## 2026-09-27 — C0 product comparison audit

Two FAFB v783 spatial products were executed and must not be conflated.

1. **Princeton synapse table:** `fafb_v783_princeton_synapse_table.csv.gz` (~2.7 GB
   compressed), 80,215,790 rows, separate pre-site/post-site coordinates, and 100%
   both-centroid graph-node coverage.
2. **Lighter synapse-coordinate product:** `synapse_coordinates.csv.gz`,
   34,156,320 rows in the executed path and 86.86% both-centroid coverage.

Both use the same v783 connection graph (3,732,460 unique directed pairs after
pair aggregation and the 5-synapse threshold). The full Princeton table is the
source of record for Gate C0 because it preserves separate pre/post coordinates
and provides complete graph-node coverage.

Distance comparison:

| Metric | Princeton table | Lighter coordinate table |
|---|---:|---:|
| Both-centroid node coverage | 100.00% | 86.86% |
| Observed-edge median | 481.001 µm | 464.205 µm |
| Observed-edge mean | 653.902 µm | 674.468 µm |
| Observed-edge q95 | 1.785 mm | 1.973 mm |
| Sampled non-edge median | 2.282 mm | 2.257 mm |
| Sampled non-edge mean | 2.529 mm | 2.523 mm |

The products are qualitatively consistent about observed edges being substantially
closer than sampled non-edges, but their numerical distributions are not identical.
The Princeton table is authoritative for Gate C0.

The later C1 feasibility run that consumed the lighter centroid artifact is historical
and superseded for the primary C1 path; it does not invalidate the Princeton C0 result.

## 2026-09-27 — Gate C0 arbor-aware spatial preflight

**Evidence status:** OBSERVED / execution-valid preflight; no spatial-null inference.

- FAFB v783 Princeton synapse table: 80,215,790 rows; separate pre-site and post-site coordinates; canonical root IDs reconstructed from the documented `720575940` header suffix convention.
- Arbor proxy definition: outgoing centroid = mean outgoing synapse pre-site; incoming centroid = mean incoming synapse post-site; anisotropic 4/4/40 nm Euclidean distance.
- Coverage: 138,584/138,584 graph nodes have both centroids (100%); malformed rows = 0.
- Distance samples: 100,000 observed edges and 100,000 unique nonedges. Observed-edge median = 481,001 nm; nonedge median = 2,282,542 nm.
- Interpretation: this validates the spatial data path and shows a strong descriptive edge/nonedge distance separation, but does not establish a mechanism or a rich-club residual after spatial control.

**Prior-art anchor:** Lin et al. (Nature 2024, DOI 10.1038/s41586-024-07968-y) explicitly defined neuron pair distances using average outgoing synapse positions as an axonal-arbor proxy and average incoming synapse positions as a dendritic-arbor proxy, then compared connectivity as a function of distance. Salova & Kovács (Network Neuroscience 2025, DOI 10.1162/netn_a_00428) show that degree and spatial constraints jointly capture connectome structure better than either constraint alone.


## 2026-09-28 — Gate C1 feasibility evidence

### EVIDENCE — authoritative Princeton spatial swap feasibility passed
**Status:** EXECUTION-VALID / FEASIBILITY, not a rich-club result.

The complete FAFB v783 graph (3,732,460 directed pairs after pair aggregation and the 5-synapse threshold) has 100% node and edge coverage under the authoritative Princeton arbor-proxy centroids. A 100,000-attempt hard-binned directed swap benchmark accepted 4,156 swaps (4.156%) while preserving edge count, exact in/out-degree sequences and the complete coarse distance-bin histogram. No edges in the tested rich-club sets at degree thresholds 37, 75, 93 or 120 were excluded.

**Provenance:** C0 Run 36318477728 / artifact 10931780910 / SHA-256 7265e20db3721f6b438a93227180eb0d0b8d3ad3fd9894bcbbe4a14a81dd5f36; C1 Run 36320329317 / artifact 10932471526 / SHA-256 efa3b9837ece2920e37fde31383ea0e40f4787d5d1da6da61fc897850882ea45.

**Project consequence:** C1 feasibility is closed. The spatial rich-club null ensemble is now the active biological control. This result does not establish a spatial mechanism, significance, novelty, or computational function.


## 2026-09-28 — Gate C spatial ensemble / cross-null checkpoint

### EVIDENCE — first authoritative spatial rich-club ensemble completed

**Source:** FAFB v783, Princeton arbor-aware C0 artifact; workflow 36381489805; commit 6eb894d6e0b0cdf8d25cf3151fb0103e4f54b403; aggregate artifact 10952943175.

Four independent spatial nulls all reached 3,732,460 successful directed edge swaps and preserved edge count, exact in/out-degree sequences and the complete coarse arbor-distance-bin histogram. The spatial null uses the outgoing presynaptic arbor-proxy centroid to incoming postsynaptic arbor-proxy centroid, anisotropic 4/4/40 nm scaling, and exact preservation of the multiset of coarse distance bins.

The ensemble gives a descriptive phi_norm > 1.01 interval of degrees 51–71 and a peak at degree 62 with phi_norm = 1.0121585.

**Evidence label:** NULL-CONTROLLED / EXTENSION.

**What this supports:** a small residual rich-club enrichment remains under the project's defined degree + coarse arbor-distance constraint.

**What this does not support:** a spatial mechanism, formal statistical significance, biological causality, computational function, architecture novelty, or exact reproduction of Lin et al.'s NND model.

### EVIDENCE — cross-null observed-graph audit

CFG 100-null, NPC-like 100-null and spatial 4-null artifacts all use 3,732,460 unique directed pairs, a 5-synapse threshold after pair aggregation, and the same 20–120 degree grid. Their observed rich-club curves have identical threshold, rich-node, rich-edge and observed-density values.

The peak phi_norm values are:
- CFG: 1.057835 at degree 96;
- NPC-like: 1.015171 at degree 57;
- Spatial: 1.012159 at degree 62.

**Interpretation:** the attenuation across CFG → NPC-like → spatial is attributable to increasingly constrained null ensembles within the defined implementations, not to a change in the observed graph.

**Evidence label:** NULL-CONTROLLED / COMPARATIVE.

### LITERATURE — spatial + topology remain separate explanatory constraints

Salova & Kovács (Network Neuroscience, 2025) report that spatial constraints alone do not reproduce broad connectome topology and degree alone does not reproduce spatial structure; combined maximum-entropy models capture additional properties beyond the supplied constraints. citeturn0search0

**Project use:** the current hard-binned spatial null is a sensitivity extension. A future maximum-entropy distance model should be treated as a distinct model family rather than retroactively redefining this result.

### LITERATURE — structure→function bridge remains downstream

Lin & Murthy (Nature Methods, 2025) emphasize that connectomes connect circuit architecture to neural activity and behavior and motivate biologically realistic functional models. citeturn0search3

Zhang et al. (Fundamental Research, 2026) report structure-constrained Drosophila activation modeling, while Li et al. (bioRxiv, 2026) report FlyWire-v783-constrained whole-brain spontaneous-activity modeling. citeturn0search1turn0search4

**Project use:** these studies justify a future structure→dynamics validation stage but do not replace the current null hierarchy.

### DECISION

Gate C1 feasibility is CLOSED. The first spatial ensemble is VALIDATED but Gate C overall remains OPEN.

Next experiment: 8-null spatial stability expansion. If stable, perform a 100,000-attempt C2 NPC+spatial feasibility pilot before designing a full combined ensemble.

Runtime record: four-null spatial ensemble ~21 minutes wall-clock; estimated 8-null ~40–45 minutes and 16-null ~80–90 minutes with four-way parallelism. Estimates are planning values, not guaranteed execution times.


## 2026-09-28 — Stability experiment active

Run 36386665317 is the pre-registered 8-null stability expansion of the validated spatial sensitivity ensemble.

No scientific interpretation is permitted from partial jobs. Acceptance requires 8/8 target completion and all edge-count, in-degree, out-degree and distance-bin invariants.

Expected runtime: approximately 40–45 minutes wall-clock using four-way parallelism, based on the completed 4-null run.


## 2026-09-28 — 8-null spatial stability result

**Evidence label:** NULL-CONTROLLED / STABILITY.

The 8-null ensemble confirms the same descriptive >1.01 interval (degrees 51–71) and same peak threshold (62) observed in the first 4-null ensemble. Peak phi_norm changed from 1.0121585 (4-null) to 1.0120821 (8-null).

**What this supports:** stability of the observed qualitative result under additional random seeds for the same project-defined spatial null.

**What this does not support:** statistical significance, spatial causality, biological mechanism, or exact reproduction of a literature spatial model.

## 2026-09-28 — C2 feasibility pilot

Run 36393368885 tests whether NPC-like neuropil block constraints and the coarse arbor-distance constraint can be jointly enforced by a degree-preserving directed edge-swap move set.

The pilot is 100,000 attempts and must be interpreted only through acceptance and invariant preservation.


## 2026-09-28 — C2 pilot correction

**Failed pilot:** run 36393368885 stopped before sampling because the implementation treated 9,869 edges lacking an NPC block assignment as a fatal coverage error.

**Diagnosis:** this was inconsistent with the existing NPC-like implementation, which already treats nodes without a dominant outgoing-neuropil block as unavailable for constrained swaps. Such edges can remain frozen while preserving global degree sequences; block-pair preservation applies to the constrained portion.

**Correction:** the pilot now freezes NPC-unassigned edges, requires complete arbor-centroid coverage, and reports the size of the constrained and frozen portions explicitly.

**Corrected run:** 36394370209, 100,000 attempts, seed 20260935. At this checkpoint it is still running.

**Evidence label:** EXECUTION / FEASIBILITY ONLY.

No scientific result is assigned to either the failed or corrected pilot until the corrected run completes.


## 2026-09-28 — C2 joint-constraint feasibility

### EXECUTION EVIDENCE — baseline corrected C2 kernel
Run `36396525136`, artifact `10958119130`, FAFB v783, seed `20260935`.

The 100,000-attempt pilot accepted 1,168 swaps (1.168%) while preserving exact edge count, in-degree, out-degree, NPC block-pair counts, coarse arbor-distance-bin histogram, no self-loops and no duplicate directed edges. 9,869 edges lacking complete NPC block assignment were frozen and retained in the full graph.

**Evidence label:** EXECUTION-VALID / FEASIBILITY ONLY.

### EXECUTION EVIDENCE — block-pair-stratified C2 kernel
Run `36396805573`, artifact `10958720816`, commit `8fd9f6ad8ca6765a5ed1d60d602ff131a86a7f1c`.

The optimized proposal samples candidate edge pairs within fixed source-neuropil -> target-neuropil block classes and retains exact distance-bin acceptance. The pilot accepted 9,789/100,000 swaps (9.789%) and preserved all declared invariants.

This improves proposal efficiency without changing the declared constraint set. It does **not** establish a rich-club result, significance, mechanism, or function.

**Runtime consequence:** simple extrapolation from the pilot still implies roughly 8 h per full null on the current Python runner. A faster implementation is required before ensemble execution.

### LITERATURE UPDATE — EDR remains a distinct cross-level control
Péntek & Ercsey-Ravasz (Network Neuroscience 2025, DOI 10.1162/netn_a_00455) explicitly treat the exponential distance rule as a useful null at the Drosophila neuropil/projectome level, including prediction of several binary and weighted projectome properties. This supports retaining EDR as a later projectome-level sensitivity control, not replacing the current neuron-level C2 null. citeturn2search0turn2search1

### LITERATURE UPDATE — current structure→function bridge
Li et al. (bioRxiv 2026) fit a FlyWire v783 connectome-constrained whole-brain model to spontaneous calcium activity and use perturbations to identify a compact neuropil core and sparse hub ensemble associated with resting-state dynamics. This is model-dependent preprint evidence and belongs downstream of structural null controls. citeturn2search4

### LITERATURE UPDATE — newer connectome scope
A 2026 Nature study reports a brain-and-ventral-nerve-cord fly connectome, expanding the biological scope beyond the FAFB brain-only v783 reference. This is not a replacement dataset for the current Gate C sequence; it is a future cross-dataset generalization opportunity. citeturn2search2
