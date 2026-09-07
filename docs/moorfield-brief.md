<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Hawker Range Systems Ltd (frozen)

UK aerospace and defence contractor. One site: Moorfield Range. Tactical
training UAS for range practice. Not a real programme. Not Meridian Freight.
Not Hatherley Plate.

This brief is the fact freeze for the sequenced SOAM jobs. Prompt files
cite it. The agent must not invent extra scope.

ArchiMate in Archi only. Do not model the air vehicle as a product
structure. SysML stays off this canvas.

## Roles

- Range Manager
- Chief Instructor
- GCS Owner
- Planning Programme Manager
- Sortie Planner
- Integration Lead

## Named as-is systems

- AirStack: airborne mission computer. Never drawn as replaced by planning
  software.
- GroundOS: ground control station software. Owns the live sortie. Never
  swallowed by RangePlan.
- SortieBoard: shared-drive spreadsheet of the day's sorties. The pain.
- RangePlan: mission-planning tool in pilot. Sales-facing for the
  programme: funded for sortie visibility only.
- LinkGate: ground datalink gateway in the comms cabin. Bridges RangePlan
  tasking to GroundOS. Does not talk to the air vehicle.

## Physical (job 5)

- Hangar
- GCS van
- Comms cabin
- Datalink mast
- Launch equipment on a range-floor node
- On-prem app server node hosting GroundOS
- LinkGate on a node in the comms cabin

## Motivation spine (job 1)

- Driver: promised sortie times do not match what the range can fly.
- Goal: instructors and the range share one sortie identity from tasking
  to live GCS.
- Outcome: Range Manager and Chief Instructor can answer "is this sortie
  on the range this morning?" without SortieBoard.
- Requirement: RangePlan must not swallow AirStack or GroundOS.

## Hard freeze

- RangePlan, AirStack, and GroundOS stay separate applications.
- Shared sortie identity, not one merged blob.
- At least one equipment or facility element assigned to a node.
- No work packages, no second site, no costing, no GroundOS rewrite.
- Do not invent a weapons system, ERP, data lake, or air-vehicle SysML
  structure.
- Do not draw RangePlan as the GCS or as the airborne computer.
