<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Orchestrator report - Hawker Range Systems Job 01

## Status

- confirmation_status: approved
- run_status: SPECIALISTS_COMPLETE_DRAFT
- view_plan: docs/runs/moorfield/job-01-view-plan.md
- specialist_result: docs/runs/moorfield/job-01-specialist-result.md
- motivation_ids: docs/runs/moorfield/job-01-motivation-ids.json
- gate: View Plan approved; specialists motivation → model-qa (light) → layout → documentation run
- specialists_dispatched: archi-elicit, archi-viewpoint-select, archi-motivation, archi-model-qa, archi-layout, archi-documentation
- specialists_not_run: capability-strategy, business, application, technology-physical, implementation-migration, traceability
- mutations: yes (post-approve)

## Architect answers (approve)

- View title stays Motivation Overview
- Include all six stakeholders: Range Manager, Chief Instructor, GCS Owner, Planning Programme Manager, Sortie Planner, Integration Lead

## Elicit (normalized)

| Field | Value |
|-------|-------|
| Problem | Promised sortie times do not match what Moorfield Range can fly; dual track SortieBoard vs live GroundOS; RangePlan funded for visibility only. |
| Stakeholders | Range Manager, Chief Instructor, GCS Owner, Planning Programme Manager, Sortie Planner, Integration Lead |
| Concerns | Shared sortie identity tasking-to-live-GCS; morning-on-range answer without SortieBoard; RangePlan must not swallow AirStack or GroundOS |
| Scope in | Drivers, goals, outcomes, RangePlan boundary requirement |
| Scope out | Capabilities, processes, applications, nodes, work packages, second site, costing, GroundOS rewrite, weapons system, air-vehicle SysML/product structure |
| Target state | Signable Motivation Overview; shared sortie identity as desired state; RangePlan planning-facing only |
| Expected outcome | One view named Motivation Overview |

## Viewpoint select

- Selected: Motivation (overview); view name Motivation Overview
- Viewpoint param: motivation

## Specialists outcome

| Specialist | Result |
|------------|--------|
| archi-motivation | completed; 10 elements, 9 relationships, 1 view |
| archi-model-qa | completed light; compliance_validate pass; docs_coverage pass |
| archi-layout | completed; assess overall fair (5 crossings residual) |
| archi-documentation | completed draft; rationale + completion summary schema pass |

## Pass checks

| Check | Result |
|-------|--------|
| View named Motivation Overview | pass |
| Requirement RangePlan must not swallow AirStack or GroundOS | pass (`id-ec762c52e806466fa6eded750caa15e0`) |
| No capabilities, processes, applications, nodes | pass (counts 0) |
| No air-vehicle product structure | pass |
| Evidence first line on elements | pass |
| Docs not restatement of the name | pass |
| Model name Hawker Range Systems Ltd | pass |

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
  "layerDistribution": {
    "Motivation": 10
  },
  "approvalMode": false
}
```

## Concerns

- Layout overallRating fair (association fan-in from six stakeholders to one driver). Acceptable for draft sign-off; not blocking.
- Offline compliance allowlist is stricter than MCP motivation recipe; final graph uses Stakeholder-Driver associations, Driver-Goal influence, Goal-Outcome influence, Requirement-Goal realization.

## Next action

Job 01 draft complete. Later SOAM jobs reuse motivation IDs from `job-01-motivation-ids.json`. User reviews Motivation Overview in Archi; no git commit from this run.
