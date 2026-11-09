# The Japan Breach Registry 2026

**The Autumn Wave of Personal-Data Breaches at Japanese Companies and Organisations — What a Ledger of Primary Notices Objectively Shows**

"Fourteen years produced three breaches of ten million records. The autumn of 2026 produced three in a month."

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Language](https://img.shields.io/badge/Language-Japanese%20%7C%20English-blue)](docs/)
[![Rows](https://img.shields.io/badge/Rows-584-informational)](data/registry.csv)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--11--10-brightgreen)](https://github.com/Leading-AI-IO/the-japan-breach-registry-2026)

<p align="left">
  <img src="./assets/ogp_design.png" width="80%">
</p>

*他の言語で読む: [日本語](README.md)*

---

> **Definition**
>
> **This registry**, by Satoshi Yamauchi (山内怜史), records personal-data breaches disclosed
> by Japanese companies and organisations on or after 1 September 2026 — **only those whose
> primary notice the author opened and read** — keeping each notice's own unit and wording.
> It never converts records into persons, never upgrades "possible" to "confirmed," and
> writes "not disclosed" where the notice is silent on the vector. Alongside the ledger, it
> sorts every claim that "attackers used AI" into four tiers — **evidence, trace,
> possibility, no mention** — with the speaker, date and original-language wording, and tests
> **eight candidate explanations** for why the autumn of 2026 concentrated in Japan on
> identical criteria. As of the first edition (31 rows), no Japanese case reaches the
> "evidence" tier and none of the eight explanations is supported for Japan. The book does not
> claim that AI caused the wave, that Claude Mythos was used, that Glasswing-disclosed
> vulnerabilities were exploited, or that the Japanese and Korean attackers are the same —
> because no primary source says so.
>
> (Corrected 10 November 2026)  
> From the fifth edition, the admission criterion is that the organisation's own primary notice was reached and its text confirms the case is in scope (a breach, or possible breach, of personal data through external unauthorised access). AI agents retrieve and check the notices, recording verbatim the sentences used as evidence; the author spot-checks notices and decides rows on the boundary of the criteria. The 300 rows up to the fourth edition are rows whose notice the author opened and read.
>
> Central question: **in a world where AI has collapsed the cost of finding vulnerabilities,
> does the defender's head start hold?** The book does not answer. It keeps the ledger that
> would.
>
> **Governance**: the author is the sole writer. Admission has one criterion — the author
> opened and read the primary notice — applied without discretion: anything meeting it is
> admitted, anything not meeting it is excluded however large. Readers verify, report errors,
> and point to primary sources.
>
> (Corrected 10 November 2026)  
> From the fifth edition, the admission criterion is that the organisation's own primary notice was reached and its text confirms the case is in scope (a breach, or possible breach, of personal data through external unauthorised access). AI agents retrieve and check the notices, recording verbatim the sentences used as evidence; the author spot-checks notices and decides rows on the boundary of the criteria. The 300 rows up to the fourth edition are rows whose notice the author opened and read.
>
> *Author & full catalog: [github.com/Leading-AI-IO](https://github.com/Leading-AI-IO)*

---

## 📖 Overview

On 7 October 2026, two documents appeared on the same day.

One was Tokyo Shoko Research's "Listed-company personal-data breaches on a record pace." Breaches of one million records or more: ten in 2026 (six in all of 2025). Breaches of ten million or more: three in "the fourteen years to 2025," and three in 2026 alone.

The other was a CrowdStrike Intelligence report. In open directories on a server controlled by the actor who attacked South Korean financial institutions, CrowdStrike found "Claude Code session histories" and the configuration files of a penetration-testing tool called ARTEX. Evidence that the attacker used AI came from the attacker's own machine.

The two documents describe different events in different countries. From the next day, Japanese media began to tell them as one story: "AI-abusing cyberattacks surge; mass personal-data leaks follow."

**This book measures the distance between the two documents.**

### The ledger

Thirty-one breaches disclosed by Japanese companies and organisations since 1 September 2026, each one admitted only because the author opened and read the organisation's own primary notice, each one recorded in the notice's own unit and wording. Sixteen further cases known only through the press — including Bookoff, Murauchi.com and View Card, which would rank near the top by size — are held outside the ledger as "pending verification."

**Eight rows exceed one million in the notice's own unit. Fourteen notices state the vector; seventeen do not. Zero notices mention AI on the attacker's side.**

(Added 16 October 2026)  
Five pending cases (Bookoff, Daiwa Securities, Sagawa Express, Uzabase, White Essence) were admitted after the author read their primary notices. The ledger now has 36 rows and 11 pending. **Ten rows exceed one million; sixteen notices state the vector, twenty do not; zero notices mention attacker-side AI.** Follow-ups to seven existing rows (GMO Research & AI's confirmed count, IDC Frontier's judgement of no data exfiltration, and others) are recorded as dated additions or corrections in the notes column, without changing row values.

(Added 26 October 2026)  
Six pending cases (Shueisha, JAEA, Study Sapuri, Nikkei, Viewcard, JR Kyushu) and 29 cases disclosed on or after 16 October (SourceNext 22,519,960; Capcom 11,774,247; Yumirlink approx. 9 million cumulative; Trustbank 4,454,097; Lindt 3,147,469; and ST approx. 2.5 million; Nikkei approx. 1.83 million; the Digital Agency, MLIT, Osaka University, Tokyo Metropolitan Government and others) were admitted. The ledger now has 71 rows and 25 pending. **Twenty-one rows exceed one million and five exceed ten million; thirty-six notices state the vector, thirty-five do not; zero notices mention attacker-side AI.** Contractor chains grew from two to seven; all five new ones start at a mail-delivery or web-building SaaS (Studio, Yumirlink, blastmail, NEC, FutureShop). Follow-ups to fourteen existing rows (Times Mobility's final figures and first disclosure of the vector, Lawson's corrected data items, skyticket's card-data correction, Sagawa Express's 5th notice — unread, press: up to approx. 53.23 million) are recorded in the notes column.

(Added 3 November 2026)  
Fourteen pending cases and 215 cases disclosed 9 October – 2 November were admitted. The ledger now has 300 rows and 67 pending. Large new rows include Ryohin Keikaku (MUJI) up to approx. 27.26 million, Nojima approx. 7 million, Prestige International up to approx. 5.5 million, Club Tourism approx. 4.32 million, Hana Cupid 4,238,242, Recruit (Carsensor.net) up to 3,709,551, istyle approx. 3 million persons, Matsuya Foods 2,377,127 and So-net 2,141,986. **Thirty-eight rows exceed one million and six exceed ten million; 226 notices state the vector, 74 do not; 163 of the 229 new rows (71%) are contractor rows.** Contractor chains grew from seven to more than twenty (blastmail 29 rows, Studio 26, Commune 18, Yumirlink 18, Arara 11, NTT DATA's bond-perk service, Amadeus with seven airlines, and others). Follow-ups to nineteen existing rows are in the notes column (Yumirlink 51,628,280 cumulative across 49 systems; skyticket 32,341 bank-account records leaked; IDC Frontier's vector disclosed).

(Added 8 November 2026)  
Fourteen pending cases, 184 cases disclosed 3–7 November and 9 cases disclosed 8 October – 2 November that the fourth edition had missed were admitted. The ledger now has 507 rows and 91 pending. Large new rows include GMO Makeshop approx. 12.6 million; BK Japan (Burger King app) approx. 11.18 million; MOS Food Services 7,517,087; Plenus up to approx. 7 million; WILLs (NetMile) up to approx. 5.49 million persons; TKC up to 2,230,812; SignalTalk 1,855,578 members; Workman up to approx. 1.45 million. **Forty-nine rows exceed one million and eight exceed ten million; 418 notices state the vector, 89 do not. 177 of the 207 new rows (86%) are contractor rows, and 137 descend from a single intrusion at Arara's mail-delivery services ("Arara Message", "repica").** Arara's own 3rd notice (6 November) put the de-duplicated email addresses at "81,329,467 (approx. 81 million)" and the affected clients at "up to approx. 380 companies". Eighty-three rows were disclosed on 4 November alone, the ledger's largest single day. New chains: the SMBC Consumer Finance guarantee system (12 partner banks), Prestige International (JA Kyosai, Nissan Financial Services, KDDI and others), CBcloud "PickGo" (Seven-Eleven Japan, Demae-can), Securitize Japan, Arcadia "SpeeCAN RAIDEN". Follow-ups to nine existing rows (Rohto's confirmed 2,797,545 and vector, Paydon's up to 257,639, Ryohin Keikaku's 2nd notice and others) are recorded in the notes. The fifth edition does not revisit the Chapter 5 judgements or Chapter 7.

(Added 10 November 2026)  
Sixty-four cases disclosed 6–9 November, 8 cases disclosed 30 October – 5 November that the fourth edition and the 8 November addition had missed, and 5 pending cases were admitted. The ledger now has 584 rows and 110 pending. Large new rows include Nitori Holdings up to 37.62 million (the largest in the ledger); Sharefull up to approx. 7.5 million personal accounts; SEGA 2,196,044; Shogakukan 1,993,665; Hotelovers 1,578,779; Aioi Nissay Dowa Insurance approx. 444,000; OPEN DOOR (Travelko) 381,926; Sato Food Service 318,513. **Fifty-four rows exceed one million and nine exceed ten million; 482 notices state the vector, 102 do not. 60 of the 77 new rows (78%) came through a contractor.** The contractor rows break down into Arara (30), Prestige International's group company Prestige Core Solution (17; roadside-assistance intake for insurers and card issuers), the SMBC Consumer Finance guarantee system (5 rows, 7 banks) and others; LENDY Servicer is a new chain. Only 13 rows had been found for 6 November on 8 November; 47 were added, making 60. Gaps against the aggregator remain for 3–5 November and were not examined. Of the 284 fifth-edition rows, the author opened and read the primary notices of 9 (301–309); at the author's instruction, AI agents re-fetched and checked the notices of the other 275 (310–584), correcting values in 8 (procedure and results in Chapter 4). Follow-ups for 2 existing rows (275 Ryohin Keikaku, 055 Trust Bank) were added to the notes.

(Corrected 3 November 2026)  
**Chapter 1's "not the count, but the size" is corrected for October.** Trend Micro's own article of 16 October (primary) counts 52 incidents in 1–9 October alone (about 5.8 a day, 2.6 times the January–September average). But 170 of the ledger's 268 October rows are contractor rows: much of the rise is organisations disclosing one intrusion, not the number of intrusions. Collapsing contractor chains, the 300 rows correspond to roughly 144 independent intrusions, about a third with a disclosed vector. Tokyo Shoko Research counted eight 10-million-plus breaches at listed companies by 23 October (three as of 5 October). **H7's "leaning refuted for large rows" is withdrawn**: skyticket, Prestige International and Yumirlink describe abused credentials, though taken during the intrusion, not bought on a market.

### Four tiers of evidence

- **Evidence**: one case, the South Korean financial sector (CrowdStrike). Zero in Japan.
- **Trace**: the Trend Micro remark that Japanese media quoted reads, in Trend Micro's own text, "there is not necessarily evidence that these attacks used AI directly, but it is a fact that the logs alone show 'behaviour unlike before'."
- **Possibility**: statements attributed to Korean regulators (press-based); absent from the regulators' own releases.
- **No mention**: all 31 Japanese notices.

(Added 26 October 2026)  
**A Japanese case entered the evidence tier.** On 15 October JPCERT/CC, reporting on attack-source servers, wrote that it had confirmed attackers "using AI" to scan known vulnerabilities and attack via APIs (「攻撃者がAIを利用して、既知の脆弱性のスキャンやAPI経由での攻撃などを実施していたことを確認しました」). On 19 October NorForge reported exposed Cairn control panels whose targets included a Japanese retailer. The **trace** tier gained JPCERT/CC's 23 October alert update (attack attempts abusing "Cairn, CyberStrikeAI, ARTEX and other AI-driven penetration-testing platforms" confirmed), Secure Sky Technology (14 Oct) and GMO Cybersecurity by Ierae (19 Oct, press-based). **No mention**: all 71 Japanese notices. The evidence appeared on the attacker's side; the victims' notices still say nothing.

(Added 3 November 2026)  
**For the first time, a victim's notice mentions attacker-side AI.** 079 Chitose Group (via Commune) wrote that the attack, "many simultaneous operations in a short time from multiple IP addresses," was 「AI等を用いて自動化された攻撃であったと推定されます」 (presumed to be an automated attack using AI or similar). With only the attack's shape as basis and no stated author of the presumption, the book places it in Tier 3 (possibility). No mention: 299 of 300 notices.

(Added 16 October 2026)  
Including the five added rows, no mention covers all 36 Japanese notices.

(Added 8 November 2026)  
None of the 207 new notices mentions attacker-side AI about its own incident; no mention stands at 506 of 507 rows.

(Added 10 November 2026)  
None of the 77 notices added on 10 November mentions attacker-side AI about its own incident either; no mention stands at 583 of 584 rows.

### Eight explanations

Attacker-side AI, disclosure rules, Japan-specific weaknesses, a single actor, tool diffusion, defender-side AI disclosing vulnerabilities, credential markets, chance. Tested on identical criteria, **none is supported for Japan.** The book writes "undetermined" and leaves it there.

### Two timelines

The defender's (Project Glasswing: announced 7 April → initial update 22 May, "more than ten thousand" → 6 October, "at least 129,000 verified software vulnerabilities") and the attacker's (ARTEX: v0.1.0 on GitHub 26 July, 17 stars → used in Korea in late September). The defender handed an unreleased frontier model to chosen organisations; the attacker used a public tool and inexpensive models. The distance between these timelines is the book's question.

---

## 📊 Data

| File | Role | Contents |
| --- | --- | --- |
| [registry.json](./data/registry.json) | **Canonical** | Admission criteria, column definitions and rules at the top; 31 rows plus 16 pending cases (36 rows and 11 pending as of 2026-10-16; 71 rows and 25 pending as of 2026-10-26; 300 rows and 67 pending as of 2026-11-03; 507 rows and 91 pending as of 2026-11-08; 584 rows and 110 pending as of 2026-11-10) |
| [registry.csv](./data/registry.csv) | Derived | Spreadsheet-friendly (UTF-8 with BOM, 14 columns) |
| [build_registry.py](./scripts/build_registry.py) | Generator | Builds the CSV and the Chapter 4 table from the canonical file |

The table in the text and the two data files are updated in the same commit.

---

## 📄 Documents

| File | Language | Contents |
| --- | --- | --- |
| [the-japan-breach-registry-2026_JP.md](./docs/jp/the-japan-breach-registry-2026_JP.md) | 🇯🇵 Japanese | Full text |
| [the-japan-breach-registry-2026_EN.md](./docs/en/the-japan-breach-registry-2026_EN.md) | 🇺🇸 English | Full text |
| [UPDATE_RUNBOOK.md](./docs/UPDATE_RUNBOOK.md) | 🇯🇵 Japanese | Update procedure, published so readers can verify how the sole writer operates |

---

## 🔄 Changelog

| Date | Version | Contents |
| --- | --- | --- |
| 2026-10-10 | v1.0 | First edition. 31 rows, 16 pending |
| 2026-10-16 | v1.0 (addendum) | Follow-ups appended. Dated additions/corrections in the notes of 7 rows (018, 019, 023, 027 are corrections). Additions in Chapters 2 and 4. Reachability of the 16 pending cases updated. Five pending cases admitted (032 Bookoff, 033 Daiwa Securities, 034 Sagawa Express, 035 Uzabase, 036 White Essence). 36 rows, 11 pending |
| 2026-10-16 | v2.0 | Second edition. 36 rows, 11 pending. The 31 first-edition rows are unchanged; 032–036 added. Further additions are made to the second edition |
| 2026-10-26 | v3.0 | Third edition. 71 rows, 25 pending. The 36 second-edition rows are unchanged; 037–071 added (6 from pending, 29 disclosed on or after 16 Oct). Dated follow-ups in the notes of 14 rows (007, 025, 028 are corrections). Chapter 3: Japanese evidence tier (JPCERT/CC, 15 Oct) and trace tier (JPCERT/CC, 23 Oct and others) added. Chapter 5: H1, H3, H4, H5, H7 verdicts dated and appended. Chapter 6: Cairn and CyberStrikeAI timelines added |
| 2026-11-03 | v4.0 | Fourth edition. 300 rows, 67 pending. The 71 third-edition rows are unchanged; 072–300 added (14 from pending, 215 disclosed 9 Oct – 2 Nov). Dated follow-ups in the notes of 19 rows (023, 028, 047, 053, 070, 071 are corrections). Chapters 1, 2 and 4 appended. Chapter 3: row 079, the first Japanese notice to mention attacker-side AI about its own incident (Tier 3). Corrections: Chapter 1 (count in October), Chapter 2 (counting of vectors by independent intrusion), Chapter 5 H7, Chapter 7 statement 3; additions to the Prologue, H1, H3, H4 and the Epilogue |
| 2026-11-08 | v5.0 | Fifth edition. 507 rows, 91 pending. The 300 fourth-edition rows are unchanged; 301–507 added (14 from pending, 184 disclosed 3–7 Nov, 9 disclosed 8 Oct – 2 Nov missed by the fourth edition). Dated follow-ups in the notes of 9 rows (241, 004, 215 are corrections). Six pending entries already admitted in v4.0 removed from the list; 2 out-of-period and 14 out-of-criteria cases removed; 55 added. Additions to the Prologue and Chapters 1–4. Chapter 5 onward not revisited |
| 2026-11-10 | v5.0 (addendum) | Before publication of the fifth edition, disclosures up to 9 November added. 584 rows, 110 pending. The 207 rows added on 8 November are unchanged; 508–584 added (5 from pending, 64 disclosed 6–9 Nov, 8 disclosed 30 Oct – 5 Nov missed by the fourth edition and the 8 November addition). Follow-ups in the notes of 2 rows (275, 055). 5 pending cases admitted; 24 added. Additions to the Prologue and Chapters 1–4. Chapter 5 onward not revisited |

---

## 📑 Contents

- Prologue: 7 October — two documents on the same day
- Chapter 1: The anomaly of scale — not the count, but the size
- Chapter 2: A map of vectors — not one hole, but many
- Chapter 3: Four tiers of evidence — who said what, and how far
- Chapter 4: The ledger
- Chapter 5: Eight explanations — supported, refuted, undetermined
- Chapter 6: The defender's bet — Glasswing's timeline and ARTEX's
- Chapter 7: Japan as an observation point — what can and cannot be said
- Epilogue: The ledger does not close

---

## 🤝 Contributing

**This book does not accept pull requests.** The author is the sole writer, by design. Keeping units unconverted, statuses unupgraded and vectors unfilled are constraints that drift as writers multiply, and a drifting ledger cannot be used for verification.

Issues are welcome, of two kinds: **corrections** (a figure or unit that does not match the notice, a wrong date, a dead URL, a vector classification that does not match the notice's wording — the author checks against the primary notice and appends a correction without deleting the original row, crediting the reporter), and **primary-source locations** for the eleven pending cases (the author reaches the source, verifies it, and admits the row without discretion).

Issues that include a verdict — "AI caused this," "AI had nothing to do with it" — are accepted minus the verdict. The book records only what primary sources say.

---

## 👤 Author

**Satoshi Yamauchi** (山内 怜史) — AI Strategist & Business Designer at Sun Asterisk Inc.; Founder / AI Strategist at [Leading.AI](https://www.leading-ai.io/). Fifteen-plus years across Business, Technology and Creative: IT consultant and PL/PM on 40 projects at Future Architect, business strategy and new-business development at Recruit, and at Sun Asterisk the author of "Depth & Velocity," a methodology for new-business development in the age of generative AI.

* [📒 Note](https://note.com/satoshi_yamauchi) · [🌐 Leading.AI](https://www.leading-ai.io/)

---

## 📝 License

Published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quote, reproduce and adapt freely with attribution.

Copyright (c) 2026 Leading.AI
