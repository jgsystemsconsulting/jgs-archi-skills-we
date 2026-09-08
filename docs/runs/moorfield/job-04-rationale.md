# Rationale - Application Support

## Purpose
Show the as-is application landscape for AirStack, GroundOS, SortieBoard, RangePlan, and LinkGate so GCS Owner, Planning Programme Manager, and Integration Lead can see which system holds planning, bridge, live control, and airborne compute without merging those systems.

## Stakeholders and Concerns
GCS Owner needs GroundOS to stay the live-control application. Planning Programme Manager needs RangePlan to stay planning-facing. Integration Lead needs five named apps distinct, with LinkGate bridging RangePlan tasking to GroundOS only and no air-vehicle talk. Range Manager and Chief Instructor need a clear map of tasking vs live vs airborne ownership.

## Viewpoint
Application Cooperation (overview), deliverable name Application Support.

## Questions Answered
Which named applications exist as-is, how RangePlan tasking reaches GroundOS via LinkGate, and how those apps lightly support the reused Task/Clear/Fly/Recover process chain without collapsing RangePlan, AirStack, and GroundOS?

## Assumptions
Job-3 BusinessProcess IDs for Task, Clear, Fly, and Recover are the shared sortie identity spine. No Application Data Object is required; identity is not a merged app. Job-2 capabilities stay off this canvas. Technology nodes and equipment wait for a later job.

## Decisions
Five ApplicationComponents with exact brief names. Flow edges RangePlan to LinkGate to GroundOS. Light Serving edges from apps to reused processes. SortieBoard modelled as an ApplicationComponent (as-is spreadsheet pain). LinkGate non-air-vehicle boundary recorded in element documentation and a view note. No nodes, equipment, work packages, weapons system, ERP, data lake, or air-vehicle structure.

## Exclusions
Technology and physical nodes or equipment. Implementation work packages. Second site and costing. GroundOS rewrite. Capability Map content on this view. Motivation spine redraw. Full Range Operations role chain redraw. Invented ERP, data lake, weapons, or air-vehicle SysML.

## Open Questions
None for this freeze. Later SOAM job covers technology and physical placement of LinkGate and GroundOS hosts.
