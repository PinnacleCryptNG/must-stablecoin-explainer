# AI-assisted editorial step: claim extraction and fact-check pass

**Tool:** a general-purpose AI assistant (Grok Bot), used on 2026-10-24. The human editor (me) made every final decision.

## Prompt v1 (original)
> You are a fact-checker. Here is my draft explainer on stablecoin payment exceptions. List every factual claim and tell me if it is true.

## AI output v1 (summary of what came back)
- It listed 9 claims and marked all 9 "true". That included "Tether only freezes on law-enforcement order" and "anyone can redeem USDC 1:1".
- It cited no sources for most claims, and attributed nonce replacement to ethereum.org.
- It didn't notice that "unused gas is refunded" was being read as "failed tx is free".

## Verification checklist (applied by me to each claim)
1. Is there a **primary** source (issuer terms, protocol docs)? Blogs and AI memory don't count.
2. Can I paste a **verbatim quote** that supports the claim as written?
3. Does the quote apply to **this user type or account** (e.g. Circle Mint vs. non-customer)?
4. Is it **implemented** behaviour, a **proposal**, or an **opinion**? Is it labelled that way?
5. Is it **time-sensitive** (terms version, dates)? Record "last updated" and the access date.
6. Does the wording overstate certainty ("always", "only", "never")?

## What the checklist caught
| Claim | Check failed | Outcome |
|---|---|---|
| Tether freezes only on legal order | 2 | Revised (ledger C5) |
| Anyone redeems 1:1 | 3, 6 | Revised (C6) |
| ethereum.org documents nonce replacement | 1, 2 | Qualified as wallet behaviour (C3) |
| Wrong-network loss per Circle | 3 | Qualified (C4) |
| Circle helps recover funds | 1 | Removed (C11) |
| Failed tx cheap because gas refunded | 6 (slipped through) | Corrected after publication (C10). This is a lesson for prompt v2 |

## Prompt v2 (improved instructions)
> You are assisting a fact-check. Do NOT judge truth from memory.
> 1. Extract each atomic factual claim from the draft as a numbered list.
> 2. For each, name the type of primary source that could prove it (issuer terms / protocol docs) and the section to look in.
> 3. Flag absolute words (always, only, never, anyone), user-type scope (customer vs. holder), and anything about fees or refunds.
> 4. Label each claim implemented / proposal / opinion.
> 5. Output a table: claim | source to check | risk flags | label. Leave "verdict" blank for the human editor.
> I will paste source excerpts; quote only from text I provide.

**Result of v2 on the same draft:** it flagged C5, C6, C3, C4 and also C10 (the fee/refund flag). It now gives the editor a checklist to work through, not verdicts.
