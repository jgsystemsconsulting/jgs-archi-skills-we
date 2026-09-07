<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Job 2: Capability Map

## Paste

```text
/archi-orchestrator on the current Hawker Range Systems model, capability map for tasking to live sortie. Reuse the motivation already modelled. No GroundOS rewrite.

Problem: Instructors, the range, and the planning programme cannot see which capabilities actually run tasking, clearance, live GCS, and recover. Job 1 already captured why visibility matters.

Stakeholders: Range Manager, Chief Instructor, GCS Owner, Planning Programme Manager, Sortie Planner.

Concerns: One capability map they can agree on. GroundOS stays the live-sortie capability owner. AirStack stays airborne. RangePlan stays planning-facing. No GroundOS rewrite.

Scope: In: tasking-to-live-sortie capabilities on the current model. Out: new processes, new applications, nodes, work packages, second site, costing, GroundOS rewrite, air-vehicle SysML.

Current state: Motivation Overview already exists. Tasking in SortieBoard, live control in GroundOS, airborne computer AirStack, RangePlan in pilot.

Target state: View named Capability Map. Same capability names if they appear on later views. Reuse job 1 motivation. Do not invent a weapons system, ERP, data lake, or air-vehicle structure.

Expected outcome: Capability Map only. Facts: docs/moorfield-brief.md.
```

## Specialists expected

- archi-elicit
- archi-viewpoint-select
- archi-capability-strategy

Do not invoke these yourself.

## Pass checks

- Confirmation gate shown before any MCP mutate
- View named exactly Capability Map
- Job 1 motivation reused, not duplicated as a second set of drivers
- No GroundOS rewrite
- Documentation fields are not a restatement of the name
