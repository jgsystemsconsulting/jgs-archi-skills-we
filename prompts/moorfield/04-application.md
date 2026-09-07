<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Job 4: Application Support

## Paste

```text
/archi-orchestrator on the current Hawker Range Systems model, application support for AirStack, GroundOS, SortieBoard, RangePlan, and LinkGate. Shared sortie identity. RangePlan, AirStack, and GroundOS stay separate.

Problem: Instructors, GCS, and integration cannot see which systems hold tasking, live control, and the airborne computer. The planning programme must not be drawn as the GCS or as AirStack.

Stakeholders: GCS Owner, Planning Programme Manager, Integration Lead, Range Manager, Chief Instructor.

Concerns: RangePlan, AirStack, and GroundOS stay separate. Shared sortie identity, not one merged blob. LinkGate bridges RangePlan tasking to GroundOS and does not talk to the air vehicle.

Scope: In: AirStack, GroundOS, SortieBoard, RangePlan, LinkGate, and how they support the operations already modelled. Out: nodes, work packages, second site, costing, GroundOS rewrite, ERP replacement, air-vehicle SysML.

Current state: Motivation, capabilities, and range operations already exist. Named systems as in docs/moorfield-brief.md.

Target state: View named Application Support. Same system names. Do not invent a weapons system, ERP, data lake, or air-vehicle structure.

Expected outcome: Application Support only. Facts: docs/moorfield-brief.md.
```

## Specialists expected

- archi-elicit
- archi-viewpoint-select
- archi-application

Do not invoke these yourself.

## Pass checks

- Confirmation gate shown before any MCP mutate
- View named exactly Application Support
- AirStack, GroundOS, SortieBoard, RangePlan, and LinkGate are present
- RangePlan, AirStack, and GroundOS remain separate
- No weapons system, ERP, data lake, or air-vehicle structure
- Documentation fields are not a restatement of the name
