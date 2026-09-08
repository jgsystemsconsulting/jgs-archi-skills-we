## Purpose
Agree which strategy capabilities cover tasking through recover on the Moorfield tasking-to-live-sortie path, with ownership boundaries held in plain language.

## Stakeholders and Concerns
Range Manager and Chief Instructor need one agreed capability map. GCS Owner needs GroundOS kept as live-sortie owner on Fly. Planning Programme Manager needs RangePlan kept planning-facing on Task. Sortie Planner needs stable capability names for later SOAM views without a second motivation spine.

## Viewpoint
Standard ArchiMate Capability Map viewpoint (`capability_map`), overview abstraction. Single group band Tasking to live sortie with spatial left-to-right order Task, Clear, Fly, Recover.

## Questions Answered
Which capabilities run tasking, clearance, live GCS, and recover? Where do GroundOS, AirStack, and RangePlan ownership sit without drawing applications? What names stay fixed for later views?

## Assumptions
Fact freeze is docs/moorfield-brief.md. Job 1 Motivation Overview and IDs remain unchanged. Cap-Cap Flow or Association is omitted after the Hatherley lesson; order on the canvas carries the spine. Named systems appear in documentation and the view note only.

## Decisions
Four top-level capabilities with plain names Task, Clear, Fly, Recover. View title Capability Map. GroundOS owns live-sortie on Fly in text only; AirStack airborne; RangePlan planning-facing. No application, process, node, or work-package elements this job.

## Exclusions
Motivation re-modelling, business processes, application components, technology and physical nodes, work packages, second site, costing, GroundOS rewrite, weapons system, air-vehicle product or SysML structure.

## Open Questions
None blocking job 02. Later SOAM jobs attach operations, applications, and technology to these capability IDs.
