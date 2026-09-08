<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Orchestrator report - Hawker Range Systems Job 02

## Status

- confirmation_status: approved
- run_status: SPECIALISTS_COMPLETE (draft checkpoint CP-G7)
- view_plan: docs/runs/moorfield/job-02-view-plan.md
- specialist_result: docs/runs/moorfield/job-02-specialist-result.md
- capability_ids: docs/runs/moorfield/job-02-capability-ids.json
- specialists_run: archi-capability-strategy, archi-model-qa (light), archi-layout, archi-documentation
- specialists_not_run: motivation (job 1 done), business, application, technology-physical, implementation-migration, traceability
- mutations: Capability Map view + 4 Capability elements + ownership note; Motivation Overview untouched

## Architect answers applied

- View title stays Capability Map
- Four top-level capabilities: Task, Clear, Fly, Recover
- GroundOS owns live-sortie (Fly) in documentation TEXT only; AirStack airborne; RangePlan planning-facing; no applications created

## Model guard (post-run)

```json
{
  "name": "Hawker Range Systems Ltd",
  "elementCount": 14,
  "relationshipCount": 9,
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

- Views: Motivation Overview (`id-02bfe33f26d844a1a34a314a40a400c0`); Capability Map (`id-6967b8a5125d46e1b6ba0edbf9b9539b`)
- Guard: name remains Hawker Range Systems Ltd

## Pass checks

| Check | Result |
|-------|--------|
| View named Capability Map | pass |
| Job 1 motivation reused; no second driver set | pass (driver count 1) |
| Capabilities Task / Clear / Fly / Recover | pass |
| GroundOS / AirStack / RangePlan ownership in text | pass (element docs + note) |
| No apps / processes / nodes | pass (0/0/0) |
| Evidence first line; docs not name restatement | pass |
| assess-layout | excellent |
| compliance_validate / docs_coverage (cap slice) | pass / pass |

## Snapshot

- PNG: `docs/runs/moorfield/id-6967b8a5125d46e1b6ba0edbf9b9539b_1788816739132.png`
- Spatial spine only (no Cap-Cap relationships; Hatherley lesson)

## Next action

Stop at draft checkpoint. Later SOAM jobs attach operations/application/technology to these capability IDs. No git commit requested.
