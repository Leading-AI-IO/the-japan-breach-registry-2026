# The Japan Breach Registry 2026 — The Autumn Wave of Personal-Data Breaches at Japanese Companies and Organisations, Read from a Ledger of Primary Notices

<p align="left">
  <img src="../../assets/ogp_design.png" alt="The Japan Breach Registry 2026" width="80%">
</p>

**Author**: Satoshi Yamauchi (山内怜史), AI Strategist
**First edition**: 10 October 2026
**License**: CC BY 4.0
**Repository**: https://github.com/Leading-AI-IO/the-japan-breach-registry-2026

*This English edition stands beside the Japanese edition rather than translating it. Verbatim quotations from Japanese and Korean sources are given in the original language with an English gloss; quotations from English sources are given as published.*

---

# Prologue: 7 October — two documents on the same day

On 7 October 2026, two documents were published.

The first was Tokyo Shoko Research's "Listed-company personal-data breaches on a record pace." Counting breach and loss incidents disclosed by listed companies and their subsidiaries, it wrote:

> 流出100万件以上は、2026年はすでに10件確認された（10月5日時点）。これは2025年（1-12件）の6回を大幅に上回っている

*(Breaches of one million records or more: ten already confirmed in 2026 as of 5 October, far above the six of 2025.)*

> 1,000万件以上の漏えい事件は2025年までの14年間で3回発生している

*(Breaches of ten million or more occurred three times in the fourteen years to 2025.)*

> すでに10月5日までに1,000万人分以上の漏えい事故が3回発生している

*(By 5 October, three breaches of ten million or more had already occurred.)*

A scale of breach that happened three times in fourteen years happened three times in 2026.

The second was CrowdStrike Intelligence's "Unknown Threat Actor Uses AI-Driven ARTEX to Target South Korean Finance." Of an attack on South Korean financial institutions, it wrote:

> Analysis of threat actor-controlled open directories uncovered Claude Code session histories

Directories on a server the attacker controlled had been left open. In them sat the session histories of an AI coding tool and the configuration files of a penetration-testing tool. Evidence that the attacker used AI came from the attacker's own machine.

The two documents describe different events in different countries. They appeared on the same day. From the next day, Japanese media began to tell them as one story: "AI-abusing cyberattacks surge; mass personal-data leaks follow."

This book measures the distance between the two documents.

## Why this ledger exists

From September into October 2026, disclosures of personal-data breaches in Japan came one after another. 10.79 million records from a yakiniku chain's app; 14.64 million from a travel-booking site; 6.6 million accounts from a car-sharing service; 23.62 million from an image-capture service. Convenience stores, karaoke, railways, a securities firm, a life insurer, a discount retailer, a central-government agency.

JPCERT/CC wrote in its alert of 8 October:

> 各被害公表や報道のとおり、直近2026年9月前後で国内組織における不正アクセスによる個人情報等の漏えい被害が相次いでいます。

*(As the disclosures and reports show, breaches of personal data through unauthorised access at domestic organisations have followed one another around September 2026.)*

And in the same document:

> 複数の製品やサービスで被害が発生している中、技術的な情報の共有が不足しており、把握している情報は限定的かつ断片的であるものの

*(With damage occurring across several products and services, technical information is under-shared, and what we know is limited and fragmentary.)*

That breaches are following one another is known. What is happening is not.

Into that gap flow words. "AI abuse is the cause." "The influence of Anthropic's unreleased model." "A single attacker." None is verified. All spread unverified.

This book does not fill the gap. It records the gap's shape.

## What this book hands over

Three things.

**First, a ledger.** Of the personal-data breaches disclosed by Japanese companies and organisations since 1 September 2026, only those whose primary notice the author opened and read, each recorded in the notice's own unit and wording. The first edition has 31 rows. Cases known only through the press are held outside the ledger as "pending verification."

(Added 16 October 2026)  
On 16 October 2026 five rows were added from the pending list; the ledger now has 36 rows. None of the five notices mentions attacker-side AI.

(Added 26 October 2026)  
On 26 October 2026, six rows were added from the pending list and 29 from cases disclosed on or after 16 October; the ledger now has 71 rows and 25 cases pending. None of the 35 added notices mentions attacker-side AI. Between 16 and 26 October, an aggregator's daily list (jouhourouei.clipmaster.jp) ran to dozens of organisations a day; the 71 rows are the part of that whose primary notices the author could open and read.

**Second, tiers of evidence.** Every claim that "the attacker used AI" is sorted into four tiers — evidence, trace, possibility, no mention — with who said what, when, in the original language. As of the first edition, no Japanese case reaches the evidence tier.

**Third, a test of explanations.** Why did large breaches concentrate in Japan in the autumn of 2026? Eight candidate explanations are tested on identical criteria and sorted into supported, refuted and undetermined. As of the first edition, most are undetermined. The book writes "undetermined."

## What this book does not write

Four things, because no primary source contains them.

1. That AI caused the increase in breaches.
2. That Anthropic's unreleased model "Claude Mythos" was used in an attack.
3. That vulnerabilities found and disclosed by AI were exploited before they were patched.
4. That the Japanese and Korean incidents share an attacker.

In Chapter 5 each of these is recorded not as refuted but as "undetermined" or "no supporting primary source." Not writing something and refuting it are different acts.

## The question

The book asks one question.

**In a world where AI has collapsed the cost of finding vulnerabilities, does the defender's head start hold?**

On 7 April 2026 Anthropic announced Project Glasswing: an unreleased frontier model, provided only to organisations that defend critical software, so that vulnerabilities could be found and fixed first. The announcement spoke of "giving defenders a durable advantage in the coming AI-driven era of cybersecurity."

Six months later, in South Korea, an attacker using an open-source tool published two months earlier and inexpensive models exfiltrated data from financial institutions. In the same weeks, Japan saw breaches of a scale that had occurred three times in fourteen years occur three times in a month.

Does the defender's head start hold? This book does not answer. It builds, and keeps updating, the ledger that would.

## How this book is run

One person writes the ledger. Opening a row, correcting it, appending to it — the author alone. Readers verify, report errors, and point to primary sources.

There is one admission criterion: the author opened and read the organisation's own primary notice. Anything that meets it is admitted without exception; anything that does not is excluded however large. The author has no discretion over admission.

(Corrected 10 November 2026)  
From the fifth edition, the admission criterion is that the organisation's own primary notice was reached and its text confirms the case is in scope (a breach, or possible breach, of personal data through external unauthorised access). AI agents retrieve and check the notices, recording verbatim the sentences used as evidence; the author spot-checks notices and decides rows on the boundary of the criteria. The 300 rows up to the fourth edition are rows whose notice the author opened and read.

The ledger is append-only. Rows are neither deleted nor rewritten; corrections are appended and marked as corrections. The table in the text and the machine-readable files (CSV, JSON) are generated from one source and updated in the same commit. The procedure is published in `docs/UPDATE_RUNBOOK.md`.

### References

- Tokyo Shoko Research, 上場企業「個人情報漏えい」、過去最悪ペース, 7 October 2026 https://www.tsr-net.co.jp/data/detail/1203305_1527.html
- CrowdStrike Intelligence, "Unknown Threat Actor Uses AI-Driven ARTEX to Target South Korean Finance," 7 October 2026 https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/
- JPCERT/CC, 直近で相次いでいる国内組織における不正アクセスに関する注意喚起, 8 October 2026 https://www.jpcert.or.jp/at/2026/at260030.html
- Anthropic, "Project Glasswing: Securing critical software for the AI era," 7 April 2026 https://www.anthropic.com/glasswing

---

# Chapter 1: The anomaly of scale — not the count, but the size

"Breaches have surged" mixes two claims: that there are more incidents, or that each incident is larger. For the autumn of 2026, what can be said is the second.

## The count: not the peak month

Two tallies of disclosed unauthorised-access incidents in Japan have been reported. Both are press-based; neither primary tally has been retrieved.

Citing Trend Micro, ITmedia reported on 8 October that disclosed incidents at Japanese companies and municipalities reached 600 by the end of September 2026, on pace to exceed 2025's full-year 593.

Citing a Trend Micro–Yomiuri tally, the Yomiuri Shimbun reported at least 503 incidents in 2024, 473 in 2025, and 506 in 2026 through 5 October, with June the busiest month at 76.

The two tallies cut the data differently and cannot be added or compared. But one thing holds in both: **2026 is on pace to exceed the prior year's count, and September is not the peak month.** By count alone, September–October is not a "wave."

(Corrected 3 November 2026)  
The statement that September–October was not a "wave" by count rested on press-based figures as of late September and 5 October; it does not hold for October. Trend Micro's own article of 16 October (primary) counts 607 incidents disclosed by Japanese organisations in January–September 2026 (2.2 a day) and writes 「2026年10月は1週目（10月1～9日分）のみで、52件に上ります」 (52 in the first nine days of October alone) — about 5.8 a day, 2.6 times the January–September average (both figures cover all incident types, counted the same way in the same article; unauthorised access was 331, 54.5%, of January–September). In this ledger, 268 rows were disclosed in October, 217 of them on or after 16 October. Most of the increase, however, comes from disclosures by the clients of a few breached contractors: 170 of the 268 October rows are contractor rows. Trend Micro itself counts such "data supply-chain" cases separately (62, 10.2%, January–September). For October: the number of disclosures rose; much of the rise is the number of organisations disclosing one intrusion, not the number of intrusions. The first-edition text is kept as a statement as of 5 October.

## The size: three in fourteen years, three in a month

What changed is size. Tokyo Shoko Research's 7 October tally, confined to listed companies and their subsidiaries, states:

- Breaches of one million records or more: 10 in 2026 as of 5 October; 6 in all of 2025.
- Breaches of ten million or more: 3 in the fourteen years 2012–2025; 3 in 2026 by 5 October.

Counting the ledger's rows (Chapter 4) that exceed one million in the notice's own unit gives eight:

| ID | Organisation | Scale (notice's unit) | Status |
|---|---|---|---|
| 005 | Helpfeel (Gyazo) | user data approx. 23.62 million records | confirmed |
| 028 | Adventure (skyticket) | approx. 14.64 million records | confirmed |
| 017 | Monogatari Corporation | 10,788,963 records | confirmed |
| 026 | Daiichikosho | approx. 8,724,000 records | possible |
| 007 | Times Mobility | approx. 6.6 million accounts | confirmed |
| 025 | Lawson | 2,155,345 records | confirmed |
| 021 | MrMax | up to 1,735,154 persons | confirmed (count is a maximum) |
| 027 | JR East | approx. 1.67 million + approx. 390,000 (maxima) | cannot be ruled out |

Tokyo Shoko Research's "three" and the ledger's three rows above ten million (005, 028, 017) coincide. The populations differ: TSR counts listed companies and subsidiaries; the ledger counts every organisation whose primary notice could be read, including the Digital Agency and JOGMEC, which are not listed companies.

(Added 16 October 2026)  
Two of the five rows added on 16 October exceed one million in the notice's own unit: 032 Bookoff Group Holdings, 「最大 約 643 万件」 (up to approx. 6.43 million; a count of member numbers, which the notice says is 「対象となる方の実際の人数ではありません」, not the actual number of persons), and 036 White Essence, 「約105万アカウント」 (approx. 1.05 million accounts). Rows above one million in the ledger rose from 8 to 10. Rows above ten million remain 3.

(Added 26 October 2026)  
Eleven of the 35 rows added on 26 October exceed one million in the notice's own unit: 044 SourceNext 「22,519,960件」, 064 Capcom 「11,774,247件（全世界合計）」 (worldwide), 053 Yumirlink 「延べ約900 万件」 (approx. 9 million, cumulative, estimated), 069 Green Monster 「約 619 万件のユーザー情報等」 (approx. 6.19 million user records, including items that are not personal data), 038 Yamato Transport 「約526万件」, 055 Trustbank 「4,454,097件」, 042 Viewcard 「約 403 万件」, 070 Lindt 「3,147,469件」, 067 and ST 「約250万件」, 045 Nikkei 「約183万件」, 043 JR Kyushu 「約 130 万件」. Rows above one million rose from 10 to 21; rows above ten million from 3 to 5. Two of the ten-million rows (044, 064) were disclosed after Tokyo Shoko Research's 5 October cut-off and are not among its "three." Row 034 Sagawa Express's fifth notice (23 October) is reported in the press as 「最大約5323万件」 (up to approx. 53.23 million); the author has not been able to read it, so the row keeps "under investigation."

(Added 3 November 2026)  
Of the 229 rows added on 3 November 2026, 17 exceed one million in the notice's own unit: 275 Ryohin Keikaku (MUJI app) 「最大 約2,726万件（退会されたお客さまの情報を含みます）」 (up to approx. 27.26 million records, including withdrawn members); 289 Nojima approx. 7 million records; 290 Prestige International up to approx. 5.5 million (including duplicates); 280 Club Tourism approx. 4.32 million; 214 Hana Cupid 4,238,242; 117 Recruit (Carsensor.net) up to 3,709,551; 121 FutureShop 3,147,469 (one store — the same member data as row 070, Lindt); 241 Arara approx. 3.01 million email addresses; 292 istyle (@cosme) approx. 3 million persons; 149 Rakuten Group (Rakuten Travel) up to approx. 2.6 million (login users); 271 Matsuya Foods 2,377,127; 178 Sony Network Communications (So-net) 2,141,986; 202 Rise UP 1,548,002 (cumulative); 072 Fines 1,536,322; 111 Hankyu Hanshin Department Stores (H2O ID) approx. 1.26 million; 259 World approx. 1.2 million (cumulative); 133 Kakao Piccoma 1,002,404. Rows above one million rose from 21 to 38; rows above ten million from 5 to 6 (275 added). These figures cannot be summed: units differ, two rows count the same people, and several are cumulative or include duplicates. Two existing rows reported larger figures in follow-ups, recorded as dated corrections without changing the row values: 053 Yumirlink, 2nd notice of 26 Oct, 「51,628,280件（延べ件数）」 across 49 systems (16 still under review); 047 Comic Cmoa, 4th notice of 21 Oct, up to approx. 4.2 million log-file records.

(Added 3 November 2026)  
Tokyo Shoko Research wrote on 23 October that listed companies and their subsidiaries had 「2026年は10月23日までに1,000万件以上の情報漏えい事故が佐川急便を含め、すでに8件（速報値）」 (eight breaches of 10 million+ by 23 October, provisional). The ledger has six rows above ten million; the populations differ, and TSR counts Sagawa Express at up to approx. 53.23 million while row 034 keeps "under investigation" until the author reads Sagawa's own 5th notice.

(Added 8 November 2026)  
Of the 207 rows added on 8 November 2026, 11 exceed one million in the notice's own unit: 484 GMO Makeshop "approx. 12.6 million records", 304 BK Japan (Burger King app) "approx. 11.18 million member records", 348 MOS Food Services "7,517,087 email addresses", 365 Plenus "up to approx. 7 million", 319 WILLs (NetMile) "up to approx. 5.49 million persons", 320 TKC (3rd notice) "up to 2,230,812", 507 SignalTalk "1,855,578 members", 345 Workman "up to approx. 1.45 million", 349 Chobirich "1,348,525", 364 Credit Saison (MUJI Card) "approx. 1.09 million", 355 Axel Entermedia "1,086,098". Rows above one million rose from 38 to 49; rows above ten million from 6 to 8 (304 and 484 added).

Seven of the eleven (484, 348, 365, 345, 349, 355, 320) are email addresses taken in the intrusion at 241 Arara, disclosed by each client for its own share. Arara's 3rd notice (6 November) put the de-duplicated total at "81,329,467 (approx. 81 million)" and the affected clients at "up to approx. 380 companies (under review)". These seven figures are parts of that total and must not be summed. 364 Credit Saison's "approx. 1.09 million" is the MUJI Card portion of 275 Ryohin Keikaku's "up to approx. 27.26 million" — the same people.

Three existing rows received follow-ups larger than the row value: 241 Arara (first notice "approx. 3.01 million" → 3rd notice "81,329,467"), 004 Rohto (no count → 6 November "2,797,545 customers"), 215 Paydon ("possible" → "up to 257,639"). Under the append-only rule the row values stay; the corrections are in the notes. Counting them, rows above ten million would be 9 and above one million 51.

(Added 10 November 2026)  
Of the 77 rows added on 10 November 2026, 5 exceed one million in the notice's own unit: 577 Nitori Holdings "up to 37.62 million records", 578 Sharefull "up to approx. 7.5 million personal accounts" (plus "up to approx. 7,500 companies"), 576 SEGA "2,196,044 email addresses", 553 Shogakukan "1,993,665 records", and 551 Hotelovers "1,578,779 records (as of 5 November 2026)". Rows above one million rose from 49 to 54, and rows above ten million from 8 to 9 (577 added). 577 is the largest row in the ledger in the notice's own unit, above 275 Ryohin Keikaku's "up to approx. 27.26 million". Its status word is "may have leaked"; the notice does not say the leak is confirmed.

(Added 14 November 2026)
Of the 260 rows added on 14 November 2026, 6 exceed one million in the notice's own unit: 599 Iris Plaza "approx. 7.7 million people" (members approx. 5.8 million, non-members approx. 1.9 million), 589 Arcadia "email addresses: approx. 3,136,000" (stated as an estimate), 629 Nagakute "up to 2,230,812" (the whole figure of the contractor TKC), 725 the Japan Chamber of Commerce and Industry "up to approx. 980,000 people (approx. 1.97 million records)", 827 Yeny "1,332,505 (including closed accounts)" and 764 Kawajun "1,214,183". Rows above one million rose from 54 to 60; rows above ten million remain 9. 604 Shiki (contractor-wide "up to 2,230,812", the city's share under investigation) and 789 ENSAPIA Tokyo (Asoview's company-wide 15,821,184) are not counted, because the row's scale is not the organisation's own figure.

Two existing rows received larger figures in follow-ups: 119 istyle (Cuenote FC) from "not stated" to "approx. 2.8 million people" (9 Nov) and 371 JA Kyosairen from "not stated" to "up to approx. 2.85 million people" (12 Nov). 053 Ymir Link's third notice (11 Nov) revised its cumulative count down from 51,628,280 to "47,864,147". Under the append-only rule the row values stay and the changes are added to the notes.

## Units are not mixed

This book does not convert records into persons, because the notices themselves refuse to.

Helpfeel's notice states that of "approx. 23.62 million records," approx. 18.01 million (76%) belong to anonymous users with no registered e-mail, and that "the number of persons actually affected is still under investigation."

Lawson's notice heads its figure "対象人数" (number of persons) while the unit it uses is "件" (records).

Daiichikosho's notice sums per-brand counts and subtracts approx. 515,000 duplicates to reach approx. 8,724,000.

Scala Communications' notice calls its "up to 713,126" a gross count of enquiries, with the same person counted once per enquiry.

Summing these into "tens of millions of people" has no basis in any notice. The ledger records scale in the notice's own unit.

## What the public bodies certified

Two public bodies issued documents in the second week of October.

The Personal Information Protection Commission published, on 7 October, an alert titled 大規模な漏えい等事案を踏まえた対応について（注意喚起） (Response in light of large-scale breach incidents).

JPCERT/CC published, on 8 October, the alert quoted in the Prologue. On the targets:

> 一般利用者向けのアプリのほか、BI（ビジネスインテリジェンス）ツールや従業員向け管理システムなど

*(Beyond consumer apps: BI tools, employee-facing management systems, and the like.)*

Neither document refers to AI on the attacker's side. The word "AI" does not occur in the JPCERT/CC alert.

### References

- Tokyo Shoko Research, as above (Prologue)
- ITmedia, NewsPicks、個人情報漏えいの可能性 業務ツールへの不正アクセスで, 8 October 2026 https://www.itmedia.co.jp/business/articles/2610/08/news105_2.html (press-based, citing Trend Micro)
- Yomiuri Shimbun via Yahoo! News, Trend Micro–Yomiuri annual and monthly counts (press-based; primary tally not retrieved)
- Personal Information Protection Commission, 7 October 2026 https://www.ppc.go.jp/news/careful_information/
- JPCERT/CC, as above (Prologue)

---

# Chapter 2: A map of vectors — not one hole, but many

"Hit by the same technique" is not supported by the ledger. The vectors the notices state are scattered.

## Rows whose notices state the vector

Of 31 rows, 14 notices state a vector. The other 17 say only "unauthorised access by a third party."

(Added 16 October 2026)  
With the five added rows, 16 of 36 rows state a vector and 20 do not. The two additions: 036 White Essence (vulnerability), 「弊社が運営する予約サイトのプログラムに存在した脆弱性を悪用され、これを起点として、弊社の基幹システムに不正アクセスされた」 (a vulnerability in the booking site's program was exploited and used as a foothold into the core system); 033 Daiwa Securities (contractor), 「SC 社のサーバーに対する不正アクセスにより、当社のお客様情報への不正アクセスおよび不正取得の形跡が確認された」 (unauthorised access to the contractor's server left traces of access to and acquisition of Daiwa's customer data). The three rows with no vector are 032 Bookoff, 034 Sagawa Express and 035 Uzabase. Row 032 writes 「脆弱性を是正し」 (remediated the vulnerability) as a response measure, not as the intrusion route, so it is classified as vector not disclosed.

(Added 26 October 2026)  
With the 35 rows added on 26 October, 36 of 71 rows state a vector and 35 do not: vulnerability 12, VPN vulnerability 1, contractor 16, unauthorised login 4, misconfiguration 2, multiple 1, not disclosed 35. The growth is in contractor rows (6 → 16) and unauthorised-login rows (0 → 4). The ten new contractor rows: 051 Studio → 052 Digital Agency; 053 Yumirlink → 065 Nomura Securities; 059 Rakus (blastmail) → 060 Tokyo Metropolitan Government, 061 Cells; 057 NEC → 058 Osaka University; 048 Iwai Cosmo Securities (via Tradeworks); 070 Lindt (via FutureShop); 042 Viewcard and 043 JR Kyushu (via IDC Frontier). The four unauthorised-login rows: 041 Nikkei 「「グーグルワークスペース」のアカウントが7月下旬以降、外部から不正にログインされ」, 045 Nikkei 「クラウドサービスにアクセスするための認証情報が何らかの手段で窃取されました」, 062 Digital Arts (credentials unlawfully obtained and used to enter the operating environment), and 057 NEC (stolen credentials of a legitimate account, classified under contractor). New vulnerability rows cite APIs and public apps — 040 Study Sapuri, 044 SourceNext 「会員情報取得APIを不正に利用し」, 051 Studio, 053 Yumirlink, 068 Treasure Factory, 069 Green Monster 「本アプリの API の機能によるもの」 — which corresponds to the APK-analysis-to-API method JPCERT/CC described on 15 October and NICT's "A2B attack"; whether any given row was breached that way, the notices do not say.

(Corrected 26 October 2026)  
007 Times Mobility disclosed its vector for the first time in its fifth notice (23 October): 「本事案は Web システムに存在した脆弱性が悪用されたことにより発生したものと判断しております」. The row keeps its first-notice classification (not disclosed) with a dated correction in the notes; counting the correction, 37 rows state a vector and 13 are vulnerabilities.

**Vulnerability (5)**

- 005 Helpfeel: 「画像アップロードサーバーに存在した脆弱性を悪用し」「任意のコマンドを実行する不正アクセス」 *(exploited a vulnerability in the image-upload server; executed arbitrary commands)*
- 006 Smaregi: 「お客さま管理画面のログイン機能に存在した脆弱性を悪用し」 *(exploited a vulnerability in the login function of the customer admin console)*
- 018 GMO Research & AI: 「当社サイトで使用していたソフトウェアの脆弱性を悪用して侵入」 *(intruded by exploiting a vulnerability in software used on the site)*
- 021 MrMax: 「本サービスを構成するソフトウェアの機能を不正に利用してサーバーに侵入し」 *(intruded by abusing a function of software that makes up the service)*
- 029 coconala: vulnerability fixed by 21:27 on 8 October 2026 (nature not disclosed)

**VPN vulnerability (1)**

- 002 Digital Agency: 「ネットワーク接続機器（VPN）の脆弱性を利用してシステムに侵入し」 *(intruded via a vulnerability in a network device (VPN))*, using a maintenance account

**Contractor / third-party service (5)**

- 024 WingArc1st, 030 Sansan, 031 LIXIL: all via Commune Inc.'s cloud service. Sansan: 「本件はコミューン社のシステムに対する攻撃により発生したものです。」 *(This incident arose from an attack on Commune's system.)* LIXIL: 「複数の不備が第三者に悪用されたことにより発生」 *(arose from multiple deficiencies exploited by a third party)*
- 026 Daiichikosho: at contractor Nippon Columbia Group, 「同社従業員の端末がマルウェアに感染し」 *(an employee's device was infected with malware)*
- 027 JR East: 「IDC フロンティア社で発生した不正アクセスに伴い」 *(following unauthorised access at IDC Frontier)*. IDC Frontier (023) itself disclosed 「第三者からのランサムウェア攻撃によるものであることが判明」 *(found to be a ransomware attack by a third party)*, affecting 495 contracting companies and municipalities

**Unauthorised login (1)**

- 022 Scala Communications: 「i-ask の管理サイトに不正にログインし、不正なプログラムを設置したうえで」 *(logged into the i-ask admin site without authorisation and installed a malicious program)*

**Misconfiguration (1)**

- 013 Benefit One: not unauthorised access but 「プログラムの条件設定不備」 *(a program condition misconfiguration)*

**Multiple (1)**

- 028 Adventure: one notice, three vectors — (1) 「一部の管理機能を不正に操作され」 *(an admin function was operated without authorisation)*; (2) 「業務管理システムの脆弱性を悪用されたもの」 *(a vulnerability in a back-office system was exploited)*; (3) 「予約完了ページがログインをしなくても表示できる状態」 *(a booking-confirmation page was viewable without login)*

(Added 3 November 2026)  
With the 229 rows added on 3 November 2026, 226 of 300 rows state a vector and 74 do not: contractor 179, vulnerability 27, unauthorised login 12, multiple 4, misconfiguration 3, VPN vulnerability 1. After re-retrieving the notices on 3 November 2026, three rows (190 Basic, 245 DIRIGIO, 290 Prestige International) were moved from vulnerability or unauthorised login to "vector not disclosed"; the figures above are the corrected ones. Of the 229 new rows, 163 (71%) are contractor rows — organisations each disclosing a single breach at a SaaS they used. Three new notices name a data-analysis tool's vulnerability as the vector without naming the tool (222 NEL, 248 Vook, and 244 Japanticket's external analysis tool); whether it is the same tool cannot be told from the notices.

Contractor chains grew from seven to more than twenty. Counting only rows added on 3 November: Rakus / blastmail 29, Studio 26, Commune 18 (074–092, all disclosed 8–12 October and missed by the third edition), Yumirlink / Cuenote 18 (after its 26 October second notice widened the scope to 49 systems), Arara 11 (plus 295 Hokuriku Electric, whose notice gives 「最大約 380 社分、約 7,700 万件」 without naming the provider), NTT DATA's corporate-bond perk service 6, digital-securities contractors 5 (two name Securitize), Amadeus (airline passenger service system) 7, WASABI SWITCH 6, Y-Mail 6, WASIMIL 4, DIRIGIO 4, Japanticket 4, and a server of Sankei Living Shimbun 4. The vectors at the origins differ (053 Yumirlink: a program vulnerability and acquired credentials; 241 Arara: a web-server vulnerability; 121 FutureShop: a software vulnerability; 154 Sonicmoov: admin-panel credentials and a functional flaw). More chains still do not mean one attacker; what they share is the structure of many organisations entrusting personal data to one SaaS.

(Added 8 November 2026)  
With the 207 rows added on 8 November, 418 of 507 rows state the vector and 89 do not: contractor 356, vulnerability 32, unauthorised login 16, multiple 7, misconfiguration 6, VPN 1, not disclosed 89. Among the 207 new rows alone, contractor rows are 177 (86%), higher still than the fourth edition's 71%. Most disclosures of 3–5 November are one intrusion — at 241 Arara's mail-delivery service — disclosed separately by each organisation that used it directly or through a sub-contractor.

Counting independent intrusions as introduced in the fourth edition's correction, the 30 non-contractor new rows (vulnerability 5, login 4, multiple 3, misconfiguration 3, not disclosed 15) add 30 intrusions, while the 177 contractor rows fold into chains whose origin is in the ledger — Arara (241), Yumirlink (053), Rakus (059), Studio (051), Wasabi (100), Prestige International (290), TKC (320), Navac (361) — or into new chains whose origin notice is not in the ledger: the SMBC Consumer Finance guarantee system (436 as origin, 12 partner banks), Securitize Japan (4), Arcadia "SpeeCAN RAIDEN" (3), CBcloud "PickGo" (2), Shibata Koji Chosa (2). Independent intrusions rise from about 144 to about 180; the vector is known for about 60, still roughly one third.

(Added 10 November 2026)  
With the 77 rows added on 10 November, 482 of 584 rows state the vector and 102 do not: contractor 417, vulnerability 33, unauthorised login 18, multiple 7, misconfiguration 6, VPN 1, not disclosed 102. The 10 November verification reclassified 352 Monteroza from vulnerability to contractor, so the 8 November figures (contractor 356, vulnerability 32) become contractor 357 and vulnerability 31 after the correction. Among the 77 new rows, contractor accounts for 60 (78%). The 17 non-contractor rows (not disclosed 13, vulnerability 2, unauthorised login 2) add independent intrusions, and LENDY Servicer (545, 546) is a new chain whose origin notice is not in the ledger. Counted as independent intrusions, the ledger now holds about 200; the vector is known for 4 of the newly added ones (528, 549, 575, 584).

(Added 14 November 2026)
With the 260 rows added on 14 November, 719 of 844 rows state the vector and 125 do not: contractor 641, vulnerability 36, unauthorised login 24, misconfiguration 10, multiple 7, VPN 1, not disclosed 125. Among the 260 new rows, contractor accounts for 224 (86%). The 36 non-contractor rows (not disclosed 23, unauthorised login 6, misconfiguration 4, vulnerability 3) add independent intrusions. The 224 contractor rows belong to chains whose origin is in the ledger (Arara 241, TKC 320, Asoview, Prestige Core Solution 290 and others), chains whose origin notice entered the ledger in this update (754 OPENLOGI, Dentsu Digital's TONARIWA, Sonicmoov's COMSBI), and chains whose origin notice is not in the ledger (the e-ticketing service teket, Fireworks AI as Notion's AI processor, Branjista Solution's "Matomaru EC Tencho"). The total of independent intrusions introduced in the fourth edition has not been recounted this time.

## Two chains

Two chains in the ledger spread from one origin to several organisations.

**IDC Frontier**: a ransomware attack beginning around 03:40 on 7 October (023) → JR East (027). Press reports extend it to View Card and JR Kyushu, whose primary notices could not be retrieved; they sit outside the ledger.

(Added 16 October 2026)  
In its fifth notice on 14 October, IDC Frontier wrote 「当社としては外部へのデータの流出はなかったと判断しています」 (we judge that no data was exfiltrated). In the same notice it wrote that in the IDCF Cloud Portal 「48社のお客さまの登録情報に対して不正な照会が行われたことを確認しました」 (unauthorised queries against the registration data of 48 customers were confirmed). On 15 October JR East added, at the top of the same PDF URL, that the mail-delivery service provider had reported 「えきねっと会員・大人の休日倶楽部会員の個人情報の漏えいがなかったと判断した」 (it judged that there had been no leak of Ekinet and Otona no Kyujitsu Club members' personal data). The figures 約167万件 and 約39万件 remain in the document. The origin (023) has judged "no exfiltration" and the downstream row (027) has received that report; both rows keep their first-notice values, with the correction recorded in the notes column.

**Commune**: unauthorised access to Commune Inc.'s cloud service → WingArc1st (024), Sansan (030), LIXIL (031), each notified by the contractor around 6 October.

Neither chain implies a single attacker. What they show is a structure: when one contractor falls, its clients disclose together. Part of the clustering of disclosure dates on 8–9 October comes from this structure.

(Added 16 October 2026)  
Adding 033 Daiwa Securities brings a third chain into the ledger. **Scala Communications**: unauthorised login to the i-ask FAQ system (022) → Daiwa Securities (033). Row 022's notice says only 「最大５社」 (up to five client companies) without naming them; 033's notice names the contractor as 「株式会社スカラコミュニケーションズ」. The access windows overlap: row 022 records 2026-10-02 around 20:30 to 10-03 around 08:00, and 033's notice gives 「10 月 2 日 20 時 33 分頃から 10 月 3 日 8 時 1 分頃までの間」 (around 20:33 on 2 October to around 08:01 on 3 October, per the contractor).

(Added 26 October 2026)  
Since 16 October the chains have grown from two to seven. All five new ones start at a SaaS for mail delivery or web building. **Studio**: a vulnerability in the no-code builder (051; intrusion 30 Sep–1 Oct, confirmed 13 Oct) → the Digital Agency (052, 22 Oct). **Yumirlink**: 「合計 5 システム」 of the Cuenote mail-delivery service (053; detected early 16 Oct) → Nomura Securities (065, 23 Oct). **Rakus**: intrusion into two API servers of blastmail (059; emergency stop 00:30, 21 Oct) → Tokyo Metropolitan Government (060), Cells (061); press counts about 245 client organisations, of which the ledger holds the two whose notices the author read. **NEC**: credentials stolen in an attack on a contractor (057) → Osaka University (058, 「77,851人」), which wrote that NEC had shared its personal data on cloud storage 「本学との契約に基づかず」 (outside its contract with the university). **FutureShop**: a vulnerability in the e-commerce platform's server (23:02 on 17 Oct to 00:16 on 18 Oct) → Lindt (070, 「3,147,469件」). The IDC Frontier chain gained Viewcard (042, 「約 403 万件」) and JR Kyushu (043, 「約 130 万件」), both of which reported on 15 October that the contractor had judged no leak — the same structure as 027. That five of seven chains arose after 16 October shows that the "one contractor falls, every client discloses" structure produced the late-October clustering. It still does not mean a single attacker.

(Added 8 November 2026)  
By 8 November the chain structure had concentrated into one system. 137 of the 207 new rows descend from the intrusion at 241 Arara's mail-delivery services ("Arara Message", "repica"). They divide into direct clients and rows via sub-contractors; the largest sub-chain is TKC (320; online-application and My Number Card appointment systems for local governments), through which 55 municipalities each disclosed their own share. Others run via "repica" (21 rows), Asoview (391 Yamanashi Prefecture, 392 Matsue City), FinoValley (377, 378; regional currencies), WingArc NEX, Japan Leisure Channel (379) and ODK Solutions.

Arara's own notices (241) went from "approx. 3.01 million" (first notice, 28 October) to "81,329,467 (approx. 81 million)" (3rd notice, 6 November), split into three routes: via the service 78,102,937; the shared environment 2,842,400; a separate cloud environment 3,249,492. The intrusion vector is "still being identified" — not disclosed. Some client notices (352 Monteroza, MIC, Infomart) quote Arara's explanation as "a vulnerability in the web server".

New non-Arara chains in the fifth edition: the **SMBC Consumer Finance guarantee system** (436, "up to 320,118 persons") with 12 partner banks disclosing on 4–5 November; the **Prestige International** chain (290) with 371 JA Kyosai, 437 Nissan Financial Services "up to approx. 236,000", 488 Porsche Japan, 492 KDDI; **CBcloud "PickGo"** with 328 Seven-Eleven Japan (orderer names in kana "164,180") and 329 Demae-can; **Navac "RESERVE GATE α"** (361) with Osaka Corona Hotel and the Tokyo Islands municipal partnership; **Securitize Japan**'s digital-securities platform with 317 JR West (bonds, via NTT DATA), 321 LIFULL, 322 Pan Pacific International Holdings, 323 Rims Capital — Securitize Japan's own notice has not been found (pending); **Arcadia "SpeeCAN RAIDEN" / "NET119"** (303 Okazaki, 305 Yanai, 309 Funabashi; disclosed 14–21 October, missed in the fourth edition); and a ransomware attack on **Shibata Koji Chosa** (survey contractor) disclosed by 367 Yuzawa City and 487 Yokote City.

(Added 10 November 2026)  
The 60 contractor rows added on 10 November break down as follows: 30 descend from 241 Arara ("Arara Message" and "repica", including rows via GMO Commerce, Asoview, ODK Solutions, TKC and GMO Makeshop); 17 from 290 Prestige International (the business system of its group company Prestige Core Solution, which handles roadside-assistance intake for car insurers, card issuers, bicycle and car-sharing services); 5 rows (7 banks) from the 436 SMBC Consumer Finance guarantee system; 2 each from LENDY Servicer and Shibata Koji Chosa; and 1 each from Studio, Navc "Reserve Gate", NTT DATA (contractor to 579 Sumitomo Life) and a Benefit One contractor (580 Credit Saison). On 8 November the Prestige International chain had 4 client-side rows (371, 437, 488, 492); with rows disclosed 2–6 November that had been missed, it now has 21.

## Rows with no vector

Seventeen rows state none. Times Mobility (6.6 million accounts), Monogatari (10.79 million), Lawson (2.16 million), Seicomart (570,000 accounts), Dai-ichi Life (120,000). Many of the largest rows are here.

(Added 16 October 2026)  
Of the five added rows, 032 Bookoff (up to approx. 6.43 million), 034 Sagawa Express (count under investigation) and 035 Uzabase (no count stated) state no vector. Rows with no vector are now 20.

(Added 26 October 2026)  
Fifteen of the 35 rows added on 26 October state no vector, among them 064 Capcom (11,774,247; the notice says the attack method was identified but does not state it), 038 Yamato Transport, 055 Trustbank, 067 and ST, 046 FANCL/Attenir and 054 Crypton. Rows with no vector are now 35.

"Cause under investigation." That is the honest state of the notice. The book records it as "not disclosed" and does not fill it.

When JPCERT/CC wrote that technical information is "limited and fragmentary," it was writing about these seventeen rows.

(Added 8 November 2026)  
Of the 207 rows added on 8 November, 15 do not state the vector. The large ones: 304 BK Japan (approx. 11.18 million; the method is "under investigation"), 319 WILLs (NetMile, up to approx. 5.49 million), 507 SignalTalk (1,855,578; "the intrusion route has been identified" but not disclosed), 435 NTT DOCOMO (up to approx. 300,000), 436 SMBC Consumer Finance (up to 320,118), 360 Uchicomi (142,591 accounts). Rows with no vector now total 89.

(Added 10 November 2026)  
Of the 77 rows added on 10 November, 13 do not state the vector. The large ones: 577 Nitori Holdings (up to 37.62 million), 578 Sharefull (up to approx. 7.5 million), 556 Aioi Nissay Dowa Insurance (approx. 444,000), 581 OPEN DOOR (Travelko, 381,926), 538 Mitsui Direct General Insurance (up to 234,000) and 569 Step Golf (up to 215,000; the notice says the figure is the number of database entries, not people). Two of the five new rows above one million (577, 578) do not state the vector. Rows with no vector now number 102.

(Added 14 November 2026)
Of the 260 rows added on 14 November, 23 do not state the vector. The large ones: 725 the Japan Chamber of Commerce and Industry (up to approx. 980,000 people / 1.97 million records), 668 Yojiya Group ("confirmed: 131,557"), 716 NTT DATA (Sumitomo Life Vitality users, "approx. 80,000"), 752 SMBC Nikko Securities (employee stock ownership system, "up to 56,487") and 586 Unirita (internal document system, "approx. 51,000"). 754 OPENLOGI is a chain origin, but its own notice does not state the vector. One of the six new rows above one million (725) does not state the vector. Rows with no vector now number 125.

## The structure of time

From rows whose notices give both intrusion and discovery dates:

| ID | Organisation | Intrusion | Discovery | Gap |
|---|---|---|---|---|
| 002 | Digital Agency | 2026-06-25 (mass access detected) | 2026-07-09 | 14 days |
| 025 | Lawson | 2026-09-12 to 14 | 2026-10-07 | 23–25 days |
| 011 | eplus | 2026-09-11 to 12 | 2026-09-14 to 15 | 2–3 days |
| 029 | coconala | 2026-10-08 02:05 | same day, approx. 15:00 | 13 hours |
| 017 | Monogatari | 2026-10-02 (access confirmed) | 2026-10-03 (leak confirmed) | 1 day |
| 028 | Adventure (1) | 2026-10-02 to 04 | 2026-10-05 | 1–3 days |

The spread is wide. Lawson took more than three weeks from intrusion to discovery; coconala cut the attack off in half a day. "AI made attacks faster" corresponds to nothing in this table. What varies is the defender's detection, and it varies widely.

(Added 26 October 2026)  
Rows added on 26 October that give both dates: 069 Green Monster, acquisition 27–30 April 2026, detected 17 October (about five and a half months); 062 Digital Arts, traces 「2025 年 7 月頃にさかのぼる」, found in a 9 October review (over a year); 041 Nikkei, late July → early August (about two weeks, on Google's notification); 051 Studio, 30 Sep–1 Oct → 13 Oct (12–13 days); 046 FANCL/Attenir, 3–10 Oct → 15 Oct; 055 Trustbank, 17 Oct → 19 Oct (2 days); 070 Lindt, night of 17–18 Oct → 19 Oct; 068 Treasure Factory, early 20 Oct → same day; 067 and ST, 07:30 on 22 Oct → 10:00 the same day (2.5 hours), disclosed the next day. The spread widened: a six-month-old acquisition and a 2.5-hour detection were disclosed on the same day, 23 October. Time to disclosure is set by whether detection exists, not by the speed of the attack.

### References

- All quotations in this chapter are from the primary URLs of the rows in Chapter 4.

---

# Chapter 3: Four tiers of evidence — who said what, and how far

"AI was used" is not one claim. There are claims with evidence, claims with traces, claims of possibility, and notices that say nothing. The book sorts them into four tiers.

## Tier 1: Evidence

**Attack on South Korean financial institutions (CrowdStrike Intelligence, 7 October 2026)**

CrowdStrike found, in open directories on an attacker-controlled server, Claude Code session histories, ARTEX configuration files and Claude memory files.

> Analysis of threat actor-controlled open directories uncovered Claude Code session histories

> The campaign was active from late September to early October 2026.

ARTEX is "a recently released open-source agentic penetration testing (pentesting) tool developed in China"; the ARTEX instance "used DeepSeek v4.1-flash as the primary LLM backend." The actor also used GLM-5.3 and Grok 4.6 in other Claude Code sessions, and "asked Claude where threat actors typically sell Korean data breach information."

On attribution, CrowdStrike did not tie the activity to a named adversary, assessed the actor as likely Chinese-speaking and financially motivated, and wrote: "This assessment is made with moderate confidence." On scope: "As of this writing, the number of organizations affected remains unconfirmed."

This is the only case in the autumn of 2026, in Japan or Korea, in which attacker-side AI use is reported with evidence. The form of the evidence — the attacker's own files left exposed — is rare.

(Added 26 October 2026)  
**The serial unauthorised-access cases in Japan (JPCERT/CC, 15 October 2026)**

In "連続不正アクセス事案の攻撃手法に関する調査" (Investigation of the attack methods in the serial unauthorised-access cases), JPCERT/CC reported on attack-source servers:

> JPCERT/CCは、複数の組織と連携し、攻撃に使用された可能性のあるインフラの調査を進めています。

> その過程で、攻撃者がAIを利用して、既知の脆弱性のスキャンやAPI経由での攻撃などを実施していたことを確認しました。

*(In the course of this, we confirmed that the attackers were using AI to scan for known vulnerabilities and to attack via APIs.)*

> こうした攻撃元サーバーはインターネット上で複数確認されており、日本以外の地域向けのWebサービスに対しても攻撃を行っていました。

*(Several such attack-source servers have been confirmed on the internet; they were also attacking web services for regions other than Japan.)*

The evidence sits on the attackers' own servers, which under this chapter's definition counts as the attacker's own material. The book records it as the first case in which attacker-side AI use in Japan is reported with evidence — with two limits. The document names neither the AI nor the tool, and it names no victim, so it cannot be matched to any row. "There is an attack server on which attackers used AI" and "a given row's breach came from that server" are different statements.

**Exposed Cairn panels (NorForge, 19 October 2026)**

NorForge examined unauthenticated control panels of the AI pentesting tool Cairn exposed on the internet ("more than 20 likely malicious panels"). Of the busiest cluster: "AIA0001 targets a wide swath of organizations, mostly in the US, Japan and Australia." An operator task read, in translation, "These are confirmed real shopping/e-commerce websites in four countries (US/CA/JP/AU), with traffic of 200,000–1.5 million." One case study is a "Japanese retailer." All tasks ran under a worker named `claudecode_deepseek-v4.1-flash`, "which could mean a Claude Code harness using the Chinese DeepSeek 4.1 Flash model that was released in September." The form of evidence is the same as CrowdStrike's in Korea — the attacker's control plane left exposed. That a Japanese retailer was targeted is evidenced; which retailer is not stated, and no match to a row is possible.

## Tier 2: Trace

**Trend Micro (Security GO, 8 October 2026, Yuya Sato)**

Much Japanese coverage quoted Trend Micro as saying that "traces of attacks launched automatically using AI have also been confirmed." The book sought Trend Micro's own text. Its Security GO article of 8 October reads:

> 現状、必ずしもこれらの攻撃がAIを直接的に用いたものであるという証拠があるわけではありませんが、ログだけ見ても「これまでとは違う挙動」を捉えていることは事実です。

*(At present there is not necessarily evidence that these attacks used AI directly, but it is a fact that even the logs alone show "behaviour unlike before.")*

The original is more cautious than the quotation. It contains both "there is not necessarily evidence" and "behaviour unlike before." The book records the original wording.

(Added 26 October 2026)  
**JPCERT/CC alert, updated 23 October 2026**

The 8 October alert was updated on 9 and 23 October. The 23 October update added:

> ケースE：AIを用いたペネトレーションテスト基盤を悪用した攻撃試行

> CairnやCyberStrikeAI、ARTEXなどのAIを用いたペネトレーションテスト基盤を悪用した攻撃試行が確認されています。

*(Attack attempts abusing AI-driven penetration-testing platforms such as Cairn, CyberStrikeAI and ARTEX have been confirmed.)*

> これらのツールを用いて、主にインターネットに公開されたWebアプリケーションを標的にさまざまな脆弱性を探索して悪用を試行したり、機器の管理不備等を悪用した攻撃（環境設定ファイルやバックアップファイルの窃取など）を確認しています。

> その中には、インターネットに公開されたWSUSサーバーを標的とした攻撃試行も含まれています。

Nine suspicious source IP addresses are listed with observation windows (the earliest from 23 September, the latest to 20 October). What is confirmed is "attack attempts"; whether any led to a breach is not stated. The book places this in Tier 2. It is a separate document from the 15 October investigation above, and the relation between the two is not stated.

**GMO Cybersecurity by Ierae (19 October 2026, press-based)**

According to press reports, the company announced on 19 October that an investigation of attack-source infrastructure targeting Japanese companies confirmed the use of ARTEX; that about 20 Japanese companies were targeted (nine in one industry); that six more AI-driven attack hosts of the same kind were found; and that eight of the targets had disclosed leaks in September–October. Reports also quote the company's view that the eight leaks were "the work of the same attack group." When the author opened the company's site on 26 October it displayed a notice that the site was temporarily running in a simplified mode as a precaution after a vulnerability was disclosed in widely used software, and the post (`https://gmo-cybersecurity.com/blog/20261019/`) could not be read. Until the original can be read, the book treats this as press-based Tier 2 and does not say which rows the eight are.

**Secure Sky Technology (Scutum, 14 October 2026)**

The developer of the Scutum WAF introduced a detection mechanism on the night of 10 October and wrote that by 14 October it had confirmed AI-agent attacks on Japanese companies' websites from at least three IP addresses. The method is undisclosed; the post says that a detection is conclusive ("false negativeはあるかもしれないが、false positiveはほぼない") but that "攻撃者が実際に使っているモデルが何なのかという情報は取得できません" (which model the attacker uses cannot be obtained). Because the method is not public, the book places this in Tier 2.

**Cyber Security Cloud (9 October 2026)** observed attacks that rotated 326 IP addresses in about 40 minutes with more than 1,200 requests and wrote that "a mechanism that can judge from responses, such as AI, may have been used," adding 「なお、これは観測された振る舞いからの推測であり、AIの利用を直接示す痕跡を確認したものではありません」 (this is an inference from observed behaviour; no trace directly showing AI use was confirmed). Tier 3.

**Macnica (7 October 2026)** wrote 「一連の事案でAIが使われたと断定できるログや痕跡は確認されていません」 (no logs or traces that would establish AI use in the series of cases have been confirmed), that no zero-day exploitation had been confirmed, and that what is actually happening is broad probing and exploitation of basic misconfigurations, access-control gaps and known vulnerabilities. Recorded as a document that explicitly states the absence of AI traces.

**South Korean mega-churches (Oasis Security's CEO, press-based)**

According to the Dong-A Ilbo (7 October 2026), the CEO of Oasis Security said of documents organising the stolen data: 「포맷 자체가 AI를 활용했을 때 나오는 전형적인 형태였다」 *(the format itself was the typical form produced when AI is used)*. Press-based; the firm's own report was not retrieved.

## Tier 3: Possibility

**South Korean financial regulators (press-based)**

Korean press reported a regulatory official saying on 1 October 「전통적인 해킹 방식이 아닌 인공지능(AI)을 이용한 공격이라고 보고받았다」 *(we were briefed that it was an attack using AI, not a traditional hacking method)* and, in the same breath, 「정확한 해킹 방식 등은 점검 결과를 지켜봐야 알 수 있다」 *(the exact method can only be known after the inspection results)*. The chair of the Financial Services Commission said on 4 October 「확정적으로 말씀드리기는 어렵지만 AI를 활용한 해킹공격의 가능성도 배제할 수 없다」 *(it is hard to say definitively, but the possibility of an AI-assisted attack cannot be ruled out)*. All press-based.

The FSC's own releases of 2 and 6 October, as far as the author could read them, contain no reference to attacker-side AI. The "AI" in the 6 October release is a defender-side voice-phishing analysis platform.

**Korea Electric Power (press-based)**

Korean press reported KEPCO describing its own incident as 「최근 인공지능을 활용한 금융권 해킹 공격과는 관련이 없는 것으로」 *(unrelated to the recent AI-assisted attacks on the financial sector)*. A denial by the party itself.

(Added 3 November 2026)  
**The first Japanese notice to mention attacker-side AI about its own incident (079 Chitose Group, posted 9 October, updated 13 October 2026)**

> コミューン株式会社の調査により、攻撃者は、同社が運営管理する全コミュニティ共通のログイン用の署名鍵を入手し、コミュニティの管理者になりすましていたことがわかりました。

> 攻撃は、複数のIPアドレスから短時間に大量の操作を同時に行うものでした。このことから、AI等を用いて自動化された攻撃であったと推定されます。

("The attack consisted of many simultaneous operations in a short time from multiple IP addresses. From this, it is presumed to have been an automated attack using AI or similar.") This book places it in Tier 3 (possibility): the sentence is a presumption; its only stated basis is the shape of the attack, the same type as Cyber Security Cloud's inference above; and it does not say who made the presumption, Commune or Chitose. Commune's own notices render by JavaScript and remain unread.

## Tier 4: No mention

**All 31 Japanese notices**

None of the 31 notices in the ledger refers to AI on the attacker's side. "AI" appears in GMO Research & AI's company name, in WingArc1st's product name "dejiren AI," and in Helpfeel's service description — none a reference to attack technique.

(Added 16 October 2026)  
The notices for the five rows added on 16 October (032–036) also contain no reference to attacker-side AI. All 36 rows remain in Tier 4.

(Added 26 October 2026)  
The notices for the 35 rows added on 26 October (037–071) also contain no reference to attacker-side AI. All 71 rows are in Tier 4. Three notices mention defender-side AI: 054 Crypton Future Media 「Mythosを活用し状況を把握」 (used Mythos to grasp the situation), 062 Digital Arts (a full review of its systems "using AI" on 9 October), and 005 Helpfeel's final report (AI-assisted static analysis as a countermeasure). These describe the defender, not the attacker.

JPCERT/CC's 8 October alert contains no "AI."

(Corrected 26 October 2026)  
The alert was updated on 9 and 23 October. The 23 October update added "Case E: attack attempts abusing AI-driven penetration-testing platforms," and with it the word "AI." The first-edition sentence stands as a description of the 8 October text; the update is recorded in Chapter 3 below.

**Tokyo Shoko Research (7 October 2026)** writes 「AI普及で、より強固な対策が必要なのは当然だが」 *(with AI spreading, stronger measures are of course needed)* — a generality, not a claim about any incident.

(Added 8 November 2026)  
None of the 207 notices added on 8 November mentions attacker-side AI about its own incident. "No mention" stands at 506 of 507 rows. Defender-side AI mentions were not counted exhaustively for the new rows.

(Added 10 November 2026)  
None of the 77 notices added on 10 November mentions attacker-side AI about its own incident either. "No mention" stands at 583 of 584 rows.

(Added 14 November 2026)
None of the 260 notices added on 14 November mentions attacker-side AI about its own incident either. "No mention" stands at 843 of 844 rows. Eight of the new rows report that information entered into Notion's AI feature ("Notion AI") may have leaked through unauthorised access to its processor, Fireworks AI; "AI" there is a product or feature name, not attacker-side AI, and is not counted.

## A dissenting view

Professor Hiroki Takakura of the National Institute of Informatics told ASCII of the Japanese cases: 「攻撃の自動化にAIが使われたとは思いますが、大きな役割は果たしていなかった。言い換えると、対策が不十分だった」 *(I think AI was used to automate the attacks, but it did not play a major role. In other words, the defences were insufficient.)* Press-based. The book records it on the same terms as the views that suspect AI.

## What the four tiers show

Evidence: one case in Korea, none in Japan. Trace: Trend Micro's own text says "not necessarily evidence." Possibility: the Korean regulators' remarks are press-based and absent from their own releases. No mention: all 31 Japanese notices.

This distribution does not mean AI was not used. It means that whether it was used cannot be determined from the Japanese notices. Recording what cannot be determined as undetermined is this chapter's job.

(Added 26 October 2026)  
As of 26 October 2026 the distribution is: **Evidence** — Korea (CrowdStrike), plus Japan's attack-source servers (JPCERT/CC, 15 Oct) and the exposed Cairn panels (NorForge, 19 Oct). **Trace** — JPCERT/CC's alert (23 Oct), Secure Sky Technology (14 Oct), GMO Cybersecurity (19 Oct, press-based). **Possibility** — Cyber Security Cloud (9 Oct), NICT (13 Oct). **No mention** — all 71 Japanese notices. What changed is that "in Japan, attack-source servers on which attackers used AI existed" can now be said from primary sources. What has not changed is that "the 71 rows' breaches were caused by AI" cannot. The evidence appeared on the attacker's side; the victims' notices, all 71, still say nothing. The distance between the two is the shape of the gap on 26 October.

### References

- CrowdStrike Intelligence, as above (Prologue)
- Trend Micro Security GO, Webサーバのセキュリティの要点は？, 8 October 2026 https://www.trendmicro.com/ja_jp/jp-security/26/j/expertview-20261008-01.html
- Dong-A Ilbo, 7 October 2026 (press-based) https://www.donga.com/news/Economy/article/all/20261007/134798126/2
- Financial Services Commission (Korea), press releases of 2 October https://fsc.go.kr/no010101/87869 and 6 October 2026 https://www.fsc.go.kr/no010101/87882
- Gukje News (KEPCO's statement, press-based) https://www.gukjenews.com/news/articleView.html?idxno=3713038
- ASCII (Professor Takakura's comment, press-based)
- Tokyo Shoko Research, as above (Prologue)

---

# Chapter 4: The ledger

## How to read it

- **Admission**: breaches, or possible breaches, disclosed on or after 1 September 2026 by companies, agencies, municipalities and other organisations headquartered or principally operating in Japan, whose primary notice the author opened and read. No lower bound on size.

(Corrected 10 November 2026)  
From the fifth edition, the admission criterion is that the organisation's own primary notice was reached and its text confirms the case is in scope (a breach, or possible breach, of personal data through external unauthorised access). AI agents retrieve and check the notices, recording verbatim the sentences used as evidence; the author spot-checks notices and decides rows on the boundary of the criteria. The 300 rows up to the fourth edition are rows whose notice the author opened and read.

  (Added 11 October 2026)  
  From the second edition onward, newly admitted rows are limited to breaches, or possible breaches, caused by external unauthorised access (including third-party intrusion, unauthorised login, and unauthorised access to a contractor or a service the organisation uses). Cases without external unauthorised access — misdelivery, mis-sent email, loss, erroneous publication, or data left viewable through a configuration error — are not admitted. Whether a case qualifies is decided by whether the notice itself describes external unauthorised access. Row 013 (Benefit One, 「プログラムの条件設定不備」, a program condition misconfiguration), admitted in the first edition, does not meet this criterion but stays as a first-edition row under the append-only rule.

- **Scale**: the notice's own unit (records, persons, accounts). Never converted to persons.
- **Status**: the notice's own wording (confirmed / possible / cannot be ruled out / maximum).
- **Vector**: classified only as far as the notice states; otherwise "unauthorised access (vector not disclosed)."
- **AI mentioned**: whether the body of the notice refers to attacker-side AI. "AI" in company or product names is not counted.
- **Primary source**: the notice the author opened. Retrieved 10 October 2026.
- This table is generated from `data/registry.json` by `scripts/build_registry.py`. All columns (data affected, intrusion/detection dates, notes) are in `data/registry.csv`.

## The 31 rows of the first edition

| ID | Published | Organisation | Scale (as stated, original unit) | Status | Vector | AI mentioned | Primary source |
|---|---|---|---|---|---|---|---|
| 001 | 2026-09-02 | Charm (Charm Honten online pet-supply store) | Confirmed leak "approx. 370,000 records"; possible leak "approx. 20,000 records" (total "approx. 390,000", revised from approx. 230,000 announced on 13 August). Separately, 239 accounts with confirmed unauthorised logins | Confirmed + possible (3rd notice) | unauthorised access (vector not disclosed) | none | [notice](https://www.charm.co.jp/honten/info/notice/20260901.html) |
| 002 | 2026-09-11 | Digital Agency (Government Solution Service, GSS) | "approx. 246,000 records" (staff and public officials "approx. 189,000", businesses and individuals "approx. 57,000"; names approx. 236,000, e-mail approx. 231,000, phone approx. 94,000, addresses approx. 1,000; overlapping) | Possible leak | VPN vulnerability | none | [notice](https://www.digital.go.jp/news/2026-0911-01) |
| 003 | 2026-09-15 | Ainokaze Toyama Railway (sightseeing-train seat system) | "1,409 persons" | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://ainokaze.co.jp/24166) |
| 004 | 2026-09-15 | Rohto Pharmaceutical (mail-order customer-service system) | Count "under investigation" (not determined) | Possible unauthorised acquisition | unauthorised access (vector not disclosed) | none | [notice](https://www.rohto.co.jp/news/whatsnew/2026/0915_01) |
| 005 | 2026-09-16 | Helpfeel (Gyazo image-capture service) | User data "approx. 23.62 million records" (anonymous users without e-mail approx. 18.01 million, 76%; users with e-mail approx. 5.62 million, 24%); image metadata "approx. 490 million records"; filtered image metadata "approx. 2.4 million"; metadata of deleted images "approx. 174 million" (added in the 2nd notice) | Confirmed exfiltration (number of persons under investigation) | vulnerability | none | [notice](https://corp.helpfeel.com/news/news-20260916-1) |
| 006 | 2026-09-25 | Smaregi (Smaregi EC Repeat / B2B) | Environments of "4 client companies"; number of persons not disclosed | Possible viewing or acquisition | vulnerability | none | [notice](https://ec.smaregi.jp/repeat/news/2026925-2/) |
| 007 | 2026-09-25 | Times Mobility (Times Car car-sharing) | "approx. 6.6 million" accounts (2nd notice, 28 Sep); of which identity-document images leaked for "approx. 1.6 million" accounts (3rd notice, 29 Sep) | Confirmed acquisition | unauthorised access (vector not disclosed) | none | [notice](https://www.park24.co.jp/news/2026/09/20260928-1.html) |
| 008 | 2026-09-26 | Nippon Rent-A-Car Service (NR app) | "41 persons" | Possible unauthorised viewing | unauthorised access (vector not disclosed) | none | [notice](https://www.nipponrentacar.co.jp/info/202609.html) |
| 009 | 2026-09-27 | Tokyo Metro (Metpo loyalty programme) | "approx. 59,000 records" | Possible viewing or acquisition | unauthorised access (vector not disclosed) | none | [notice](https://www.tokyometro.jp/info/files/9172e2efa7222d15f8d4f601b6385457.pdf) |
| 010 | 2026-09-27 | Starts Publishing (OZmall) | E-mail addresses "up to 447,610 persons" (27 Sep) → "up to 442,779 persons" (2nd notice, 1 Oct) | Possible viewing (maximum) | unauthorised access (vector not disclosed) | none | [notice](https://starts-pub.jp/info20260927) |
| 011 | 2026-09-29 | eplus (e-ticket refund management system) | "1,463 records" (bank transfer 751, card refund 644, postal money order 68) | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://corp.eplus.jp/press-release/1824/) |
| 012 | 2026-09-29 | Seicomart (Seicomart app) | "approx. 570,000 accounts" (user IDs possibly accessed) | Possible leak (one unauthorised account deletion confirmed) | unauthorised access (vector not disclosed) | none | [notice](https://online.seicomart.co.jp/delivery/cms/preview.php?disp_flg=pc&pre_no=119) |
| 013 | 2026-09-30 | Benefit One (Benefit One Platform) | "2,322 companies/organisations, 13,460 persons" | Data viewable by other client companies (one download by one person at one company; deletion confirmed) | misconfiguration | none | [notice](https://corp.benefit-one.co.jp/company/news/news/2026/20260930/20260930.pdf) |
| 014 | 2026-09-30 | G-Plan (G-Point) | Member identifiers "up to approx. 70,000" | Possible leak (maximum) | unauthorised access (vector not disclosed) | none | [notice](https://www.g-plan.net/news/details/20260930.html) |
| 015 | 2026-10-02 | Japan Organization for Metals and Energy Security (JOGMEC) | Staff e-mail addresses "approx. 1,100"; external e-mail addresses "approx. 7,400" | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.jogmec.go.jp/news/information/information_00706.html) |
| 016 | 2026-10-02 | Dai-ichi Life Insurance (HR system) | "approx. 120,000 persons" (approx. 50,000 employees, approx. 70,000 former employees) | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.dai-ichi-life.co.jp/information/pdf/index_192.pdf) |
| 017 | 2026-10-05 | Monogatari Corporation (Yakiniku King official app) | "the number of leaked records is 10,788,963" (of 10,808,784 registered users) | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.monogatari.co.jp/news/261005_news/) |
| 018 | 2026-10-05 | GMO Research & AI (infoQ survey panel) | "up to 948,498 records" (all records held as of 5 Oct). Fraudulent point exchanges: 611 cases, ¥2,869,500 | Unauthorised access confirmed; count is a maximum | vulnerability | none | [notice](https://gmo-research.ai/pressroom/notice/notice-20261005) |
| 019 | 2026-10-05 | Kufu Company (Machi-Talk beta) | E-mail address of "at least 1 person" confirmed; others under investigation | Confirmed + possible | unauthorised access (vector not disclosed) | none | [notice](https://kufu.co.jp/2026/10/05/kufu-announce/) |
| 020 | 2026-10-05 | Daiki Suisan (official app) | "174,933 persons" (registered 1 Nov 2024–15 Sep 2026, incl. withdrawn members) | Leak cannot be ruled out | unauthorised access (vector not disclosed) | none | [notice](https://www.daiki-suisan.co.jp/files/optionallink/00000164_file.pdf) |
| 021 | 2026-10-06 | MrMax (app and online-store members) | "up to 1,735,154 persons" (members registered as of 3 Oct 2026) | Leak confirmed; count is a maximum | vulnerability | none | [notice](https://www.mrmax.co.jp/info/incident_20261006/) |
| 022 | 2026-10-06 | Scala Communications (i-ask FAQ system) | "up to 713,126" enquiry records (gross, with duplicates); "up to 5" client companies | Possible leak | unauthorised login | none | [notice](https://scala-com.jp/news/2026/10-1/) |
| 023 | 2026-10-07 | IDC Frontier (IDCF Cloud) | "495 companies and municipalities" contracting IDCF Cloud (number of contracting organisations, not of personal records) | Exfiltration of personal data not stated | unauthorised access (vector not disclosed) | none | [notice](https://www.idcf.jp/news/topics/20261007002) |
| 024 | 2026-10-08 | WingArc1st (nest Portal user community) | "approx. 1,200 persons (current estimate; under investigation)" | Possible leak | contractor / third-party service | none | [notice](https://corp.wingarc.com/public/202610/news3042.html) |
| 025 | 2026-10-08 | Lawson (Lawson ID and app reservations) | Lawson ID "2,155,345 records"; app reservations "26 records" (the notice's heading says 'persons' but the unit used is 'records') | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.lawson.co.jp/contents/cont07/1533174_3310.html) |
| 026 | 2026-10-08 | Daiichikosho (customer and employee data of Big Echo and other brands) | "approx. 8,724,000 records" (customers "approx. 8,631,000", employees "approx. 93,000", after deducting duplicates "approx. 515,000") | Possible leak (external leak not confirmed) | contractor / third-party service | none | [notice](https://www.dkkaraoke.co.jp/news/newsletter/261008_2.html) |
| 027 | 2026-10-09 | JR East (Ekinet and Otona no Kyujitsu Club) | Ekinet "approx. 1.67 million records"; Otona no Kyujitsu Club "approx. 390,000 records" (both maxima) | Leak cannot be ruled out | contractor / third-party service | none | [notice](https://www.jreast.co.jp/press/2026/20261009_ho02.pdf) |
| 028 | 2026-10-09 | Adventure Inc. (skyticket travel booking) | (1) "approx. 14.64 million records (of which approx. 4.13 million include login passwords)"; (2) "17,780 records (incl. duplicates; more under investigation)"; (3) bus reservations "approx. 12,000" | (1) confirmed; (2) confirmed or possible; (3) viewed or possibly viewed | multiple vectors | none | [notice](https://skyticket.jp/news/maintenance/67603) |
| 029 | 2026-10-09 | coconala (coconala skill marketplace) | "449 CVs and 1,845 career-history documents" (document counts, not persons) | Confirmed exfiltration | vulnerability | none | [notice](https://coconala.co.jp/news-20261009/) |
| 030 | 2026-10-09 | Sansan (Sansan User Forum community) | Confirmed "1,325 persons"; possible "8,687 persons" | Confirmed + possible | contractor / third-party service | none | [notice](https://jp.corp-sansan.com/news/2026/1009.html) |
| 031 | 2026-10-09 | LIXIL (Sumai Hiroba and Nekokabe Hiroba communities) | Not stated (scope under investigation) | Possible leak | contractor / third-party service | none | [notice](https://www.lixil.co.jp/announce/notice-info-leak.htm) |

(Added 16 October 2026)  
For five of the pending cases, the author opened and read the primary notice on 16 October 2026 and admitted them as rows. The first-edition table of 31 rows stays as it is above; the added rows follow. The two tables together match the 36 rows in `data/registry.json`.

(Added 26 October 2026)  
On 26 October 2026 the author added 35 rows (037–071): six from the pending list and 29 disclosed on or after 16 October. The two earlier tables stay as they are; the added rows follow in a third table. The three tables together match the 71 rows in `data/registry.json`.

### The five rows added on 16 October 2026

| ID | Published | Organisation | Scale (as stated, original unit) | Status | Vector | AI mentioned | Primary source |
|---|---|---|---|---|---|---|---|
| 032 | 2026-10-09 | Bookoff Group Holdings (subsidiary's member-management system) | Member records possibly leaked "up to approx. 6.43 million" (note 1: the count of member numbers, "not the actual number of persons") | Exfiltration confirmed (count is a maximum of possible records) | unauthorised access (vector not disclosed) | none | [notice](https://ssl4.eir-parts.net/doc/9278/tdnet/2893077/00.pdf) |
| 033 | 2026-10-05 | Daiwa Securities (via contractor Scala Communications) | Information on "approx. 110,000 customers" (name, email, account number, etc.); including enquiries without identifying information, "approx. 220,000 records" in total | Possible leak | contractor / third-party service | none | [notice](https://ssl4.eir-parts.net/doc/8601/tdnet/2891437/00.pdf) |
| 034 | 2026-09-30 | Sagawa Express (parcel-enquiry service) | "The number and scope are under investigation" (as of the 2nd notice; not determined) | Possible exfiltration | unauthorised access (vector not disclosed) | none | [notice](https://www2.sagawa-exp.co.jp/information/detail/420/) |
| 035 | 2026-10-08 | Uzabase (NewsPicks) | No count stated ("some of the customers who used NewsPicks services up to 8 October 2026") | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://corp.newspicks.com/info/20261008) |
| 036 | 2026-10-05 | White Essence (booking site and core system) | "Persons affected: approx. 1.05 million accounts" (customers and related parties registered as of 5 August 2026; items vary by person) | Exfiltration found | vulnerability | none | [notice](https://www.whiteessence.co.jp/news/?action=detail&id=56&p=1) |

### The 35 rows added on 26 October 2026

| ID | Published | Organisation | Scale (as stated, original unit) | Status | Vector | AI mentioned | Primary source |
|---|---|---|---|---|---|---|---|
| 037 | 2026-09-28 | Shueisha (HAPPY PLUS COMMUNITY blogger platform) | "2,835 persons" (blogger records "2,835"); project records "630"; all emails sent by the system "11,237"; business-partner list "10,780" (email addresses "26", phone numbers "113") | May have been viewed or taken; leak found | misconfiguration | none | [notice](https://www.shueisha.co.jp/wp-content/uploads/2026/09/Shueisha20260928-1.pdf) |
| 038 | 2026-09-29 | Yamato Transport (Kuroneko deferred-payment service) | "Approx. 5.26 million records" (of which "approx. 490,000" include email addresses); recipients "approx. 50,000"; member merchants "approx. 4,100" (fixed in 4th notice, 16 Oct 2026) | Some data found to have been taken out | unauthorised access (vector not disclosed) | none | [notice](https://www.yamato-hd.co.jp/important/info_260929_1.html) |
| 039 | 2026-10-01 | Japan Atomic Energy Agency (research-support site on contracted cloud) | Unauthorised downloads "2,419 files", of which "367" contain personal data ("175 persons": 200 photo-ID documents incl. 6 with My Number, 146 special health-check results, 21 radiation-worker certificates) | Leak (confirmed) | unauthorised access (vector not disclosed) | none | [notice](https://www.jaea.go.jp/02/press2026/p26100105/) |
| 040 | 2026-10-03 | Recruit (Study Sapuri) | "3,687 records" (email addresses) | Unauthorised access confirmed; no leak of data other than email addresses confirmed | vulnerability | none | [notice](https://studysapuri.jp/info/important/#ssntc_303) |
| 041 | 2026-10-04 | Nikkei Inc. (Google Workspace account) | "1,646 persons" | Suspected leak | unauthorised login | none | [notice](https://www.nikkei.co.jp/nikkeiinfo/news/information/1547.html) |
| 042 | 2026-10-09 | Viewcard (VIEW's NET; via contractor IDC Frontier) | "Approx. 4.03 million records" (email addresses registered with VIEW's NET) | Possible leak; viewing or acquisition cannot be ruled out | contractor / third-party service | none | [notice](https://www.jreast.co.jp/card/news/pdf/20261009.pdf) |
| 043 | 2026-10-09 | JR Kyushu (web members; via contractor IDC Frontier) | "Affected (maximum)": JR Kyushu web members "approx. 1.3 million records" | Possible leak; cannot be ruled out | contractor / third-party service | none | [notice](https://www.jrkyushu.co.jp/common/inc/news/newtopics/__icsFiles/afieldfile/2026/10/09/202691009_mail_address_access_1.pdf) |
| 044 | 2026-10-15 | SourceNext (member-information API) | "Affected: 22,519,960 records" | Leak (confirmed) | vulnerability | none | [notice](https://www.sourcenext.com/support/i/2026/1015_info/) |
| 045 | 2026-10-16 | Nikkei Inc. (development cloud environment) | "Approx. 1.83 million records" (incl. "approx. 150,000" with personal data, of which "approx. 120,000" include email addresses; "approx. 1.68 million" identifiers only) | Leak (confirmed) | unauthorised login | none | [notice](https://www.nikkei.co.jp/nikkeiinfo/news/information/1561.html) |
| 046 | 2026-10-16 | FANCL / Attenir | FANCL "393,785 records, 368,184 persons"; Attenir "441,162 records, 417,312 persons" | Unauthorised access confirmed; no misuse confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.fancl.jp/news/pdf/husei.pdf) |
| 047 | 2026-10-16 | NTT Solmare (Comic Cmoa) | Not stated ("under review") | Leak (confirmed) | unauthorised access (vector not disclosed) | none | [notice](https://www.nttsolmare.com/press/2026/1016.html) |
| 048 | 2026-10-16 | Iwai Cosmo Securities (via contractor Tradeworks) | "Affected: 4,975 persons (364 added in this notice)" (2nd notice, 20 Oct 2026; 1st notice "4,611 persons") | Leak (confirmed) | contractor / third-party service | none | [notice](https://www.iwaicosmo.co.jp/info/2026/10201710.html) |
| 049 | 2026-10-17 | Joshin Denki | Not stated | Leak cannot be ruled out; whether data leaked is under confirmation | unauthorised access (vector not disclosed) | none | [notice](https://www.joshin.co.jp/ja/news/info/info-20261017/main/0/link/20261017Notice%20and%20Apology%20Regarding%20System%20Disruption%20Caused%20by%20Unauthorized%20Access.pdf) |
| 050 | 2026-10-17 | Ishikawa Computer Center (customer-support site) | Not stated | Under investigation | unauthorised access (vector not disclosed) | none | [notice](https://www.icc.co.jp/news/2026/20261017.html) |
| 051 | 2026-10-18 | Studio Inc. (no-code web builder "Studio") | Not stated ("counts per function are under review") | Unauthorised access confirmed; possible leak; treated as taken | vulnerability | none | [notice](https://studio.design/ja/security/notice/2026-10-incident) |
| 052 | 2026-10-22 | Digital Agency (web forms; via contractor Studio Inc.) | Opinions etc. "max. 8,833"; recruitment enquiries "max. 250"; vaccination-certificate app enquiries "max. 3,661"; mascot-costume loans "max. 117"; event applications "max. 462"; Studio accounts "35" | Possible leak | contractor / third-party service | none | [notice](https://www.digital.go.jp/press/a0a8f66c-b32d-4695-9372-bcd5d4280f22) |
| 053 | 2026-10-19 | Yumirlink (Cuenote FC and other mail-delivery systems) | Estimated "approx. 9 million records (cumulative) including email addresses were output"; "5 systems in total" | Exfiltration of personal data confirmed | vulnerability | none | [notice](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261019/20261019553124.pdf) |
| 054 | 2026-10-19 | Crypton Future Media (SONICWIRE / D2R) | Member records "362,137"; quotation/invoice records "671"; non-member newsletter "11" (updated 22 Oct 2026; first notice "max. approx. 420,000") | Leaked (changed from "possible" in 22 Oct update) | unauthorised access (vector not disclosed) | none | [notice](https://www.crypton.co.jp/cfm/news/2026/10/20info) |
| 055 | 2026-10-20 | Trustbank (Furusato Choice) | "4,454,097 records" ("may change with further investigation") | Leaked externally (facts still being confirmed) | unauthorised access (vector not disclosed) | none | [notice](https://www.trustbank.co.jp/newsroom/newsrelease/news261020/) |
| 056 | 2026-10-20 | MLIT (Housing Energy-Saving 2024 Campaign office, run by Hakuhodo) | "23,918 persons (16,950 businesses) (preliminary)" | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.mlit.go.jp/report/press/house04_hh_001366.html) |
| 057 | 2026-10-20 | NEC Corporation (via a contractor) | Not stated | Leak confirmed | contractor / third-party service | none | [notice](https://jpn.nec.com/news/info/20261020.html) |
| 058 | 2026-10-21 | Osaka University (via contractor NEC) | "77,851 persons (deduplicated)" ("graduates 59,014, students 15,035, staff 3,802") | Leak (confirmed) | contractor / third-party service | none | [notice](https://www.osaka-u.ac.jp/ja/news/topics/2026/10/21004) |
| 059 | 2026-10-21 | Rakus / Rakus Light Cloud (blastmail) | Number of contracts not stated (sales-management data of "all contracting customers"); contracts whose recipient lists were confirmed leaked updated in later notices (press: "344" as of 24 Oct) | Exfiltration confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.rakus.co.jp/news/2026/1021-3.html) |
| 060 | 2026-10-23 | Tokyo Metropolitan Government (via contractor Rakus Light Cloud) | "Max. approx. 16,000 records" | Possible leak | contractor / third-party service | none | [notice](https://www.metro.tokyo.lg.jp/information/press/2026/10/2026102317) |
| 061 | 2026-10-23 | Cells Co. (via contractor Rakus Light Cloud) | "Max. approx. 18,000 records (under review)" | Possible leak | contractor / third-party service | none | [notice](https://www.cells.co.jp/news/115953) |
| 062 | 2026-10-21 | Digital Arts (cloud-service operating environment) | Not stated | Some customer data possibly viewed by a third party | unauthorised login | none | [notice](https://www.daj.jp/ir/data/daj2326_202703_3q_1.pdf) |
| 063 | 2026-10-22 | GMO Internet (Onamae.com Desktop Cloud) | "Servers possibly affected: 26,739" | Unauthorised access and exfiltration of customer data confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.onamae.com/news/article/11593) |
| 064 | 2026-10-22 | Capcom (CAPCOM ID) | "Affected: 11,774,247 records (worldwide)" (incl. "43" with date of birth etc., "196" with passwords changed without authorisation) | Unauthorised access confirmed; part of customer data found leaked | unauthorised access (vector not disclosed) | none | [notice](https://www.capcom.co.jp/ir/news/html/261022.html) |
| 065 | 2026-10-23 | Nomura Securities (i-Port; via contractor Yumirlink) | Not stated | Reported as possibly leaked | contractor / third-party service | none | [notice](https://www.nomuraholdings.com/jp/news/topics/20261023.html) |
| 066 | 2026-10-15 | M3 Inc. (MR-kun pharma-facing service) | m3.com members etc. "25,775 persons" ("6 include email addresses"); pharma-company staff "2,260 persons" ("264 include email addresses") (fixed 23 Oct 2026) | Unauthorised access confirmed; no misuse confirmed | unauthorised access (vector not disclosed) | none | [notice](https://corporate.m3.com/assets.ctfassets.net/1pwj74siywcy/TYwLIgktADUIxwA5M6XFE/3bcb64e5e6857ebaf8e5a5a4efd8f25f/20261023_Public_J.pdf) |
| 067 | 2026-10-23 | and ST HD (formerly Adastria) | Customers "approx. 2.5 million records"; business partners "approx. 10,000"; employees "scope under confirmation" | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.andst-hd.co.jp/news/notice/entry-17234/) |
| 068 | 2026-10-23 | Treasure Factory (case-management system) | Customer records affected "746,277" (email addresses; "of which 11" include name and address). Separately, business partners/employees: "names and email addresses: 750", "names and device identifiers: 1,000" | Unauthorised acquisition confirmed | vulnerability | none | [notice](https://www.treasure-f.com/info/detail/st825/) |
| 069 | 2026-10-23 | Green Monster (FX Navi app) | "Approx. 6.19 million user records etc." (email "66,003", gender "142,578", age band "139,293", occupation "149,137", X IDs "6,434", first-survey answers "4,809,631", transfer codes "5,120" etc.) | Possibly acquired; no leak confirmed | vulnerability | none | [notice](https://assets.minkabu.jp/news/article_media_content/urn:newsml:tdnet.info:20261023555394/140120261023555394.pdf) |
| 070 | 2026-10-23 | Lindt & Sprüngli Japan (via contractor FutureShop) | "3,147,469 records" (members at the time of intrusion, excluding withdrawn) | Unauthorised access confirmed; no misuse confirmed | contractor / third-party service | none | [notice](https://www.lindt.jp/contents/chocolat-cafe/notice_20261023/) |
| 071 | 2026-10-22 | System5 (system linked to its online shop) | "Max. approx. 15,000 persons" (24 Oct 2026) | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://info.system5.jp/whatsnew/apology-20261024) |

(Added 3 November 2026)  
229 rows were added: 14 from the pending list and 215 disclosed 9 October – 2 November 2026. Earlier tables are unchanged; together the four tables match the 300 rows of `data/registry.json`. IDs follow the publication date; the order within one date carries no meaning. (Added 3 November 2026) Five rows whose publication date was corrected after the IDs were assigned (126, 146, 184, 213, 283) kept their IDs, so for these five the ID order does not match the date order. As in the third edition, the author opened and read the primary notice of each of the 229 rows before inclusion. In addition, on 3 November 2026 an AI agent re-retrieved the primary notice of each of the 229 rows and compared scale and unit, status wording, vector, AI mention and publication date with the notice: 186 matched; values corrected in 24; a note added in 7; 2 left unchanged because the notes already said it; 9 annotated in the notes as boundary cases for admission criterion 3 (leak or possible leak of personal information); 1 (239) could not be retrieved. The notes carry the tag 「（2026年11月3日、一次公表文を再取得して照合）」. Rows 072–300 were retrieved on 3 November 2026. Candidate discovery and drafting used AI-agent web search and retrieval of each notice, as in the third edition; passages whose verbatim match could not be confirmed are marked 「逐語未確認」 in the notes column.

### The 229 rows added on 3 November 2026

| ID | Published | Organisation | Scale (as stated, original unit) | Status | Vector | AI mentioned | Primary source |
|---|---|---|---|---|---|---|---|
| 072 | 2026-09-25 | Fines (reservation systems "Itsuaki" and "TSUNAGU") | "Records affected: 1,536,322" | Leak confirmed for reservation data; other data possibly leaked, under investigation | vulnerability | none | [notice](https://e-tenki.co.jp/news/reserve-system-incident/) |
| 073 | 2026-09-25 | Japan Post (web form for international mail inquiry requests) | "Customer information (approx. 600 records)" (16 Oct update) | Viewable by third parties; actual viewing not confirmed; no misuse found | unauthorised access (vector not disclosed) | none | [notice](https://files.japanpost.jp/assets/34d9d11432734cfaa759e78fe395b688/99a38c8fdea24951b26188d86b797684/20261016_04_01.pdf) |
| 074 | 2026-10-08 | VALX (VALX "FUN" community, via Commune) | "Member list information of 2,950 of 3,813 members" | Possibly viewed/acquired (estimated) | contractor / third-party service | none | [notice](https://corp.valx.jp/news/451vhhqdf29c/) |
| 075 | 2026-10-08 | Aomori Prefecture (tourism fan community 'Aomori Biiki', via Commune) | "Up to 2,950 persons" (prefecture) / "2,950 (est.)" (Commune's document in the same PDF) | Possible leak | contractor / third-party service | none | [notice](https://www.pref.aomori.lg.jp/release/files/2026/81561.pdf) |
| 076 | 2026-10-08 | OPEN SMILE (points site "Warau") | Not stated | Member information possibly acquired by a third party | vulnerability | none | [notice](https://www.opensmile.co.jp/corp/news/note/20261015/) |
| 077 | 2026-10-09 | LY Corporation (DS.LAB community in DS.INSIGHT, via Commune) | "Information of 1,750 users" | Possibly viewed/acquired | contractor / third-party service | none | [notice](https://www.lycorp.co.jp/ja/privacy-security/announcement/020892/) |
| 078 | 2026-10-09 | ZENB JAPAN (online community ZENB GARDEN, via Commune) | "Leak of 897 members confirmed"; "up to all 949 members" | Leak confirmed | contractor / third-party service | none | [notice](https://zenb.jp/blogs/news/20261009) |
| 079 | 2026-10-09 | Chitose Group (community site 'Chitose Academy', via Commune) | "Max. 843 persons at present" | Possibly viewed/acquired; leak presumed | contractor / third-party service | 「AI等を用いて自動化された攻撃であったと推定されます。」 | [notice](https://chitose-bio.com/jp/news/12177/) |
| 080 | 2026-10-09 | Doppuri Kochi Tabi Campaign Committee (Kochi tourism fan site, via Commune) | "All 358 members" | Partially viewed/acquired (leaked) | contractor / third-party service | none | [notice](https://doppuri.kochi-tabi.jp/news/information.html?id=77) |
| 081 | 2026-10-09 | Calbee (fan site 'Zeppin-bu', via Commune) | Not stated | Viewed/acquired | contractor / third-party service | none | [notice](https://www.calbee.co.jp/notice/pdf/69-54565.pdf) |
| 082 | 2026-10-09 | Suzuki (official car community 'Suzuki Village', via Commune) | "Member information of approx. 3,000 persons" | Possibly viewed/acquired | contractor / third-party service | none | [notice](https://www.suzuki.co.jp/release/d/2026/1009/) |
| 083 | 2026-10-09 | Softbrain (eSales Manager user community site, via Commune) | "Persons affected: 1,164" | Possible leak | contractor / third-party service | none | [notice](https://www.softbrain.co.jp/news/topics/2026/20261009_1817/) |
| 084 | 2026-10-09 | Bandai Namco Experience (Wangan Midnight Arcade Portal, via Commune) | "Member information of 1,694 persons" | Possible leak | contractor / third-party service | none | [notice](https://wanganmaxi-official.com/wanganmaxi6rrplus/jp/news/035.html) |
| 085 | 2026-10-09 | Panasonic (LUMIX community and Hairsup community, via Commune) | "Approx. 2,000 (LUMIX community) and approx. 3,000 (Hairsup)" | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.panasonic.com/jp/about/news/20261009.html) |
| 086 | 2026-10-09 | Yamaha Corporation (Yamaha Network Engineer community, via Commune) | "Approx. 1,600 persons" | Leaked; no misuse confirmed | contractor / third-party service | none | [notice](https://www.yamaha.com/ja/news_release/files/news/26100901/pdf/2610090101.pdf) |
| 087 | 2026-10-09 | Unifa (childcare worker site 'Lookmee Room', via Commune) | "Member information of 1,450 persons" | Possibly viewed/acquired | contractor / third-party service | none | [notice](https://unifa-e.com/news/info/20261009-info) |
| 088 | 2026-10-09 | JMA Management Center (community site 'Toki Labo', via Commune) | "Persons affected: 2,950" | Leak confirmed | contractor / third-party service | none | [notice](https://www.jmam.co.jp/assets/images/topics/toki-labo_20261009.pdf) |
| 089 | 2026-10-09 | Morinaga Milk (fan community 'Mount Cafe-bu', via Commune) | "Member list information of 291 members" | Possibly viewed/acquired (estimated); outflow not confirmed | contractor / third-party service | none | [notice](https://www.morinagamilk.co.jp/information/newsentry-4168.html) |
| 090 | 2026-10-09 | Koikeya (fan site 'Koikeya GOGO! Land', via Commune) | "Members affected: up to 1,800" | Viewed and partially leaked | contractor / third-party service | none | [notice](https://koikeya.co.jp/images/pdf/info_20261009.pdf) |
| 091 | 2026-10-11 | Future Design Shibuya ('Shibuya Mirai Design COMMUNITY', via Commune) | "495 registered members" | Possibly viewed/acquired | contractor / third-party service | none | [notice](https://fds.or.jp/news/1091/) |
| 092 | 2026-10-12 | Yamaha Motor (YAMAHA PAS Life community, via contractor Commune) | "Member information of approx. 1,600 persons" | Possibly viewed/acquired; possible leak | contractor / third-party service | none | [notice](https://global.yamaha-motor.com/jp/news/2026/1012/leakage.html) |
| 093 | 2026-10-14 | Aena (off-price store "Aena" EC app) | "Members whose data may have been viewed: max. 817,215 persons" | My-page data possibly viewed; no secondary damage confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.aena.co.jp/news/detail/7826/) |
| 094 | 2026-10-15 | ACCESS Co., Ltd. (Taiwan subsidiary ACCESS AP TAIWAN; e-commerce support service "CROS") | "155,280 customer IDs", "231,998 order IDs", card-related "1,671 (gross)" / "1,305 accounts"; full card data for 4 | Leaked externally | unauthorised access (vector not disclosed) | none | [notice](https://www.access-company.com/files/2026/10/n261015.pdf) |
| 095 | 2026-10-15 | Medley (clinic support system "@link" and patient app) | "Up to all 787 medical institutions using @link etc." (patient count not disclosed) | Possible leak (15 Oct) -> leak confirmed (23 Oct) | unauthorised access (vector not disclosed) | none | [notice](https://www2.jpx.co.jp/disc/44800/140120261014550839.pdf) |
| 096 | 2026-10-15 | Daiwa Institute of Research (Naito Securities' online trading system "Financial Plate/WB4", operated under contract) | "Max. 631 persons" (users logged in during the access window) | Possible leak; no misuse or fraudulent withdrawals/trades confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.dir.co.jp/release/2026101501.pdf) |
| 097 | 2026-10-16 | Link-U Group (corporate site inquiry form, via Studio) | "7,663 records (as of 16 Oct 2026)" | Possible leak | contractor / third-party service | none | [notice](https://content.link-u.co.jp/irdata/news/ir-news_261016_01.pdf) |
| 098 | 2026-10-16 | Luup (website forms, via Studio) | "21,368 records in total, including multiple submissions by the same person" | Possible outflow; actual acquisition not confirmed | contractor / third-party service | none | [notice](https://luup.sc/news/2026-10-16/) |
| 099 | 2026-10-16 | Raksul (website forms, via Studio) | "6,412 records" (form submissions, not persons) | Possible leak; actual acquisition not confirmed | contractor / third-party service | none | [notice](https://corp.raksul.com/news/press/261016raksul_studio/) |
| 100 | 2026-10-16 | Wasabi (EC order management system WASABI SWITCH) | Not stated | Outflow confirmed | unauthorised access (vector not disclosed) | none | [notice](https://wasabi-inc.biz/help/news/20261016-01/) |
| 101 | 2026-10-16 | Kyoto City (arts programmes run via Kyoto Arts and Culture Association, via Studio) | "30 records" and "3 records" | Possible leak | contractor / third-party service | none | [notice](https://www.city.kyoto.lg.jp/bunshi/page/0000359411.html) |
| 102 | 2026-10-16 | Minaminihon Broadcasting (forms on four event sites, via Studio) | "29", "5", "2", "2" records (four sites) | Possible outflow | contractor / third-party service | none | [notice](https://www.mbc.co.jp/info/owabi/index.html) |
| 103 | 2026-10-16 | Saitama Prefecture (Saitama Green Forest Museum, managed by Ishizaka Sangyo, via Studio) | "162 records of personal information" (as of 16 Oct) | Possible leak | contractor / third-party service | none | [notice](https://www.pref.saitama.lg.jp/a0508/news/page/news2026101603.html) |
| 104 | 2026-10-16 | Fukuoka City (startup division / Fukuoka Growth Next website forms, via Studio) | City: "name and email of 42 persons". Fukuoka Growth Next: "185", "87", "190", "3", "89", "75" records by form | Possible leak (under investigation) | contractor / third-party service | none | [notice](https://www.city.fukuoka.lg.jp/shisei/kouhou-hodo/hodo-happyo/2026/documents/261016_sogyo.pdf) |
| 105 | 2026-10-16 | TradeWorks (online trading system provided to Iwai Cosmo Securities) | "4,611 persons" (16 Oct) -> "4,975 persons" (23 Oct update) | Leak confirmed (first report); described as possible leak in update; no secondary damage confirmed | misconfiguration | none | [notice](https://www2.jpx.co.jp/disc/39970/140120261023555541.pdf) |
| 106 | 2026-10-17 | OpenStreet (HELLO CYCLING website forms, via Studio) | "1,734 stored responses in total" | Possible outflow; actual acquisition not confirmed | contractor / third-party service | none | [notice](https://www.openstreet.co.jp/news/usLRgR7Y) |
| 107 | 2026-10-17 | Smartround (website forms, via Studio) | "1,371 records (approx. 1,050 persons)" | Possible outflow | contractor / third-party service | none | [notice](https://jp.smartround.com/corporate/news/posts/Ab4Kkfrj) |
| 108 | 2026-10-17 | Tohoku Electric Power Frontier (website inquiries, via Studio) | "182 records cumulative" | Possible leak | contractor / third-party service | none | [notice](https://www.tohoku-epco.co.jp/information/1249253_2521.html) |
| 109 | 2026-10-19 | Uzabase (website forms, via Studio) | Not stated | Possible outflow | contractor / third-party service | none | [notice](https://www.uzabase.com/jp/info/20261019/) |
| 110 | 2026-10-19 | Mitsuke City (relocation site 'Happiness Mitsuke', via Studio) | "13 individuals, 57 companies" | Possible leak | contractor / third-party service | none | [notice](https://www.city.mitsuke.niigata.jp/soshiki/19/59434.html) |
| 111 | 2026-10-19 | Hankyu Hanshin Department Stores / H2O Retailing (H2O ID, reservation site) | "Part of the personal data of approx. 1.26 million H2O ID records leaked"; 2nd report adds "6,243" reservation-form entries | Leak confirmed (H2O ID); e-commerce sites under investigation, later no leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.hankyu-dept.co.jp/honten/info/detail/__icsFiles/afieldfile/2026/10/19/1019owabi1.pdf) |
| 112 | 2026-10-20 | Youji Katsudou Kenkyukai (corporate network) | Not stated | Under investigation; no leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261020/20261020553396.pdf) |
| 113 | 2026-10-20 | San Holdings (flower/offering e-order systems of sub-subsidiaries Tamanoya and Kigetsudo Celeo) | Not stated | Possible leak; no leak or exfiltration traces confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www2.jpx.co.jp/disc/96280/140120261020553567.pdf) |
| 114 | 2026-10-20 | Kusatsu City (Kusatsu River Park website, via park manager / Studio) | "108 records in total" (as of 16 Oct) | Possible leak | contractor / third-party service | none | [notice](https://www.city.kusatsu.shiga.jp/kurashi/toshikeikaku/kusatsugawaatochi/oshirase/kusatsu_river221019.html) |
| 115 | 2026-10-21 | AZOO (hotel management system WASIMIL) | Not stated (under investigation) | Leak confirmed | vulnerability | none | [notice](https://www.wasimil.com/press-release/incident-report-20261021) |
| 116 | 2026-10-21 | M3 (M3PSP service site and '1 person 1 yen fund' site, via Studio) | M3PSP "271 persons"; fund site "127 persons" | Possible leak; actual acquisition not confirmed | contractor / third-party service | none | [notice](https://corporate.m3.com/assets.ctfassets.net/1pwj74siywcy/7tQjGKGMtsasFkBD2dX3Sq/05abba2f58cdd6543d38fa3c6e5e140c/20261021_Public_J.pdf) |
| 117 | 2026-10-21 | Recruit (Carsensor.net / C-MATCH) | "Max. 3,709,551 records" (users who enquired with dealers 3,210,421; review posters 5,289; C-MATCH dealers 483,168; staff/contractors etc. 10,673) | Possible leak; no secondary damage confirmed as of 21 Oct | unauthorised access (vector not disclosed) | none | [notice](https://www.recruit.co.jp/newsroom/pressrelease/2026/1021_149447.html) |
| 118 | 2026-10-22 | Valtec ("MOT" business system series) | 3rd report: "Corporate info of service contractors: 1,213"; "Sales etc. data: 875 companies"; personal-data count under investigation | 1st: deemed outflow confirmed; 2nd: possible leak, not confirmed; 3rd: data sent out may include personal data | vulnerability | none | [notice](https://www.webjapan.co.jp/maintenance/serviceteishi261022/) |
| 119 | 2026-10-23 | istyle (part of its email delivery, via Ymirlink Cuenote FC) | Not stated | Personal data taken out (per contractor) | contractor / third-party service | none | [notice](https://www.istyle.co.jp/news/info/2026/10/20261023.html) |
| 120 | 2026-10-23 | Xebio Holdings (subsidiary GALLERY 2; third-party EC platform "Commerble") | "(1) buyer info max. approx. 128,000; (2) address info max. approx. 122,000; (3) email history max. approx. 158,000" (categories overlap; not a head count) | Possible leak; no exfiltration confirmed | contractor / third-party service | none | [notice](https://www2.jpx.co.jp/disc/82810/140120261022554661.pdf) |
| 121 | 2026-10-23 | FutureShop (SaaS EC platform "futureshop") | "3,147,469 records / 1 store" | Leak confirmed; no secondary damage reported | vulnerability | none | [notice](https://www.future-shop.jp/news/2026/10/23.html) |
| 122 | 2026-10-24 | Half Price (Noukasan no Mikata e-commerce order management, via WASABI SWITCH by Wasabi Inc.) | Not stated | Outflow reported by vendor | contractor / third-party service | none | [notice](https://noukasan-mikata.com/article/127685/) |
| 123 | 2026-10-24 | Shizuoka City Culture & Creative Industry Center (CCC newsletter, via Blastmail) | Not stated | Possible leak; no leak confirmed | contractor / third-party service | none | [notice](https://www.c-c-c.or.jp/schedule/2026-10-24%E3%80%80%E3%80%90%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B-%E3%80%91ccc%E3%83%A1%E3%83%BC%E3%83%AB%E3%83%9E%E3%82%AC%E3%82%B8%E3%83%B3%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6) |
| 124 | 2026-10-24 | NGT48 (Official CD Shop newsletter, via Blastmail) | Not stated (under confirmation with provider) | Notified of leak to outside | contractor / third-party service | none | [notice](https://ngt48.boosty.app/feeds/1268) |
| 125 | 2026-10-24 | Human Respect (Mind Map School mail service, via Y-Mail) | Not stated (3 phishing mails sent) | Possible outflow under investigation | contractor / third-party service | none | [notice](https://www.mindmap-school.jp/【重要】不正アクセスおよび情報流出の可能性に関するお詫びと注意喚起/) |
| 126 | 2026-10-26 | Minamiuonuma City (mail service, via Y-Mail) | Not stated | Possible leak; under investigation | contractor / third-party service | none | [notice](https://www.city.minamiuonuma.niigata.jp/docs/87148.html) |
| 127 | 2026-10-24 | Daito Kaihatsu (Katashina Kogen newsletter, via Y-Mail) | "253 customers" (30 Oct follow-up); phishing sent to approx. 30,800 addresses | Possibly misused (24 Oct); possibly viewed (30 Oct) | contractor / third-party service | none | [notice](https://katashinakogen.co.jp/20261024topics/) |
| 128 | 2026-10-24 | Yamada Shoten (newsletter, via Blastmail) | Not stated (cites provider's 344 contracts) | Possible leak; whether own list affected not confirmed | contractor / third-party service | none | [notice](https://www.yamada-shoten.com/onlinestore/blog/?p=28370) |
| 129 | 2026-10-24 | Iwakuni City (Commerce Promotion Division newsletter, via Blastmail) | Not stated | Possible leak; not confirmed | contractor / third-party service | none | [notice](https://www.city.iwakuni.lg.jp/soshiki/38/121455.html) |
| 130 | 2026-10-24 | Chozo Goya (reservation system, via AZOO "WASIMIL") | Not stated | Possible outflow | contractor / third-party service | none | [notice](https://chozogoya.com/contents/info20261024.html) |
| 131 | 2026-10-24 | Syuppin (external marketplace stores incl. Rakuten Ichiba, via WASABI "WASABI SWITCH") | "Order information from customers on external marketplace sites: 2,269 (up 53 from 2,216 reported on 23 Oct)"; 2nd report: "admin account info: 31" | Outflow confirmed (per WASABI's notice, 23 Oct) | contractor / third-party service | none | [notice](https://www.syuppin.co.jp/news/%e3%80%90%e9%87%8d%e8%a6%81%e3%81%aa%e3%81%8a%e7%9f%a5%e3%82%89%e3%81%9b%e3%80%91%e5%a7%94%e8%a8%97%e5%85%88%e3%81%a7%e3%81%82%e3%82%8b%e6%a0%aa%e5%bc%8f%e4%bc%9a%e7%a4%be%e3%83%af%e3%82%b5%e3%83%93/) |
| 132 | 2026-10-24 | Igreks (email delivery service "Y-mail") | "Total number of records leaked or possibly leaked: 22,527" (19th report, 2026-11-03); the 6th report said up to 30 addresses per mail magazine possibly viewed | Email addresses possibly viewed; no direct exfiltration of personal data found | multiple vectors | none | [notice](https://igreks.jp/archives/782) |
| 133 | 2026-10-24 | Kakao Piccoma (Piccoma; via contractor Rakus Lite Cloud "blastmail") | "Customer email addresses (1,002,404)" | Leaked externally | contractor / third-party service | none | [notice](https://www.kakaopiccoma.com/info/%e6%a0%aa%e5%bc%8f%e4%bc%9a%e7%a4%be%e3%83%a9%e3%82%af%e3%82%b9%e3%83%a9%e3%82%a4%e3%83%88%e3%82%af%e3%83%a9%e3%82%a6%e3%83%89%e3%81%ae%e3%83%a1%e3%83%bc%e3%83%ab%e9%85%8d%e4%bf%a1%e3%82%b7%e3%82%b9.html) |
| 134 | 2026-10-24 | Chariloto (keirin/autorace betting app "Chariloto") | "Affected: 373 persons" | Leak confirmed; no secondary misuse confirmed | vulnerability | none | [notice](https://chariloto.jp/news/20261024/index.html) |
| 135 | 2026-10-25 | Gifu Association of Radiological Technologists (member mailing, via Blastmail) | Not stated | Possible outflow | contractor / third-party service | none | [notice](https://gifuart.org/blog/info/%e9%87%8d%e8%a6%81%e5%bd%93%e4%bc%9a%e5%88%a9%e7%94%a8%e3%81%ae%e3%83%a1%e3%83%bc%e3%83%ab%e9%85%8d%e4%bf%a1%e3%82%b7%e3%82%b9%e3%83%86%e3%83%a0%e3%81%b8%e3%81%ae%e4%b8%8d%e6%ad%a3%e3%82%a2%e3%82%af/) |
| 136 | 2026-10-25 | Hida Takayama Tourism & Convention Association (official tourism site inquiry form, maintained by Travelzip) | "449 records (excluding duplicates)" | Leak confirmed | vulnerability | none | [notice](https://dmo-hidatakayama.com/news/417/) |
| 137 | 2026-10-25 | eJudo (mailing list, via Blastmail) | Not stated ("entire mailing list" reported leaked) | Leak confirmed | contractor / third-party service | none | [notice](https://ejudo.info/articles/34272) |
| 138 | 2026-10-25 | Futaba Town, Fukushima (town newsletter, via Y-Mail) | "Up to 60 records may have leaked" (2nd report, 27 Oct); approx. 1,400 subscribers | Possible outflow | contractor / third-party service | none | [notice](https://www.town.fukushima-futaba.lg.jp/12944.htm) |
| 139 | 2026-10-26 | Gunosy (internal business account) | Business partners "25 persons", officers/employees etc. "107 persons" | Leak confirmed | unauthorised login | none | [notice](https://gunosy.co.jp/news/464) |
| 140 | 2026-10-26 | Asmarq (D style web etc., via contractor Ymirlink) | Not stated (being identified by Ymirlink) | Possible leak | contractor / third-party service | none | [notice](https://www.asmarq.co.jp/news/external_service_20261026/) |
| 141 | 2026-10-26 | Cybozu (notification mail list, via contractor Ymirlink) | Not stated (scope not yet confirmed) | Leak highly likely | contractor / third-party service | none | [notice](https://topics.cybozu.co.jp/news/2026/10/26-19556.html) |
| 142 | 2026-10-26 | Doutor Coffee (internal system, employee data) | "951 persons in total" (employees and former employees of 4 stores) | Possibly leaked | unauthorised access (vector not disclosed) | none | [notice](https://www.doutor.co.jp/news/newsrelease/detail/20261026144748.html) |
| 143 | 2026-10-26 | ValueCommerce (mail delivery, via contractor Ymirlink) | Not stated in first report; 30 Oct addendum: "6,096 (7,588 cumulative)" | Leak highly likely | contractor / third-party service | none | [notice](https://www.valuecommerce.co.jp/news/c_news/6819/) |
| 144 | 2026-10-26 | Bandai Namco HD / BANDAI SPIRITS / Bandai Logipal (Ichiban Kuji ONLINE delivery data) | Not stated (under investigation) | Possible leak confirmed | unauthorised login | none | [notice](https://www.bandainamco.co.jp/files/2026102620HPE794A820E4B88DE6ADA3E382A2E382AFE382BB.pdf) |
| 145 | 2026-10-26 | Money Forward and group companies (inquiry forms, via contractor Studio) | Money Forward "4,150", MF Home "713", MF X "257", MF Kessai "2,984", Outlook Consulting "5" | Possible leak; leak not confirmed | contractor / third-party service | none | [notice](https://corp.moneyforward.com/news/info/20261026-mf-press-1/) |
| 146 | 2026-10-30 | Yakult Honsha (official website) | Not stated in first report; second report (30 Oct): "approx. 40,000" | Leak confirmed (second report) | unauthorised access (vector not disclosed) | none | [notice](https://www.yakult.co.jp/maintenance/) |
| 147 | 2026-10-26 | Chubu Electric Power (mail magazine, via subcontractor using Blastmail) | "324 persons" | Possible leak; no actual leak confirmed | contractor / third-party service | none | [notice](https://www.chuden.co.jp/publicity/press/1218551_3273.html) |
| 148 | 2026-10-26 | Japan Post Group Union (JP Rouso, legacy mail magazine system) | "40,000 or more" | Leak discovered | unauthorised access (vector not disclosed) | none | [notice](https://www.jprouso.or.jp/system/servlet/yusei.UserMain?method=show_detail&clause_id=18457) |
| 149 | 2026-10-26 | Rakuten Group (Rakuten Travel overseas hotel booking pages and multilingual booking site) | Event 1: "max. approx. 40,000" bookers (of which "max. approx. 36,000" with payment info), "max. approx. 2.6 million" logged-in users; Event 2: "max. approx. 860,000" and "max. approx. 40,000" property staff accounts | "Information subject to unauthorised access" (no 'leak' wording) | unauthorised access (vector not disclosed) | none | [notice](https://travel.rakuten.co.jp/info/announce/20261026.html) |
| 150 | 2026-10-26 | Shizuoka Gas (Web Eneria member site, via contractor Rakus Lite Cloud) | "95,412 records" | Leak confirmed (taken out) | contractor / third-party service | none | [notice](https://www.shizuokagas.co.jp/news/documents/20261026_1.pdf) |
| 151 | 2026-10-26 | JR Central, JR West and JR Kyushu (EX reservation / smartEX, via Ymirlink) | Count "being confirmed by Ymirlink" | Leak reported by contractor | contractor / third-party service | none | [notice](https://jr-central.co.jp/news/release/_pdf/000046119.pdf) |
| 152 | 2026-10-26 | ZEN University (inquiry form, via Studio) | "Max. 107 records" | Possible outflow | contractor / third-party service | none | [notice](https://zen.ac.jp/news/202610_announcement_studio) |
| 153 | 2026-10-26 | Akatsuki (web forms of four group companies, via Studio) | "Max. 2,884 records in total" (Akatsuki 425, Akatsuki Solutions 936, Akatsuki Ventures (Dawn Capital) 531, Akatsuki Media Studio 992) | Found to have been retrievable from outside (possible outflow) | contractor / third-party service | none | [notice](https://aktsk.jp/news/77142/) |
| 154 | 2026-10-26 | Sonicmoov ("COMSBI Enterprise Platform") | Not stated (only some customers affected) | Leaked or possibly leaked | multiple vectors | none | [notice](https://sonicmoov.com/news/xr5qdn-cnfsn) |
| 155 | 2026-10-26 | Panhouse (forms on former website, via Studio) | "1,209 records in total (739 persons)" | Possible outflow; actual exfiltration not confirmed | contractor / third-party service | none | [notice](https://panhouse.jp/news/2026-10-notice-001/) |
| 156 | 2026-10-26 | Furukawa Electric Power Systems (shipment management web system, Disaster Prevention Products Div.) | Not stated (under review) | Possibly viewed or acquired from outside | unauthorised access (vector not disclosed) | none | [notice](https://www.feps.co.jp/news/20261026/) |
| 157 | 2026-10-26 | Tokuma Shoten ("GoodsPress Web" test environment) | "103 records in total" | Possible leak; actual leak or misuse not confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.tokuma.jp/news/n65028.html) |
| 158 | 2026-10-26 | JMA Management Center (email delivery via Ymirlink "Cuenote") | Not stated (contents and count under confirmation) | Leak of part of the information confirmed | contractor / third-party service | none | [notice](https://www.jmam.co.jp/assets/images/topics/cuenote_20261026.pdf) |
| 159 | 2026-10-26 | Yomisen (Yomisen WEST Shikoku branch website, "Yomi Post" leaflet service) | "At least 1,700 persons" | Possible outflow | unauthorised access (vector not disclosed) | none | [notice](https://www.yomisen.co.jp/news/info/2603.html) |
| 160 | 2026-10-26 | FTF Inc. (online order management, via WASABI SWITCH by Wasabi Inc.) | "906 order records in total" | Possible outflow | contractor / third-party service | none | [notice](https://ftfinc.co.jp/%E3%80%90%E9%87%8D%E8%A6%81%E3%80%91%E3%80%8Cwasabi-switch%E3%80%8D%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%8A%E7%9F%A5/) |
| 161 | 2026-10-26 | GoWeb Cloud (rental application service GoWeb) | Not stated (under investigation) | Possibly affected information (no explicit leak wording) | vulnerability | none | [notice](https://gowebcloud.co.jp/news-ir/803) |
| 162 | 2026-10-26 | MMDLabo (MMD Research Institute newsletter, via Blastmail) | Not stated | Leak confirmed (27 Oct update) | contractor / third-party service | none | [notice](https://mmdlabo.jp/press_release/detail_2582.html) |
| 163 | 2026-10-26 | Asakawa Systems (BowNow email function, via sub-contractor Blastmail) | "Up to 8,500 records" (exact count under investigation) | Leak confirmed | contractor / third-party service | none | [notice](https://www.a-sk.co.jp/news/7471/) |
| 164 | 2026-10-26 | Iwaki Film Commission Council (extras registrant mailing, via Blastmail) | Not stated | Possible leak; not confirmed as of 26 Oct | contractor / third-party service | none | [notice](https://iwaki-fc.jp/2026/news/8038/) |
| 165 | 2026-10-26 | Apides (BowNow email function, via sub-contractor Blastmail) | "Up to 4,483 records" (exact count under investigation) | Leak confirmed (heading says possible scope) | contractor / third-party service | none | [notice](https://www.apides.co.jp/news/261026.html) |
| 166 | 2026-10-26 | Dear Care (Dear Care / Dear Care Premium, via an external system it uses) | Not stated | Outflow not confirmed but cannot be ruled out | unauthorised access (vector not disclosed) | none | [notice](https://dearcare.almediaweb.jp/maintenance/maintenance.html) |
| 167 | 2026-10-26 | Tricycle (order management, via WASABI SWITCH by Wasabi Inc.) | "312 order records in total" | Possible outflow | contractor / third-party service | none | [notice](https://tricycle-ce.com/archives/599) |
| 168 | 2026-10-26 | Kyoto Bunkyo University (essay scoring service AI.R-Scorer by LevelEnter) | "18 faculty" and "197 FY2026 Faculty of Sociology entrants (excluding transfer students)" | Possible leak; no exfiltration confirmed | contractor / third-party service | none | [notice](https://www.cyber.kbu.ac.jp/kbu/whatnew/2026/10/post-288.html) |
| 169 | 2026-10-26 | Kyosei Co., Ltd. (BowNow email, via sub-contractor Blastmail) | "Up to approx. 5,500 records" (exact count under investigation) | Leak confirmed | contractor / third-party service | none | [notice](https://www.kyosei-kk.co.jp/news/detail_8.html) |
| 170 | 2026-10-26 | Taiwa Town, Miyagi (matchmaking and tourism bus tour applicants, via contractor Sendai Living Shimbun / Sankei Living Shimbun server) | "61 persons" (matchmaking) and "29 persons" (bus tour) | Possible outflow/leak | contractor / third-party service | none | [notice](https://www.town.taiwa.miyagi.jp/material/files/group/3/2026_10_26.pdf) |
| 171 | 2026-10-26 | Hiroshima Prefectural Board of Education (Early Childhood Education Support Center survey-monitor recruitment, via contractor Hiroshima Living Shimbun / Sankei Living Shimbun server) | "65 records" | Possible leak | contractor / third-party service | none | [notice](https://www.pref.hiroshima.lg.jp/uploaded/attachment/687440.pdf) |
| 172 | 2026-10-26 | Higashimatsushima City (matchmaking event applicants, via contractor Sendai Living Shimbun / Sankei Living Shimbun server) | "47 persons" | Possible leak | contractor / third-party service | none | [notice](https://www.city.higashimatsushima.miyagi.jp/kurashi/manabu-tanoshimu/kekkonshien/261026.files/1.pdf) |
| 173 | 2026-10-26 | giftee (Tabisaki Nozei ID, e-Machi Platform, giftee Benefit mailings, via Rakus Lite Cloud "blastmail") | Not stated (the 344 cumulative confirmed cases are Rakus Lite Cloud's; giftee's contract is not among them) | Possible leak; actual leak not confirmed | contractor / third-party service | none | [notice](https://giftee.co.jp/press/news/info20261026/) |
| 174 | 2026-10-27 | DCM Holdings (Maibo member mail, via contractor Ymirlink) | Not stated (first report) | Possible leak | contractor / third-party service | none | [notice](https://www.dcm-hc.co.jp/news/news_file/file/20261027news.pdf) |
| 175 | 2026-10-27 | NTT Docomo (docomo Hikari plala S course, via contractor Sony Network Communications) | "443,495 records" | Leak confirmed | contractor / third-party service | none | [notice](https://www.docomo.ne.jp/info/notice/page/261027_05_m.html) |
| 176 | 2026-10-27 | Zigexn (Minaoshi B2B comparison site mail magazine, via contractor Rakus Lite Cloud) | "40,026 records" | Leak confirmed | contractor / third-party service | none | [notice](https://3naoshi.com/announcements/20261027) |
| 177 | 2026-10-27 | Resona Bank, Saitama Resona Bank, Kansai Mirai Bank (via contractor Ymirlink) | Not stated (under investigation by Ymirlink) | Highly likely taken out; possible leak | contractor / third-party service | none | [notice](https://www.resona-gr.co.jp/holdings/news/newsrelease_c/2026/files/20261027_1t.pdf) |
| 178 | 2026-10-27 | Sony Network Communications (So-net member database) | So-net members "2,141,986", plala (S course) members "443,495", bank account data "16", member notice data "7" | Leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.sonynetwork.co.jp/corporation/release/2026/v5e5u00000000zwj-att/20261027.pdf) |
| 179 | 2026-10-27 | Sourcenext (mail delivery, via contractor Ymirlink) | Not stated (not yet determined) | Possible leak | contractor / third-party service | none | [notice](https://www.sourcenext.com/support/i/2026/1027_info/) |
| 180 | 2026-10-27 | Bandai Namco Entertainment / BANDAI SPIRITS (THE GUNDAM BASE MEMBERS, via contractor Ymirlink) | "346,247 records" | Leaked | contractor / third-party service | none | [notice](https://www.bandainamcoid.com/portal/info?mode=detail&id=1221) |
| 181 | 2026-10-27 | Bushiroad (BanG Dream! Our Notes CBT applicants and support users, via development contractor) | CBT applicants "10,194", staff "71", survey respondents "5", support inquirers "3,034" | Leak confirmed | contractor / third-party service | none | [notice](https://bushiroad.co.jp/media/a87298c628c65925) |
| 182 | 2026-10-27 | Mos Food Services (SNS campaign, external tool OWNLY) | Not stated | Traces of viewing/downloading | contractor / third-party service | none | [notice](https://www.mos.jp/topics/20261027_1/) |
| 183 | 2026-10-27 | Cable Television Toyama (application/inquiry forms, via Studio) | Not stated | Possible outflow; acquisition by third parties not confirmed | contractor / third-party service | none | [notice](https://ctt.ne.jp/news/important/webstudio.html) |
| 184 | 2026-10-30 | Sendenkaigi (email delivery via Ymirlink "Cuenote FC") | "Confirmed leak count: 194,175 (unique email addresses)" (2nd report, 30 Oct 2026) | Possible outflow (1st report); leak count confirmed (2nd report) | contractor / third-party service | none | [notice](https://www.sendenkaigi.com/news/9mbgxovav) |
| 185 | 2026-10-27 | MICIN (curon online medical consultation) | "3 medical institutions (73 patients)"; 6 accounts at 5 institutions; 14 patient accounts | Possibly viewed | unauthorised login | none | [notice](https://micin.jp/news/14859/) |
| 186 | 2026-10-27 | UPSIDER (Breakthrough GRID member site) | Not stated | Leak confirmed; data exfiltrated | unauthorised access (vector not disclosed) | none | [notice](https://corp-news.up-sider.com/261027-pr-2/) |
| 187 | 2026-10-27 | Dou Shuppan (mail service, via Y-Mail) | Not stated | Possible leak (reported by provider) | contractor / third-party service | none | [notice](https://www.dou-shuppan.com/20261027-3/) |
| 188 | 2026-10-27 | SmartShare (SNS campaign tool "OWNLY") | "14,034 records" | Leak confirmed | vulnerability | none | [notice](https://www.smartshare.jp/news/20261027) |
| 189 | 2026-10-27 | Daihatsu Motor (Daihatsu Media Site, via Blastmail) | Not stated | Leak reported by provider | contractor / third-party service | none | [notice](https://www.daihatsu.com/jp/news/2026/20261027-1.html) |
| 190 | 2026-10-27 | Basic Inc. (ferret One) | Not stated (6 accounts with unauthorised login) | Possibly viewed or acquired | unauthorised access (vector not disclosed) | none | [notice](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261027/20261027556805.pdf) |
| 191 | 2026-10-27 | Chitose City (website mail service, via Blastmail) | "1,141" | Leak confirmed | contractor / third-party service | none | [notice](https://www.city.chitose.lg.jp/c70/1002860/1007035.html) |
| 192 | 2026-10-27 | Miyazaki Prefecture (AR tourism guide, via palan) | "551 records" | Outflow confirmed | contractor / third-party service | none | [notice](https://www.pref.miyazaki.lg.jp/kanko-suishin/press/2026/10/20261027100338.html) |
| 193 | 2026-10-27 | Gifu Prefecture (digital stamp rally; contractor Gifu Shimbun, subcontractor palan) | "Email addresses of 1,135 participants" | Leak confirmed | contractor / third-party service | none | [notice](https://www.pref.gifu.lg.jp/site/pressrelease/524450.html) |
| 194 | 2026-10-27 | Hiroshima Gakuin Junior & Senior High School (Microsoft 365 accounts) | Not stated (8 accounts compromised; phishing to 2,107 mailboxes) | Possibly viewed | unauthorised login | none | [notice](https://www.hiroshimagakuin.ed.jp/oshirase/oshirase-82418/) |
| 195 | 2026-10-27 | Japan External Trade Organization (JETRO "e-Venue", via contractor) | "Up to 133" | Possible leak | contractor / third-party service | none | [notice](https://www.jetro.go.jp/news/announcement/2026/5eebe72f41bc2230.html) |
| 196 | 2026-10-27 | Inuneko Seikatsu (house-call clinic website, via Studio) | "148 records" (inquiry form, 23 Apr 2024–3 Oct 2026) | Possible leak | contractor / third-party service | none | [notice](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261027/20261027556466.pdf) |
| 197 | 2026-10-27 | Yugi Tsushin (corporate member mailing, via Blastmail) | Not stated | Possible leak; not confirmed | contractor / third-party service | none | [notice](https://www.yugitsushin.jp/announcement/%E3%83%A1%E3%83%BC%E3%83%AB%E3%83%9E%E3%82%AC%E3%82%B8%E3%83%B3%E9%85%8D%E4%BF%A1%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%80%8C%E3%83%96%E3%83%A9%E3%82%B9%E3%83%88%E3%83%A1%E3%83%BC%E3%83%AB%E3%80%8D/) |
| 198 | 2026-10-27 | Tokyo Fire Department (via LEVEL ENTER, contractor grading recruitment exam essays) | "Images of past recruitment-exam essays and correction results (198 items)"; one contains a staff member's name | Possible leak | contractor / third-party service | none | [notice](https://www.tfd.metro.tokyo.lg.jp/inf/saiyo-hacking.html) |
| 199 | 2026-10-27 | Ibaraki Prefectural Board of Education ("Ibaraki no Shogai Gakushu" newsletter, via Rakus Lite Cloud "blastmail") | "Registered email addresses: 1,390 (as of 30 Sep 2026)" | Possible leak; as of 1 Nov no report that registered addresses were leaked | contractor / third-party service | none | [notice](https://www.gakusyu.pref.ibaraki.jp/plugin/blogs/show/339/2726/686) |
| 200 | 2026-10-28 | B-R 31 Ice Cream (31 Mobile Order, via DIRIGIO) | "9,799 orders", "max. 8,174 customers", "190 stores" | Leak confirmed | contractor / third-party service | none | [notice](https://www.br31.jp/contents/topics/261028_01.html) |
| 201 | 2026-10-28 | ENEOS Power (ENEOS Denki) | "57 records (57 persons)" | Leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.eneos-power.co.jp/denkigas/information/uploads/denki-important-20261028-394.pdf) |
| 202 | 2026-10-28 | Rise UP (MoreContact, via contractor Ymirlink) | "1,548,002 records" (cumulative, duplicates included) | Leaked | contractor / third-party service | none | [notice](https://r-up.jp/news/2026-10-28-cuenote-fc/) |
| 203 | 2026-10-28 | Animate (online shop / Pokedora mail magazines, via contractor Ymirlink) | Not stated (under investigation by Ymirlink) | Leak confirmed | contractor / third-party service | none | [notice](https://www.animate.co.jp/news/53375/) |
| 204 | 2026-10-28 | GameTrade (game account trading site) | Not stated (first report) | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://gametrade.jp/official_notifications/283) |
| 205 | 2026-10-28 | Subway Japan (official mobile order, via DIRIGIO PICKS) | "3 stores", "7 orders / 7 customers" | Possible leak | contractor / third-party service | none | [notice](https://subway.co.jp/news/bhi2h9kf00mf/) |
| 206 | 2026-10-28 | Better Home Association (mail-order newsletter, via Blastmail) | "7,015 records" | Leaked | contractor / third-party service | none | [notice](https://www.betterhome.jp/info/48303) |
| 207 | 2026-10-28 | Benefit One (Tokugai for Credit Saison members, via contractor Forestec) | "Tokugai: 29,465 persons" | Leak confirmed | contractor / third-party service | none | [notice](https://corp.benefit-one.co.jp/company/news/news/2026/20261028/20261028.pdf) |
| 208 | 2026-10-28 | Persona (H2O Retailing subsidiary, info mail, via contractor Ymirlink) | "28,052 records" | Highly likely acquired | contractor / third-party service | none | [notice](https://www.h2o-retailing.co.jp/ja/news/news3907232089918425776/main/0/link/PERSONA_20261028.pdf) |
| 209 | 2026-10-28 | Medicare Life Insurance (via insurance agent Sony Life's system) | "approx. 385,000 records" | Leak confirmed | contractor / third-party service | none | [notice](https://www.medicarelife.com/pdf/20261029.pdf) |
| 210 | 2026-10-28 | Life Card (notification mail, via contractor Ymirlink) | "Contracts affected: 339,610"; partial ETC card numbers "60" | Possible leak | contractor / third-party service | none | [notice](https://www.lifecard.co.jp/info/important-notice.html) |
| 211 | 2026-10-28 | Kyushu University (alumni mail via Blastmail; QLIFICA clinical trial system) | Mail service registrations "max. 9,999"; QLIFICA "9 staff" | Leak confirmed (alumni); possible (QLIFICA) | contractor / third-party service | none | [notice](https://www.kyushu-u.ac.jp/ja/notices/view/3198) |
| 212 | 2026-10-28 | Miyagi Prefecture (relocation mail magazine, via contractor Image Park using Blastmail) | "2,271 subscriber email addresses" | Possible leak | contractor / third-party service | none | [notice](https://www.pref.miyagi.jp/soshiki/sinkou/zyouhourouei-miyagiizyuukouryuugaido.html) |
| 213 | 2026-10-30 | Japan Airlines / Japan Transocean Air (reservation records, via contractor Amadeus) | "approx. 90,000" + "approx. 2,000" = "approx. 92,000 persons" | Traces of being viewed | contractor / third-party service | none | [notice](https://www.jal.co.jp/ja-jp/news/general/2026/other/261028.html) |
| 214 | 2026-10-28 | Hana Cupid (Internet Hana Cupid etc.) | "4,238,242 records (customers possibly affected)" | Leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.hana-cupid.co.jp/news/news/20261028/) |
| 215 | 2026-10-28 | Kagoshima Bank, Minami-Nippon Bank, Kagoshima Sogo Shinkin, Kagoshima Shinkin (Paydon, via contractor Arara) | Not stated | Possible leak confirmed | contractor / third-party service | none | [notice](https://www.kagin.co.jp/important/emergency_20261029_3.html) |
| 216 | 2026-10-28 | Miyagi Prefecture (remote-island campaign photo contest entrants, via contractor Sendai Living Shimbun / Sankei Living Shimbun server) | "18 applicants" | Possible outflow | contractor / third-party service | none | [notice](https://www.pref.miyagi.jp/soshiki/sinkou/ritou_20261028.html) |
| 217 | 2026-10-28 | H2INT (game store "DIRECT GAMES") | Not stated | Leak of member information confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.h2int.jp/news/news_view.html?idx=456) |
| 218 | 2026-10-28 | Generic Seiyaku (mail order; warehouse management system used by its delivery contractor) | No count; all customers whose shipments were arranged on or before 23 Oct 2026 | Leak highly likely | contractor / third-party service | none | [notice](https://shop.generics.co.jp/shop/information/gene20261028) |
| 219 | 2026-10-28 | Saitama Prefecture (Kawagoe Prefectural High School festival inquiry form, via Studio) | "39 persons" | Possible leak | contractor / third-party service | none | [notice](https://www.pref.saitama.lg.jp/f2207/news/page/news2026102801.html) |
| 220 | 2026-10-29 | AB Accomo (IMANO Osaka Shinsaibashi Hostel, via AZOO's WASIMIL) | Not stated (under investigation) | Leak confirmed | contractor / third-party service | none | [notice](https://imano.jp/osaka/204-2/) |
| 221 | 2026-10-29 | ELESTYLE (OneQR / elepay admin system) | "Part of merchants' registration data (7,162 records)" | Possibly acquired by outside party | vulnerability | none | [notice](https://elestyle.jp/20261029-report) |
| 222 | 2026-10-29 | NEL (osina) | "235,329 persons" (per the preliminary report filed with the PPC on 17 Oct 2026) | Leak to outside confirmed | vulnerability | none | [notice](https://www.nel-all.com/news/632/) |
| 223 | 2026-10-29 | NTT Smile Energy (Eco-Megane solar monitoring service) | "Under review" (30 Oct update) | First notice: no outflow confirmed; 30 Oct: judged possible leak | unauthorised access (vector not disclosed) | none | [notice](https://nttse.com/news/2026/10-29/3284/) |
| 224 | 2026-10-29 | PIECE Inc. (PIECE HOSTEL SANJO, via AZOO's WASIMIL) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://piecehotel.com/jp/news/6xIeAuj4) |
| 225 | 2026-10-29 | Ryori Okoku editorial office (Ryori Okoku web magazine) | "Approx. 8,000 records (cumulative)" | Leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://cuisine-kingdom.com/pdf/202610.pdf) |
| 226 | 2026-10-29 | Clubnets (CN Point satellite systems) | "16,936 (unique)" member ID + name; "2,857 (unique)" member ID, name, email, phone, address | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.clubnets.jp/infos/id/221) |
| 227 | 2026-10-29 | GOODS Co. (former online shop goods-co.net) | "Approx. 19,000 persons" (registered members of old site); guest buyers under investigation | Possible leak; no actual leak or misuse confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.goods-co.net/blogs/news/security-incident-20261029) |
| 228 | 2026-10-29 | StarFlyer (Amadeus passenger service system via ANA) | Not stated | Traces of viewing reported | contractor / third-party service | none | [notice](https://www.starflyer.jp/news/2026/news_20261029_info.html) |
| 229 | 2026-10-29 | Solaseed Air (Amadeus passenger service system via ANA) | Not stated | Traces of viewing reported | contractor / third-party service | none | [notice](https://www.solaseedair.jp/info/2026/10/info-20261029.html) |
| 230 | 2026-10-29 | Chugoku Electric Power (reward delivery via Sagawa Express) | "Approx. 17,600 records (including duplicates)" | Possible leak | contractor / third-party service | none | [notice](https://www.energia.co.jp/assets/info/2026/info20261029.pdf) |
| 231 | 2026-10-29 | All Nippon Airways (booking data via Amadeus passenger service system) | Not stated (first notice) | Traces of data being viewed reported | contractor / third-party service | none | [notice](https://www.anahd.co.jp/group/pr/202610/notification.html) |
| 232 | 2026-10-29 | Hachijuni Nagano Bank (Wallet+ mailing, via iBank / Uyumi Link) | "88,107 email addresses" | Leak confirmed | contractor / third-party service | none | [notice](https://bank.82group.jp/news/2026/20261029.html) |
| 233 | 2026-10-29 | Japan Society of Civil Engineers (email delivery via Arara) | Not stated | Contractor reported leak of some email addresses; whether JSCE's are included is under investigation | contractor / third-party service | none | [notice](https://committees.jsce.or.jp/jsceoffice/node/218) |
| 234 | 2026-10-29 | Yamanashi Prefecture (home-care training / advisory forms, via Studio) | "59", "54", "102", "90" by form/year | Possible leak reported; no leak confirmed | contractor / third-party service | none | [notice](https://www.pref.yamanashi.jp/release/imuka/0810/r8zaitakuiryokensyuukaiadobaizari.html) |
| 235 | 2026-10-29 | Japan Post (International Mail My Page service notification emails, via email-delivery contractor) | Not stated | Possible leak of email addresses | contractor / third-party service | none | [notice](https://www.post.japanpost.jp/newsrelease/pressrelease/01175116571.html) |
| 236 | 2026-10-29 | Okinawa Prefecture ("Shima-maru" newsletter, via Arara) | "2,560 records" | Possible leak | contractor / third-party service | none | [notice](https://www.pref.okinawa.lg.jp/kensei/shinko/1017087/1017118/1041801.html) |
| 237 | 2026-10-29 | Kanagawa Prefecture ("On-Kana! news" newsletter, via Rakus Lite Cloud) | "Approx. 7,800" (email addresses) | Possible leak | contractor / third-party service | none | [notice](https://www.pref.kanagawa.jp/docs/ap4/prs/r5309411.html) |
| 238 | 2026-10-29 | Nagaoka City (inquiry forms of municipal sports facilities, via Studio) | "63" (Yukyuzan Stadium) and "16" (Tochio sports facilities) | Possible leak; no outflow confirmed | contractor / third-party service | none | [notice](https://www.city.nagaoka.niigata.jp/shisei/cate02/houdou-shiryou/file/20261029-05.pdf) |
| 239 | 2026-10-29 | Takatsuki City (i-FILTER@Cloud, via Digital Arts) | Not stated | Possibly viewed; no exfiltration confirmed | contractor / third-party service | none | [notice](https://www.city.takatsuki.osaka.jp/soshiki/90/188920.html) |
| 240 | 2026-10-29 | Treasure Factory (subsidiaries Pickup Japan and GK Factory, via WASABI SWITCH by Wasabi) | Pickup Japan "2,026 order records"; GK Factory "253 order records", "63 purchase records" (data units, not persons) | Partial outflow confirmed | contractor / third-party service | none | [notice](https://www.treasure-f.com/info/detail/st831/) |
| 241 | 2026-10-29 | Arara (email delivery service "Arara Message") | "Approx. 3.01 million email addresses" | Exfiltration confirmed | vulnerability | none | [notice](https://www.arara.com/news/info/20261029_arara) |
| 242 | 2026-10-30 | AIRDO (Amadeus passenger service system via ANA) | Not stated | Traces of viewing reported | contractor / third-party service | none | [notice](https://www.airdo.jp/news/2026/news-10716.html) |
| 243 | 2026-10-30 | AUTHENTIC JAPAN (COCOHELI mailing, via Arara) | Not stated | Contractor confirmed outflow; whether COCOHELI customers are included is unknown | contractor / third-party service | none | [notice](https://www.cocoheli.com/news/suspicious-email) |
| 244 | 2026-10-30 | CS-C (Japan Food Guide, via Japanticket) | Not stated | Outflow | contractor / third-party service | none | [notice](https://s-cs-c.com/news/20261030/) |
| 245 | 2026-10-30 | DIRIGIO (mobile ordering platform PICKS) | "9,992 orders"; "8,312 persons (deduplicated, incl. non-member orders)" | Leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://dirigio.jp/news/release20261030) |
| 246 | 2026-10-30 | Japanticket (external analytics tool) | "Max. approx. 264,000 records (under review)" | Leak confirmed | contractor / third-party service | none | [notice](https://www.japanticket.com/news-20261029/) |
| 247 | 2026-10-30 | KDDI / LIFENET Insurance (au life insurance linkage system) | "4,524", "226", "8,434", "3,662", "4,888", "807" records by data combination (no total stated) | Possible leak | vulnerability | none | [notice](https://newsroom.kddi.com/news/assets/2026/kddi_nr_s-82_4796/kddi_nr_s-82_4796_pdf_01.pdf) |
| 248 | 2026-10-30 | Vook (video-creator platform, internal data-analysis tool) | Not stated | Possible leak | vulnerability | none | [notice](https://vook.co.jp/574) |
| 249 | 2026-10-30 | jinjer (inquiry form, via Studio) | "173 submissions (cumulative)" | Possible outflow | contractor / third-party service | none | [notice](https://jinjer.co.jp/news/post-14906/) |
| 250 | 2026-10-30 | IBEX Airlines (Amadeus passenger service system via ANA) | Not stated | Traces of viewing reported | contractor / third-party service | none | [notice](https://www.ibexair.co.jp/information/20261030-info.html) |
| 251 | 2026-10-30 | LTR (Chiikawa Bakery priority-entry booking, via Japanticket) | Not stated | Leak confirmed | contractor / third-party service | none | [notice](https://chiikawabakery.jp/20261030_news/) |
| 252 | 2026-10-30 | Oriental Air Bridge (Amadeus passenger service system via ANA) | Not stated | Traces of viewing reported | contractor / third-party service | none | [notice](https://www.orc-air.co.jp/20261030-23936/) |
| 253 | 2026-10-30 | Ganesha (SHOGUN BURGER app mobile ordering, via DIRIGIO) | Not stated | Leak confirmed | contractor / third-party service | none | [notice](https://shogun-burger.com/news/217) |
| 254 | 2026-10-30 | Coade (online lottery "Hanikuji Land") | "Max. 7,622 persons" | Possible outflow | unauthorised access (vector not disclosed) | none | [notice](https://www.coade-net.co.jp/blog/topics/38538/) |
| 255 | 2026-10-30 | Suzuki Motor (Suzuki media site mailing, via Arara) | "Max. 2,575 email addresses" | Possible outflow | contractor / third-party service | none | [notice](https://www.suzuki.co.jp/release/d/2026/1030/) |
| 256 | 2026-10-30 | Sony Bank (digital securities, via external contractor) | "4 customers: name, address, DOB, account number"; "617 customers: name" | Leak confirmed | contractor / third-party service | none | [notice](https://sonybank.jp/info/2026/1030-01.html) |
| 257 | 2026-10-30 | DHC (DHC online shop) | "Data altered in 5,096 accounts (max. 5,520 addresses), 27 suspicious orders, 71 fraudulent registrations" | Possibly viewed; no exfiltration confirmed | vulnerability | none | [notice](https://dhc-corporate.co.jp/cms_dH8vjpRq/wp-content/uploads/2026/10/0deb6f2426f1d5ab2b2b1824288b374d.pdf) |
| 258 | 2026-10-30 | Medianavi (newsletter, via Rakus Lite Cloud) | "Approx. 110,000" | Leak confirmed | contractor / third-party service | none | [notice](https://www.medianavi.co.jp/info/info_20261030.html) |
| 259 | 2026-10-30 | World Co. (subsidiary Tin Pan Alley) | "Approx. 1.2 million records (cumulative)" | Possible outflow | unauthorised access (vector not disclosed) | none | [notice](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261030/20261030560364.pdf) |
| 260 | 2026-10-30 | Mie Prefecture (relocation seminar applicants, via Sankei Living Shimbun / Uyumi Link) | "156 persons (cumulative)" | Possible outflow | contractor / third-party service | none | [notice](https://www.pref.mie.lg.jp/TOPICS/m0346800028.htm) |
| 261 | 2026-10-30 | Ryobi Systems (health-checkup booking system AITEL) | "778 records" (5 across 3 organisations, 773 in 1) | Leaked or possibly leaked | unauthorised login | none | [notice](https://www.ryobi.co.jp/news/2026/202061030) |
| 262 | 2026-10-30 | Saitama Prefecture (mail to senior-employment pledge companies, via contractor / Rakus Lite Cloud) | "Approx. 2,900 companies" | Possible leak cannot be ruled out | contractor / third-party service | none | [notice](https://www.pref.saitama.lg.jp/a0816/news/page/news2026103001.html) |
| 263 | 2026-10-30 | Ministry of Foreign Affairs (externally connected network) | "Approx. 3,600 (of which approx. 900 belong to non-MOFA persons)" | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.mofa.go.jp/mofaj/press/release/pressit_000001_04395.html) |
| 264 | 2026-10-30 | Yamanashi Prefecture (Mt Fuji Yoshida trail booking system, via Japanticket) | "Approx. 70,000" (Japanticket total: max. approx. 264,000) | Leak confirmed (Japanticket-wide) | contractor / third-party service | none | [notice](https://www.pref.yamanashi.jp/fujisan/261030.html) |
| 265 | 2026-10-30 | Iwate Prefectural University (ANPIC safety-confirmation system, via Avance System) | "Approx. 5,300" | Possible leak | contractor / third-party service | none | [notice](https://www.iwate-pu.ac.jp/storage/website/2602-ad722587d7281f8ecf7f41df7db6c0be/page/hd-f5790ee1-cc0c-4e89-b748-39e521cb65f9/081030_ANPIC.pdf) |
| 266 | 2026-10-30 | Federation of Pharmaceutical Manufacturers' Associations of Japan, JPMA, Tokyo and Kansai pharmaceutical associations (PRAISE-NET mailing, via Uyumi Link) | "30,750 email addresses (as of 29 Oct 2026)" | Possible leak (reported by contractor) | contractor / third-party service | none | [notice](https://www.jpma.or.jp/news_room/release/2026/261030.html) |
| 267 | 2026-10-30 | Chuo City, Tokyo ("Chuo Oshigoto WEB" inquiry form, via HRP / Studio) | "14" | Possible outflow | contractor / third-party service | none | [notice](https://www.city.chuo.lg.jp/a0016/shigoto/koyouroudou/mensetsukai/shuuroukoyoushienhuseiakusesu.html) |
| 268 | 2026-10-30 | TEPCO Holdings (hired-car users, via Nihon Kotsu) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.tepco.co.jp/press/news/2026/pdf/261030j0101.pdf) |
| 269 | 2026-10-30 | Tokyu Land (GREEN CROSS PARK and GREENUP Cooldown Project websites) | "4,079" and "3" records | Possible outflow | multiple vectors | none | [notice](https://www.tokyu-land.co.jp/news/uploads/4e81382e895fcd779559705843fcb56f83846c28.pdf) |
| 270 | 2026-10-30 | Tokyu Land (website inquiry forms, via Studio) | Not stated | Possible outflow | contractor / third-party service | none | [notice](https://www.tokyu-land.co.jp/news/2026/001809.html) |
| 271 | 2026-10-30 | Matsuya Foods Holdings (Matsuya official app / admin system) | Matsuya official-app members "2,000 records (possibly up to 3,000)"; Matsuben Net / mobile order / Matsuben Delivery users "2,377,127 records" | Leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261030/20261030561172.pdf) |
| 272 | 2026-10-30 | Okinawa Prefecture (MICE newsletter, via OCVB / Rakus Lite Cloud) | "8,152 records" | Possible leak | contractor / third-party service | none | [notice](https://www.pref.okinawa.lg.jp/bunkakoryu/sport/1009786/1041818.html) |
| 273 | 2026-10-30 | Okinawa Prefecture (Nakagusuku Park / Prefectural Forest campsite booking via "Nap", R.project / Rakus Lite Cloud) | Not stated | Outflow confirmed | contractor / third-party service | none | [notice](https://www.pref.okinawa.lg.jp/machizukuri/park/1041826.html) |
| 274 | 2026-10-30 | Atami City Tourism Association (website inquiries, via site maintainer Travelzip) | "966 records" | Outflow confirmed | contractor / third-party service | none | [notice](https://www.ataminews.gr.jp/notices/471) |
| 275 | 2026-10-30 | Ryohin Keikaku (MUJI app) | "Max. approx. 27.26 million records (including withdrawn customers)" | Possible outflow; no dark-web exposure or misuse confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.ryohin-keikaku.jp/news/articles/2026_1030_01) |
| 276 | 2026-10-30 | Nishinihon Mitsubishi Motor Sales (Microsoft 365 email) | Not stated | Possible outflow | unauthorised login | none | [notice](https://west-mitsubishi-motor-sales.com/news/p=112040) |
| 277 | 2026-10-30 | e+ (eplus) (admin system of 'FES app') | "3,571 records" | Leak confirmed | unauthorised login | none | [notice](https://corp.eplus.jp/press-release/1835/) |
| 278 | 2026-10-31 | NTT DATA (bond-holder perk service, via contractor SaaS) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.nttdata.com/global/ja/news/release/2026/103101/) |
| 279 | 2026-10-31 | Kagome (1st unsecured bond digital perk, via NTT DATA's contractor) | "109 of 5,472 customers" | Possible leak | contractor / third-party service | none | [notice](https://www.kagome.co.jp/s3-contents/notification/20261031054555.pdf) |
| 280 | 2026-10-31 | Club Tourism (internet members) | "Approx. 4.32 million records" | Possible outflow | unauthorised access (vector not disclosed) | none | [notice](https://www.club-tourism.co.jp/jpn/news/2026/1031/) |
| 281 | 2026-10-31 | Credit Saison (real-estate security-token member platform, via external contractor) | "1,889 persons with confirmed leak" (39 + 1,850) | Leak reported | contractor / third-party service | none | [notice](https://www.saisoncard.co.jp/customer-support/information/20261031/) |
| 282 | 2026-10-31 | Starts Securities (real-estate security tokens, via Securitize) | Not stated | Leak concern | contractor / third-party service | none | [notice](https://www.starts-sc.com/info/20261031.html) |
| 283 | 2026-11-02 | Phillip Capital Securities Japan (digital securities, via external contractor) | 162 customers who made purchases; names and transaction quantities | Leak confirmed | contractor / third-party service | none | [notice](https://www.phillip.co.jp/information/news/11486) |
| 284 | 2026-10-31 | Lifecard (V-Preca prepaid card, via contractor) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://vpc.lifecard.co.jp/news/2026/detail/important-notice2.html) |
| 285 | 2026-10-31 | Mitsubishi UFJ Morgan Stanley Securities (Kintetsu bond buyers, via NTT DATA's contractor) | "95 customers" | Possible leak | contractor / third-party service | none | [notice](https://www.sc.mufg.jp/company/news/inform/info20261031.html) |
| 286 | 2026-10-31 | Rakuten Securities (digital-perk bonds, via NTT DATA's contractor) | "362 records (cumulative)" | Possible leak | contractor / third-party service | none | [notice](https://www.rakuten-sec.co.jp/web/info/info20261031-01.html) |
| 287 | 2026-10-31 | Kintetsu Group Holdings (135th unsecured bond digital-perk service, via NTT DATA) | "2,678 records" | Possible leak (reported) | contractor / third-party service | none | [notice](https://files.microcms-assets.io/assets/b5bb8ced8fa1487390ad071605410061/3d5fea5cb2814f86a6e7f89d5aec14a0/20261031hd.pdf) |
| 288 | 2026-10-31 | Nomura Securities (digital-perk bonds, via NTT DATA's contractor) | Not stated | Possible leak (reported) | contractor / third-party service | none | [notice](https://www.nomuraholdings.com/jp/news/topics/20261031.html) |
| 289 | 2026-11-02 | Nojima (Nojima Online member management system) | "Approx. 7 million records" (excluding withdrawn members) | Leak to outside parties confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.nojima.co.jp/wp-content/uploads/2026/11/fa47750556e505f2ddb83dc080a6420f.pdf) |
| 290 | 2026-11-02 | Prestige International (group business system) | "Max. approx. 5.5 million records" (incl. duplicates) | Exfiltrated | unauthorised access (vector not disclosed) | none | [notice](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261102/20261102563007.pdf) |
| 291 | 2026-11-02 | Zaif Inc. (crypto exchange, via contractor Arara) | Not stated | Possible exfiltration; whether users' addresses are included is under investigation | contractor / third-party service | none | [notice](https://corp.zaif.jp/info/20261102-1) |
| 292 | 2026-11-02 | istyle (@cosme, @cosme common ID) | "Approx. 3 million persons" | Leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.istyle.co.jp/news/info/2026/11/1102.html) |
| 293 | 2026-11-02 | Life Corporation (Life official app) | "298 records" | Possibly viewed / possible leak | unauthorised login | none | [notice](https://www.lifecorp.jp/vc-files/pdf/newsrelease/others/20261102-1.pdf) |
| 294 | 2026-11-02 | Marui Group (digital bond administration, via contractor Securitize Japan) | "Max. 9,086 persons" (of whom 54 possibly including bank account numbers) | Partial leak confirmed | contractor / third-party service | none | [notice](https://www.0101maruigroup.co.jp/nr/o-20-0zfdye) |
| 295 | 2026-11-02 | Hokuriku Electric Power (Hokulink member service, via contractor's email delivery service) | "Approx. 550,000" member email addresses | Exfiltration confirmed | contractor / third-party service | none | [notice](https://www.rikuden.co.jp/press/attach/26110201.pdf) |
| 296 | 2026-11-02 | Osaka Gas (FitDish meal-kit subscription, via contractor Arara) | "34,489 records" | Exfiltration confirmed | contractor / third-party service | none | [notice](https://www.osakagas.co.jp/company/press/pr2026/1828107_60967.html) |
| 297 | 2026-11-02 | Himeji City (online procedures portal, via contractor TKC and Arara) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.city.himeji.lg.jp/shisei/0000034645.html) |
| 298 | 2026-11-02 | Kobe Shimbun (newsletter, via Arara) | "Approx. 40,000" (email addresses only) | Leak notified by contractor | contractor / third-party service | none | [notice](https://www.kobe-np.co.jp/news/information/202611/0020994385.shtml) |
| 299 | 2026-11-02 | Kintetsu Miyako Hotels International (Miyako Plus member emails, via contractor using Arara) | "129,153" email addresses | Leak confirmed | contractor / third-party service | none | [notice](https://www.miyakohotels.ne.jp/topic/information/238/) |
| 300 | 2026-11-02 | Shizuoka City Children's Creative Town Maaru (mailing, via Blastmail) | Not stated | Possible leak; no leak confirmed | contractor / third-party service | none | [notice](https://maaru-ct.jp/news/270383/) |

(Added 8 November 2026)  
207 rows were added: 14 from the pending list, 184 disclosed 3–7 November 2026, and 9 disclosed 8 October – 2 November that the fourth edition had missed. Earlier tables are unchanged; together the five tables match the 507 rows of `data/registry.json`. IDs follow the order of publication date; order within a date carries no meaning.

Three of the nine missed cases (303 Okazaki, 305 Yanai, 309 Funabashi) belong to the Arcadia "SpeeCAN RAIDEN" / "NET119" chain disclosed 14–21 October, which the fourth edition's candidate search had not picked up at all. Arcadia's own notice is pending.

As in the third and fourth editions, candidates were found and drafted by AI agents using web search and retrieval of each notice, with the period split across several agents and the results merged. Admission rests, as before, on the author opening and reading each row's `primary_url`; any row not so verified is moved back to pending before the commit. Rows whose page carries no date (date inferred from URL or secondary sources), whose counts appear only in an image, or whose notice sits on the organisation's blog are marked "unverified" or "author's judgement" in the notes. On 8 November a separate AI agent that had not seen the drafting re-fetched the `primary_url` of 30 of the 207 new rows (the 16 largest and 14 at random) and compared scale and unit, status wording, vector, AI mention and date against the notice: 23 matched; 4 were corrected (318 Suntory: the unit 「名」 missing from the breakdown; 345 Workman and 476 Ehime Bank: status wording not verbatim; 365 Plenus: the notice's 「流出した」 not reflected in the status); 3 received a note only (364, 476, 477: notices say "partner" or "guarantee company" without the word 「委託」 and are classified as contractor rows). The other 177 rows have not been through this re-check.

### The 207 rows added on 8 November 2026

| ID | Published | Organisation | Scale (as stated, original unit) | Status | Vector | AI mentioned | Primary source |
|---|---|---|---|---|---|---|---|
| 301 | 2026-10-08 | Open Smile Inc. (point site Warau) | not stated (affected members contacted individually) | obtained (Yahoo! JAPAN ID link tokens) / possibly obtained (registration data etc.) | vulnerability | none | [notice](https://www.opensmile.co.jp/corp/news/note/20261015) |
| 302 | 2026-10-09 | Ajinomoto Co., Inc. (Ajinomo-Talk community; vendor Commune) | not stated | customers whose data may have leaked to be contacted individually | contractor / third-party service | none | [notice](https://park.ajinomoto.co.jp/) |
| 303 | 2026-10-14 | Okazaki City (disaster emergency e-mail, school information e-mail, fire dispatch e-mail; contractor Arcadia "SpeeCAN RAIDEN") | About 37,000 records; guardians of about 30,000 students; about 2,400 records | Possible leak | contractor / third-party service | none | [notice](https://www.city.okazaki.lg.jp/shisei/koho/1006195/1017450.html) |
| 304 | 2026-10-15 | BK Japan (Burger King official app) | approx. 11.18 million official-app member records | leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.burgerking.co.jp/images/notice/2026/10/15/d4d114ca-ebd7-4f3d-94ef-c4ea7a84a139.pdf) |
| 305 | 2026-10-16 | Yanai City (disaster information delivery service "SpeeCAN RAIDEN" run by Arcadia) | 8,146 records possibly leaked | Possible leak | contractor / third-party service | none | [notice](https://www.city-yanai.jp/soshiki/6/bousaimailoshirase.html) |
| 306 | 2026-10-17 | MBC Kaihatsu Co., Ltd. (Digital Day 2026 in Kagoshima DAY2 site; vendor Studio) | 5 records | possible leak identified | contractor / third-party service | none | [notice](https://mbckh.com/%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E3%82%88%E3%82%8B%E6%83%85%E5%A0%B1%E6%BC%8F%E6%B4%A9%E3%81%AE%E5%8F%AF%E8%83%BD%E6%80%A7%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%8A/) |
| 307 | 2026-10-20 | NTTPC Communications (email delivery via Yumirlink Cuenote FC) | 60,929 records (3rd report, 2026-11-02); not stated in first report | possible leak (1st) → confirmed included in leak (3rd) | contractor / third-party service | none | [notice](https://www.nttpc.co.jp/press/info/2026/10/202610201600.html) |
| 308 | 2026-10-20 | Anchor Network Service Co., Ltd. (EC sites; vendor Wasabi WASABI SWITCH) | 1,011 order records (Rakuten 617, Yahoo! Shopping 279, Shopify 102, Rakuma 12, Qoo10 1) | possible | contractor / third-party service | none | [notice](https://www.anchor-net.co.jp/news/2026/10/3027/) |
| 309 | 2026-10-21 | Funabashi City (Fire Department "NET119" emergency call system; operator Arcadia) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.city.funabashi.lg.jp/emergency/news/attention1/p150975.html) |
| 310 | 2026-10-22 | Kagoshima City (Industry Creation Division; email delivery via Rakus Light Cloud Blastmail) | approx. 4,300 persons cumulative (2nd report; 1st report approx. 500), at risk and under review by the provider | risk / concern of leak | contractor / third-party service | none | [notice](https://www.city.kagoshima.lg.jp/san-sousyutu/shisetsu/sangyo/san-sou-oshirase20261026.html) |
| 311 | 2026-10-22 | KOMOJU Co., Ltd. (formerly DEGICA; payment service KOMOJU; CRM system) | not stated on the pages read | leak confirmed with personal information included (2nd report); possible (1st) | unauthorised access (vector not disclosed) | none | [notice](https://ja.komoju.com/news/1026-notice/) |
| 312 | 2026-10-22 | Okazaki City (crime-prevention e-mail newsletter and public-housing e-mail service; contractor Rakus Light Cloud "blastmail") | About 26,000 email addresses (crime-prevention newsletter); public-housing service count under confirmation | Possible leak | contractor / third-party service | none | [notice](https://www.city.okazaki.lg.jp/shisei/koho/1006195/1006358/1016621/1017457.html) |
| 313 | 2026-10-23 | Creema Ltd. (newsletter via Rakus Light Cloud Blastmail) | not stated (some customers) | leak confirmed (per vendor report) | contractor / third-party service | none | [notice](https://www.creema.jp/news/1567/detail) |
| 314 | 2026-10-26 | StarX Co., Ltd. (data analytics tool "Metabase" used by logistics system "CloudLogi") | Not stated | Possible leak of personal data; API key leak confirmed | unauthorised access (vector not disclosed) | none | [notice](https://starx.co.jp/news/1040.html) |
| 315 | 2026-10-27 | Impress Corporation (DIGITAL X News newsletter; external delivery system) | not stated on the page read | part of the information was leaked | contractor / third-party service | none | [notice](https://dcross.impress.co.jp/docs/about/004916.html) |
| 316 | 2026-10-31 | Ryokuwado Inc. (EC site; vendor Wasabi WASABI SWITCH) | up to 351 persons | leak confirmed | contractor / third-party service | none | [notice](https://www.ryokuwado.com/96780/) |
| 317 | 2026-10-31 | West Japan Railway Company (investor data for the 80th unsecured bond; NTT DATA digital securities platform) | 2 investor records | possible leak | contractor / third-party service | none | [notice](https://www.westjr.co.jp/press/article/2026/10/31/items/261031_00_press_gaibuservice.pdf) |
| 318 | 2026-11-02 | Suntory Holdings / Suntory Beverage & Food (external cloud service used by the group) | (1) approx. 90,000 (names/emails), (2) 7,323, (3) 7,173, (4) 1,097, (5) 324, (6) 96, (7) 25 (as of 2026-11-01; investigation ongoing) | leak; personal information confirmed in downloaded files | contractor / third-party service | none | [notice](https://www.suntory.co.jp/note/detail/261102_008203.html) |
| 319 | 2026-11-02 | WILLs Inc. (point exchange service Netmile) | up to approx. 5.49 million persons (including withdrawn members) | possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www2.jpx.co.jp/disc/44820/140120261102562660.pdf) |
| 320 | 2026-11-02 | TKC Corporation (mail delivery vendor Arara for municipal online application / My Number Card reservation systems) | up to 2,230,812 email addresses (3rd report, Nov 4) | possible leak (1st report); only email addresses leaked (3rd report) | contractor / third-party service | none | [notice](https://www.tkc.jp/news/2026/20261102_1/) |
| 321 | 2026-11-02 | LIFULL Co., Ltd. (LIFULL Investment real-estate crowdfunding; contractor Securitize Japan) | Up to 238 customers | Confirmed | contractor / third-party service | none | [notice](https://lifull.com/news/50881/) |
| 322 | 2026-11-02 | Pan Pacific International Holdings Corporation (digital bond management system; contractor Securitize Japan) | Not stated | Unauthorized access confirmed; leak under investigation | contractor / third-party service | none | [notice](https://ppih.co.jp/news/pdf/4e630f1d37e8a69c0c33fa66a61c74ee.pdf) |
| 323 | 2026-11-02 | Rims Capital (real-estate crowdfunding "BATSUNAGU"; platform provider Securitize "Securitize PF") | Not stated | Leak (title); third-party access to part of customer data "has been found" (判明) | contractor / third-party service | none | [notice](https://batsunagu-funding.com/%E3%80%90%E9%87%8D%E8%A6%81%E3%80%91%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E3%82%88%E3%82%8B%E5%80%8B%E4%BA%BA%E6%83%85%E5%A0%B1%E6%B5%81%E5%87%BA%E3%81%AE%E5%8F%AF%E8%83%BD/) |
| 324 | 2026-11-03 | Seijo Ishii (seijoishii.com mail magazine; vendor Arara 'arara message') | up to 168,630 (email addresses) | confirmed leak (count 'up to', vendor investigating) | contractor / third-party service | none | [notice](https://seijoishii.com/pages/information_202611) |
| 325 | 2026-11-03 | St.Cousair (mail magazine; vendor Arara 'arara message') | 878,343 email addresses | confirmed (email addresses); other items being checked | contractor / third-party service | none | [notice](https://www.stcousair.co.jp/company/news/36892) |
| 326 | 2026-11-03 | Belc (Belclub mail magazine / Otodoke Pack; vendor Arara) | 786,739 email addresses; 2,352 customer names | confirmed leak; investigation continuing | contractor / third-party service | none | [notice](https://www.belc.jp/news/20261029) |
| 327 | 2026-11-03 | Camel Coffee (KALDI Coffee Farm online store mail magazine; vendor Arara) | 820,420 (email addresses) | possible leak | contractor / third-party service | none | [notice](https://camelcoffee.jp/news/important/2026/002221.html) |
| 328 | 2026-11-03 | Seven-Eleven Japan (7NOW delivery; contractor CBcloud 'PickGo') | 164,180 (kana name only); 4,762 (kana name + address); 209 (kana name, address, phone, postal code) | confirmed (acquired by third party) | contractor / third-party service | none | [notice](https://www.sej.co.jp/company/important/185116.html) |
| 329 | 2026-11-03 | Demae-can (delivery contractor CBcloud 'PickGo') | 799 names; 794 addresses; 33 phone numbers/postal codes | possible leak (heading) / confirmed acquisition per CBcloud | contractor / third-party service | none | [notice](https://corporate.demae-can.co.jp/pr/info/20261103.html) |
| 330 | 2026-11-03 | Ekitan (train information emails; vendor Arara 'arara message') | not stated | leak reported by vendor; scope being confirmed | contractor / third-party service | none | [notice](https://ekitan.co.jp/corp/news/20261103-01/) |
| 331 | 2026-11-03 | Okayama Prefecture (medical safety / infectious disease mail magazines; Arara) | not stated (count under vendor investigation) | leak reported by vendor | contractor / third-party service | none | [notice](https://www.pref.okayama.jp/page/detail-26532.html) |
| 332 | 2026-11-03 | The Yokohama Rubber Co. (news release / news mail distribution; vendor Arara) | not stated | leak notified by vendor | contractor / third-party service | none | [notice](https://www.y-yokohama.com/release/?id=4909&lang=ja) |
| 333 | 2026-11-03 | GOLF NETWORK PLUS (mail magazine tool; Arara 'repica') | 209,460 total (may include duplicates) | confirmed | contractor / third-party service | none | [notice](https://tv.golfnetwork.co.jp/news/detail/147) |
| 334 | 2026-11-03 | Jyoseikan (guidance emails; Arara mail service used by contractor) | 34,063 email addresses | leak identified | contractor / third-party service | none | [notice](https://www.jyoseikan.co.jp/info/infosec261103/) |
| 335 | 2026-11-03 | AKASE GROUP / Masterwal (mail service 'repica'; Arara) | 52,735 (email address records; not number of customers) | leak; verification ongoing | contractor / third-party service | none | [notice](https://www.masterwal.jp/news/list/0/detail/2411) |
| 336 | 2026-11-03 | Natural Science / Natural Island (online shop email addresses; vendor Arara 'repica') | not stated | leak identified | contractor / third-party service | none | [notice](https://www.natural-s.jp/info/update/20261103.html) |
| 337 | 2026-11-03 | City of Yokohama (e-application system mail sending service; via contractor) | not stated | possible leak; being confirmed | contractor / third-party service | none | [notice](https://www.city.yokohama.lg.jp/city-info/koho-kocho/press/somu/2026/1103denshishinsei.html) |
| 338 | 2026-11-03 | Otsu City (My Number Card pickup reservation system emails; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.otsu.lg.jp/d_news/77544.html) |
| 339 | 2026-11-03 | Niigata City (e-NIIGATA online application system external mail service; TKC / Arara) | not stated | possible leak; under investigation | contractor / third-party service | none | [notice](https://www.city.niigata.lg.jp/shisei/seisaku/it/keikaku/e-niigata-info202611.html) |
| 340 | 2026-11-03 | Shimotsuke City (Shimotsuke Online Service external mail service; TKC / Arara) | not stated | possible leak; no confirmed leak of city users yet | contractor / third-party service | none | [notice](https://www.city.shimotsuke.lg.jp/0017/info-0000010791-3.html) |
| 341 | 2026-11-03 | Takanezawa Town (My Number Card reservation external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.town.takanezawa.tochigi.jp/information/2026-1103-0845-77.html) |
| 342 | 2026-11-03 | Toyohashi City (My Number Card reservation confirmation mail server; TKC / Arara) | not stated | leak notified by provider; city impact being confirmed | contractor / third-party service | none | [notice](https://www.city.toyohashi.lg.jp/item/126526.htm) |
| 343 | 2026-11-03 | Fujinomiya City (My Number Card reservation system external mail service; TKC / Arara) | not stated for the city (TKC-wide up to 2,230,812 email addresses) | leak announced by provider; city-specific impact unknown | contractor / third-party service | none | [notice](https://www.city.fujinomiya.lg.jp/1023200000/p004072.html) |
| 344 | 2026-11-03 | Denny's Japan (Denny's app; old-to-new app migration process) | not stated | possible leak; under investigation | unauthorised login | none | [notice](https://www.dennys.co.jp/dennys-japan/pdf/261103.pdf) |
| 345 | 2026-11-04 | Workman (online store mail magazine members; vendor Arara) | up to about 1.45 million (email addresses) | leak reported by vendor; 'up to' | contractor / third-party service | none | [notice](https://www.workman.co.jp/wp-content/uploads/2026/11/1104.pdf) |
| 346 | 2026-11-04 | Internet Initiative Japan (IIJmio customer emails; vendor Arara) | 983,458 (including cancelled services) | leak identified; attribute details being confirmed | contractor / third-party service | none | [notice](https://www.iij.ad.jp/news/information/2026/1104.html) |
| 347 | 2026-11-04 | Duskin (DDuet member site emails; vendor Arara 'repica') | 657,886 (DDuet member email addresses) | confirmed leak | contractor / third-party service | none | [notice](https://www.duskin.co.jp/news/2026/pdf/261104_01.pdf) |
| 348 | 2026-11-04 | MOS Food Services (MOS WEB members emails; vendor Arara) | 7,517,087 email addresses | leak identified | contractor / third-party service | none | [notice](https://www.mos.jp/topics/20261104_2/) |
| 349 | 2026-11-04 | Chobirich (point site member emails; vendor Arara 'arara message') | 1,348,525 email addresses (not member count) | email addresses acquired (reported); other items possible | contractor / third-party service | none | [notice](https://chobirich.co.jp/1sgvii4gv9/) |
| 350 | 2026-11-04 | Ministry of Internal Affairs and Communications (English newsletter; contractor Arara) | 775 email addresses; 21 names | leak reported | contractor / third-party service | none | [notice](https://www.soumu.go.jp/menu_news/s-news/01tsushin06_02000364.html) |
| 351 | 2026-11-04 | Sumitomo Realty & Development (property inquiry emails; contractor DataX / Arara) | 205,208 (email addresses) | leak; no misuse confirmed | contractor / third-party service | none | [notice](https://www.sumitomo-rd.co.jp/uploads/20261104_release.pdf) |
| 352 | 2026-11-04 | Monteroza (mail magazine members; vendor Arara) | 625,429 (email addresses), of which 31,333 include optional attributes | possible leak | contractor / third-party service | none | [notice](https://www.monteroza.co.jp/wp-content/uploads/2026/11/news261104mm.pdf) |
| 353 | 2026-11-04 | Solaseed Air (reservation emails; contractor's mail delivery service) | about 490,000 (email addresses) | possible exfiltration / leak | contractor / third-party service | none | [notice](https://www.solaseedair.jp/info/2026/11/post-20260912.html) |
| 354 | 2026-11-04 | Kyushu Railway Company (JR Kyushu; condominium newsletter via contractor using Arara) | up to about 13,000 | possible leak | contractor / third-party service | none | [notice](https://www.jrkyushu.co.jp/common/inc/news/newtopics/__icsFiles/afieldfile/2026/11/04/20261104_info_data_breach.pdf) |
| 355 | 2026-11-04 | Axel Entermedia (fan club site emails; vendor Arara) | 1,086,098 (customers' email addresses) | leak; other items under investigation | contractor / third-party service | none | [notice](https://www.axelentermedia.co.jp/notice_20261104.html) |
| 356 | 2026-11-04 | Japan Digital Laboratory (JDL; mail delivery vendor Arara) | 28,921 records | possible leak | contractor / third-party service | none | [notice](https://www.jdl.co.jp/info/security-info202611.html) |
| 357 | 2026-11-04 | Kracie (Kampoful Life member emails; vendor Arara 'repica') | 59,428 (email addresses) | leak identified | contractor / third-party service | none | [notice](https://www.kracie.co.jp/release/10193700_3833.html) |
| 358 | 2026-11-04 | BOAT RACE Promotion Association (Teleboat newsletters via Nihon Leisure Channel / Arara) | up to 684,772 (email addresses) | leak; 'up to'; investigation continuing | contractor / third-party service | none | [notice](https://www.boatrace-pr.jp/pc/site/release/2026/11/11924/) |
| 359 | 2026-11-04 | Shippio (Shippio Platform; via internal business tool) | all customers' company info viewed; about 1,300 document files downloaded; about 1,100 teams affected | confirmed leak; some items under investigation | unauthorised login | none | [notice](https://www.shippio.io/news/20261104/) |
| 360 | 2026-11-04 | Uchicomi (real estate site 'Uchicomi!' server; ransomware) | 142,591 accounts | possible leak | unauthorised access (vector not disclosed) | none | [notice](https://uchicomi.co.jp/news/647) |
| 361 | 2026-11-04 | NAVC (hotel reservation system 'RESERVE GATE α') | up to about 350,000 (all RGα member records) | leak identified; count 'possible, up to' | vulnerability | none | [notice](https://navc2.co.jp/news_detail.php?id=44) |
| 362 | 2026-11-04 | OSIRO (community platform 'OSIRO' member data) | up to 12,661 people (1,101 may have had real names shown) | leak; 'up to'; possible | misconfiguration | none | [notice](https://osiro.it/news/14624) |
| 363 | 2026-11-04 | Gains (Getchu.com membership management system) | not stated | leak identified; items 'possible' | unauthorised access (vector not disclosed) | none | [notice](https://www.getchu.com/getchu/news20261104.html) |
| 364 | 2026-11-04 | Credit Saison (MUJI Card member data; unauthorized access to Ryohin Keikaku systems) | about 1.09 million (about 345,000 active cards; about 745,000 inactive) | possible leak | contractor / third-party service | none | [notice](https://www.saisoncard.co.jp/customer-support/information/20261104/) |
| 365 | 2026-11-04 | Plenus (Hotto Motto mail magazine; outsourced mail delivery service) | up to about 7 million (member records) | Leak reported by the contractor | contractor / third-party service | none | [notice](https://www.plenus.co.jp/files/optionallink/00003434_file.pdf) |
| 366 | 2026-11-04 | Dentsu Soken (cloud service FACERE, one client company's environment) | not stated | possible leak | misconfiguration | none | [notice](https://www.dentsusoken.com/news/topics/2026/1104_1.html) |
| 367 | 2026-11-04 | Yuzawa City (survey contractor Shibata Koji Chosa; ransomware) | 2,256 cumulative records (as of Nov 4, 2026 report) | possible leak | contractor / third-party service | none | [notice](https://www.city-yuzawa.jp/soshiki/14/6597.html) |
| 368 | 2026-11-04 | Nomura Investor Relations (IR information service 'Kikan Navi') | not stated | leak; items possible; under investigation | unauthorised access (vector not disclosed) | none | [notice](https://www.nomura-ir.co.jp/ja/news/news/news20261104/main/00/link/20261104.pdf) |
| 369 | 2026-11-04 | Tokyo Islands Towns and Villages Partial Affairs Association (Tosho Kaikan reservation system; vendor NAVC 'RESERVE GATE α') | 3,021 (per Nov 5 notice; initially under investigation) | possible leak (Nov 4) / leak reported by vendor (Nov 5) | contractor / third-party service | none | [notice](https://www.tosho-kaikan.jp/information_notice.pdf) |
| 370 | 2026-11-04 | Osaka Corona Hotel (direct website booking members; vendor NAVC 'RESERVE GATE α') | not stated | high possibility of leak | contractor / third-party service | none | [notice](https://www.osakacoronahotel.jp/topics/2026/122103/) |
| 371 | 2026-11-04 | JA Kyosai (National Mutual Insurance Federation of Agricultural Cooperatives; roadside service contractor Prestige Core Solution) | not stated | possible leak (first report) | contractor / third-party service | none | [notice](https://www.ja-kyosai.or.jp/info/2026/20261104-2.html) |
| 372 | 2026-11-04 | Hasegawa (Buddhist altar retailer; mail delivery vendor Arara 'repica') | 305 (email addresses) | leak identified (first report) | contractor / third-party service | none | [notice](https://www.hasegawa.jp/blogs/news/261104s1) |
| 373 | 2026-11-04 | Maker's Shirt Kamakura (mail magazine; vendor Arara 'repica') | about 160,000 email addresses | confirmed leak; items 'possible' | contractor / third-party service | none | [notice](https://yomukama.shirt.co.jp/5374) |
| 374 | 2026-11-04 | Takii Seed (Takii Net Shop mail magazine; Arara mail delivery system) | 103,986 (email addresses) | confirmed leak | contractor / third-party service | none | [notice](https://shop.takii.co.jp/news/129) |
| 375 | 2026-11-04 | Kotsu Shimbunsha (media letter / mail magazine; vendor Arara 'repica') | 8,817 (email addresses) | leak identified | contractor / third-party service | none | [notice](https://www.kotsu.co.jp/information/2026/post_58.html) |
| 376 | 2026-11-04 | Toho Cash and Carry (A-Price Online Shop member emails; Arara 'repica') | 15,497 e-mail addresses (company PDF notice) | leak identified | contractor / third-party service | none | [notice](https://tcc.to-ho.co.jp/news/news_r081104.html) |
| 377 | 2026-11-04 | Hida Shinkumi (Sarubobo Coin; maintenance vendor Finnovalley using Arara 'arara message') | not stated | leak notified; other items being confirmed | contractor / third-party service | none | [notice](https://www.hidashin.co.jp/storage/001/202611/261104_news.pdf) |
| 378 | 2026-11-04 | Kimitsu Shinkumi / Kisarazu City / Kisarazu CCI (Aqua Coin; vendor Finnovalley, sub-vendor Arara) | not stated | possible leak; being confirmed | contractor / third-party service | none | [notice](https://www.kisarazu-aquacoin.com/information/20261104mailincident/) |
| 379 | 2026-11-04 | Japan Leisure Channel (Teleboat / boat race venue newsletters; vendor Arara 'arara message') | 684,772 (email addresses) | leak (email addresses only) | contractor / third-party service | none | [notice](https://www.jlc.ne.jp/2026/11/4818/) |
| 380 | 2026-11-04 | Shiftworks (job site mail delivery; Arara) | 280,596 (per Nov 5 update; initially up to 461,437 per secondary source) | leak; details being confirmed | contractor / third-party service | none | [notice](https://sftworks.jp/notice/info_20261104.html) |
| 381 | 2026-11-04 | Granvista Hotels & Resorts (Granvillage member mail magazine; vendor Arara) | 88,684 (email addresses) | leak; details being confirmed | contractor / third-party service | none | [notice](https://www.granvista.co.jp/news/detail/1424) |
| 382 | 2026-11-04 | Tokyo Soir (online store email addresses; vendor Arara 'repica') | 19,082 (email addresses) | leak identified | contractor / third-party service | none | [notice](https://www.soir.co.jp/news/30497/) |
| 383 | 2026-11-04 | Medica Publishing (bulk marketing emails; Arara 'repica' linked to external marketing system) | not stated | leak (email addresses); count being confirmed | contractor / third-party service | none | [notice](https://www.medica.co.jp/news/information/3854/) |
| 384 | 2026-11-04 | ILL Inc. (seminar/exhibition emails; DataX service using Arara 'repica') | 42,285 email addresses | leak identified | contractor / third-party service | none | [notice](https://www.ill.co.jp/info/261104/) |
| 385 | 2026-11-04 | M Stage / M Stage Management Solutions (mail vendor's sub-vendor Arara 'repica') | 38,256 email addresses (two companies combined) | possible leak | contractor / third-party service | none | [notice](https://mstage-corp.jp/news/news-452/) |
| 386 | 2026-11-04 | JAVA Corporation (J Lounge online store / JAVA MEMBERS CLUB app emails; Arara 'repica') | 333,423 (email addresses) | leak confirmed (definitive report received) | contractor / third-party service | none | [notice](https://www.j-lounge.jp/blogs/information/info20261104) |
| 387 | 2026-11-04 | Nihon Fukushi University (newsletter and safety confirmation system; vendor Arara 'repica' / 'arara message') | 50,041 (newsletter) and 5,613 (safety confirmation system) email addresses; being confirmed | leak or possible leak | contractor / third-party service | none | [notice](https://www.n-fukushi.ac.jp/about/news/2026/11/04/d42f534ec77c81eebdf6bfc40ec400e88bf63a67.html) |
| 388 | 2026-11-04 | Infomart (BtoB Platform Invoice free-user emails; Arara 'arara message') | 3,577 email addresses | leak (first report) | contractor / third-party service | none | [notice](https://corp.infomart.co.jp/news/20261104_6211/) |
| 389 | 2026-11-04 | Boarderless (DOLK STATION emails; external service Arara 'repica') | 24,828 (email address records) | leak (as reported by vendor) | contractor / third-party service | none | [notice](https://dolk.jp/pages/special/notice_20261104/) |
| 390 | 2026-11-04 | The Shikoku Bank (contractor's mail delivery service) | not stated | leak identified | contractor / third-party service | none | [notice](https://www.shikokubank.co.jp/info/post_203.html) |
| 391 | 2026-11-04 | Yamanashi Prefecture (Mt. Fuji Yoshida Route reservation system; contractor Asoview / Arara) | up to 83,013 (FY2025) and up to 114,543 (FY2026) people; Asoview-wide 15,821,184 records | possible leak; 'up to'; under investigation | contractor / third-party service | none | [notice](https://www.pref.yamanashi.jp/fujisan/20261104/20261104tsuukouyoyakuryuusyutu.html) |
| 392 | 2026-11-04 | Matsue City (Asoview! ticketing for Matsue Castle etc.; Asoview / Arara) | not stated | leak reported | contractor / third-party service | none | [notice](https://www.city.matsue.lg.jp/soshikikarasagasu/matsueshiyakusho/oshirase_joho/26816.html) |
| 393 | 2026-11-04 | Itami City (mail magazine system and online application system; Arara mail service used by system providers) | not stated (registrant counts listed per service) | possible leak; being confirmed | contractor / third-party service | none | [notice](https://www.city.itami.lg.jp/oshirase/50668.html) |
| 394 | 2026-11-04 | Kashiwazaki City (mail delivery service via contractor; Arara) | 5,364 registered users (leaked count under investigation) | leak confirmed (title); details under investigation | contractor / third-party service | none | [notice](https://www.city.kashiwazaki.lg.jp/daijinaoshirase/50458.html) |
| 395 | 2026-11-04 | Boat Race Marugame (campaign prize notification emails via Japan Leisure Channel / Arara) | up to 759 (email addresses) | leak; 'up to' | contractor / third-party service | none | [notice](https://www.marugameboat.jp/asp/marugame/00info/info.php?type=4#184) |
| 396 | 2026-11-04 | Boat Race Biwako (official mail magazine via Japan Leisure Channel / Arara) | up to 1,917 (email addresses) | leak; 'up to' | contractor / third-party service | none | [notice](https://www.boatrace-biwako.jp/modules/news/?kind=1&storyid=2399) |
| 397 | 2026-11-04 | Isahaya City (My Number Card reservation system emails; TKC / Arara) | up to 21,383 (email addresses) | possible leak; 'up to' | contractor / third-party service | none | [notice](https://www.city.isahaya.nagasaki.jp/soshiki/42/51075.html) |
| 398 | 2026-11-04 | Miyazaki City (Smart Application System emails; provider Densan / system provider TKC / Arara) | not stated | possible leak; being confirmed | contractor / third-party service | none | [notice](https://www.city.miyazaki.miyazaki.jp/city/policy/administration/419100.html) |
| 399 | 2026-11-04 | Mibu Town (Smart Application System external mail service; TKC / Arara) | not stated | possible leak; no confirmed leak | contractor / third-party service | none | [notice](https://www.town.mibu.tochigi.jp/docs/2026110400033) |
| 400 | 2026-11-04 | Misato Town, Saitama (My Number Card reservation system; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.town.saitama-misato.lg.jp/0000002810.html) |
| 401 | 2026-11-04 | Kameyama City (My Number Card reservation system external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.kameyama.mie.jp/docs/2026110400033/) |
| 402 | 2026-11-04 | Itako City (My Number Card reservation system mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.itako.lg.jp/ku-te/mynumber-card/page009209.html) |
| 403 | 2026-11-04 | Sanjo City (e-application system mail service; TKC / Arara) | not stated | leak (title); whether leaked being confirmed | contractor / third-party service | none | [notice](https://www.city.sanjo.niigata.jp/soshiki/shimimbu/shimimmadoguchika/madoguchi/madoguchi/21317.html) |
| 404 | 2026-11-04 | Sakai City (e-application system; Arara mail service used by TKC) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.sakai.lg.jp/shisei/gyosei/it/20261104_denshishinsei.html) |
| 405 | 2026-11-04 | Yaita City (My Number Card reservation system mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.yaita.tochigi.jp/soshiki/simin/mynumberjoho.html) |
| 406 | 2026-11-04 | Miyoshi Town, Saitama (My Number Card reservation system mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.town.saitama-miyoshi.lg.jp/life/mynumber/huseiakusesu.html) |
| 407 | 2026-11-04 | Ryugasaki City (My Number Card reservation system mail service; TKC / Arara) | not stated for city (TKC-wide up to 2,230,812) | leak occurred at vendor; whether city users included being confirmed | contractor / third-party service | none | [notice](https://www.city.ryugasaki.ibaraki.jp/kurashi/todokede/tetsuduki/20261104132101909.html) |
| 408 | 2026-11-04 | Odawara City (My Number Card reservation system mail vendor; TKC / Arara) | not stated for city (TKC-wide up to about 2.23 million) | possible leak; city impact being confirmed | contractor / third-party service | none | [notice](https://www.city.odawara.kanagawa.jp/field/tax-resi/resident/mynumber/p43342.html) |
| 409 | 2026-11-04 | Yokoshibahikari Town (My Number Card reservation system external mail service; TKC / Arara) | not stated | possible leak; under investigation | contractor / third-party service | none | [notice](https://www.town.yokoshibahikari.chiba.jp/soshiki/7/29683.html) |
| 410 | 2026-11-04 | Oi Town, Kanagawa (My Number Card reservation system mail service; TKC / Arara) | not stated | possible leak; no confirmed leak | contractor / third-party service | none | [notice](https://www.town.oi.kanagawa.jp/soshiki/4/seisaku-oshirase20261104.html) |
| 411 | 2026-11-04 | Aya Town, Miyazaki (Smart Application System mail function; TKC / Arara) | not stated | possible leak; being confirmed | contractor / third-party service | none | [notice](https://www.town.aya.miyazaki.jp/soshiki/soumuka/11258.html) |
| 412 | 2026-11-04 | Hakone Town (Smart Application System tax consultation reservations; TKC / Arara) | not stated | possible leak; unknown | contractor / third-party service | none | [notice](https://www.town.hakone.kanagawa.jp/www/contents/1793778869713/index.html) |
| 413 | 2026-11-04 | Ashikaga City (online application system external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.ashikaga.tochigi.jp/goverment/000085/000477/p008876.html) |
| 414 | 2026-11-04 | Higashikurume City (My Number Card / e-certificate reservation external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.higashikurume.lg.jp/shisei/joho/1005146/1029998.html) |
| 415 | 2026-11-04 | Kaisei Town (My Number Card reservation management system external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.town.kaisei.kanagawa.jp/info/2770) |
| 416 | 2026-11-04 | Hanamaki City (My Number Card reservation system external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.hanamaki.iwate.jp/kurashi/todokede/mynumber/1026220.html) |
| 417 | 2026-11-04 | Kumagaya City (My Number Card reservation system mail vendor; TKC / Arara) | under investigation | possible leak | contractor / third-party service | none | [notice](https://www.city.kumagaya.lg.jp/kurashi/mynumber/mynumber-johoroei.html) |
| 418 | 2026-11-04 | Matsudo City (online application system user emails; TKC / Arara) | not stated (about 136,000 registered users) | possible leak; under investigation | contractor / third-party service | none | [notice](https://www.city.matsudo.chiba.jp/shisei/keikaku-kousou/digital/online-sinsei.html) |
| 419 | 2026-11-04 | Nakai Town (e-application and My Number Card reservation systems mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.town.nakai.kanagawa.jp/kinkyu/4071.html) |
| 420 | 2026-11-04 | Nishiwaki City (city mail delivery service and My Number Card reservation system; TKC / WingArc NEX / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.nishiwaki.lg.jp/jyuyo_oshirase/31654.html) |
| 421 | 2026-11-04 | Shioya Town (online application system external mail service; TKC / Arara) | under investigation | possible leak | contractor / third-party service | none | [notice](https://www.town.shioya.tochigi.jp/info/2883) |
| 422 | 2026-11-04 | Motegi Town (online application system external mail service; TKC / Arara) | 60 (registered users) | possible leak | contractor / third-party service | none | [notice](https://www.town.motegi.tochigi.jp/motegi/nextpage.php?cd=8711&syurui=2) |
| 423 | 2026-11-04 | Kasama City (My Number Card reservation management system external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.kasama.lg.jp/page/page017706.html) |
| 424 | 2026-11-04 | Ome City (My Number Card reservation system emails; TKC / Arara) | not stated | leak at vendor; city impact unknown | contractor / third-party service | none | [notice](https://www.city.ome.tokyo.jp/soshiki/13/127643.html) |
| 425 | 2026-11-04 | Naha City (online application system external mail service; TKC / Arara) | not stated (about 82,000 registered users) | possible leak | contractor / third-party service | none | [notice](https://www.city.naha.okinawa.jp/admin/kaikaku/1008233/1004100/1013242.html) |
| 426 | 2026-11-04 | Saito City (Smart Application System external mail service; Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.saito.lg.jp/info/post_202611041132) |
| 427 | 2026-11-04 | Achi Village (My Number Card reservation confirmation mail server; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.vill.achi.lg.jp/soshiki/3/huseiakusesu20261104.html) |
| 428 | 2026-11-05 | AIRDO (reservation/flight-status/My AIRDO emails; external mail delivery system) | up to 673,920 (email addresses) | leak reported; 'up to' | contractor / third-party service | none | [notice](https://www.airdo.jp/news/2026/news-10708.html) |
| 429 | 2026-11-05 | Sumitomo Mitsui Banking Corporation (some email delivery operations; vendor Arara 'arara message') | 227,216 email addresses | confirmed leak | contractor / third-party service | none | [notice](https://www.smbc.co.jp/news/pdf/j20261105_02.pdf) |
| 430 | 2026-11-05 | Matsui Securities (outsourced mail delivery service, Arara) | up to 830,000 (email addresses) | leak; 'up to' | contractor / third-party service | none | [notice](https://www.matsui.co.jp/company/press/pdf/pr261105.pdf) |
| 431 | 2026-11-05 | Mitsui Fudosan (&BIZ mail magazine addresses; Arara system used by contractor) | 133,323 (email addresses) | leak | contractor / third-party service | none | [notice](https://www.mitsuifudosan.co.jp/corporate/news/2026/1105/download/sonota/20261105.pdf) |
| 432 | 2026-11-05 | GMO Payment Service (law firm Martial Arts' use of Arara 'arara message') | up to 106,997 total (101,226 email-only; 5,771 with additional data) | leak; 'up to' | contractor / third-party service | none | [notice](https://www.gmo-ps.com/news/20261105/) |
| 433 | 2026-11-05 | Rakuten Securities (economic indicator alert emails; Minkabu's vendor Arara) | 2,109 (email addresses) | possible leak | contractor / third-party service | none | [notice](https://www.rakuten-sec.co.jp/web/info/info20261105-01.html) |
| 434 | 2026-11-05 | Asahi Mutual Life Insurance (Arara mail system used by contractor) | about 19,000 (email addresses) | leak identified | contractor / third-party service | none | [notice](https://www.asahi-life.co.jp/company/newsrelease/20261105.pdf) |
| 435 | 2026-11-05 | NTT DOCOMO (docomo Online Shop / My docomo servers) | up to about 300,000 | confirmed leak; 'up to' | unauthorised access (vector not disclosed) | none | [notice](https://www.docomo.ne.jp/info/notice/page/261105_03_m.html) |
| 436 | 2026-11-05 | SMBC Consumer Finance (loan guarantee business system) | up to 320,118 people | confirmed leak; 'up to' | unauthorised access (vector not disclosed) | none | [notice](https://www.smbc-cf.com/news/data/2026/11/news_20261105.pdf) |
| 437 | 2026-11-05 | Nissan Financial Services (roadside assistance contractor Prestige Core Solution 'PremierNet2') | up to about 236,000 | possible leak; 'up to' | contractor / third-party service | none | [notice](https://www.nissan-fs.co.jp/info_list/pdf/261105.pdf) |
| 438 | 2026-11-05 | euglena Co. (akyrise EC site; vendor Arara mail system; Sagawa Express parcel inquiry service) | not stated in text (secondary: about 490,000 login accounts / about 900,000 records; 177,063 email addresses via Arara; about 5,000 records via Sagawa) | confirmed (EC site); possible (vendors) | multiple vectors | none | [notice](https://www.euglena.jp/news/20261105-1/) |
| 439 | 2026-11-05 | Kyushu Electric Power Transmission and Distribution (some systems; electricity usage data) | 4,139 records | possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.kyuden.co.jp/td/press/2026/261105.html) |
| 440 | 2026-11-05 | docomo SMTB Net Bank (card loans; guarantee partner SMBC Consumer Finance's system) | up to 122,635 people | leak; 'up to'; being confirmed | contractor / third-party service | none | [notice](https://www.netbk.co.jp/contents/company/info/2026/1105_006601.html) |
| 441 | 2026-11-05 | FOOD & LIFE COMPANIES (Akindo Sushiro part-time staff portal) | 1,117 employee numbers | leak | unauthorised login | none | [notice](https://food-and-life.co.jp/corporate-news/31909/) |
| 442 | 2026-11-05 | Odawara Municipal General Medical Center (pediatric appointment system; vendor KTK Solutions 'Actmedical') | not stated (about 22,000 registrants) | possible leak | contractor / third-party service | none | [notice](https://www.city.odawara.kanagawa.jp/hospital/news_hp/p43360.html) |
| 443 | 2026-11-05 | Matsue City (official LINE registration data; former vendor Sonic Move 'COMSBI') | not stated | possible leak; no confirmed leak | contractor / third-party service | none | [notice](https://www.city.matsue.lg.jp/soshikikarasagasu/matsueshiyakusho/oshirase_joho/26821.html) |
| 444 | 2026-11-05 | THS (online shop 'Unicolle' member data) | up to 19,468 people | leak; items 'possible'; 'up to' | vulnerability | none | [notice](https://food.ths-net.com/articles/notice/18421/) |
| 445 | 2026-11-05 | Tokio Marine Direct Insurance (My Page / app for &e and docomo auto insurance) | 74 (contracts/records, preliminary) | leak identified; scope being confirmed | unauthorised access (vector not disclosed) | none | [notice](https://www.e-design.net/company/news/2026/2026_11_05.html) |
| 446 | 2026-11-05 | GlobaR (Q-navi ORDER chat API) | 17 access events confirmed (no record count) | unauthorized access confirmed; leak cannot be ruled out | misconfiguration | none | [notice](https://www.globar.co.jp/news/category-news/2026/11/05/1842/) |
| 447 | 2026-11-05 | Wellness Communications (subsidiary Ashita-Team's 'Ashita no Survey'; OEM provider Lafool) | 3 client companies, 209 people | confirmed (data illegally obtained) | contractor / third-party service | none | [notice](https://assets.minkabu.jp/news/article_media_content/urn:newsml:tdnet.info:20261104564889/140120261104564889.pdf) |
| 448 | 2026-11-05 | Konaka (subsidiaries Samantha Thavasa Japan / Barndest Rose Japan mail delivery; Arara 'repica') | 434,414 email addresses | leak identified | contractor / third-party service | none | [notice](https://www.konaka.co.jp/ir/assets/2026/11/261105.pdf) |
| 449 | 2026-11-05 | NTT Townpage (mail magazine; Arara 'repica' used by contractor) | 142,126 (email addresses) | leak (as reported by vendor) | contractor / third-party service | none | [notice](https://www.ntt-tp.co.jp/news/other-news/notice261104.html) |
| 450 | 2026-11-05 | GMO Epsilon (merchant emails; Arara 'repica' via DataX marketing tool) | 24,645 (merchant email addresses) | leak | contractor / third-party service | none | [notice](https://www.epsilon.jp/news/20261105.html) |
| 451 | 2026-11-05 | Kindai University (UCARO admissions portal emails; ODK Solutions using Arara 'arara message') | not stated | suspected leak; under investigation | contractor / third-party service | none | [notice](https://www.kindai.ac.jp/news-pr/important/2026/11/052159.html) |
| 452 | 2026-11-05 | Gakken Holdings (vendor Arara mail delivery service) | not stated | leak reported (first report) | contractor / third-party service | none | [notice](https://www.gakken.co.jp/ja/news/20269370289940467.html) |
| 453 | 2026-11-05 | Ibaraki Prefecture (Ibaraki wo Tabeyou mail magazine; contractor Nissen Medix using Arara) | up to 110,656 email addresses | confirmed leak; 'up to' | contractor / third-party service | none | [notice](https://www.pref.ibaraki.jp/somu/hodo/hodo/pressrelease/hodohappyoushiryou/2203/documents/26110hanbaisenryaku.pdf) |
| 454 | 2026-11-05 | Edogawa Ward (My Number Card pickup reservation emails; contractor using Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.edogawa.tokyo.jp/e004/kuseijoho/kohokocho/press/2026/11/1105.html) |
| 455 | 2026-11-05 | Tomakomai City (My Number Card reservation confirmation mail system; Arara) | up to 3,561 | possible leak; 'up to' | contractor / third-party service | none | [notice](https://www.city.tomakomai.hokkaido.jp/kurashi/mynumber/fusei.html) |
| 456 | 2026-11-05 | Miyazaki Prefecture (Hinata MAFiN mail service; contractor WingArc NEX / Arara) | 3,583 registrant email addresses | possible leak; being confirmed | contractor / third-party service | none | [notice](https://www.pref.miyazaki.lg.jp/noseikikaku/press/2026/11/20261105122858.html) |
| 457 | 2026-11-05 | Fukuoka City (My Number Card reservation system emails; TKC / Arara) | not stated | possible leak; under investigation | contractor / third-party service | none | [notice](https://www.city.fukuoka.lg.jp/shimin/kusei/myna_yoyaku_kojinjohorouei.html) |
| 458 | 2026-11-05 | Suzuka City (My Number Card reservation system; Officemation / TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.suzuka.lg.jp/kurashi/koseki/1009629/1018245.html) |
| 459 | 2026-11-05 | Kanegasaki Town (My Number Card reservation system external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.town.kanegasaki.iwate.jp/articles/2026110400040/) |
| 460 | 2026-11-05 | Ninomiya Town (My Number Card reservation system confirmation mail service; TKC) | not stated | leak confirmed at vendor; town users' inclusion unconfirmed | contractor / third-party service | none | [notice](https://www.town.ninomiya.kanagawa.jp/0000003661.html) |
| 461 | 2026-11-05 | Iwaki City (My Number Card reservation system; TKC's mail vendor Arara) | about 120 (email addresses) | possible leak | contractor / third-party service | none | [notice](https://www.city.iwaki.lg.jp/www/contents/1793766039632/index.html) |
| 462 | 2026-11-05 | Ueda City (My Number Card reservation system emails; TKC's vendor Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.ueda.nagano.jp/soshiki/simin/139251.html) |
| 463 | 2026-11-05 | Tsu City (My Number Card reservation system confirmation mail service; TKC / Arara) | not stated | leak announced by vendor; city inclusion under investigation | contractor / third-party service | none | [notice](https://www.info.city.tsu.mie.jp/kurashi/koseki_juuminhyou/1001575/1014112.html) |
| 464 | 2026-11-05 | Kuwana City (My Number Card reservation system; Officemation / TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.kuwana.lg.jp/kosekijyumin/kurashi/todokede/20261105.html) |
| 465 | 2026-11-05 | Nasukarasuyama City (My Number Card reservation system emails; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.nasukarasuyama.lg.jp/kurashi/my-number/my-number-system/page006988.html) |
| 466 | 2026-11-05 | Kitakami City (online application system / My Number Card reservation external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.kitakami.iwate.jp/life/emergency/30276.html) |
| 467 | 2026-11-05 | Ohtawara City (My Number Card reservation system external mail service; TKC / Arara) | not stated | possible leak (first report) | contractor / third-party service | none | [notice](https://www.city.ohtawara.tochigi.jp/docs/2026110500030/) |
| 468 | 2026-11-05 | Inami Town, Hyogo (online application system; TKC's sub-vendor Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.town.hyogo-inami.lg.jp/0000007767.html) |
| 469 | 2026-11-05 | Haga Town (My Number Card reservation system mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.town.tochigi-haga.lg.jp/kurashi/kurashi/kojinbangou/20261104_huseiakusesu.html) |
| 470 | 2026-11-05 | Naka City (My Number Card reservation system external mail service; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.city.naka.lg.jp/kurashi-tetsuduki/tetsuduki/mynumber/mynumber-card/page011919.html) |
| 471 | 2026-11-05 | Minamiaizu Town (My Number Card reservation service emails; TKC / Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.town.minamiaizu.lg.jp/official/soshikikarasagasu/sogoseisakuka/oshirase/1/4090.html) |
| 472 | 2026-11-05 | Toyama Prefecture (energy-saving appliance campaign; JTB Toyama branch using Arara) | 247 (recipients of a Sept 28, 2026 email) | possible leak | contractor / third-party service | none | [notice](https://www.pref.toyama.jp/1705/kensei/kouhou/houdou/2026/1030_shoene.html) |
| 473 | 2026-11-05 | Juhachi-Shinwa Bank (digital local currencies MINA Coin / Yudepi; Finnovalley's vendor Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.18shinwabank.co.jp/announcement/important/y2026/1105.html) |
| 474 | 2026-11-05 | Daishi Hokuetsu Bank (personal loan 'Benrina 365'; guarantor SMBC Consumer Finance) | up to 1,307 people | confirmed leak; 'up to' | contractor / third-party service | none | [notice](https://www.dhbk.co.jp/important/1202858_2311.html) |
| 475 | 2026-11-05 | The Bank of Fukuoka (guarantor SMBC Consumer Finance's system) | not stated | leak; items being confirmed | contractor / third-party service | none | [notice](https://www.fukuokabank.co.jp/announcement/important/y2026/1105.html) |
| 476 | 2026-11-05 | The Ehime Bank (partner SMBC Consumer Finance's guarantee system) | not stated | Confirmed to be within the leak; scope under confirmation | contractor / third-party service | none | [notice](https://www.himegin.co.jp/new_csr/pdf/20261105_1.pdf) |
| 477 | 2026-11-05 | North Pacific Bank (card loan 'Super Arca'; guarantor SMBC Consumer Finance) | not stated | leak reported | contractor / third-party service | none | [notice](https://www.hokuyobank.co.jp/newsrelease/pdf/20261105_076990.pdf) |
| 478 | 2026-11-05 | The Kumamoto Bank (guarantor SMBC Consumer Finance's system) | not stated | leak; items being confirmed | contractor / third-party service | none | [notice](https://www.kumamotobank.co.jp/announcement/important/y2026/20261105josirase2.html) |
| 479 | 2026-11-05 | Juhachi-Shinwa Bank (guarantor SMBC Consumer Finance's system) | not stated | leak; found; possible inclusion; leaked items "being confirmed" | contractor / third-party service | none | [notice](https://www.18shinwabank.co.jp/announcement/important/y2026/13539683396aec34dc471ef20261105164844.html) |
| 480 | 2026-11-05 | The Chugoku Bank (card loan 'Coreca' / free loan; guarantor SMBC Consumer Finance) | not stated | leak identified | contractor / third-party service | none | [notice](https://www.chugin.co.jp/news/3583.html) |
| 481 | 2026-11-05 | Hiroshima Bank (card loans; guarantor SMBC Consumer Finance) | under investigation | leak identified; items being confirmed | contractor / third-party service | none | [notice](https://www.hirogin.co.jp/information/info261105/info261105.pdf) |
| 482 | 2026-11-05 | The Kiyo Bank (guarantee partner SMBC Consumer Finance) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.kiyobank.co.jp/personal/get_pdf.php?f=00003323) |
| 483 | 2026-11-05 | Tsukuba Bank (partner SMBC Consumer Finance's guarantee system) | not stated | leak reported; being confirmed | contractor / third-party service | none | [notice](https://www.tsukubabank.co.jp/cms/article/76ee6818987f5e1c31d22e2302d6e0e18688c745/) |
| 484 | 2026-11-05 | GMO MakeShop (Mail Delivery Plus / MakeRepeater; external mail service Arara 'arara message') | about 12.6 million (email addresses) | leak identified; affected shops not yet identified | contractor / third-party service | none | [notice](https://www.makeshop.co.jp/news/info/2026-11-05_2/) |
| 485 | 2026-11-05 | GMO Commerce (mail delivery features; external mail service Arara) | not stated | leak | contractor / third-party service | none | [notice](https://www.gmo-c.jp/info/%E5%BD%93%E7%A4%BE%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%A7%E5%88%A9%E7%94%A8%E3%81%99%E3%82%8B%E5%A4%96%E9%83%A8%E3%81%AE%E3%83%A1%E3%83%BC%E3%83%AB%E9%85%8D%E4%BF%A1%E3%82%B5%E3%83%BC%E3%83%93/) |
| 486 | 2026-11-05 | Terrada Warehouse (TERRADA ID, minikura, etc. email delivery; vendor Arara) | not stated | possible leak | contractor / third-party service | none | [notice](https://www.terrada.co.jp/ja/news/17123/) |
| 487 | 2026-11-05 | Yokote City (survey contractor Shibata Koji Chosa; ransomware attack) | 12 contracted projects; about 1,300 people cumulative | possible leak | contractor / third-party service | none | [notice](https://www.city.yokote.lg.jp/shigoto/1001164/1001361/1013864.html) |
| 488 | 2026-11-05 | Porsche Japan / Porsche Financial Services Japan (roadside / accident reception contractor Prestige Core Solution) | not stated | exfiltration confirmed at vendor; scope unidentified | contractor / third-party service | none | [notice](https://www.porsche.com/japan/jp/legal/notice/) |
| 489 | 2026-11-05 | Lieferant (ecoco online shop / Rakuten store order management account) | not stated | leak confirmed (first report) | unauthorised login | none | [notice](https://ecoco.cloud/blogs/important/1) |
| 490 | 2026-11-05 | Japan Arts Council (member mailings; Arara 'repica' via contractor) | about 38,000 (email addresses) | leak identified | contractor / third-party service | none | [notice](https://www.ntj.jac.go.jp/topics/top/2026/20261104_mailservice_personalinformation_incident/) |
| 491 | 2026-11-05 | Rosette (mail delivery; external service Arara 'repica') | 2,115 email addresses | leak identified | contractor / third-party service | none | [notice](https://rosette.jp/Page/notice20261105.aspx) |
| 492 | 2026-11-05 | KDDI (au Bicycle Support; contractor Prestige Core Solution's business system) | not stated | possible leak; under investigation | contractor / third-party service | none | [notice](https://www.au.com/information/notice_mobile/service/2026-012/) |
| 493 | 2026-11-05 | Martial Arts Legal Professional Corporation (notification emails; Arara mail system) | 101,226 (email only); 5,823 (email plus other data) | leak confirmed | contractor / third-party service | none | [notice](https://www.martial-arts.jp/information/notice.html) |
| 494 | 2026-11-06 | Japan Network Security Association (JNSA) - Information Security Literacy Check Service | Up to 15,128 records expected | Possible leak (feared) | unauthorised access (vector not disclosed) | none | [notice](https://www.jnsa.org/dl/annual/20261106.pdf) |
| 495 | 2026-11-06 | TeamSpirit Inc. (cloud environment accessed via software development server) | 28,824 records excluding duplicates (incl. 35 records of sensitive personal information) | Confirmed leak | multiple vectors | none | [notice](https://corp.teamspirit.com/news/information/2026/11/2026_1106_01/) |
| 496 | 2026-11-06 | Mizkan Co., Ltd. (member community site "Mizkan 365") | 487 members affected (458 tampering only; 29 leak and tampering) | Confirmed leak (29) and tampering (487) | vulnerability | none | [notice](https://www.mizkan.co.jp/file.jsp?id=2021_Renewal%2Ffiles%2Fpdf%2Femg%2Fnews%2Foshirase18.pdf) |
| 497 | 2026-11-06 | Kyoto City (Ikiiki Senior Point Program; contractor JTB Kyoto Branch / subcontractor Sagawa Express "Parcel Inquiry Service") | 253 records | Possible leak | contractor / third-party service | none | [notice](https://www.city.kyoto.lg.jp/hokenfukushi/page/0000359972.html) |
| 498 | 2026-11-06 | Doutor Coffee Co., Ltd. (official online shop "Doutor Online Shop"; development/maintenance contractor) | 24,762 member records and 9 delivery-address records (24,771 in total) | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.doutor.co.jp/news/newsrelease/detail/20261106150715.html) |
| 499 | 2026-11-06 | Kobe International University (safety confirmation system "ANPIC"; external contractor) | Not stated | Confirmed leak | contractor / third-party service | none | [notice](https://www.kobe-kiu.ac.jp/news/615723/) |
| 500 | 2026-11-06 | Shiga University (safety confirmation system "ANPIC" run by Avance System; mail delivery via Arara Message) | Not stated for the university (about 1,000,000 email addresses for ANPIC overall, per the operator) | Leak reported by operator; university's share under confirmation | contractor / third-party service | none | [notice](https://www.shiga-u.ac.jp/48359/) |
| 501 | 2026-11-06 | Kakogawa City (Kakogawa Online Application System provided by TKC; mail delivery via Arara Message) | Not stated | Possible leak (reported by vendor) | contractor / third-party service | none | [notice](https://www.city.kakogawa.lg.jp/soshikikarasagasu/kikakubu/jouhouseisakuka/onlineshinsei/51343.html) |
| 502 | 2026-11-06 | Sendai City (My Number Card issuance reservation/management system run by TKC; mail delivery via Arara Message) | 12,211 registered email addresses as of Nov 4 | Possible leak | contractor / third-party service | none | [notice](https://www.city.sendai.jp/kosekijumin/20261106.html) |
| 503 | 2026-11-06 | Shiseido Company, Limited (online skin measurement system "FCA") | 2,515 records confirmed leaked | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://corp.shiseido.com/jp/notice/20261106.html) |
| 504 | 2026-11-06 | Life Corporation (Life Net Super e-mail newsletter; contractor Fujitsu / subcontractor Arara) | 133,330 records | Possible leak | contractor / third-party service | none | [notice](https://www.lifecorp.jp/vc-files/pdf/newsrelease/others/20261106.pdf) |
| 505 | 2026-11-06 | Cosmo Energy Holdings Co., Ltd. (IR e-mail newsletter; contractor Tribeck's external cloud service / Arara) | 220 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.cosmo-energy.co.jp/ja/information/topics/2026/261106-01.html) |
| 506 | 2026-11-06 | Pacific League Marketing Corporation (match-update newsletters of 5 Pacific League clubs via Arara Message / Chiba Lotte Marines official site) | (1) 13,711 email addresses via Arara (5 clubs); (2) 11,875 email addresses and 37,070 nicknames from Chiba Lotte Marines official site | Confirmed leak | multiple vectors | none | [notice](https://prtimes.jp/main/html/rd/p/000000326.000019259.html) |
| 507 | 2026-11-07 | SignalTalk Co., Ltd. (online mahjong "Maru-Jan") | 1,855,578 members' email addresses and passwords | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://prtimes.jp/main/html/rd/p/000000136.000009867.html) |

(Added 10 November 2026)  
77 rows (508–584) were added on 10 November 2026: 5 from the pending list (508, 514, 516, 556, 560), 64 disclosed 6–9 November 2026, and 8 disclosed 30 October – 5 November that the fourth edition and the 8 November addition had missed. The table of 207 rows added on 8 November is left as it was, and the new rows follow below; the six tables together match the 584 rows of `data/registry.json`. IDs follow publication date, with no meaning to the order within a day; 508 (30 October) is placed at the head of the 10 November addition.

Discovery and drafting again used AI-agent web search and retrieval of each notice, merging five agents split by publication date (first and second halves of 6 November, 7–9 November, 9 November, and a sweep of 8–9 November plus chain-origin follow-ups) and removing duplicates. The basis of admission and the verification procedure are set out before the table. On 8 November only 13 rows had been found for 6 November, while the daily list of the aggregator jouhourouei.clipmaster.jp shows more than 50; 47 were added now. Gaps against the same site remain for 3–5 November and were not examined this time. Rows whose notice sits outside the organisation's own domain (519 Yamaguchi on a campaign site, 527 G.M Corporation on a rental server, 538 Mitsui Direct on the parent MS&AD Holdings' domain, 582 Manbou on the parent JR Kyushu's domain) and a row whose count appears only in an image (565 Fujio Food System) are noted in the notes.In addition, on 10 November 2026 a separate AI agent that had not seen the drafting re-fetched the `primary_url` of 30 of the 77 new rows (the 16 largest and 14 at random) and checked scale and unit, status wording, vector, AI mention and publication date: 24 matched; 2 were corrected (554 SUBARU: the body's "it was found that ... leaked to the outside" was missing from the status; 561 Resona, Kansai Mirai and Minato banks: per-bank counts confirmed from the notice's table); 4 received notes only (509 Kinko's Japan: the count is on the separate second-notice page; 546 Bank of Okinawa: the notice gives no day; 571 Sato Food Service: second-notice date; 577 Nitori: the phrase "addressed the vulnerable points"). The remaining 47 rows were checked in the verification described below.

(Added 10 November 2026)  
The 284 rows added in the fifth edition (301–584) were verified differently from earlier editions. The author personally opened and read the primary notices of 9 rows (301–309), all consistent with the ledger. For the remaining 275 rows (310–584), at the author's instruction, AI agents re-fetched each row's `primary_url` on 10 November 2026 and checked scale and unit, status wording, vector, AI mention, publication date and the admission criteria against the notice (30 rows in the re-check described above, 245 rows by six agents splitting the rows), recording verbatim the sentences used as evidence. Of the 245 rows: 180 matched; 6 had values corrected; 53 received notes only; for 2 the `primary_url` page is not the notice that gives the count (320 TKC, 508 JERA; the count comes from follow-ups cited in the notes); 3 could not be re-fetched (404 Sakai and 466 Kitakami refused or errored; 565 Fujio Food System's text is an image). The 6 corrections: 323 Rims Capital (status word to the notice's "found"), 352 Monteroza (vector from vulnerability to contractor; the vulnerability was the contractor Arara's), 376 Toho Cash and Carry (scale to "15,497 e-mail addresses" from the company's PDF notice), 398 Miyazaki City (provider Densan added to the organisation field), 479 Juhachi-Shinwa Bank ("under investigation" is not in the notice; status set to the notice's words), 566 Okayama Prefecture (status to "may have leaked"). Notes were added where the page gives no publication date or only an update date, where the page has been updated to a later version, where the `primary_url` is a different notice in the series, where the body states the status more strongly than the title, or where the vector classification needs judgement. Nine of the agents' verdicts (310, 376, 398, 566 and five rows drawn at random from those judged matching) were re-checked by the AI that did the editorial work, opening the notices again: 8 held, and the proposed correction for 398 (that the provider is not TKC) was not adopted, since the notice names both "provider (Densan Co., Ltd.)" and "TKC Corporation, the system provider". Rows noted as on the boundary of the admission criteria (322, 369, 441, 513, 528, 550) await the author's judgement.

### The 77 rows added on 10 November 2026

| ID | Published | Organisation | Scale (as stated, original unit) | Status | Vector | AI mentioned | Primary source |
|---|---|---|---|---|---|---|---|
| 508 | 2026-10-30 | JERA (movie discount service "JERA Sunday"; external e-mail delivery service of Arara) | 30,337 e-mail addresses (Nov 7 update; approx. 110,000 on Nov 2) | Confirmed leak | contractor / third-party service | none | [notice](https://www.jera.co.jp/news/notice/20261030_2567) |
| 509 | 2026-11-02 | Kinko's Japan (Smart Membership member newsletter; Arara "Arara Message") | 266,395 records (second report, Nov 9); not stated in first report | Confirmed leak | contractor / third-party service | none | [notice](https://www.kinkos.co.jp/news/important-20261102/) |
| 510 | 2026-11-02 | ENEOS Corporation ("ENEOS Car Lease" administration; contractor Prestige Core Solution) | up to 8,500 contracts | Confirmed leak (count stated as up to, possibly affected contracts) | contractor / third-party service | none | [notice](https://www.eneos.co.jp/announcement/20261102.html) |
| 511 | 2026-11-02 | Fire Equipment and Safety Center of Japan (e-mail newsletter and training-schedule notices; contractor Arara) | 11,548 records (3rd report); initially approx. 12,000 e-mail addresses plus approx. 720 fire-department addresses | Confirmed leak (3rd report) | contractor / third-party service | none | [notice](https://www.fesc.or.jp/cms/wp-content/uploads/2026/11/メール配信委託先への不正アクセスによる情報漏えいについて（第3報）-2.pdf) |
| 512 | 2026-11-02 | Nippon Rent-A-Car Service (accident/breakdown reception contractor Prestige Core Solution) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.nipponrentacar.co.jp/info/202611.html) |
| 513 | 2026-11-02 | Sony Assurance (road-service contractor Prestige Core Solution's business system) | Not stated | Under investigation (exfiltration being checked) | contractor / third-party service | none | [notice](https://from.sonysonpo.co.jp/topics/information/02112026_288508.html) |
| 514 | 2026-11-04 | Okazaki City (reservation-confirmation e-mail service of the My Number card reservation system; TKC / Arara) | Under confirmation | Possible leak | contractor / third-party service | none | [notice](https://www.city.okazaki.lg.jp/shisei/koho/1006195/1006358/1017062/1017558.html) |
| 515 | 2026-11-04 | JACCS (road service attached to CLUB AJ Card / 2Rinkan JACCS Card; contractor Prestige Core Solution) | Not stated | Confirmed leak | contractor / third-party service | none | [notice](https://www.jaccs.co.jp/information/emerge/page_01196.html) |
| 516 | 2026-11-05 | Hatoya (Hatoya Road Service; contractor Prestige Core Solution) | 1,085 records (preliminary; may include duplicates) | Leak (preliminary count) | contractor / third-party service | none | [notice](https://hatoya.co.jp/shop-infomation/20261105) |
| 517 | 2026-11-05 | Sompo Japan Insurance (auto-insurance inquiry/reception management; contractor Prestige Core Solution "PremierNet2") | approx. 65,000 records | Possible leak | contractor / third-party service | none | [notice](https://www.sompo-japan.co.jp/-/media/SJNK/files/news/2026/20261105_1.pdf) |
| 518 | 2026-11-05 | Panasonic Automotive Systems (Panasonic Blue Battery support; contractor Prestige Core Solution) | 173 records | Confirmed leak | contractor / third-party service | none | [notice](https://automotive.panasonic.com/information/20261105-01) |
| 519 | 2026-11-06 | Yamaguchi Prefecture (Buchi-Eco Yamaguchi energy-saving appliance purchase support campaign bulk notification e-mail; campaign secretariat JTB / Giftpad joint venture / Arara 'Arara Message') | Not stated (under investigation) | Possible leak (under investigation) | contractor / third-party service | none | [notice](https://buchieco-yamaguchi-shoene.jp/news/29) |
| 520 | 2026-11-06 | San ju San Bank (San ju San Bank Free Loan; guarantor SMBC Consumer Finance guarantee system) | 914 people (identified so far per SMBC CF report) | Confirmed leak | contractor / third-party service | none | [notice](https://www.33bank.co.jp/release/back-number/2026/pdf/20261106.pdf) |
| 521 | 2026-11-06 | Tajima Bank (card loans and some other products; partner / guarantor SMBC Consumer Finance guarantee system) | Not stated (under investigation by SMBC CF) | Confirmed leak (affected items being confirmed) | contractor / third-party service | none | [notice](https://www.tajimabank.co.jp/news/important/data_leak_SMBCCF.pdf) |
| 522 | 2026-11-06 | Bank of Toyama ('Pocket Loan'; guarantee partner SMBC Consumer Finance guarantee system) | Not stated (being confirmed) | Confirmed leak | contractor / third-party service | none | [notice](https://www.toyamabank.co.jp/pages/oshirase/2026/20261106.pdf) |
| 523 | 2026-11-06 | Tottori Bank (Tottori Bank Free Loan; guarantor SMBC Consumer Finance guarantee system) | Not stated | Confirmed leak | contractor / third-party service | none | [notice](https://www.tottoribank.co.jp/oshirase/pdf/2026-11-06.pdf) |
| 524 | 2026-11-06 | 2Rinkan Yellow Hat (2Rinkan road services incl. JACCS card member road service; contractor Prestige Core Solution) | Not stated (under investigation) | Possible leak | contractor / third-party service | none | [notice](https://2rinkan.jp/annai/20261106/) |
| 525 | 2026-11-06 | Sakai City ('Sakai Premium Gift Certificates 2026'; e-mail delivery service of Arara used by the JTB / EVENTIFY / Giftpad consortium) | Up to approx. 290,000 records (voucher winners) and up to approx. 2,600 records (participating stores); under investigation | Possible leak (up to; under investigation) | contractor / third-party service | none | [notice](https://www.city.sakai.lg.jp/shisei/koho/hodo/hodoteikyoshiryo/kakohodo/r8/r811/081106_06.files/1106_06.pdf) |
| 526 | 2026-11-06 | CYBIRD (e-mail delivery for multiple services; Arara e-mail delivery service) | 98,738 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.cybird.co.jp/news/2026110602/) |
| 527 | 2026-11-06 | G.M Corporation / Grateful Mind Corporation (ELECTRON ONLINE SHOP e-mail newsletter; outsourced provider Arara 'repica') | 31,855 records | Confirmed leak | contractor / third-party service | none | [notice](https://xs620092.xsrv.jp/blog/2026/11/06/elinfo2611/) |
| 528 | 2026-11-06 | All prefectures and all designated cities (Takarakuji official lottery website and app members) | Not stated (some members) | Possible exposure (member data viewed; no data exfiltration confirmed) | unauthorised login | none | [notice](https://www.takarakuji-preliminary.jp/宝くじ公式サイトおよび公式アプリの一時停止について_20261106.pdf) |
| 529 | 2026-11-06 | MINKABU THE INFONOID (e-mail delivery function of financial information solutions for financial institutions; contractor Arara) | Approx. 4,000 e-mail addresses | Possible leak | contractor / third-party service | none | [notice](https://minkabu.co.jp/20261106_4174/) |
| 530 | 2026-11-06 | Saitama Prefecture (SAITAMA Hike & Cycle Stamp Rally survey invitation e-mail; Arara 'Arara Message' used by the contractor) | Not stated (being confirmed) | Possible leak | contractor / third-party service | none | [notice](https://www.pref.saitama.lg.jp/a0806/news/page/news2026110601.html) |
| 531 | 2026-11-06 | Kyoto City (Kyoto City KYOCERA Museum of Art via 'ARTPASS' operated by Inventit, and Nijo-jo Castle via 'asoview!' operated by Asoview; both via Arara's system) | Not stated | Possible leak (ARTPASS) / confirmed leak reported (asoview!); under investigation | contractor / third-party service | none | [notice](https://www.city.kyoto.lg.jp/bunshi/page/0000359980.html) |
| 532 | 2026-11-06 | Saitama Prefecture (e-tickets for prefectural park pools and Saitama Children's Zoo; designated manager Saitama Park & Greenery Association / Asoview / Arara 'Arara Message') | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.pref.saitama.lg.jp/a1105/news/page/news2026110601.html) |
| 533 | 2026-11-06 | Okinawa Prefecture (Okinawa single-parent household living support program; contractor J-G joint venture / Arara e-mail delivery service) | 217 e-mail addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.pref.okinawa.jp/kyoiku/kosodate/1008226/1036501/1036531/1041859.html) |
| 534 | 2026-11-06 | Okayama Prefecture (Okayama energy-saving appliance purchase and home insulation renovation support campaign; campaign secretariat JTB / Arara e-mail delivery service) | Up to approx. 1,100 records | Possible leak (up to) | contractor / third-party service | none | [notice](https://www.pref.okayama.jp/uploaded/life/1064690_10321381_misc.pdf) |
| 535 | 2026-11-06 | Nishi-Nippon Financial Holdings (Nishi-Nippon FH Business Contest pre-entry and inquiry forms; Studio) | 141 records (pre-entry form) and 47 records (inquiry form) | Possible leak | contractor / third-party service | none | [notice](https://www.nnfh.co.jp/assets/pdf/news/nnfh_20261106-2.pdf) |
| 536 | 2026-11-06 | Daisen City (land surveying and other contracted work; contractor Shibata Koji Chosa) | 31 records (cumulative) | Possible leak | contractor / third-party service | none | [notice](https://www.city.daisen.lg.jp/archive/p20261106093509) |
| 537 | 2026-11-06 | Yurihonjo City (pre-construction building survey and compensation survey work; contractor Shibata Koji Chosa, ransomware attack) | Not stated (under investigation; two contracted jobs affected) | Possible leak (under investigation) | contractor / third-party service | none | [notice](https://www.city.yurihonjo.lg.jp/1000002/1001867/1001932/1010291/1014011.html) |
| 538 | 2026-11-06 | Mitsui Direct General Insurance (company website and app) | Up to 234,000 records | Confirmed leak (up to) | unauthorised access (vector not disclosed) | none | [notice](https://www.ms-ad-hd.com/ja/news_group/20261106_mitsui_direct/main/0/link/20261106_mitsuidirect.pdf) |
| 539 | 2026-11-06 | Pal System Consumers' Co-operative Union (promotional e-mails for trial-set applications and brochure requests; e-mail delivery service Arara) | Not stated | Possible leak (under investigation) | contractor / third-party service | none | [notice](https://information.pal-system.co.jp/topics/20261106-incident/) |
| 540 | 2026-11-06 | Chuo Alps Kanko (Hotel Senjojiki official booking site; external reservation management system "Reserve Gate" operated by Navc) | Not stated | Confirmed access/acquisition by a third party (per Navc) | contractor / third-party service | none | [notice](https://chuo-alps.com/%E5%A4%96%E9%83%A8%E4%BA%88%E7%B4%84%E7%AE%A1%E7%90%86%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%80%8C%E3%83%AA%E3%82%B6%E3%83%BC%E3%83%96%E3%82%B2%E3%83%BC%E3%83%88%E3%80%8D%E3%81%A7%E7%99%BA%E7%94%9F/) |
| 541 | 2026-11-06 | Sanrio (Sanrio Online Shop "GMO Atobarai" deferred-payment users; GMO Payment Service's contractor Martial Arts law firm / Arara "Arara Message") | 191 records (e-mail address only) + 5 records (e-mail, name, billing details, etc.) | Confirmed leak | contractor / third-party service | none | [notice](https://shop.sanrio.co.jp/news/86) |
| 542 | 2026-11-06 | Konan University (e-mail addresses registered on exam portal "UCARO"; operator ODK Solutions / Arara) | Not stated | Suspected leak (under investigation) | contractor / third-party service | none | [notice](https://www.konan-u.ac.jp/news/archives/58522) |
| 543 | 2026-11-06 | Enoshima Electric Railway (Enoshima Sea Candle and other facility tickets via "asoview!" app; operator Asoview / Arara) | Not stated | Confirmed leak (reported by contractor) | contractor / third-party service | none | [notice](https://www.enoden.co.jp/corporate-news/20261106-1/) |
| 544 | 2026-11-06 | IDOM (roadside-assistance operations; contractor Prestige Core Solution) | 694 records | Confirmed leak | contractor / third-party service | none | [notice](https://idom-inc.com/news/press/20261106-38772.html) |
| 545 | 2026-11-06 | IDOM (debt-collection operations; contractor LENDY Servicer's business system) | 1,663 records | Confirmed leak (viewed; download possible) | contractor / third-party service | none | [notice](https://idom-inc.com/news/press/20261106-38772.html) |
| 546 | 2026-11-06 | Bank of Okinawa (collection of overdue "Chekit" personal loans; contractor LENDY Servicer's negotiation-record system) | 211 people | Possible leak | contractor / third-party service | none | [notice](https://www.okinawa-bank.co.jp/news_release/2026110600037/file_contents/nr.pdf) |
| 547 | 2026-11-06 | WingArc NEX ("SMART L-Gov ALERT", "Ikukuru Mail", custom systems and "Rakuriza" e-mail engine; Arara "Arara Message") | approx. 290,000 e-mail addresses (+ approx. 5,900 for Rakuriza, added Nov 9) | Confirmed leak | contractor / third-party service | none | [notice](https://www.wingarc-nex.com/news/202611/information.html) |
| 548 | 2026-11-06 | Zurich Insurance Company Ltd, Japan Branch (roadside assistance; former contractor Prestige Core Solution's business system) | Not stated | Confirmed leak (reported by contractor; scope under investigation) | contractor / third-party service | none | [notice](https://www.zurich.co.jp/aboutus/news/news/2026/1106/) |
| 549 | 2026-11-06 | EDION (server area storing log files of its e-commerce site) | up to 4,131 people + up to 9,554 people (fewer than 13,685 combined); third category under review | Possible leak | vulnerability | none | [notice](https://www.edion.co.jp/system/files/news-release/pdf/ja/2026-11/20261106_pr_1.pdf) |
| 550 | 2026-11-06 | BitCash Inc. ("WebMoney" e-money system) | Not stated | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.webmoney.jp/news/2026/18259.html) |
| 551 | 2026-11-06 | Hotelovers (e-mail delivery "GMO Marketing Connect" for its online shop; GMO Commerce / delivery platform Arara) | 1,578,779 records | Confirmed leak | contractor / third-party service | none | [notice](https://hotelovers.co.jp/news/3630) |
| 552 | 2026-11-06 | Canon Marketing Japan ("MSI Store" member/purchaser e-mail addresses; GMO Makeshop "MakeRepeater" / Arara) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://jpstore.msi.com/new/2026-11-06-172139.html) |
| 553 | 2026-11-06 | Shogakukan ("Shogakukan ID" and other member data; e-mail delivery system Arara) | 1,993,665 records | Confirmed leak (title says possible) | contractor / third-party service | none | [notice](https://www.shogakukan.co.jp/news/477708) |
| 554 | 2026-11-06 | SUBARU (call-center contractor Prestige Core Solution's business system; roadside-assistance intake) | up to 228,734 records (call-center intake records) | Possible leak | contractor / third-party service | none | [notice](https://www.subaru.co.jp/pdf/info/2026_1106_2026-11-06-135049.pdf) |
| 555 | 2026-11-06 | Subaru Finance (auto-insurance roadside assistance "SUBARU Anshin Hotline"; contractor Prestige Core Solution's external system) | up to 3,117 records | Confirmed leak | contractor / third-party service | none | [notice](https://sfc.subaru.co.jp/topics/20261105175142/) |
| 556 | 2026-11-06 | Aioi Nissay Dowa Insurance ("Policyholder dedicated page") | approx. 444,000 records | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.aioinissaydowa.co.jp/corporate/about/news/pdf/2026/news_2026110601531.pdf) |
| 557 | 2026-11-06 | cyma Yellow Hat (bicycle after-sales support service; contractor Prestige Core Solution) | Not stated | Leak (items under investigation) | contractor / third-party service | none | [notice](https://cyclemarket.jp/static/news/2026110601/) |
| 558 | 2026-11-06 | REXEV (customer-center operations for "eemo" car sharing and partner services; contractor Prestige Core Solution) | 547 records (inquiry records as of Nov 4) | Confirmed leak | contractor / third-party service | none | [notice](https://rexev.co.jp/2026/11/06/post-15282/) |
| 559 | 2026-11-06 | Kohnan Shoji ("Kohnan Bicycle Anshin Plan" roadside assistance; sub-contractor Prestige Core Solution) | 949 records (under review) | Confirmed leak | contractor / third-party service | none | [notice](https://www.hc-kohnan.com/wprnw/wp-content/uploads/2026/11/%E3%80%8C%E3%82%B3%E3%83%BC%E3%83%8A%E3%83%B3%E8%87%AA%E8%BB%A2%E8%BB%8A%E3%81%82%E3%82%93%E3%81%97%E3%82%93%E3%83%97%E3%83%A9%E3%83%B3%E3%80%8D%E6%A5%AD%E5%8B%99%E5%86%8D%E5%A7%94%E8%A8%97%E5%85%88%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E3%82%88%E3%82%8B%E3%81%8A%E5%AE%A2%E6%A7%98%E6%83%85%E5%A0%B1%E6%BC%8F%E6%B4%A9%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%8A%E8%A9%AB%E3%81%B3%E3%81%A8%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B.pdf) |
| 560 | 2026-11-06 | Mitsui Sumitomo Insurance (policyholder-only web page) | About 37,000 records | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.ms-ins.com/news/fy2026/pdf/1106_1.pdf) |
| 561 | 2026-11-06 | Resona Bank, Kansai Mirai Bank, Minato Bank (guarantee-business system of guarantor SMBC Consumer Finance) | 139 / 5,793 / 3 records (bank mapping unverified; total 5,935 per secondary sources) | Confirmed leak (closed accounts) | contractor / third-party service | none | [notice](https://www.resona-gr.co.jp/holdings/news/newsrelease_c/2026/files/20261106_1k.pdf) |
| 562 | 2026-11-06 | BMW Japan / BMW Japan Finance (road-assistance contractor Prestige Core Solution) | Not stated (not yet identified) | Possible leak | contractor / third-party service | none | [notice](https://www.bmw.co.jp/ja/topics/announcement/202611-01.html) |
| 563 | 2026-11-06 | Ceres Inc. (development environment of point site "Point Income") | approx. 11,100 members; 4 device IDs | Leak | unauthorised access (vector not disclosed) | none | [notice](https://media.ceres-inc.jp/news/2026/11/20261106_v2-1.pdf) |
| 564 | 2026-11-06 | Ceres / Mercury (crypto exchange "CoinTrade" e-mail; Arara "repica" used by contractor) | 88,289 e-mail addresses (deduplicated) | Confirmed leak | contractor / third-party service | none | [notice](https://media.ceres-inc.jp/news/2026/11/20261106_v2-1.pdf) |
| 565 | 2026-11-06 | Fujio Food System (e-mail delivery for Kushiya Monogatari / Delices du Palais) | Not stated in text (image only; 316,668 per secondary sources) | Leak (as titled) | contractor / third-party service | none | [notice](https://fujiogroup.com/company/news/2026/11/post-287.html) |
| 566 | 2026-11-07 | Okayama Prefecture (invitation e-mails for OTEX 2026 and the business-succession "Corporate Growth Training"; contractor Okayama Prefectural Industrial Promotion Foundation / Arara e-mail delivery service) | 19,555 + 3,057 e-mails sent (22,612 in total) | Possible leak (under investigation) | contractor / third-party service | none | [notice](https://www.pref.okayama.jp/page/1064879.html) |
| 567 | 2026-11-07 | ASOBISYSTEM (fan-club site newsletters for its artists; site operator Fanplus / Arara "Arara Message") | Not stated | Confirmed leak | contractor / third-party service | none | [notice](https://asobisystem.com/news/77602/) |
| 568 | 2026-11-07 | Tsukaeru.net ("Tsukaeru Portal" contract management and purchase portal; VPS and shared servers) | Not stated (127 VPS instances under investigation; not a leak count) | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.tsukaeru.net/news/20261107/) |
| 569 | 2026-11-07 | Step Golf (business system and reservation system) | Up to 215,000 records (database registrations; not number of people) | Highly likely leak (under investigation) | unauthorised access (vector not disclosed) | none | [notice](https://www.stepgolf.co.jp/news/261107) |
| 570 | 2026-11-07 | MERY (MERY e-mail newsletter; Arara e-mail delivery system contracted and operated by parent company Shogakukan) | Up to 10,110 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.mery.co.jp/notice/20261107) |
| 571 | 2026-11-07 | Sato Food Service ("Sato Kids Club" e-mail service; contractor GMO Commerce / subcontractor Arara) | 318,513 e-mail addresses | Confirmed leak (exfiltrated) | contractor / third-party service | none | [notice](https://www.sato-res.com/blogs/news/n-20261107) |
| 572 | 2026-11-09 | Mitsui Sumitomo Insurance (road-service operations for some auto insurance policies; contractor Prestige Core Solution business system) | About 228,000 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.ms-ins.com/news/fy2026/pdf/1109_1.pdf) |
| 573 | 2026-11-09 | Mitsui Sumitomo Insurance ("MS Compass" information site for mid-sized and small businesses) | About 23,000 records | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.ms-ins.com/news/fy2026/pdf/1109_2.pdf) |
| 574 | 2026-11-09 | Waseda University (user-information management system used for logging in to the MyWaseda portal) | 3,342 records in total (about 3,400) | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.waseda.jp/top/news/topic/124183) |
| 575 | 2026-11-09 | RAKSUL (data-submission processing system of the RAKSUL printing service) | Being tallied | Possible leak | unauthorised login | none | [notice](https://corp.raksul.com/news/press/261109_unauthorized-access/) |
| 576 | 2026-11-09 | SEGA (some newsletters for SEGA and SEGA FAVE products and services; contractor Arara "Arara Message") | 2,196,044 e-mail addresses (92,273 with delivery-related information) | Confirmed leak | contractor / third-party service | none | [notice](https://www.sega.co.jp/release/261109_1.html) |
| 577 | 2026-11-09 | Nitori Holdings (company-managed system; Nitori Net and official Nitori shops on e-commerce malls) | up to 37.62 million records (no breakdown given) | Possible leak (up to) | unauthorised access (vector not disclosed) | none | [notice](https://www.nitorihd.co.jp/news/items/2b702dbe4d438f7fef74945d68e5bd27_3.pdf) |
| 578 | 2026-11-09 | Sharefull (internal management system of the gig-work app "Sharefull") | up to approx. 7.5 million individual accounts; up to approx. 7,500 companies | Possible leak (up to) | unauthorised access (vector not disclosed) | none | [notice](https://sharefull.com/information/9480/) |
| 579 | 2026-11-09 | Sumitomo Life Insurance ("Sumitomo Life Vitality trial / corporate" and "Vitality Smart" incl. employee-benefit type; contractor NTT DATA) | approx. 80,000 customers (of whom approx. 1,000 had partially masked credit card numbers leaked) | Confirmed leak | contractor / third-party service | none | [notice](https://www.sumitomolife.co.jp/news/detail/newsrelease_261109.html) |
| 580 | 2026-11-09 | Credit Saison ("Eraberu Gold Yutai" benefits for SAISON GOLD Premium members; system used by a contractor of partner Benefit One) | 198,660 people in total (excluding duplicates) | Confirmed leak | contractor / third-party service | none | [notice](https://www.saisoncard.co.jp/customer-support/information/20261109/) |
| 581 | 2026-11-09 | OPEN DOOR Inc. (travel comparison site "Travelko" website; e-mail newsletter subscribers) | 381,926 records | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.opendoor.co.jp/shared/pdf/20261109_info.pdf) |
| 582 | 2026-11-09 | Manbou Co., Ltd. (e-mail newsletter; e-mail delivery service of Arara used by its contractor) | up to approx. 10,100 records | Leak (as titled); no secondary damage confirmed | contractor / third-party service | none | [notice](https://www.jrkyushu.co.jp/common/inc/news/newtopics/__icsFiles/afieldfile/2026/11/09/20261109_Apology_Regarding_the_Email_Address_Leak_Due_to_Unauthorized_Access.pdf) |
| 583 | 2026-11-09 | Kanagawa University (authentication infrastructure; MNS accounts) | Not stated | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.kanagawa-u.ac.jp/news/article0101_04968) |
| 584 | 2026-11-09 | Shikoku Create Association (website inquiry and job-application forms) | 146 form submissions (124 inquiry, 22 job application) from 92 people | Possible leak | vulnerability | none | [notice](https://www.sk-create.jp/archives/9323) |

(Added 14 November 2026)
260 rows (585–844) were added on 14 November 2026: 24 from the pending list, 128 disclosed 10–13 November 2026, and 108 disclosed 7 September – 9 November that earlier additions had missed. The table of 77 rows added on 10 November is left as it was, and the new rows follow below; the seven tables together match the 844 rows of `data/registry.json`. IDs follow publication date, with no meaning to the order within a day.

As in the fifth edition, AI agents were used to find candidates, draft rows, and retrieve and check the primary notices. The results of seven agents, split by date and role (10–11 November; 12–14 November; rows missed for 3–9 November; the pending retry; follow-ups to existing rows; and two groups of first notices missed, found through follow-ups), were merged and de-duplicated by primary URL. Candidates were found through the monthly list of the aggregator jouhourouei.clipmaster.jp and press reports. Retrieval was by WebFetch only, so some PDFs could not be read in full; notes marked "未確認" or "逐語未確認" contain extracts not confirmed against the original. Notices of 14 November were not yet captured at the time of the work (morning of 14 November). Thirty of the 260 rows (the 16 largest and 14 at random) were re-checked against the primary notices by a separate AI agent that had not seen the drafts; one value was corrected (724), and eight rows received notes or were kept as classified. The other 230 rows were not re-checked.

Rows on the boundary of the admission rule, for the author to decide: rows whose first notice disclosed a possible leak and whose follow-up said no leak was confirmed (Japanese Red Cross Tokyo Chapter, Toho Holdings, Yamagata Prefecture, Toyama Prefecture "Shukatsu Line Toyama", Kyoto Lifelong Active Creative Center); a row whose first notice mentioned neither an external attack nor personal data (Osaka Metropolitan University; published is the first notice of 2 October, the leak was confirmed in the fifth notice of 21 October); rows whose notice gives no date, filled with the page's update date or the aggregator's first-seen date (Ise, Nasushiobara, Higashiosaka, Nagareyama, Nagakute, Omura, Otofuke, Shima and others); notices outside the organisation's own domain (589 Arcadia's official blog, Makihiroshige Atelier's shop blog); rows whose count is the whole chain's figure (629 Nagakute for TKC, the Kanagawa municipal employees' mutual aid association for plus Baton); and rows overlapping existing rows (the Kanagawa towns' joint information system association and towns 410, 412, 415, 419, 460; Hino and Hachioji for a co-hosted event; Kyoto City and Kyoto Art Center).

### The 260 rows added on 14 November 2026

| ID | Published | Organisation | Scale (as stated, original unit) | Status | Vector | AI mentioned | Primary source |
|---|---|---|---|---|---|---|---|
| 585 | 2026-09-07 | Institute of Science Tokyo (information infrastructure) | Not stated (scope under investigation) | Suspected leak | unauthorised access (vector not disclosed) | none | [notice](https://www.isct.ac.jp/ja/news/mrep3c3mj6bx) |
| 586 | 2026-09-29 | UNIRITA (in-house document management system, SaaS) | approx. 51,000 records (personal information of customers' employees and external contacts); approx. 910 records (own employees incl. former); approx. 6,100 records (contract information); approx. 370 records (authentication information); approx. 2,500 records (other) | Confirmed leak (data stolen and published by attacker) | unauthorised access (vector not disclosed) | none | [notice](https://www.unirita.co.jp/news/2026/media_20260929.html) |
| 587 | 2026-10-02 | Osaka Metropolitan University (university IT infrastructure; terminal of NEC's subcontractor and NEC-managed cloud storage) | approx. 170,000 persons' personal data (students and staff), of which approx. 1,400 persons' highly sensitive data (from NEC-managed cloud storage etc.); separately approx. 130,000 records in the university's own academic systems flagged as possibly leaked | Confirmed leak from NEC/subcontractor side; possible leak from the university's own systems | contractor / third-party service | none | [notice](https://www.omu.ac.jp/news/12123) |
| 588 | 2026-10-06 | Koike Sanso Kogyo (company servers) | No count given | Possible leak (data exfiltration recognized; personal data involvement under investigation) | unauthorised access (vector not disclosed) | none | [notice](https://koike-japan.com/pages/1?detail=1&b_id=206&r_id=524) |
| 589 | 2026-10-13 | Arcadia (disaster-information delivery "SpeeCAN RAIDEN", "NET119" emergency reporting system, "119RAIDEN", etc.) | approx. 3,136,000 email addresses, approx. 105,000 phone numbers, approx. 15,000 fax numbers (estimates; second report) | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://raiden.site.ktaiwork.jp/archives/4597) |
| 590 | 2026-10-19 | Papyless (e-book store "Renta!") | Not stated ("some customers") | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www2.jpx.co.jp/disc/36410/140120261019552777.pdf) |
| 591 | 2026-10-21 | Oita Prefecture ('Oita child-rearing support passport'; blastmail used by website operator QTmedia) | 8,218 records confirmed leaked | Confirmed leak | contractor / third-party service | none | [notice](https://www.pref.oita.jp/soshiki/12520/kosodateouen-passport3.html) |
| 592 | 2026-10-22 | Yamagata Prefecture (two prefectural email newsletters; Rakus Lite Cloud's 'blastmail') | No count given | Possible leak (initial); follow-up: no leak confirmed for prefecture-operated lists | contractor / third-party service | none | [notice](https://www.pref.yamagata.jp/documents/54937/mailmagazine_press.pdf) |
| 593 | 2026-10-22 | Toyama Prefecture ('Shukatsu Line Toyama' and 'Young Job Toyama' email delivery; Rakus Lite Cloud's 'blastmail') | Registered at 22 Oct: 4,278 persons and 1,490 companies (Shukatsu Line Toyama); 1,143 companies (Young Job Toyama) — scope of possible leak, not confirmed counts | Possible leak (initial); follow-up: no evidence of leakage for Shukatsu Line Toyama | contractor / third-party service | none | [notice](https://www.pref.toyama.jp/130321/sangyou/roudou/roudoukoyou/08uij.html) |
| 594 | 2026-10-23 | Japanese Red Cross Society Tokyo Chapter ("NT (Nisseki Tokyo) NEWS" newsletter; contractor Rakus Lite Cloud's "blastmail") | Not stated | Initially possible leak; final report (Nov 11) states no leak | contractor / third-party service | none | [notice](https://www.jrc.or.jp/chapter/tokyo/news/2026/1023_056631.html) |
| 595 | 2026-10-23 | G-Yet (Mac-House email newsletter; contractor Rakus Lite Cloud's 'blastmail') | Count under review (initial notice) | Possible leak | contractor / third-party service | none | [notice](https://assets.minkabu.jp/news/article_media_content/urn:newsml:tdnet.info:20261023555550/140120261023555550.pdf) |
| 596 | 2026-10-23 | Toho Holdings (subsidiary e-Healthcare's email delivery; Rakus Lite Cloud's 'blastmail') | approx. 8,000 records of physician names and email addresses (incl. approx. 1,000 for Byoin Navi PR service); approx. 1,000 medical institution names; approx. 7,000 survey admin URLs; dates of birth of approx. 30 physicians (initial); follow-up found no trace of leakage | Possible leak (initial); follow-up: no evidence of leakage found | contractor / third-party service | none | [notice](https://www2.jpx.co.jp/disc/81290/140120261023555469.pdf) |
| 597 | 2026-10-23 | Kyoto Prefecture Lifelong Active Creative Center (email delivery to trainees; Rakus Lite Cloud's 'blastmail') | 15,576 persons' data possibly taken (initial); follow-up: no leak | Possible leak (initial); follow-up: confirmed no leak | contractor / third-party service | none | [notice](https://recurrent-kyoto.com/news/8826/) |
| 598 | 2026-10-28 | Shibuya City (online services "Shibuya My Portal" and facility reservation system) | 218 user accounts with confirmed leak of personal information (of which 217 accounts tampered with and 5 accounts misused) | Confirmed leak (plus tampering and account misuse) | vulnerability | none | [notice](https://www.city.shibuya.tokyo.jp/kusei/koho/shibuya-portal/unauthorized_access_202610.html) |
| 599 | 2026-10-29 | IRIS PLAZA (official online store "Iris Plaza"; external cloud service used by the company) | approx. 7.7 million people's data (approx. 5.8 million members, approx. 1.9 million non-members) | Possible leak | contractor / third-party service | none | [notice](https://www.irisohyama.co.jp/news/2026/1105.pdf) |
| 600 | 2026-11-02 | Mitsui Direct General Insurance (roadside-service contractor Prestige Core Solution) | Not stated | Possible leak (reported by contractor) | contractor / third-party service | none | [notice](https://www.mitsui-direct.co.jp/information/20261102.html) |
| 601 | 2026-11-02 | Ryobi Holdings (Ryobi Bus email newsletter; external service Arara "repica") | 43,221 records (cumulative) | Confirmed leak | contractor / third-party service | none | [notice](https://www.ryobi-holdings.jp/bus/news-kousoku/20261102/) |
| 602 | 2026-11-02 | LightUp Shopping Club (email delivery via a marketing platform; Arara "repica") | 43,506 email addresses (corrected from 43,605 on Nov 9) | Confirmed leak | contractor / third-party service | none | [notice](https://www.lightup.jp/info-261102.html) |
| 603 | 2026-11-02 | Bank of The Ryukyus (email delivery service provided by contractor; Arara "repica") | 96,477 email addresses (second report) | Confirmed leak | contractor / third-party service | none | [notice](https://www.ryugin.co.jp/corporate/news/100767/) |
| 604 | 2026-11-02 | Shiki City (email sending for the My Number Card issuance reservation system; ARARA's "ARARA Message" used by the contractor) | Not stated (whether city data is included is under investigation; contractor-wide: up to 2,230,812 email addresses leaked) | Possible leak (inclusion of city data under investigation) | contractor / third-party service | none | [notice](https://www.city.shiki.lg.jp/soshiki/13/44759.html) |
| 605 | 2026-11-02 | Coffee Style UCC (LINE integration service; contractor Sonicmoov's 'COMSBI Enterprise Platform') | 449,442 LINE user IDs; 172,309 LINE nicknames; 6,116 email addresses (initial); plus up to 175,372 persons' LINE profile information (2nd report) | Confirmed leak (initial items); possible acquisition of additional profile data (2nd report) | contractor / third-party service | none | [notice](https://www.coffeestyleucc.co.jp/news2611/) |
| 606 | 2026-11-03 | ENSAPIA Tokyo (online game portal "Hange" server) | 61,962 hashed passwords; 51,025 email addresses; 28,251 birth dates; 2,994 name/address/phone records; 36,545 external-service-ID email addresses; partial card numbers (masked) "2.961" as printed; 6 security codes; 97 phone numbers; 2 cardholder names; 97 other email addresses | Confirmed leak (4th report) | unauthorised access (vector not disclosed) | none | [notice](https://ensapia-tokyo.com/news/topics/id=21412/) |
| 607 | 2026-11-03 | Higashimurayama Regional Promotion Organization (local currency "Ain Pay" email delivery; external service Arara "Arara Message"; contractor Finovalley) | Not stated | Possible (no leak confirmed as of announcement) | contractor / third-party service | none | [notice](https://einpay.jp/news/513/) |
| 608 | 2026-11-03 | Osaka City (email delivery for the Osaka City Administrative Online System; Arara's email service used by system provider TKC) | Not stated (under investigation, including whether any leak occurred) | Possible leak (reported by the system provider) | contractor / third-party service | none | [notice](https://www.city.osaka.lg.jp/hodoshiryo/ictsenryakushitsu/0000690714.html) |
| 609 | 2026-11-03 | Iwamizawa City (press-release email delivery system; website maintenance contractor WingArc NEX / Arara "Arara Message") | 26 registrations (including 2 internal city addresses) | Confirmed leak | contractor / third-party service | none | [notice](https://www.city.iwamizawa.hokkaido.jp/material/files/group/1/20261103-2.pdf) |
| 610 | 2026-11-04 | Tokyo Zoological Park Society (metropolitan zoos/aquarium tickets sold via "asoview!"; external mail service used by asoview, Arara) | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.tokyo-zoo.net/news/13874/index.html) |
| 611 | 2026-11-04 | Adventure World (park tickets sold via "asoview!"; external mail service used by asoview, Arara) | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.aws-s.com/topics/detail?id=top4775) |
| 612 | 2026-11-04 | Nagano Prefectural Credit Union (website input forms; via server of website maintenance contractor) | 2,923 form records (number containing personal data under investigation) | Possible leak | contractor / third-party service | none | [notice](https://system.naganokenshin.jp/7fBZWEs/api/v1/files/zfiles/4ef295bcc0794ad0643c40a31e8d907035e877e1-1793776530216.pdf) |
| 613 | 2026-11-04 | Idealog (development/test environment of "Kaijo Best Search" and "Supenavi") | Not stated (under investigation) | Possible (leak not confirmed) | misconfiguration | none | [notice](https://idealog.co.jp/news/unauthorized-access-20261104) |
| 614 | 2026-11-04 | Lawson Entertainment ("Enta GO" venue merchandise system and "LAWSON DO! SPORTS" entry site; Dentsu Soken "FACERE" and "iPLAss") | Enta GO: up to 12,196 persons; LAWSON DO! SPORTS: 57 files, 27,908 persons | Possible leak | contractor / third-party service | none | [notice](https://www.ent.lawson.co.jp/wp/wp-content/uploads/2026/11/20261104.pdf) |
| 615 | 2026-11-04 | Toda City ("Iitoda Mail" and Toda smart application system email delivery; TKC / WingArc NEX / Arara) | Not stated (under confirmation) | Possible leak | contractor / third-party service | none | [notice](https://www.city.toda.saitama.jp/soshiki/154/joho-security-incident.html) |
| 616 | 2026-11-04 | Higashiosaka City (electronic application system; external email delivery service used by provider) | Not stated (under confirmation) | Possible leak | contractor / third-party service | none | [notice](https://www.city.higashiosaka.lg.jp/0000045459.html) |
| 617 | 2026-11-04 | Kasukabe City (safety information mail "Kasukabe"; external service provider) | 17,481 email addresses (registered as of end of October) | Confirmed leak (reported by provider) | contractor / third-party service | none | [notice](https://www.city.kasukabe.lg.jp/soshikikarasagasu/citysaleskohoka/gyomuannai/5/39086.html) |
| 618 | 2026-11-04 | Noritake (Noritake tableware official online shop newsletter; Arara "repica" used by provider) | 40,575 recipient email addresses | Confirmed leak (reported by provider) | contractor / third-party service | none | [notice](https://www.noritake.co.jp/news/detail/743/) |
| 619 | 2026-11-04 | Tokyo Kantei (email delivery; contractor Arara "Arara Message") | 3,276 records (email addresses; second report) | Leak reported by contractor (3,276 target addresses in second report) | contractor / third-party service | none | [notice](https://www.kantei.ne.jp/news/info/9656/) |
| 620 | 2026-11-04 | Osaka Prefecture (Osaka Prefecture Administrative Online System; external email delivery service used by the system provider) | Not stated (under investigation, including whether any leak occurred) | Possible leak (reported by the system provider) | contractor / third-party service | none | [notice](https://www.pref.osaka.lg.jp/hodo/fumin/o050180/prs_00001.html) |
| 621 | 2026-11-04 | Koriyama City (online application service and My Number Card reservation system; TKC / Arara "Arara Message") | approx. 32,600 registered user accounts (individuals and businesses) and approx. 20,000 reservation records (as of Nov 4; affected number under investigation) | Possible leak | contractor / third-party service | none | [notice](https://www.city.koriyama.lg.jp/uploaded/attachment/132827.pdf) |
| 622 | 2026-11-04 | Fujiidera City (email delivery service used for online counters, etc.; system provider TKC / Arara) | Not stated (under investigation) | Possible leak | contractor / third-party service | none | [notice](https://www.city.fujiidera.lg.jp/topics/21580.html) |
| 623 | 2026-11-04 | OPENDOOR ("Travelko" email newsletter; delivery contractor Arara) | 318,495 records | Leak reported by contractor (specific addresses still being identified) | contractor / third-party service | none | [notice](https://www.opendoor.co.jp/shared/pdf/20261104_info.pdf) |
| 624 | 2026-11-05 | Asahi Metal Fine (email delivery of e-commerce platform "makeshop"; Arara "Arara Message") | up to 5,865 records (after 11/9 update) | Possible leak | contractor / third-party service | none | [notice](https://www.asahimetalfine.com/news/860) |
| 625 | 2026-11-05 | Otofuke Town (email service "Arara Message" used by My Number card appointment system) | up to 8,217 records (under investigation) | Possible leak (up to) | contractor / third-party service | none | [notice](https://www.town.otofuke.hokkaido.jp/kurashi/mynumber/kojinjyouhou.html) |
| 626 | 2026-11-05 | Fanplus (EBiDAN official site; external email service Arara "Arara Message" used by operator Fanplus) | Not stated | Possible (whether site members are included not yet known) | contractor / third-party service | none | [notice](https://ebidan.jp/news/detail/50001429) |
| 627 | 2026-11-05 | Kanagawa Towns and Villages Information System Joint Association (email service of member bodies' smart application and My Number card appointment systems; TKC / Arara) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://system.c2-kanagawa.jp/wp-content/uploads/sites/5/2026/11/%E6%83%85%E5%A0%B1%E6%BC%8F%E3%81%88%E3%81%84%E3%81%AE%E5%8F%AF%E8%83%BD%E6%80%A7%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6.pdf) |
| 628 | 2026-11-05 | Nagareyama City (email service of My Number card appointment system; contractor TKC / Arara "Arara Message") | Not stated (under confirmation) | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.city.nagareyama.chiba.jp/life/1000371/1056143.html) |
| 629 | 2026-11-05 | Nagakute City (My Number card appointment system completion emails; TKC's delivery contractor Arara) | up to 2,230,812 records (reportedly TKC-wide figure) | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.city.nagakute.lg.jp/soshiki/somubu/shiminka/1/1/mynumber/28224.html) |
| 630 | 2026-11-05 | Omura City (digital local currency app "Yudepi"; external email service Arara "Arara Message") | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.city.omura.nagasaki.jp/digital/kurashi/dx/shiawase/yudepi_fuseiacsess.html) |
| 631 | 2026-11-05 | Okinawa Prefecture (Okinawa energy-saving appliance campaign secretariat; Arara email service) | 503 personal email addresses (possible); later report reportedly 4,670 (unverified) | Possible leak | contractor / third-party service | none | [notice](https://okinawa-shoene.jp/oshirase_syousai.php?id=18) |
| 632 | 2026-11-05 | Shinagawa Prince Hotel (external email service Arara used by e-ticket seller asoview) | Not stated | Possible leak (reported by contractor) | contractor / third-party service | none | [notice](https://www.princehotels.co.jp/file.jsp?id=528509) |
| 633 | 2026-11-05 | Kamakura Prince Hotel (external email service Arara used by e-ticket seller asoview) | Not stated | Possible leak (reported by contractor) | contractor / third-party service | none | [notice](https://www.princehotels.co.jp/file.jsp?id=528480) |
| 634 | 2026-11-05 | Kainan City (My Number card appointment system; Arara, email contractor of TKC) | Not stated (under investigation) | Possible leak | contractor / third-party service | none | [notice](https://www.city.kainan.lg.jp/kakubusho/soumubu/shiminka/oshirase/8934.html) |
| 635 | 2026-11-05 | Matsumoto University (safety confirmation system "ANPIC"; contractor's external mail provider Arara) | Not stated | Confirmed leak | contractor / third-party service | none | [notice](https://www.matsumoto-u.ac.jp/news2026/11/37140.php) |
| 636 | 2026-11-05 | Japan Post (contractor CBcloud's dispatch system "PickGo" for pickup/delivery) | 1,672 full names; 2,091 surnames only | Confirmed leak | contractor / third-party service | none | [notice](https://www.post.japanpost.jp/newsrelease/pressrelease/414336381813.html) |
| 637 | 2026-11-05 | Iga City (My Number Card issuance reservation and management system; contractor Officemation / TKC / Arara) | Not stated | Possible leak (reported) | contractor / third-party service | none | [notice](https://www.city.iga.lg.jp/0000014607.html) |
| 638 | 2026-11-05 | Okinawa Prefecture (facilities in Okinawa Commemorative National Government Park, Ocean Expo and Shurijo areas; designated manager Okinawa Churashima Foundation / Asoview / Arara "Arara Message") | Not stated | Leak (reported; park users possibly included) | contractor / third-party service | none | [notice](https://www.pref.okinawa.jp/machizukuri/park/1041852.html) |
| 639 | 2026-11-05 | Fukui City (ticket buyers of Seiren Planet, branch of the Museum of Natural History; email system used by ticket seller Asoview) | Not stated | Possible leak (notified by contractor) | contractor / third-party service | none | [notice](https://www.city.fukui.lg.jp/kyoiku/gakusyu/museum/p073537.html) |
| 640 | 2026-11-05 | Nakanoshima Museum of Art, Osaka (email newsletter; Arara, the delivery contractor of Asoview! and ARTPASS) | Not stated (affected addresses not yet identified) | Confirmed leak (affected addresses not yet identified) | contractor / third-party service | none | [notice](https://nakka-art.jp/news/20261105/) |
| 641 | 2026-11-05 | Ogaki Kyoritsu Bank (card loans "THE Maximum", "Haikurasu Pocket", "Haikurasu Big"; partner SMBC Consumer Finance) | Not stated (scope under investigation) | Confirmed leak (partial) | contractor / third-party service | none | [notice](https://www.okb.co.jp/assets/pdf/archive/2026/20261105-03.pdf) |
| 642 | 2026-11-05 | GMO TECH (contact forms of the former GMO TRYHATCH corporate site and "Growth MEO"; contractor Studio) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://gmotech.jp/news_release/?p=13481) |
| 643 | 2026-11-05 | GMO MAKESHOP (contact form of the GMO Make Appli, formerly anect, corporate site; contractor Studio) | Not stated | Possible leak (treated as obtained by the provider) | contractor / third-party service | none | [notice](https://www.makeshop.co.jp/news/info/2026-11-05/) |
| 644 | 2026-11-06 | Digital Hollywood (prospectus requesters; Arara email system used by contractor) | 10,958 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.dhw.co.jp/news261106.html) |
| 645 | 2026-11-06 | Tokorozawa City (37th Tokorozawa City Marathon entries; Dentsu Soken "iPLAss" used by Lawson Entertainment's "LAWSON DO! SPORTS") | 178 persons (89 applicants + 89 emergency contacts) | Possible leak (reported by contractor) | contractor / third-party service | none | [notice](https://www.city.tokorozawa.saitama.jp/tokoronews/press/r8/11gatu/sports.html) |
| 646 | 2026-11-06 | JR West Hotels ("Kaijo Best Search" management system; operator Idealog's dev/test environment) | Not stated (under investigation) | Possible leak | contractor / third-party service | none | [notice](https://jrwest-hotels.jp/news/2192/) |
| 647 | 2026-11-06 | Shiro (SHIRO online store; "GMO Atobarai"; Arara "Arara Message" used by GMO Payment Service's contractor Martial Arts law firm) | 43 persons (email only) and 8 persons (email, name, billing details) | Leak (per title) | contractor / third-party service | none | [notice](https://www.shiro-shiro.pro/ec/sp?F=9050) |
| 648 | 2026-11-06 | PAL (PAL CLOSET online store; "GMO Atobarai" and "Yuru-PAL Barai"; Arara "Arara Message" used by GMO Payment Service's contractor Martial Arts law firm) | GMO Atobarai: 364 (email only); Yuru-PAL Barai: 125 (email only); plus records incl. names (reportedly 24 and 3; total 516, unverified) | Confirmed leak | contractor / third-party service | none | [notice](https://www.palcloset.jp/display/article/detail/?acd=261106all_004&b=&bg=outlet) |
| 649 | 2026-11-06 | cyma Yellow Hat (bicycle e-commerce "cyma" emails/newsletters; contractor Arara "Arara Message") | up to 79,107 records | Possible leak (up to) | contractor / third-party service | none | [notice](https://cyclemarket.jp/static/news/2026110602/) |
| 650 | 2026-11-06 | Ministry of Health, Labour and Welfare (antimicrobial resistance surveillance system JANIS; operated by contractor JIHS) | up to 21,023 users' records | Possible leak (up to) | contractor / third-party service | none | [notice](https://janis.mhlw.go.jp/) |
| 651 | 2026-11-06 | Kurihara City (smart application system "Dokodemo Madoguchi"; external email service Arara "Arara Message" used by operator TKC) | 2,379 individual accounts; 111 business accounts | Possible leak | contractor / third-party service | none | [notice](https://www.kuriharacity.jp/w067/020/070/PAGE000000000000012648.html) |
| 652 | 2026-11-06 | Chiba Kogyo Bank (email delivery service provided via contractor; Arara) | 171,260 email addresses | Confirmed leak (reported by contractor) | contractor / third-party service | none | [notice](https://www.chibakogyo-bank.co.jp/news/important/of_ja_important_2.html) |
| 653 | 2026-11-06 | Shin-Yokohama Prince Hotel (external email service Arara used by e-ticket seller asoview) | Not stated | Possible leak (reported by contractor) | contractor / third-party service | none | [notice](https://www.princehotels.co.jp/file.jsp?id=528588) |
| 654 | 2026-11-06 | Snow Brand Beanstalk (official online shop; operator Takeda Printing / GMO MakeShop "MakeRepeater" / Arara) | Not stated (under review) | Possible leak | contractor / third-party service | none | [notice](https://www.beanstalksnow.co.jp/news/8498/) |
| 655 | 2026-11-06 | Akita Northern Happinets (email delivery to "Club Happinets" fan-club members; contractor Axel Entermedia's subcontractor ARARA) | 41 records (39 members: email address only; 2 members: email address and name); initial notice: up to 9,530 members possibly affected | Confirmed leak (41 records; initially possible, up to 9,530 members) | contractor / third-party service | none | [notice](https://northern-happinets.com/news/detail/id=23087) |
| 656 | 2026-11-06 | Avanti Staff (guidance emails to assigned staff and job-introduction emails to registrants; contractor ARARA's email delivery service) | 78,310 records (email address only) and 12 records (name and email address); counts may include duplicate addresses and do not represent the number of people | Confirmed leak (impact on safety-confirmation system under investigation) | contractor / third-party service | none | [notice](https://www.avantistaff.com/staff/topics/detail/139) |
| 657 | 2026-11-06 | Maki Hiroshige Atelier (gomme official online shop; 'Arara Message' used for makeshop newsletters) | 2,585 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://gomme.xsrv.jp/blog/%E3%80%90%E9%87%8D%E8%A6%81%E3%80%91%E5%A4%96%E9%83%A8%E3%83%A1%E3%83%BC%E3%83%AB%E9%85%8D%E4%BF%A1%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB/) |
| 658 | 2026-11-07 | Kyoei Seicha (online shop "Morihan tea & coffee"; mail delivery platform of a formerly used CRM service, Arara "Arara Message") | 6,796 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.tea-and-coffee.shop/view/news/20261107003443) |
| 659 | 2026-11-08 | Sesion Suginami (designated manager; e-ticketing service "teket" used for event tickets) | 452 persons (cumulative) | Possible leak | contractor / third-party service | none | [notice](https://www.sesion-suginami.jp/cms/wp-content/uploads/2026/11/20261108-1.pdf) |
| 660 | 2026-11-08 | Tokyo Metropolitan Foundation for Sports and Culture (Smile Sports program; external application site "teket") | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://tef.or.jp/news/teket-1.html) |
| 661 | 2026-11-08 | Sapporo Science Center (event ticketing via "teket") | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.ssc.slp.or.jp/news/single/153) |
| 662 | 2026-11-08 | Tsukuba Expo '85 Memorial Foundation (Tsukuba Expo Center; event ticketing via "teket") | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.expocenter.or.jp/topics/detail/id=5520) |
| 663 | 2026-11-08 | Kyoto Modern Architecture Festival Executive Committee (ticketing site "teket") | Under investigation | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://kyoto.kenchikusai.jp/2026/11/08/teket-2/) |
| 664 | 2026-11-08 | LF Concert (ticketing site "teket") | Not stated | Leak incident at contractor; scope under confirmation | contractor / third-party service | none | [notice](https://music.lflc.jp/news/cyj6nq7ouqf6/) |
| 665 | 2026-11-08 | Kurashiki City Tamashima Civic Exchange Center (contracted e-ticketing service "teket") | Not stated | Confirmed leak | contractor / third-party service | none | [notice](https://www.tamashima-cec.jp/archives/10401/) |
| 666 | 2026-11-08 | Hockey Japan League (match ticketing via "teket") | Not stated | Leak confirmed at teket; league customers possibly included | contractor / third-party service | none | [notice](https://hjl-hockey.tv/news/2026/11/08/30411/) |
| 667 | 2026-11-08 | Sapporo Lifelong Learning Center Chieria (ticketing via "teket") | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](http://chieria.slp.or.jp/news/2026/2026-1108-1923-18.html) |
| 668 | 2026-11-09 | Yojiya Group (member information management system; member data API) | 131,557 persons confirmed; potential maximum 134,344 persons | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.yojiya.co.jp/261109-01) |
| 669 | 2026-11-09 | Saitama Prefecture (Saitama Prefectural Museum of Literature e-tickets; Arara "Arara Message" used by contractor asoview) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.pref.saitama.lg.jp/f2216/news/page/news2026110901.html) |
| 670 | 2026-11-09 | Japan Triathlon Union (event entries; Lawson Entertainment "LAWSON DO! SPORTS"; Dentsu Soken "iPLAss") | 3,609 entrants and 2,831 non-applicants (6,440 persons) | Possible leak | contractor / third-party service | none | [notice](https://www.jtu.or.jp/news/2026/11/09/88043) |
| 671 | 2026-11-09 | Neo Career (care staffing service "Nice! Kaigo" emails; Arara "Arara Message") | Not stated (under confirmation) | Confirmed leak | contractor / third-party service | none | [notice](https://www.neo-career.co.jp/news/article_26486) |
| 672 | 2026-11-09 | Giken (one business server; ransomware) | approx. 3,200 persons | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.giken.com/ja/news/notices/notice_20261109/) |
| 673 | 2026-11-09 | Tokyo Metropolitan Government (Bureau of Industrial and Labor Affairs; Arara "Arara Message" used by Tokyo Convention & Visitors Bureau's contractor) | 132 email-only records; 2 name+email records | Confirmed leak | contractor / third-party service | none | [notice](https://www.sangyo-rodo.metro.tokyo.lg.jp/documents/d/sangyo-rodo/2026-11-09-193909-968) |
| 674 | 2026-11-09 | Lafool (legacy system file storage of organizational survey service "Lafool Survey") | 182 companies, 24,232 persons (may change) | Confirmed (data obtained) | misconfiguration | none | [notice](https://corp.lafool.co.jp/news/information/172/) |
| 675 | 2026-11-09 | T-PEC ("plus Baton" member newsletter; Arara "Arara Message" used in DataX service) | 234,753 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.t-pec.co.jp/news/topics/20261109/) |
| 676 | 2026-11-09 | Furukawa Electric Health Insurance Society ("plus Baton" email delivery; contractor T-PEC) | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.furukawadenko-kenpo.com/2026/11/09/%E5%81%A5%E5%BA%B7%E6%83%85%E5%A0%B1%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%80%8Cplus-baton%E3%80%8D%E3%81%AE%E3%83%A1%E3%83%BC%E3%83%AB%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E6%B5%81%E5%87%BA%E3%81%AB/) |
| 677 | 2026-11-09 | Nishinihon Packaging Health Insurance Society ("plus Baton" member site; T-PEC) | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://packagingkenpo.jp/pop/detail372) |
| 678 | 2026-11-09 | Kanagawa Municipal Employees Mutual Aid Association ("plus Baton" email delivery; contractor T-PEC) | 234,753 records (plus Baton overall) | Confirmed leak (email addresses) | contractor / third-party service | none | [notice](https://www.kanagawa-kyosai.jp/pop/detail712) |
| 679 | 2026-11-09 | PEPPY (cloud data storage used by online shops "Peppy" and "Peppy Vet") | 6,503 veterinary clinics (possibly affected; incl. withdrawn) | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://peppy.co.jp/%E5%BD%93%E7%A4%BE%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%B8%E3%81%AE%E4%B8%8D%E6%AD%A3%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B9%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%8A%E8%A9%AB%E3%81%B3%E3%81%A8/) |
| 680 | 2026-11-09 | Mitsui Home (LINE official account "Mitsui Home Club"; former contractor Sonicmoov's system) | 4 email addresses confirmed; LINE profile data (count not stated) | Confirmed (4) / possible (LINE profile data) | contractor / third-party service | none | [notice](https://www.mitsuihomeclub.com/notice/detail.php?id=50&type=im) |
| 681 | 2026-11-09 | Ome Marathon Foundation (59th Ome Marathon entries; development platform used by Lawson Entertainment "LAWSON DO! SPORTS") | 110 persons | Possible leak | contractor / third-party service | none | [notice](https://www.ohme-marathon.jp/news/jimukyoku/2026/11/09/9485) |
| 682 | 2026-11-09 | Shima City (appointment management system; contractor Officemation / provider TKC / Arara) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.city.shima.mie.jp/kakuka/shiminseikatsubu/shiminka/9885.html) |
| 683 | 2026-11-09 | Welby (email delivery contractor Arara "Arara Message") | 163,316 email addresses (as reported by Arara) | Leak (email addresses) | contractor / third-party service | none | [notice](https://welby.jp/category/news/261109174039.html) |
| 684 | 2026-11-09 | TV Shin-Hiroshima (email delivery incl. flower subscription "Lohas Flower"; Arara "Arara Message") | 5,192 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.tss-tv.co.jp/archives/001/202611/eb9986e10c858c3cf330dfcf4591f89631da65960e177becec25b50252774a40.pdf) |
| 685 | 2026-11-09 | Relo Club ("Relo Engagemental Survey" sold under OEM from Lafool) | 4,741 persons (33 client companies) | Confirmed leak | contractor / third-party service | none | [notice](https://www.reloclub.jp/news/20261109) |
| 686 | 2026-11-09 | Kanagawa Prefecture ("Kanagawa Re-Koten Project"; e-ticketing service "teket" used by contractor Dragon) | Under review by teket | Possible leak | contractor / third-party service | none | [notice](https://www.pref.kanagawa.jp/docs/yi4/prs/r7861888.html) |
| 687 | 2026-11-09 | Fukushima Prefecture (prefecture-hosted event "Fukushima Sake, Miso & Soy Sauce Festival"; e-ticket operator teket) | Not stated | Leak (as reported by teket) | contractor / third-party service | none | [notice](https://www.pref.fukushima.lg.jp/sec/32031c/teket.html) |
| 688 | 2026-11-09 | Osaka City (lectures etc. hosted by Osaka Museum of History; e-ticketing service "teket") | Under confirmation | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.city.osaka.lg.jp/hodoshiryo/keizaisenryaku/0000691211.html) |
| 689 | 2026-11-09 | Okazaki City (FY2023 Ieyasu Procession seat ticket sales; "teket") | Under confirmation | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.city.okazaki.lg.jp/shisei/koho/1006195/1006358/1017062/1017625.html) |
| 690 | 2026-11-09 | Ichinomiya City (Fire Department; 48th fire band concert e-ticketing contractor teket) | Not stated | Leak / possible leak | contractor / third-party service | none | [notice](https://www.city.ichinomiya.aichi.jp/shisei/houdouhappyo/1068631/1076554/1077440.html) |
| 691 | 2026-11-09 | Hino City (ticket sales for "Tanizo Family Concert" via "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://www.city.hino.lg.jp/kosodate/1008312/jidokan/1009226/1032419.html) |
| 692 | 2026-11-09 | Hachioji City ("Tanizo Family Concert" co-hosted with Hino City; "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://kosodate.city.hachioji.tokyo.jp/soshiki/kodomonoshiawaseka/3986.html) |
| 693 | 2026-11-09 | Kyoto Arts and Culture Association (Kyoto Art Center; event ticketing via "teket") | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.kac.or.jp/news/%E3%80%90%E3%81%8A%E8%A9%AB%E3%81%B3%E3%81%A8%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B%EF%BC%88%E7%AC%AC%E4%B8%80%E5%A0%B1%EF%BC%89%E3%80%91%E9%9B%BB%E5%AD%90%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E8%B2%A9/) |
| 694 | 2026-11-09 | Ishikawa Music Culture Promotion Foundation (Ishikawa Ongakudo; concert ticketing via "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://ongakudo.jp/notice-event/detail-5523/) |
| 695 | 2026-11-09 | Chuo University (AI and Data Science Center event registration via "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://www.chuo-u.ac.jp/aboutus/efforts/ai_and_ds/news/2026/11/89194/) |
| 696 | 2026-11-09 | Musashino Academia Musicae (ticketing system "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://www.musashino-music.ac.jp/news/info/2026-11-09/) |
| 697 | 2026-11-09 | Kunitachi College of Music (concert ticketing via "teket") | Not stated | Possible (whether own customers included not confirmed) | contractor / third-party service | none | [notice](https://www.kunitachi.ac.jp/NEWS/introduction/20261109_01.html) |
| 698 | 2026-11-09 | Japan Philharmonic Orchestra (some concerts ticketed via "teket") | Under investigation | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://japanphil.or.jp/news/20261109-2/) |
| 699 | 2026-11-09 | Nagoya Philharmonic Orchestra (concert ticketing via "teket") | Not stated | Leak incident at contractor (own customers not specified) | contractor / third-party service | none | [notice](https://www.nagoya-phil.or.jp/news/news_2026_11_09_140047) |
| 700 | 2026-11-09 | Pacific Philharmonia Tokyo (concert ticketing via "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://ppt.or.jp/information/news20261109/) |
| 701 | 2026-11-09 | Edo Tokyo Traditional Performing Arts Festival Executive Committee (some performances via "teket") | Not stated | Leak (as reported by teket) | contractor / third-party service | none | [notice](https://edotokyo-dentogeinosai.jp/news/news_teket/) |
| 702 | 2026-11-09 | meSquare (Office meSquare; online seminar registration via "teket") | Under investigation | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://me-square.com/?p=1431) |
| 703 | 2026-11-09 | Yokohama DeNA BayStars (event ticketing via "teket") | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://sp.baystars.co.jp/news/2026/11/1109_05.php) |
| 704 | 2026-11-09 | Amateur Radio Festival Executive Committee (Ham Fair admission tickets via "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://www.jarl.org/Japanese/2_Joho/2-5_info/info2026_1109.html) |
| 705 | 2026-11-09 | Tokyo Reiki Kogyo (event registration via "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://www.to-rei.jp/news/%E5%BC%8A%E7%A4%BE%E5%88%A9%E7%94%A8%E3%81%AE%E9%9B%BB%E5%AD%90%E3%83%81%E3%82%B1%E3%83%83%E3%83%88%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%80%8Cteket%E3%80%8D%E3%81%B8%E3%81%AE-%E4%B8%8D%E6%AD%A3/) |
| 706 | 2026-11-09 | Matsuyama Yushi ("Sumida Factory Autumn Open Factory 2026" registration via "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://www.matsuyama.co.jp/news/52458) |
| 707 | 2026-11-09 | Kyoto City (Culture and Arts Planning Division facilities; e-ticketing service "teket") | Under review | Leak reported (for one facility) | contractor / third-party service | none | [notice](https://www.city.kyoto.lg.jp/bunshi/page/0000360015.html) |
| 708 | 2026-11-09 | FC Fujizakura Yamanashi (ticketing via "teket") | Not stated | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://www.fujizakura-sc.jp/news/26348/) |
| 709 | 2026-11-09 | Nagoya City Cultural Promotion Agency (ticketing site "teket") | Under investigation | Leak (as announced by teket) | contractor / third-party service | none | [notice](https://www.bunka758.or.jp/news/headquarters/detail/_1_16.html) |
| 710 | 2026-11-09 | Setagaya Arts Foundation (Setagaya Lifestyle Design Center; workshop registration via "teket") | Not stated | Leak incident at contractor (own customers not specified) | contractor / third-party service | none | [notice](https://www.setagaya-ldc.net/news/485/) |
| 711 | 2026-11-09 | Niigata Prefecture Teachers' Mutual Aid Association (FY2026 cultural events; "teket" used by contractor) | up to 3,058 records (total event applicants; teket users are a subset) | Confirmed leak (as reported) | contractor / third-party service | none | [notice](https://www.sinkyogo.com/%E4%BA%92%E5%8A%A9%E4%BC%9A%E3%81%8B%E3%82%89%E3%81%AE%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B-1/%E5%A0%B1%E9%81%93%E7%99%BA%E8%A1%A8/) |
| 712 | 2026-11-09 | Yokohama Furusato History Foundation (event registration for foundation facilities via "teket") | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.yokohama-history.org/yokohama-history/937/) |
| 713 | 2026-11-09 | Chiba Dot (club ticketing via "teket") | Not stated | Leak incident at contractor (own customers not specified) | contractor / third-party service | none | [notice](https://chibadot.jp/topics/teket1109/) |
| 714 | 2026-11-09 | Minato City Sports, Culture and Health Foundation (registration for Minato arts network meeting via "teket") | Not stated | Possible leak (reported by contractor) | contractor / third-party service | none | [notice](https://www.kissport.or.jp/news/oshirase-teket_261109) |
| 715 | 2026-11-09 | Machida City (city event registrations via "teket") | Not stated | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.city.machida.tokyo.jp/shisei/koho/koho/announce/teket.html) |
| 716 | 2026-11-09 | NTT DATA (service for applications to Sumitomo Life "Vitality" trial/corporate and "Vitality Smart", operated under contract) | approx. 80,000 users (of whom approx. 1,000 had partially masked card numbers leaked) | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.nttdata.com/global/ja/news/release/2026/110900/) |
| 717 | 2026-11-10 | Ise City (My Number Card issuance reservation system; contractor Officemation / service provider TKC / Arara) | Not stated (under investigation by the system provider) | Possible leak | contractor / third-party service | none | [notice](https://www.city.ise.mie.jp/kurashi/koseki/mynumber/1021053.html) |
| 718 | 2026-11-10 | Sanko Techno (internal servers of Vietnamese subsidiary SANKO FASTEM (VIETNAM)) | 898 people (subsidiary-related persons) plus 10 officers/employees of the company and group companies; 1,348 Vietnamese business partners (companies) | Confirmed leak (published on dark web) | misconfiguration | none | [notice](https://www2.jpx.co.jp/disc/34350/140120261110571505.pdf) |
| 719 | 2026-11-10 | Toyama Prefectural University (safety-confirmation system ANPIC; Arara Message used by operator Avance System) | Not stated (email addresses of students and staff sent via ANPIC, Jul 1 to Oct 31, 2026) | Confirmed leak (as reported by the vendor) | contractor / third-party service | none | [notice](https://www.pu-toyama.ac.jp/tpu/wp-content/uploads/2026/11/bf304e0fdebab04ebfedd9902f0f79aa.pdf) |
| 720 | 2026-11-10 | Airu (CROSS POINT customer-management service; member-data API of one client company) | Not stated (members of one client company) | Confirmed (data obtained by a third party) | unauthorised login | none | [notice](https://www.ill.co.jp/info/261110/) |
| 721 | 2026-11-10 | Soft99 Corporation (official online shop) | up to 136,968 people | Possible leak (up to) | vulnerability | none | [notice](https://www.soft99.co.jp/important/detail/261110/) |
| 722 | 2026-11-10 | Nasushiobara City (smart application system and My Number card appointment system email; Arara service used by contractor TKC) | 5,652 records in total (as updated Nov 12) | Confirmed leak (first report described a possibility) | contractor / third-party service | none | [notice](https://www.city.nasushiobara.tochigi.jp/soshikikarasagasu/digitalsuishinka/huseiakusesu_zyouhourouei/24640.html) |
| 723 | 2026-11-10 | AEON Smart Technology (some AEON Group websites; gift order system) | 414 records | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.aeon-st.co.jp/news/20261110_security-notice/AST261110.pdf) |
| 724 | 2026-11-10 | Kirin Brewery and Kirin Beverage (SNS campaign tool OWNLY by Smartshare) | 1,825 records in total, of which 329 personal-data records (per-company split from the annex table, not verified verbatim) | Confirmed leak | contractor / third-party service | none | [notice](https://www.kirinholdings.com/jp/newsroom/release/2026/1110_03.pdf) |
| 725 | 2026-11-10 | Japan Chamber of Commerce and Industry (online exam management system on an external server) | up to about 980,000 people (about 1.97 million records) | Possible leak (up to) | unauthorised access (vector not disclosed) | none | [notice](https://www.kentei.ne.jp/51816) |
| 726 | 2026-11-10 | Kyoto Prefecture (Music Fusion in Kyoto festival committee; teket e-ticketing used by contractor Style KYOTO) | about 160 people | Leak confirmed at teket; possible for festival buyers | contractor / third-party service | none | [notice](https://www.pref.kyoto.jp/press/documents/2026111006.pdf) |
| 727 | 2026-11-10 | Tokyo Metropolitan Government (Policy Planning Bureau; Tokyo Green Biz Walk; system used by partner Sumitomo Life's app) | 475 people (of about 38,000 registered) | Confirmed leak | contractor / third-party service | none | [notice](https://www.metro.tokyo.lg.jp/information/press/2026/11/2026111101) |
| 728 | 2026-11-10 | Kawai Musical Instruments (teket e-ticketing for its events) | Not stated | Leak at teket; own customers unconfirmed | contractor / third-party service | none | [notice](https://www.kawai.co.jp/news/20261110/) |
| 729 | 2026-11-10 | Sapporo International Short Film Festival (online tickets via teket) | Under review | Confirmed leak at teket | contractor / third-party service | none | [notice](https://sapporoshortfest.jp/page_news_jp/teket-owabi/) |
| 730 | 2026-11-10 | e-Stadium (fan-meeting applications via teket) | Not stated | Leak at teket (reported) | contractor / third-party service | none | [notice](https://estadium.co.jp/uncategorized/p/1135/) |
| 731 | 2026-11-10 | Toyoda Gosei (Blue Falcon Nagoya handball team; teket ticketing) | Not stated | Confirmed leak at teket | contractor / third-party service | none | [notice](https://www.toyoda-gosei.co.jp/sports/handball/topics/detail.php?id=1035) |
| 732 | 2026-11-10 | Waseda University Cheerleading Club Brass Band (concert tickets via teket) | Not stated | Leak confirmed at teket; scope for own buyers undetermined | contractor / third-party service | none | [notice](https://www.w-ouen.com/%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B/) |
| 733 | 2026-11-10 | Kurashiki City (Tamashima Civic Exchange Center; teket e-ticketing) | Not stated | Leak confirmed at teket; possible for own users | contractor / third-party service | none | [notice](https://www.city.kurashiki.okayama.jp/kurashi/jinken/1012991/1002450/1028586.html) |
| 734 | 2026-11-10 | Kanagawa Ward, Yokohama City (clean-up event applications; teket used by contractor Gab) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.city.yokohama.lg.jp/city-info/koho-kocho/press/kanagawa/2026/1110shigen.html) |
| 735 | 2026-11-10 | Kiyose City (Kiyose Keyaki Hall; teket e-ticketing) | Not stated | Leak reported by teket | contractor / third-party service | none | [notice](https://www.city.kiyose.lg.jp/shisetsu/syogaigakusyu/keyakihall/1002795/1016943.html) |
| 736 | 2026-11-10 | Valtes Holdings (Qbook member newsletter; Arara Message) | 47,502 email addresses (deduplicated) | Confirmed leak | contractor / third-party service | none | [notice](https://www.valtes-hd.co.jp/news/2026/202611101996/) |
| 737 | 2026-11-10 | Obanazawa City (lecture event e-tickets via teket) | up to 44 records | Possible leak (up to) | contractor / third-party service | none | [notice](https://www.city.obanazawa.yamagata.jp/news/4620) |
| 738 | 2026-11-10 | Izumisano City (esports fan meeting; contractors NANKAI and e-Stadium; teket) | Not stated | Leak at teket (reported) | contractor / third-party service | none | [notice](https://www.city.izumisano.lg.jp/kakuka/seicyou/omotenasi/menu/oshirase/19406.html) |
| 739 | 2026-11-10 | Idemitsu Kosan (idemitsu Car Maintenance Reservation web service, formerly PIT in plus) | Not stated (under investigation) | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.idemitsu.com/jp/information/2026/261110.pdf) |
| 740 | 2026-11-10 | Kyoto University of Foreign Studies (former website server) | 5,376 people in total | Possible leak (files read in bulk during intrusion) | vulnerability | none | [notice](https://www.kufs.ac.jp/cms_image/file/file_1794271641.pdf) |
| 741 | 2026-11-10 | Kobe City (BE KOBE student navigation site email; Arara Message) | 20,730 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.city.kobe.lg.jp/a95287/031239648142.html) |
| 742 | 2026-11-10 | Yokohama City Health and Social Welfare Bureau (community care plaza facility booking system email; contractor WingArc NEX / Arara) | 508 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.city.yokohama.lg.jp/city-info/koho-kocho/press/kenko/2026/1110cp.files/kf-20261110.pdf) |
| 743 | 2026-11-10 | Konan Hospital (nursing department inquiry form on hospital website) | about 124 people (as of Nov 2) | Confirmed leak (some described as possible) | unauthorised access (vector not disclosed) | none | [notice](https://www.kohnan-sendai.or.jp/news/patient/jyouhou.html) |
| 744 | 2026-11-10 | TradeWaltz (TradeWaltz trade platform production and training environments) | 130 trade documents (containing names and initials) | Confirmed leak | contractor / third-party service | none | [notice](https://www.tradewaltz.com/news/13816/) |
| 745 | 2026-11-10 | Neyagawa City (Mail Neyagawa; Arara service used by provider WingArc NEX) | Not stated | Possible leak (cannot be ruled out) | contractor / third-party service | none | [notice](https://www.city.neyagawa.osaka.jp/topics/27626.html) |
| 746 | 2026-11-10 | immedio (cloud storage for videos uploaded to immedio Box) | up to about 14% of stored videos (number of individuals unknown) | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.immedio.io/news/page-5162/) |
| 747 | 2026-11-10 | Tabiiro Travel (Tabiiro email delivery; Arara Message) | 53,304 email addresses (deduplicated) | Confirmed leak | contractor / third-party service | none | [notice](https://tabiiro.jp/information/arara_notice_20261110.pdf) |
| 748 | 2026-11-10 | Kyushu Electric Power (weev EV car-sharing members; Arara mail engine used by contractor) | 978 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.kyuden.co.jp/press/2026/h261110-1.html) |
| 749 | 2026-11-10 | Smart Value (Kuruma Base platform; Arara Message linked to WingArc NEX SMART L-Gov ALERT) | 9,173 records (email addresses) | Confirmed leak | contractor / third-party service | none | [notice](https://www.smartvalue.ad.jp/news/11186/) |
| 750 | 2026-11-11 | Maizuru City (Vitality walking events; Sumitomo Life's contractor NTT DATA system) | 75 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.city.maizuru.kyoto.jp/0000015754.html) |
| 751 | 2026-11-11 | Cabinet Office (14 email newsletters; mail delivery provider Arara) | 61,751 records (deduplicated) | Leak reported by vendor | contractor / third-party service | none | [notice](https://www.cao.go.jp/others/csi/security/20261111notice.pdf) |
| 752 | 2026-11-11 | SMBC Nikko Securities (employee stock ownership plan management system) | up to 56,487 people | Confirmed leak (up to) | unauthorised access (vector not disclosed) | none | [notice](https://www.smbcnikko.co.jp/news/release/2026/pdf/261111_01.pdf) |
| 753 | 2026-11-11 | Dentsu Digital (TONARIWA marketing platform admin account) | Not stated (2 client companies confirmed as of Nov 12) | Possible leak (confirmed for 2 clients in second report) | unauthorised login | none | [notice](https://www.dentsudigital.co.jp/news/updates/services/2026-1111-001111) |
| 754 | 2026-11-11 | Openlogi (shipping data on the Openlogi logistics platform) | Not stated (under investigation) | Confirmed (data exfiltrated) | unauthorised access (vector not disclosed) | none | [notice](https://corp.openlogi.com/news/notice/notice-20261111/) |
| 755 | 2026-11-11 | SKIYAKI (Bitfan storage and shipping; contractor Openlogi) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://skiyaki.com/contents/1126864) |
| 756 | 2026-11-11 | Mynet (delivery data of some group services; Openlogi) | 25 delivery records (cumulative) | Possible leak | contractor / third-party service | none | [notice](https://www.mynet.co.jp/news/info/251111) |
| 757 | 2026-11-11 | Yasukuni Shrine (online amulet and merchandise site) | about 14,500 records (provisional) | Confirmed leak | unauthorised access (vector not disclosed) | none | [notice](https://www.yasukuni.or.jp/news_detail.html?id=734) |
| 758 | 2026-11-11 | Seven Bank (residence-card submission site and account-closure site) | up to about 150 records | Possible leak (up to) | unauthorised access (vector not disclosed) | none | [notice](https://www.sevenbank.co.jp/support/info_notice127.html) |
| 759 | 2026-11-11 | Okhotsk Garinko Tower (official goods shop; delivery contractor Openlogi) | Not stated | Confirmed (data exfiltrated) | contractor / third-party service | none | [notice](https://azarashiseal.kawaiishop.jp/p/00003) |
| 760 | 2026-11-11 | LRM (Notion AI interaction logs; environment of Notion's AI subprocessor Fireworks AI) | Under investigation | Possible leak | contractor / third-party service | none | [notice](https://www.lrm.jp/info/news/info_20261111/) |
| 761 | 2026-11-11 | jig.jp (Palette Project official store; contractor Openlogi) | Not stated | Possible leak (exfiltration confirmed at contractor) | contractor / third-party service | none | [notice](https://paletteproject.jp/20261111-2) |
| 762 | 2026-11-11 | Kochi City (staff recruitment exam; recorded video interview service by ApplyNow) | 1,464 records | Possible leak | contractor / third-party service | none | [notice](https://www.city.kochi.kochi.jp/site/syokuin-saiyo/2026rokugafusei.html) |
| 763 | 2026-11-11 | Japan Post (LINE account surveys; contractor Dentsu Digital's TONARIWA) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.post.japanpost.jp/newsrelease/pressrelease/685401036.html) |
| 764 | 2026-11-11 | Kawajun (KEYUCA online shop newsletter; Arara Message) | 1,214,183 email addresses | Confirmed leak (as reported by vendor) | contractor / third-party service | none | [notice](https://www.kawajun.co.jp/news/keyuca/notification-of-unauthorized-access-20261111-2/) |
| 765 | 2026-11-11 | Yamaguchi Prefecture (Yamaguchi Vitality Walk; Sumitomo Life's contractor NTT DATA system) | 42 people (of 3,065 applicants) | Confirmed leak | contractor / third-party service | none | [notice](https://www.pref.yamaguchi.lg.jp/press/369833.html) |
| 766 | 2026-11-11 | Mutsu City (My Number card appointment system email; Arara Message) | Under investigation | Possible leak | contractor / third-party service | none | [notice](https://www.city.mutsu.lg.jp/kurashi/mynumber/2026-1111-1733-39.html) |
| 767 | 2026-11-11 | Rinavis (home-delivery cleaning newsletters; Arara repica) | 158,960 records (email addresses) | Confirmed leak | contractor / third-party service | none | [notice](https://rinavis.com/f/notice_20261111) |
| 768 | 2026-11-11 | Sanjo City (self blood-glucose check program email; contractors Nippon Life and Welby; provider Arara) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.city.sanjo.niigata.jp/material/files/group/17/HP.pdf) |
| 769 | 2026-11-11 | Mitsubishi UFJ Financial Group (shareholder e-gift program; Arara system used by contractor Giftpad) | 20,000 email addresses | Confirmed leak (as reported) | contractor / third-party service | none | [notice](https://www.mufg.jp/dam/pressrelease/2026/pdf/news-20261111-001_ja.pdf) |
| 770 | 2026-11-11 | Giftpad (some email delivery operations; Arara Message) | 144,364 email addresses | Confirmed leak (as reported by vendor) | contractor / third-party service | none | [notice](https://corp.giftpad.co.jp/article_source/data/news/detail/2026/253.html) |
| 771 | 2026-11-11 | Bijyu (Otabe online shop; GMO Makeshop MakeRepeater / Arara Message) | up to about 114,000 records (cumulative) | Confirmed leak (count up to, not finalized) | contractor / third-party service | none | [notice](https://www.otabe.jp/view/news/20261111171517) |
| 772 | 2026-11-11 | TV Tokyo and TV Tokyo Communications (three online stores; EC logistics contractor Openlogi) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.tv-tokyo.co.jp/kaisha/pdf/20261111.pdf) |
| 773 | 2026-11-11 | Kiyokawaya (inventory management system Matomaru EC Tencho for its online stores) | up to 392 records | Confirmed leak (count up to) | contractor / third-party service | none | [notice](https://www.kiyokawaya.co.jp/information/6545/) |
| 774 | 2026-11-11 | Ucoop consumer co-op (HAPPY COLLECTION and other deliveries; Sagawa Express parcel inquiry service) | 11,891 shipments, 297 people and 897 people (shipments/people using Sagawa, not confirmed leaks) | Possible leak | contractor / third-party service | none | [notice](https://www.ucoop.or.jp/info/2026/info_34598.html) |
| 775 | 2026-11-11 | BONX (logistics contractor Openlogi) | up to 1,144 records | Possible leak (up to) | contractor / third-party service | none | [notice](https://bonx.co/ja/news-release/20261111-2/) |
| 776 | 2026-11-11 | Pilot Corporation (PILABOT product buyers; logistics contractor Openlogi) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.pilot.co.jp/information/01/2026/11/11/post_243.html) |
| 777 | 2026-11-11 | REALITY Studios (official shop; logistics contractor Openlogi) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://reality-studios.inc/news/20261111/) |
| 778 | 2026-11-11 | Aderia (Aderia Retro official shop; contractor Openlogi) | Not stated | Possible leak (exfiltration confirmed at contractor) | contractor / third-party service | none | [notice](https://aderia-retro.com/pages/20261111) |
| 779 | 2026-11-11 | smartship (smartship store; storage and shipping contractor Openlogi) | Under investigation | Possible leak | contractor / third-party service | none | [notice](https://store.smartship.co.jp/openlogi-20261111/) |
| 780 | 2026-11-11 | Takami (TAKAMI BRIDAL; collective. online store shipping; contractor Openlogi) | Not stated | Possible leak | contractor / third-party service | none | [notice](https://www.takami-bridal.co.jp/news/1384/) |
| 781 | 2026-11-11 | Faeger (Notion AI interaction logs; Notion's subprocessor Fireworks AI) | Under investigation | Possible leak | contractor / third-party service | none | [notice](https://faeger.company/news-security-incident-20261111/) |
| 782 | 2026-11-11 | Axel Entermedia (campaign winner emails for an FTISLAND release event; Arara Message; posted on FNC Entertainment Japan's official site) | 500 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.ftisland-official.jp/post/261111) |
| 783 | 2026-11-11 | jig.jp (Paredemia Gakuen official store; contractor Openlogi) | Not stated | Possible leak (exfiltration confirmed at contractor) | contractor / third-party service | none | [notice](https://www.parerdemia.jp/news/ivl9rm2yft) |
| 784 | 2026-11-11 | JCOM (bicycle road-service products; Prestige Core Solution business system via KDDI) | Not stated (under investigation) | Possible leak | contractor / third-party service | none | [notice](https://notices.jcom.co.jp/notice/95259.html) |
| 785 | 2026-11-11 | Odakyu Electric Railway (forms on ichinoichi, TORA NO TE and NEUU websites; Studio site builder) | about 550 form responses (ichinoichi), about 50 (NEUU), TORA NO TE under review | Possible leak | contractor / third-party service | none | [notice](https://www.odakyu.jp/support/makhce0000003mqi-att/makhce0000003mqp.pdf) |
| 786 | 2026-11-11 | Dairek (vaultroom official online store; delivery contractor Openlogi) | Not stated | Exfiltration confirmed at contractor; own customers under review | contractor / third-party service | none | [notice](https://vaultroom.shop/blogs/news/important) |
| 787 | 2026-11-11 | Toyo University (email newsletter; Arara Message) | Not stated | Confirmed leak | contractor / third-party service | none | [notice](https://www.toyo.ac.jp/news/20261111-20555.html) |
| 788 | 2026-11-12 | ENSAPIA Tokyo (shipping data handled by delivery contractor OPENLOGI) | count not disclosed | Possible leak | contractor / third-party service | none | [notice](https://ensapia-tokyo.com/news/topics/id=21395/) |
| 789 | 2026-11-12 | ENSAPIA Tokyo ("asoview!" member data of ticketing contractor Asoview; Asoview's email vendor Arara) | own count not disclosed (Asoview total: 15,821,184 records) | Possible leak | contractor / third-party service | none | [notice](https://ensapia-tokyo.com/news/topics/id=21395/) |
| 790 | 2026-11-12 | Cyber Security Cloud (company-managed area on GitHub; an employee's leaked GitHub credential) | count not disclosed (under investigation) | Possible leak | unauthorised login | none | [notice](https://www.cscloud.co.jp/news/info/20261112-2/) |
| 791 | 2026-11-12 | Kewpie (five group companies; auto-reply emails for campaign entries and inquiry forms; contractor Arara's email service) | 125,788 records (five companies combined) | Confirmed leak | contractor / third-party service | none | [notice](https://lp.kewpie.com/notices/2026/2026e/) |
| 792 | 2026-11-12 | BookLive (member accounts of the "BookLive" e-book store; credential-stuffing attack) | suspected unauthorized logins to 6,127 people's accounts | Possible viewing of account pages (no bulk leak confirmed) | unauthorised login | none | [notice](https://www.booklive.co.jp/topics/18739) |
| 793 | 2026-11-12 | Weathernews (official online shop "SORASHOP"; delivery contractor OPENLOGI) | count under investigation by OPENLOGI | Possible leak | contractor / third-party service | none | [notice](https://jp.weathernews.com/news/58120/) |
| 794 | 2026-11-12 | Macromill (part of the "Macromill Monitor Site" survey-panel system) | 317 panelists (people), incl. 82 with bank-account details | Confirmed leak (viewed) | unauthorised access (vector not disclosed) | none | [notice](https://monitor.macromill.com/news/20261112-oshirase.html) |
| 795 | 2026-11-12 | Tokyo Gas (registrants of the gas main location check service; contractor Arara's "Arara Message") | 85,565 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.tokyo-gas.co.jp/news/press/20261112-02.html) |
| 796 | 2026-11-12 | ONE CAREER ("Notion AI" chat history; Notion's AI processing contractor Fireworks AI) | up to approx. 2,300 records | Possible leak (up to) | contractor / third-party service | none | [notice](https://onecareer.co.jp/news/information/261112/) |
| 797 | 2026-11-12 | baton (shipping data for online stores incl. "QurioStore"; logistics contractor OPENLOGI) | count under investigation | Confirmed exfiltration of shipping data (own customers: possible) | contractor / third-party service | none | [notice](https://quriostore.com/blogs/news/openlogi-security-notice) |
| 798 | 2026-11-12 | Nikkei Research (cloud tool "Notion"; Notion's contractor Fireworks AI) | count not disclosed | Possible leak | contractor / third-party service | none | [notice](https://www.nikkei-r.co.jp/news/information/20261112) |
| 799 | 2026-11-12 | United Super Markets Holdings ("Scan&Go ignica" app system) | 64,003 accounts (of approx. 2.4 million app accounts) | Possible leak | unauthorised access (vector not disclosed) | none | [notice](https://www.usmh.co.jp/wp-content/uploads/2026/11/us_20261112.pdf) |
| 800 | 2026-11-12 | Hyakujushi Bank (shareholder e-gift winner emails; Arara email system used by contractor Giftpad) | 1,500 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.114bank.co.jp/important/pdf/imp20261112.pdf) |
| 801 | 2026-11-12 | Ota City Culture and Sports Promotion Foundation (Ota Sports Academy; "Hanamaru Renrakucho" app by Satellite; its email vendor Arara) | approx. 4,500 records (cumulative registrants, incl. duplicates) | Possible leak | contractor / third-party service | none | [notice](https://www.ota-sports-academy.com/topics/i_etc/%e3%81%af%e3%81%aa%e3%81%be%e3%82%8b%e9%80%a3%e7%b5%a1%e5%b8%b3%e3%82%a2%e3%83%97%e3%83%aa%e3%81%ae%e4%b8%8d%e6%ad%a3%e3%82%a2%e3%82%af%e3%82%bb%e3%82%b9%e3%81%ab%e4%bc%b4%e3%81%86%e5%80%8b%e4%ba%ba/) |
| 802 | 2026-11-12 | Koka City (regional information infrastructure; audio broadcasting system server; ransomware attack) | count not disclosed | Possible leak (under investigation) | unauthorised access (vector not disclosed) | none | [notice](https://www.city.koka.lg.jp/item/45076.htm) |
| 803 | 2026-11-12 | Adventure World (email delivery of ticketing company Terravie; Arara's "Arara Message") | 5,709 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.aws-s.com/topics/detail?id=top4787) |
| 804 | 2026-11-12 | Persol Career ("doda" LINE official account operations; contractor Dentsu Digital's "TONARIWA") | count not disclosed | Possible leak | contractor / third-party service | none | [notice](https://www.persol-career.co.jp/info/20261112_2370/) |
| 805 | 2026-11-12 | VAZ (shipping data for "Mel:See from classroom"; logistics contractor OPENLOGI) | count not disclosed | Confirmed exfiltration | contractor / third-party service | none | [notice](https://vaz.co.jp/topics/7820/) |
| 806 | 2026-11-12 | RECEPTIONIST ("Notion AI" interaction records; Notion's contractor Fireworks AI) | 53 external people (plus employee data) | Possible leak | contractor / third-party service | none | [notice](https://receptionist.co.jp/news/20261112-notice) |
| 807 | 2026-11-12 | Sonicmoov (admin console of the cloud LINE-integration service "COMSBI (SaaS edition)") | count not disclosed (data of multiple client companies/organizations) | Confirmed leak | unauthorised login | none | [notice](https://sonicmoov.com/news/5ttj9ndzh) |
| 808 | 2026-11-12 | Chiba Kogyo Bank (two loan products; guarantor SMBC Consumer Finance's guarantee system) | 3,398 people | Confirmed leak | contractor / third-party service | none | [notice](https://www.chibakogyo-bank.co.jp/news/important/of_ja_important_2_1.html) |
| 809 | 2026-11-12 | Fujiya (official online shop "Family Town" newsletter; contractor Arara's "Arara Message") | 149,892 records (maximum) | Leak found (scope described as possible) | contractor / third-party service | none | [notice](https://www.fujiya-peko.co.jp/assets/pdf/release20261112_1.pdf) |
| 810 | 2026-11-12 | Kitakyushu City (litter-pickup event entries; e-ticket service "teket" used by contractor Gab) | 117 people (representatives) | Possible leak | contractor / third-party service | none | [notice](https://www.city.kitakyushu.lg.jp/contents/008_00014.html) |
| 811 | 2026-11-12 | New National Theatre Tokyo ("asoview!" member data; Arara email service used by Asoview) | count not disclosed | Leak reported by contractor | contractor / third-party service | none | [notice](https://www.nntt.jac.go.jp/release/detail/23_032519.html) |
| 812 | 2026-11-12 | TimeTree ("Notion AI" interactions; external processor Fireworks AI) | 13 + 5 + 81 people | Possible leak | contractor / third-party service | none | [notice](https://timetreeapp.com/intl/ja/newsroom/2026-11-12/announce) |
| 813 | 2026-11-12 | IVRy (groupware "Notion"; Notion's contractor Fireworks AI) | 33 records (client contacts) + 12 records (candidates); sales-related client data under review | Confirmed leak (further data under review) | contractor / third-party service | none | [notice](https://ivry.jp/corporate/news/4wu8ght2l2/) |
| 814 | 2026-11-12 | DreamArts (prompts and responses in "Notion AI"; Notion's contractor Fireworks AI) | count not disclosed | Possible leak | contractor / third-party service | none | [notice](https://www.dreamarts.co.jp/news/information/inf261112/) |
| 815 | 2026-11-12 | Sanfrecce Hiroshima (email delivery of the TSS Sanfrecce Hiroshima official mobile site; Arara's "Arara Message") | 2,900 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.sanfrecce.co.jp/news/other/13058) |
| 816 | 2026-11-12 | Watts (customer emails of contact-lens shop "Appeal"; Arara's "repica" via DataX) | 38,904 records (as of 2026-11-11) | Confirmed leak | contractor / third-party service | none | [notice](https://appeal-w.co.jp/data-breach) |
| 817 | 2026-11-12 | Prima Meat Packers (online shop newsletter; e-commerce operator GMO Makeshop / Arara's "Arara Message") | count not disclosed | Possible leak | contractor / third-party service | none | [notice](https://www.primaham.co.jp/fixed/2026/post_429.html) |
| 818 | 2026-11-12 | Kobe Tea (online shop; Arara Message linked to GMO Makeshop's MakeRepeater) | 12,538 records | Confirmed leak | contractor / third-party service | none | [notice](https://teacourt.jp/blog/6675/) |
| 819 | 2026-11-12 | Namerikawa City (nursery nap-check sensor; system provider icuco) | 27 children (people) | Possible leak | contractor / third-party service | none | [notice](https://www.city.namerikawa.toyama.jp/soshiki/24/1/11688.html) |
| 820 | 2026-11-12 | eBay Japan ("Qoo10" e-commerce marketplace system) | count not disclosed | Confirmed viewing (items listed as possibly affected) | unauthorised access (vector not disclosed) | none | [notice](https://www.qoo10.jp/gmkt.inc/Main/PopupNotice.aspx?nid=6246) |
| 821 | 2026-11-12 | Mitsukoshi Isetan Human Solutions (job-information emails to Mitsukoshi Isetan part-timers; Arara email service) | 2,511 records (email addresses) | Confirmed leak | contractor / third-party service | none | [notice](https://www.imh-sol.co.jp/news/news/N261112.html) |
| 822 | 2026-11-12 | Shijonawate City (nap-check support system "icuco touch&care"; provider icuco) | 18 children and 26 staff (people) | Possible leak | contractor / third-party service | none | [notice](https://www.city.shijonawate.lg.jp/page/122452.html) |
| 823 | 2026-11-12 | Itami City ("icuco book" incl. for family; provider icuco) | count not disclosed | Possible leak (under investigation) | contractor / third-party service | none | [notice](https://www.city.itami.lg.jp/oshirase/50774.html) |
| 824 | 2026-11-12 | Osaka City Abeno Ward Office (FY2026 elementary English support program; Arara email service used by contractor Ing) | email addresses of 245 event winners (people) | Confirmed leak | contractor / third-party service | none | [notice](https://www.city.osaka.lg.jp/hodoshiryo/abeno/0000691524.html) |
| 825 | 2026-11-12 | Balus (operator of SPWN; shipping data for SPWN orders; contractor OPENLOGI) | count not disclosed | Possible leak | contractor / third-party service | none | [notice](https://spwn.zendesk.com/hc/ja/articles/64237644479513) |
| 826 | 2026-11-12 | Nanashi Inc. (774inc.; goods sales contractor SPWN's shipping contractor OPENLOGI) | count not disclosed | Possible leak | contractor / third-party service | none | [notice](https://www.774.ai/post/%E3%80%90%E9%87%8D%E8%A6%81%E3%80%91%E5%BD%93%E7%A4%BE%E3%82%B0%E3%83%83%E3%82%BA%E8%B2%A9%E5%A3%B2%E5%A7%94%E8%A8%97%E5%85%88%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B%E5%80%8B%E4%BA%BA%E6%83%85%E5%A0%B1%E6%BC%8F%E6%B4%A9%E3%81%AE%E5%8F%AF%E8%83%BD%E6%80%A7%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E3%81%8A%E8%A9%AB%E3%81%B3%E3%81%A8%E3%81%8A%E7%9F%A5%E3%82%89%E3%81%9B) |
| 827 | 2026-11-12 | Yeny (member data of several prepaid "Pay" services by PayBlend; API connection settings) | 1,332,505 records (incl. former members) | Confirmed leak | misconfiguration | none | [notice](https://yeny.jp/pressrelease/1547/) |
| 828 | 2026-11-13 | Aioi Nissay Dowa Insurance (emails from the "Fleekdrive" online storage used to share dashcam footage; Fleekdrive's contractor Arara) | approx. 16,000 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.aioinissaydowa.co.jp/corporate/about/news/pdf/2026/news_2026111301533.pdf) |
| 829 | 2026-11-13 | Kintetsu Miyako Hotels International ("Miyako Hotel Online Shop"; Arara email delivery service used by a contractor) | 16 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.miyakohotels.ne.jp/topic/information/241/) |
| 830 | 2026-11-13 | Mitsui Sumitomo Insurance (emails from the "Fleekdrive" online storage used to share dashcam footage; Fleekdrive's contractor Arara) | approx. 15,000 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.ms-ins.com/news/fy2026/pdf/1113_1.pdf) |
| 831 | 2026-11-13 | Niigata Prefecture ("Niigata Environment Mail" delivery service; operator EMZ) | count under investigation (current registrants: approx. 750 people) | Possible leak (under investigation) | contractor / third-party service | none | [notice](https://www.pref.niigata.lg.jp/site/kankyo/kankyomail-rouei.html) |
| 832 | 2026-11-13 | Yamaguchi Financial Group (subsidiary Chiiki Shosha Yamaguchi's "jimotto" newsletter; Arara Message used by GMO Makeshop's MakeRepeater) | 3,287 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.ymfg.co.jp/files/51d89ee4528ae712edae0c14902afdb29ae9c9212eedf9dc82918b45aa1e265c) |
| 833 | 2026-11-13 | Brave group (group online stores incl. VSPO! official store; fulfilment contractor OPENLOGI) | count not disclosed ("part of customer information") | Confirmed exfiltration (heading says possible leak) | contractor / third-party service | none | [notice](https://bravegroup.co.jp/news/12429/) |
| 834 | 2026-11-13 | At Home (admin site of the "Rental Management System" for real-estate agencies) | 6,901 records (details under investigation) | Possible leak | unauthorised login | none | [notice](https://www.athome.co.jp/corporate/news/topics/oshirase-202611/) |
| 835 | 2026-11-13 | TEAC ("TEAC Store" email delivery; Arara Message used by GMO Makeshop's MakeRepeater and Mail Delivery Plus) | 7,140 records (MakeRepeater) + 7,050 records (Mail Delivery Plus) | Confirmed leak | contractor / third-party service | none | [notice](https://assets.minkabu.jp/news/article_media_content/urn:newsml:tdnet.info:20261113579636/140120261113579636.pdf) |
| 836 | 2026-11-13 | Vega Corporation (LOWYA stores on e-commerce malls; API integration with Branding Solution's "Matomaru EC Tencho") | up to 392 records | Possible leak (up to) | contractor / third-party service | none | [notice](https://assets.minkabu.jp/news/article_media_content/urn:newsml:tdnet.info:20261113577617/140120261113577617.pdf) |
| 837 | 2026-11-13 | Human Adjust (Sonicmoov's cloud service "COMSBI (SaaS edition)") | up to 58,510 people (users) and up to 116,518 people (LINE official account friends) | Possible leak (up to) | contractor / third-party service | none | [notice](https://assets.minkabu.jp/news/article_media_content/urn:newsml:tdnet.info:20261113579962/140120261113579962.pdf) |
| 838 | 2026-11-13 | Cabinet Office (Okinawa policy; "OKINAWA41" PR project; rental server used by JTB's subcontractor Beethoven, operated by Sakura Internet) | count not disclosed | Possible leak | contractor / third-party service | none | [notice](https://www8.cao.go.jp/okinawa/rireki/20261113okinawa41.html) |
| 839 | 2026-11-13 | Mitsui Direct General Insurance (emails from the "Fleekdrive" online storage; Fleekdrive's contractor Arara) | approx. 1,200 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.mitsui-direct.co.jp/information/20261113.html) |
| 840 | 2026-11-13 | Kobe City (email delivery of the "e-KOBE" online application system; external delivery service "Arara Message" used by the system operator) | 85,707 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://www.city.kobe.lg.jp/a32541/893242339895.html) |
| 841 | 2026-11-13 | Corona Corporation (official online store newsletters; Arara email delivery service used by the provider's contractor) | 7,299 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.corona.co.jp/report/safety/post_153.html) |
| 842 | 2026-11-13 | Osaka City Naniwa Ward Office (FY2026 junior-high learning support program; Arara email service used by contractor Ing) | email addresses of 48 registrants (people) | Confirmed leak | contractor / third-party service | none | [notice](https://www.city.osaka.lg.jp/hodoshiryo/naniwa/0000691595.html) |
| 843 | 2026-11-13 | Honda Motor (shareholder e-gift emails; Arara email service used by contractor Giftpad) | 1,741 email addresses | Confirmed leak | contractor / third-party service | none | [notice](https://global.honda/jp/news/2026/c261113.html) |
| 844 | 2026-11-13 | Hokkaido Electric Power ("Kirameku Store" e-commerce newsletter; Arara Message used by GMO Makeshop's MakeRepeater) | 5,664 records | Confirmed leak | contractor / third-party service | none | [notice](https://www.hepco.co.jp/info/2026/1253239_2073.html) |

## Counting

- Of 31 rows, 14 notices state the vector; 17 do not.
- Vulnerability 5, VPN vulnerability 1, contractor 5, unauthorised login 1, misconfiguration 1, multiple 1.
- Notices mentioning attacker-side AI: 0.
- Rows exceeding one million in the notice's own unit: 8 (005, 007, 017, 021, 025, 026, 027, 028).
- Non-corporate organisations: 2 (002 Digital Agency, 015 JOGMEC).
- Rows whose subjects are employees rather than customers: 3 (002, 016, part of 026).

(Added 16 October 2026)  
Follow-up notices the author confirmed between publication of the first edition and 16 October are listed below. Row values are unchanged; each row's notes column carries a dated addition or correction.

| ID | Organisation | Follow-up date | Content (notice's own wording) |
|---|---|---|---|
| 001 | Charm | 2026-10-07 (4th notice) | Former members' data 「約2.5万件」 (approx. 25,000 records); 「大部分について漏えいを確認」 (leak confirmed for most), the rest 「漏えいのおそれ」 (possible leak) |
| 008 | Nippon Rent-A-Car Service | 2026-10-01 (separate incident) | 「55名」 (55 members); 「第一事象報告に係る不正アクセスとは異なる手法」 (a different method from the first incident). Separate from this row's 41 |
| 018 | GMO Research & AI | 2026-10-14 (2nd notice) | 「最大94万8,498件」 → 「外部に持ち出された件数は89万4,082件であることを確定」 (records taken out confirmed at 894,082). Correction |
| 019 | Kufu Company | 2026-10-13 (investigation result) | 「少なくとも1名」 → 「対象となるお客さま：308名」 (308 customers); vector 「システムの一部の脆弱性」 (a vulnerability in part of the system). Correction |
| 023 | IDC Frontier | 2026-10-14 (5th notice) | 「外部へのデータの流出はなかったと判断」 (judged no exfiltration); 「48社」 registration records subject to 「不正な照会」 (unauthorised queries) in the portal. Correction |
| 027 | JR East | 2026-10-15 (same PDF updated) | Contractor reported 「漏えいがなかったと判断」 (judged no leak). Figures remain. Correction |
| 028 | Adventure | 2026-10-13 | Phone contact window opened. No change in figures or vector |

With the follow-ups included, notices mentioning attacker-side AI remain at 0. The two rows that reached a confirmed figure (018, 019) both moved below the first-notice maximum. The one row that judged "no exfiltration" (023) changed the status of one downstream row (027). For the other 24 rows, no notice update was confirmed by 16 October; not confirmed does not mean none exists.

(Added 16 October 2026)  
Counts after adding five rows:

- Of 36 rows, 16 notices state the vector; 20 do not.
- Vulnerability 6, VPN vulnerability 1, contractor 6, unauthorised login 1, misconfiguration 1, multiple 1.
- Notices mentioning attacker-side AI: 0.
- Rows exceeding one million in the notice's own unit: 10 (the first edition's 8 plus 032 and 036).

(Added 26 October 2026)  
Follow-ups confirmed between the second edition and 26 October (row values unchanged; dated additions or corrections in the notes column): 005 Helpfeel, final report of 21 Oct (counts unchanged; 「432件」 images owned by 「133名」 found viewed or taken; vulnerability described as unsanitised input interpreted as server commands); 007 Times Mobility, 5th notice of 23 Oct (「6,628,007 件」; ID images with exfiltration traces 「1,464,800 件」; vector disclosed for the first time as a web-system vulnerability — correction); 012 Seicomart, 15 Oct (service restart schedule); 017 Monogatari, 20 Oct (security measures; 「外部の第三者からの断続的な攻撃」 from 09:00 on 2 Oct; no vector detail); 023 IDC Frontier, 6th notice of 18 Oct (backup service restarted); 025 Lawson, 24 Oct update (email addresses and newsletter data not leaked; date of birth possibly leaked — correction; counts unchanged); 028 Adventure, 2nd notice of 16 Oct (card data 「最大6,140名」; first notice's statement on card numbers corrected); 032 Bookoff, 2nd notice of 13 Oct and later PDFs (unreachable, unread; press: 6,383,279 persons); 034 Sagawa Express, 5th notice of 23 Oct (JavaScript-only page, unread; press: up to approx. 53.23 million); 035 Uzabase, 2nd notice of 9 Oct (unread; press: per-item maxima); 030/031 via Commune's 21 Oct follow-up (unread; press: 166,505 persons). Even with the follow-ups, zero notices mention attacker-side AI. The one fixed count (007) moved below the first notice's maximum for ID images; the two changed data scopes moved in opposite directions (025 dropped email addresses, 028 added card numbers); the one vector disclosed afterwards (007) was a vulnerability.

(Added 26 October 2026)  
Counts after adding 35 rows:

- Of 71 rows, 36 state a vector and 35 do not
- Vulnerability 12, VPN vulnerability 1, contractor 16, unauthorised login 4, misconfiguration 2, multiple 1
- Notices mentioning attacker-side AI: 0. Notices mentioning defender-side AI: 3 (005, 054, 062)
- Rows above one million in the notice's own unit: 21; above ten million: 5 (005, 028, 017, 044, 064)
- Non-company organisations: 7 (002, 015, 039, 052, 056, 058, 060)
- Rows whose subjects are employees, staff or related persons rather than customers: 6 (002, 016, part of 026, 039, 041, 058)
- Chains with both origin and client in the ledger: 6 (IDC Frontier, Commune, Scala Communications, Studio, Yumirlink, Rakus, NEC — FutureShop has only its client 070)

On the admission rule: 049 Joshin Denki and 050 Ishikawa Computer Center state neither scale nor data items; 047 Comic Cmoa and 051 Studio give counts as "under review." They are admitted because the ledger sets no lower bound. A ledger of only the cases whose size is known would be a ledger of what is known, not of what was disclosed.

(Added 3 November 2026)  
Follow-ups to 19 existing rows were confirmed and added to the notes column (row values unchanged). Corrections: 023 IDC Frontier (7th notice, 27 Oct: vector disclosed as an open-source software vulnerability in its portal's authentication system; unauthorised queries up to 71 companies), 028 skyticket (3rd notice, 30 Oct: refund bank-account data 「32,341件」 leaked; partial card data approx. 936,000 records and travel-insurance data approx. 118,000 records possibly leaked), 047 Comic Cmoa (319 records; up to approx. 4.2 million log records), 053 Yumirlink (51,628,280 cumulative, 49 systems), 070 Lindt (3,147,469 → 3,147,377, duplicate removed), 071 System5 (up to 15,671 persons). Additions: 012, 025, 026, 050, 051, 054, 055, 059, 061, 062, 063, 064. Unlike the third edition, confirmed figures did not all move downward: 070 and 071 settled, while 053 and 047 moved up.

Counts after adding 229 rows:

- Of 300 rows, 226 state a vector and 74 do not
- Contractor 179, vulnerability 27, unauthorised login 12, multiple 4, misconfiguration 3, VPN vulnerability 1
- Notices mentioning attacker-side AI about their own incident: 1 (079 Chitose Group, a presumption; Tier 3)
- Rows above one million in the notice's own unit: 38; above ten million: 6 (005, 028, 017, 044, 064, 275)
- National and local government bodies, incorporated administrative agencies and public universities: 43 (the third edition's 7 plus 36)
- 140 of the 229 new rows were disclosed in five days, 26–30 October

(Added 8 November 2026)  
Follow-ups to existing rows confirmed by 8 November, recorded as dated additions or corrections in the notes without changing row values: 241 Arara 3rd notice (6 Nov) "81,329,467 (approx. 81 million)" de-duplicated, "up to approx. 380 companies", up to approx. 7.13 million phishing mails sent — correction; 004 Rohto (6 Nov) "2,797,545 customers", 9,715 with card data in call recordings, vector: misuse of telephone-system credentials — correction; 215 Paydon (4 Nov) leak confirmed, "up to 257,639" — correction; 275 Ryohin Keikaku 2nd notice (4 Nov) MUJI online-store members included, card data possibly accessed; 290 Prestige International 2nd notice (6 Nov) "3" card numbers newly confirmed; 223 NTT Smile Energy (6 Nov) approx. 14,000 fraudulent point exchanges, no personal-data leak confirmed; 195 JETRO (6 Nov) 142 / 9,252 / 19 records — same incident as the row is unconfirmed; 032 Bookoff 3rd notice (6 Nov) PDF unreachable, unread; 297 Himeji 2nd notice linked, URL not identified.

In the fifth edition every confirmed figure moved upward: Arara from approx. 3.01 million to 81,329,467; Rohto from no count to 2,797,545; Paydon from "possible" to up to 257,639. The observation through the third edition — that confirmed figures move below the first maximum — split in the fourth edition and reversed in the fifth. A contractor's first figure multiplying 27-fold in nine days is also why clients cannot state their own counts in their first notices.

(Added 10 November 2026)  
Follow-ups confirmed by 9 November, added to the notes with dates: 275 Ryohin Keikaku 4th notice (9 Nov: a list-based login attack on the online store, and confirmed unauthorised access to part of the data on cash-on-delivery recipients from 2 January 2020 to 10 February 2025; the notice says previously announced counts have partly changed, but the revised table could not be read); 055 Trust Bank 6th notice (9 Nov: no change in count or vector; app restarted and all members' passwords invalidated). No new follow-ups were found for 7–9 November from the chain origins 241, 290, 320, 436, 485, 484 or 304; the timely disclosures of Arara's parent, Paycloud Holdings, refused retrieval.

Among the rows added on 10 November, two counts moved in follow-ups: 508 JERA from "approx. 110,000" (2 Nov) to "30,337" (7 Nov), a downward move; and 509 Kinko's Japan, whose second notice (9 Nov) gave "266,395" and added name and date of birth to the leaked items. SEGA Fave, cited in the fourth edition as an example of a notice outside the admission rule, is covered by 576 SEGA's notice of 9 November, which reports that SEGA was told by Arara on 29 October that no leak had been confirmed, and on 3 November that the email addresses had leaked — a client's initial "no leak" changing as the contractor's investigation advanced.

(Added 8 November 2026)  
After adding 207 rows: 507 rows, of which 418 state the vector and 89 do not (about 180 independent intrusions, vector known for about 60); contractor 356, vulnerability 32, unauthorised login 16, multiple 7, misconfiguration 6, VPN 1; attacker-side AI mentioned about the incident in 1 row (079), none among the new rows; 49 rows exceed one million and 8 exceed ten million (005, 028, 017, 044, 064, 275, 304, 484); national and local public bodies (incl. agencies and public universities) rose from 43 to 120, 55 of the 77 new ones being municipalities in the TKC chain; new rows by date: 3 Nov 21, 4 Nov 83, 5 Nov 66, 6 Nov 13, 7 Nov 1 — 4 November is the ledger's largest single day; 97 new rows state no count. Two admission notes: notices that only say the organisation's data "is not included" or "no leak confirmed", without raising the possibility, remain excluded; notices not on the organisation's own domain (TOAST on note.com, AKB48 Mail on ameblo.jp) are held as pending for the author's judgement.

(Added 10 November 2026)  
After adding 77 rows: 584 rows, of which 482 state the vector and 102 do not (about 200 independent intrusions); contractor 417, vulnerability 33, unauthorised login 18, multiple 7, misconfiguration 6, VPN 1; attacker-side AI mentioned about the incident in 1 row (079), none among the new rows; 54 rows exceed one million and 9 exceed ten million (005, 028, 017, 044, 064, 275, 304, 484, 577); national and local public bodies rose by 12 to 132 (Yamaguchi, Sakai, Saitama ×2, Kyoto City, Okinawa, Okayama ×2, Daisen, Yurihonjo, Okazaki, and all prefectures and designated cities as issuers of Takarakuji); new rows by date: 30 Oct 1, 2 Nov 5, 4 Nov 2, 5 Nov 3, 6 Nov 47, 7 Nov 6, 9 Nov 13 — 6 November now has 60 rows; no row is dated 8 November (teket's notice could not be read and is pending); 26 new rows state no count. Three notices were reached but not admitted: the Japan Society for the Promotion of Science ("no leak of personal information has been confirmed at this time"), Meijiza (only unauthorised access and suspension), and Fukui Prefecture's "291JOBS" (files viewable through a maintenance contractor's misconfiguration, with no unauthorised access described). Rows on the boundary of admission rule 2 are admitted with a note for the author's judgement: 528 Takarakuji, 550 BitCash, 513 Sony Assurance. Mos Food Services (Mos Card) and Value Design came up again but the fifth edition's exclusion (no personal information) stands.

(Added 14 November 2026)
After adding 260 rows: 844 rows, of which 719 state the vector and 125 do not; contractor 641, vulnerability 36, unauthorised login 24, misconfiguration 10, multiple 7, VPN 1; attacker-side AI mentioned about the incident in 1 row (079), none among the new rows; 60 rows exceed one million and 9 exceed ten million; 62 new rows are named national bodies, prefectures or municipalities (universities, agencies and municipal foundations not included); new rows by date: 7 Sep 1, 29 Sep 1, 2–29 Oct 11, 2 Nov 6, 3 Nov 4, 4 Nov 14, 5 Nov 20, 6 Nov 14, 7 Nov 1, 8 Nov 9, 9 Nov 49, 10 Nov 33, 11 Nov 38, 12 Nov 40, 13 Nov 17 — 4 November (99 rows) remains the ledger's largest single day; 44 new rows have a scale beginning "記載なし" (not stated).

Follow-ups were added with dates to the notes of 20 existing rows (053, 059, 119, 236, 339, 346, 361, 371, 418, 425, 436, 445, 528, 549, 556, 558, 560, 569, 575, 583). Corrections: 053 Ymir Link (cumulative count finalised), 119 istyle (count disclosed), 361 Navac (approx. 350,000 → 320,720), 445 Tokio Marine & Nichido Direct (74 → 71; the page version differs from the 10 November re-check and needs the author's confirmation), and 549 EDION (the second notice found a tampering of payment processing and withdrew the first notice's "no leak of card data or passwords").

Notices reached but not admitted: no statement of a leak or possible leak of personal data (GMO Aozora Net Bank, PLAID "KARTE", AXA Non-Life "MyAXA", Wakao Sogo Butai, NTT Sonority, Turing, Iore, Shibuya City's web-filtering case, Dentsu Soken's iPLAss vulnerability notice, Medi Face, Meiji Gakuin University, Tokyo Sunbeams, Keio Corporation, Cocopeli, Kodaira City); not external unauthorised access (SOURCENEXT's inquiry form, paiza's staging environment); outside the period (Geniee, first notice 21 May 2026); not a Japanese organisation (Notion Labs, Inc.). Keio ("we are investigating the scope of impact, including leakage") and Iore (other organisations' notices on the same Fireworks AI case describe unauthorised access) are boundary cases for the author.

## Pending verification (outside the ledger)

Known through the press or secondary sources, but not admitted because the author could not open the primary notice. Each becomes a row when its primary notice is verified. Press-based scales are given for reference only and are not ledger figures.

| Organisation | Disclosed | Press-based scale | Reason not admitted |
|---|---|---|---|
| Bookoff Group Holdings | 2026-10-09 | up to approx. 6.43 million (reported footnote: member-number count, not persons) | TDnet PDF could not be retrieved |
| Sagawa Express | 2026-09-30 / 10-01 | under investigation | notice page requires JavaScript; body not retrieved |
| Uzabase (NewsPicks) | 2026-10-08 | under investigation | notice body not retrieved |
| Daiwa Securities | 2026-10-05 | approx. 220,000 records (approx. 110,000 persons) | TDnet PDF not retrieved; contractor's notice (022) admitted |
| View Card | 2026-10-09 | approx. 4.03 million | PDF body not retrieved |
| JR Kyushu | 2026-10-09 | up to approx. 1.3 million | primary notice not retrieved |
| Nikkei Inc. | approx. 2026-10-04 | 1,646 persons and others | primary notice not retrieved |
| Shueisha | 2026-09-28 | 2,835 bloggers and others | PDF body not retrieved |
| Recruit (StudySapuri) | 2026-10-03 | 3,687 records | primary notice not found |
| Ticket Plus | 2026-10-01 | up to 107 persons | primary notice not found |
| Japan Atomic Energy Agency | 2026-10-01 | 175 persons | primary notice not retrieved |
| Murauchi.com | Sep–Oct 2026 | 7,716,811 records (secondary) | primary notice not retrieved |
| Sakura Internet | 2026-09-10 (3rd notice) | up to 1,360,563 accounts (secondary) | primary notice not retrieved |
| Fines | Sep–Oct 2026 | 1,536,322 records (secondary) | primary notice not retrieved |
| White Essence | Sep–Oct 2026 | approx. 1.05 million accounts (secondary) | primary notice not retrieved |
| SoftBank | — | — | named in press; no matching primary notice found |

The pending list includes Bookoff (6.43 million), Murauchi.com (7.72 million) and View Card (4.03 million), which would rank near the top by size. The first-edition ledger is not the whole of the autumn of 2026; it is the part the author could reach in primary sources.

(Added 16 October 2026)  
On 16 October the author retried all 16. The result falls into three groups. The body of the primary notice was reached for nine: View Card, JR Kyushu, Nikkei Inc., Shueisha, Recruit (StudySapuri), Ticket Plus, Japan Atomic Energy Agency, Sakura Internet and Fines. Partial reach (heading and meta description only, a second notice published only as an image, or only the contractor's notice) for three: Uzabase, Daiwa Securities and White Essence. Still unreachable are three: Bookoff (TDnet PDF not retrievable; a second notice dated 13 October is confirmed in the listing), Sagawa Express (notice page requires JavaScript) and Murauchi.com (notice page returns an error). For SoftBank no notice of its own was found; only the subsidiary IDC Frontier's notices (023) exist, so no separate row can stand. Of the nine reached, Ticket Plus states 「不正アクセスおよびデータベースの改ざんは確認されておりません」 (no unauthorised access or database tampering confirmed) and does not meet the admission criterion added on 11 October (external unauthorised access). For the remaining eight and the three partial cases, the author will read the notice body and verify before deciding on admission in the second edition. This addition records reachability; it is not an admission decision.

(Added 16 October 2026)  
After recording the reachability above, the author opened and read the primary notices of five cases on the same day and admitted them as rows: Bookoff (032, TDnet disclosure of 9 October 2026), Daiwa Securities (033, 5 October 2026), Sagawa Express (034, second notice), Uzabase (035, first notice) and White Essence (036, 5 October 2026). Eleven cases remain pending. Bookoff's second notice, Sagawa Express's third and fourth notices and Uzabase's second notice have not yet been read by the author. For Murauchi.com, the summary page the author could read (updated 15 September 2026) states no count; it stays pending until the author reads the second notice that does.

(Added 26 October 2026)  
On 26 October the author retried the 11 pending cases and added the cases disclosed since 16 October. Six moved into the ledger: Shueisha (037), JAEA (039), Recruit/Study Sapuri (040), Nikkei (041), Viewcard (042; its notice is a PDF under jreast.co.jp/card, not viewcard.co.jp), JR Kyushu (043). Two were removed: Ticket Plus, whose notice says 「不正アクセスおよびデータベースの改ざんは確認されておりません」 and attributes the incident to a cache-setting change, so it does not meet the admission criterion; and SoftBank, for which no notice of its own was found (the 19 October suspension of My SoftBank reports a detected attempt, not a leak). Three remain: Murauchi.com (page unreachable), Fines (body URL unreachable), Sakura Internet (primary notice reached, but the count first appeared in the second notice of 19 August, before the 1 September cut-off; admission is the author's call). Twenty-two were added: two reached but needing a judgement (E-Store, first notice 1 August, final notice 16 October 「約23,356,000人」; MOS Food Services/Value Design, where the data is card numbers, PINs and balances and the contractor states no personal data), one reached but unread (Daiwa Institute of Research), and 19 unreachable (Nifty, Recruit/Carsensor, Hankyu Hanshin Department Stores, Fuji Television, Xebio, Yamada Holdings, Good Smile Company, Kakao Piccoma, Niigata Nippo, Japan Post, Igreks, Chariloto, Burger King Japan, Aena, Medley, ACCESS, FutureShop, Tradeworks and others). Pending is now 25. The full list, in Japanese, is in the Japanese edition and in `data/registry.json`. Pending still includes cases that would rank near the top by size: Sagawa Express's fifth notice (press: up to approx. 53.23 million; row 034 exists but its scale is unread), E-Store (approx. 23.36 million persons), Burger King (approx. 11.18 million). The third edition, too, is the range the author could reach, not the whole of the autumn.

(Added 3 November 2026)  
Of the 25 pending cases, 14 were admitted (072, 073, 093, 094, 095, 096, 105, 111, 117, 120, 121, 132, 133, 134) and 11 remain. 56 new cases were added to the pending list; it now holds 67 cases (full list in `data/registry.json` and the Japanese text). Pending cases include Sony Life (press: approx. 385,000), Netmile (press: up to approx. 5.49 million persons), Mainichi, Asahi and Impress (Yumirlink chain) and Satofull. Clients of the blastmail, NEC, FutureShop and IDC Frontier chains disclosed 9–23 October have not been surveyed exhaustively, and disclosures by Arara's clients began only on 2 November. The fourth-edition ledger, too, is the range the author could reach in primary sources, not the whole of autumn 2026.

(Added 8 November 2026)  
On 8 November the author retried the 67 pending cases and surveyed disclosures of 3–8 November. 14 moved into the ledger (301, 302, 304, 306, 307, 308, 310, 311, 313, 315, 316, 317, 318, 319). Six pending entries (Syuppin, Tricycle, Generic Pharmaceutical, So-net, Saitama/Kawagoe High School, Shizuoka Maaru) had already been admitted as rows in the fourth edition (131, 167, 218, 178, 219, 300) — a reconciliation miss, now removed from the list. 16 more were removed: 2 out of period (Sakura Internet, E-Store; first notices before 1 September) and 14 reached but not meeting the criteria (no personal data; no leak or no mention of one; no wording of unauthorised access; confirmed "not affected"; reposts only; access traces with no possibility of exfiltration — Moi). 36 remain unreachable, and 55 new cases were added (largest unreachable: Asoview, 15,821,184 per secondary sources; Kakaku.com approx. 5.7 million; ODK Solutions 791,551). The pending list now holds 91 cases; the full list as of 8 November is in the Japanese edition and in `data/registry.json`.

(Added 10 November 2026)  
On 10 November, 5 pending cases moved into the ledger: JERA Sunday (508), Okazaki (514), Hatoya (516), Aioi Nissay Dowa Insurance (556) and Mitsui Sumitomo Insurance (560; the 3 November notice announced a suspension, and the leak was announced on 6 November). Sony Life, the Metropolitan Police Department, Osaka City (premium vouchers) and SBC Shinetsu Broadcasting were retried without success. Sony Life is reported to have announced on 9 November a further approx. 2.9 million records, over 3.2 million in total; it remains among the largest pending cases. 24 cases were added, among them notices of 8–9 November that could not be read (Sony Small Amount and Short Term Insurance, NTT DATA, ENEOS Charge Plus, FWD Life, teket), unreached notices in the Prestige Core Solution chain, LENDY Servicer itself, the second notice of existing row 356, candidates found but not yet fetched, and Institute of Science Tokyo. 110 cases are pending; the full list is in `pending` in `data/registry.json`.

(Added 14 November 2026)
On 14 November, all 110 pending cases were retried. 23 moved into the ledger (585, 589, 599, 600–603, 608, 609, 619–623, 637–643, 716, 717), and Nasushiobara (722) moved during the 10–13 November search. Meiji Gakuin University was removed because its notice says no leak of personal data was confirmed, and Hasegawa was removed as the same case as existing row 372. The remaining 85 stay pending because the notice could not be reached (domain-wide blocking, robots refusal, retrieval errors, JavaScript-rendered pages) or the text did not confirm the admission rule; their reasons now begin "2026-11-14 再試行". 35 cases were added, including teket organisers that report only unauthorised access (Showa University of Music, Toyo Eiwa Jogakuin, Kagoshima Wind Band Association), cases still under investigation (Chikugo, Palma), Notion-processor cases not readable or not confirmed (SecureNavi, Yayoi), OPENLOGI clients not reached (HUMAN MADE, Tsunaide) and large cases not readable (Yomiuri Giants, 807,030 per the aggregator). The pending list now holds 120 cases.

---

# Chapter 5: Eight explanations — supported, refuted, undetermined

Why did large breaches concentrate in Japan in the autumn of 2026? This chapter tests eight candidates on identical criteria. For each, it first writes what would be observed if the candidate were true, then whether it was observed. No candidate is investigated more thoroughly because it is preferred.

## H1: Attacker-side AI made vulnerability discovery and attack automation cheap

**Would be observed**: traces of AI tools in notices or forensic reports.

**Observed?** In Korea, yes (Chapter 3, Tier 1). In Japan, no: none of the 31 notices mentions attacker-side AI, and Trend Micro's own text says "not necessarily evidence."

(Added 16 October 2026)  
The notices of all 36 rows, including the five added, contain no description of attacker-side AI.

**Verdict**: supported for Korea. Causation for the Japanese wave **undetermined**.

(Added 26 October 2026)  
For Japan, what should be observed was observed: JPCERT/CC (15 Oct) confirmed attackers "using AI" on attack-source servers and (23 Oct) attack attempts abusing Cairn, CyberStrikeAI and ARTEX (Chapter 3). None of the 71 notices describes attacker-side AI. The verdict splits: **that attackers used AI in Japan — supported (JPCERT/CC, primary); that this caused the breaches in the ledger's rows — undetermined (no primary source ties a document to a row).** On cost, Gambit Security and NorForge give estimates for overseas campaigns; there is none for Japan.

## H2: Stronger disclosure rules made previously unreported incidents visible (an apparent increase)

**Would be observed**: growth mainly in small incidents, with large incidents already disclosed before; a step change at the date of a rule change.

**Observed?** The reporting duty under the Act on the Protection of Personal Information began in April 2022; no primary source shows a new duty taking effect just before September 2026. Tokyo Shoko Research's count of million-plus breaches rose from 6 to 10, which an apparent increase does not explain. But the same-basis monthly series for the past three years has not been retrieved.

**Verdict**: weakly supported as an explanation for the autumn concentration. **Undetermined**.

## H3: Japan-specific weaknesses (contractor management, legacy web apps, authentication, VPN devices)

**Would be observed**: vectors skewed toward a particular weakness, at a higher rate than abroad.

**Observed?** The ledger shows contractor 5, vulnerability 5, VPN 1, misconfiguration 1, unauthorised login 1 — no skew; 17 rows state no vector. No same-basis statistics for comparison abroad were obtained.

(Added 16 October 2026)  
Across 36 rows — contractor 6, vulnerability 6, VPN 1, misconfiguration 1, unauthorised login 1, multiple 1 — there is still no skew toward one weakness. Rows with no vector are now 20.

(Added 26 October 2026)  
Across 71 rows: contractor 16, vulnerability 12, unauthorised login 4, misconfiguration 2, VPN 1, multiple 1, not disclosed 35. The growth since 16 October is in contractor (+10) and unauthorised login (+4); the contractor growth comes from chains starting at mail-delivery and web-building SaaS (Chapter 2, seven chains). For late October, "contractor management" is observed as a skew. But a shared SaaS platform falling and every client disclosing is not specific to Japan, and no comparable overseas statistic has been obtained.

**Verdict (26 October 2026)**: weaknesses supported; a skew toward contractors supported for late October; Japan-specificity **undetermined** (unchanged).

(Added 3 November 2026)  
In 300 rows contractor is the largest class (179) across the whole period, not only late October; Trend Micro (16 Oct, primary) counts "data supply-chain" cases at 62 (10.2%) for January–September. Chain origins include non-Japanese platforms (Amadeus; Securitize), so the structure is not Japan-specific. **Verdict (3 November 2026)**: skew toward contractors supported for the whole period; Japan-specificity **undetermined**.

**Verdict**: the existence of weaknesses is supported; their Japan-specificity is **undetermined**.

## H4: A single attacker or campaign

**Would be observed**: shared IPs, techniques or attribution between the Japanese and Korean incidents.

**Observed?** For the Korean financial institutions, CrowdStrike analysed overlapping infrastructure as one campaign. For Japan, no primary source indicates a single attacker. What the Japanese rows share are contractor vectors (IDC Frontier, Commune), which are not attribution. JPCERT/CC calls its information "limited and fragmentary."

(Added 26 October 2026)  
Two primary sources were added. JPCERT/CC (15 Oct) wrote that several attack-source servers were confirmed and "were also attacking web services for regions other than Japan" — several servers attacking Japan and elsewhere, with no statement either way on a single actor. Press-based: GMO Cybersecurity by Ierae reported attack infrastructure targeting about 20 Japanese companies, six further hosts of the same kind, and called the eight disclosed leaks among the targets "the work of the same attack group"; the original is unread and the eight are unidentified. NorForge's Cairn clusters target US, Japanese and Australian retailers and are not tied to the Korean financial campaign.

**Verdict (26 October 2026)**: within Korea — supported (unchanged). Shared attack infrastructure against multiple Japanese organisations — supported in the press, "several confirmed" in the primary source. A joint Japan–Korea campaign — **undetermined** (unchanged).

(Added 3 November 2026)  
Mail-delivery SaaS providers were breached in succession in October (053 Yumirlink, detected 16 Oct; 059 Rakus blastmail, 21 Oct; 241 Arara, 28 Oct), but their notices describe different vectors and no primary source links them to one attacker. **Verdict (3 November 2026)**: succession of the same type of target observed; a single attacker **undetermined**.

**Verdict**: supported within the Korean financial sector. A joint Japan–Korea campaign **undetermined**.

## H5: Diffusion of intrusion tools published in 2026 (ARTEX and others)

**Would be observed**: reports of abuse in several countries and organisations after publication.

**Observed?** ARTEX's GitHub releases run from v0.1.0 on 26 July 2026 to v0.3.14 on 24 September (verified by the author on 10 October). CrowdStrike's Korean campaign, late September to early October, follows the latest release immediately. The only reported abuse is the one Korean campaign; no primary source places ARTEX in a Japanese incident.

**Verdict**: supported for Korea. Explanation of the Japanese wave **undetermined**.

(Added 26 October 2026)  
A primary source now places ARTEX in Japan: JPCERT/CC's 23 October alert, 「CairnやCyberStrikeAI、ARTEXなどのAIを用いたペネトレーションテスト基盤を悪用した攻撃試行が確認されています」. Of the three tools, ARTEX is the one this chapter named in the first edition; Cairn was reported by Gambit Security on 22 September (overseas retailers) and by NorForge on 19 October (targets including a Japanese retailer); CyberStrikeAI by Team Cymru on 2 March (FortiGate devices). What should be observed — public tools abused in several countries — was observed in Japan. What was confirmed is "attack attempts"; which rows, if any, were breached by these tools is not stated.

**Verdict (26 October 2026)**: Korea — supported (unchanged). Japan — tool diffusion and attack attempts supported (JPCERT/CC, primary); explanation of the ledger's rows **undetermined**.

## H6: Defender-side AI disclosed vulnerabilities that attackers exploited before patches

**Would be observed**: breach vectors matching CVEs found and disclosed by Glasswing.

**Observed?** None of the 31 notices cites a CVE number. No primary source links a Glasswing-found vulnerability to a Japanese incident. Anthropic's initial update (22 May) reports 530 disclosures, 75 patched and 65 public advisories, but nothing says any of them was exploited in Japan.

(Added 16 October 2026)  
None of the 36 notices, including the five added, cites a CVE number.

(Added 26 October 2026)  
None of the 71 notices cites a CVE number. The one primary source that does is JPCERT/CC's alert, Case C: 「MetabaseのSQLインジェクションの脆弱性（CVE-2026-72898）」, with suspicious IPs active from early August to early September. Nothing the author has read says whether that vulnerability was a Glasswing finding. The late-October rows that state "vulnerability" (007, 051, 053, 068, 070) name none; 007 Times Mobility withheld the method to prevent secondary harm.

**Verdict (26 October 2026)**: **no supporting primary source** (unchanged).

**Verdict**: **no supporting primary source**. This is the third of the four claims the Prologue says the book will not write.

## H7: Growth of the market in stolen credentials

**Would be observed**: large breaches entering through unauthorised logins or credential stuffing.

**Observed?** The notices of the large rows (Helpfeel, Times, Monogatari, Lawson, skyticket, Daiichikosho) do not name credential stuffing or password reuse as the vector. Only Scala Communications (022) states an unauthorised login. Charm (001) says the origin of the e-mail addresses and passwords used for unauthorised logins "has not been identified."

**Verdict**: leaning refuted for the large rows. Overall **undetermined**.

(Added 26 October 2026)  
Rows stating unauthorised login with stolen credentials rose from one to four (041, 045, 062, and 057 under contractor). All describe the credentials as 「何らかの手段で窃取」 or 「不正に取得」, none as bought on a market. The large rows (044, 064, 055, 067, 038) still do not cite unauthorised login.

**Verdict (26 October 2026)**: leaning refuted for the large rows (unchanged); credential theft observed in more small and mid-size rows, link to a growing market **undetermined**.

(Corrected 3 November 2026)  
"Leaning refuted for the large rows" no longer holds. 028 skyticket's 3rd notice (30 Oct) writes that 「不正に取得された認証情報が悪用され」 (illegitimately obtained credentials were abused); 290 Prestige International (up to approx. 5.5 million) invalidated 「不正に利用された認証情報」; 053 Yumirlink found attackers had obtained support staff credentials. All three describe credentials taken during the intrusion, not bought on a market. Credential-stuffing and brute force appear in small rows (185 MICIN, 277 e+, 293 Life Corporation). **Verdict (3 November 2026)**: "leaning refuted" withdrawn; credential abuse observed in large rows; link to a credential market **undetermined**.

## H8: Chance or seasonality

**Would be observed**: comparable concentrations in the same months of the past three years.

**Observed?** In the press-based Trend Micro tally, 2026's busiest month is June (76), not September (Chapter 1); the count shows no September seasonality. Size, by Tokyo Shoko Research's year-on-year comparison, rose from 6 to 10 million-plus breaches, with no basis for treating it as chance. Same-basis monthly series by size for the past three years were not obtained.

**Verdict**: **undetermined** — with no positive evidence that this is a normal year either.

## The eight together

| Candidate | Verdict |
|---|---|
| H1 Attacker-side AI | Korea: supported / Japan: undetermined |
| H2 Disclosure rules | undetermined (weak) |
| H3 Japan-specific weaknesses | weaknesses: supported / specificity: undetermined |
| H4 Single attacker | within Korea: supported / Japan–Korea: undetermined |
| H5 Tool diffusion | Korea: supported / Japan: undetermined |
| H6 Defender-side disclosure | no supporting primary source |
| H7 Credential market | large rows: leaning refuted / overall: undetermined |
| H8 Chance / seasonality | undetermined |

For Japan, not one of the eight can be called supported. Nor can any be called refuted beyond H6's "no supporting source" and H7's "leaning refuted."

This is everything that can be said from primary sources as of 10 October 2026. The book exists to fill in this table.

(Added 26 October 2026)  
The table as of 26 October 2026:

| Candidate | Verdict (2026-10-26) | Change |
|---|---|---|
| H1 Attacker-side AI | Korea: supported / Japan: attacker-side AI use supported (JPCERT/CC); causation for the rows undetermined | Japan's verdict split |
| H2 Disclosure rules | Undetermined (weakly supported) | None |
| H3 Japan-specific weaknesses | Weaknesses supported / contractor skew supported for late October / specificity undetermined | Contractor skew added |
| H4 Single attacker | Korea: supported / Japan: "several servers confirmed" in the primary source / Japan–Korea: undetermined | More primary sources |
| H5 Tool diffusion | Korea: supported / Japan: attack attempts supported (JPCERT/CC); explanation of rows undetermined | Japan's verdict split |
| H6 Defender-side AI disclosures | No supporting primary source | None |
| H7 Credential market | Large rows: leaning refuted / overall undetermined | More unauthorised-login rows |
| H8 Chance or seasonality | Undetermined | None |

For Japan, parts of two candidates can now be called supported: H1's "attackers used AI" and H5's "public tools were used in attack attempts in Japan." Both are facts on the attacker's side; the tie to the ledger's rows — the victims' side — stays undetermined. The gap the first edition described has, as of 26 October, been half filled, from the attacker's side.

### References

- Personal Information Protection Commission, 漏えい等の対応とお役立ち資料 https://www.ppc.go.jp/personalinfo/legal/leakAction/
- GitHub, Autumn-27/ARTEX, Releases (retrieved 10 October 2026) https://github.com/Autumn-27/ARTEX/releases
- Anthropic, "Project Glasswing: An initial update," 22 May 2026 https://www.anthropic.com/research/glasswing-initial-update
- and the references of Chapters 1, 3 and 4

---

# Chapter 6: The defender's bet — Glasswing's timeline and ARTEX's

The book's question is whether the defender's head start holds. This chapter lays the defender's timeline beside the attacker's. Not to assert a cause: so that readers can measure the distance between the two for themselves.

## The defender: Project Glasswing

| Date | Event | Primary wording |
|---|---|---|
| 2026-03-26 | A misconfigured external CMS at Anthropic made draft content about an unreleased model viewable | No standalone Anthropic statement found. Company response to Fortune: "An issue with one of our external CMS tools led to draft content being accessible," "human error in the CMS configuration" (press-based) |
| 2026-04-07 | Project Glasswing announced. Claude Mythos Preview, "a general-purpose, unreleased frontier model," provided to defending organisations only | "giving defenders a durable advantage in the coming AI-driven era of cybersecurity." Twelve launch partners (AWS, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks) and "over 40 additional organizations." "up to $100M in usage credits," "$4M in direct donations." "within 90 days, Anthropic will report publicly on what we've learned" |
| 2026-05-22 | Initial update | "approximately 50 partners" have found "more than ten thousand" vulnerabilities; "disclosed 530 high- or critical-severity bugs to maintainers," of which "75 … have now been patched" and "65 of those have been given public advisories." "The software industry's longstanding convention is to disclose new vulnerabilities 90 days after they're discovered." |
| 2026-06-02 | Expansion | to more than 15 countries and approx. 150 new organisations (Anthropic) |
| 2026-10-06 | Folded into the Cyber Verification Program | "our partners uncovered at least 129,000 verified software vulnerabilities between April and July 2026" (partial data from 33 partner reports). "Existing members of Project Glasswing will transition to this tier" |

In four months, defender-side AI found "at least 129,000" verified vulnerabilities. As of 22 May, 75 of 530 disclosed had been patched. There is a distance between the speed of finding and the speed of fixing. That distance sits at the centre of the book's question — and, as Chapter 5's H6 records, no primary source connects it to a Japanese breach.

## The attacker: ARTEX

| Date | Event | Basis |
|---|---|---|
| 2026-07-26 | ARTEX v0.1.0 published on GitHub by Autumn-27 (「AI 自主渗透测试系统」, AI autonomous penetration-testing system) | GitHub releases (verified by the author, 2026-10-10) |
| 2026-08-11 to 09-24 | v0.2.0 to v0.3.14 released (eight releases in September) | same |
| late Sep – early Oct 2026 | ARTEX used against South Korean financial institutions | CrowdStrike: "The campaign was active from late September to early October 2026." |
| 2026-10-07 | CrowdStrike publishes | as above |
| approx. 2026-10-08 | Developer reported to announce closed-sourcing, citing abuse | Press-based. When the author checked the GitHub profile and repository README on 10 October, no such statement was present and the repository remained public |

(Added 26 October 2026)  
Japan entered ARTEX's timeline: 2026-10-15, JPCERT/CC confirms attackers "using AI" on attack-source servers (no tool named; primary); 2026-10-19, GMO Cybersecurity by Ierae reports ARTEX on infrastructure targeting about 20 Japanese companies (press-based; original unreachable); 2026-10-23, JPCERT/CC adds Case E naming Cairn, CyberStrikeAI and ARTEX (primary). The repository's current state (public, private or deleted) could not be checked from the author's working environment on 26 October. Two further tools now sit beside ARTEX. **CyberStrikeAI**: open source by "Ed1s0nZ"; Team Cymru reported on 2 March 2026 its use against FortiGate firewalls (21 IPs running it between 20 January and 26 February; press-based, the report unread). **Cairn**: "an autonomous penetration testing engine"; Gambit Security reported on 22 September 2026, from an attacker's staging server, "105 attack projects" against overseas retailers, "at least 27 companies were compromised," at "a mean of $25.46 over 101 completed scans"; NorForge reported on 19 October 2026, from "more than 20" exposed panels, a cluster targeting US, Japanese and Australian retailers, with successful break-ins taking "a little under 23 hours" and an estimated cost of about $5 per task. The three tools share three things: each was published as open source for penetration testing; the models were not an unreleased frontier model but ones anyone can call by API (DeepSeek v4.1 Flash, GLM, Grok, Opus 4.6); and the evidence came from the attacker's side (staging server, control panels, attack-source servers). What the first edition called "the diffusion of mid-tier capability" is, as of 26 October, a story of three tools rather than one. No new Anthropic primary source on Glasswing or the Cyber Verification Program appeared between 6 and 26 October, as far as the author could find; the defender's timeline stops at 6 October.

The repository had 17 stars when the author checked. What attacked Korean banks was not a famous tool but one published two months earlier and barely known. The models were not an unreleased frontier model but DeepSeek v4.1-flash, GLM-5.3 and Grok 4.6, all available to anyone through an API.

## Between the two timelines

The defender handed an unreleased frontier model to chosen organisations. The attacker used a public tool and inexpensive models.

Glasswing presupposed that frontier capability would, for now, be held by few. The Korean case showed that a public tool and inexpensive models suffice to exfiltrate data from financial institutions. These do not contradict each other. Glasswing manages frontier capability; ARTEX is the diffusion of mid-tier capability.

What the book asks is whether the defender's head start holds against this diffusion of mid-tier capability. Glasswing's 129,000 is not an answer to that. The answer lies in how the ledger of Chapter 4 moves from here.

## On Claude Mythos

The book does not write that Claude Mythos was used in any attack in Japan or Korea. Anthropic's primary sources describe Mythos Preview as "unreleased." The models in CrowdStrike's report are DeepSeek v4.1-flash, GLM-5.3 and Grok 4.6; Claude Code was used as a tool, and CrowdStrike does not name its model. No Japanese notice contains the word Mythos.

"What was feared about Mythos has happened" does not mean Mythos was used. It means the fear — that AI makes vulnerability discovery cheap — may have come true at a layer other than Mythos. The book keeps that distinction.

### References

- Anthropic, "Project Glasswing," as above (Prologue)
- Anthropic, "Project Glasswing: An initial update," as above (Chapter 5)
- Anthropic, "Expanding Project Glasswing," 2 June 2026 https://www.anthropic.com/news/expanding-project-glasswing
- Anthropic, "Expanding the Cyber Verification Program," 6 October 2026 https://www.anthropic.com/news/cyber-verification-program
- Fortune, 26 March 2026 (Anthropic's response, press-based) https://fortune.com/2026/03/26/anthropic-leaked-unreleased-model-exclusive-event-security-issues-cybersecurity-unsecured-data-store/
- GitHub, Autumn-27/ARTEX, as above (Chapter 5)
- CrowdStrike Intelligence, as above (Prologue)

---

# Chapter 7: Japan as an observation point — what can and cannot be said

## Twenty of thirty-five

Nikkei Asia reported that of 35 breaches of 100,000 or more people disclosed worldwide since September 2026, 20 were in Japan, affecting 57 million people (relayed by Business Standard, 9 October 2026; Nikkei Asia's text could not be retrieved directly owing to robots restrictions — press-based).

Reuters reported on 9 October under the headline "South Korea, Japan buffeted by hacks as AI lowers bar for cybercriminals," placing the two countries together. The same report does not describe a worldwide surge.

From these two reports: **the disclosure of large breaches in the autumn of 2026 is concentrated in Japan and South Korea.**

Part of that concentration is structural. Nikkei's tally counts *disclosed* incidents. Since April 2022 Japan has required reporting of certain breaches to the Personal Information Protection Commission and notification of the individuals concerned, and companies disclose. Incidents in countries without such disclosure do not enter the tally. The book records this as "undetermined" under H2.

## The world's large cases, and where the evidence is

Of the same period's breaches of 100,000 or more outside Japan, what the author could verify in primary sources:

- **IDScan.net (United States)**: the company's notice (filed with Massachusetts) states "an unauthorized third party may have accessed and/or copied certain customer information" and gives no number. The "153 million" in the press is a dark-market claim, not a company figure. No reference to attacker-side AI.
- **Dodo Brands (Kazakhstan and others)**: no company figure; "68 million" is the attacker's claim. No reference to attacker-side AI.
- **South Korean financial institutions**: AI use reported with evidence by CrowdStrike (Chapter 3); number of affected organisations unconfirmed.

The world's two largest cases carry no AI evidence. The one case with evidence is smaller than Japan's. **Scale and AI evidence are not in the same place.**

## What can be said

1. In the autumn of 2026, personal-data breaches disclosed by Japanese companies and organisations reached a scale without precedent in fourteen years (Tokyo Shoko Research, primary).
2. The disclosed vectors are scattered; no primary source indicates a single technique (Chapter 4, primary).
3. None of the 31 Japanese notices mentions attacker-side AI (Chapter 4, primary).
4. In Korea, evidence of attacker-side AI came from the attacker's own machine (CrowdStrike, primary).
5. The tools were an open-source project two months old and models anyone can use (CrowdStrike, GitHub, primary).

(Added 16 October 2026)  
Item 3 holds for all 36 notices, including the five rows added on 16 October 2026.

(Added 26 October 2026)  
Item 3 holds for all 71 notices. Two items are added: 6. In Japan, several attack-source servers on which attackers used AI existed and also attacked targets outside Japan (JPCERT/CC, primary). 7. In Japan, attack attempts abusing public AI pentesting tools (Cairn, CyberStrikeAI, ARTEX) were confirmed (JPCERT/CC, primary). Of what cannot be said, item 1 changes form: whether AI was used in attacks on Japan can now be said (items 6 and 7); what cannot be said is which of the 71 rows' breaches, if any, involved AI. Items 2–4 are unchanged. On 26 October, Japan is an observation point where the AI evidence exists only on the attacker's side; the 71 victims' notices still contain none.

(Corrected 3 November 2026)  
Statement 3 no longer holds as of 3 November 2026: one of 300 notices (079 Chitose Group) presumes attacker-side AI (Chapter 3, Tier 3). It now reads: "Of 300 Japanese notices, one mentions attacker-side AI about its own incident, as a presumption."

(Added 3 November 2026)  
8. October's disclosures far exceeded the January–September daily average, but much of the increase is clients disclosing intrusions at a few contractors (Trend Micro, ledger; Chapter 1).
9. Collapsing contractor chains, the 300 rows correspond to roughly 144 independent intrusions, of which notices disclose the vector for about a third (ledger; Chapter 2).

## What cannot be said

1. Whether AI was used in the Japanese breaches.
2. Why the Japanese breaches increased.
3. Whether the Japanese and Korean attackers are the same.
4. Whether Glasswing-found vulnerabilities were exploited.

## As an observation point

Japan is the largest observation point for the autumn of 2026: there is a disclosure regime, the notices can be read in Japanese, and 20 of 35 cases are here.

Japan is also the observation point with not one piece of AI evidence.

Where both are true at once, the book places its ledger. If evidence appears, a tier rises. If it does not, its absence is recorded. To the book, both outcomes are of equal value.

### References

- Business Standard, "Global data breaches exposed 320 mn people's info since September: Report," 9 October 2026 (relaying Nikkei Asia; press-based) https://www.business-standard.com/technology/tech-news/global-data-breaches-320-million-people-september-india-cyber-attacks-126100900461_1.html
- Reuters, "South Korea, Japan buffeted by hacks as AI lowers bar for cybercriminals," 9 October 2026 (press-based)
- IDScan.net, Notification of Data Security Incident (Massachusetts filing) https://www.mass.gov/doc/2026-1577-idscannet/download
- CrowdStrike Intelligence, as above (Prologue)

---

# Epilogue: The ledger does not close

This book has answered nothing.

Not "was AI the cause." Not "why Japan." Not "does the defender's head start hold."

It has not answered because the primary sources do not contain the answers. The book writes nothing that the primary sources do not. That is the one discipline this twenty-fourth book shares with the other twenty-three.

## What the book did

Three things.

**First**, it opened the notices and laid them out in their own units and wording. Thirty-one rows. It made no "tens of millions of people." It recorded the "件" under the heading "対象人数" as "件."

**Second**, it sorted "AI was used" into four tiers. Evidence: one in Korea, zero in Japan. The Trend Micro words quoted as a trace read, in the original, "not necessarily evidence."

**Third**, it tested eight explanations on identical criteria. For Japan, not one was supported.

## What the book will do

The ledger will be appended.

The sixteen pending cases become rows as their primary notices are verified. When Bookoff's 6.43 million, Murauchi.com's 7.72 million and View Card's 4.03 million enter, the count of million-plus rows in Chapter 1 changes; the change is appended and marked.

(Added 16 October 2026)  
Five pending cases, including Bookoff (6.43 million), have become rows. Million-plus rows in Chapter 1 rose from 8 to 10, and 11 cases remain pending.

(Added 26 October 2026)  
On 26 October 35 rows were added: 71 rows, 25 pending; 21 rows above one million, 5 above ten million. Chapter 3's evidence tier gained Japan's attack-source servers (JPCERT/CC). Chapter 5's H1 and H5 split into "supported" for the attacker's side and "undetermined" for the tie to the rows. Chapter 6's attacker timeline became a story of three tools. Thirty-five rows in ten days is what the author could open, not the whole of what was disclosed; the aggregator's daily lists ran to dozens of organisations a day between 16 and 25 October, and what the ledger has not caught up with sits outside it, as pending or not yet even pending.

Chapter 3's tiers rise if evidence appears. If an attacker's files are exposed in a Japanese case, it becomes Tier 1. If not, the absence remains.

Chapter 5's verdicts change as primary sources appear: the Commission's annual report for H2; a security firm's report on a Japanese case for H1 and H4.

Chapter 6's timelines lengthen with Glasswing's next report and the next tool to be published.

## The connection to the forecast registry

Before this book, the author published *The AI Forecast Registry*, which records forecasts about AI before they are settled and follows their outcomes in the forecasters' own words.

Glasswing's announcement spoke of "giving defenders a durable advantage." That is a forecast. It has no deadline, no magnitude, no resolution condition. It has a subject: the defender's durable advantage.

This ledger can be where that forecast's outcome is observed. If large breaches continue in Japan and AI evidence appears in their vectors, a durable advantage was not observed. If they do not continue, or no evidence appears, a different record remains. Both are in a shape the forecast registry's outcome layer can hold.

The book keeps observing.

## Last

On 7 October 2026, two documents appeared on the same day. One described the anomaly of scale in Japan; the other, the evidence of AI in Korea.

As of 10 October 2026, the distance between them has not closed.

This book is the ledger that keeps measuring it.

---

**Update procedure**: `docs/UPDATE_RUNBOOK.md`
**Machine-readable data**: `data/registry.json` (canonical), `data/registry.csv` (derived)
**Japanese edition**: `docs/jp/the-japan-breach-registry-2026_JP.md`
**Author and catalog**: https://github.com/Leading-AI-IO
