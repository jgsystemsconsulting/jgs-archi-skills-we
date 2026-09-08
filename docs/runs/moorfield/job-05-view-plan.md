<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# View Plan - Hawker Range Systems Job 05 (Technology and Physical close-out)

Run: job-05. Model: Hawker Range Systems Ltd (jobs 01-04 present). Fact freeze: `docs/moorfield-brief.md`.
Status: pending confirmation. No MCP mutations until approve.

## Intent Summary

Range engineers need hangar, GCS van, comms cabin, and launch equipment on the drawing so RangePlan cannot be mistaken for the GCS or the airborne computer. Motivation, capabilities, range operations, and application support already exist. This pass adds as-is technology and physical facts only: hangar, GCS van, comms cabin, datalink mast, launch equipment on a range-floor node, on-prem app server hosting GroundOS, and LinkGate on a node in the comms cabin. At least one equipment or facility element must be assigned to a node. Then run whole-model traceability, QA, layout, and documentation. Hard freeze: no work packages; RangePlan, AirStack, and GroundOS stay separate applications (reuse job-04 IDs); LinkGate does not talk to the air vehicle; no air-vehicle SysML or product structure; no second site, costing, GroundOS rewrite, weapons system, ERP, or data lake. Target deliverable is one view named **Technology and Physical**, then close-out on the as-is model.

## Stakeholders and Concerns

- **Range Manager** - hangar, range-floor launch equipment, and cabin/van layout visible so floor reality is not abstract software.
- **GCS Owner** - GroundOS hosted on an on-prem app server node; GCS van present; RangePlan still not drawn as the GCS.
- **Integration Lead** - LinkGate on a node inside the comms cabin; datalink mast; LinkGate still does not talk to the air vehicle; no invented extra architecture.
- **Planning Programme Manager** - RangePlan remains planning-facing and separate from GroundOS and AirStack; physical close-out does not expand programme scope into work packages or rewrite.

## Proposed Viewpoints

- **Technology Usage** (standard ArchiMate Technology Usage viewpoint; view name **Technology and Physical**)
  - Purpose: design the as-is deployment of named range-floor facilities, equipment, and nodes, show GroundOS hosted on the on-prem app server node and LinkGate on a node in the comms cabin, and keep application boundaries intact by reusing job-04 app IDs (not recreating them).
  - Stakeholders served: Range Manager (facilities and range-floor equipment); GCS Owner (GroundOS host node and GCS van); Integration Lead (LinkGate node placement and mast); Planning Programme Manager (no programme expansion; apps stay separate).
  - Abstraction: overview.
  - Trace: stakeholder x concern coverage in Appendix: Viewpoint Trace. Scope freezes this job to one new content view; prior four views stay content-intent stable.

## Layers Involved

- Technology and physical: nodes (range-floor, on-prem app server, LinkGate host in comms cabin), facilities (hangar, GCS van, comms cabin as needed), equipment (datalink mast, launch equipment, and any other brief-named gear), assignment of at least one facility or equipment element to a node, and assignment/nesting of GroundOS and LinkGate onto their host nodes.
- Application reuse only: job-04 ApplicationComponents AirStack, GroundOS, SortieBoard, RangePlan, LinkGate by existing IDs. Do not recreate or merge them. AirStack stays the airborne application identity without drawing air-vehicle product structure.
- Close-out (not new architecture layers): cross-layer traceability across the whole as-is model, model QA, layout, and documentation fields.
- Explicitly not this job: work packages, plateaus, migration path, second site, costing, GroundOS rewrite, weapons system, ERP, data lake, air-vehicle SysML/product structure, extra application architecture beyond reuse of the five named apps.

## Modelling Sequence

1. Confirm this View Plan (approve / revise / abort). No creates until approve.
2. **Technology and physical specialist** - create technology/physical content only per brief: Hangar; GCS van; Comms cabin; Datalink mast; Launch equipment on a range-floor node; on-prem app server node hosting GroundOS; LinkGate on a node in the comms cabin. Enforce at least one Assignment of Facility or Equipment to a Node. Seed reuse registry from `job-01-motivation-ids.json`, `job-02-capability-ids.json`, `job-03-operations-ids.json`, and `job-04-application-ids.json`. Reuse GroundOS `id-a3eaf0c0d5b74284a190ac0c70c4830d` and LinkGate `id-23d0ad9fc6be4d2b93b3fabd9f6ca0c9` (and other apps by ID if placed for context). Do not recreate RangePlan, AirStack, or GroundOS. Do not create WorkPackage elements. Do not model air-vehicle product structure. Document that LinkGate does not talk to the air vehicle.
3. Place content on a single view named **Technology and Physical** using the Technology Usage viewpoint. Prefer node containment / assignment for hosting; light associations for mast or cabin adjacency only if needed. Do not redraw Motivation Overview, Capability Map, Range Operations, or Application Support.
4. **Traceability** - whole as-is model cross-layer traces after technology/physical IDs exist (motivation through physical), without inventing migration or work packages.
5. **Model QA** - structural checks; confirm facility/equipment-to-node assignment; confirm RangePlan, AirStack, GroundOS remain three distinct app IDs; confirm zero WorkPackage; confirm no air-vehicle SysML structure; confirm LinkGate non-air-vehicle boundary still holds.
6. **Layout** - overview fit for Range Manager, GCS Owner, and Integration Lead on Technology and Physical; touch other views only if QA/layout requires non-content fixes already in scope.
7. **Documentation** - rationale and completion summary on new elements and the close-out; documentation fields must not merely restate element names; stop.

## Dependencies

- Open model is Hawker Range Systems Ltd: 27 elements, 24 relationships, 4 views (**Motivation Overview** `id-02bfe33f26d844a1a34a314a40a400c0`, **Capability Map** `id-6967b8a5125d46e1b6ba0edbf9b9539b`, **Range Operations** `id-782395c6d18347a9a24da626f81ee275`, **Application Support** `id-5ed7d076bfc449d78537f5468ed476fb`). Snapshot read-only: elementCount 27, viewCount 4, zero Node/Equipment/Facility today.
- Reuse registry seed: `docs/runs/moorfield/job-01-motivation-ids.json`, `job-02-capability-ids.json`, `job-03-operations-ids.json`, `job-04-application-ids.json` (apps: AirStack, GroundOS, SortieBoard, RangePlan, LinkGate).
- Fact freeze is `docs/moorfield-brief.md`; physical list and hard freeze are binding.
- Hard freeze: at least one equipment or facility assigned to a node; no work packages; RangePlan, AirStack, GroundOS stay separate; LinkGate on comms cabin node does not talk to air vehicle; no air-vehicle SysML.
- User approval of this plan before any create/update/delete via MCP.

## Validation Points

- Exactly one new content view: **Technology and Physical**. Prior four views unchanged in content intent.
- Hangar, GCS van, comms cabin, datalink mast, launch equipment, range-floor node, on-prem app server (GroundOS host), and LinkGate host node in the comms cabin are present as modelled elements consistent with the brief.
- At least one Facility or Equipment element has an Assignment (or equivalent valid assignment) to a Node.
- GroundOS assigned/hosted on the on-prem app server node (reuse GroundOS ID).
- LinkGate assigned/hosted on a node in the comms cabin (reuse LinkGate ID); documentation states no air-vehicle interface.
- RangePlan, AirStack, and GroundOS remain three distinct application IDs (no merge, no duplicate creates).
- Zero WorkPackage elements. No weapons system, ERP, data lake, or air-vehicle product/SysML structure.
- Traceability, QA, layout, and documentation complete for close-out.
- Documentation fields are not a restatement of the element name.
- Offline/live QA and compliance checks pass or surface needs-user items only.

## Done When

Stop rule: named-deliverable

Pass checks:
- View named exactly Technology and Physical
- At least one facility or equipment element assigned to a node
- RangePlan, AirStack, and GroundOS remain separate (job-04 IDs reused)
- No work packages
- Trace, QA, layout, and documentation ran
- Model still as-is (no migration invent)
- No air-vehicle product structure
- Documentation fields are not a restatement of the element name
- No MCP mutations before View Plan approve

MUST NOT:
- Merge or recreate RangePlan, AirStack, GroundOS as new IDs
- Draw RangePlan as the GCS or as the airborne computer
- Create WorkPackage elements
- Invent weapons system, ERP, data lake, or air-vehicle SysML/product structure
- Place LinkGate as talking to the air vehicle
- GroundOS rewrite or second site / costing content

## Open Questions for User

- None blocking the frozen physical list. Confirm view title stays **Technology and Physical** (required by job prompt).
- Typing defaults (approve or revise): Hangar, GCS van, Comms cabin as Facility; Datalink mast and Launch equipment as Equipment; range-floor, on-prem app server, and LinkGate host as Node. GCS van remains Facility (vehicle shelter/location), not a substitute for the GroundOS app.
- AirStack placement: default keep AirStack off this canvas as a hosted deployable (no air-vehicle node). Reuse ID only if a minimal off-node reference is needed; do not invent airframe structure.
- Network detail: default light Association between nodes/mast only if needed for readability; no full network inventory.
- Close-out depth: default whole-model trace + QA + layout + documentation after technology/physical; no Implementation and Migration specialist and no work packages.

## Confirmation Gate

**No model creates or updates run until you confirm this View Plan.**

Reply with one of:

- **approve** - proceed to post-approve specialists in order: technology-physical, then traceability, model-qa, layout, documentation. Reuse job-01..04 IDs; physical facts per brief; apps stay separate; no work packages; no air-vehicle SysML.
- **revise** - send notes; plan updates and re-check; still no mutations.
- **abort** - stop; summarize learning; no mutations.

## Appendix: Viewpoint Trace

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Technology Usage | Range Manager; GCS Owner | Hangar, GCS van, range-floor launch equipment, GroundOS on on-prem app server node | design | overview | yes | MCP view-patterns: Technology Usage for deployment of applications onto infrastructure (nodes, devices, assignment). Single deliverable view **Technology and Physical**. |
| Technology Usage | Integration Lead | LinkGate on a node in the comms cabin; datalink mast; LinkGate does not talk to air vehicle; no extra architecture | design | overview | yes | Hosting placement and cabin/mast topology are deployment concerns; air-vehicle non-talk stays documentation and omission of airframe structure. |
| Technology Usage | Planning Programme Manager | RangePlan not drawn as GCS or airborne computer; no work packages; apps stay separate | design | overview | yes | Reuse job-04 app IDs on host nodes only where brief requires (GroundOS, LinkGate); RangePlan/AirStack not swallowed; Implementation and Migration rejected (work packages out). |

## Organisation-Specific Proposals

None this pass. Standard Technology Usage covers the stakeholder x concern set for a single overview deployment view. View title **Technology and Physical** is the signed deliverable name on that viewpoint. Physical and Technology matrix candidates remain supporting tags for facilities/equipment/nodes inside this one view.

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Physical (alone) | Strong on facilities/equipment; weaker on application-to-node hosting for GroundOS/LinkGate. Technology Usage covers both on one canvas. |
| Technology (structure-only) | Good for nodes/infra; Technology Usage better matches app deployment onto nodes per MCP patterns. |
| Implementation and Migration | Work packages and migration explicitly out of freeze. |
| Application Cooperation | Job 4 already delivered Application Support; reuse apps by ID only. |
| Application Structure | Internal app composition not the concern; hosting is. |
| Layered | Would pull full stack redraw; job freezes one technology/physical view plus close-out, not a new landscape stack. |
| Motivation / Capability Map / Business Process Cooperation | Already delivered in jobs 1-3; reuse only. |
| Information Structure | Data-only view misses facilities, equipment, and nodes. |

Matrix runs: `helpers/viewpoint_selection_matrix.py` with purpose=design, abstraction=overview, concerns facilities/equipment/nodes/infrastructure/deployment. Physical and Technology score 4 each (standard_fit true); Implementation and Migration and Motivation also score 4 on purpose/abstraction alone and are rejected by scope (no work packages; motivation already done). Scope filter selects Technology Usage as the MCP-pattern deployment viewpoint for the single named view.

## Appendix: Technical Hints

- Target view name: `Technology and Physical`.
- Viewpoint param when creating view: `technology_usage` / Technology Usage per MCP patterns; recipe family technology-deployment (nodes as containers) informs topology.
- Reuse registry seed: job-01..04 ID JSON files under `docs/runs/moorfield/`.
- Must reuse (not recreate): GroundOS `id-a3eaf0c0d5b74284a190ac0c70c4830d`, LinkGate `id-23d0ad9fc6be4d2b93b3fabd9f6ca0c9`, RangePlan `id-1f24a5f8fd8846df99eccfc2157a1663`, AirStack `id-4c7eefcd80b44e7586295bded35cddb5`, SortieBoard `id-e163a120914643a5904ce0d5bcdc1fa6`.
- Create after approve (names from brief): Facility Hangar, Facility GCS van, Facility Comms cabin; Equipment Datalink mast, Equipment Launch equipment; Node range-floor (or equivalent brief name), Node on-prem app server, Node LinkGate host (in comms cabin). Assign launch equipment (and/or facility) to range-floor node; assign GroundOS to app server node; assign LinkGate to its cabin node; relate LinkGate host to Comms cabin.
- Do not create WorkPackage. Do not create air-vehicle structure. Do not merge or duplicate the three frozen apps.
- Naming policy: title-collapse-v1; brief names exact where listed.
- LinkGate documentation must restate no air-vehicle interface.
- Post-approve specialist order: archi-technology-physical → archi-traceability → archi-model-qa → archi-layout → archi-documentation.
