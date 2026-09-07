<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Viewpoint Trace - Hatherley Plate Job 03

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
