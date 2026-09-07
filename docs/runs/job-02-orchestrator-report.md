<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Orchestrator report - Hatherley Plate Job 02

## Status

- confirmation_status: **approved**
- run_status: **SPECIALISTS_COMPLETE** (draft checkpoint)
- view_plan: docs/runs/job-02-view-plan.md
- viewpoint_trace: docs/runs/job-02-viewpoint-trace.md
- specialist_result: docs/runs/job-02-specialist-result.md
- capability_ids: docs/runs/job-02-capability-ids.json
- mutations: yes (post-approve)

## Architect answers applied

- View title: Capability Map
- Four top-level capabilities: Promise, Order, Mill schedule, Collect
- Integration Lead omitted from this view (IDs retained from job 1)

## Elicit / viewpoint select (prior)

Unchanged from plan gate. Capability Map only; motivation reuse.

## Specialists run (post-approve)

1. archi-capability-strategy - four Strategy Capability elements; Capability Map view
2. archi-model-qa (light) - no driver duplicate; zero apps/processes/nodes; compliance_validate pass on slice after Cap-Cap edges removed
3. archi-layout - LTR grid; assess-layout excellent; PNG export
4. archi-documentation - view rationale + completion summary schemas pass

Skipped: motivation, business, application, technology-physical, implementation-migration, traceability.

## Model snapshot (final)

- name: Hatherley Plate Ltd
- elementCount: 14
- relationshipCount: 15 (job-01 only; no Cap-Cap edges retained)
- viewCount: 2
- Strategy: 4 Capability; Motivation: 10 (unchanged spine)
- application/process/node: 0
- New view: Capability Map `id-6613e98758a3455d95e1fcc5b8e731f7`
- Motivation Overview intact: `id-05f18c92556242fc8ce2a2252fc36867`

## Capabilities created

| Name | ID |
|------|-----|
| Promise | id-9c2c1a6a78f0475681b48889b2664099 |
| Order | id-f6c7c6a74874412ba24c60d318292ad2 |
| Mill schedule | id-ed34ec1744a1458b9f7e1579932f2af6 |
| Collect | id-50f22633aea34b3b8536e05a14fda533 |

Job-01 driver duplicated: **no**.

## Pass checks

- View named exactly Capability Map: pass
- Job 1 motivation reused: pass
- No ERP replacement / processes / apps / nodes / work packages: pass
- Evidence first line on new elements: pass
- Docs not restatement of name: pass

## Next

Draft complete for job 02. Later SOAM jobs add process/app/tech layers and legal cross-layer edges.
