<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# How to run the Hatherley Plate jobs

Two sequenced examples share this repository. Hatherley Plate is the mill
run. Moorfield Range is the aerospace and defence run
([docs/moorfield-brief.md](moorfield-brief.md),
[prompts/moorfield/](../prompts/moorfield/)).

Do not paste job 2 until job 1 has an approved View Plan and the pass
checks hold. Do not mutate Hatherley while Moorfield is the job, or the
reverse. Confirm `get-model-info` name before the first write.

## Prerequisites

- Archi 5.7+ with the JGS Archi Bridge plugin.
- Bridge listening at `http://127.0.0.1:18090/mcp`.
- jgs-archi-skills installed for ZCode (`python install.py` in that pack).
- Python 3.10+ on PATH (standard library only).
- This working copy open. The model file is
  `models/hatherley-plate.archimate`.

## Start

1. Open `models/hatherley-plate.archimate` in Archi. The model name must
   read **Hatherley Plate Ltd**.
2. Start the MCP server in Archi. Confirm the menu shows Stop MCP Server.
3. Restart the ZCode session so it sees the skills and the MCP tools.
4. Paste the fence from `prompts/01-motivation.md` into ZCode. Nothing else.
5. Approve, revise, or abort the View Plan. Nothing is written until yes.
6. After a pass, add a row to `prompts/record.md` and commit the working
   model. Then paste the next job.

MCP down or the wrong model open: stop. Do not invent architecture.

Lessons from the first live mill run:

- Open a diagram editor (even an empty view) before the first mutate.
  Otherwise the Bridge returns `MUTATION_FAILED` on the UI thread.
- If that error still appears, MCP Server → Stop, then Start.
- After every passed job: File → Save in Archi, then commit the working
  `.archimate`. The Bridge has no save tool. Closing Archi without Save
  loses the run.

## Refuse

If the agent invents WMS, TMS, a data lake, an ERP replacement, work
packages, a second site, or draws OrderSight as replacing MillOS: refuse,
log a row in `defects/log.md`, and re-paste the same job with "do not
add X."

A refused View Plan stays on that job. Do not paste job N+1.

## Reset

If a run is trash, copy `models/hatherley-plate.seed.archimate` over
`models/hatherley-plate.archimate` and reopen the model in Archi.

## Git after a live job (later, not v1 ship)

Passed job: commit `models/hatherley-plate.archimate` and the new
`prompts/record.md` row. Failed job: defect row only, no model commit.
Never overwrite the seed file.
