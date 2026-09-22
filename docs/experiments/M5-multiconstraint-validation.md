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

Every stage is compared with strong controls:

- Erdős-Rényi-style random graph at matched density;
- degree-preserving directed null;
- cost-matched graph;
- hierarchy-only graph;
- spatial-only graph;
- hub-only graph.

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
- long-range edge fraction.

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
- task performance after topology is fixed.

## Human-reference constraints

Human literature is used as a reference layer, not as a target to imitate literally.

The current hypotheses to test are:

- nested hierarchy;
- within-level local connectivity;
- selective hierarchy-spanning connections;
- rich-club integration backbone;
- spatially constrained wiring;
- multiscale topology-to-dynamics coupling;
- separation of anatomical topology from learned/latent dynamics.

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

Record:

- dataset and version;
- exact resource URL/data product;
- preprocessing rules;
- node/edge sampling policy;
- random seed;
- hierarchy parameters;
- spatial length scale;
- long-range fraction;
- rich-club threshold/null model;
- all metric definitions;
- software commit.

Do not report real-data results until the experiment is actually executed.
