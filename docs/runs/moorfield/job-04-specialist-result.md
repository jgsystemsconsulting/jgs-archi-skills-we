# Specialist Result - Hawker Range Systems Job 04 (Application Support)

**Status:** completed (draft checkpoint CP-G7)
**Confirmation:** approved (job-04-view-plan.md + architect answers)

## Pass checks

| Check | Result |
|-------|--------|
| View named Application Support | pass `id-5ed7d076bfc449d78537f5468ed476fb` |
| Five apps present and separate | pass |
| RangePlan ≠ GroundOS ≠ AirStack | pass |
| No weapons/ERP/data lake/air-vehicle | pass |
| Node count 0 | pass |
| Evidence first line | pass |
| Docs not restatement of name | pass |
| Job-3 processes reused | pass |
| Job-2 caps omitted from canvas | pass |
| Layout assess | excellent |
| Offline compliance | true |
| Docs coverage | true |
| QA aggregate | pass |

## Specialist: archi-application

**Status:** completed

### Views touched
- Application Support (created) `id-5ed7d076bfc449d78537f5468ed476fb` viewpoint `application_cooperation`

### Elements and relationships

| Action | Name | Type | ID |
|--------|------|------|-----|
| created | AirStack | ApplicationComponent | id-4c7eefcd80b44e7586295bded35cddb5 |
| created | GroundOS | ApplicationComponent | id-a3eaf0c0d5b74284a190ac0c70c4830d |
| created | SortieBoard | ApplicationComponent | id-e163a120914643a5904ce0d5bcdc1fa6 |
| created | RangePlan | ApplicationComponent | id-1f24a5f8fd8846df99eccfc2157a1663 |
| created | LinkGate | ApplicationComponent | id-23d0ad9fc6be4d2b93b3fabd9f6ca0c9 |
| reused | Task | BusinessProcess | id-8b426a10197b48b4b0864f0b4445ec3e |
| reused | Clear | BusinessProcess | id-c0d2f85265bb4414b03c5a7e69934983 |
| reused | Fly | BusinessProcess | id-b866710ad3b448d3829e71df6397738f |
| reused | Recover | BusinessProcess | id-43ccf54a35034dfe8b7846c141d8f6b5 |
| created | RangePlan → LinkGate | ServingRelationship | id-89f559f9f1f043f3a61172f01ab6e546 |
| created | LinkGate → GroundOS | ServingRelationship | id-a97ea82ce8ba45c2b1c766d834a96aed |
| created | app → process servings | ServingRelationship x6 | see job-04-application-ids.json |

### Notes
- Initial FlowRelationship app-to-app edges rejected by compliance_validate (behaviour-only Flow). Replaced with Serving bridge edges (legal ApplicationComponent pattern). MUTATION succeeded; no MUTATION_FAILED.
- Shared sortie identity: process chain only; no data object.
- LinkGate docs state no air-vehicle interface; freeze note on view.

### Candidate disposition
See `job-04-disposition.md` (helper ok).

### Compliance notes
- compliance_validate job-04-slice.json: ok
- docs_coverage --require-evidence: ok
- Live QA: 5 apps, 0 nodes, distinct freeze, evidence OK

### Open questions
- none

## Specialist: archi-model-qa (light)

**Status:** completed
**Fixes applied:** deleted 2 illegal Flow edges; created 2 Serving bridge edges (authorized post-approve modelling correction)

### Findings
| ID | Severity | Object | Problem | Proposed alternative |
|----|----------|--------|---------|----------------------|
| F1 | high | Flow app→app | Flow not permitted ApplicationComponent→ApplicationComponent | ServingRelationship bridge (applied) |

## Specialist: archi-layout

**Status:** completed

### Views laid out
| View | Tools used | Residual issues |
|------|------------|-----------------|
| Application Support | auto-layout-and-route, auto-route-connections, note below-content | assess=excellent; edgeCrossingCount=1 (rating still excellent) |

## Specialist: archi-documentation

**Status:** completed

### Rationale written
| View | Schema valid | Model field updated |
|------|--------------|---------------------|
| Application Support | yes | yes |

### Completion summary
- file: job-04-completion-summary.md
- snapshot: job-04-application-support.png

### Scope statement
Work stayed inside confirmed application scope. No nodes, equipment, work packages, weapons, ERP, data lake, or air-vehicle structure.
