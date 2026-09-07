<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Job 1: Motivation Overview

## Paste

```text
/archi-orchestrator Hatherley Plate: drivers, goals, and outcomes for order visibility. OrderSight must not swallow MillOS. No capabilities, processes, applications, or nodes.

Problem: Promised plate dates do not match mill reality. Sales tracks customer promises in PromiseSheet. The mill runs on MillOS. OrderSight is funded to fix visibility. Plant engineers fear OrderSight will be drawn as if it replaces MillOS.

Stakeholders: Plant Manager, Head of Sales, MES Owner, CRM Programme Manager, Operations Planner, Integration Lead.

Concerns: Sales and mill must share one order identity from promise to schedule. Plant Manager and Head of Sales must answer "is this order on the mill this week?" without PromiseSheet. OrderSight must not swallow MillOS.

Scope: In: drivers, goals, outcomes, and the OrderSight-must-not-swallow-MillOS requirement. Out: capabilities, processes, applications, nodes, work packages, second site, costing, MES rewrite.

Current state: Hatherley Plate Ltd, independent UK plate mill, one site Hatherley Works, Rotherham. Hot-rolled carbon plate for construction and heavy OEM. Promises live in PromiseSheet. Mill schedule lives in MillOS. WorksERP holds works orders. OrderSight is in pilot.

Target state: A Motivation Overview that Plant Manager and Head of Sales can sign. Shared order identity as a desired state. OrderSight remains sales-facing, not a mill system.

Expected outcome: View named Motivation Overview. No other views this job. Do not invent WMS, TMS, data lake, or ERP replacement. Facts: docs/plant-brief.md in the worked-example repository.
```

## Specialists expected

- archi-elicit
- archi-viewpoint-select
- archi-motivation

Do not invoke these yourself.

## Pass checks

- Confirmation gate shown before any MCP mutate
- View named exactly Motivation Overview
- OrderSight-must-not-swallow-MillOS is present as a requirement
- No capabilities, processes, applications, or nodes added
- Documentation fields are not a restatement of the name
