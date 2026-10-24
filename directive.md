# Directive: Trustworthy crypto explainer + editorial workflow
**Objective:** publish one accurate, sourced explainer that answers question A (intent.md), with a reproducible draft→review→approve→publish→update workflow.
**Scope:** one article, one diagram, one table, one synthetic worked example; a local static CMS; local git history. Not deployed.
**Requirements:** 700–1,000 words; prerequisites, limits and failure modes; Implemented / Proposal / Opinion labels; ≥3 primary sources with access dates and quotes; ≥2 revisions; one correction note; one update trigger; AI step documented.
**Completion criteria:** `python3 build.py` passes metadata and alt-text checks; every claim maps to a ledger entry; git log shows all 5 stages; the correction is visible in the article and the changelog.

## Appendix
- Live preview: [PLACEHOLDER URL: Vercel/GitHub Pages, not yet deployed]
- Repo: [PLACEHOLDER URL: not yet created]
- Loom: [PLACEHOLDER URL: to be recorded]

**Viewing steps:** `git log --oneline` → `python3 build.py --preview` (or without the flag for published only) → `python3 -m http.server -d site 8000` → open http://localhost:8000/. Use `git diff <draft> <review>` to see the fact-check revisions and `git diff <v1.0> <v1.1>` to see the correction.

**Checks run (2026-10-24):** build OK (metadata, alt text, draft gating); body prose 983 words; all 3 sources fetched and quoted; `python3 check_triggers.py` → both baselines OK.

**AI contributions:** the first draft, outline and the diagram/table structure were AI-assisted (ai-step/README.md). AI errors caught in review: C3, C5, C6, C11. One error (C10, failed-tx fees) slipped past review and was corrected in v1.1. I own every final decision.

**Limitations:** EVM-focused; issuer terms can change (hence the triggers); the trigger checker uses a date regex and needs a human to read the diff; metrics are hypotheses with no data; the CMS is minimal (no auth or roles; review is enforced by convention plus git).
