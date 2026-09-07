<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Job 5: Technology and Physical, then close-out

## Paste

```text
/archi-orchestrator on the current Hatherley Plate model, technology and physical for the mill, then trace, QA, layout, and documentation. No work packages. No extra architecture.

Problem: Plant engineers need mill equipment and the comms room on the drawing so OrderSight cannot be mistaken for the mill.

Stakeholders: Plant Manager, MES Owner, Integration Lead, CRM Programme Manager.

Concerns: Plate mill building, comms room, rolling equipment on a mill-floor node, on-prem app server hosting MillOS and WorksERP, PlantGate on a node in the comms room. At least one equipment or facility element assigned to a node. OrderSight still must not swallow MillOS.

Scope: In: those physical and node facts, then traceability, QA, layout, and documentation on the whole as-is model. Out: work packages, second site, costing, MES rewrite, extra architecture, WMS, TMS, data lake, ERP replacement.

Current state: Motivation, capabilities, production operations, and application support already exist.

Target state: View named Technology and Physical. Then traces, QA report, layout, and documentation fields. Model remains as-is. Do not invent work packages.

Expected outcome: Technology and Physical plus close-out. Facts: docs/plant-brief.md.
```

## Specialists expected

- archi-elicit
- archi-viewpoint-select
- archi-technology-physical
- archi-traceability
- archi-model-qa
- archi-layout
- archi-documentation

Do not invoke these yourself.

## Pass checks

- Confirmation gate shown before any MCP mutate
- View named exactly Technology and Physical
- At least one facility or equipment element assigned to a node
- OrderSight and MillOS remain separate
- No work packages
- Trace, QA, layout, and documentation ran
- Model still as-is
- Documentation fields are not a restatement of the name
