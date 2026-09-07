<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Specialist Result - Hatherley Plate Job 03 (Production Operations)

**Status:** completed (draft checkpoint, CP-G7)
**Confirmation:** approved
**Model:** Hatherley Plate Ltd

## Specialists run

1. archi-business
2. archi-model-qa (light)
3. archi-layout
4. archi-documentation

Skipped by scope: motivation, capability-strategy, application, technology-physical, implementation-migration, traceability.

## Views touched

| View | ID | Action |
|------|-----|--------|
| Production Operations | `id-c189cce2288642d8b1cf3c267270d571` | created; viewpoint `business_process` |
| Motivation Overview | `id-05f18c92556242fc8ce2a2252fc36867` | left intact |
| Capability Map | `id-6613e98758a3455d95e1fcc5b8e731f7` | left intact |

## Elements and relationships

| Action | Name | Type | ID |
|--------|------|------|----|
| created | Plant Manager | BusinessRole | `id-c2d53b4de0d44d7c92f5e4ea51332ccf` |
| created | Head of Sales | BusinessRole | `id-a10b3ee5bc3c49088e973710f1b8397e` |
| created | Operations Planner | BusinessRole | `id-7a3f4a278904406cbb3c52f2fa45825a` |
| created | MES Owner | BusinessRole | `id-8c313bffb8d3411c8fe9dec39a89624b` |
| created | Promise | BusinessProcess | `id-c338aa0260a345ed9be332a6b9e26be9` |
| created | Works order | BusinessProcess | `id-69e033ce9ca242d499799db7a6b42272` |
| created | Mill schedule | BusinessProcess | `id-d6a875984a84411d958d73759e2ffe1a` |
| created | Plate rolling | BusinessProcess | `id-ed0201833e864e08ab2950d70d2994aa` |
| reused | Plant Manager (Motivation) | Stakeholder | `id-0260a5aa995b41c7b84d93d3541592c0` |
| reused | Head of Sales (Motivation) | Stakeholder | `id-988afa0e45894cd3a657ac9c7085ed98` |
| reused | Operations Planner (Motivation) | Stakeholder | `id-ee9aa7f5d13c4ec9ba9da957d3768ed2` |
| reused | MES Owner (Motivation) | Stakeholder | `id-db0cfaa61b4048e7900b2b9bad3eea97` |
| reused off-canvas | CRM Programme Manager | Stakeholder | `id-92664a6b007b411d979d63c25480a38c` |
| reused off-canvas | Integration Lead | Stakeholder | `id-9fc4203ce6ac494fbe546220c92f44b9` |
| reused off-canvas | Promise / Order / Mill schedule / Collect | Capability | job-02 IDs; not placed |

### Relationships created

| Type | Source | Target | ID |
|------|--------|--------|-----|
| AssignmentRelationship | Head of Sales | Promise | `id-cca33037e4cf47c5846fa7f9138f3d3c` |
| AssignmentRelationship | Operations Planner | Works order | `id-e1043c22e2244bf29190224c526bb58e` |
| AssignmentRelationship | Operations Planner | Mill schedule | `id-b098390798814b57963e3fe28cc45745` |
| AssignmentRelationship | MES Owner | Plate rolling | `id-a6699eacb79b45cf8795e341ec2d9457` |
| AssignmentRelationship | Plant Manager | Plate rolling | `id-7d3ffe8b4b2c43b49332c15fa5b219da` |
| TriggeringRelationship | Promise | Works order | `id-848ce647fbce4d989656c31499819b00` |
| TriggeringRelationship | Works order | Mill schedule | `id-2474f5e6c0634451b110c48817d3a26d` |
| TriggeringRelationship | Mill schedule | Plate rolling | `id-8adabf3975ca4e0b80de6e744704b9d0` |

## Candidate disposition

| Candidate | Disposition | Target | Reason |
|-----------|-------------|--------|--------|
| Promise process | captured | BusinessProcess @ Production Operations | |
| Works order process | captured | BusinessProcess @ Production Operations | |
| Mill schedule process | captured | BusinessProcess @ Production Operations | |
| Plate rolling process | captured | BusinessProcess @ Production Operations | |
| Plant Manager role | captured | BusinessRole @ Production Operations | |
| Head of Sales role | captured | BusinessRole @ Production Operations | |
| Operations Planner role | captured | BusinessRole @ Production Operations | |
| MES Owner role | captured | BusinessRole @ Production Operations | |
| CRM Programme Manager | folded | Stakeholder job-01 ID | off-canvas; reuse only |
| Integration Lead | folded | Stakeholder job-01 ID | off-canvas; reuse only |
| Job-02 capabilities | out-of-scope | | omit from canvas per approved plan |
| PromiseSheet and named systems | out-of-scope | | wording and pain note only; no application elements |
| Applications nodes work packages | out-of-scope | | hard freeze this job |

## Model QA (light)

- View name exact: Production Operations
- Processes present: Promise, Works order, Mill schedule, Plate rolling
- Application count: 0; node count: 0
- PromiseSheet element count: 0 (pain note only)
- Stakeholder count remains 6 (no duplicate Motivation Stakeholders)
- BusinessRole 4 created (required for assignment; not Motivation duplicates)
- Layout assess-layout: overallRating **excellent** (all ratingBreakdown dimensions pass)
- Prior views intact (viewCount 3)

## Layout

- Roles top row; process chain left to right; PromiseSheet note below-content
- Tools: add-to-view placements, apply-positions, auto-route-connections, assess-layout, export-view
- PNG: `docs/runs/job-03-production-operations.png`

## Documentation

- View rationale written to view documentation and `docs/runs/job-03-rationale.md`
- Completion summary: `docs/runs/job-03-completion-summary.md`
- IDs: `docs/runs/job-03-operations-ids.json`
- First generation is draft (CP-G7)

## Compliance notes

- none blocking
- Business Role shares display names with Motivation Stakeholders by design (different types; required for business-layer assignment). Not a second Stakeholder create.
- Capability names Promise and Mill schedule coexist with BusinessProcess of the same labels (different types; job-02 off-canvas).

## Open questions

- none blocking

## get-model-info snapshot (after)

```json
{
  "name": "Hatherley Plate Ltd",
  "elementCount": 22,
  "relationshipCount": 23,
  "viewCount": 3,
  "elementTypeDistribution": {
    "Capability": 4,
    "BusinessRole": 4,
    "BusinessProcess": 4,
    "Stakeholder": 6,
    "Driver": 1,
    "Goal": 1,
    "Outcome": 1,
    "Requirement": 1
  },
  "layerDistribution": {
    "Strategy": 4,
    "Business": 8,
    "Motivation": 10
  }
}
```

## Confirmation assumption

Work ran under approved View Plan Job 03. Scope stayed business roles and processes only.
