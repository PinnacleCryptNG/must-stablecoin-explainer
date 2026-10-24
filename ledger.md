# Claim-to-source ledger

Accessed **2026-10-24** (Africa/Lagos) via direct fetch of each page. Quotes are verbatim. Status: ✅ supported · ✏️ revised · ⚠️ qualified · ❌ removed.

## Sources (all primary)
| ID | Source | URL | Version seen |
|---|---|---|---|
| S1 | Circle, USDC Terms | https://www.circle.com/legal/usdc-terms | "Last Updated: October 15, 2026" |
| S2 | Tether, Token Terms of Sale and Service | https://tether.to/en/legal/ | "Last updated: February 26, 2026" |
| S3 | ethereum.org, Transactions (developer docs) | https://ethereum.org/en/developers/docs/transactions/ | live page (no version date shown) |

## Claims
| # | Claim (final text) | Source | Quoted support | Status |
|---|---|---|---|---|
| C1 | USDC transfers can't be reversed by Circle | S1 §13 | "USDC transactions are not reversible." / "Circle does not have the ability to reverse or recall any transaction once initiated." | ✅ |
| C2 | USDT transfers are not reversible | S2 §5 | "Tether Token transactions are not reversible." | ✅ |
| C3 | Stuck tx: wallets often let you "speed up/cancel" by re-sending the same nonce with a higher fee (**wallet behaviour, not a guarantee**) | S3 | S3 defines nonce as "a sequentially incrementing counter…" and the fee fields; it does **not** describe replacement | ⚠️ qualified |
| C4 | Sending USDC to an address that doesn't support it may mean loss (**stated in the Circle Mint section**) | S1 §8 | "If you attempt to send USDC from your Circle Mint account to a wallet or address that does not support USDC, your USDC will be lost forever." | ⚠️ qualified |
| C5 | Tether may freeze/blacklist at its discretion for Prohibited Use, or when directed by a government | S2 §6, §8 | "freezing or confiscation of any… Tether Tokens… blacklisting any Digital Tokens Address" / "when Tether is directed to do so by any Government" | ✏️ revised |
| C6 | Redemption at $1 is limited to Circle Mint / verified Tether customers; no $1 guarantee on third-party platforms | S1 §2, §13; S2 §4.1 | "Circle does not guarantee that the value of one (1) USDC will always equal 1 USD ($1) on other platforms." / "you must be a verified customer of Tether" | ✏️ revised |
| C7 | Finalized blocks could only be changed by an attack costing billions | S3 | "Once a block is 'finalized' it could only ever be changed by a network level attack that would cost many billions of dollars." | ✅ |
| C8 | Bridged/wrapped tokens are not the issuer's tokens | S1 §8; S2 §4.5 | "These Digital Tokens are not Tether Tokens… they cannot be redeemed with Tether" | ✅ |
| C9 | Circle can block on-chain transfers and freeze on legal order | S1 §13 | "block the transfer of USDC to and from an address on chain" / "freeze USDC… in the event it receives a legal order" | ✅ |
| C10 | A failed tx still costs gas | S3 (gas section) + general EVM behaviour | S3 says "Any gas not used in a transaction is refunded", which does **not** mean a reverted tx is free | ✏️ corrected post-publication (v1.1) |
| C11 | ~~Circle will help recover funds sent on the wrong chain~~ | S1 | no support; S1 disclaims responsibility | ❌ removed |

## Before → after (revisions caught during checking)
1. **C5.** *Before (AI draft):* "Tether only freezes tokens when ordered by law enforcement." *After:* "Tether may freeze tokens and blacklist addresses for a Prohibited Use, in its sole and absolute discretion, or when directed by a government." *Why:* S2 §8 grants discretionary freezes, not only on legal order.
2. **C6.** *Before:* "Anyone can always redeem 1 USDC for $1." *After:* redemption is only for Circle Mint accounts and verified Tether customers, with no $1 price guarantee on other platforms. *Why:* S1 §2 ("User Type B… may not redeem"), S1 §13.
3. **C3.** *Before:* "ethereum.org says you can replace a stuck transaction using the same nonce." *After:* labelled as wallet behaviour. *Why:* S3 doesn't say this. I didn't cite a non-primary source for it.
4. **C4.** *Before:* "Circle says wrong-network USDC is lost forever." *After:* the clause is attributed to the Circle Mint section.
5. **C11.** Removed: unsupported.
6. **C10.** Published v1.0 implied failed transactions are cheap because "unused gas is refunded". Corrected in v1.1 (see CHANGELOG).
