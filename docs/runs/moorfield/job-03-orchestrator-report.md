<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Orchestrator report - Hawker Range Systems Job 03

## Status

- confirmation_status: approved
- run_status: SPECIALISTS_COMPLETE (draft checkpoint)
- view_plan: docs/runs/moorfield/job-03-view-plan.md
- specialists_run: archi-elicit, archi-viewpoint-select, archi-business, archi-model-qa (light), archi-layout, archi-documentation
- mutations: yes (post-approve)
- specialist_result: docs/runs/moorfield/job-03-specialist-result.md

## Intent (elicited)

- Problem: cannot show tasked sortie → live GCS path; SortieBoard still the pain
- Stakeholders: Range Manager, Chief Instructor, Sortie Planner, GCS Owner (+ Planning Programme Manager, Integration Lead off-canvas)
- Concerns: as-is range floor only; roles + processes; no apps/nodes; no airframe
- Scope in: task, clear, fly, recover + named roles
- Scope out: new apps, nodes, work packages, second site, costing, GroundOS rewrite, air-vehicle SysML
- Target: view **Range Operations**; roles and processes only
- Outcome: Range Operations delivered; facts `docs/moorfield-brief.md`

## Viewpoint selection

- Selected: Business Process Cooperation (overview); deliverable view name **Range Operations**
- View id: `id-782395c6d18347a9a24da626f81ee275`

## Architect answers applied

- View title stays Range Operations
- BusinessProcess Task, Clear, Fly, Recover (new IDs)
- On canvas: Range Manager, Chief Instructor, Sortie Planner, GCS Owner as BusinessRole
- Off canvas: Planning Programme Manager, Integration Lead (job-1 stakeholder IDs)
- Job-2 capabilities not placed on this view
- SortieBoard pain in documentation/note only
- No Motivation Stakeholder duplication for Range Manager

## Delivered structure

| Kind | Count / IDs |
|------|-------------|
| BusinessProcess | Task id-8b426a10197b48b4b0864f0b4445ec3e; Clear id-c0d2f85265bb4414b03c5a7e69934983; Fly id-b866710ad3b448d3829e71df6397738f; Recover id-43ccf54a35034dfe8b7846c141d8f6b5 |
| BusinessRole created | Range Manager, Chief Instructor, Sortie Planner, GCS Owner |
| Stakeholders reused | 6 (job-01) |
| Capabilities registry | 4 (job-02, not on view) |
| Apps / nodes | 0 / 0 |
| Layout | assess-layout overallRating excellent |
| Snapshot | job-03-range-operations.png |

## Model guard (final)

```json
{
  "name": "Hawker Range Systems Ltd",
  "elementCount": 22,
  "relationshipCount": 16,
  "viewCount": 3,
  "elementTypeDistribution": {
    "Capability": 4,
    "BusinessProcess": 4,
    "BusinessRole": 4,
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

## QA

- compliance_validate: ok
- docs_coverage --require-evidence: ok
- naming conflicts: 0
- aspect-hints: 4 low (plain process labels; accepted)
- Motivation Overview + Capability Map unchanged

## Open questions

- none blocking

## Next action

Draft checkpoint complete. User may review snapshot and approve as final or request NL changes. Later SOAM jobs: application / technology.
