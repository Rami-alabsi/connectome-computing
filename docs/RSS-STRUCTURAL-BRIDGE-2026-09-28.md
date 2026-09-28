# RSS ↔ FAFB Structural Bridge — 2026-09-28

## Question

Which of the existing RSS mechanisms C/D/J has a structural substrate in the FAFB connectome that is strong enough to justify a testable hypothesis, without treating the connectome as a specification?

RSS definitions:
- C: dynamic layered/context-prioritized routing over the full candidate pool.
- D: dynamic higher-order/collective coordination using bounded group pooling.
- J: dynamic layered routing with brokerage/overlap nodes removed from contextual priority under matched resources.

These are computational hypotheses. A static connectome cannot by itself establish dynamic routing, context dependence, or computational benefit.

## Evidence matrix

| RSS mechanism | FAFB / fly-connectome evidence | What it supports | What it does not establish |
|---|---|---|---|
| C — dynamic layered/context-prioritized routing | Whole-brain work identifies hierarchical modular organization, neuropil-specific pathways, and rich-club neurons distributed across sensory modalities. The 2026 visual-pathway study reports shallow, parallel feature-biased pathways with spatial organization persisting into central brain. | A structural substrate for multiple layers/pathways, parallel routes, and context-specific candidate routing. | The dynamic priority rule or context-dependent switching itself. |
| D — bounded collective coordination | Whole-brain analyses report over-represented reciprocal/recurrent three-node motifs; rich-club/integrator/broadcaster populations provide convergence/divergence; connectome-constrained dynamics work identifies a compact core with sparse inhibitory hubs and reciprocal excitatory partners. | A substrate for local collective motifs, convergence/divergence, and bounded coordination hypotheses. | That bounded pooling is the causal or computational principle, or that it improves tasks. The 2026 dynamics result is model-dependent preprint evidence. |
| J — brokerage/overlap-node ablation | Rich-club neurons are more likely to span hemispheres and bridge optic-lobe ↔ central-brain bottlenecks; integrators/broadcasters are explicitly identified. The 2026 brain-and-cord connectome finds long-range ascending/descending circuits linking distributed local control modules. | Strong structural basis for testing bridge/broker nodes as a matched ablation/control. | That broker removal improves routing, robustness, efficiency, or generalization. |

## Current interpretation

J has the clearest direct structural substrate, because bridge/integrator/broadcaster populations are already explicit connectomic observables.

C has a substantial structural substrate, because hierarchical modular organization and parallel pathways are directly observed, but the dynamic/context-priority component remains unproven.

D has the weakest direct bridge to a specific computational mechanism. Motifs and convergence/divergence support the existence of collective structures, but they do not uniquely imply bounded pooling.

This ordering is an evidence assessment, not a ranking of the mechanisms as engineering choices.

## Critical Gate-C boundary

The current FAFB Gate-C result does not demonstrate C, D, or J. The spatial null only shows that the rich-club residual changes under increasingly constrained structural nulls. The missing C2 question is whether the residual remains when NPC-like mesoscale organization and arbor-distance structure are constrained simultaneously.

Therefore the correct bridge is:

surviving structural residual → identify candidate structural observable → map that observable to C/D/J hypothesis → matched computational ablation

not:

rich-club residual → RSS mechanism.

## Required next tests after Gate C

1. Complete the C2 joint NPC + spatial control only after exact sampler/runtime validation.
2. If a structural residual survives, compute explicit broker/bridge observables in FAFB v783:
   - participation across neuropils;
   - cross-module/hemisphere bridge counts;
   - betweenness or flow-bottleneck proxies;
   - rich-club membership overlap with bridge populations;
   - integrator/broadcaster overlap;
   - spatial cost of those bridge edges.
3. For C, test whether observed hierarchical/parallel structure predicts the benefit of context-prioritized routing under matched candidates and budgets.
4. For D, test whether motif/convergence structure predicts bounded collective pooling benefit beyond degree- and candidate-topology-matched controls.
5. For J, remove matched-size bridge/broker populations and compare against degree-, module-, and resource-matched removals.
6. No mechanism receives a biological or computational claim until its matched ablation is positive and reproducible.

## Literature anchors

- Lin et al., Nature (2024): whole-brain Drosophila network statistics; rich club, motifs, integrators/broadcasters, neuropil structure, and bottleneck-crossing rich-club neurons.
- Hierarchical Modular Structure of the Drosophila Connectome: hierarchical communities and recovered layered pathways.
- Hulse et al., eLife (2021/2022): central-complex motifs and pathways associated with context-dependent action selection.
- Hoeller et al., Cell (2026): shallow, parallel visual pathways and persistent spatial organization.
- Bates et al., Nature (2026): distributed, parallel, embodied brain-and-cord control linked by ascending/descending circuits.
- Li et al., bioRxiv (2026): FlyWire-v783-constrained spontaneous-activity model; useful structure→dynamics evidence, but model-dependent and not yet a structural proof.
