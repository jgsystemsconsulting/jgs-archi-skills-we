<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Orchestrator report - Hatherley Plate Job 05

## Status

- confirmation_status: **approved**
- run_status: **SPECIALISTS_COMPLETE** (DONE)
- view_plan: docs/runs/job-05-view-plan.md
- viewpoint_trace: docs/runs/job-05-viewpoint-trace.md
- normalized_intent: docs/runs/job-05-normalized-intent.md
- specialist_result: docs/runs/job-05-specialist-result.md
- technology_ids: docs/runs/job-05-technology-ids.json
- mutations: **yes** (technology-physical through documentation)

## Guard

- get-model-info name: **Hatherley Plate Ltd** (pass)
- final snapshot: elementCount 33, relationshipCount 41, viewCount 5
- layers: {"Strategy": 4, "Business": 8, "Application": 5, "Technology": 3, "Physical": 3, "Motivation": 10}

## Specialists run (post-approve)

1. archi-technology-physical,  view **Technology and Physical** `id-6ef45eb1bf8340f2b2eba45c4f92b9e9` viewpoint `technology_usage`
2. archi-traceability,  light whole-model traces (req↔host; app→capability Realization)
3. archi-model-qa,  freeze and structural checks recorded
4. archi-layout,  assess **excellent**; PNG exported
5. archi-documentation,  rationale + completion summary (schema pass)

Skipped: motivation, capability-strategy, business, application (reuse), implementation-migration.

## Pass checks

```json
{
  "view_named_technology_and_physical": true,
  "facility_or_equipment_assigned_to_node": true,
  "ordersight_millos_separate": true,
  "ordersight_not_on_mill_appserver": true,
  "millos_workserp_on_onprem": true,
  "plantgate_on_plantgate_node": true,
  "plantgate_no_equipment_link": true,
  "work_package_count_0": true,
  "no_forbidden_systems": true,
  "evidence_ok": true,
  "model_as_is": true,
  "layout_excellent": true
}
```

## Hard freeze

- Equipment/facility assigned to node: true (Mill floor node → Rolling equipment)
- Work packages: 0
- OrderSight != MillOS; OrderSight not on mill app-server node: true
- No extra architecture beyond named physical/nodes
- Hosting legality note: Realization Node→App used (Assignment Node↔App rejected by bridge)

## Next

Draft close-out complete. No git commit from this job.
