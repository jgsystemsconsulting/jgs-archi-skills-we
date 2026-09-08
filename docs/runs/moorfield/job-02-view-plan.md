<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hawker Range Systems Job 02 (Capability Map)

Run: job-02. Model: Hawker Range Systems Ltd (job-01 motivation present). Fact freeze: `docs/moorfield-brief.md`.
Status: pending confirmation. No MCP mutations until approve.

## Intent Summary

Instructors, the range, and the planning programme cannot see which capabilities actually run tasking, clearance, live GCS, and recover on the path from tasking to live sortie. Job 1 already captured why shared sortie visibility matters; this pass does not restate or duplicate that motivation spine. Stakeholders need one Capability Map they can agree on, with GroundOS as live-sortie capability owner, AirStack airborne, and RangePlan planning-facing only. No GroundOS rewrite, no new processes or applications, no nodes or work packages. Target deliverable is a single view named Capability Map on the current model, reusing job-1 motivation IDs and keeping capability names stable for later SOAM views.

## Stakeholders and Concerns

- **Range Manager** - one agreed capability map for tasking-to-live-sortie so range control stays clear without inventing new systems.
- **Chief Instructor** - same map for instructor-facing clarity on what capabilities run the day from tasking through recover.
- **GCS Owner** - GroundOS remains the live-sortie capability owner; map must not imply a GroundOS rewrite or RangePlan as GCS.
- **Planning Programme Manager** - RangePlan stays planning-facing; capability map must not expand programme scope into live control or airborne computer.
- **Sortie Planner** - tasking and planning capabilities visible and named consistently for later views; no second set of motivation drivers.

## Proposed Viewpoints

- **Capability Map** (standard ArchiMate Capability Map viewpoint; view name **Capability Map**)
  - Purpose: decide and agree which strategy-layer capabilities cover tasking, clearance, live GCS, recover (and adjacent planning/airborne ownership) on the tasking-to-live-sortie path.
  - Stakeholders served: Range Manager, Chief Instructor (agreement); GCS Owner and Planning Programme Manager (ownership boundaries); Sortie Planner (stable names for later views).
  - Abstraction: overview.
  - Trace: stakeholder x concern coverage in Appendix: Viewpoint Trace. Scope freezes this job to one view.

## Layers Involved

- Strategy / capability map (capabilities that run tasking-to-live-sortie; ownership language only).
- Motivation reuse only: job-1 Motivation Overview elements and IDs stay as-is; do not duplicate drivers/goals/outcomes/requirements.
- Explicitly not this job: new business processes, application components, technology/physical nodes, implementation work packages, second site, costing, GroundOS rewrite, weapons system, air-vehicle product/SysML structure.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). No creates until approve.
2. **Capability-strategy specialist** - create Capability elements only for the tasking-to-live-sortie map. Prefer plain names that will stick on later views. Seed reuse registry from `job-01-motivation-ids.json`; do not recreate motivation elements. Do not create processes, applications, or nodes. Do not invent weapons system, ERP, data lake, or air-vehicle structure.
3. Place content on a single view named **Capability Map** using the Capability Map viewpoint. Optional light association or serving-style links only if needed to show ownership boundaries in plain capability language; do not draw application components.
4. **Model QA** (light) - structural checks for this view; confirm no duplicate motivation; confirm no apps/nodes/work packages.
5. **Layout** - overview grid/groups fit for Range Manager and Chief Instructor agreement.
6. **Documentation** - short rationale and completion summary; stop. Later SOAM jobs handle operations/application/technology.

## Dependencies

- Open model is Hawker Range Systems Ltd with job-1 content: 10 motivation elements, 9 relationships, 1 view **Motivation Overview** (`id-02bfe33f26d844a1a34a314a40a400c0`).
- Reuse registry seed: `docs/runs/moorfield/job-01-motivation-ids.json` (all six stakeholders, driver, goal, outcome, requirement IDs).
- Fact freeze is `docs/moorfield-brief.md`; named systems (AirStack, GroundOS, SortieBoard, RangePlan, LinkGate) inform capability ownership wording only; they are not modelled as application elements in this job.
- Hard freeze: GroundOS owns live sortie; AirStack airborne; RangePlan planning-facing; no GroundOS rewrite; shared capability names if they appear on later views.
- User approval of this plan before any create/update/delete via MCP.

## Validation Points

- Exactly one new view: **Capability Map**. Motivation Overview unchanged.
- Job-1 motivation elements reused by ID; no second driver/goal/outcome/requirement set.
- Capability map covers tasking, clearance, live GCS, and recover on the tasking-to-live-sortie path; ownership language keeps GroundOS live, AirStack airborne, RangePlan planning-facing.
- No process, application, node, work package, weapons-system, or air-vehicle product-structure elements created.
- Documentation fields are not a restatement of the element name.
- Offline/live QA: schema and compliance checks for created objects when modelling runs.


## Done When

Stop rule: named-deliverable

Pass checks:
- View named exactly Capability Map
- Job 1 motivation reused by ID; no second driver/goal/outcome/requirement set
- Capability coverage includes tasking, clearance, live GCS, and recover
- GroundOS live-sortie ownership, AirStack airborne, RangePlan planning-facing preserved in capability language
- Documentation fields are not a restatement of the element name
- No MCP mutations before View Plan approve

MUST NOT:
- Duplicate job-1 motivation spine
- Create processes, applications, nodes, or work packages
- GroundOS rewrite or RangePlan-as-GCS / RangePlan-as-AirStack
- Invent weapons system, ERP, data lake, or air-vehicle SysML/product structure
- Second site or costing content

## Open Questions for User

- None blocking the frozen capability-map scope. Confirm view title stays **Capability Map** (required by job prompt) versus a different signed label.
- Capability naming preference if you want exact labels now (default specialist will use plain tasking / clearance / live GCS / recover plus planning-facing and airborne ownership caps without inventing extra domains). Approve defaults, or supply preferred names on approve.

## Confirmation Gate

**No model creates or updates run until you confirm this View Plan.**

Reply with one of:

- **approve** - proceed to capability-strategy modelling in a later step (specialists: capability-strategy, then light QA, layout, documentation). Motivation IDs reused; no GroundOS rewrite.
- **revise** - send notes; plan updates and re-check; still no mutations.
- **abort** - stop; summarize learning; no mutations.

## Appendix: Viewpoint Trace

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Capability Map | Range Manager; Chief Instructor | One capability map they can agree on for tasking-to-live-sortie | decide | overview | yes | Matrix ranks capability-map with purpose=decide, abstraction=overview (score 4, standard_fit). MCP view-patterns treat Capability map as a grid inventory of capability domains. Job scope is one Capability Map view only. |
| Capability Map | GCS Owner; Planning Programme Manager | GroundOS owns live-sortie capability; AirStack airborne; RangePlan planning-facing; no GroundOS rewrite | decide | overview | yes | Capability ownership language on the map records boundaries without drawing application components this job. |
| Capability Map | Sortie Planner | Stable capability names for later views; reuse job-1 motivation | decide | overview | yes | Overview map fixes names early; motivation IDs come from job-01 registry, not a second motivation viewpoint this pass. |

## Organisation-Specific Proposals

None this pass. Standard Capability Map viewpoint covers the stakeholder x concern set for job 2.

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Motivation | Job 1 already delivered Motivation Overview; duplicating motivation is out of scope. |
| Application Cooperation | Needs application components and integration; applications out of scope this job. |
| Business Product | Product/value offering and air-vehicle product structure out of freeze. |
| Implementation and Migration | Work packages and migration out of freeze. |
| Layered | Cross-layer stack would pull business/app/tech content forbidden this job. |
| Project | No work packages this run. |
| Business Process | Processes explicitly out of scope; detail level wrong for capability agreement. |

Matrix run: `helpers/viewpoint_selection_matrix.py` with purpose=decide, abstraction=overview; Capability Map score 4, standard_fit true. Scope filter selected Capability Map only.

## Appendix: Technical Hints

- Target view name: `Capability Map`.
- Viewpoint param when creating view: capability-map key / Capability Map label per matrix and MCP patterns (grid layout).
- Reuse registry seed: `job-01-motivation-ids.json` (do not recreate those 10 elements).
- Concept spine (names only; create after approve): capabilities covering Tasking, Clearance, Live GCS (GroundOS-owned), Recover; keep Planning-facing (RangePlan) and Airborne (AirStack) ownership visible without application elements.
- Do not create ApplicationComponent for AirStack/GroundOS/RangePlan/SortieBoard/LinkGate in this job.
- Naming policy: title-collapse-v1; same capability names if they appear on later views.
