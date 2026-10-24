# Directive: Trustworthy crypto explainer + editorial workflow
**Objective:** publish one accurate, sourced explainer that answers question A (intent.md), with a reproducible draft→review→approve→publish→update workflow.
**Scope:** one article, one diagram, one table, one synthetic worked example; a local static CMS; local git history. Not deployed.
**Requirements:** 700–1,000 words; prerequisites, limits and failure modes; Implemented / Proposal / Opinion labels; ≥3 primary sources with access dates and quotes; ≥2 revisions; one correction note; one update trigger; AI step documented.
**Completion criteria:** `python3 build.py` passes metadata and alt-text checks; every claim maps to a ledger entry; git log shows all 5 stages; the correction is visible in the article and the changelog.

## Appendix
- Live site (GitHub Pages): https://pinnaclecryptng.github.io/must-stablecoin-explainer/
- Article: https://pinnaclecryptng.github.io/must-stablecoin-explainer/stablecoin-payment-exceptions/
- Changelog: https://pinnaclecryptng.github.io/must-stablecoin-explainer/changelog.html
- Repo: https://github.com/PinnacleCryptNG/must-stablecoin-explainer
- Files: [article source](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/blob/main/content/stablecoin-payment-exceptions.md) · [ledger](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/blob/main/ledger.md) · [AI step](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/blob/main/ai-step/README.md) · [CHANGELOG](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/blob/main/CHANGELOG.md) · [Pages workflow](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/blob/main/.github/workflows/pages.yml)
- Commits: [draft v0.1](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/commit/49715e9007a850915a6eb72639b0806e9d1d61d3) · [review fixes](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/commit/121d4d7cb95993ec9431487010d8449387318797) · [publish v1.0](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/commit/58d5191202a6df9a864f04634380cadc80c5c9a9) · [v1.1 correction](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/commit/b44a49eb8bf80632cd18d39deb0d70b4251b2a8a)
- Diffs: [draft→review](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/compare/49715e9...121d4d7) · [v1.0→v1.1](https://github.com/PinnacleCryptNG/must-stablecoin-explainer/compare/58d5191...b44a49e)
- Loom: [PLACEHOLDER URL: to be recorded]

**Viewing steps:** open the live site above, or locally: `git log --oneline` → `python3 build.py --preview` (or without the flag for published only) → `python3 -m http.server -d site 8000` → open http://localhost:8000/. Use `git diff <draft> <review>` to see the fact-check revisions and `git diff <v1.0> <v1.1>` to see the correction.

**Checks run (2026-10-24):** build OK (metadata, alt text, draft gating); body prose 983 words; all 3 sources fetched and quoted; `python3 check_triggers.py` → both baselines OK.

**AI contributions:** the first draft, outline and the diagram/table structure were AI-assisted (ai-step/README.md). AI errors caught in review: C3, C5, C6, C11. One error (C10, failed-tx fees) slipped past review and was corrected in v1.1. I own every final decision.

**Limitations:** EVM-focused; issuer terms can change (hence the triggers); the trigger checker uses a date regex and needs a human to read the diff; metrics are hypotheses with no data; the CMS is minimal (no auth or roles; review is enforced by convention plus git).
