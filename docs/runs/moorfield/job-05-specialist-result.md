<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Specialist Result - Hawker Range Systems Job 05

**Status:** DONE
**Confirmation:** approved

## Specialists run
1. archi-technology-physical
2. archi-traceability
3. archi-model-qa
4. archi-layout
5. archi-documentation

## Views touched
- **Technology and Physical** `id-7585e12756874cd1855d73253da55504` (viewpoint='technology_usage')
- Prior four views intact (no rebuild)

## Technology / physical elements
| Action | Name | Type | ID |
|--------|------|------|----|
| created_new | Range floor node | Node | id-38c34403663d47f89cb62a7240e16e5f |
| created_new | On-prem app server | Node | id-996182b6c7394a038accf601f3139a0a |
| created_new | LinkGate node | Node | id-0c90872c58974113baf4ef07d05bf59e |
| created_new | Hangar | Facility | id-54ebbe9850ae4485b5932078a0c8cc14 |
| created_new | GCS van | Facility | id-7b2d4974798e4faeabed3599b8ae08f2 |
| created_new | Comms cabin | Facility | id-622e47e2c1ae42438c8c5fe4b2929cff |
| created_new | Datalink mast | Equipment | id-024345e85bea4028bb2e35bf46be6752 |
| created_new | Launch equipment | Equipment | id-f2e4e924c5ed4ff09eb64fffd09551f1 |

## Application hosting (reuse)
| App | Host node | Relationship | App ID |
|-----|-----------|--------------|--------|
| GroundOS | On-prem app server | Realization Node→App + nested on view | id-a3eaf0c0d5b74284a190ac0c70c4830d |
| LinkGate | LinkGate node | Realization Node→App + nested on view | id-23d0ad9fc6be4d2b93b3fabd9f6ca0c9 |
| RangePlan | **none this job** (omitted from host nodes) | — | id-1f24a5f8fd8846df99eccfc2157a1663 |
| AirStack | **none this job** (off canvas; no air-vehicle node) | — | id-4c7eefcd80b44e7586295bded35cddb5 |
| SortieBoard | **none this job** | — | id-e163a120914643a5904ce0d5bcdc1fa6 |

Hosting note: JGS Archi Bridge rejects `AssignmentRelationship` between Node and ApplicationComponent. Compliant alternative applied: `RealizationRelationship` Node→ApplicationComponent plus nested containment on the Technology and Physical view.

## Assignment freeze evidence
- `AssignmentRelationship` id-38c34403663d47f89cb62a7240e16e5f → id-f2e4e924c5ed4ff09eb64fffd09551f1 (`id-f451ca647fc7405f8fcc03724164f084`)
- `AssignmentRelationship` id-54ebbe9850ae4485b5932078a0c8cc14 → id-38c34403663d47f89cb62a7240e16e5f (`id-e169b9f06efd4128a955fa360449f5cb`)
- `AssignmentRelationship` id-7b2d4974798e4faeabed3599b8ae08f2 → id-996182b6c7394a038accf601f3139a0a (`id-5de585d0805045899c8ee4cb3f4ebda1`)
- `AssignmentRelationship` id-622e47e2c1ae42438c8c5fe4b2929cff → id-0c90872c58974113baf4ef07d05bf59e (`id-39efb8cb9e554c4f814cee7aa2e029b9`)
- assign_freeze_count: 4
- assigned_ok flag: True

## Relationships (this job)
| Action | Type | Source | Target | ID |
|--------|------|--------|--------|-----|
| created | RealizationRelationship | On-prem app server | GroundOS | id-68b896e478c8419dacaac1373f2f2b26 |
| created | RealizationRelationship | LinkGate node | LinkGate | id-10a3dcbbf6d2496fac1256e761854851 |
| created | AssignmentRelationship | Range floor node | Launch equipment | id-f451ca647fc7405f8fcc03724164f084 |
| created | AssignmentRelationship | Hangar | Range floor node | id-e169b9f06efd4128a955fa360449f5cb |
| created | AssignmentRelationship | GCS van | On-prem app server | id-5de585d0805045899c8ee4cb3f4ebda1 |
| created | AssignmentRelationship | Comms cabin | LinkGate node | id-39efb8cb9e554c4f814cee7aa2e029b9 |
| created | AssociationRelationship | Datalink mast | LinkGate node | id-1c59ff1dc5b34dbf8dbd847b523078a9 |
| created | AssociationRelationship | RangePlan must not swallow AirStack or GroundOS | On-prem app server | id-b645383bdf924bb5acd43b825d4c5f73 |
| created | RealizationRelationship | GroundOS | Fly (capability) | id-3d0b11d9d4e040009b1aee0e6ea43204 |
| created | RealizationRelationship | LinkGate | Clear (capability) | id-c113148f28144edd8772c4809103097e |
| created | RealizationRelationship | GroundOS | Recover (capability) | id-ebec741536e44609a30f52606f94d23c |

## Candidate disposition
| Candidate | Disposition | Target |
|-----------|-------------|--------|
| Range floor node | captured | element @ Technology and Physical |
| On-prem app server | captured | element @ Technology and Physical |
| LinkGate node | captured | element @ Technology and Physical |
| Hangar | captured | element @ Technology and Physical |
| GCS van | captured | element @ Technology and Physical |
| Comms cabin | captured | element @ Technology and Physical |
| Datalink mast | captured | element @ Technology and Physical |
| Launch equipment | captured | element @ Technology and Physical |
| GroundOS hosting | folded | reused app + Realization to On-prem app server |
| LinkGate hosting | folded | reused app + Realization to LinkGate node |
| RangePlan hosting | out-of-scope | omitted from host nodes (brief + approve) |
| AirStack hosting | out-of-scope | no air-vehicle node (brief + approve) |
| Work packages | out-of-scope | freeze |
| Air-vehicle SysML | out-of-scope | freeze |

## Traceability
- Requirement "RangePlan must not swallow AirStack or GroundOS" ↔ On-prem app server (Association)
- GroundOS → Fly / Recover capabilities (Realization)
- LinkGate → Clear capability (Realization)
- Trace rel ids: ['id-b645383bdf924bb5acd43b825d4c5f73', 'id-3d0b11d9d4e040009b1aee0e6ea43204', 'id-c113148f28144edd8772c4809103097e', 'id-ebec741536e44609a30f52606f94d23c']
- Gap (by design): RangePlan/AirStack have no tech host this job; SortieBoard not hosted

## Model QA
```json
{
  "work_package_count": 0,
  "node_count": 3,
  "facility_count": 3,
  "equipment_count": 2,
  "application_component_count": 5,
  "assign_freeze_count": 4,
  "rangeplan_airstack_groundos_distinct": true,
  "rangeplan_airstack_not_on_range_floor_host": true,
  "linkgate_no_launch_link": true,
  "forbidden_names": [],
  "evidence_first_line_ok": true,
  "doc_not_name_only": true,
  "view_name": "Technology and Physical",
  "viewpoint_used": "technology_usage",
  "node_names": [
    "LinkGate node",
    "On-prem app server",
    "Range floor node"
  ],
  "facility_names": [
    "Comms cabin",
    "GCS van",
    "Hangar"
  ],
  "equipment_names": [
    "Datalink mast",
    "Launch equipment"
  ],
  "app_names": [
    "AirStack",
    "GroundOS",
    "LinkGate",
    "RangePlan",
    "SortieBoard"
  ],
  "apps": {
    "AirStack": "id-4c7eefcd80b44e7586295bded35cddb5",
    "GroundOS": "id-a3eaf0c0d5b74284a190ac0c70c4830d",
    "SortieBoard": "id-e163a120914643a5904ce0d5bcdc1fa6",
    "RangePlan": "id-1f24a5f8fd8846df99eccfc2157a1663",
    "LinkGate": "id-23d0ad9fc6be4d2b93b3fabd9f6ca0c9"
  }
}
```
Pass checks:
```json
{
  "view_named_technology_and_physical": true,
  "facility_or_equipment_assigned_to_node": true,
  "rangeplan_airstack_groundos_separate": true,
  "rangeplan_airstack_not_on_range_hosts": true,
  "groundos_on_onprem": true,
  "linkgate_on_linkgate_node": true,
  "linkgate_no_launch_equipment_link": true,
  "work_package_count_0": true,
  "no_forbidden_systems": true,
  "evidence_ok": true,
  "doc_not_name_only": true,
  "model_as_is": true,
  "layout_ok": true,
  "no_air_vehicle_structure": true
}
```
Work package count: 0
Compliance helper: see job-05-technology-ids.json compliance field.

## Layout
- assess-layout overallRating: excellent
- PNG: docs/runs/moorfield/job-05-technology-and-physical.png
- Note: id-3751f896f107477393c1ecf5cb6734fa

## Documentation
- View documentation updated with rationale sections
- job-05-rationale.md / job-05-completion-summary.md written

## get-model-info (final)
```json
{
  "name": "Hawker Range Systems Ltd",
  "elementCount": 35,
  "relationshipCount": 35,
  "viewCount": 5,
  "specializationCount": 0,
  "elementTypeDistribution": {
    "Capability": 4,
    "BusinessProcess": 4,
    "BusinessRole": 4,
    "ApplicationComponent": 5,
    "Node": 3,
    "Facility": 3,
    "Equipment": 2,
    "Stakeholder": 6,
    "Driver": 1,
    "Goal": 1,
    "Outcome": 1,
    "Requirement": 1
  },
  "relationshipTypeDistribution": {
    "AssociationRelationship": 8,
    "InfluenceRelationship": 2,
    "RealizationRelationship": 6,
    "AssignmentRelationship": 8,
    "TriggeringRelationship": 3,
    "ServingRelationship": 8
  },
  "layerDistribution": {
    "Strategy": 4,
    "Business": 8,
    "Application": 5,
    "Technology": 3,
    "Physical": 5,
    "Motivation": 10
  },
  "approvalMode": false
}
```

## Concerns
- none blocking. Hosting uses Realization Node→App because Assignment Node↔App is illegal on this bridge (documented).

## Next
Draft checkpoint (CP-G7). No git commit.
