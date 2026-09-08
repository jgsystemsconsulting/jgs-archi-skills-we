# Rationale - Range Operations

## Purpose
Show the as-is Moorfield range-floor chain task to clear to fly to recover with the named business roles that run each step, so Range Manager and Chief Instructor can see the path from tasked sortie to live GCS without inventing systems.

## Stakeholders and Concerns
Range Manager and Chief Instructor need floor visibility. Sortie Planner owns tasking; GCS Owner owns the live fly period. Planning Programme Manager and Integration Lead witness the freeze (off-canvas). SortieBoard remains the pain in narrative, not a drawn application.

## Viewpoint
Business Process Cooperation (overview), deliverable name Range Operations.

## Questions Answered
How does a tasked sortie become a live GCS period on the range floor, and which roles perform task, clear, fly, and recover?

## Assumptions
BusinessRole elements are required for assignment; job-1 Stakeholder IDs are not duplicated as a second stakeholder set. Process labels match capability labels but are distinct BusinessProcess IDs. Job-2 capabilities stay off this view.

## Decisions
On-canvas roles: Sortie Planner to Task, Range Manager to Clear, GCS Owner to Fly, Chief Instructor to Recover. Triggering flow between the four processes. No applications, nodes, work packages, or air-vehicle structure. SortieBoard documentation-only pain.

## Exclusions
New ApplicationComponents (including SortieBoard, GroundOS, RangePlan, AirStack, LinkGate as elements). Technology and physical nodes. Implementation work packages. Capability Map redraw. Motivation spine redraw. Second site and costing.

## Open Questions
None for this freeze. Later SOAM jobs cover application and technology layers.
