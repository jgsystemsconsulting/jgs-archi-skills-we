## Purpose
Show where MillOS, WorksERP, and PlantGate run, and place plate mill physical assets so plant and CRM audiences cannot mistake OrderSight for the mill stack.

## Stakeholders and Concerns
Plant Manager needs the plate mill building and rolling equipment on a mill-floor node. MES Owner needs MillOS with WorksERP on the on-prem app server. Integration Lead needs PlantGate on a comms-room node with no mill-equipment link. CRM Programme Manager needs OrderSight kept off every mill host node.

## Viewpoint
Technology Usage viewpoint (`technology_usage` preferred) carrying Physical concerns on one canvas named Technology and Physical. Nodes host applications by nested containment; facilities and equipment supply physical context.

## Questions Answered
Which node hosts MillOS and WorksERP? Where does PlantGate run? Is rolling equipment assigned to a mill-floor node? Is OrderSight drawn as part of mill hosting? Does PlantGate connect to mill equipment?

## Assumptions
Single Hatherley Works site remains as-is. Job 01-04 motivation, capability, operations, and application elements are reused without recreation. OrderSight has no mill host in the brief, so it is omitted from all nodes this job.

## Decisions
Created three nodes (Mill floor node, On-prem app server, PlantGate node), two facilities (Plate mill building, Comms room), and Rolling equipment. Assigned MillOS and WorksERP to On-prem app server; PlantGate to PlantGate node; rolling equipment (or facility) assignment satisfies the freeze. No work packages. No second site.

## Exclusions
Work packages, plateaus, gaps, WMS, TMS, data lake, ERP replacement, MES rewrite, costing, second site, and any OrderSight hosting on mill infrastructure.

## Open Questions
None for this draft close-out. Node asset tags were not supplied; plain brief labels used.
