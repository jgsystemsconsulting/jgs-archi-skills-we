<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Viewpoint Trace - Hatherley Plate Job 05

## Viewpoint Trace Table

| Viewpoint | Stakeholder | Concern | Purpose | Abstraction | Standard? | Justification |
|-----------|-------------|---------|---------|-------------|-----------|---------------|
| Technology Usage | Plant Manager; MES Owner | On-prem app server hosts MillOS and WorksERP; mill path stays separate from CRM; OrderSight must not swallow MillOS | inform | mixed | yes | Standard Technology Usage shows applications assigned to infrastructure nodes. Reuse MillOS and WorksERP as distinct components on the mill app-server node; do not place OrderSight on that node so CRM cannot be read as the mill stack. |
| Technology Usage | Integration Lead | PlantGate on a node in the comms room; PlantGate does not talk to mill equipment | inform | mixed | yes | PlantGate (reused application) assigned to a dedicated comms-room node; separation from mill-floor equipment node documents the non-equipment bridge. |
| Physical | Plant Manager; MES Owner | Plate mill building; rolling equipment on a mill-floor node; at least one equipment or facility assigned to a node | inform | mixed | yes | Matrix top rank Physical (score 6) on purpose=inform, abstraction=mixed, concern tags physical/equipment. Facility and equipment elements with assignment to the mill-floor node satisfy the hard freeze. |
| Physical | Integration Lead; CRM Programme Manager | Comms room visible so sales CRM path is not mistaken for mill floor | inform | mixed | yes | Comms room as facility (or equivalent physical place) with the PlantGate node located there keeps CRM/integration housing distinct from plate mill building and rolling equipment. |

## Organisation-Specific Proposals

### Technology and Physical (view name only)
- Stakeholders / concerns / purpose / abstraction: all four stakeholders; combined tech hosting + physical place/equipment; purpose inform; abstraction mixed.
- Why standards insufficient as separate canvases: user target is **one** view named Technology and Physical, not two diagrams.
- Compliance constraints: single canvas carries Technology Usage content (nodes + reused apps MillOS, WorksERP, PlantGate) and Physical content (plate mill building, comms room, rolling equipment). No work packages. No second site. No invented WMS/TMS/data lake/ERP. OrderSight remains a separate application and is not hosted on the mill app-server node. Formal `create-view` viewpoint param: `technology_usage` (MCP-known); view **name** organisation-specific: **Technology and Physical**. If live create rejects mixing physical types under that param, omit viewpoint or use `technology` and keep the same element set (user still gets one named view).

## Rejected Alternatives

| Viewpoint | Why rejected |
|-----------|--------------|
| Application Usage | Already job 04 (Application Support); reuse app IDs only. |
| Application Structure | App inventory without nodes; misses physical freeze. |
| Application Cooperation | Integration-only; does not place facilities/equipment. |
| Technology (structure-only) | Weaker than Technology Usage for "what runs where" with named apps; still useful as fallback viewpoint param. |
| Layered | Would invite extra cross-layer architecture beyond named physical/nodes; freeze says no extra architecture. |
| Implementation and Migration | Work packages explicitly out. |
| Project | No programme packages this job. |
| Business Process | Already job 03; reuse only. |
| Capability Map | Already job 02; reuse only. |
| Motivation | Already job 01; reuse only. |
| Business Product | Not the ask. |

Matrix run: `helpers/viewpoint_selection_matrix.py` purpose=inform, abstraction=mixed; Physical 6 (top), Technology 4, standard_fit true. Scope filter: Physical + Technology Usage combined on one view named Technology and Physical; Implementation/Migration and Layered rejected by freeze.
