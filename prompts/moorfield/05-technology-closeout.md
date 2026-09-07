<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Job 5: Technology and Physical, then close-out

## Paste

```text
/archi-orchestrator on the current Hawker Range Systems model, technology and physical for Moorfield Range, then trace, QA, layout, and documentation. No work packages. No extra architecture. Do not model the air vehicle as product structure.

Problem: Range engineers need hangar, GCS van, comms cabin, and launch equipment on the drawing so RangePlan cannot be mistaken for the GCS or the airborne computer.

Stakeholders: Range Manager, GCS Owner, Integration Lead, Planning Programme Manager.

Concerns: Hangar, GCS van, comms cabin, datalink mast, launch equipment on a range-floor node, on-prem app server hosting GroundOS, LinkGate on a node in the comms cabin. At least one equipment or facility element assigned to a node. RangePlan still must not swallow AirStack or GroundOS.

Scope: In: those physical and node facts, then traceability, QA, layout, and documentation on the whole as-is model. Out: work packages, second site, costing, GroundOS rewrite, extra architecture, weapons system, ERP, data lake, air-vehicle SysML.

Current state: Motivation, capabilities, range operations, and application support already exist.

Target state: View named Technology and Physical. Then traces, QA report, layout, and documentation fields. Model remains as-is. Do not invent work packages.

Expected outcome: Technology and Physical plus close-out. Facts: docs/moorfield-brief.md.
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
- RangePlan, AirStack, and GroundOS remain separate
- No work packages
- Trace, QA, layout, and documentation ran
- Model still as-is
- No air-vehicle product structure
- Documentation fields are not a restatement of the name
