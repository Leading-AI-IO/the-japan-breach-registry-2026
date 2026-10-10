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

## Two chains

Two chains in the ledger spread from one origin to several organisations.

**IDC Frontier**: a ransomware attack beginning around 03:40 on 7 October (023) → JR East (027). Press reports extend it to View Card and JR Kyushu, whose primary notices could not be retrieved; they sit outside the ledger.

**Commune**: unauthorised access to Commune Inc.'s cloud service → WingArc1st (024), Sansan (030), LIXIL (031), each notified by the contractor around 6 October.

Neither chain implies a single attacker. What they show is a structure: when one contractor falls, its clients disclose together. Part of the clustering of disclosure dates on 8–9 October comes from this structure.

## Rows with no vector

Seventeen rows state none. Times Mobility (6.6 million accounts), Monogatari (10.79 million), Lawson (2.16 million), Seicomart (570,000 accounts), Dai-ichi Life (120,000). Many of the largest rows are here.

"Cause under investigation." That is the honest state of the notice. The book records it as "not disclosed" and does not fill it.

When JPCERT/CC wrote that technical information is "limited and fragmentary," it was writing about these seventeen rows.

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

## Tier 2: Trace

**Trend Micro (Security GO, 8 October 2026, Yuya Sato)**

Much Japanese coverage quoted Trend Micro as saying that "traces of attacks launched automatically using AI have also been confirmed." The book sought Trend Micro's own text. Its Security GO article of 8 October reads:

> 現状、必ずしもこれらの攻撃がAIを直接的に用いたものであるという証拠があるわけではありませんが、ログだけ見ても「これまでとは違う挙動」を捉えていることは事実です。

*(At present there is not necessarily evidence that these attacks used AI directly, but it is a fact that even the logs alone show "behaviour unlike before.")*

The original is more cautious than the quotation. It contains both "there is not necessarily evidence" and "behaviour unlike before." The book records the original wording.

**South Korean mega-churches (Oasis Security's CEO, press-based)**

According to the Dong-A Ilbo (7 October 2026), the CEO of Oasis Security said of documents organising the stolen data: 「포맷 자체가 AI를 활용했을 때 나오는 전형적인 형태였다」 *(the format itself was the typical form produced when AI is used)*. Press-based; the firm's own report was not retrieved.

## Tier 3: Possibility

**South Korean financial regulators (press-based)**

Korean press reported a regulatory official saying on 1 October 「전통적인 해킹 방식이 아닌 인공지능(AI)을 이용한 공격이라고 보고받았다」 *(we were briefed that it was an attack using AI, not a traditional hacking method)* and, in the same breath, 「정확한 해킹 방식 등은 점검 결과를 지켜봐야 알 수 있다」 *(the exact method can only be known after the inspection results)*. The chair of the Financial Services Commission said on 4 October 「확정적으로 말씀드리기는 어렵지만 AI를 활용한 해킹공격의 가능성도 배제할 수 없다」 *(it is hard to say definitively, but the possibility of an AI-assisted attack cannot be ruled out)*. All press-based.

The FSC's own releases of 2 and 6 October, as far as the author could read them, contain no reference to attacker-side AI. The "AI" in the 6 October release is a defender-side voice-phishing analysis platform.

**Korea Electric Power (press-based)**

Korean press reported KEPCO describing its own incident as 「최근 인공지능을 활용한 금융권 해킹 공격과는 관련이 없는 것으로」 *(unrelated to the recent AI-assisted attacks on the financial sector)*. A denial by the party itself.

## Tier 4: No mention

**All 31 Japanese notices**

None of the 31 notices in the ledger refers to AI on the attacker's side. "AI" appears in GMO Research & AI's company name, in WingArc1st's product name "dejiren AI," and in Helpfeel's service description — none a reference to attack technique.

JPCERT/CC's 8 October alert contains no "AI."

**Tokyo Shoko Research (7 October 2026)** writes 「AI普及で、より強固な対策が必要なのは当然だが」 *(with AI spreading, stronger measures are of course needed)* — a generality, not a claim about any incident.

## A dissenting view

Professor Hiroki Takakura of the National Institute of Informatics told ASCII of the Japanese cases: 「攻撃の自動化にAIが使われたとは思いますが、大きな役割は果たしていなかった。言い換えると、対策が不十分だった」 *(I think AI was used to automate the attacks, but it did not play a major role. In other words, the defences were insufficient.)* Press-based. The book records it on the same terms as the views that suspect AI.

## What the four tiers show

Evidence: one case in Korea, none in Japan. Trace: Trend Micro's own text says "not necessarily evidence." Possibility: the Korean regulators' remarks are press-based and absent from their own releases. No mention: all 31 Japanese notices.

This distribution does not mean AI was not used. It means that whether it was used cannot be determined from the Japanese notices. Recording what cannot be determined as undetermined is this chapter's job.

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

## Counting

- Of 31 rows, 14 notices state the vector; 17 do not.
- Vulnerability 5, VPN vulnerability 1, contractor 5, unauthorised login 1, misconfiguration 1, multiple 1.
- Notices mentioning attacker-side AI: 0.
- Rows exceeding one million in the notice's own unit: 8 (005, 007, 017, 021, 025, 026, 027, 028).
- Non-corporate organisations: 2 (002 Digital Agency, 015 JOGMEC).
- Rows whose subjects are employees rather than customers: 3 (002, 016, part of 026).

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

---

# Chapter 5: Eight explanations — supported, refuted, undetermined

Why did large breaches concentrate in Japan in the autumn of 2026? This chapter tests eight candidates on identical criteria. For each, it first writes what would be observed if the candidate were true, then whether it was observed. No candidate is investigated more thoroughly because it is preferred.

## H1: Attacker-side AI made vulnerability discovery and attack automation cheap

**Would be observed**: traces of AI tools in notices or forensic reports.

**Observed?** In Korea, yes (Chapter 3, Tier 1). In Japan, no: none of the 31 notices mentions attacker-side AI, and Trend Micro's own text says "not necessarily evidence."

**Verdict**: supported for Korea. Causation for the Japanese wave **undetermined**.

## H2: Stronger disclosure rules made previously unreported incidents visible (an apparent increase)

**Would be observed**: growth mainly in small incidents, with large incidents already disclosed before; a step change at the date of a rule change.

**Observed?** The reporting duty under the Act on the Protection of Personal Information began in April 2022; no primary source shows a new duty taking effect just before September 2026. Tokyo Shoko Research's count of million-plus breaches rose from 6 to 10, which an apparent increase does not explain. But the same-basis monthly series for the past three years has not been retrieved.

**Verdict**: weakly supported as an explanation for the autumn concentration. **Undetermined**.

## H3: Japan-specific weaknesses (contractor management, legacy web apps, authentication, VPN devices)

**Would be observed**: vectors skewed toward a particular weakness, at a higher rate than abroad.

**Observed?** The ledger shows contractor 5, vulnerability 5, VPN 1, misconfiguration 1, unauthorised login 1 — no skew; 17 rows state no vector. No same-basis statistics for comparison abroad were obtained.

**Verdict**: the existence of weaknesses is supported; their Japan-specificity is **undetermined**.

## H4: A single attacker or campaign

**Would be observed**: shared IPs, techniques or attribution between the Japanese and Korean incidents.

**Observed?** For the Korean financial institutions, CrowdStrike analysed overlapping infrastructure as one campaign. For Japan, no primary source indicates a single attacker. What the Japanese rows share are contractor vectors (IDC Frontier, Commune), which are not attribution. JPCERT/CC calls its information "limited and fragmentary."

**Verdict**: supported within the Korean financial sector. A joint Japan–Korea campaign **undetermined**.

## H5: Diffusion of intrusion tools published in 2026 (ARTEX and others)

**Would be observed**: reports of abuse in several countries and organisations after publication.

**Observed?** ARTEX's GitHub releases run from v0.1.0 on 26 July 2026 to v0.3.14 on 24 September (verified by the author on 10 October). CrowdStrike's Korean campaign, late September to early October, follows the latest release immediately. The only reported abuse is the one Korean campaign; no primary source places ARTEX in a Japanese incident.

**Verdict**: supported for Korea. Explanation of the Japanese wave **undetermined**.

## H6: Defender-side AI disclosed vulnerabilities that attackers exploited before patches

**Would be observed**: breach vectors matching CVEs found and disclosed by Glasswing.

**Observed?** None of the 31 notices cites a CVE number. No primary source links a Glasswing-found vulnerability to a Japanese incident. Anthropic's initial update (22 May) reports 530 disclosures, 75 patched and 65 public advisories, but nothing says any of them was exploited in Japan.

**Verdict**: **no supporting primary source**. This is the third of the four claims the Prologue says the book will not write.

## H7: Growth of the market in stolen credentials

**Would be observed**: large breaches entering through unauthorised logins or credential stuffing.

**Observed?** The notices of the large rows (Helpfeel, Times, Monogatari, Lawson, skyticket, Daiichikosho) do not name credential stuffing or password reuse as the vector. Only Scala Communications (022) states an unauthorised login. Charm (001) says the origin of the e-mail addresses and passwords used for unauthorised logins "has not been identified."

**Verdict**: leaning refuted for the large rows. Overall **undetermined**.

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
