<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Specialist Result - Hatherley Plate Job 01

**Status:** completed
**Confirmation:** approved (Motivation Overview; six stakeholders; frozen spine)

## Candidate disposition

| Candidate | Disposition | Target / reason |
|-----------|-------------|-----------------|
| Driver: Promised plate dates do not match mill reality | captured | Driver @ Motivation Overview (id-fcf6a7e660504afaa4580a9a92e062d9) |
| Goal: Sales and mill share one order identity from promise to schedule | captured | Goal @ Motivation Overview (id-77f9fed68144498386bf15c188fc2d21) |
| Outcome: Plant Manager and Head of Sales answer on-mill-this-week without PromiseSheet | captured | Outcome @ Motivation Overview (id-bbf70387a3014a0bac693ecca4cce026) |
| Requirement: OrderSight must not swallow MillOS | captured | Requirement @ Motivation Overview (id-8387c0d7776b46b8a08ee1ad05bd0953) |
| Stakeholder: Plant Manager | captured | reused existing Stakeholder @ Motivation Overview (id-0260a5aa995b41c7b84d93d3541592c0) |
| Stakeholder: Head of Sales | captured | Stakeholder @ Motivation Overview (id-988afa0e45894cd3a657ac9c7085ed98) |
| Stakeholder: MES Owner | captured | Stakeholder @ Motivation Overview (id-db0cfaa61b4048e7900b2b9bad3eea97) |
| Stakeholder: CRM Programme Manager | captured | Stakeholder @ Motivation Overview (id-92664a6b007b411d979d63c25480a38c) |
| Stakeholder: Operations Planner | captured | Stakeholder @ Motivation Overview (id-ee9aa7f5d13c4ec9ba9da957d3768ed2) |
| Stakeholder: Integration Lead | captured | Stakeholder @ Motivation Overview (id-9fc4203ce6ac494fbe546220c92f44b9) |
| Application / capability / process / node elements | out-of-scope | Job 1 motivation-only freeze |
| WMS, TMS, data lake, ERP replacement, second site | out-of-scope | plant-brief hard freeze |

## Reuse registry

| concept_key | element_id | decision | notes |
|-------------|------------|----------|-------|
| stakeholder:plant manager | id-0260a5aa995b41c7b84d93d3541592c0 | reuse | probe create; documentation refreshed |
| stakeholder:head of sales | id-988afa0e45894cd3a657ac9c7085ed98 | create | |
| stakeholder:mes owner | id-db0cfaa61b4048e7900b2b9bad3eea97 | create | |
| stakeholder:crm programme manager | id-92664a6b007b411d979d63c25480a38c | create | |
| stakeholder:operations planner | id-ee9aa7f5d13c4ec9ba9da957d3768ed2 | create | |
| stakeholder:integration lead | id-9fc4203ce6ac494fbe546220c92f44b9 | create | |
| driver:promised plate dates do not match mill reality | id-fcf6a7e660504afaa4580a9a92e062d9 | create | |
| goal:sales and mill share one order identity from promise to schedule | id-77f9fed68144498386bf15c188fc2d21 | create | |
| outcome:plant manager and head of sales answer on-mill-this-week without promisesheet | id-bbf70387a3014a0bac693ecca4cce026 | create | |
| requirement:ordersight must not swallow millos | id-8387c0d7776b46b8a08ee1ad05bd0953 | create | |

## Elements and relationships

### View

- Motivation Overview id-05f18c92556242fc8ce2a2252fc36867 viewpoint motivation

### Elements

| Action | Name | Type | ID |
|--------|------|------|----|
| reused | Plant Manager | Stakeholder | id-0260a5aa995b41c7b84d93d3541592c0 |
| created | Head of Sales | Stakeholder | id-988afa0e45894cd3a657ac9c7085ed98 |
| created | MES Owner | Stakeholder | id-db0cfaa61b4048e7900b2b9bad3eea97 |
| created | CRM Programme Manager | Stakeholder | id-92664a6b007b411d979d63c25480a38c |
| created | Operations Planner | Stakeholder | id-ee9aa7f5d13c4ec9ba9da957d3768ed2 |
| created | Integration Lead | Stakeholder | id-9fc4203ce6ac494fbe546220c92f44b9 |
| created | Promised plate dates do not match mill reality | Driver | id-fcf6a7e660504afaa4580a9a92e062d9 |
| created | Sales and mill share one order identity from promise to schedule | Goal | id-77f9fed68144498386bf15c188fc2d21 |
| created | Plant Manager and Head of Sales answer on-mill-this-week without PromiseSheet | Outcome | id-bbf70387a3014a0bac693ecca4cce026 |
| created | OrderSight must not swallow MillOS | Requirement | id-8387c0d7776b46b8a08ee1ad05bd0953 |

### Relationships (15)

| Type | Source | Target | ID |
|------|--------|--------|----|
| Association | Plant Manager | Driver | id-667ac7aeab054091a4569dfd1f97107c |
| Association | Head of Sales | Driver | id-380de8549ac54ebabc4d4962e9af9943 |
| Association | MES Owner | Driver | id-43ab2b86f1804fc88e87dd9113cb6965 |
| Association | CRM Programme Manager | Driver | id-19d9b00629d14813b54456c13937e373 |
| Association | Operations Planner | Driver | id-f3edb77ba6cc4bdaa6c199b09f34d6c2 |
| Association | Integration Lead | Driver | id-489e778685bd499eb4cd1f3c4d2ab4f5 |
| Influence | Driver | Goal | id-7fc557ea98cc4a81baf6e68c6637bfd5 |
| Realization | Outcome | Goal | id-80931b7bffd04ed2875ac31bc65caa63 |
| Realization | Requirement | Goal | id-6d24ba8943244ed1b7cc0adcb807ecf1 |
| Association | Plant Manager | Outcome | id-ac34f9357252446a8e90c2870dba2558 |
| Association | Head of Sales | Outcome | id-2123bb07b54948ccaa6aab7a247cd503 |
| Association | Operations Planner | Goal | id-e248a5a1e04247daa01ce86499b1782f |
| Association | Integration Lead | Goal | id-533bf192ca6643b0986664aa6c9ed853 |
| Association | MES Owner | Requirement | id-c6ea99817b22457c909b8328595787c0 |
| Association | CRM Programme Manager | Requirement | id-44c44def4b364147ba651c1038a4059c |

Relationships documented via update-relationship after create.

## Specialists run

| Specialist | Result |
|------------|--------|
| archi-motivation | completed |
| archi-model-qa | completed (light) |
| archi-layout | completed (overall good) |
| archi-documentation | completed (draft) |

## QA findings

- Model Hatherley Plate Ltd: elements 10, relationships 15, views 1.
- Types Stakeholder 6, Driver 1, Goal 1, Outcome 1, Requirement 1. Motivation only.
- App/capability/process/node count: 0.
- Requirement present: OrderSight must not swallow MillOS (id-8387c0d7776b46b8a08ee1ad05bd0953).
- Evidence first lines present on all elements. Plant Manager reused.
- Offline compliance_validate fixture vs live MCP motivation recipe: fixture flags some Association/Realization pairs; MCP recipe permits them. MCP is SoT; no rewrite.

## Layout notes

- auto-layout-and-route + auto-route-connections + resize/spacing.
- Final assess: overall good, layout excellent, routing good.
- PNG: docs/runs/job-01-motivation-overview.png

## Documentation

- update-view rationale on Motivation Overview (RATE-01 sections).
- update-model documentation unsupported. No save-model tool.

## Completion summary (draft CP-G7)

- Views Touched: Motivation Overview (id-05f18c92556242fc8ce2a2252fc36867)
- Decisions: approved; motivation-only; six stakeholders; boundary requirement; PM reused
- Open Questions: none on spine
- Confirmation Status: approved
- Specialists Run: motivation, model-qa light, layout, documentation
- Deliberately Deferred: non-motivation layers
- Improve Next: optional banded groups; allowlist vs recipe

## MCP snapshot (final)

name Hatherley Plate Ltd; elementCount 10; relationshipCount 15; viewCount 1; Motivation only; approvalMode false

