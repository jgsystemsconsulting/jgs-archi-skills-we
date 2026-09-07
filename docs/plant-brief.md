<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Hatherley Plate Ltd (frozen)

Independent UK plate mill. One site: Hatherley Works, Rotherham. Hot-rolled
carbon plate for construction and heavy OEM. Not Meridian Freight. Not a
multi-site group.

This brief is the fact freeze for the sequenced SOAM jobs. Prompt files
cite it. The agent must not invent extra scope.

## Roles

- Plant Manager
- Head of Sales
- MES Owner
- CRM Programme Manager
- Operations Planner
- Integration Lead

## Named as-is systems

- MillOS: MES. Owns mill schedule. Never drawn as replaced by CRM.
- WorksERP: on-site ERP. Works orders, invoices, plate stock. Not replaced
  this run.
- PromiseSheet: shared-drive spreadsheet. Customer promises. The pain.
- OrderSight: CRM in pilot. Sales-facing. Funded for visibility only.
- PlantGate: integration gateway in the comms room. Bridges OrderSight
  promises to WorksERP works orders. Does not talk to mill equipment.

## Physical (job 5)

- Plate mill building
- Comms room
- Rolling equipment on a mill-floor node
- On-prem app server node hosting MillOS and WorksERP
- PlantGate on a node in the comms room

## Motivation spine (job 1)

- Driver: promised plate dates do not match mill reality.
- Goal: sales and mill share one order identity from promise to schedule.
- Outcome: Plant Manager and Head of Sales can answer "is this order on
  the mill this week?" without PromiseSheet.
- Requirement: OrderSight must not swallow MillOS.

## Hard freeze

- OrderSight and MillOS stay separate applications.
- Shared order identity, not one merged blob.
- At least one equipment or facility element assigned to a node.
- No work packages, no second site, no costing, no MES rewrite.
- Do not invent WMS, TMS, data lake, or ERP replacement.
