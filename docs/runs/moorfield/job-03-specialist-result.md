<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Specialist Result - Hawker Range Systems Job 03 (Range Operations)

**Status:** completed (draft checkpoint CP-G7)
**Confirmation:** approved (job-03-view-plan.md + architect answers)

## Pass checks

| Check | Result |
|-------|--------|
| View named Range Operations | pass `id-782395c6d18347a9a24da626f81ee275` |
| Task / Clear / Fly / Recover present | pass (BusinessProcess, new IDs) |
| No new applications | pass (app_count=0) |
| SortieBoard stays the pain | pass (note + docs only) |
| No air-vehicle structure | pass |
| Evidence first line on creates | pass |
| Docs not restatement of name | pass |
| Job-1 stakeholders not duplicated | pass (6 Stakeholder unchanged) |
| Job-2 capabilities not duplicated | pass (4 Capability unchanged; not on view) |

## Specialist: archi-business

**Status:** completed

### Views touched
- Range Operations (created) `id-782395c6d18347a9a24da626f81ee275` viewpoint `business_process_cooperation`

### Elements and relationships

| Action | Name | Type | ID |
|--------|------|------|-----|
| created | Task | BusinessProcess | id-8b426a10197b48b4b0864f0b4445ec3e |
| created | Clear | BusinessProcess | id-c0d2f85265bb4414b03c5a7e69934983 |
| created | Fly | BusinessProcess | id-b866710ad3b448d3829e71df6397738f |
| created | Recover | BusinessProcess | id-43ccf54a35034dfe8b7846c141d8f6b5 |
| created | Range Manager | BusinessRole | id-20972da34bbb434ab4ffe45eed56b121 |
| created | Chief Instructor | BusinessRole | id-d43bcfe1df2448359ea677c9b5135051 |
| created | Sortie Planner | BusinessRole | id-9e06116e788e40239a3ad697c91a2d06 |
| created | GCS Owner | BusinessRole | id-b25651dc1b5e44399395fbce5ba90087 |
| reused | Range Manager (etc.) | Stakeholder x6 | job-01 IDs (off-canvas witnesses) |
| reused | Task/Clear/Fly/Recover | Capability x4 | job-02 IDs (registry only) |
| created | Sortie Planner → Task | AssignmentRelationship | id-9859c332fee245449a2e73c86679c868 |
| created | Range Manager → Clear | AssignmentRelationship | id-cb4300984071419c87c1a537c0148ab0 |
| created | GCS Owner → Fly | AssignmentRelationship | id-e4108767c6d9403eb038b4ad98f44673 |
| created | Chief Instructor → Recover | AssignmentRelationship | id-fb87b731bffb455198412a99e5b67f62 |
| created | Task → Clear | TriggeringRelationship | id-e695269512f9459d9f003d84ff7c5eec |
| created | Clear → Fly | TriggeringRelationship | id-b4680b8852914b9088c737e220bf140c |
| created | Fly → Recover | TriggeringRelationship | id-0bb0bba503c84905a1f0351f84806fac |

### On-canvas vs off-canvas
- On canvas: Sortie Planner, Range Manager, GCS Owner, Chief Instructor (BusinessRole) + Task, Clear, Fly, Recover (BusinessProcess)
- Off canvas: Planning Programme Manager, Integration Lead (job-1 Stakeholder IDs only)
- Not on view: job-2 Capability IDs

### Candidate disposition
| Candidate | Disposition | Notes |
|-----------|-------------|-------|
| Task/Clear/Fly/Recover processes | captured | BusinessProcess @ Range Operations |
| Four on-canvas roles | captured | BusinessRole @ Range Operations |
| Planning Programme Manager | folded | off-canvas job-1 stakeholder |
| Integration Lead | folded | off-canvas job-1 stakeholder |
| Job-2 capabilities | folded | registry only |
| SortieBoard | out-of-scope | pain in documentation/note only |
| Applications / nodes / airframe | out-of-scope | freeze |

### Compliance notes
- none illegal. House-style aspect-hints (behaviour_not_verb_noun) on plain labels Task/Clear/Fly/Recover: accepted per architect approve; not auto-renamed.

### Open questions
- none

## Specialist: archi-model-qa (light)

**Status:** completed
**Fixes applied:** none

### Findings
| ID | Severity | Object | Problem | Proposed alternative |
|----|----------|--------|---------|----------------------|
| H1 | low | BusinessProcess Task/Clear/Fly/Recover | House-style prefers verb-noun behaviour names | Keep plain brief labels (architect approve); rename later only if programme asks |

### Compliance
- compliance_validate job-03-slice.json: ok, 0 findings
- docs_coverage --require-evidence: ok, 0 findings
- naming conflicts: 0
- app_count=0 node_count=0 workpackage_count=0
- stakeholders=6 capabilities=4 (no duplicates)
- Motivation Overview + Capability Map unchanged

## Specialist: archi-layout

**Status:** completed

### Views laid out
| View | Tools used | Residual issues |
|------|------------|-----------------|
| Range Operations | auto-layout-and-route (retry), auto-route-connections, assess-layout | none; overallRating excellent |

Snapshot: `docs/runs/moorfield/id-782395c6d18347a9a24da626f81ee275_1788817318167.png` (also `job-03-range-operations.png`)

## Specialist: archi-documentation

**Status:** completed

### Rationale written
| View | Schema valid | Model field updated |
|------|--------------|---------------------|
| Range Operations | yes (rationale_schema) | yes (update-view documentation) |

### Completion summary
- path: job-03-completion-summary.md (schema pass)
- Views Touched / Decisions / Open Questions / Confirmation Status / Specialists Run / Deliberately Deferred / Improve Next present

### Schema validation
- rationale_schema: pass
- completion_summary_schema: pass

### Note
- SortieBoard pain note placed below-content on the view (annotate last)

## Model state (final)

```json
{
  "name": "Hawker Range Systems Ltd",
  "elementCount": 22,
  "relationshipCount": 16,
  "viewCount": 3,
  "elementTypeDistribution": {
    "Capability": 4,
    "BusinessProcess": 4,
    "BusinessRole": 4,
    "Stakeholder": 6,
    "Driver": 1,
    "Goal": 1,
    "Outcome": 1,
    "Requirement": 1
  }
}
```

## Artifacts
- `docs/runs/moorfield/job-03-operations-ids.json`
- `docs/runs/moorfield/job-03-slice.json`
- `docs/runs/moorfield/job-03-rationale.md`
- `docs/runs/moorfield/job-03-completion-summary.md`
- `docs/runs/moorfield/job-03-assess-final.json`
- `docs/runs/moorfield/job-03-range-operations.png`

## Confirmation assumption
Work ran under approved View Plan with architect answers (title Range Operations; process labels Task/Clear/Fly/Recover; four roles on canvas; PPM/IL off-canvas; no capabilities on view; SortieBoard pain only).
