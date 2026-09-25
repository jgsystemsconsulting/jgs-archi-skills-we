# Copyright (c) 2026 JG Systems Consulting Ltd. Source: https://github.com/jgsystemsconsulting/jgs-archi-skills-we. See LICENSE.
# SPDX-License-Identifier: MIT
"""Release gate (RR-B-15): required files, forbidden paths, forbidden
content (including .archimate models), headers present, BOM, version
consistency, ArchiMate product content. Exits non-zero on any failure.

CI (validate.yml) inlines the same checks and MUST NOT execute this file.
Run locally: python scripts/check_release.py
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys
import xml.etree.ElementTree as ET


def check_site_version(root, release_re):
    """docs/index.html version strings must equal RELEASE-INFO.txt (ported from jgs-lit-memory)."""
    m = re.search(release_re, (root / "RELEASE-INFO.txt").read_text(encoding="utf-8"), re.M)
    if not m:
        return ["RELEASE-INFO.txt: no version line"]
    expected = m.group(1)
    page = (root / "docs" / "index.html").read_text(encoding="utf-8")
    loci = {
        "softwareVersion": r'"softwareVersion":\s*"(\d+\.\d+\.\d+)"',
        "masthead REV": r"REV <b>(\d+\.\d+\.\d+)</b>",
        "footer Rev": r'<span class="label">Rev</span><b>(\d+\.\d+\.\d+)</b>',
    }
    bad = []
    for name, pat in loci.items():
        v = re.search(pat, page)
        val = v.group(1) if v else None
        if val != expected:
            bad.append(f"{name}={val!r} (expected {expected})")
    if bad:
        return ["site page version mismatch or missing pattern: " + "; ".join(bad)]
    print(f"site page versions agree at {expected}")
    return []


fails: list[str] = []

# Mirror: .github/workflows/validate.yml step "Required files". Edit both.
REQUIRED = [
    "LICENSE",
    "COPYRIGHT",
    "NOTICE",
    "README.md",
    "CHANGELOG.md",
    "RELEASE-INFO.txt",
    "CITATION.cff",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    ".gitignore",
    "docs/plant-brief.md",
    "docs/moorfield-brief.md",
    "docs/how-to-run.md",
    "models/hatherley-plate.archimate",
    "models/hatherley-plate.seed.archimate",
    "models/moorfield-range.archimate",
    "models/moorfield-range.seed.archimate",
    "prompts/README.md",
    "prompts/moorfield/README.md",
    "docs/index.html",
    "docs/site.css",
    "docs/runs/job-01-motivation-overview.png",
    "docs/runs/job-02-capability-map.png",
    "docs/runs/job-03-production-operations.png",
    "docs/runs/job-04-application-support.png",
    "docs/runs/job-05-technology-and-physical.png",
    "prompts/01-motivation.md",
    "prompts/02-capability.md",
    "prompts/03-operations.md",
    "prompts/04-application.md",
    "prompts/05-technology-closeout.md",
    "prompts/moorfield/01-motivation.md",
    "prompts/moorfield/02-capability.md",
    "prompts/moorfield/03-operations.md",
    "prompts/moorfield/04-application.md",
    "prompts/moorfield/05-technology-closeout.md",
]
for f in REQUIRED:
    if not pathlib.Path(f).is_file():
        fails.append(f"required file missing: {f}")

tracked = subprocess.run(
    ["git", "ls-files"], capture_output=True, text=True, check=True
).stdout.splitlines()
FORBIDDEN_PATH_PARTS = [
    "__pycache__",
    ".venv",
    ".worktrees",
    ".pytest_cache",
    ".ruff_cache",
    ".bak",
]
for f in tracked:
    if any(part in f for part in FORBIDDEN_PATH_PARTS):
        fails.append(f"forbidden tracked path: {f}")

FORBIDDEN_CONTENT = [
    re.compile(r"BEGIN [A-Z ]*PRIVATE KEY"),
    re.compile(r"CONFIDENTIAL\s+[-—]\s+Not for external distribution"),
]
for f in tracked:
    if f.startswith(".github/"):
        continue
    # Mirror: .github/workflows/validate.yml step "Forbidden content" suffix tuple. Edit both.
    if not f.endswith(
        (".py", ".md", ".txt", ".yml", ".yaml", ".json", ".cff", ".html", ".archimate")
    ):
        continue
    if not pathlib.Path(f).is_file():
        continue
    text = pathlib.Path(f).read_text(encoding="utf-8", errors="ignore")
    for rx in FORBIDDEN_CONTENT:
        if rx.search(text):
            fails.append(f"forbidden content in {f}: {rx.pattern}")

HEADER_SENTINEL = "Copyright (c) 2026 JG Systems Consulting Ltd"
for f in tracked:
    if not f.endswith(".py"):
        continue
    if not pathlib.Path(f).is_file():
        continue
    head = pathlib.Path(f).read_text(encoding="utf-8", errors="ignore")[:600]
    if HEADER_SENTINEL not in head:
        fails.append(f"header missing: {f}")
    if "SPDX-License-Identifier" not in head:
        fails.append(f"SPDX missing: {f}")

fails += check_site_version(pathlib.Path("."), r"^Version:\s*(\d+\.\d+\.\d+)")

# Mirror: .github/workflows/validate.yml step "BOM check". Edit both.
BOM_SUFFIXES = (".toml", ".json", ".yaml", ".yml", ".cff")
bom = [
    f
    for f in tracked
    if f.endswith(BOM_SUFFIXES)
    and pathlib.Path(f).is_file()
    and pathlib.Path(f).read_bytes()[:3] == b"\xef\xbb\xbf"
]
if bom:
    fails.append("UTF-8 BOM in: " + ", ".join(bom))

# Mirror: .github/workflows/validate.yml step "Version consistency". Edit both.
VERSION_SOURCES = {
    "CHANGELOG": ("CHANGELOG.md", r"^##\s*\[?v?(\d+\.\d+\.\d+)"),
    "RELEASE-INFO": ("RELEASE-INFO.txt", r"^Version:\s*(\d+\.\d+\.\d+)"),
    "CITATION.cff": ("CITATION.cff", r"^version:\s*[\"']?(\d+\.\d+\.\d+)"),
}
versions = {}
for label, (path, pattern) in VERSION_SOURCES.items():
    p = pathlib.Path(path)
    m = re.search(pattern, p.read_text(encoding="utf-8"), re.M) if p.is_file() else None
    versions[label] = m.group(1) if m else None
if None in versions.values() or len(set(versions.values())) != 1:
    fails.append(f"version mismatch across sources: {versions}")

# Mirror: .github/workflows/validate.yml step "ArchiMate product content". Edit both.
XSI = "{http://www.w3.org/2001/XMLSchema-instance}type"
ROOT_TAG = "{http://www.archimatetool.com/archimate}model"
VIEW_SUFFIXES = ("DiagramModel", "SketchModel", "CanvasModel")
SEED_RATIO = 10
EXPECTED_VIEWS = {
    "models/moorfield-range.archimate": {
        "id-02bfe33f26d844a1a34a314a40a400c0": ("archimate:ArchimateDiagramModel", "Motivation Overview", "motivation"),
        "id-6967b8a5125d46e1b6ba0edbf9b9539b": ("archimate:ArchimateDiagramModel", "Capability Map", "capability_map"),
        "id-782395c6d18347a9a24da626f81ee275": ("archimate:ArchimateDiagramModel", "Range Operations", "business_process_cooperation"),
        "id-5ed7d076bfc449d78537f5468ed476fb": ("archimate:ArchimateDiagramModel", "Application Support", "application_cooperation"),
        "id-7585e12756874cd1855d73253da55504": ("archimate:ArchimateDiagramModel", "Technology and Physical", "technology_usage"),
    },
    "models/hatherley-plate.archimate": {
        "id-05f18c92556242fc8ce2a2252fc36867": ("archimate:ArchimateDiagramModel", "Motivation Overview", "motivation"),
        "id-6613e98758a3455d95e1fcc5b8e731f7": ("archimate:ArchimateDiagramModel", "Capability Map", "capability_map"),
        "id-c189cce2288642d8b1cf3c267270d571": ("archimate:ArchimateDiagramModel", "Production Operations", "business_process"),
        "id-90bb9ec6131b44f9966ac494bd89a90c": ("archimate:ArchimateDiagramModel", "Application Support", "application_usage"),
        "id-6ef45eb1bf8340f2b2eba45c4f92b9e9": ("archimate:ArchimateDiagramModel", "Technology and Physical", "technology_usage"),
    },
}
FREEZE = {
    "models/moorfield-range.archimate": ("RangePlan", "AirStack", "GroundOS", "LinkGate", "SortieBoard"),
    "models/hatherley-plate.archimate": ("OrderSight", "MillOS", "WorksERP", "PromiseSheet", "PlantGate"),
}
SEEDS = {
    "models/moorfield-range.seed.archimate": "models/moorfield-range.archimate",
    "models/hatherley-plate.seed.archimate": "models/hatherley-plate.archimate",
}


def parse_model(f):
    p = pathlib.Path(f)
    if not p.is_file():
        return None
    try:
        root = ET.parse(p).getroot()
    except ET.ParseError as exc:
        fails.append(f"model parse error in {f}: {exc}")
        return None
    if root.tag != ROOT_TAG:
        fails.append(f"wrong root tag in {f}: {root.tag}")
    return root


for f, expected in EXPECTED_VIEWS.items():
    root = parse_model(f)
    if root is None:
        continue
    els = list(root.iter("element"))
    view_els = [e for e in els if e.get(XSI, "").endswith(VIEW_SUFFIXES)]
    if len(view_els) != len(expected):
        fails.append(f"{f}: expected {len(expected)} views, found {len(view_els)}")
    found = {e.get("id"): (e.get(XSI), e.get("name"), e.get("viewpoint")) for e in view_els}
    for vid, want in expected.items():
        got = found.get(vid)
        if got != want:
            fails.append(f"{f}: view {vid} expected {want}, found {got or 'missing'}")
    for vid, got in found.items():
        if vid not in expected:
            fails.append(f"{f}: unexpected view {vid} {got}")
    if any(e.get(XSI) == "archimate:WorkPackage" for e in els):
        fails.append(f"{f}: archimate:WorkPackage present")
    apps = {e.get("name") for e in els if e.get(XSI) == "archimate:ApplicationComponent"}
    for name in FREEZE[f]:
        if name not in apps:
            fails.append(f"{f}: freeze application missing: {name}")

for seed, model in SEEDS.items():
    root = parse_model(seed)
    if root is not None:
        n = sum(1 for _ in root.iter("element"))
        if n:
            fails.append(f"seed not empty: {seed} has {n} element nodes")
    sp, mp = pathlib.Path(seed), pathlib.Path(model)
    if sp.is_file() and mp.is_file() and sp.stat().st_size * SEED_RATIO >= mp.stat().st_size:
        fails.append(
            f"seed too large: {seed} is {sp.stat().st_size} bytes, "
            f"{SEED_RATIO}x must stay below {model} ({mp.stat().st_size} bytes)"
        )

if fails:
    print("RELEASE GATE FAILED:")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
print("release gate: PASS")
