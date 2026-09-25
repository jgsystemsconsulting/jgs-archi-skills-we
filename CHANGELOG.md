<!-- Copyright (c) 2026 JG Systems Consulting Ltd. Source: https://github.com/jgsystemsconsulting/jgs-archi-skills-we. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Changelog

Single-source history for jgs-archi-skills-we. Tags are three-component semver
(`vMAJOR.MINOR.PATCH`).

## [Unreleased]

## [0.2.0] - 2026-09-25

Public surface cut. The repo is public, the landing page is live, and the release gate checks product content.

- README states the three-repo split: Bridge, skill pack, this evidence checkout.
- Repository flipped public. Landing page live at
  https://jgsystemsconsulting.github.io/jgs-archi-skills-we/ with the five
  Hatherley views, the Moorfield range, install, and the replay first-run.
- Pages site aligned to the JGS family standard, favicon included.
- Branch protection on `master`: pull request plus the `integrity` check.
- Replay-loop diagram added to `docs/how-to-run.md`.
- Release gate hardened: product-content checks (ArchiMate models and views)
  and identical checks in local `scripts/check_release.py` and CI `validate.yml`.
- Site version gate: `docs/index.html` JSON-LD, masthead, and footer versions
  must equal `RELEASE-INFO.txt`.

## [0.1.0] - 2026-09-08

First worked-example cut. Two fictional SOAM runs in Archi.

- Hatherley Plate Ltd: mill as-is plus CRM visibility. Five views.
- Hawker Range Systems Ltd (Moorfield Range): training UAS as-is. Five views.
  Air-vehicle SysML stays off the canvas.
- Sequenced `/archi-orchestrator` pastes, view plans, specialist results, named
  view PNGs, empty seed models plus saved working models.
- Operator lessons: open a view before first mutate; restart MCP on UI-thread
  fail; File, Save after every passed job.
