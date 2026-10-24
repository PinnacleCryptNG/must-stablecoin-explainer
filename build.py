#!/usr/bin/env python3
"""Tiny stdlib-only static CMS preview. Usage: python3 build.py  -> site/
Reads content/*.md (YAML-ish frontmatter), renders HTML, refuses to build
pages whose status is not 'published' unless --preview is passed (drafts get a banner)."""
import re, sys, html, pathlib, json
ROOT = pathlib.Path(__file__).parent
PREVIEW = "--preview" in sys.argv
# --base=/repo-name  (or BASE_PATH env) prefixes root-relative links for sub-path hosting
import os
BASE = next((a.split("=",1)[1] for a in sys.argv if a.startswith("--base=")), os.environ.get("BASE_PATH", "")).rstrip("/")
REQUIRED = ["title", "slug", "description", "status", "version", "last_verified"]

def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":"); meta[k.strip()] = v.strip().strip('"')
    return meta, m.group(2)

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1">', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*(?!\s)(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s

def slugify(t): return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

def render(md):
    out, lines, i = [], md.splitlines(), 0
    while i < len(lines):
        l = lines[i]
        if not l.strip(): i += 1; continue
        if l.startswith("#"):
            n = len(l) - len(l.lstrip("#")); t = l[n:].strip()
            out.append(f'<h{n} id="{slugify(t)}">{inline(t)}</h{n}>'); i += 1; continue
        if l.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in lines[i].strip("|").split("|")]); i += 1
            h = "".join(f"<th>{inline(c)}</th>" for c in rows[0])
            b = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rows[2:])
            out.append(f"<table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>"); continue
        if l.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].startswith(">"): buf.append(lines[i][1:].strip()); i += 1
            out.append(f"<blockquote>{inline(' '.join(buf))}</blockquote>"); continue
        if re.match(r"^(- |\d+\. )", l):
            tag = "ol" if l[0].isdigit() else "ul"; items = []
            while i < len(lines) and re.match(r"^(- |\d+\. )", lines[i]):
                items.append(re.sub(r"^(- |\d+\. )", "", lines[i])); i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>"); continue
        if l.startswith("<"):  # raw html (figure)
            buf = []
            while i < len(lines) and lines[i].strip(): buf.append(lines[i]); i += 1
            out.append("\n".join(buf)); continue
        buf = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#|\||>|- |\d+\. |<)", lines[i]):
            buf.append(lines[i]); i += 1
        out.append(f"<p>{inline(' '.join(buf))}</p>")
    return "\n".join(out)

CSS = "body{max-width:760px;margin:2rem auto;font:17px/1.6 system-ui;padding:0 1rem;color:#111}table{border-collapse:collapse;font-size:14px}td,th{border:1px solid #ccc;padding:6px;vertical-align:top}blockquote{border-left:4px solid #888;margin:0;padding:.2rem 1rem;background:#f5f5f5}.banner{background:#ffe08a;padding:8px;font-weight:bold}.meta{color:#555;font-size:14px}figure img{max-width:100%}"

def main():
    site = ROOT / "site"; site.mkdir(exist_ok=True); index = []; errors = []
    for f in sorted((ROOT / "content").glob("*.md")):
        meta, body = fm(f.read_text())
        missing = [k for k in REQUIRED if not meta.get(k)]
        if missing: errors.append(f"{f.name}: missing {missing}"); continue
        if meta["status"] != "published" and not PREVIEW:
            print(f"skip {f.name}: status={meta['status']} (use --preview)"); continue
        banner = "" if meta["status"] == "published" else f'<div class="banner">PREVIEW: status = {meta["status"]}, not for publication</div>'
        page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(meta['title'])}</title><meta name="description" content="{html.escape(meta['description'])}">
<link rel="canonical" href="/{meta['slug']}/"><style>{CSS}</style></head><body>{banner}
<p class="meta">v{meta['version']} · status: {meta['status']} · last verified {meta['last_verified']} · AI-assisted: {meta.get('ai_assisted','')}</p>
{render(body)}<hr><p class="meta"><a href="/">All articles</a> · <a href="/changelog.html">Changelog</a></p></body></html>"""
        d = site / meta["slug"]; d.mkdir(exist_ok=True); (d / "index.html").write_text(page)
        imgs = re.findall(r"<img [^>]*>", page); noalt = [x for x in imgs if 'alt=""' in x or "alt=" not in x]
        if noalt: errors.append(f"{f.name}: images without alt text: {noalt}")
        index.append(meta); print(f"built /{meta['slug']}/ ({meta['status']} v{meta['version']})")
    links = "".join(f'<li><a href="/{m["slug"]}/">{html.escape(m["title"])}</a>: {html.escape(m["description"])}</li>' for m in index)
    (site / "index.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Explainers</title><style>{CSS}</style></head><body><h1>Explainers</h1><ul>{links}</ul></body></html>')
    cl = (ROOT / "CHANGELOG.md").read_text() if (ROOT / "CHANGELOG.md").exists() else ""
    (site / "changelog.html").write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Changelog</title><style>{CSS}</style></head><body>{render(cl)}</body></html>')
    if BASE:
        for f in site.rglob("*.html"):
            f.write_text(re.sub(r'(href|src)="/(?!/)', lambda m: f'{m.group(1)}="{BASE}/', f.read_text()))
    if errors: print("\n".join(errors)); sys.exit(1)
    print("OK")
main()
