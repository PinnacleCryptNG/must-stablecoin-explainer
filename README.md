# MUST task: Trustworthy crypto explainer + editorial workflow
Stdlib-only static CMS. Build: `python3 build.py` (published only) or `python3 build.py --preview` (includes drafts, with a banner). Then serve with `python3 -m http.server -d site 8000` and open http://localhost:8000/stablecoin-payment-exceptions/
Lifecycle: `status:` in frontmatter goes draft → review → approved → published, with one git commit per stage (`git log --oneline`). The build refuses non-published pages unless you pass --preview, and fails if required metadata or image alt text is missing.
Deploy later (not done): Vercel with build command `python3 build.py` and output dir `site`, or GitHub Pages from `site/`.
