<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hatherley Plate Job 05 (Technology and Physical + close-out)

Run: job-05. Model: Hatherley Plate Ltd. Fact freeze: `docs/plant-brief.md`.
Status: pending confirmation. No mutations this turn.
Prior jobs: Motivation Overview (job-01), Capability Map (job-02), Production Operations (job-03), Application Support (job-04) already on model. REUSE existing elements. Do not duplicate MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate, or prior motivation/capability/business content.

## Intent Summary

Plant engineers need mill equipment and the comms room on the drawing so OrderSight cannot be mistaken for the mill. Motivation, capabilities, production operations, and application support already exist; this pass adds technology and physical placement only, then closes the as-is model with traceability, QA, layout, and documentation. In scope: plate mill building, comms room, rolling equipment on a mill-floor node, on-prem app server hosting MillOS and WorksERP, PlantGate on a node in the comms room, and the hard freeze that at least one equipment or facility is assigned to a node. OrderSight and MillOS stay separate applications; OrderSight must not swallow MillOS and must not appear as the mill stack. Out of scope: work packages, second site, costing, MES rewrite, extra architecture, WMS, TMS, data lake, ERP replacement. Target deliverable is one view named **Technology and Physical**, then whole-model trace, QA, layout, and documentation fields. Model remains as-is.

## Stakeholders and Concerns

- **Plant Manager** - plate mill building and rolling equipment readable on a mill-floor node; mill path cannot be confused with CRM.
- **MES Owner** - MillOS stays on the on-prem mill app server with WorksERP; OrderSight is not drawn as MES or as host of mill schedule infrastructure.
- **Integration Lead** - PlantGate sits on a node in the comms room; still does not talk to mill equipment; physical separation from mill-floor equipment is visible.
- **CRM Programme Manager** - OrderSight remains sales-facing and separate from MillOS; physical drawing must not let OrderSight swallow the mill.

## Proposed Viewpoints

- **Technology Usage** (standard ArchiMate Technology Usage viewpoint; view name **Technology and Physical**)
  - Purpose: inform plant, MES, integration, and CRM audiences which nodes host MillOS, WorksERP, and PlantGate, and keep OrderSight off the mill hosting path.
  - Stakeholders served: Plant Manager, MES Owner, Integration Lead, CRM Programme Manager.
  - Abstraction: mixed (named nodes plus reused application components).
  - Trace: Appendix: Viewpoint Trace. Single new view this job.

- **Physical** (standard ArchiMate Physical viewpoint concerns on the same canvas)
  - Purpose: show plate mill building, comms room, and rolling equipment, with at least one equipment or facility assigned to a node.
  - Stakeholders served: Plant Manager, MES Owner, Integration Lead, CRM Programme Manager.
  - Abstraction: mixed (facilities/equipment with node assignment).
  - Trace: same appendix. Not a second view; content lands on **Technology and Physical**.

## Layers Involved

- Technology layer (nodes hosting applications): mill-floor node; on-prem app server node; PlantGate node in the comms room.
- Physical layer (facilities and equipment): plate mill building; comms room; rolling equipment assigned onto the mill-floor node (hard freeze).
- Application layer is **reuse only**: MillOS, WorksERP, PlantGate (and OrderSight kept separate, not hosted on mill app server). PromiseSheet reuse optional off-canvas.
- Business, strategy/capability, and motivation are **reuse only** for later traceability; no new views in those layers this job.
- Explicitly not this job: work packages, plateaus, gaps, second site, costing, MES rewrite, WMS/TMS/data lake/ERP replacement, extra architecture beyond the named physical/node facts.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). **No creates until approve.**
2. **Technology-physical specialist** - create technology/physical content only for plant-brief facts: plate mill building; comms room; rolling equipment; mill-floor node with rolling equipment assigned; on-prem app server node hosting reused MillOS and WorksERP; PlantGate node in the comms room hosting reused PlantGate. Enforce freezes: at least one equipment or facility assigned to a node; OrderSight != MillOS; do not place OrderSight on the mill app-server node; PlantGate does not connect to mill equipment; no work packages; no invented systems. Seed reuse registry from `docs/runs/job-01-motivation-ids.json`, `docs/runs/job-02-capability-ids.json`, `docs/runs/job-03-operations-ids.json`, `docs/runs/job-04-application-ids.json`. Place content on one view named **Technology and Physical** (viewpoint param `technology_usage` or MCP-equivalent; fallback `technology` / omit if needed). Leave prior four views intact.
3. **Traceability specialist** - cross-layer traces on the whole as-is model (motivation through technology/physical) without adding scope objects.
4. **Model QA** - structural and freeze checks (equipment/facility to node assignment present; OrderSight and MillOS distinct; zero work packages; no duplicate apps; no extra architecture).
5. **Layout** - readable technology/physical layout for plant/MES/integration/CRM audience on **Technology and Physical**; do not churn prior views unless QA requires a non-mutating fix the user approves.
6. **Documentation** - rationale fields and completion summary; stop.

Skipped by scope: motivation, capability-strategy, business, application (reuse only), implementation-migration (no work packages).

## Dependencies

- Open model is **Hatherley Plate Ltd** with jobs 01-04 complete: `elementCount=27`, `relationshipCount=31`, `viewCount=4`. Layer distribution at plan time: Motivation 10, Strategy 4, Business 8, Application 5; Technology/Physical 0 (nodes 0).
- Existing views (do not replace): Motivation Overview `id-05f18c92556242fc8ce2a2252fc36867`; Capability Map `id-6613e98758a3455d95e1fcc5b8e731f7`; Production Operations `id-c189cce2288642d8b1cf3c267270d571`; Application Support `id-90bb9ec6131b44f9966ac494bd89a90c`.
- Reuse application IDs (job-04): MillOS `id-e74300558c24411c9ca9cf76c2d9ecd6`; WorksERP `id-45a53e69f46a4c80a0e8bcb81ba24cf9`; PromiseSheet `id-d5dab10f11a04eedb0ba9532bd2940b1`; OrderSight `id-b8e160d2c6d24f34badc02f1b6ae6c6f`; PlantGate `id-d0698a626afc460d8de1493b05a421e6`.
- Fact freeze is `docs/plant-brief.md` Physical (job 5) and Hard freeze sections.
- User approval of this plan before any create/update/delete via MCP.

## Validation Points

- Exactly one new view: **Technology and Physical**. Prior four views left intact.
- Nodes present covering: mill-floor; on-prem app server; PlantGate/comms-room node.
- Facilities/places: plate mill building; comms room.
- Rolling equipment present; **at least one equipment or facility assigned to a node**.
- MillOS and WorksERP reused and hosted on the on-prem app server node (not recreated).
- PlantGate reused and hosted on the comms-room node; no relationship that makes PlantGate talk to mill equipment.
- OrderSight and MillOS remain separate elements; OrderSight not assigned to the mill app-server node.
- Zero work packages, plateaus, gaps, second-site, WMS, TMS, data lake, or ERP-replacement elements.
- Traceability run covers whole as-is model after tech/physical content exists.
- QA report recorded; layout assessed; documentation/rationale fields written.
- Offline/live QA: no illegal mixes; schema and compliance checks when modelling runs.

## Open Questions for User

- Confirm view title stays **Technology and Physical** (recommended) versus a different signed label.
- Formal viewpoint param: `technology_usage` for the combined canvas (recommended) versus `technology` or omit-viewpoint general-purpose if Archi rejects physical types under Technology Usage.
- OrderSight hosting: omit from all nodes this job (recommended; brief gives no mill host for CRM; reinforces not-the-mill) versus document off-canvas only.
- Node naming: plain brief labels (Mill floor node, On-prem app server, PlantGate node / Comms room node) (recommended) versus site-specific asset tags if you supply them.
- Plate mill building and comms room: Facility elements (recommended) versus Node-only places without Facility types.
- Rolling equipment: Equipment element assigned to mill-floor node (recommended) to satisfy freeze explicitly.
- Traceability depth after tech/physical: whole-model light trace (recommended) versus tech-to-app edges only.

## Confirmation Gate

**No model creates or updates run until you confirm this View Plan.**

Reply with one of:

- **approve** - proceed to modelling in a later step. Post-approve specialist order: **archi-technology-physical**, then **archi-traceability**, then **archi-model-qa**, then **archi-layout**, then **archi-documentation**. Motivation, capability-strategy, business, and application skipped (reuse only). Implementation-migration skipped (no work packages).
- **revise** - send notes; plan updates and re-check; still no mutations.
- **abort** - stop; summarize learning; no mutations.

## Appendix: Viewpoint Trace

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Technology Usage | Plant Manager; MES Owner | On-prem app server hosts MillOS and WorksERP; OrderSight must not swallow MillOS | inform | mixed | yes | Technology Usage shows apps on nodes; MillOS/WorksERP reused on app server; OrderSight kept off mill host path. |
| Technology Usage | Integration Lead | PlantGate on a node in the comms room; does not talk to mill equipment | inform | mixed | yes | PlantGate on comms-room node; no equipment link. |
| Physical | Plant Manager; MES Owner | Plate mill building; rolling equipment on mill-floor node; equipment/facility assigned to a node | inform | mixed | yes | Matrix Physical score 6; facilities/equipment with node assignment meet hard freeze. |
| Physical | Integration Lead; CRM Programme Manager | Comms room visible so CRM path is not mistaken for the mill | inform | mixed | yes | Comms room facility with PlantGate node keeps integration housing distinct from mill floor. |

## Organisation-Specific Proposals

View **name** organisation-specific: **Technology and Physical**. Formal viewpoint remains standard Technology Usage (`technology_usage`) carrying Physical concerns on one canvas. No second metamodel types invented.

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Application Usage | Job 04 done; reuse apps only. |
| Layered | Extra architecture risk beyond named physical/nodes. |
| Implementation and Migration | Work packages out of freeze. |
| Technology structure-only | Weaker "what runs where" than Technology Usage; fallback param only. |
| Motivation / Capability Map / Business Process | Prior jobs; reuse only. |

Matrix: Physical 6, Technology 4, standard_fit true. Combined one view per user target state.

## Appendix: Technical Hints

- Target view name: `Technology and Physical`.
- Viewpoint param when creating view: `technology_usage` (confirm against live create-view; fallback `technology` or omit).
- Recipe to read at model time: `archimate://recipes/technology-deployment` (nodes as containers; nest deployed apps; do not invent Path relationship type).
- Physical facts (names only; create after approve): Plate mill building; Comms room; Rolling equipment; Mill-floor node; On-prem app server; PlantGate/comms node.
- App reuse (do not recreate): MillOS, WorksERP on app server; PlantGate on comms node; OrderSight not on mill app server; PromiseSheet optional off-canvas.
- Freeze: equipment or facility assigned to a node; OrderSight != MillOS; no work packages; no WMS/TMS/data lake/ERP replacement; no second site.
- Reuse registry seed: job-01..job-04 ID JSON under `docs/runs/`.
- Existing views (do not modify unless user asks): Motivation Overview `id-05f18c92556242fc8ce2a2252fc36867`; Capability Map `id-6613e98758a3455d95e1fcc5b8e731f7`; Production Operations `id-c189cce2288642d8b1cf3c267270d571`; Application Support `id-90bb9ec6131b44f9966ac494bd89a90c`.
- Model snapshot at plan time: name Hatherley Plate Ltd; elementCount 27; relationshipCount 31; viewCount 4; Application 5; Technology/Physical 0; nodes 0.
