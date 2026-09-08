<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Specialist Result - Hawker Range Systems Job 01 (Motivation Overview)

**Status:** completed (draft checkpoint, CP-G7)
**Confirmation:** approved (Motivation Overview; six stakeholders; frozen spine)
**Model:** Hawker Range Systems Ltd

## Specialists run

1. archi-motivation
2. archi-model-qa (light)
3. archi-layout
4. archi-documentation

Skipped: capability-strategy, business, application, technology-physical, implementation-migration, traceability.

## Views touched

| View | ID | Action |
|------|-----|--------|
| Motivation Overview | `id-02bfe33f26d844a1a34a314a40a400c0` | created; viewpoint `motivation` |

## Candidate disposition

| Candidate | Disposition | Target | Reason |
|-----------|-------------|--------|--------|
| Driver: Promised sortie times do not match what the range can fly | captured | Driver @ Motivation Overview (id-407b7250961f4e029b285f64965e37cd) | |
| Goal: Instructors and the range share one sortie identity from tasking to live GCS | captured | Goal @ Motivation Overview (id-d262b5beaf4a46a9bf3a03a1a7f6a319) | |
| Outcome: Range Manager and Chief Instructor answer on-range-this-morning without SortieBoard | captured | Outcome @ Motivation Overview (id-00c2c5228d494559b21c5c10f8f53359) | |
| Requirement: RangePlan must not swallow AirStack or GroundOS | captured | Requirement @ Motivation Overview (id-ec762c52e806466fa6eded750caa15e0) | |
| Stakeholder: Range Manager | captured | Stakeholder @ Motivation Overview (id-f1cf33210db04f8d80c4d357b35eeede) | |
| Stakeholder: Chief Instructor | captured | Stakeholder @ Motivation Overview (id-bc23506291674caf8f55964f0381568b) | |
| Stakeholder: GCS Owner | captured | Stakeholder @ Motivation Overview (id-37db77111a96462299c6f4f7a06c2079) | |
| Stakeholder: Planning Programme Manager | captured | Stakeholder @ Motivation Overview (id-5eee5b3ec1074f10a684417d23c4242b) | |
| Stakeholder: Sortie Planner | captured | Stakeholder @ Motivation Overview (id-ff2c9308cb134f2e98350b6087097981) | |
| Stakeholder: Integration Lead | captured | Stakeholder @ Motivation Overview (id-7a10b06f1bfa41e5b30885ee93d65d7c) | |
| Application / capability / process / node elements | out-of-scope | | Job 1 motivation-only freeze |
| Air vehicle product / SysML, second site, costing, GroundOS rewrite | out-of-scope | | moorfield-brief hard freeze |

## Reuse registry

| concept_key | element_id | decision | notes |
|-------------|------------|----------|-------|
| stakeholder:range manager | id-f1cf33210db04f8d80c4d357b35eeede | create | seed empty |
| stakeholder:chief instructor | id-bc23506291674caf8f55964f0381568b | create | |
| stakeholder:gcs owner | id-37db77111a96462299c6f4f7a06c2079 | create | |
| stakeholder:planning programme manager | id-5eee5b3ec1074f10a684417d23c4242b | create | |
| stakeholder:sortie planner | id-ff2c9308cb134f2e98350b6087097981 | create | |
| stakeholder:integration lead | id-7a10b06f1bfa41e5b30885ee93d65d7c | create | |
| driver:promised sortie times do not match what the range can fly | id-407b7250961f4e029b285f64965e37cd | create | |
| goal:instructors and the range share one sortie identity from tasking to live gcs | id-d262b5beaf4a46a9bf3a03a1a7f6a319 | create | |
| outcome:range manager and chief instructor answer on-range-this-morning without sortieboard | id-00c2c5228d494559b21c5c10f8f53359 | create | |
| requirement:rangeplan must not swallow airstack or groundos | id-ec762c52e806466fa6eded750caa15e0 | create | |

## Elements and relationships

### View

- Motivation Overview `id-02bfe33f26d844a1a34a314a40a400c0` viewpoint motivation

### Elements (10)

| Action | Name | Type | ID |
|--------|------|------|----|
| created | Range Manager | Stakeholder | id-f1cf33210db04f8d80c4d357b35eeede |
| created | Chief Instructor | Stakeholder | id-bc23506291674caf8f55964f0381568b |
| created | GCS Owner | Stakeholder | id-37db77111a96462299c6f4f7a06c2079 |
| created | Planning Programme Manager | Stakeholder | id-5eee5b3ec1074f10a684417d23c4242b |
| created | Sortie Planner | Stakeholder | id-ff2c9308cb134f2e98350b6087097981 |
| created | Integration Lead | Stakeholder | id-7a10b06f1bfa41e5b30885ee93d65d7c |
| created | Promised sortie times do not match what the range can fly | Driver | id-407b7250961f4e029b285f64965e37cd |
| created | Instructors and the range share one sortie identity from tasking to live GCS | Goal | id-d262b5beaf4a46a9bf3a03a1a7f6a319 |
| created | Range Manager and Chief Instructor answer on-range-this-morning without SortieBoard | Outcome | id-00c2c5228d494559b21c5c10f8f53359 |
| created | RangePlan must not swallow AirStack or GroundOS | Requirement | id-ec762c52e806466fa6eded750caa15e0 |

### Relationships (9)

| Type | Source | Target | ID |
|------|--------|--------|----|
| Association | Range Manager | Driver | id-0ed26afd9dc6430bbb37fc5407953e5b |
| Association | Chief Instructor | Driver | id-bedec9d3a9da4831b4ad9421f0dbcea9 |
| Association | GCS Owner | Driver | id-2662e1593e2042b28fc733813f72615a |
| Association | Planning Programme Manager | Driver | id-cce70ab31ea143a38667063904b0160d |
| Association | Sortie Planner | Driver | id-5ffbf6af779b4c748a837a508c17dbd7 |
| Association | Integration Lead | Driver | id-d88be420fd5e4298a99c06f64033a495 |
| Influence | Driver | Goal | id-399c8f100a054f4dac0ff089cc3f477d |
| Influence | Goal | Outcome | id-815b5d3ce08c42b48927569b39c85469 |
| Realization | Requirement | Goal | id-03ec9a4d2ea240abbf44d77d1622016d |

Relationships documented via update-relationship after create. Stakeholder concern ownership for boundary and identity is carried in element documentation and the view note; extra Stakeholder-Goal/Requirement associations were dropped so offline compliance_validate stays clean (MCP recipe allows broader association; offline allowlist is stricter).

## QA (light)

| Check | Result |
|-------|--------|
| Model name | Hawker Range Systems Ltd |
| View name exact | Motivation Overview |
| Requirement present | yes (`id-ec762c52e806466fa6eded750caa15e0`) |
| ApplicationComponent / BusinessProcess / Node / Capability count | 0 / 0 / 0 / 0 |
| Evidence first line on elements | yes |
| Docs not name restatement | yes |
| compliance_validate (job-01-slice.json) | pass (0 findings) |
| docs_coverage --require-evidence | pass (0 findings) |
| assess-layout | overallRating fair (5 edge crossings; residual association fan-in to driver) |
| Layer | Motivation only |

## Layout

- Four bands per motivation recipe: Stakeholders; Drivers and Assessments; Goals and Outcomes; Requirements and Principles.
- layout-within-group (row) + arrange-groups (column) + auto-layout-and-route (grouped) + auto-route-connections.
- Draft note below content (CP-G5).
- Final assess: overall fair; layout structure good; routing residual fair (association hub on driver).
- PNG export under `docs/runs/moorfield/` (latest `id-02bfe33f26d844a1a34a314a40a400c0_*.png`).

## Documentation

- View rationale on Motivation Overview (RATE-01 sections); rationale_schema pass (`job-01-rationale.md`).
- Completion summary schema pass (`job-01-completion-summary.md`).
- Element and relationship docs: Evidence first line; named systems only in requirement text.

## Completion summary (draft CP-G7)

- Views Touched: Motivation Overview (`id-02bfe33f26d844a1a34a314a40a400c0`)
- Decisions: approved; motivation-only; six stakeholders; boundary requirement; Goal-Influence-Outcome chain
- Open Questions: none on spine
- Confirmation Status: approved
- Specialists Run: motivation, model-qa light, layout, documentation
- Deliberately Deferred: non-motivation layers; layout push fair to excellent
- Improve Next: later jobs reuse these IDs; do not recreate requirement as an application box

## get-model-info (final)

```json
{
  "name": "Hawker Range Systems Ltd",
  "elementCount": 10,
  "relationshipCount": 9,
  "viewCount": 1,
  "elementTypeDistribution": {
    "Stakeholder": 6,
    "Driver": 1,
    "Goal": 1,
    "Outcome": 1,
    "Requirement": 1
  },
  "relationshipTypeDistribution": {
    "AssociationRelationship": 6,
    "InfluenceRelationship": 2,
    "RealizationRelationship": 1
  },
  "layerDistribution": {
    "Motivation": 10
  },
  "approvalMode": false
}
```

## IDs for downstream

See `docs/runs/moorfield/job-01-motivation-ids.json`.
