## Purpose
Show where GroundOS and LinkGate run, and place hangar, GCS van, comms cabin, mast, and launch kit so range audiences cannot mistake RangePlan for the GCS or the airborne computer.

## Stakeholders and Concerns
Range Manager needs hangar, range-floor launch equipment, and cabin/van layout. GCS Owner needs GroundOS on the on-prem app server with the GCS van present. Integration Lead needs LinkGate on a node in the comms cabin with datalink mast and no air-vehicle talk. Planning Programme Manager needs RangePlan kept off host nodes and separate from AirStack and GroundOS.

## Viewpoint
Technology Usage viewpoint (`technology_usage`) carrying Physical concerns on one canvas named Technology and Physical. Nodes host applications by nested containment; facilities and equipment supply physical context.

## Questions Answered
Which node hosts GroundOS? Where does LinkGate run? Is launch equipment assigned to a range-floor node? Are RangePlan and AirStack drawn as hosted on range nodes? Does LinkGate connect to the air vehicle?

## Assumptions
Single Moorfield Range site remains as-is. Jobs 01-04 motivation, capability, operations, and application elements are reused without recreation. AirStack stays off this canvas (no air-vehicle node). RangePlan has no range-floor or app-server host this job.

## Decisions
Created three nodes (Range floor node, On-prem app server, LinkGate node), three facilities (Hangar, GCS van, Comms cabin), and two equipment elements (Datalink mast, Launch equipment). Hosted GroundOS on On-prem app server and LinkGate on LinkGate node via Realization Node→App plus nested view containment (Assignment Node↔App illegal on bridge). Assigned Launch equipment to Range floor node. No work packages. No air-vehicle product structure.

## Exclusions
Work packages, plateaus, gaps, second site, costing, GroundOS rewrite, weapons system, ERP, data lake, air-vehicle SysML/product structure, and hosting of RangePlan or AirStack on range nodes.

## Open Questions
None for this draft close-out. Network inventory beyond light mast adjacency was not required.
