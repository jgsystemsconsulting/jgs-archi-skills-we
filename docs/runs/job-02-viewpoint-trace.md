<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Viewpoint Trace - Hatherley Plate Job 02

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
