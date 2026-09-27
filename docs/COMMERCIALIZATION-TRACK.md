# Commercialization Track

Updated: 2026-09-27

This document separates scientific validation from commercial opportunity. It is
not a business forecast and does not claim that the project is currently
commercially validated.

## 1. Core principle

The project should not be monetized by selling the biological connectome itself.

The potentially valuable asset is the original layer built on top of biological
evidence:

- algorithms;
- computational abstractions;
- scalable generators;
- runtimes/compilers;
- benchmark suites;
- optimization methods;
- reproducible tooling;
- proprietary extensions or customer-specific implementations.

## 2. What would create commercial value?

The strongest technical signal would be a reproducible result such as:

- equal task quality at lower memory/communication cost;
- equal quality at lower latency;
- useful performance under sparse/event-driven execution;
- better robustness per unit resource;
- a scaling behavior that remains favorable as the workload grows;
- a software tool that reduces the cost of exploring or deploying sparse
  relational architectures.

A biological resemblance by itself is not a customer value proposition.

## 3. Possible business forms

These are possible structures, not predictions:

### A. Research/engineering platform
A software platform for generating, testing and benchmarking connectome-derived
architectures.

Potential customers: AI research teams, neuromorphic groups, universities,
advanced R&D organizations.

### B. SDK/runtime/compiler
If the project produces a useful sparse relational execution model, the
implementation could become an SDK, runtime or compiler layer.

### C. Enterprise optimization/IP licensing
A validated algorithm could be licensed to companies if it provides measurable
resource or performance advantages on their workloads.

### D. Specialized accelerator / hardware co-design
Only consider this after a software architecture demonstrates a repeatable
advantage and the memory/communication model is sufficiently understood.

### E. Research services
Earlier-stage revenue could come from specialized architecture experiments,
connectome analysis, or benchmarking while the deeper IP is still being
validated.

## 4. What would make the project investable/sellable?

A buyer or investor would need something more concrete than a compelling
scientific story. The strongest evidence would be:

1. a clearly specified method;
2. reproducible benchmarks;
3. strong conventional baselines;
4. ablations identifying the source of the gain;
5. scaling evidence;
6. a defined customer workload;
7. ownership/licensing clarity;
8. an implementation that others cannot trivially reproduce from the paper alone;
9. a credible path to deployment.

## 5. Current commercial maturity

Current status:

- Scientific foundation: active.
- CFG biological control: closed for the defined v783 path.
- NPC biological control: active.
- Spatial control: not started.
- Computational advantage: not demonstrated.
- Product-market fit: not tested.
- Patentability: not assessed.
- Commercial IP/data clearance: not completed.

Therefore the project is currently a **research asset**, not a validated
commercial product.

## 6. IP and data boundary

FlyWire states that its public release data are made available under
CC BY-NC 4.0. Therefore the project must not assume that a commercial product
may redistribute FlyWire-derived datasets or package them as commercial data.

The repository should maintain a strict boundary between:

- third-party biological data;
- our original source code;
- our original algorithms;
- derived measurements/results;
- future proprietary datasets;
- future customer data.

Before commercial distribution, obtain appropriate legal/IP review of the
specific data, licenses, dependencies and ownership structure.

## 7. Commercialization gate

Do not pivot the scientific project into product development merely because a
biological pattern looks interesting.

The commercialization gate should open only after:

**validated structural constraint**
-> **computational primitive**
-> **measured workload benefit**
-> **matched-resource benchmark**
-> **ablation**
-> **scaling**
-> **IP/data clearance**

At that point, choose the business form that matches the measured value.

## 8. Strategic conclusion

The project can plausibly become a source of commercial value, but that value
must come from a validated computational method or product layer, not from the
claim that it is inspired by a fly connectome.

The current work is therefore still the correct foundation for a future
commercial path: prove the mechanism first, then package the proven mechanism.
