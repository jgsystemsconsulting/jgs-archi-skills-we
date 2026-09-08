<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Specialist Result - Hatherley Plate Job 05

**Status:** DONE
**Confirmation:** approved

## Specialists run
1. archi-technology-physical
2. archi-traceability
3. archi-model-qa
4. archi-layout
5. archi-documentation

## Views touched
- **Technology and Physical** `id-6ef45eb1bf8340f2b2eba45c4f92b9e9` (viewpoint=`technology_usage`)
- Prior four views intact (no rebuild)

## Technology / physical elements
| Action | Name | Type | ID |
|--------|------|------|----|
| created | Mill floor node | Node | id-c2b0ccf345fb4ce78c7e0687ed2fbe52 |
| created | On-prem app server | Node | id-ef9c0f14635a4a95adb8ba9858a25df2 |
| created | PlantGate node | Node | id-8d9fc0f78d2b4122bb9977edc94e9305 |
| created | Plate mill building | Facility | id-b1d315115a8249809f7750591162b405 |
| created | Comms room | Facility | id-9da853906d8c4af7805ac95eca12d643 |
| created | Rolling equipment | Equipment | id-057eb745f829482892236d1023a52c3a |

## Application hosting (reuse)
| App | Host node | Relationship | App ID |
|-----|-----------|--------------|--------|
| MillOS | On-prem app server | Realization Node→App + nested on view | id-e74300558c24411c9ca9cf76c2d9ecd6 |
| WorksERP | On-prem app server | Realization Node→App + nested on view | id-45a53e69f46a4c80a0e8bcb81ba24cf9 |
| PlantGate | PlantGate node | Realization Node→App + nested on view | id-d0698a626afc460d8de1493b05a421e6 |
| OrderSight | **none this job** (omitted from all nodes) |,  | id-b8e160d2c6d24f34badc02f1b6ae6c6f |

Hosting note: JGS Archi Bridge rejects `AssignmentRelationship` between Node and ApplicationComponent. Compliant alternative applied: `RealizationRelationship` Node→ApplicationComponent plus nested containment on the Technology and Physical view.

## Assignment freeze evidence
- `AssignmentRelationship` Mill floor node → Rolling equipment (`id-3a0ba7d10b264e43b860e0ec791a4292`)
- Also Facility→Node: Plate mill building → Mill floor node; Comms room → PlantGate node
- assign_freeze_count: 3

## Relationships (tech/physical this job)
| Action | Type | Source | Target | ID |
|--------|------|--------|--------|-----|
| created | RealizationRelationship | On-prem app server | MillOS | id-a8d339fd00d64299aa2f3008bacea830 |
| created | RealizationRelationship | On-prem app server | WorksERP | id-57653d64319145e88ab47d9978cd5f74 |
| created | RealizationRelationship | PlantGate node | PlantGate | id-8dc23741dfa244c2820bdd3104eb6d94 |
| created | AssignmentRelationship | Mill floor node | Rolling equipment | id-3a0ba7d10b264e43b860e0ec791a4292 |
| created | AssignmentRelationship | Plate mill building | Mill floor node | id-115de4c51cd4490b8c2950ec47542f55 |
| created | AssignmentRelationship | Comms room | PlantGate node | id-8436dfd673dc4dd9832441177db2c83b |
| created | AssociationRelationship | OrderSight must not swallow MillOS | On-prem app server | id-8734853a12894a10b0b0b6577eab080c |

## Candidate disposition
| Candidate | Disposition | Target |
|-----------|-------------|--------|
| Mill floor node | captured | element @ Technology and Physical |
| On-prem app server | captured | element @ Technology and Physical |
| PlantGate node | captured | element @ Technology and Physical |
| Plate mill building | captured | element @ Technology and Physical |
| Comms room | captured | element @ Technology and Physical |
| Rolling equipment | captured | element @ Technology and Physical |
| MillOS hosting | folded | reused app + Realization to On-prem app server |
| WorksERP hosting | folded | reused app + Realization to On-prem app server |
| PlantGate hosting | folded | reused app + Realization to PlantGate node |
| OrderSight hosting | out-of-scope | omitted from all nodes (brief + approve) |
| Work packages | out-of-scope | freeze |
| WMS/TMS/data lake/ERP replacement | out-of-scope | freeze |

## Traceability
- Requirement "OrderSight must not swallow MillOS" ↔ On-prem app server (Association)
- MillOS → Mill schedule capability (Realization)
- WorksERP → Order capability (Realization)
- PlantGate → Promise capability (Realization)
- Trace rel ids: ['id-8734853a12894a10b0b0b6577eab080c', 'id-bd5a755261de4b5293d81ad5d1db6d33', 'id-2cf9b9ec9afd4bddbf6b651d7fcf6036', 'id-3f4184aeef1f48c58ddd2064108a369c']
- Gap (by design): OrderSight has no tech host; PromiseSheet not hosted this job

## Model QA
- work_package_count: 0
- nodes: 3; facilities: 2; equipment: 1; apps: 5
- OrderSight != MillOS; OrderSight not on mill app-server / not on tech view
- PlantGate has no equipment relationship
- evidence first line ok on new elements
- no WMS/TMS/data lake/ERP replacement
Pass checks:
```json
{
  "view_named_technology_and_physical": true,
  "facility_or_equipment_assigned_to_node": true,
  "ordersight_millos_separate": true,
  "ordersight_not_on_mill_appserver": true,
  "millos_workserp_on_onprem": true,
  "plantgate_on_plantgate_node": true,
  "plantgate_no_equipment_link": true,
  "work_package_count_0": true,
  "no_forbidden_systems": true,
  "evidence_ok": true,
  "model_as_is": true,
  "layout_excellent": true
}
```

## Layout
- assess-layout overallRating: **excellent**
- PNG: docs/runs/job-05-technology-and-physical.png
- Note: id-6e83b113439e4ca9ab235d711a6bea04

## Documentation
- View documentation updated with rationale sections
- job-05-rationale.md / job-05-completion-summary.md written (schema ok)

## get-model-info (final)
```json
{
  "name": "Hatherley Plate Ltd",
  "elementCount": 33,
  "relationshipCount": 41,
  "viewCount": 5,
  "specializationCount": 0,
  "elementTypeDistribution": {
    "Capability": 4,
    "BusinessRole": 4,
    "BusinessProcess": 4,
    "ApplicationComponent": 5,
    "Node": 3,
    "Facility": 2,
    "Equipment": 1,
    "Stakeholder": 6,
    "Driver": 1,
    "Goal": 1,
    "Outcome": 1,
    "Requirement": 1
  },
  "relationshipTypeDistribution": {
    "AssociationRelationship": 13,
    "InfluenceRelationship": 1,
    "RealizationRelationship": 8,
    "AssignmentRelationship": 8,
    "TriggeringRelationship": 3,
    "ServingRelationship": 8
  },
  "layerDistribution": {
    "Strategy": 4,
    "Business": 8,
    "Application": 5,
    "Technology": 3,
    "Physical": 3,
    "Motivation": 10
  },
  "approvalMode": false
}
```

## Concerns
- none blocking. Hosting uses Realization Node→App because Assignment Node↔App is illegal on this bridge (documented).

## Next
Draft checkpoint (CP-G7). No git commit.
