<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Defect log

One row per hit during a live run. Empty at v1 ship.

| Job | Date | Skill or gate | What happened | What we did |
|-----|------|---------------|---------------|-------------|
| 1 | 2026-09-07 | MCP mutate / CommandStack | View Plan approved. Every write (`create-element`, `get-or-create-element`, `update-model`, batch commit) returned `MUTATION_FAILED: Mutation failed on UI thread`. Reads worked. Model Hatherley Plate Ltd empty, `approvalMode=false`, GUI_ATTACHED. Likely CommandStack not attached (no diagram editor open). | Refused to invent architecture. Logged. Did not start job 2. |
