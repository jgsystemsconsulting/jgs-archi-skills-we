<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Rationale - Hatherley Plate Job 04

Application Usage viewpoint under the org view name Application Support. Sales, mill, and integration need to see which named systems hold promises, works orders, and mill schedule on the already-modelled operations chain.

Five ApplicationComponents match the plant brief names. OrderSight and MillOS are separate elements so the CRM pilot is not drawn as the MES. PromiseSheet is modelled as the as-is pain application. PlantGate is documented as the OrderSight-to-WorksERP bridge only and does not talk to mill equipment; no node or equipment elements this job.

Job-03 processes are reused on the canvas with Serving links from the apps that hold each step. Job-02 capabilities stay off-canvas. No WMS, TMS, data lake, ERP replacement, or work packages.

Draft only (CP-G7).
