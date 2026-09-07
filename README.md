<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Hatherley Plate worked example

Private sequenced SOAM run for the landing-page plant story: as-is shop
floor plus the CRM programme that is supposed to fix order visibility.
Archi stays the system of record. This repository holds the script, the
seed model, and (after live jobs) the working model.

This is not a finished architecture. v1 does not run the jobs.

## Prerequisites

- Archi 5.7+
- [JGS Archi Bridge](https://github.com/jgsystemsconsulting/jgs-archi-mcp)
- [jgs-archi-skills](https://github.com/jgsystemsconsulting/jgs-archi-skills)
  installed for ZCode
- Python 3.10+ (standard library only)

## Start

Open `models/hatherley-plate.archimate` in Archi. Start the Bridge at
`http://127.0.0.1:18090/mcp`. Paste job 1 from `prompts/01-motivation.md`.

Full operator notes: [docs/how-to-run.md](docs/how-to-run.md). Frozen
facts: [docs/plant-brief.md](docs/plant-brief.md). Job order:
[prompts/README.md](prompts/README.md).

Do not invoke layer specialists. Do not paste element-create commands.
