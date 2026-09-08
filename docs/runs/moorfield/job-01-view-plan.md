<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hawker Range Systems Job 01 (Motivation Overview)

Run: job-01. Model: Hawker Range Systems Ltd seed (empty). Fact freeze: `docs/moorfield-brief.md`.
Status: approved. Specialists run (motivation, model-qa light, layout, documentation).

## Intent Summary

Promised sortie times do not match what Moorfield Range can fly. Instructors track the day in SortieBoard while the live sortie runs on GroundOS; RangePlan is funded only to fix visibility. This pass models drivers, goals, outcomes, and the hard requirement that RangePlan must not swallow AirStack or GroundOS. Capabilities, processes, applications, nodes, work packages, second site, costing, GroundOS rewrite, weapons system, and air-vehicle product/SysML structure stay out of scope. Target deliverable is one signed Motivation Overview for Range Manager and Chief Instructor that states shared sortie identity as desired state and keeps RangePlan planning-facing, not the GCS and not the airborne computer.

## Stakeholders and Concerns

- **Range Manager** - answer "is this sortie on the range this morning?" without SortieBoard; keep range control of live systems.
- **Chief Instructor** - same morning-on-range answer for instructors; stop dual tracking in SortieBoard.
- **GCS Owner** - GroundOS remains the live GCS system of record; RangePlan must not be drawn as its replacement.
- **Planning Programme Manager** - RangePlan stays planning-facing visibility scope; funded fix must not expand into GroundOS or AirStack rewrite.
- **Sortie Planner** - one sortie identity from tasking through to live GCS so plan and flown day stop diverging.
- **Integration Lead** - shared identity across systems without merging GroundOS or AirStack into RangePlan (boundary constraint for later jobs).

## Proposed Viewpoints

- **Motivation** (standard ArchiMate Motivation viewpoint; view name **Motivation Overview**)
  - Purpose: decide and sign the why - driver (promised sortie times vs range reality), goal (shared sortie identity tasking-to-live-GCS), outcome (morning-on-range answer without SortieBoard), requirement (RangePlan must not swallow AirStack or GroundOS).
  - Stakeholders served: Range Manager, Chief Instructor (signatories); GCS Owner and Planning Programme Manager (boundary witnesses); Sortie Planner and Integration Lead (identity and boundary concerns).
  - Abstraction: overview.
  - Trace: stakeholder x concern coverage in Appendix: Viewpoint Trace. Scope freezes this job to one view.

## Layers Involved

- Motivation only (why we care: drivers, goals, outcomes, requirements, stakeholders).
- Explicitly not this job: strategy/capability maps, business processes, application components, technology/physical nodes, implementation work packages, air-vehicle product structure.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). No creates until approve.
2. **Motivation specialist** - create Motivation-layer content only for the frozen spine: driver, goal, outcome, RangePlan-must-not-swallow-AirStack-or-GroundOS requirement, and stakeholder elements needed to show ownership of those concerns. Prefer plain names from the brief. Do not create capabilities, processes, applications, or nodes. Do not model the air vehicle as product structure.
3. Place content on a single view named **Motivation Overview** using the Motivation viewpoint.
4. **Model QA** (light) - structural checks only for this view; no cross-layer invent.
5. **Layout** - overview layout fit for Range Manager and Chief Instructor sign-off.
6. **Documentation** - short rationale and completion summary; stop. Later SOAM jobs handle other layers.

## Dependencies

- Open model is the empty Hawker Range Systems Ltd seed (`elementCount=0`, `viewCount=0` at plan time).
- Fact freeze is `docs/moorfield-brief.md`; do not invent a weapons system, ERP, data lake, second site, GroundOS rewrite, or air-vehicle SysML structure.
- Named as-is systems (AirStack, GroundOS, SortieBoard, RangePlan, LinkGate) are context for wording the requirement only; they are not modelled as application elements in this job.
- User approval of this plan before any create/update/delete via MCP.
- Job 1 complete Motivation Overview before any later layer jobs reuse its IDs.

## Validation Points

- Exactly one view: **Motivation Overview**. No other views this job.
- Motivation spine present in plain language: driver, goal, outcome, requirement (RangePlan must not swallow AirStack or GroundOS).
- Shared sortie identity expressed as desired state (goal/outcome language), not as a merged system blob.
- No capability, process, application, node, work package, weapons-system, or air-vehicle product-structure elements created.
- Range Manager and Chief Instructor can read the view as a signable why-statement without SortieBoard as the answer path.
- Offline/live QA: no illegal motivation mixes; schema and compliance checks for created objects when modelling runs.

## Open Questions for User

- None blocking the frozen spine. Confirm view title stays **Motivation Overview** (recommended) versus a different signed label.
- Optional later (out of this job): which stakeholder elements to show beyond Range Manager and Chief Instructor if the diagram feels crowded - default is include all six roles lightly or only the two signatories plus GCS Owner / Planning Programme Manager as boundary witnesses. Preference?

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
| Motivation | Range Manager; Chief Instructor | Answer "is this sortie on the range this morning?" without SortieBoard | decide (sign Motivation Overview) | overview | yes | MCP view-patterns lists Motivation for goals, requirements, and stakeholder concerns. Job scope is motivation spine only. |
| Motivation | Sortie Planner; Integration Lead | Shared sortie identity from tasking to live GCS | decide | overview | yes | Goal/outcome language covers identity as desired state without modelling processes or apps. |
| Motivation | GCS Owner; Planning Programme Manager | RangePlan must not swallow AirStack or GroundOS; RangePlan stays planning-facing | decide | overview | yes | Requirement element on Motivation viewpoint records the hard freeze without application-layer draws. |

## Organisation-Specific Proposals

None this pass. Standard Motivation viewpoint covers the stakeholder x concern set for job 1.

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Application Cooperation | Matrix tied on purpose/abstraction; needs application components and integration; applications out of scope this job. |
| Business Product | Product/value offering and air-vehicle product structure out of job-1 freeze. |
| Capability Map | Capabilities explicitly out of scope. |
| Implementation and Migration | Work packages and migration out of freeze. |
| Layered | Cross-layer stack would pull business/app/tech content forbidden this job. |
| Project | No work packages this run. |
| Business Process | Processes out of scope; detail level wrong for executive sign-off. |

Matrix run: `helpers/viewpoint_selection_matrix.py` with purpose=decide, abstraction=overview; Motivation score 4, standard_fit true. Scope filter selected Motivation only.

## Appendix: Technical Hints

- Target view name: `Motivation Overview`.
- Viewpoint param when creating view: `motivation` (per MCP archimate-view-patterns).
- Concept spine (names only; create after approve): Driver "Promised sortie times do not match what the range can fly"; Goal "Instructors and the range share one sortie identity from tasking to live GCS"; Outcome "Range Manager and Chief Instructor answer on-range-this-morning without SortieBoard"; Requirement "RangePlan must not swallow AirStack or GroundOS".
- Stakeholder elements as needed for the overview; do not add ApplicationComponent for AirStack/GroundOS/RangePlan/SortieBoard/LinkGate in this job.
- Reuse registry: seed empty (model empty at plan time).
