# Update triggers for /stablecoin-payment-exceptions/
Re-verify the affected claims and bump the version when any of these happen:
1. **Issuer terms change**: the "Last Updated" date on S1 (currently October 15, 2026) or S2 (currently February 26, 2026) changes. Check with `python3 check_triggers.py` (weekly).
2. ethereum.org changes its transaction lifecycle or finality text (S3).
3. An issuer adds or drops support for a chain (e.g. Tether's ended USDT redemptions on Omni/BCH SLP/Kusama/EOS/Algorand, effective Sept 1, 2025, per S2 §4.1).
4. A reader correction is confirmed.
Process: open the article → status: review → update ledger → approve → publish with a CHANGELOG entry.
