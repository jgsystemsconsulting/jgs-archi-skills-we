<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Job 3: Production Operations

## Paste

```text
/archi-orchestrator on the current Hatherley Plate model, as-is production operations: promise, works order, mill schedule, plate rolling. Named roles plus those processes. No new applications.

Problem: The mill cannot show how a customer promise becomes a mill schedule. PromiseSheet is still the pain.

Stakeholders: Plant Manager, Head of Sales, Operations Planner, MES Owner.

Concerns: As-is shop floor only. PromiseSheet stays. Do not sneak in applications or nodes.

Scope: In: promise, works order, mill schedule, plate rolling, and the named roles (Plant Manager, Head of Sales, MES Owner, CRM Programme Manager, Operations Planner, Integration Lead). Out: new applications, nodes, work packages, second site, costing, MES rewrite.

Current state: Capability Map and Motivation Overview already exist. Promises in PromiseSheet, works orders in WorksERP, mill schedule in MillOS.

Target state: View named Production Operations. Roles and processes only. PromiseSheet remains the pain. Do not invent WMS, TMS, data lake, or ERP replacement.

Expected outcome: Production Operations only. Facts: docs/plant-brief.md.
```

## Specialists expected

- archi-elicit
- archi-viewpoint-select
- archi-business

Do not invoke these yourself.

## Pass checks

- Confirmation gate shown before any MCP mutate
- View named exactly Production Operations
- Promise, works order, mill schedule, and plate rolling are present
- No new applications
- PromiseSheet stays the pain
- Documentation fields are not a restatement of the name
