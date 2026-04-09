# HydrologicalTwinAlphaSeries

HydrologicalTwinAlphaSeries is the standalone scientific backend supporting CaWaQS-ViZ.

It serves as a proof-of-concept (POC) for the HydrologicalTwin framework and is dedicated to the definition, validation, and consolidation of its core computational structures.

The repository provides the backend layer required to structure hydrological simulation outputs, expose controlled programmatic interfaces, and support post-processing workflows required by the visualization layer. It focuses strictly on the backend domain, including data structuring and transformation, computational services, configuration models, and API exposure for external consumers. It does not include user interface components, QGIS integration logic, or visualization responsibilities.

It is intentionally developed independently from the QGIS application layer, which consumes it as an external dependency.

HydrologicalTwinAlphaSeries constitutes the AlphaSeries of the HydrologicalTwin framework. In this context, Alpha does not denote instability in the conventional software sense, but a phase in which the system is under formal construction. Core assumptions, data structures, and computational behaviors are actively explored and stress-tested.

The term Series designates a coherent progression of such states. Each iteration contributes to the convergence toward a stable and reproducible backend foundation, ensuring that future versions rely on explicitly validated principles rather than implicit design choices.

---

## Status

This repository is part of the AlphaSeries phase.

This phase is dedicated to:

* defining core architectural invariants,
* validating backend behaviors under real use cases,
* stabilizing interfaces with the visualization environment.

No long-term API stability is guaranteed at this stage.

---

## Relationship with CaWaQS-ViZ

CaWaQS-ViZ is the primary consumer of this repository.

The integration follows a clear separation of concerns:

* HydrologicalTwinAlphaSeries → backend computation and data structuring
* CaWaQS-ViZ → visualization, interaction, and GIS integration

The backend is intended to be integrated as an external dependency (e.g. Git submodule), avoiding duplication and ensuring consistency between computation and visualization layers.

---

## Repository Structure

* `src/HydrologicalTwinAlphaSeries/domain`
  Core domain entities (e.g. compartments, meshes, observations)

* `src/HydrologicalTwinAlphaSeries/services`
  Computational services and transformation operators

* `src/HydrologicalTwinAlphaSeries/ht`
  Backend facade and exposed API types

* `src/HydrologicalTwinAlphaSeries/config`
  Configuration models and constants

* `src/HydrologicalTwinAlphaSeries/tools`
  Shared utilities

* `tests`
  Backend validation and integration checks

* `docs`
  Technical notes and backend-oriented documentation
  (see [canonical_monolith.md](docs/canonical_monolith.md) for the target architecture,
  [domain_model.md](docs/domain_model.md) for the compartment-centric domain model)

---

## Development Principles

* strict separation between computation and visualization layers,
* reproducible backend behavior,
* explicit configuration-driven workflows,
* minimal coupling with external applications.

---

## Integration Workflow

When used within CaWaQS-ViZ:

* this repository is mounted as an external dependency,
* development can occur independently on both sides,
* synchronization is handled through version control (submodule or equivalent mechanism).

---

## Authorship

* Project Manager: Nicolas Flipo
* Main Developer: Simone Mazzarelli
* Proto implementation (CaWaQS-ViZ backend): Lise-Marie Girod

Contributors (ongoing):
Tristan Bourgeois, Nicolas Gallois, Fulvia Baratelli, Pierre Guillou, Fabien Ors, Mariam Taki

---

## Positioning

HydrologicalTwinAlphaSeries is not a generic Python package.

It is the computational foundation of a hydrological twin system, currently under active definition and validation.

---