# Distribution adaptation (draft, not posted)

## X thread (draft for @PinnacleCrypt)
1/ Getting paid in USDC or USDT? Most payments just work. Here's what happens when one doesn't, from the issuers' own terms 🧵
2/ There's no chargeback. Circle: "USDC transactions are not reversible." Tether says the same of USDT. A refund is a NEW payment you choose to send.
3/ "Confirmed" ≠ final. On Ethereum, blocks go included → justified → finalized. For big invoices, wait for finality before you deliver.
4/ Stuck "pending"? Usually the fee is too low, or an earlier tx (nonce) is blocking it. Many wallets let you speed up or replace it. That's a wallet feature, not a guarantee.
5/ "Failed" means it was included, reverted, and the gas is gone. Your tokens didn't move.
6/ Wrong network is the classic mistake. Bridged or wrapped copies aren't Circle's or Tether's tokens, and recovery depends on whoever controls the receiving address.
7/ Both issuers can freeze. Receiving funds from a blocked address can get your USDC frozen too, so know your counterparties.
8/ Fix it on the invoice: name the network and token contract, and ask for a 1 USDC test first. Full explainer + source ledger 👇 [LINK]

## LinkedIn (short)
If your business invoices in stablecoins, know this: transfers can't be reversed, "confirmed" isn't "final", and the issuer can freeze funds. I wrote a sourced explainer on wrong-network sends, stuck transactions, refunds and freezes, with a one-table playbook. [LINK]

# Measurement plan (no results yet; all targets are hypotheses)
| Goal | Metric | Source | Hypothesis target (unvalidated) | Review |
|---|---|---|---|---|
| Reach the right readers | Thread impressions; % of profile visits that click the article | X analytics | H1: ≥2% of impressions click through | 7 days after posting |
| Usefulness | Avg engaged time on the article; scroll depth to the playbook table | Site analytics (e.g. Vercel Analytics, to be set up) | H2: ≥50% reach the table | 7 and 30 days |
| Trust | Corrections requested by readers; ledger link clicks | Replies, DMs, link clicks | H3: zero unaddressed correction requests >48h | Ongoing |
| Business value | Saves or bookmarks; inbound questions from merchants | X bookmarks, DMs | H4: qualitative only, collect examples | 30 days |
Rule: report actual numbers only once they exist. If a hypothesis misses, record it and adjust the headline or format, not the data.
