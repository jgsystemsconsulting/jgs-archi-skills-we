<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hawker Range Systems Job 03 (Range Operations)

Run: job-03. Model: Hawker Range Systems Ltd (job-01 Motivation Overview + job-02 Capability Map present). Fact freeze: `docs/moorfield-brief.md`.
Status: pending confirmation. No MCP mutations until approve.

## Intent Summary

The range cannot show how a tasked sortie becomes a live GCS period. SortieBoard is still the pain. This pass models as-is range floor operations only: task, clear, fly, and recover, with the named roles that run them. Job 1 already holds the motivation spine; job 2 already holds capabilities Task, Clear, Fly, Recover. Do not duplicate those IDs or invent a second motivation set. No new applications, no nodes, no work packages, no second site, no costing, no GroundOS rewrite, and no air-vehicle product or SysML structure. Target deliverable is one view named **Range Operations** showing roles and processes only, with SortieBoard remaining the stated pain in documentation language.

## Stakeholders and Concerns

- **Range Manager** - as-is range floor path from task through recover stays visible without inventing systems or drawing the airframe.
- **Chief Instructor** - instructor-facing clarity on who runs task, clear, fly, recover on the day.
- **Sortie Planner** - tasking step on the operations view; SortieBoard stays the pain, not replaced by a new app.
- **GCS Owner** - live control step (fly) stays role/process language; no GroundOS rewrite and no application components this job.
- **Planning Programme Manager** - planning role present; no programme expansion into apps, nodes, or costing.
- **Integration Lead** - process handoffs stay business-layer; no weapons system, ERP, data lake, or air-vehicle structure.

## Proposed Viewpoints

- **Business Process Cooperation** (standard ArchiMate Business Process Cooperation viewpoint; view name **Range Operations**)
  - Purpose: design the as-is range-floor process chain task → clear → fly → recover and show which named roles perform each step, with SortieBoard kept as the pain (documentation), not as a new application.
  - Stakeholders served: Range Manager, Chief Instructor (floor visibility); Sortie Planner and GCS Owner (tasking vs live control steps); Planning Programme Manager and Integration Lead (scope freeze witnesses).
  - Abstraction: overview.
  - Trace: stakeholder x concern coverage in Appendix: Viewpoint Trace. Scope freezes this job to one view.

## Layers Involved

- Business only: named roles (business roles/actors as needed) and business processes for task, clear, fly, recover and their handoffs.
- Reuse only: job-1 stakeholders (and other motivation IDs if referenced); job-2 capabilities Task, Clear, Fly, Recover by ID. Do not recreate them.
- Explicitly not this job: new application components, technology/physical nodes, implementation work packages, second site, costing, GroundOS rewrite, weapons system, air-vehicle product/SysML structure. Named systems (SortieBoard, GroundOS, AirStack, RangePlan, LinkGate) may appear in documentation text only.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). No creates until approve.
2. **Business specialist** - create business-layer content only: processes for task, clear, fly, recover and assignment of the named roles to those steps. Seed reuse registry from `job-01-motivation-ids.json` (stakeholders) and `job-02-capability-ids.json` (Task/Clear/Fly/Recover capabilities). Do not recreate stakeholders or capabilities. Do not create applications or nodes. Do not model the air vehicle as product structure. Keep SortieBoard as pain in documentation language only.
3. Place content on a single view named **Range Operations** using the Business Process Cooperation viewpoint. Triggering/flow between the four processes and assignment from roles as needed for handoffs; optional light link to existing capabilities by reuse ID only if it clarifies realization without duplicating caps.
4. **Model QA** (light) - structural checks for this view; confirm no new apps/nodes/work packages; confirm no duplicate stakeholders or capabilities; confirm task/clear/fly/recover present.
5. **Layout** - overview process chain fit for Range Manager and Chief Instructor.
6. **Documentation** - short rationale and completion summary; stop. Later SOAM jobs handle application and technology.

## Dependencies

- Open model is Hawker Range Systems Ltd with job-1 and job-2 content: 14 elements, 9 relationships, 2 views (**Motivation Overview** `id-02bfe33f26d844a1a34a314a40a400c0`, **Capability Map** `id-6967b8a5125d46e1b6ba0edbf9b9539b`).
- Reuse registry seed: `docs/runs/moorfield/job-01-motivation-ids.json` (six stakeholders + motivation spine) and `docs/runs/moorfield/job-02-capability-ids.json` (Task, Clear, Fly, Recover capability IDs).
- Fact freeze is `docs/moorfield-brief.md`; named systems inform wording only; no application elements this job.
- Hard freeze: no new applications; SortieBoard stays the pain; no air-vehicle product structure; no GroundOS rewrite; no work packages, second site, or costing.
- User approval of this plan before any create/update/delete via MCP.

## Validation Points

- Exactly one new view: **Range Operations**. Motivation Overview and Capability Map unchanged.
- Task, clear, fly, and recover present as process behaviour on the view (names plain and stable).
- Job-1 stakeholders reused by ID; job-2 capabilities reused by ID if shown; no second stakeholder or capability set.
- No new application, node, work package, weapons-system, or air-vehicle product-structure elements created.
- SortieBoard remains the pain in documentation (not drawn as a replacement application).
- Documentation fields are not a restatement of the element name.
- Offline/live QA: schema and compliance checks for created objects when modelling runs.

## Done When

Stop rule: named-deliverable

Pass checks:
- View named exactly Range Operations
- Task, clear, fly, and recover are present
- Job 1 stakeholders and job 2 capabilities reused by ID; no duplicates
- No new applications
- SortieBoard stays the pain
- No air-vehicle product structure
- Documentation fields are not a restatement of the element name
- No MCP mutations before View Plan approve

MUST NOT:
- Duplicate job-1 stakeholders or motivation spine
- Duplicate job-2 Capability elements Task / Clear / Fly / Recover
- Create applications, nodes, or work packages
- GroundOS rewrite or RangePlan-as-GCS / RangePlan-as-AirStack
- Invent weapons system, ERP, data lake, or air-vehicle SysML/product structure
- Second site or costing content

## Open Questions for User

- None blocking the frozen operations scope. Confirm view title stays **Range Operations** (required by job prompt).
- Process element names: default plain **Task**, **Clear**, **Fly**, **Recover** as BusinessProcess (distinct elements from job-2 Capabilities of the same labels). Approve defaults, or supply preferred process labels on approve so capability vs process collision is explicit in docs.
- Whether to place job-2 capability IDs on Range Operations for realization hints this job, or keep the view roles+processes only (recommended: roles+processes only; capability IDs stay in registry for later trace).

## Confirmation Gate

**No model creates or updates run until you confirm this View Plan.**

Reply with one of:

- **approve** - proceed to business-layer modelling in a later step (specialists: business, then light QA, layout, documentation). Reuse job-1 stakeholders and job-2 capabilities; no new apps; SortieBoard stays the pain.
- **revise** - send notes; plan updates and re-check; still no mutations.
- **abort** - stop; summarize learning; no mutations.

## Appendix: Viewpoint Trace

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Business Process Cooperation | Range Manager; Chief Instructor | As-is range floor: task, clear, fly, recover with named roles | design | overview | yes | MCP view-patterns: Business Process Cooperation for process interactions and handoffs. Recipes index routes process-flow/handoffs to behaviour-process-flow family. Matrix ranks Business Process highly when concerns include processes and roles (score 4–5). Job scope is one Range Operations view only. |
| Business Process Cooperation | Sortie Planner; GCS Owner | Tasking vs live control steps; SortieBoard remains the pain; no new applications | design | overview | yes | Process chain shows tasking-to-live handoff in business language without application components. Pain stays documentation, not a drawn app. |
| Business Process Cooperation | Planning Programme Manager; Integration Lead | No nodes, no air-vehicle product structure, no programme invent | design | overview | yes | Business-layer-only viewpoint keeps freeze; rejected app/tech/migration viewpoints cover out-of-scope concerns. |

## Organisation-Specific Proposals

None this pass. Standard Business Process Cooperation viewpoint covers the stakeholder x concern set for job 3. View title **Range Operations** is the signed deliverable name on that viewpoint.

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Application Cooperation | Matrix high on design/overview; needs application components; no new applications this job. |
| Application Structure | Application concern; apps out of scope. |
| Application Usage | Would pull applications into the view; forbidden this job. |
| Motivation | Job 1 already delivered Motivation Overview; do not duplicate. |
| Capability Map | Job 2 already delivered Capability Map; reuse caps by ID, do not redraw the map. |
| Implementation and Migration | Work packages and migration out of freeze. |
| Technology / Physical | Nodes and facilities are job 5; explicitly out. |
| Business Product | Product/value offering and air-vehicle product structure out of freeze. |
| Layered | Cross-layer stack would pull app/tech content forbidden this job. |
| Organization | Structure-only roles without the task-clear-fly-recover process chain would miss the primary concern. |

Matrix runs: `helpers/viewpoint_selection_matrix.py` with purpose=design, abstraction=overview|detail, concerns including processes/roles; Business Process score 4–5, standard_fit true. Scope filter selected Business Process Cooperation only; view name fixed to Range Operations.

## Appendix: Technical Hints

- Target view name: `Range Operations`.
- Viewpoint param when creating view: business_process_cooperation / Business Process Cooperation per MCP patterns.
- Reuse registry seed: `job-01-motivation-ids.json` (stakeholders + motivation spine); `job-02-capability-ids.json` (Task `id-637e89c75e944169983f389d7a572f98`, Clear `id-97ebdecf31914a67bb2dbd87f3229ddb`, Fly `id-03db6547aef1422db55f7e1277e94923`, Recover `id-44a1e398965248e8a79831ea7cc78298`).
- Create after approve (names only): BusinessProcess for Task, Clear, Fly, Recover (new IDs; not the capability IDs); BusinessRole or reuse Stakeholder placement for Range Manager, Chief Instructor, GCS Owner, Planning Programme Manager, Sortie Planner, Integration Lead as required by assignment.
- Do not create ApplicationComponent for AirStack/GroundOS/RangePlan/SortieBoard/LinkGate in this job.
- Naming policy: title-collapse-v1; process labels default Task/Clear/Fly/Recover with docs that distinguish process vs job-2 capability.
- SortieBoard: documentation pain only; no element required unless user revises.
