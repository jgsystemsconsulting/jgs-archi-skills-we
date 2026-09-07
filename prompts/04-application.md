<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Job 4: Application Support

## Paste

```text
/archi-orchestrator on the current Hatherley Plate model, application support for MillOS, WorksERP, PromiseSheet, OrderSight, and PlantGate. Shared order identity. OrderSight and MillOS stay separate.

Problem: Sales, mill, and integration cannot see which systems hold promises, works orders, and the mill schedule. The CRM programme must not be drawn as the MES.

Stakeholders: MES Owner, CRM Programme Manager, Integration Lead, Plant Manager, Head of Sales.

Concerns: OrderSight and MillOS stay separate. Shared order identity, not one merged blob. PlantGate bridges OrderSight promises to WorksERP works orders and does not talk to mill equipment.

Scope: In: MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate, and how they support the operations already modelled. Out: nodes, work packages, second site, costing, MES rewrite, ERP replacement.

Current state: Motivation, capabilities, and production operations already exist. Named systems as in docs/plant-brief.md.

Target state: View named Application Support. Same system names. Do not invent WMS, TMS, data lake, or ERP replacement.

Expected outcome: Application Support only. Facts: docs/plant-brief.md.
```

## Specialists expected

- archi-elicit
- archi-viewpoint-select
- archi-application

Do not invoke these yourself.

## Pass checks

- Confirmation gate shown before any MCP mutate
- View named exactly Application Support
- MillOS, WorksERP, PromiseSheet, OrderSight, and PlantGate are present
- OrderSight and MillOS remain separate
- No WMS, TMS, data lake, or ERP replacement
- Documentation fields are not a restatement of the name
