<!-- Copyright (c) 2026 JG Systems Consulting Ltd. Source: https://github.com/jgsystemsconsulting/jgs-archi-skills-we. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Contributing

This repository is MIT-licensed. Fork it, add a replay note, and send a pull
request if the change belongs upstream.

Skill and Bridge defects do not belong here. File those on
[jgs-archi-skills](https://github.com/jgsystemsconsulting/jgs-archi-skills)
or [jgs-archi-mcp](https://github.com/jgsystemsconsulting/jgs-archi-mcp).

## Local setup

Python 3.10+, no extra packages. Archi 5.7+ to open the models.

```bash
python scripts/check_release.py
```

Open `models/hatherley-plate.archimate` (mill) or
`models/moorfield-range.archimate` (range). Do not open the `.seed.archimate`
files unless you are resetting a run.

Optional replay: paste a fence from `prompts/` into an agent with the skill
pack installed. Stop at the View Plan gate.

## Pull requests

One concern. No tokens, keys, or live client model content. You have the
right to license the contribution under the MIT License in LICENSE.
