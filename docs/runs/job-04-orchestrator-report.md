<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Orchestrator report - Hatherley Plate Job 04

## Status

- confirmation_status: **approved**
- run_status: **SPECIALISTS_COMPLETE** (draft checkpoint, CP-G7)
- view_plan: docs/runs/job-04-view-plan.md
- viewpoint_trace: docs/runs/job-04-viewpoint-trace.md
- normalized_intent: docs/runs/job-04-normalized-intent.md
- specialist_result: docs/runs/job-04-specialist-result.md
- application_ids: docs/runs/job-04-application-ids.json
- mutations: **applied** under approved View Plan

## Architect answers locked

- View title: Application Support
- Canvas: five apps plus reused job-03 processes with Serving links
- PromiseSheet: ApplicationComponent (as-is spreadsheet pain)
- Job-02 capabilities: omitted from this canvas
- PlantGate equipment constraint: documentation only; no nodes/equipment

## Specialists run

1. archi-application
2. archi-model-qa (light)
3. archi-layout
4. archi-documentation

Skipped by scope: motivation, capability-strategy, business (reuse), technology-physical, implementation-migration, traceability.

## Deliverable

- View **Application Support** `id-90bb9ec6131b44f9966ac494bd89a90c` (viewpoint `application_usage`)
- Five ApplicationComponents: MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate (OrderSight != MillOS)
- Eight Serving links from apps to reused job-03 processes; job-03 Triggering chain reused on canvas
- Prior three views left intact
- Layout assess: **good**
- Offline compliance_validate on view slice: ok
- get-model-info: elementCount 27, relationshipCount 31, viewCount 4, Application 5, nodes 0

## Guard

- get-model-info name: **Hatherley Plate Ltd** (pass throughout)
- No MUTATION_FAILED stop condition hit on required creates

## Concerns (non-blocking)

- Temporary ApplicationComponent Flow edges were removed after compliance_validate; PlantGate bridge is documentation plus Serving to Promise/Works order, not an app-to-app Flow edge.
- First generation remains draft (CP-G7).

## Next

Stop at draft checkpoint. Later SOAM jobs handle technology/physical.
