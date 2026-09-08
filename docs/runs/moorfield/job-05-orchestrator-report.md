<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Orchestrator report - Hawker Range Systems Job 05

## Status

- confirmation_status: **approved**
- run_status: **SPECIALISTS_COMPLETE** (DONE)
- view_plan: docs/runs/moorfield/job-05-view-plan.md
- specialist_result: docs/runs/moorfield/job-05-specialist-result.md
- technology_ids: docs/runs/moorfield/job-05-technology-ids.json
- mutations: **yes** (technology-physical through documentation)
- specialists_run: archi-elicit, archi-viewpoint-select, archi-technology-physical, archi-traceability, archi-model-qa, archi-layout, archi-documentation

## Guard

- get-model-info name: **Hawker Range Systems Ltd** (pass)
- final snapshot: elementCount 35, relationshipCount 35, viewCount 5
- layers: {"Strategy": 4, "Business": 8, "Application": 5, "Technology": 3, "Physical": 5, "Motivation": 10}

## Specialists run (post-approve)

1. archi-technology-physical — view **Technology and Physical** `id-7585e12756874cd1855d73253da55504` viewpoint `technology_usage`
2. archi-traceability — light whole-model traces (req↔host; app→capability Realization)
3. archi-model-qa — freeze and structural checks recorded
4. archi-layout — assess excellent; PNG exported
5. archi-documentation — rationale + completion summary

Skipped: motivation, capability-strategy, business, application (reuse), implementation-migration.

## Pass checks

```json
{
  "view_named_technology_and_physical": true,
  "facility_or_equipment_assigned_to_node": true,
  "rangeplan_airstack_groundos_separate": true,
  "rangeplan_airstack_not_on_range_hosts": true,
  "groundos_on_onprem": true,
  "linkgate_on_linkgate_node": true,
  "linkgate_no_launch_equipment_link": true,
  "work_package_count_0": true,
  "no_forbidden_systems": true,
  "evidence_ok": true,
  "doc_not_name_only": true,
  "model_as_is": true,
  "layout_ok": true,
  "no_air_vehicle_structure": true
}
```

## Hard freeze

- Equipment/facility assigned to node: True
- Work packages: 0
- RangePlan, AirStack, GroundOS separate; RangePlan/AirStack not on range hosts: True
- LinkGate on cabin node; no launch-equipment link pretending air interface: True
- Hosting legality note: Realization Node→App used (Assignment Node↔App rejected by bridge)
- No air-vehicle SysML / product structure

## Next

Draft close-out complete. No git commit from this job.
