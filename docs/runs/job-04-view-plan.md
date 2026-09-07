<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hatherley Plate Job 04 (Application Support)

Run: job-04. Model: Hatherley Plate Ltd. Fact freeze: `docs/plant-brief.md`.
Status: approved. Specialists complete (draft CP-G7).
Prior jobs: Motivation Overview (job-01), Capability Map (job-02), Production Operations (job-03) already on model. Reuse stakeholders, roles, processes, and capabilities; do not duplicate.

## Intent Summary

Sales, mill, and integration cannot see which systems hold promises, works orders, and the mill schedule. Motivation, capabilities, and production operations already exist; this pass adds application support only. In scope: MillOS, WorksERP, PromiseSheet, OrderSight, and PlantGate, and how they support the operations already modelled. OrderSight and MillOS stay separate applications. Shared order identity is shown across systems, not as one merged blob. PlantGate bridges OrderSight promises to WorksERP works orders and does not talk to mill equipment (document that; no equipment or nodes this job). Out of scope: nodes, work packages, second site, costing, MES rewrite, ERP replacement, and invented WMS/TMS/data lake. Target deliverable is one view named **Application Support** with the same system names as the plant brief.

## Stakeholders and Concerns

- **MES Owner** - MillOS remains the MES that owns mill schedule; CRM programme must not be drawn as the MES; OrderSight stays separate from MillOS.
- **CRM Programme Manager** - OrderSight is sales-facing CRM in pilot; must not swallow MillOS; shared order identity without merge.
- **Integration Lead** - PlantGate bridges OrderSight promises to WorksERP works orders only; document that PlantGate does not talk to mill equipment; no invented integration stack.
- **Plant Manager** - which systems hold works orders and mill schedule is readable; mill path stays clear of CRM-as-MES confusion.
- **Head of Sales** - which systems hold promises is visible; PromiseSheet remains the as-is pain; OrderSight stays sales-facing.

## Proposed Viewpoints

- **Application Usage** (standard ArchiMate Application Usage viewpoint; view name **Application Support**)
  - Purpose: inform sales, mill, and integration which named applications hold and support promises, works orders, and mill schedule on the already-modelled operations chain, without merging OrderSight and MillOS.
  - Stakeholders served: MES Owner, CRM Programme Manager, Integration Lead, Plant Manager, Head of Sales.
  - Abstraction: mixed (named application set plus support links to existing business processes).
  - Trace: stakeholder x concern coverage in Appendix: Viewpoint Trace. Scope freezes this job to one view. Motivation, Capability Map, and Production Operations remain reuse-only.

## Layers Involved

- Application layer (named application components and how they support existing business processes): MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate.
- Business layer is **reuse only**: job-03 processes (Promise, Works order, Mill schedule, Plate rolling) and business roles as needed for serving/usage links; do not recreate processes or roles.
- Motivation is **reuse only**: job-01 stakeholder IDs and requirement language (OrderSight must not swallow MillOS); no second motivation view.
- Strategy/capability is **reuse only**: job-02 capability IDs may be referenced off-canvas; default omit from this canvas.
- Explicitly not this job: technology/physical nodes, equipment, facilities, implementation work packages, second site, costing, MES rewrite, WMS/TMS/data lake/ERP replacement.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). No creates until approve.
2. **Application specialist** - create Application-layer content only for the five named systems as separate application components: MillOS (MES; mill schedule), WorksERP (works orders, invoices, plate stock wording as needed), PromiseSheet (as-is promise pain), OrderSight (CRM pilot; sales-facing), PlantGate (integration gateway bridging OrderSight promises to WorksERP works orders). Document PlantGate does not talk to mill equipment; do not create equipment or node elements. Enforce freeze: OrderSight and MillOS remain distinct; no single merged application for order identity. Prefer Serving (or equivalent allowed) links from applications to reused job-03 processes so holders of promise / works order / mill schedule are visible. Seed reuse registry from `docs/runs/job-01-motivation-ids.json`, `docs/runs/job-02-capability-ids.json`, and `docs/runs/job-03-operations-ids.json`. Do not recreate stakeholders, roles, processes, or capabilities. Do not invent WMS, TMS, data lake, or ERP replacement.
3. Place content on a single view named **Application Support** using the Application Usage viewpoint. Leave Motivation Overview, Capability Map, and Production Operations intact.
4. **Model QA** (light) - structural checks for this view; confirm OrderSight ≠ MillOS; zero nodes/equipment; no duplicate job-01/02/03 elements; no invented systems.
5. **Layout** - mixed application-support layout readable for MES, CRM, integration, plant, and sales audience.
6. **Documentation** - short rationale and completion summary; stop. Later SOAM jobs handle technology/physical.

## Dependencies

- Open model is Hatherley Plate Ltd with jobs 01–03 complete: `elementCount=22`, `relationshipCount=23`, `viewCount=3` (Motivation Overview, Capability Map, Production Operations). Layer distribution at plan time: Motivation 10, Strategy 4, Business 8; Application 0; Technology/Physical 0.
- Existing views (do not replace): Motivation Overview `id-05f18c92556242fc8ce2a2252fc36867`; Capability Map `id-6613e98758a3455d95e1fcc5b8e731f7`; Production Operations `id-c189cce2288642d8b1cf3c267270d571`.
- Reuse registry seed: job-01 stakeholders/driver/goal/outcome/requirement; job-02 capabilities (Promise, Order, Mill schedule, Collect); job-03 roles and processes (Promise, Works order, Mill schedule, Plate rolling). Do not create second copies of those names.
- Fact freeze is `docs/plant-brief.md`. Named systems only; PlantGate non-equipment constraint is documentation this job.
- User approval of this plan before any create/update/delete via MCP.

## Validation Points

- Exactly one new view: **Application Support**. Prior three views left intact; no other new views this job.
- Five application components present with plant-brief names: MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate.
- OrderSight and MillOS are separate elements; no merged CRM/MES blob.
- Shared order identity expressed as cross-app support of the same process chain (or documented identity concern), not one application absorbing another.
- PlantGate documentation states bridge OrderSight→WorksERP only and does not talk to mill equipment; zero equipment/node elements created.
- Support links visible from apps to reused promise / works order / mill schedule (and plate rolling as needed) processes.
- No WMS, TMS, data lake, ERP replacement, work package, or second-site elements.
- Stakeholders can answer which system holds promises, works orders, and mill schedule from this view.
- Offline/live QA: no illegal mixes; schema and compliance checks when modelling runs.

## Open Questions for User

- Confirm view title stays **Application Support** (recommended) versus a different signed label.
- Canvas content: five apps plus reused job-03 processes with serving links (recommended) versus apps-only without process objects on the canvas.
- PromiseSheet modelling: ApplicationComponent for the as-is spreadsheet pain (recommended, matches named systems list) versus documentation/note only.
- Job-02 capabilities on canvas: omit (recommended) versus light optional placement for orientation.
- PlantGate equipment constraint: documentation field only this job (recommended; no nodes) versus defer all PlantGate physical notes to job 5.

## Confirmation Gate

**No model creates or updates run until you confirm this View Plan.**

Reply with one of:

- **approve** - proceed to application-layer modelling in a later step (specialists: application, then light QA, layout, documentation). Motivation, capability-strategy, and business skipped (reuse only). Technology-physical and implementation-migration skipped this job.
- **revise** - send notes; plan updates and re-check; still no mutations.
- **abort** - stop; summarize learning; no mutations.

## Appendix: Viewpoint Trace

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Application Usage | MES Owner; CRM Programme Manager | OrderSight and MillOS stay separate applications; CRM must not be drawn as the MES | inform | mixed | yes | Matrix ranks Application Usage (score 5) on purpose=inform, abstraction=mixed, support concern. Usage viewpoint shows which apps support which operations without merging systems into one component. |
| Application Usage | Integration Lead; Plant Manager | Shared order identity across systems; PlantGate bridges OrderSight promises to WorksERP works orders and does not talk to mill equipment | inform | mixed | yes | Application Usage can place PlantGate as integration app serving the promise-to-works-order path; equipment/node absence is documented, not drawn (tech out of scope). |
| Application Usage | Head of Sales; Sales/mill/integration audience | Which systems hold promises, works orders, and mill schedule; PromiseSheet remains the pain | inform | mixed | yes | Reuses job-03 processes (Promise, Works order, Mill schedule, Plate rolling) with serving links from named apps so holders of each step are visible. |

## Organisation-Specific Proposals

None this pass. Standard Application Usage viewpoint covers stakeholder x concern set for job 4. View **name** is organisation-specific: **Application Support** (viewpoint remains Application Usage).

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Application Structure | Matrix top (score 6) on applications/systems tags, but does not show support of already-modelled operations; structure-only would miss process linkage the problem asks for. |
| Application Cooperation | Strong on PlantGate integration, weaker on full process-support picture for sales/mill readers; can be expressed as relationships inside Application Usage. |
| Business Process | Already delivered job 03 (Production Operations); reuse processes only. |
| Business Product | Sales tag noise; product/value offering is not the ask. |
| Physical | Equipment token from "does not talk to mill equipment"; physical/nodes explicitly out this job. |
| Technology | Nodes/infra out of freeze this job. |
| Capability Map | Already job 02; reuse IDs only. |
| Motivation | Already job 01; reuse stakeholders only. |
| Layered | Would pull technology/physical forbidden this job. |
| Implementation and Migration | Work packages out of freeze. |
| Project | No programme delivery packages this job. |

Matrix run: `helpers/viewpoint_selection_matrix.py` with purpose=inform, abstraction=mixed; Application Structure 6, Application Usage 5, standard_fit true. Scope filter selects Application Usage only; view name Application Support.

## Appendix: Technical Hints

- Target view name: `Application Support`.
- Viewpoint param when creating view: `application_usage` or MCP-equivalent Application Usage key (confirm against live create-view enum at model time; matrix key `application-usage`).
- Application components (names only; create after approve): MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate.
- Freeze: OrderSight and MillOS distinct; no WMS/TMS/data lake/ERP replacement; PlantGate docs = OrderSight to WorksERP bridge, no mill equipment.
- Reuse registry seed: job-01, job-02, job-03 ID JSON files under `docs/runs/`.
- Existing views (do not modify unless user asks): Motivation Overview `id-05f18c92556242fc8ce2a2252fc36867`; Capability Map `id-6613e98758a3455d95e1fcc5b8e731f7`; Production Operations `id-c189cce2288642d8b1cf3c267270d571`.
- Model snapshot at plan time: name Hatherley Plate Ltd; elementCount 22; relationshipCount 23; viewCount 3; Application 0; nodes 0.

