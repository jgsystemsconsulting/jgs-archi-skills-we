<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

## Purpose
Show the as-is shop-floor chain from customer promise through works order and mill schedule to plate rolling so plant and sales readers can follow one path without new systems on the canvas.

## Stakeholders and Concerns
Plant Manager, Head of Sales, Operations Planner, and MES Owner need the promise-to-rolling chain readable. CRM Programme Manager and Integration Lead stay off-canvas; job-01 stakeholder IDs are reused only. PromiseSheet remains the named pain in narrative, not an application element.

## Viewpoint
Business Process viewpoint. View name Production Operations.

## Questions Answered
How does a customer promise become a works order, mill schedule, and plate rolling today? Which business roles perform each step on the as-is path?

## Assumptions
Named systems (PromiseSheet, WorksERP, MillOS, OrderSight, PlantGate) are wording only this job. Job-02 capabilities stay off this canvas. Motivation stakeholders are not duplicated as second Stakeholder elements; Business Role elements carry assignment on the operations view.

## Decisions
Four business processes with plain brief names: Promise, Works order, Mill schedule, Plate rolling. Four Business Role elements on canvas matching the primary audience. Triggering chain left to right. Assignment from roles to processes. One PromiseSheet pain note below the content.

## Exclusions
Application components, nodes, work packages, second site, costing, MES rewrite, WMS, TMS, data lake, ERP replacement. Job-02 capability redraw. Motivation redraw. CRM Programme Manager and Integration Lead on-canvas placement.

## Open Questions
None blocking. First generation is a draft checkpoint (CP-G7). Later SOAM jobs add application usage and technology.
