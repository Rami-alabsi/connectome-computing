# M6-COSMIC: Field vs Explicit Relational Communication

## Scope

M6-COSMIC tests a narrow engineering hypothesis derived from the cross-domain synthesis:
a compact global relational field may carry aggregate information efficiently, while
explicit sparse relations remain necessary for pair-sensitive information.

This is a synthetic computational experiment. It is **not** a model of gravity,
quantum fields, spacetime, or the physical cosmic web.

## Matched conditions

The first benchmark contains three conditions:

1. **Field** — one compact global field payload.
2. **Sparse** — explicit endpoint effective states for selected module pairs.
3. **Hybrid** — global field plus selected explicit pair relations.

The benchmark records transmitted values/bytes and evaluates two task classes:

- **Global aggregate task:** recover the mean effective state across modules.
- **Pair-sensitive task:** recover the effective state of one selected module pair.

The fixture intentionally makes the selected pair different from the global mean, so
a field that discards module identity cannot pass the pair-sensitive test by accident.

## Interpretation rule

No architecture is declared superior from this benchmark alone.

The intended falsifiable result is a **tradeoff curve**:

- field communication should be compact for aggregate information;
- explicit pair communication should retain pair identity;
- hybrid communication should be evaluated for whether a small explicit backbone can
  recover pair-sensitive information without losing the communication advantage of
  the compact field.

## Next benchmark gates

Before any novelty claim:

- scale modules and hierarchy size;
- sweep field dimension;
- sweep explicit active-pair budget;
- add random/degree-matched relation controls;
- add noise/perturbation tests;
- separate global, local, and pair-sensitive tasks;
- report communication bytes, useful information/error, active relations and compute proxy;
- repeat across random seeds;
- compare against non-biological compression/routing baselines;
- re-run targeted prior-art search.

## Current status

The first implementation and unit tests are committed. Scientific benchmark results are
not yet claimed. CI must be green on the latest commit before the implementation is
treated as stable.
