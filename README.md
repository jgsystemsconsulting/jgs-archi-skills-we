<!-- Copyright (c) 2026 JG Systems Consulting Ltd. Source: https://github.com/jgsystemsconsulting/jgs-archi-skills-we. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# jgs-archi-skills-we

<p align="center">
  <img src="https://img.shields.io/badge/licence-MIT-green" alt="Licence: MIT">
  <img src="https://img.shields.io/badge/version-0.1.0-green" alt="Version 0.1.0">
  <img src="https://img.shields.io/badge/canvas-Archi-orange" alt="Canvas: Archi">
</p>

**Open the mill model. Archi stays the system of record.**

Worked examples for [jgs-archi-skills](https://github.com/jgsystemsconsulting/jgs-archi-skills).
Two fictional SOAM runs live in Archi: a UK plate mill, and a training UAS
range. You can look at the finished views without running an agent. You can
replay a job from a paste fence and stop at the View Plan gate.

These are author-run frozen briefs, not client engagements. No speedup claim.

## Install

You need Archi 5.7+ to open the models. To replay a job you also need the
[JGS Archi Bridge](https://github.com/jgsystemsconsulting/jgs-archi-mcp) and
the [skill pack](https://github.com/jgsystemsconsulting/jgs-archi-skills).
Python 3.10+ (standard library only) for the release gate.

```bash
git clone https://github.com/jgsystemsconsulting/jgs-archi-skills-we
cd jgs-archi-skills-we
```

Open `models/hatherley-plate.archimate` in Archi. That is the mill. Do not
open the `.seed.archimate` copy unless you are resetting a run.

## Usage

Hatherley Plate Ltd is the public walk. Five views:

| View | What to look at |
|------|-----------------|
| Motivation Overview | OrderSight must not swallow MillOS |
| Capability Map | Promise, Order, Mill schedule, Collect |
| Production Operations | Shop-floor chain. No applications on this view |
| Application Support | MillOS, WorksERP, PromiseSheet, OrderSight, PlantGate stay distinct |
| Technology and Physical | Rolling equipment assigned to the mill-floor node |

PNG exports: `docs/runs/job-01-motivation-overview.png` through
`docs/runs/job-05-technology-and-physical.png`. Captions are not a substitute
for opening Archi.

Moorfield Range (Hawker Range Systems Ltd) is the same method with aerospace
and defence nouns. Open `models/moorfield-range.archimate`. Do not model the
air vehicle as product structure. SysML stays off this canvas.

Replay: paste a fence from `prompts/` (mill) or `prompts/moorfield/` (range)
into an agent that has the skill pack. Specialists stay
orchestrator-dispatched. Nothing mutates until you approve the View Plan.
Confirm `get-model-info` names the model you meant. Open a diagram editor
before the first write. After a passed job: File, Save in Archi.

Full operator notes: [docs/how-to-run.md](docs/how-to-run.md). Briefs:
[docs/plant-brief.md](docs/plant-brief.md),
[docs/moorfield-brief.md](docs/moorfield-brief.md).

## Licence

MIT. See [LICENSE](LICENSE). To request a commercial or academic licence for
JGSC Labs products, or if you are unsure which licence you need, use
https://labs.jgsystemsconsulting.com/licensing.html.

## Support

- Defect in an example, prompt, or model file: GitHub issue form on this repo.
- Skill pack defect: [jgs-archi-skills](https://github.com/jgsystemsconsulting/jgs-archi-skills).
- Bridge defect: [jgs-archi-mcp](https://github.com/jgsystemsconsulting/jgs-archi-mcp).
- Security: private GitHub advisory. See [SECURITY.md](SECURITY.md).
