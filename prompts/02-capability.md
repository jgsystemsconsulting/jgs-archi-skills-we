<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Job 2: Capability Map

## Paste

```text
/archi-orchestrator on the current Hatherley Plate model, capability map for sales to mill. Reuse the motivation already modelled. No ERP replacement.

Problem: Finance, operations, and the plant cannot see which capabilities actually run promise, order, mill schedule, and collect. Job 1 already captured why visibility matters.

Stakeholders: Plant Manager, Head of Sales, MES Owner, CRM Programme Manager, Operations Planner.

Concerns: One capability map they can agree on. MillOS stays the mill capability owner. OrderSight stays sales-facing. No ERP replacement.

Scope: In: sales-to-mill capabilities on the current model. Out: new processes, new applications, nodes, work packages, second site, costing, MES rewrite.

Current state: Motivation Overview already exists. Promises in PromiseSheet, works orders in WorksERP, mill schedule in MillOS, OrderSight in pilot.

Target state: View named Capability Map. Same capability names if they appear on later views. Reuse job 1 motivation. Do not invent WMS, TMS, data lake, or ERP replacement.

Expected outcome: Capability Map only. Facts: docs/plant-brief.md.
```

## Specialists expected

- archi-elicit
- archi-viewpoint-select
- archi-capability-strategy

Do not invoke these yourself.

## Pass checks

- Confirmation gate shown before any MCP mutate
- View named exactly Capability Map
- Job 1 motivation reused, not duplicated as a second set of drivers
- No ERP replacement
- Documentation fields are not a restatement of the name
