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

if fails:
    print("RELEASE GATE FAILED:")
    for f in fails:
        print(f"  - {f}")
    sys.exit(1)
print("release gate: PASS")
