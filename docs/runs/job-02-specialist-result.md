<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Specialist Result - Hatherley Plate Job 02 (Capability Map)

**Status:** completed (draft checkpoint, CP-G7)  
**Confirmation:** approved  
**Model:** Hatherley Plate Ltd

## Specialists run

1. archi-capability-strategy
2. archi-model-qa (light)
3. archi-layout
4. archi-documentation

Skipped: motivation (reuse job-01), business, application, technology-physical, implementation-migration, traceability.

## Views touched

| View | ID | Action |
|------|-----|--------|
| Capability Map | `id-6613e98758a3455d95e1fcc5b8e731f7` | created; viewpoint `capability_map` |
| Motivation Overview | `id-05f18c92556242fc8ce2a2252fc36867` | left intact; not modified |

## Elements and relationships

| Action | Name | Type | ID |
|--------|------|------|----|
| created | Promise | Capability | `id-9c2c1a6a78f0475681b48889b2664099` |
| created | Order | Capability | `id-f6c7c6a74874412ba24c60d318292ad2` |
| created | Mill schedule | Capability | `id-ed34ec1744a1458b9f7e1579932f2af6` |
| created | Collect | Capability | `id-50f22633aea34b3b8536e05a14fda533` |

Relationships created for Cap-Cap chain: none kept. Offline `compliance_validate` rejects Capability-Flow-Capability and Capability-Association-Capability. Overview map uses left-to-right spatial order only (Promise, Order, Mill schedule, Collect). Job-01 motivation relationships unchanged (15).

## Candidate disposition

| Candidate | Disposition | Target |
|-----------|-------------|--------|
| Promise | captured | Capability @ Capability Map |
| Order | captured | Capability @ Capability Map |
| Mill schedule | captured | Capability @ Capability Map |
| Collect | captured | Capability @ Capability Map |
| Integration Lead on this view | out-of-scope | IDs remain from job-01; omitted per approve |
| Job-01 driver/goal/outcome/requirement/stakeholders | folded | reuse registry; not recreated |
| Applications (MillOS, OrderSight, …) | out-of-scope | ownership text only |
| Processes / nodes / work packages | out-of-scope | later jobs |

## QA (light)

| Check | Result |
|-------|--------|
| Model name | Hatherley Plate Ltd |
| View name exact | Capability Map |
| Job-01 driver duplicated | no (1 Driver: Promised plate dates do not match mill reality) |
| ApplicationComponent count | 0 |
| BusinessProcess count | 0 |
| Node count | 0 |
| Capability count | 4 |
| Evidence first line on new elements | yes |
| Docs not name restatement | yes |
| compliance_validate (job-02-slice.json) | pass (0 findings) |
| docs_coverage --require-evidence | pass (0 findings) |
| assess-layout | overallRating excellent (all dimensions pass) |
| Motivation Overview intact | yes (10 elements) |

## Layout

- LTR single row: Promise → Order → Mill schedule → Collect
- Ownership note below content (docs only: MillOS owns Mill schedule; OrderSight sales-facing)
- export-view PNG: `docs/runs/job-02-capability-map.png`

## Documentation

- View rationale written on Capability Map (Purpose through Open Questions); rationale_schema pass
- Completion summary: `docs/runs/job-02-completion-summary.md`; schema pass
- Element docs: Evidence first line; MillOS / OrderSight ownership in capability text only

## get-model-info (final)

```json
{
  "name": "Hatherley Plate Ltd",
  "elementCount": 14,
  "relationshipCount": 15,
  "viewCount": 2,
  "elementTypeDistribution": {
    "Capability": 4,
    "Stakeholder": 6,
    "Driver": 1,
    "Goal": 1,
    "Outcome": 1,
    "Requirement": 1
  },
  "layerDistribution": {
    "Strategy": 4,
    "Motivation": 10
  }
}
```

## Compliance notes

- Cap-Cap Flow and Association were created then removed after offline validator findings. Spatial chain only on the map. Later jobs can attach processes/apps with legal realization/serving edges.
- `update-model` documentation field not supported on this bridge (name/purpose/properties only); run status lives in artifacts.

## Open questions

- None for overview grain.

## IDs artifact

`docs/runs/job-02-capability-ids.json`

## Confirmation assumption

Work ran under approved View Plan job-02 with architect answers: title Capability Map; four top-level capabilities Promise, Order, Mill schedule, Collect; Integration Lead omitted from view.
