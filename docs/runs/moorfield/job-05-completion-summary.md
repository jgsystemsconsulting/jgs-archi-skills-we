## Views Touched
- Technology and Physical (id-7585e12756874cd1855d73253da55504),  created/updated this job
- Prior views left intact: Motivation Overview, Capability Map, Range Operations, Application Support

## Decisions
- Nodes: Range floor node; On-prem app server; LinkGate node
- Facilities: Hangar; GCS van; Comms cabin
- Equipment: Launch equipment assigned to range-floor node (freeze); Datalink mast light adjacency
- Hosting: GroundOS on On-prem app server; LinkGate on LinkGate node (Realization + nest)
- RangePlan and AirStack omitted from host nodes; remain separate from GroundOS
- Viewpoint param used: 'technology_usage'
- Layout assess: excellent

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
- AirStack host topology (no air-vehicle node)
- Full network inventory beyond mast adjacency

## Improve Next
- If Archi nesting flattened after auto-layout, re-nest deployed apps inside node containers and re-assess.
