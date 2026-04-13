# HydrologicalTwin API Capabilities

`HydrologicalTwin` exposes a macro-only public contract for external consumers.

For `cawaqsviz`, the target surface is limited to:

- `configure`
- `load`
- `describe`
- `extract`
- `transform`
- `render`
- `export`

Everything else is either an internal implementation detail or a transitional
compatibility wrapper. External code must not orchestrate `domain/`, `services/`,
`config/`, `tools/`, nor call detailed facade helpers as its primary integration path.

All operations act on compartment aggregates and structured public request or response
types. External consumers must not construct or manipulate low-level backend objects
such as `Compartment`, `Mesh`, `Observation`, or `Extraction` directly.

---

## Lifecycle

| Method | Required State | Next State | Description |
|---|---|---|---|
| `configure` | EMPTY | CONFIGURED | Attach project and geometry configuration |
| `load` | CONFIGURED | LOADED | Build and register project compartments |
| `describe` | LOADED | (unchanged) | Return the frontend catalog and twin metadata |
| `extract` | LOADED | (unchanged) | Extract workflow payloads through typed requests |
| `transform` | LOADED | (unchanged) | Compute aggregations, criteria, budgets, regimes, runoff ratio, and AQ balances |
| `render` | LOADED | (unchanged) | Produce final artefacts such as reports, plots, and AQ balance diagrams |
| `export` | LOADED | (unchanged) | Export twin snapshots or derived outputs |

---

## Macro Intents

### `configure(request)`
Attach project-level and geometry configuration.

### `load(request)`
Accept a public project-load request and build compartments internally.

### `describe(request)`
Return the frontend catalog: compartments, layers, observations, units, supported
workflow kinds, and available outputs.

### `extract(request)`
Return workflow payloads through stable kinds. Current kinds include:

- `simulation_matrix`
- `observations`
- `sim_obs_bundle`
- `spatial_map`
- `catchment_cells`
- `aquifer_outcropping`
- `aq_balance_inputs`

### `transform(request)`
Perform workflow computations. Current kinds include:

- `temporal_aggregation`
- `spatial_average`
- `criteria`
- `budget`
- `hydrological_regime`
- `runoff_ratio`
- `aq_balance`

### `render(request)`
Produce final artefacts. Current kinds include:

- `budget_barplot`
- `hydrological_regime`
- `sim_obs_pdf`
- `sim_obs_interactive`
- `aq_flux_diagram`

### `export(request)`
Export data or snapshots. `pickle` remains the canonical persisted export format.

---

## Transitional Compatibility Layer

Some detailed methods still exist on the facade for migration compatibility.
Examples include `register_compartment`, `build_watbal_spatial_gdf`,
`build_effective_rainfall_gdf`, `build_aq_spatial_gdf`,
`build_aquifer_outcropping`, `render_sim_obs_pdf`, and
`render_sim_obs_interactive`.

These methods are not the architectural target. They are wrappers retained to
bridge legacy callers until all frontend workflows consume only the macro methods
listed above.

---

## Transport Layer

No HTTP schema or web framework integration is defined at this stage.
The Python-level macro facade is the only canonical contract.
