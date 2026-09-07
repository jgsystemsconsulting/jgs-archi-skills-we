## Views Touched
- Technology and Physical (id-6ef45eb1bf8340f2b2eba45c4f92b9e9) — created/updated this job
- Prior views left intact: Motivation Overview, Capability Map, Production Operations, Application Support

## Decisions
- Layout assess: excellent
- Nodes: Mill floor node; On-prem app server; PlantGate node
- Facilities: Plate mill building; Comms room
- Equipment: Rolling equipment assigned with mill-floor node (freeze)
- Hosting: MillOS + WorksERP on On-prem app server; PlantGate on PlantGate node
- OrderSight omitted from all nodes; remains separate from MillOS
- Viewpoint param used: 'technology_usage'

## Open Questions
- None blocking draft close-out

## Confirmation Status
approved (View Plan Job 05)

## Specialists Run
- archi-technology-physical
- archi-traceability
- archi-model-qa
- archi-layout
- archi-documentation

## Deliberately Deferred
- Implementation and migration work packages
- OrderSight hosting topology outside mill
- Extra architecture beyond plant-brief physical facts

## Improve Next
- If Archi nesting flattened after auto-layout, re-nest deployed apps inside node containers and re-assess.
