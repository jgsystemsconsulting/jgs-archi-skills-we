<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hawker Range Systems Job 04 (Application Support)

Run: job-04. Model: Hawker Range Systems Ltd (job-01 Motivation Overview + job-02 Capability Map + job-03 Range Operations present). Fact freeze: `docs/moorfield-brief.md`.
Status: approved. Specialists executed.

## Intent Summary

Instructors, GCS, and integration cannot see which systems hold tasking, live control, and the airborne computer. The planning programme must not be drawn as the GCS or as AirStack. This pass models as-is application support only for the five named systems: AirStack, GroundOS, SortieBoard, RangePlan, and LinkGate, and how they support the operations already on Range Operations. Hard freeze: RangePlan, AirStack, and GroundOS stay separate applications; shared sortie identity is not one merged blob; LinkGate bridges RangePlan tasking to GroundOS and does not talk to the air vehicle (document that boundary; no equipment this job). No nodes, work packages, second site, costing, GroundOS rewrite, ERP replacement, weapons system, data lake, or air-vehicle SysML/product structure. Target deliverable is one view named **Application Support** using the same system names from the brief.

## Stakeholders and Concerns

- **GCS Owner** - GroundOS remains the live-control application; not swallowed by RangePlan; AirStack stays airborne, not redrawn as planning software.
- **Planning Programme Manager** - RangePlan stays planning-facing and separate; programme must not be drawn as GCS or AirStack; funded for sortie visibility only.
- **Integration Lead** - five named apps present and distinct; LinkGate is the bridge from RangePlan tasking to GroundOS only; no air-vehicle talk from LinkGate; no invented ERP/data lake/weapons system.
- **Range Manager** - can see which systems hold tasking vs live control vs airborne computer without SortieBoard as the only answer.
- **Chief Instructor** - same application map for instructor-facing clarity on where sortie identity lives across systems (shared, not merged).

## Proposed Viewpoints

- **Application Cooperation** (standard ArchiMate Application Cooperation viewpoint; view name **Application Support**)
  - Purpose: design the as-is application landscape so AirStack, GroundOS, SortieBoard, RangePlan, and LinkGate stay separate, show cooperation/flows that carry shared sortie identity (not one blob), and show LinkGate bridging RangePlan tasking to GroundOS without air-vehicle contact.
  - Stakeholders served: GCS Owner and Planning Programme Manager (ownership boundaries); Integration Lead (interfaces and freeze); Range Manager and Chief Instructor (which system holds what).
  - Abstraction: overview.
  - Trace: stakeholder x concern coverage in Appendix: Viewpoint Trace. Scope freezes this job to one view.

## Layers Involved

- Application: the five named application components (and light interfaces/flows or data objects only if needed to show shared sortie identity and LinkGate bridge without inventing new product families).
- Reuse only: job-1 stakeholders/motivation IDs; job-2 capabilities; job-3 business processes and roles by ID when linking support to operations. Do not recreate them.
- Explicitly not this job: technology/physical nodes or equipment, implementation work packages, second site, costing, GroundOS rewrite, weapons system, ERP, data lake, air-vehicle product/SysML structure. LinkGate air-vehicle non-talk is documentation language (and optional note), not equipment.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). No creates until approve.
2. **Application specialist** - create application-layer content only for AirStack, GroundOS, SortieBoard, RangePlan, and LinkGate as separate ApplicationComponents (same names). Seed reuse registry from `job-01-motivation-ids.json`, `job-02-capability-ids.json`, and `job-03-operations-ids.json`. Do not recreate stakeholders, capabilities, processes, or roles. Do not create nodes or equipment. Do not invent weapons system, ERP, data lake, or air-vehicle structure. Keep RangePlan, AirStack, and GroundOS as three distinct components. Model shared sortie identity as cooperation/flow or data object language, not a merge. LinkGate bridges RangePlan → GroundOS only; document that LinkGate does not talk to the air vehicle.
3. Place content on a single view named **Application Support** using the Application Cooperation viewpoint. Optional serving/flow links to existing job-3 processes (reuse IDs) only if they clarify support without redrawing Range Operations. Prefer light cross-layer edges over duplicating the process chain.
4. **Model QA** (light) - structural checks; confirm five named apps present and separate; confirm no nodes/work packages/weapons/ERP/data lake/air-vehicle structure; confirm no duplicate motivation/capability/process IDs.
5. **Layout** - overview fit for GCS Owner, Planning Programme Manager, and Integration Lead.
6. **Documentation** - short rationale and completion summary; LinkGate non-air-vehicle boundary in docs; stop. Later SOAM job handles technology/physical.

## Dependencies

- Open model is Hawker Range Systems Ltd with job-1/2/3 content: 22 elements, 16 relationships, 3 views (**Motivation Overview** `id-02bfe33f26d844a1a34a314a40a400c0`, **Capability Map** `id-6967b8a5125d46e1b6ba0edbf9b9539b`, **Range Operations** `id-782395c6d18347a9a24da626f81ee275`).
- Reuse registry seed: `docs/runs/moorfield/job-01-motivation-ids.json`, `job-02-capability-ids.json`, `job-03-operations-ids.json` (processes Task/Clear/Fly/Recover and on-canvas roles).
- Fact freeze is `docs/moorfield-brief.md`; system names are fixed.
- Hard freeze: RangePlan, AirStack, GroundOS stay separate; shared sortie identity not one merged blob; LinkGate does not talk to the air vehicle (document; no equipment this job); no nodes, work packages, second site, costing, GroundOS rewrite, weapons system, ERP, data lake, air-vehicle SysML.
- User approval of this plan before any create/update/delete via MCP.

## Validation Points

- Exactly one new view: **Application Support**. Prior three views unchanged in content intent.
- AirStack, GroundOS, SortieBoard, RangePlan, and LinkGate present as separate application elements (same names).
- RangePlan, AirStack, and GroundOS remain three distinct components (not collapsed).
- Shared sortie identity shown without merging the three into one application blob.
- LinkGate role is RangePlan tasking → GroundOS bridge; non-talk to air vehicle stated in documentation (no equipment element this job).
- No weapons system, ERP, data lake, air-vehicle product/SysML structure, nodes, or work packages created.
- Documentation fields are not a restatement of the element name.
- Offline/live QA: schema and compliance checks for created objects when modelling runs.

## Done When

Stop rule: named-deliverable

Pass checks:
- View named exactly Application Support
- AirStack, GroundOS, SortieBoard, RangePlan, and LinkGate are present
- RangePlan, AirStack, and GroundOS remain separate
- No weapons system, ERP, data lake, or air-vehicle structure
- Documentation fields are not a restatement of the element name
- No MCP mutations before View Plan approve
- Job-1/2/3 IDs reused; no duplicate motivation, capability, process, or role sets

MUST NOT:
- Merge RangePlan, AirStack, and GroundOS into one application
- Draw RangePlan as the GCS or as the airborne computer
- Create nodes, equipment, or work packages this job
- Invent weapons system, ERP, data lake, or air-vehicle SysML/product structure
- GroundOS rewrite or second site / costing content
- Duplicate job-1 stakeholders/motivation, job-2 capabilities, or job-3 processes/roles

## Open Questions for User

- None blocking the frozen application scope. Confirm view title stays **Application Support** (required by job prompt).
- Shared sortie identity representation: default a single Application Data Object (or equivalent plain data element) named for sortie identity, flowed/accessed among the apps that share it, without merging app components. Approve default, or prefer flow-only labels with no data object.
- Whether to place light Serving links from apps to job-3 processes (Task/Clear/Fly/Recover by reuse ID) on Application Support, or keep the view application-cooperation only (recommended: light serving to processes if it clarifies support without redrawing Range Operations).
- SortieBoard: keep as ApplicationComponent (as-is pain spreadsheet system) per brief named systems list (recommended), vs documentation-only pain with no component (would fail the five-name presence check).

## Confirmation Gate

**No model creates or updates run until you confirm this View Plan.**

Reply with one of:

- **approve** - proceed to application-layer modelling in a later step (specialists: application, then light QA, layout, documentation). Reuse job-1/2/3 IDs; five named apps separate; LinkGate bridge only; no nodes/equipment this job.
- **revise** - send notes; plan updates and re-check; still no mutations.
- **abort** - stop; summarize learning; no mutations.

## Appendix: Viewpoint Trace

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Application Cooperation | GCS Owner; Planning Programme Manager | RangePlan, AirStack, GroundOS stay separate; planning not drawn as GCS or AirStack | design | overview | yes | MCP view-patterns: Application Cooperation for how applications integrate and exchange data. Matrix ranks Application Cooperation top (score 6) on purpose=design, abstraction=overview, concerns interfaces/cooperation. One deliverable view **Application Support**. |
| Application Cooperation | Integration Lead | LinkGate bridges RangePlan tasking to GroundOS; does not talk to air vehicle; no invented ERP/data lake/weapons | design | overview | yes | Cooperation viewpoint shows bridge flows and keeps five components distinct; air-vehicle non-talk stays documentation this job (no equipment). |
| Application Cooperation | Range Manager; Chief Instructor | Which systems hold tasking, live control, airborne computer; shared sortie identity not one merged blob | design | overview | yes | Overview application map answers ownership without merging apps; shared identity as cooperation/data, not a single app blob. |

## Organisation-Specific Proposals

None this pass. Standard Application Cooperation viewpoint covers the stakeholder x concern set for job 4. View title **Application Support** is the signed deliverable name on that viewpoint.

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Application Structure | Strong on detail structure; job needs cooperation/flows and shared identity more than internal composition; overview cooperation wins matrix for this intent. |
| Application Usage | Useful for process support; secondary. Single-view freeze prefers Application Cooperation; optional light serving edges can still reference job-3 processes without switching viewpoint. |
| Business Process Cooperation | Job 3 already delivered Range Operations; reuse processes by ID, do not redraw. |
| Capability Map | Job 2 already delivered; reuse caps by ID only. |
| Motivation | Job 1 already delivered Motivation Overview. |
| Technology / Physical | Nodes and equipment are job 5; explicitly out. |
| Implementation and Migration | Work packages and migration out of freeze. |
| Layered | Cross-layer stack would pull tech content forbidden this job. |
| Information Structure | Data-only view would miss application ownership freeze for the five named systems. |

Matrix runs: `helpers/viewpoint_selection_matrix.py` with purpose=design, abstraction=overview, concerns applications/interfaces/cooperation/data/processes; Application Cooperation score 6, standard_fit true. Scope filter selected Application Cooperation only; view name fixed to Application Support.

## Appendix: Technical Hints

- Target view name: `Application Support`.
- Viewpoint param when creating view: application_cooperation / Application Cooperation per MCP patterns.
- Reuse registry seed: job-01 motivation/stakeholders; job-02 capabilities Task/Clear/Fly/Recover; job-03 processes and roles (`job-03-operations-ids.json`).
- Create after approve (names only): ApplicationComponent AirStack, GroundOS, SortieBoard, RangePlan, LinkGate (new IDs; five separate). Optional ApplicationDataObject (or brief-approved equivalent) for shared sortie identity. Flows/serving: RangePlan → LinkGate → GroundOS; GroundOS owns live; AirStack airborne; SortieBoard as-is pain spreadsheet app.
- Do not create Node, Equipment, Device, or Work Package this job.
- Naming policy: title-collapse-v1; system names exact from brief.
- LinkGate documentation must state no air-vehicle interface.
- Hard freeze requirement already in model: RangePlan must not swallow AirStack or GroundOS (`id-ec762c52e806466fa6eded750caa15e0`); do not recreate.
