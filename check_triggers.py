#!/usr/bin/env python3
"""Compare issuers' 'Last updated' strings against the recorded baseline. Read-only GET requests."""
import re, urllib.request
BASE = {"https://www.circle.com/legal/usdc-terms": "October 15, 2026", "https://tether.to/en/legal/": "February 26, 2026"}
for url, known in BASE.items():
    try:
        t = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=20).read().decode("utf8", "ignore")
        t = re.sub(r"<[^>]+>", " ", t)
        m = re.search(r"Last [Uu]pdated:?\s*([A-Z][a-z]+ \d{1,2}, \d{4})", t)
        seen = m.group(1) if m else "NOT FOUND"
        print(("OK      " if seen == known else "TRIGGER ") + f"{url} baseline={known} seen={seen}")
    except Exception as e:
        print(f"ERROR   {url}: {e}")
