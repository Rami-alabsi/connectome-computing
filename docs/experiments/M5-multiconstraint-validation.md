# M5 Multi-Constraint Validation Protocol

## Objective

Determine whether a synthetic connectome can reproduce selected biological constraints
without hiding which constraint caused each improvement.

## Constraint ladder

Run the same observed-data split and target edge budget through:

1. density only;
2. density + degree distribution;
3. + reciprocity;
4. + hierarchy/modularity;
5. + spatial distance law;
6. + explicit long-range budget;
7. + rich-club/backbone;
8. full multi-constraint model.

Additional mechanistic branch for M6 preparation:

9. + typed cooperation/competition;
10. + dynamic/state-dependent hierarchy.

Every stage is compared with strong controls:

- random graph at matched density;
- degree-preserving directed null;
- cost-matched graph;
- hierarchy-only graph;
- spatial-only graph;
- hub-only graph;
- cooperation-only vs cooperation+competition;
- flat hierarchy vs state-dependent hierarchy.

## Metrics

### Structure
- node count;
- directed edge count and density;
- in/out degree quantiles and coefficient of variation;
- reciprocity;
- modularity and participation;
- rich-club density across multiple thresholds;
- motif/graphlet statistics;
- edge-length distribution;
- long-range edge fraction;
- within-level vs hierarchy-crossing edge fractions.

### Cost/resource proxies
- total wiring length;
- mean edge length;
- maximum and mean fan-in/fan-out;
- messages per simulated step;
- state memory per node;
- communication bytes/event when a simulator exists.

### Dynamics (M6+)
- activity autocorrelation;
- propagation latency;
- state-transition/control energy;
- multiscale mode reconstruction;
- effective hierarchy by state;
- cooperative vs competitive interaction effects;
- task performance after topology is fixed.

## Human-reference constraints

Human literature is used as a reference layer, not as a target to imitate literally.

Current hypotheses:

- nested hierarchy;
- within-level local connectivity;
- selective hierarchy-spanning connections;
- rich-club integration backbone;
- spatially constrained wiring;
- multiscale topology-to-dynamics coupling;
- state-dependent effective hierarchy;
- distributed spatial influence/control.

## Fly embodied-control constraint

The 2026 unified fly brain-and-nerve-cord connectome motivates a separate hypothesis:
local sensory-to-effector feedback loops can remain relatively autonomous while
long-range ascending/descending pathways coordinate behavior modules.

This should be compared against a centralized-control baseline rather than assumed superior.

## Cooperation/competition constraint

A 2026 cross-species mammalian study reports that faithful whole-brain dynamics
combine modular cooperative interactions with diffuse long-range competitive interactions.
This motivates a typed interaction branch:

- local/modular cooperation;
- diffuse long-range competition.

The engineering hypothesis is not that inhibition/competition is universally beneficial.
It is that mixed interaction signs may provide a different stability/expressivity/resource
trade-off than cooperation-only networks.

## Novelty gate

No novelty claim is permitted from matching these properties individually.
A novelty candidate requires:

1. exact method specification;
2. targeted prior-art search for the combined method;
3. reproducible controls;
4. ablation evidence;
5. statistically appropriate uncertainty reporting;
6. independent or held-out validation;
7. an engineering result that cannot be explained by parameter count,
   density, degree sequence or another generic advantage.

## Reproducibility

Record dataset/version, resource URL, preprocessing, node/edge sampling, random seed,
all generator parameters, null-model definition, metric definitions, software commit,
and environment information.

Do not report real-data results until the experiment is actually executed.
