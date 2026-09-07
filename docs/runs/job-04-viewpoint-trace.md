<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Viewpoint Trace - Hatherley Plate Job 04

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
