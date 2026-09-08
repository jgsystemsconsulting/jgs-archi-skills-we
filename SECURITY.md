<!-- Copyright (c) 2026 JG Systems Consulting Ltd. Source: https://github.com/jgsystemsconsulting/jgs-archi-skills-we. See LICENSE. -->
<!-- SPDX-License-Identifier: MIT -->

# Security Policy

## Reporting a vulnerability

Report security issues privately via GitHub security advisories on this
repository (Security, Advisories, New advisory), or open a pull request with
the fix when that is safe. Do not open a public issue for a suspected
vulnerability.

We aim to acknowledge reports within 5 business days. Include the affected
version (see RELEASE-INFO.txt), reproduction steps, and impact.

## Scope notes

This repository holds fictional ArchiMate models, prompt packs, and view
exports. Sensitive surfaces are: the `.archimate` files on disk, documentation
fields inside those models, and any live Archi Bridge endpoint the operator
points at while replaying a job. The repo does not hold API keys and does not
phone home.

Skill defects belong on
[jgs-archi-skills](https://github.com/jgsystemsconsulting/jgs-archi-skills).
Bridge defects belong on
[jgs-archi-mcp](https://github.com/jgsystemsconsulting/jgs-archi-mcp).

## General support

Non-security questions: open a bug report using the issue form. Do not use
the advisory channel for ordinary defects.
