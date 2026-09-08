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
`master` is three commits ahead of origin (Hatherley live run, Moorfield
seed, Moorfield live run). Not pushed.

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
9. Push WE `master` (three local commits) only after steps 5 to 8, or
   push now as private backup and flip visibility after the README
   rewrite. Do not flip public while README still says the jobs were
   not run.

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

## Out of scope for this release

Client anonymisation (none to do). IEEE rewrite. SysML bridge. Third
fictional firm. GitHub Actions against Archi. Claiming the PNG pack
replaces a live Archi session.
