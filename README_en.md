# The Japan Breach Registry 2026

**The Autumn Wave of Personal-Data Breaches at Japanese Companies and Organisations — What a Ledger of Primary Notices Objectively Shows**

"Fourteen years produced three breaches of ten million records. The autumn of 2026 produced three in a month."

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Language](https://img.shields.io/badge/Language-Japanese%20%7C%20English-blue)](docs/)
[![Rows](https://img.shields.io/badge/Rows-31-informational)](data/registry.csv)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--10--10-brightgreen)](https://github.com/Leading-AI-IO/the-japan-breach-registry-2026)

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
> Central question: **in a world where AI has collapsed the cost of finding vulnerabilities,
> does the defender's head start hold?** The book does not answer. It keeps the ledger that
> would.
>
> **Governance**: the author is the sole writer. Admission has one criterion — the author
> opened and read the primary notice — applied without discretion: anything meeting it is
> admitted, anything not meeting it is excluded however large. Readers verify, report errors,
> and point to primary sources.
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

### Four tiers of evidence

- **Evidence**: one case, the South Korean financial sector (CrowdStrike). Zero in Japan.
- **Trace**: the Trend Micro remark that Japanese media quoted reads, in Trend Micro's own text, "there is not necessarily evidence that these attacks used AI directly, but it is a fact that the logs alone show 'behaviour unlike before'."
- **Possibility**: statements attributed to Korean regulators (press-based); absent from the regulators' own releases.
- **No mention**: all 31 Japanese notices.

### Eight explanations

Attacker-side AI, disclosure rules, Japan-specific weaknesses, a single actor, tool diffusion, defender-side AI disclosing vulnerabilities, credential markets, chance. Tested on identical criteria, **none is supported for Japan.** The book writes "undetermined" and leaves it there.

### Two timelines

The defender's (Project Glasswing: announced 7 April → initial update 22 May, "more than ten thousand" → 6 October, "at least 129,000 verified software vulnerabilities") and the attacker's (ARTEX: v0.1.0 on GitHub 26 July, 17 stars → used in Korea in late September). The defender handed an unreleased frontier model to chosen organisations; the attacker used a public tool and inexpensive models. The distance between these timelines is the book's question.

---

## 📊 Data

| File | Role | Contents |
| --- | --- | --- |
| [registry.json](./data/registry.json) | **Canonical** | Admission criteria, column definitions and rules at the top; 31 rows plus 16 pending cases |
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

Issues are welcome, of two kinds: **corrections** (a figure or unit that does not match the notice, a wrong date, a dead URL, a vector classification that does not match the notice's wording — the author checks against the primary notice and appends a correction without deleting the original row, crediting the reporter), and **primary-source locations** for the sixteen pending cases (the author reaches the source, verifies it, and admits the row without discretion).

Issues that include a verdict — "AI caused this," "AI had nothing to do with it" — are accepted minus the verdict. The book records only what primary sources say.

---

## 👤 Author

**Satoshi Yamauchi** (山内 怜史) — AI Strategist & Business Designer at Sun Asterisk Inc.; Founder / AI Strategist at [Leading.AI](https://www.leading-ai.io/). Fifteen-plus years across Business, Technology and Creative: IT consultant and PL/PM on 40 projects at Future Architect, business strategy and new-business development at Recruit, and at Sun Asterisk the author of "Depth & Velocity," a methodology for new-business development in the age of generative AI.

* [📒 Note](https://note.com/satoshi_yamauchi) · [🌐 Leading.AI](https://www.leading-ai.io/)

---

## 📝 License

Published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Quote, reproduce and adapt freely with attribution.

Copyright (c) 2026 Leading.AI
