<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

## Views Touched
- Production Operations (created; viewpoint business_process; id-c189cce2288642d8b1cf3c267270d571)
- Motivation Overview (left intact)
- Capability Map (left intact)

## Decisions
- Four BusinessProcess elements: Promise, Works order, Mill schedule, Plate rolling
- Four BusinessRole elements on canvas: Plant Manager, Head of Sales, Operations Planner, MES Owner
- Job-01 Motivation Stakeholders reused, not duplicated; CRM Programme Manager and Integration Lead off-canvas
- Job-02 capabilities omitted from this view
- PromiseSheet documented as pain note and narrative only (not an application)
- Triggering chain Promise → Works order → Mill schedule → Plate rolling
- Assignment edges from roles to processes
- Zero new applications or nodes

## Open Questions
- None blocking for this draft checkpoint

## Confirmation Status
- approved

## Specialists Run
- archi-business
- archi-model-qa (light)
- archi-layout
- archi-documentation

## Deliberately Deferred
- application components and usage
- technology and physical nodes
- implementation and migration work packages
- cross-layer traceability to job-01 goal and job-02 capabilities

## Improve Next
- Application-usage job can bind WorksERP / MillOS / OrderSight / PlantGate without inventing replacements
- Optional realization or serving links from processes to job-02 capabilities in a later traceability pass
