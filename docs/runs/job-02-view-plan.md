<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hatherley Plate Job 02 (Capability Map)

Run: job-02. Model: Hatherley Plate Ltd. Fact freeze: `docs/plant-brief.md`.
Status: pending user confirmation. No model mutations until approve.
Prior job: Motivation Overview already on model (job-01). Reuse motivation IDs; do not duplicate drivers/goals.

## Intent Summary

Finance, operations, and the plant cannot see which capabilities actually run promise, order, mill schedule, and collect at Hatherley Works. Job 1 already captured why visibility matters; this pass does not re-model motivation. Scope is one agreed sales-to-mill capability map on the current model. MillOS stays the mill capability owner; OrderSight stays sales-facing; no ERP replacement. Target deliverable is a single view named **Capability Map** with stable capability names for later views. Do not invent WMS, TMS, data lake, ERP replacement, new processes, applications, nodes, work packages, second site, costing, or MES rewrite.

## Stakeholders and Concerns

- **Plant Manager** - one capability map the plant can agree on; keep mill capabilities under plant control (MillOS owns mill schedule capability).
- **Head of Sales** - same map covers sales-facing promise/order capabilities; OrderSight remains sales-facing, not mill owner.
- **MES Owner** - mill schedule capability stays with MillOS; map must not imply OrderSight or ERP swallows mill capability.
- **CRM Programme Manager** - OrderSight scope stays visibility/sales-facing; map must not expand CRM into mill rewrite or ERP replacement.
- **Operations Planner** - map names the capabilities that run promise, order, mill schedule, and collect so plan and promise stop talking past each other.
- **Integration Lead** (context from brief/job-01, not primary signatory this job) - shared order identity remains a motivation constraint; no merge of systems on this map.

## Proposed Viewpoints

- **Capability Map** (standard ArchiMate Capability Map viewpoint; view name **Capability Map**)
  - Purpose: decide and agree which sales-to-mill capabilities run promise, order, mill schedule, and collect; freeze names for later views.
  - Stakeholders served: Plant Manager, Head of Sales (agreement owners); MES Owner and CRM Programme Manager (MillOS vs OrderSight boundary); Operations Planner (promise-to-schedule capability chain).
  - Abstraction: overview.
  - Trace: stakeholder x concern coverage in Appendix: Viewpoint Trace. Scope freezes this job to one view. Motivation remains reuse-only (existing Motivation Overview); no second motivation view.

## Layers Involved

- Strategy/capability map content only (what the organisation can do along sales-to-mill: capabilities, and only light strategy structure if needed to group the map).
- Motivation is **reuse only**: existing job-01 stakeholders/driver/goal/outcome/requirement IDs may be referenced for trace language; do not create duplicate motivation elements or a second motivation view.
- Explicitly not this job: new business processes, application components, technology/physical nodes, implementation work packages, second site, costing, MES rewrite, WMS/TMS/data lake/ERP replacement.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). No creates until approve.
2. **Capability / strategy specialist** - create Capability-layer content only for the sales-to-mill chain covering promise, order, mill schedule, and collect. Prefer plain capability names that can stay stable on later views. Do not create processes, applications, nodes, or work packages. Do not recreate job-01 motivation elements; seed reuse registry from `docs/runs/job-01-motivation-ids.json`.
3. Place content on a single view named **Capability Map** using the Capability Map viewpoint. Optional: show minimal links to reused motivation goal/requirement for context only if the specialist judges it helps agreement without clutter; default is capabilities-first map.
4. **Model QA** (light) - structural checks for this view; no cross-layer invent; confirm no duplicate drivers/goals.
5. **Layout** - overview grid/groups fit for Plant Manager and Head of Sales agreement (capability-map layout guidance).
6. **Documentation** - short rationale and completion summary; stop. Later SOAM jobs handle process/app/tech layers.

## Dependencies

- Open model is Hatherley Plate Ltd with job-01 complete: `elementCount=10`, `relationshipCount=15`, `viewCount=1` (Motivation Overview only). Layer distribution Motivation-only today.
- Reuse registry seed: `docs/runs/job-01-motivation-ids.json` (six stakeholders, driver, goal, outcome, requirement). Do not create second copies of those names.
- Fact freeze is `docs/plant-brief.md`; do not invent WMS, TMS, data lake, ERP replacement, second site, or MES rewrite.
- Named as-is systems (MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate) are ownership/context wording for capability boundaries only; they are not modelled as application elements in this job.
- User approval of this plan before any create/update/delete via MCP.
- Capability names chosen here should be reusable on later views without rename churn.

## Validation Points

- Exactly one new view: **Capability Map**. Motivation Overview left intact; no other new views this job.
- Sales-to-mill capabilities present covering promise, order, mill schedule, and collect in plain language stakeholders can agree on.
- MillOS remains mill capability owner in naming/docs; OrderSight remains sales-facing; no ERP replacement capability invented.
- No new process, application, node, work package, or second-site elements created.
- No duplicate job-01 driver/goal/outcome/requirement/stakeholder elements.
- Plant Manager and Head of Sales can read the map as an agreed capability set for later jobs.
- Offline/live QA: no illegal mixes; schema and compliance checks for created objects when modelling runs.

## Open Questions for User

- Confirm view title stays **Capability Map** (recommended) versus a different signed label.
- Capability naming grain: four top-level capabilities aligned to promise / order / mill schedule / collect (recommended for overview agreement), versus a slightly richer sales-to-mill set if you already have preferred names. Default if approve with no notes: four top-level names, no invented logistics/warehouse/ERP-replacement capabilities.
- Optional: whether Integration Lead appears on the Capability Map (default: omit from this view to keep agreement audience tight; IDs still reused later).

## Confirmation Gate

**No model creates or updates run until you confirm this View Plan.**

Reply with one of:

- **approve** - proceed to capability-map modelling in a later step (specialists: capability-strategy, then light QA, layout, documentation). Motivation specialist skipped (reuse only).
- **revise** - send notes; plan updates and re-check; still no mutations.
- **abort** - stop; summarize learning; no mutations.

## Appendix: Viewpoint Trace

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Capability Map | Plant Manager; Head of Sales | One agreed sales-to-mill capability map | decide (sign Capability Map) | overview | yes | Matrix ranks Capability Map with purpose=decide, abstraction=overview. MCP view-patterns lists capability-map layout (grid/groups). Job outcome is Capability Map only. |
| Capability Map | Operations Planner | Name capabilities that run promise, order, mill schedule, collect | decide | overview | yes | Overview capability set answers which organisational abilities own the chain without modelling processes. |
| Capability Map | MES Owner; CRM Programme Manager | MillOS mill owner; OrderSight sales-facing; no ERP replacement | decide | overview | yes | Capability ownership language records boundary without application-layer draws this job. |

## Organisation-Specific Proposals

None this pass. Standard Capability Map viewpoint covers the stakeholder x concern set for job 2.

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Business Product | Matrix top score from sales tag; product/value offering is not the ask; capability agreement is. |
| Application Cooperation | Needs application components and integration; applications out of scope this job. |
| Motivation | Already delivered as Motivation Overview in job 1; reuse only, do not re-model. |
| Implementation and Migration | Work packages and migration out of freeze. |
| Layered | Cross-layer stack would pull business/app/tech content forbidden this job. |
| Business Process | Processes explicitly out of scope. |
| Project | No work packages this run. |

Matrix run: `helpers/viewpoint_selection_matrix.py` with purpose=decide, abstraction=overview; Capability Map score 4, standard_fit true. Scope filter selected Capability Map only.

## Appendix: Technical Hints

- Target view name: `Capability Map`.
- Viewpoint param when creating view: `capability_map` or MCP-equivalent capability-map key (confirm against live create-view enum at model time; matrix key `capability-map`).
- Layout hint from MCP view-patterns: capability map uses grid; groups for capability domains.
- Concept spine (names only; create after approve): capabilities covering Promise, Order, Mill schedule, Collect along sales-to-mill. Keep names stable for later views. Do not invent WMS/TMS/data-lake/ERP-replacement capabilities.
- Ownership notes in documentation only this job: MillOS owns mill schedule capability; OrderSight stays sales-facing; WorksERP remains works-order/invoice context without replacement.
- Reuse registry seed: load `docs/runs/job-01-motivation-ids.json` registry entries; never recreate those motivation elements.
- Motivation Overview view id (do not modify unless user asks): `id-05f18c92556242fc8ce2a2252fc36867`.
