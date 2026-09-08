<!-- Copyright (c) 2026 JG Systems Consulting Ltd. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Release-ready plan: worked examples

Date: 2026-09-08. Status: proposed. Live runs exist for Hatherley Plate and
Moorfield Range. This note is the quality bar and the sequence to make one
of them public without pretending both are finished adoption assets.

## Goal

Ship one public worked walk that an architect can open in Archi and
believe. Hatherley Plate is that walk. Moorfield Range stays a second
model in the same repository until a defence talk needs it. The public
skills pack keeps its three one-liners. The walk sits behind them as
proof, not as a replacement for a ten-second paste.

## Current state (2026-09-08)

Private repository `jgsystemsconsulting/jgs-archi-skills-we`. Local
`master` is four commits ahead of origin (Hatherley live run, Moorfield
seed, Moorfield live run, this plan). Not pushed.

| Surface | State |
|---------|--------|
| Hatherley `.archimate` | Saved live model, five views, 67 KB. Seed file still empty. |
| Moorfield `.archimate` | Saved live model, five views, 71 KB. Seed file still empty. |
| Prompt packs | Five self-contained pastes per example. Records filled. |
| Run docs | View plans, specialist results, named view PNGs, ID maps. |
| Public skills pack | Pointer still says Hatherley is private and will be published after the first live run. That sentence is now stale. |
| Landing page | Three one-liners. No link to a finished mill. No Moorfield. |
| Implementation/migration | Not modelled. Landing-page TMS run remains a one-liner only. |

Honesty line for any public page: two author-run frozen briefs exist in
Archi. They are not client engagements. No speedup claim.

## Release Repo Standard (same bar as jgs-archi-skills)

Profile: **Base only** (`RR-B`). Open-source MIT. Standalone repo. Not a
skills pack (`RR-S` N/A: no `skills/`, no installer, no host marketplace
manifests) and not an MCP bridge (`RR-M` N/A).

Auditor (`audit.py`, Base profile) on 2026-09-08: **9 FAIL, 2 WARN, 13 PASS**.
The skills pack on the same tool: 2 FAIL (commit-identity history and
diagram HTML em dashes), 23 PASS. WE must reach the same Base MUST set
the skills pack already ships. Do not copy RR-S files (`install.py`,
`SKILLS.md`, `.claude-plugin/`) into WE.

### Auditor FAILs (MUST, blocking)

| ID | Gap | Fix |
|----|-----|-----|
| RR-B-05 | README missing Usage and Support; missing licence-enquiry URL | Rewrite README with those H2s. Licence section must contain `https://labs.jgsystemsconsulting.com/licensing.html` as a raw https URL. |
| RR-B-07 | no SECURITY.md | Copy skills-pack SECURITY.md, retarget advisory URL to this repo, rewrite Scope notes for model files and PNGs (no MCP tools in this repo). Advisory route, not email. |
| RR-B-08 | no CHANGELOG.md | Add changelog. First released entry `0.1.0` after the public walk exists. Keep `## [Unreleased]`. |
| RR-B-09 | no version | Single version `0.1.0` in CHANGELOG, RELEASE-INFO.txt, CITATION.cff, README badge. Bump together. |
| RR-B-10 | no RELEASE-INFO.txt | `Product: jgs-archi-skills-we` / `Version: 0.1.0` / `Built: <UTC>` / `Tag: v0.1.0`. |
| RR-B-15 | no gate script, no CI | `scripts/check_release.py` listing WE required files (legal set, README, CHANGELOG, RELEASE-INFO, CITATION, SECURITY, CONTRIBUTING, CoC, models, prompt READMEs). `.github/workflows/validate.yml` inlines the same checks and MUST NOT execute checked-out Python from this repo (same pattern as the skills pack). |
| RR-B-28 | em dash in seven run reports | Strip U+2014 from those seven files (Hatherley job-01 orchestrator report; both examples' job-05 completion, orchestrator report, specialist result). Public README/how-to/landing: avoid-ai-writing + `prose_check.py`. |
| RR-B-31 | no CITATION.cff | Org-authored CFF, version 0.1.0, `repository-code` this repo, MIT. |
| RR-B-32 | no bug form, no chooser | `.github/ISSUE_TEMPLATE/bug_report.yml` + `config.yml` (`blank_issues_enabled: false`, security advisory contact, sibling link to jgs-archi-skills for pack defects). SHOULD: `skill_improvement.yml` renamed or an `example-improvement.yml`. |

### Auditor WARNs

- RR-B-24: no `docs/*.html` yet. Phase A companion page in the skills pack
  (`docs/hatherley.html` using `site.css`) carries the mechanical taste
  overlay. WE itself MAY stay markdown-only if Pages is the skills-pack
  site. If WE enables GitHub Pages, it needs `docs/index.html` + shared
  CSS and `landing_taste.py` zero hits.
- RR-B-32 improvement form: add with the bug form.

### OSS posture extras (RR-B-12 MUST when MIT)

Copy and retarget from the skills pack: `CONTRIBUTING.md`,
`CODE_OF_CONDUCT.md`, `.github/pull_request_template.md`. CONTRIBUTING
setup commands become: open the named `.archimate`, optional replay of
job 1, `python scripts/check_release.py`. No `install.py`.

### N/A (do not cargo-cult from the skills pack)

RR-S entire profile. RR-B-29 host marketplace manifests. RR-B-16
agent-install prompt (this repo is not installed as skills). `SKILLS.md`,
`install.py` / `.sh` / `.ps1`, `.claude-plugin/`, `.cursor-plugin/`,
`.agents/plugins/`, `gemini-extension.json`.

RR-B-29b / RR-M-07b directory submissions: N/A (not an agent plugin).

### SHOULD after files exist (Phase A publish)

- RR-B-18: tag `v0.1.0` when CHANGELOG has a released entry.
- RR-B-21: GitHub About description as search snippet; topics include
  `archimate`, `archi`, `soam`.
- RR-B-22: GitHub Release notes include the licence-enquiry URL.
- RR-B-23: branch protection on `master` after the repo is public
  (solo-maintainer shape, same as the skills pack).
- RR-B-20: landing either this repo's Pages or the skills-pack
  companion page. Licence-enquiry URL on that HTML.
- Re-run the auditor until FAIL count is 0. Then add the GitHub platform
  flags once the repo is public.

### Verify command (done means this is green)

```text
python ~/.zcode/skills/release-repo-standard/tools/audit.py --repo . --profile base
python scripts/check_release.py
```

Exit 0 on both. MANUAL list still walked by a human (usage-doc depth,
landing content, taste-skill if HTML exists).

## Quality bar (release, not "files exist")

A public walk fails if any of these fail.

### Model

- Open in Archi 5.7+ with no repair dialog.
- Model name matches the brief (Hatherley Plate Ltd / Hawker Range Systems Ltd).
- Exactly the five named views. No scratch views, no duplicate "Live Smoke"
  leftovers, no empty Default View.
- Freeze visible on the canvas, not only in a specialist markdown file:
  CRM/MES (or RangePlan/AirStack/GroundOS) remain separate applications;
  at least one equipment or facility assigned to a node; zero work
  packages on the as-is picture.
- Documentation first lines still start with `Evidence:`. Spot-check ten
  elements after any layout pass.
- Seed file remains the empty native tree. Working file is the live
  model. README says which to open.

### Pictures

Named PNGs in `docs/runs/` are talk assets. They are not a substitute
for opening Archi, but they are what LinkedIn and the companion site
will show. Bar:

- One PNG per named view, exported from Archi at a readable width
  (roughly 1600 px or the Bridge export default if that is already
  sharp).
- No truncated names, no overlapping boxes that hide a freeze element,
  no "note soup" covering the spine.
- Caption under each image on the public page: view name, who it is
  for, one sentence of what to look at (the refuse constraint, not a
  tour of every box).
- Job 1 Hatherley layout was scored fair in the live run. Re-export
  Motivation Overview after a layout pass if crossings still fight a
  slide. Moorfield job 1 had the same fan-in. Fix both or caption
  "overview density, open Archi for the readable copy."

Human visual gate: look at all five Hatherley PNGs on a laptop and on a
phone-width window. If a freeze element is unreadable, it is not
release-ready. Do not treat a clean `prose_check` as a visual pass.

### Prose

Every public markdown page (WE README, how-to-run, example landing
section, skills-pack pointer) goes through avoid-ai-writing (technical
  voice, edit) and `python ~/.zcode/scripts/prose_check.py`. Zero em
dashes in body prose. No "it's not X, it's Y." No speedup, no industry
adoption, no marketing smoothness. Copyright HTML comment false
positives may remain.

Specialist-result files and view plans stay in the repo as run evidence.
They do not need a marketing rewrite. They must not contradict the
public captions.

### Operator path

A stranger with Archi 5.7+, the Bridge, and the skills pack can:

1. Clone or download the worked-example repo.
2. Open the working `.archimate` (not the seed).
3. See the five views without running an agent.
4. Optionally replay job 1 from the paste fence and stop at the View
   Plan gate (nothing mutates until they approve).

How-to-run must state, in this order: open the named model; confirm
`get-model-info` name; open a diagram editor before first mutate;
restart MCP if `MUTATION_FAILED` on the UI thread; File → Save after
every passed job. Those three live-run failures are part of the product
now.

### Claims

Allowed: method (gated run, Archi as system of record, language in MCP
resources), two completed as-is pictures, freeze constraints held,
operator lessons.

Forbidden: client names, "production use," timing percentages, "the
community has adopted this," SysML replacement, ArchiMate as a combat
system model.

## What to publish, and in what order

### Phase A. Make Hatherley the public walk (this release)

Public repository (flip `jgs-archi-skills-we` to public, or publish a
sanitised copy). Recommended: flip this repo. History already contains
only fictional mills and ranges.

Contents of the public hero:

- README rewritten as a walk, not a seed disclaimer. Lead with "open
  this model." Then the five view names with PNG + one-line caption.
  Then "replay" (paste job 1, stop at the gate).
- `models/hatherley-plate.archimate` as the open file.
- `prompts/01` through `05` unchanged in method (self-contained
  pastes).
- `docs/plant-brief.md` and `docs/how-to-run.md` with the operator
  lessons.
- Five PNGs on a companion-site page in the skills pack
  (`docs/hatherley.html` or a section on `index.html`). Skills README
  and `docs/skill-usage.md` replace the stale "maintained privately"
  sentence with a URL.

Refuse moment: one extra figure or a short GIF. View Plan confirmation
gate, architect replies abort or revise, model counts unchanged. That
figure is more persuasive than a sixth architecture view.

Moorfield: linked from README as "same method, aerospace and defence
nouns" with a warning that SysML stays off the canvas. Not the hero.
No extra companion page until Phase C.

### Phase B. Pack and landing copy (same release window)

- Skills README / skill-usage: one paragraph, clone URL, "open the
  mill model." Still list the three one-liners first.
- `docs/papers/landing.md` and companion `index.html`: optional fourth
  line under Three runs, "Worked mill model (Hatherley Plate)" with
  the GitHub and Pages URLs. Do not bury the one-liners.
- `why-soam.md` status box: move "worked-run reports" from community-
  dependent toward evidence, with the honest qualifier (author-run
  frozen brief).

No change to IEEE cuts in this phase.

### Phase C. Moorfield as the A&D room (after A is live)

- Companion page or a section on the Hatherley page.
- Caption the SysML boundary in one sentence.
- Do not lead LinkedIn with UAS if the audience is general EA.

### Phase D. Intentionally later

- One migration job on Moorfield or a named TMS: plateaus and work
  packages, operating model untouched. Fills landing-page run 3.
- Invoice-to-cash as a third full model. Skip until someone asks.
- Automated eval against these mills. Meridian Freight stays the
  frozen eval scenario.

## Visual and editorial work list (Phase A)

Do these in Archi, then re-export PNGs, then edit public prose. Do not
publish the current PNGs without a human look.

1. Open Hatherley working model. Walk all five views at 100% zoom.
   Fix overlap, truncated labels, notes covering freeze elements.
   Motivation Overview first (known fair layout).
2. Confirm folder placement matches house style enough for a stranger
   (Motivation / Strategy / Business / Application / Technology &
   Physical / Views). Nested folders are fine.
3. Export five PNGs to replace `docs/runs/job-0N-*.png` if the on-disk
   exports are soft or cropped.
4. Same pass on Moorfield if it will be linked at all from the public
   README (even as a secondary model). Launch equipment on the range-
   floor node must be visible.
5. Rewrite WE README. Delete "v1 does not run the jobs." State what
   the visitor opens.
6. Rewrite how-to-run as two tracks: "look at the finished mill" and
   "replay from job 1."
7. Skills-pack pointer + companion page with five figures and the
   refuse caption.
8. `prose_check` and avoid-ai-writing on every new public page.
9. Apply the Release Repo Standard Base file set (SECURITY, CHANGELOG,
   RELEASE-INFO, CITATION, CONTRIBUTING, CoC, PR template, issue
   forms, `scripts/check_release.py`, inline CI). Version `0.1.0`.
   Strip em dashes from the seven run reports the auditor named.
10. Re-run the Base-profile auditor until FAIL is 0.
11. Push WE `master` as private backup if wanted. Flip public only after
    README no longer says the jobs were not run, and after step 10.

## Skill and Bridge follow-ups (not a blocker for Phase A)

These came out of the live runs. They improve the next adopter's first
mutate. They are not required to publish a finished `.archimate`.

- Skills: abort text when CommandStack is missing (empty model, no
  diagram editor). Completion summary: "Save in Archi."
- Bridge (upstream issue, not a PR from the skills repo): mutation
  error should name missing CommandStack; consider a save tool; document
  Node hosts Application (Assignment rejected; Realization plus nesting
  used).
- Pack note: Capability-Capability Flow/Association dropped on both
  live maps; spatial order is the current legal overview.

## Verification for "release-ready"

- WE README opens with the mill, names the five views, links PNGs,
  links the working `.archimate`.
- Stranger test: clone, open model, five views present, freeze
  elements findable without the specialist markdown.
- Skills README no longer says the example is unpublished.
- Companion page: five figures, refuse caption, no em dash, no
  speedup.
- `python -m unittest discover -s tests -q` in the skills pack still
  green after the pointer edit.
- WE `git status` clean on the files the public will see. Scratch
  (`docs/runs/**/*.py`, transcripts, slices) stays gitignored.
- Base-profile `audit.py` FAIL count 0. `python scripts/check_release.py`
  exit 0.

## Out of scope for this release

Client anonymisation (none to do). IEEE rewrite. SysML bridge. Third
fictional firm. GitHub Actions against Archi. Claiming the PNG pack
replaces a live Archi session.
