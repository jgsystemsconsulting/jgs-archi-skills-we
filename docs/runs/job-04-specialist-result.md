<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Specialist Result - Hatherley Plate Job 04 (Application Support)

**Status:** completed (draft checkpoint, CP-G7)
**Confirmation:** approved
**Model:** Hatherley Plate Ltd

## Specialists run

1. archi-application
2. archi-model-qa (light)
3. archi-layout
4. archi-documentation

Skipped by scope: motivation, capability-strategy, business (reuse), technology-physical, implementation-migration, traceability.

## Views touched

| View | ID | Action |
|------|-----|--------|
| Application Support | `id-90bb9ec6131b44f9966ac494bd89a90c` | created; viewpoint `application_usage` |
| Motivation Overview | `id-05f18c92556242fc8ce2a2252fc36867` | left intact |
| Capability Map | `id-6613e98758a3455d95e1fcc5b8e731f7` | left intact |
| Production Operations | `id-c189cce2288642d8b1cf3c267270d571` | left intact |

## Elements and relationships

| Action | Name | Type | ID |
|--------|------|------|----|
| created | MillOS | ApplicationComponent | `id-e74300558c24411c9ca9cf76c2d9ecd6` |
| created | WorksERP | ApplicationComponent | `id-45a53e69f46a4c80a0e8bcb81ba24cf9` |
| created | PromiseSheet | ApplicationComponent | `id-d5dab10f11a04eedb0ba9532bd2940b1` |
| created | OrderSight | ApplicationComponent | `id-b8e160d2c6d24f34badc02f1b6ae6c6f` |
| created | PlantGate | ApplicationComponent | `id-d0698a626afc460d8de1493b05a421e6` |
| reused | Promise | BusinessProcess | `id-c338aa0260a345ed9be332a6b9e26be9` |
| reused | Works order | BusinessProcess | `id-69e033ce9ca242d499799db7a6b42272` |
| reused | Mill schedule | BusinessProcess | `id-d6a875984a84411d958d73759e2ffe1a` |
| reused | Plate rolling | BusinessProcess | `id-ed0201833e864e08ab2950d70d2994aa` |

Serving relationships (created; documented via `update-relationship`):

| Source | Target | ID |
|--------|--------|-----|
| PromiseSheet | Promise | `id-5abf0b65ccaf4d16ae90aafa800b5032` |
| OrderSight | Promise | `id-9212de6280604f5e9c6507431cab0bf2` |
| PlantGate | Promise | `id-be1b3be3034c42c28733cba2796fd526` |
| PlantGate | Works order | `id-070c651ce29e4e69be6f0d91242bce0a` |
| WorksERP | Works order | `id-e3e73197b6834536b2e7468769cc70ad` |
| MillOS | Mill schedule | `id-86a670b0e85949cca5d9663599568f3e` |
| MillOS | Plate rolling | `id-0e6ba889393144d58873fe2cab91b803` |
| WorksERP | Mill schedule | `id-77977799d7f2461ba5e81fbce42b3581` |

Job-03 Triggering chain appears on the canvas via auto-connect (reused, not recreated).

## Candidate disposition

| Candidate | Disposition | Target |
|-----------|-------------|--------|
| MillOS | captured | ApplicationComponent @ Application Support |
| WorksERP | captured | ApplicationComponent @ Application Support |
| PromiseSheet | captured | ApplicationComponent @ Application Support |
| OrderSight | captured | ApplicationComponent @ Application Support |
| PlantGate | captured | ApplicationComponent @ Application Support |
| job-03 processes (4) | captured (reuse) | same IDs on Application Support |
| job-02 capabilities | out-of-scope | omitted from canvas per approval |
| nodes / equipment | out-of-scope | PlantGate constraint is documentation only |
| WMS / TMS / data lake / ERP replacement | out-of-scope | freeze |

## Compliance notes

- OrderSight `id-b8e160d2c6d24f34badc02f1b6ae6c6f` != MillOS `id-e74300558c24411c9ca9cf76c2d9ecd6`.
- ApplicationComponent count = 5; BusinessProcess count still 4; node/equipment count = 0.
- No WMS, TMS, data lake, or ERP replacement elements.
- PlantGate documentation states bridge OrderSight promises to WorksERP works orders and does not talk to mill equipment.
- Evidence first line present on all five new applications.
- Two FlowRelationship edges (OrderSight-PlantGate, PlantGate-WorksERP) were created then removed after offline `compliance_validate` flagged ApplicationComponent-Flow-ApplicationComponent as illegal. Bridge remains in PlantGate element docs plus Serving to Promise and Works order.
- Offline `helpers/compliance_validate.py` on `job-04-slice.json`: ok true, findings empty.
- Layout `assess-layout`: overall **good** (all breakdown dimensions pass or good).

## Layout and export

- PNG: `docs/runs/job-04-application-support.png`
- Freeze note on canvas (below content): OrderSight/MillOS separate; PlantGate bridge only; no nodes this job.
- View documentation fields set (purpose, stakeholders, exclusions). Draft only (CP-G7).

## get-model-info (after)

- name: Hatherley Plate Ltd
- elementCount: 27
- relationshipCount: 31
- viewCount: 4
- Application: 5; nodes: 0

## Open questions

- None blocking. First generation is draft (CP-G7).

## IDs artifact

- `docs/runs/job-04-application-ids.json`

## Scope statement

Work stayed inside the approved Application Support / Application Usage plan: application layer create, job-03 process reuse, light QA, layout, documentation. No motivation, capability, business recreate, technology/physical, migration, or extra views.
