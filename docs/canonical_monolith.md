# Canonical Monolithic Architecture for HTAS

## Core Invariant

> HTAS exposes a single canonical object (`HydrologicalTwin`) as its public interface;
> all internal complexity is strictly encapsulated behind this façade.

---

## Public Entry Point

`HydrologicalTwin` is the **single public entry point** for all backend operations.

```python
from HydrologicalTwinAlphaSeries import HydrologicalTwin
```

No other import is required for normal usage.

---

## Internal Layers (not part of the public API)

| Layer        | Purpose                                     |
|------------- |---------------------------------------------|
| `domain/`    | State & entities (no orchestration)         |
| `services/`  | Operations (no global state)                |
| `config/`    | Configuration models and constants          |
| `tools/`     | Generic utilities only                      |
| `ht/`        | Façade + public result types                |

---

## Public API — Macro-Methods (≤ 8)

The facade exposes only high-level macro-capabilities:

| Method        | Purpose                                          |
|-------------- |--------------------------------------------------|
| `configure`   | Set project and geometry configuration           |
| `load`        | Register compartments and mesh data              |
| `describe`    | Inspect twin metadata and compartment info       |
| `extract`     | Extract simulation or observation data           |
| `transform`   | Apply temporal/spatial aggregation               |
| `render`      | Produce visualizations (PDF, interactive plots)  |
| `export`      | Export data to files (CSV, pickle, GeoDataFrame) |

These methods **delegate** to `services/` and `domain/` — they contain no heavy logic.

---

## Internal State Model

`HydrologicalTwin` enforces an explicit lifecycle via an internal state machine:

```
EMPTY → CONFIGURED → LOADED → READY
```

- **EMPTY**: Instance created, no configuration.
- **CONFIGURED**: Configuration attached, no data loaded.
- **LOADED**: Compartments registered, data accessible.
- **READY**: Alias for LOADED — all operations available.

Invalid call sequences raise `InvalidStateError`.

---

## Rules

- **domain/** holds state, no orchestration.
- **services/** holds operations, no global state.
- **tools/** holds generic utilities with no domain meaning.
- **ht/** holds the façade, public result types, and persistence.
- Public API returns **structured result types** (not raw dicts or internal objects).
- No direct numerical logic inside the façade.
- No direct file I/O inside the façade (delegated to services).

---

## Transport / API Layer

No web framework dependency exists in core. HTTP/REST/FastAPI/Django concerns are
explicitly deferred. The Python-level canonical API is the only contract at this stage.

See also: `docs/api_capabilities.md` for the list of façade methods and their intent.
