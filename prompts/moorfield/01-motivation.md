<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Job 1: Motivation Overview

## Paste

```text
/archi-orchestrator Hawker Range Systems: drivers, goals, and outcomes for sortie visibility. RangePlan must not swallow AirStack or GroundOS. No capabilities, processes, applications, or nodes. Do not model the air vehicle as product structure.

Problem: Promised sortie times do not match what Moorfield Range can fly. Instructors track the day in SortieBoard. The live sortie runs on GroundOS. RangePlan is funded to fix visibility. Range engineers fear RangePlan will be drawn as if it replaces GroundOS or AirStack.

Stakeholders: Range Manager, Chief Instructor, GCS Owner, Planning Programme Manager, Sortie Planner, Integration Lead.

Concerns: Instructors and the range must share one sortie identity from tasking to live GCS. Range Manager and Chief Instructor must answer "is this sortie on the range this morning?" without SortieBoard. RangePlan must not swallow AirStack or GroundOS.

Scope: In: drivers, goals, outcomes, and the RangePlan-must-not-swallow-AirStack-or-GroundOS requirement. Out: capabilities, processes, applications, nodes, work packages, second site, costing, GroundOS rewrite, weapons system, air-vehicle SysML.

Current state: Hawker Range Systems Ltd, UK contractor, one site Moorfield Range. Tactical training UAS. Sorties live in SortieBoard. Live control lives in GroundOS. AirStack flies on the air vehicle. RangePlan is in pilot.

Target state: A Motivation Overview that Range Manager and Chief Instructor can sign. Shared sortie identity as a desired state. RangePlan remains planning-facing, not the GCS and not the airborne computer.

Expected outcome: View named Motivation Overview. No other views this job. Do not invent a weapons system, ERP, data lake, or air-vehicle structure. Facts: docs/moorfield-brief.md in the worked-example repository.
```

## Specialists expected

- archi-elicit
- archi-viewpoint-select
- archi-motivation

Do not invoke these yourself.

## Pass checks

- Confirmation gate shown before any MCP mutate
- View named exactly Motivation Overview
- RangePlan-must-not-swallow-AirStack-or-GroundOS is present as a requirement
- No capabilities, processes, applications, or nodes added
- No air-vehicle product structure
- Documentation fields are not a restatement of the name
