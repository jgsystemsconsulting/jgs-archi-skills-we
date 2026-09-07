<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hatherley Plate Job 01 (Motivation Overview)

Run: job-01. Model: Hatherley Plate seed (empty). Fact freeze: `docs/plant-brief.md`.
Status: pending user confirmation. No model mutations until approve.

## Intent Summary

Promised plate dates do not match mill reality at Hatherley Works. Sales tracks customer promises in PromiseSheet while the mill schedule lives in MillOS; OrderSight is funded only to fix visibility. This pass models drivers, goals, outcomes, and the hard requirement that OrderSight must not swallow MillOS. Capabilities, processes, applications, nodes, work packages, second site, costing, and MES rewrite stay out of scope. Target deliverable is one signed Motivation Overview for Plant Manager and Head of Sales that states shared order identity as desired state and keeps OrderSight sales-facing.

## Stakeholders and Concerns

- **Plant Manager** - answer "is this order on the mill this week?" without PromiseSheet; keep mill systems under plant control.
- **Head of Sales** - same weekly-on-mill answer for customer promises; stop dual tracking in PromiseSheet.
- **MES Owner** - MillOS remains the mill system of record for schedule; OrderSight must not be drawn as its replacement.
- **CRM Programme Manager** - OrderSight stays sales-facing visibility scope; funded fix must not expand into mill rewrite.
- **Operations Planner** - one order identity from promise through to schedule so plan and promise stop diverging.
- **Integration Lead** - shared identity across systems without merging MillOS into OrderSight (boundary constraint for later jobs).


## Proposed Viewpoints

- **Motivation** (standard ArchiMate Motivation viewpoint; view name **Motivation Overview**)
  - Purpose: decide and sign the why - driver (promise vs mill reality), goal (shared order identity promise-to-schedule), outcome (weekly-on-mill answer without PromiseSheet), requirement (OrderSight must not swallow MillOS).
  - Stakeholders served: Plant Manager, Head of Sales (signatories); MES Owner and CRM Programme Manager (boundary witnesses); Operations Planner and Integration Lead (identity and boundary concerns).
  - Abstraction: overview.
  - Trace: stakeholder x concern coverage in Appendix: Viewpoint Trace. Scope freezes this job to one view.

## Layers Involved

- Motivation only (why we care: drivers, goals, outcomes, requirements, stakeholders).
- Explicitly not this job: strategy/capability maps, business processes, application components, technology/physical nodes, implementation work packages.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). No creates until approve.
2. **Motivation specialist** - create Motivation-layer content only for the frozen spine: driver, goal, outcome, OrderSight-must-not-swallow-MillOS requirement, and stakeholder elements needed to show ownership of those concerns. Prefer plain names from the brief. Do not create capabilities, processes, applications, or nodes.
3. Place content on a single view named **Motivation Overview** using the Motivation viewpoint.
4. **Model QA** (light) - structural checks only for this view; no cross-layer invent.
5. **Layout** - overview layout fit for Plant Manager and Head of Sales sign-off.
6. **Documentation** - short rationale and completion summary; stop. Later SOAM jobs handle other layers.

## Dependencies

- Open model is the empty Hatherley Plate seed (`elementCount=0`, `viewCount=0` at plan time).
- Fact freeze is `docs/plant-brief.md`; do not invent WMS, TMS, data lake, ERP replacement, second site, or MES rewrite.
- Named as-is systems (MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate) are context for wording the requirement only; they are not modelled as application elements in this job.
- User approval of this plan before any create/update/delete via MCP.
- Job 1 complete Motivation Overview before any later layer jobs reuse its IDs.

## Validation Points

- Exactly one view: **Motivation Overview**. No other views this job.
- Motivation spine present in plain language: driver, goal, outcome, requirement (OrderSight must not swallow MillOS).
- Shared order identity expressed as desired state (goal/outcome language), not as a merged system blob.
- No capability, process, application, node, work package, or second-site elements created.
- Plant Manager and Head of Sales can read the view as a signable why-statement without PromiseSheet as the answer path.
- Offline/live QA: no illegal motivation mixes; schema and compliance checks for created objects when modelling runs.

## Open Questions for User

- None blocking the frozen spine. Confirm view title stays **Motivation Overview** (recommended) versus a different signed label.
- Optional later (out of this job): which stakeholder elements to show beyond Plant Manager and Head of Sales if the diagram feels crowded - default is include all six roles lightly or only the two signatories plus MES Owner / CRM Programme Manager as boundary witnesses. Preference?

## Confirmation Gate

**No model creates or updates run until you confirm this View Plan.**

Reply with one of:

- **approve** - proceed to motivation-only modelling in a later step (specialists: motivation, then light QA, layout, documentation).
- **revise** - send notes; plan updates and re-check; still no mutations.
- **abort** - stop; summarize learning; no mutations.

## Appendix: Viewpoint Trace

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Motivation | Plant Manager; Head of Sales | Answer "is this order on the mill this week?" without PromiseSheet | decide (sign Motivation Overview) | overview | yes | MCP view-patterns lists Motivation for goals, requirements, stakeholder concerns. Job scope is motivation spine only. |
| Motivation | Operations Planner; Integration Lead | Shared order identity from promise to schedule | decide | overview | yes | Goal/outcome language covers identity as desired state without modelling processes or apps. |
| Motivation | MES Owner; CRM Programme Manager | OrderSight must not swallow MillOS; OrderSight stays sales-facing | decide | overview | yes | Requirement element on Motivation viewpoint records the hard freeze without application-layer draws. |

## Organisation-Specific Proposals

None this pass. Standard Motivation viewpoint covers the stakeholder x concern set for job 1.

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Business Product | Matrix top score from sales tag; product/value offering out of job-1 scope. |
| Application Cooperation | Needs application components and integration; applications out of scope this job. |
| Capability Map | Capabilities explicitly out of scope. |
| Implementation and Migration | Work packages and migration out of freeze. |
| Layered | Cross-layer stack would pull business/app/tech content forbidden this job. |
| Business Process | Processes out of scope; detail level wrong for executive sign-off. |
| Project | No work packages this run. |

Matrix run: `helpers/viewpoint_selection_matrix.py` with purpose=decide, abstraction=overview; Motivation score 4, standard_fit true. Scope filter selected Motivation only.

## Appendix: Technical Hints

- Target view name: `Motivation Overview`.
- Viewpoint param when creating view: `motivation` (per MCP archimate-view-patterns).
- Concept spine (names only; create after approve): Driver "Promised plate dates do not match mill reality"; Goal "Sales and mill share one order identity from promise to schedule"; Outcome "Plant Manager and Head of Sales answer on-mill-this-week without PromiseSheet"; Requirement "OrderSight must not swallow MillOS".
- Stakeholder elements as needed for the overview; do not add ApplicationComponent for MillOS/OrderSight in this job.
- Reuse registry: seed empty (model empty at plan time).

