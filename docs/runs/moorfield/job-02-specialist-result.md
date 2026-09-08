<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Specialist Result - Hawker Range Systems Job 02 (Capability Map)

**Status:** completed (draft checkpoint, CP-G7)
**Confirmation:** approved (Capability Map; Task/Clear/Fly/Recover; ownership text only)
**Model:** Hawker Range Systems Ltd

## Specialists run

1. archi-capability-strategy
2. archi-model-qa (light)
3. archi-layout
4. archi-documentation

Skipped: motivation (job 1), business, application, technology-physical, implementation-migration, traceability.

## Views touched

| View | ID | Action |
|------|-----|--------|
| Capability Map | `id-6967b8a5125d46e1b6ba0edbf9b9539b` | created; viewpoint `capability_map` |
| Motivation Overview | `id-02bfe33f26d844a1a34a314a40a400c0` | unchanged |

## Candidate disposition

| Candidate | Disposition | Target | Reason |
|-----------|-------------|--------|--------|
| Capability: Task | captured | Capability @ Capability Map (`id-637e89c75e944169983f389d7a572f98`) | Architect plain name; planning-facing ownership text |
| Capability: Clear | captured | Capability @ Capability Map (`id-97ebdecf31914a67bb2dbd87f3229ddb`) | Architect plain name |
| Capability: Fly | captured | Capability @ Capability Map (`id-03db6547aef1422db55f7e1277e94923`) | Architect plain name; GroundOS live-sortie ownership in documentation only |
| Capability: Recover | captured | Capability @ Capability Map (`id-44a1e398965248e8a79831ea7cc78298`) | Architect plain name |
| Cap-Cap Flow/Association | out-of-scope | | Hatherley lesson; spatial left-to-right order only |
| Application / process / node elements | out-of-scope | | Job 2 freeze; named systems text only |
| Second motivation driver/goal/outcome/requirement | out-of-scope | | Reuse job-01-motivation-ids.json |
| GroundOS rewrite / RangePlan-as-GCS | out-of-scope | | moorfield-brief hard freeze |

## Reuse registry

| concept_key | element_id | decision | notes |
|-------------|------------|----------|-------|
| capability:task | id-637e89c75e944169983f389d7a572f98 | create | |
| capability:clear | id-97ebdecf31914a67bb2dbd87f3229ddb | create | |
| capability:fly | id-03db6547aef1422db55f7e1277e94923 | create | |
| capability:recover | id-44a1e398965248e8a79831ea7cc78298 | create | |
| (all job-1 motivation keys) | see job-01-motivation-ids.json | reuse | not recreated |

## Elements and relationships

### View

- Capability Map `id-6967b8a5125d46e1b6ba0edbf9b9539b` viewpoint capability_map
- Group band: Tasking to live sortie
- Ownership note below content (CP-G5)

### Elements (4 created this job)

| Action | Name | Type | ID |
|--------|------|------|----|
| created | Task | Capability | id-637e89c75e944169983f389d7a572f98 |
| created | Clear | Capability | id-97ebdecf31914a67bb2dbd87f3229ddb |
| created | Fly | Capability | id-03db6547aef1422db55f7e1277e94923 |
| created | Recover | Capability | id-44a1e398965248e8a79831ea7cc78298 |

### Relationships (0 created this job)

Spatial order Task → Clear → Fly → Recover carries the spine. No Cap-Cap edges.

## QA (light)

| Check | Result |
|-------|--------|
| Model name | Hawker Range Systems Ltd |
| View name exact | Capability Map |
| Job 1 driver duplicated | no (Driver count = 1) |
| ApplicationComponent / BusinessProcess / Node | 0 / 0 / 0 |
| Capability count | 4 (Task, Clear, Fly, Recover) |
| Evidence first line on capabilities | yes |
| Docs not name restatement | yes |
| compliance_validate (cap slice) | pass (0 findings) |
| docs_coverage --require-evidence (cap slice) | pass (0 findings) |
| naming conflicts / aspect hints | 0 / 0 |
| assess-layout | overallRating excellent |
| Motivation Overview intact | 10 elements, 9 relationships |
| Layers after job | Motivation 10 + Strategy 4 |

Whole-model docs_coverage flags empty relationship documentation on job-1 edges when the bridge read path omits rel docs; those IDs already carry documentation from job 1 transcript/update-relationship and are not in scope to rewrite this job.

## Layout

- Grouped Capability Map band with four capabilities left to right.
- Manual horizontal positions after grouped auto-layout stacked vertically.
- Ownership note below-content.
- Final assess: overall excellent; all ratingBreakdown dimensions pass.
- PNG: `docs/runs/moorfield/id-6967b8a5125d46e1b6ba0edbf9b9539b_1788816739132.png`

## Documentation

- View rationale on Capability Map (RATE-01); rationale_schema pass (`job-02-rationale.md`).
- Completion summary schema pass (`job-02-completion-summary.md`).
- IDs: `job-02-capability-ids.json`

## Scope statement

Work stayed inside the approved View Plan: strategy capabilities only, job-1 motivation reused by ID, no apps/processes/nodes, no GroundOS rewrite.

## Open questions

- None blocking. Draft checkpoint (CP-G7).
