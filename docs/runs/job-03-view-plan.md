<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hatherley Plate Job 03 (Production Operations)

Run: job-03. Model: Hatherley Plate Ltd. Fact freeze: `docs/plant-brief.md`.
Status: pending user confirmation. No model mutations until approve.
Prior jobs: Motivation Overview (job-01) and Capability Map (job-02) already on model. Reuse job-01 stakeholders and job-02 capabilities; do not duplicate.

## Intent Summary

The mill cannot show how a customer promise becomes a mill schedule; PromiseSheet remains the pain. This pass models as-is production operations only: promise, works order, mill schedule, and plate rolling, with the named plant roles. Motivation Overview and Capability Map already exist and stay intact. No new applications, nodes, work packages, second site, costing, MES rewrite, WMS, TMS, data lake, or ERP replacement. Target deliverable is one view named **Production Operations** with business roles and processes only, so Plant Manager, Head of Sales, Operations Planner, and MES Owner can read the promise-to-rolling chain without inventing systems.

## Stakeholders and Concerns

- **Plant Manager** - as-is shop-floor chain from promise to plate rolling; keep mill path clear without new apps or nodes.
- **Head of Sales** - same chain visible from customer promise; PromiseSheet stays named as the pain, not silently replaced.
- **Operations Planner** - promise → works order → mill schedule → plate rolling as readable process flow.
- **MES Owner** - mill schedule and plate rolling stay mill-side processes; no MES rewrite and no application elements this job.
- **CRM Programme Manager** - named in scope; OrderSight stays out of this canvas (no apps); reuse stakeholder ID only.
- **Integration Lead** - named in scope; no PlantGate/app/node draws this job; reuse stakeholder ID only.

## Proposed Viewpoints

- **Business Process** (standard ArchiMate Business Process viewpoint; view name **Production Operations**)
  - Purpose: inform as-is shop floor how a customer promise becomes works order, mill schedule, and plate rolling, with named roles; PromiseSheet remains the pain in narrative.
  - Stakeholders served: Plant Manager, Head of Sales, Operations Planner, MES Owner (primary); CRM Programme Manager and Integration Lead (scope-named, reuse IDs, default off-canvas).
  - Abstraction: mixed (role set plus process-chain detail).
  - Trace: stakeholder x concern coverage in Appendix: Viewpoint Trace. Scope freezes this job to one view. Motivation and Capability Map remain reuse-only.

## Layers Involved

- Business layer only (roles and processes that run promise, works order, mill schedule, plate rolling).
- Motivation is **reuse only**: job-01 stakeholder IDs (and optional driver/goal language in docs); do not create duplicate stakeholders or a second motivation view.
- Strategy/capability is **reuse only**: job-02 capability IDs (Promise, Order, Mill schedule, Collect) may be referenced later for cross-layer; default this view is processes and roles only, no capability re-draw required.
- Explicitly not this job: application components, technology/physical nodes, implementation work packages, second site, costing, MES rewrite, WMS/TMS/data lake/ERP replacement.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). No creates until approve.
2. **Business specialist** - create Business-layer content only: business roles (or actors) needed on the canvas and business processes for promise, works order, mill schedule, and plate rolling in as-is chain order. Prefer plain names from the brief and this plan. Seed reuse registry from `docs/runs/job-01-motivation-ids.json` and `docs/runs/job-02-capability-ids.json`. Reuse existing Stakeholder elements; do not create second Plant Manager / Head of Sales / etc. Do not create application, node, or work-package elements. Do not recreate capabilities.
3. Place content on a single view named **Production Operations** using the Business Process viewpoint. Document PromiseSheet as the pain (process/docs narrative), not as a new application element.
4. **Model QA** (light) - structural checks for this view; confirm zero new applications and zero nodes; no duplicate job-01/job-02 elements.
5. **Layout** - mixed process-chain layout readable for plant and sales audience.
6. **Documentation** - short rationale and completion summary; stop. Later SOAM jobs handle application and technology layers.

## Dependencies

- Open model is Hatherley Plate Ltd with job-01 and job-02 complete: `elementCount=14`, `relationshipCount=15`, `viewCount=2` (Motivation Overview + Capability Map). Layers today: Motivation 10, Strategy 4 Capability; process/application/node count 0.
- Reuse registry seed: `docs/runs/job-01-motivation-ids.json` (six stakeholders + driver/goal/outcome/requirement) and `docs/runs/job-02-capability-ids.json` (Promise, Order, Mill schedule, Collect). Do not create second copies of those names.
- Fact freeze is `docs/plant-brief.md`. Named systems (MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate) are as-is context wording only this job; they are not modelled as application or node elements here.
- User approval of this plan before any create/update/delete via MCP.
- Process names chosen here should stay stable for later application-usage jobs.

## Validation Points

- Exactly one new view: **Production Operations**. Motivation Overview and Capability Map left intact; no other new views this job.
- Processes present covering promise, works order, mill schedule, and plate rolling.
- Named roles available via reuse (and shown as needed on canvas); no duplicate stakeholders.
- PromiseSheet remains the pain in documentation/narrative; not replaced by invented systems.
- No new application, node, work package, or second-site elements created.
- No WMS, TMS, data lake, or ERP replacement invented.
- Plant Manager, Head of Sales, Operations Planner, and MES Owner can read the as-is chain.
- Offline/live QA: no illegal mixes; schema and compliance checks when modelling runs.

## Open Questions for User

- Confirm view title stays **Production Operations** (recommended) versus a different signed label.
- Canvas audience: show four primary roles only (Plant Manager, Head of Sales, Operations Planner, MES Owner) and keep CRM Programme Manager / Integration Lead off-canvas (recommended), versus place all six roles on the view.
- Capability context on this view: omit job-02 capabilities from the canvas (recommended; processes only), versus light optional placement of Promise / Order / Mill schedule for orientation without redefining them.
- Process naming grain: four processes named Promise, Works order, Mill schedule, Plate rolling (recommended, matches prompt), versus slightly different plant-native labels if you already have preferred names.

## Confirmation Gate

**No model creates or updates run until you confirm this View Plan.**

Reply with one of:

- **approve** - proceed to business-layer modelling in a later step (specialists: business, then light QA, layout, documentation). Motivation and capability-strategy skipped (reuse only). Application and technology specialists skipped this job.
- **revise** - send notes; plan updates and re-check; still no mutations.
- **abort** - stop; summarize learning; no mutations.

## Appendix: Viewpoint Trace

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Business Process | Plant Manager; Operations Planner | Show how customer promise becomes mill schedule on as-is shop floor | inform | mixed | yes | Matrix top rank Business Process (score 6) on purpose=inform, abstraction=mixed, operations/roles tags. Standard viewpoint covers process chain plus roles without applications. |
| Business Process | Head of Sales; MES Owner | PromiseSheet stays the pain; mill schedule remains mill-owned path; no apps or nodes sneaked in | inform | mixed | yes | Business Process viewpoint can show roles and processes only. Application Structure / Technology rejected by scope freeze. |
| Business Process | CRM Programme Manager; Integration Lead | Named in scope for identity; keep out of app/integration draws this job | inform | mixed | yes | Stakeholders reused from job 01; process view does not require application cooperation or layered stack. |

## Organisation-Specific Proposals

None this pass. Standard Business Process viewpoint covers the stakeholder x concern set for job 3. View **name** is organisation-specific: **Production Operations** (viewpoint remains Business Process).

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Application Structure | Matrix hit on "applications" token from "no new applications"; apps explicitly out of scope. |
| Technology | Matrix hit on "nodes" token from "no nodes"; physical/tech out this job. |
| Business Product | Sales tag noise; product/value offering is not the ask. |
| Application Usage | Needs application components; no new applications. |
| Capability Map | Already delivered job 02; reuse IDs only, do not re-model. |
| Motivation | Already delivered job 01; reuse stakeholders only. |
| Layered | Would pull app/tech layers forbidden this job. |
| Implementation and Migration | Work packages out of freeze. |
| Organisation | Structure of org units not requested; need process chain. |
| Actor Cooperation | Actor/collab focus weaker than end-to-end promise-to-rolling process chain. |

Matrix run: `helpers/viewpoint_selection_matrix.py` with purpose=inform, abstraction=mixed; Business Process score 6, standard_fit true. Scope filter selected Business Process only; view name Production Operations.

## Appendix: Technical Hints

- Target view name: `Production Operations`.
- Viewpoint param when creating view: `business_process` or MCP-equivalent Business Process key (confirm against live create-view enum at model time; matrix key `business-process`).
- Concept spine (names only; create after approve): Business processes Promise, Works order, Mill schedule, Plate rolling; business roles as needed on canvas from the six named roles.
- PromiseSheet: documentation/pain narrative only this job; do not create ApplicationComponent for PromiseSheet, WorksERP, MillOS, OrderSight, or PlantGate.
- Reuse registry seed: load job-01 motivation IDs and job-02 capability IDs; never recreate those elements.
- Existing views (do not modify unless user asks): Motivation Overview `id-05f18c92556242fc8ce2a2252fc36867`; Capability Map `id-6613e98758a3455d95e1fcc5b8e731f7`.
- Model snapshot at plan time: name Hatherley Plate Ltd; elementCount 14; relationshipCount 15; viewCount 2; apps/processes/nodes 0.
