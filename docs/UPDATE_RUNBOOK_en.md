# The Japan Breach Registry 2026 — Update Runbook

This file is public. The registry is written by one person, the author (see "Governance" in the README), and this runbook sets out the exact steps that person follows when adding or correcting rows, so that readers can verify them. The verifiability this book asks of its readers is applied here to the author's own working procedure.

**Target repository**: `https://github.com/Leading-AI-IO/the-japan-breach-registry-2026`
**Signing key**: `3DD95BA9EC194524` (`Satoshi Yamauchi <s3atoshi@gmail.com>`, ed25519). It is the same key as for `the-ai-forecast-registry`. The public key is registered on the author's GitHub account and can be checked against the `Verified` badge on each commit. The private key is not included here.
**Last updated**: 2026-10-26 (v3.0, 71 rows, 25 pending items. Follow-up additions and corrections reflected in 14 rows; 6 rows, 037–043, admitted from the pending list and 29 rows admitted from notices published from 16 October onward)
(Added 3 November 2026) 2026-11-03 (v4.0, 300 rows, 67 pending items. Follow-up additions and corrections reflected in 19 rows; 14 rows admitted from the pending list and 215 rows from notices published between 9 October and 2 November)
(Added 8 November 2026) 2026-11-08 (v5.0, 507 rows, 91 pending items. Follow-up additions and corrections reflected in 9 rows; 14 rows admitted from the pending list, 184 rows from notices published between 3 and 7 November, and 9 rows from notices published between 8 October and 2 November that the fourth edition had missed)
(Added 10 November 2026) 2026-11-10 (v5.0, 584 rows, 110 pending items. Before publication of the fifth edition, 5 rows were admitted from the pending list, 64 rows from notices published between 6 and 9 November, and 8 rows from notices published between 30 October and 5 November that the fourth edition and the 8 November additions had missed; follow-up additions were reflected in 2 rows)
(Added 14 November 2026) 2026-11-14 (v6.0, 844 rows, 120 pending items. 24 rows were admitted from the pending list, 128 rows from notices published between 10 and 13 November, and 108 rows from notices published between 7 September and 9 November that additions up to the fifth edition had missed; follow-up additions and corrections were reflected in 20 rows)
(Added 15 November 2026) 2026-11-15 (v6.1, 844 rows, 120 pending items. No rows were changed; English columns, `registry_en.csv` and `registry_en.json` were added, and `registry.csv` was made Japanese-only)
(Added 26 November 2026) 2026-11-26 (v8.0, 1,315 rows, 129 pending items. 13 rows were admitted from the pending list, 32 rows from notices published between 21 and 25 November (one of them Tower Records Japan, moved from pending), and 37 rows from notices published on or before 20 November that the additions through the seventh edition had missed; follow-up additions and corrections reflected in 23 rows)

---

## What this runbook protects

The book declares five operating rules in its text. **Every step in this runbook exists to implement these five.**

1. **Admit only rows whose primary notice the author has opened and read.** Never create a row from press reports, secondary sources, or the output of another AI.
   (Corrected 10 November 2026)
   From the fifth edition, rule 1 is amended to: "Admit only rows confirmed against the primary notice. Never create a row from press reports or secondary sources alone. AI agents retrieve and check the primary notices and record verbatim the sentences of the notice used as the basis for the decision. The author spot-checks, and decides rows on the boundary of the admission criteria."
2. **Keep units and wording exactly as in the notice.** Do not convert records into people. Do not rewrite "possible" as "confirmed". If the notice does not state the route, write "unauthorised access (vector not disclosed)".
3. **Append-only.** Never delete or rewrite a row. A correction is appended with a statement that it is a correction and its date.
4. **Canonical file and derived files are updated together.** Edit `data/registry.json`, generate `registry.csv` and the tables in the text with `scripts/build_registry.py`, and put them in the same commit.
   (Added 15 November 2026)
   From v6.1, the English `registry_en.csv` and `registry_en.json` are added to the generated files.
5. **Sign every commit; never put the private key in the repository.** Same as the runbook of `the-ai-forecast-registry` (Appendices A and B).

If you are unsure at any point in the procedure, go back to which of these five the operation is meant to protect.

---

## 0. Pre-work checks (every time)

```powershell
cd <clone location of the repository>
git remote -v
git fetch origin
git log --oneline HEAD..origin/main
git status
git config --get pull.rebase
Get-ChildItem -Recurse -File -Include *.asc,*.rev,*.gpg,*.key,*.pgp
```

- `git remote -v` shows `the-japan-breach-registry-2026.git`
- The output of `git log --oneline HEAD..origin/main` is empty (if not, run `git pull --no-rebase --no-edit`)
- `git status` reports `nothing to commit, working tree clean`
- `pull.rebase` is `false`
- The last command prints nothing

---

## 1. Adding a row (from the pending list to the registry, or a new case)

### 1-1. Reach the primary notice

The author opens and reads, personally, a notice on the affected organisation's own domain (HTML or PDF), or a timely disclosure (the same text distributed through TDnet). Press articles, aggregator sites and summaries by other AIs are not grounds for having reached the notice.

(Corrected 10 November 2026)
From the fifth edition, reaching the primary notice and checking its text are done by AI agents. In the check, the scale and unit, the status wording, the route, any mention of AI, the publication date and the admission criteria are compared against the notice, and the sentences of the notice used as the basis for the decision are recorded verbatim (for an example of the record, see the list of fifth-edition check results). Rows that could not be opened are marked "could not be retrieved" and are never filled in by guesswork. Part of the checker's decisions is re-verified by another AI or by the author, who opens the notice again. Press articles and aggregator sites remain, as before, not grounds for having reached the notice.

If the notice cannot be reached, do not create a row. In `pending` of `registry.json`, write the organisation name, publication date, press-based scale, the reason it is not admitted, and the reference URL (if it is already in `pending`, leave it as it is).

### 1-2. Gather what to record

From the notice, extract the following in the notice's own wording.

| Field | Rule |
|---|---|
| `published` | The date of the notice. If there are follow-ups, `published` is the date of the first notice, and the dates of follow-ups go in `scale_ja` or `notes_ja` |
| `scale_ja` | The number and unit of the notice verbatim (in quotation marks). "Up to", "approx.", "records", "persons" and "accounts" exactly as written. Breakdown, if any, in brackets |
| `status_ja` | The notice's own words, such as "confirmed", "possible", "risk", "up to", "cannot be ruled out" |
| `vector` | One of `脆弱性` (vulnerability) / `VPNの脆弱性` (VPN vulnerability) / `委託先` (contractor) / `設定不備` (misconfiguration) / `不正ログイン` (unauthorised login) / `複合` (multiple vectors) / `不正アクセス（経路未公表）` (unauthorised access, vector not disclosed). If the notice does not describe the route, the last one |
| `dates_ja` | Whichever of the intrusion, detection, discovery and cut-off dates the notice gives. If none, "not stated" (記載なし) |
| `ai_mention` | If the body of the notice has words about AI on the attacker's side, verbatim; otherwise `なし` (none). "AI" in company or product names is not counted |
| `primary_url` | The URL of the notice that was opened |
| `retrieved` | The date it was opened |
| `notes_ja` | The verbatim route, URLs of follow-ups, relation to other rows and so on |

(Added 15 November 2026)
From v6.1, so that the English `registry_en.csv` can be generated, each row also carries English columns: `org_en`, `scale_en`, `status_en`, `data_en`, `dates_en`, `ai_mention_en` and `notes_en`. They are English translations of the Japanese columns; quotations are translated into English and enclosed in double quotation marks (the verbatim Japanese wording stays in the Japanese columns). If `ai_mention` is `なし`, `ai_mention_en` is `none`. Pending entries (`pending`) also carry English fields: `org_en`, `published_en`, `reported_scale_en`, `reason_en` and `reference_en`. When an addition or correction is written in a Japanese column, write it in the English column too, with the same date, prefixed by `(Added D Month YYYY)` or `(Corrected D Month YYYY)`. If an English column is missing, `build_registry.py` stops.

### 1-3. Edit the file and generate

```powershell
# Append the row at the end of rows in data/registry.json (IDs are sequential). If it was in pending, delete it from there
python scripts/build_registry.py
```

Replace the table under "## 第1版の31行" ("The 31 rows of the first edition"; update the row count in the heading when the edition changes) in the main text `docs/jp/the-japan-breach-registry-2026_JP.md` with the content of the generated `docs/jp/_table_ch4.md`. Do the same for the English edition with `docs/en/_table_ch4.md`.

Update the following to the new row count: "## 数えると" ("Counting") and "## 照合待ち（台帳の外）" ("Pending (outside the registry)") in the text, the table of "rows above one million" in Chapter 1, the tally of routes in Chapter 2, the Rows badge and the update history in the README, and the row count in `llms.txt`. **Where first-edition figures are touched, prefix (added D Month YYYY) and append, leaving the first-edition wording in place.**

### 1-4. Commit and push

```powershell
git add data/registry.json data/registry.csv data/registry_en.csv data/registry_en.json docs/jp/_table_ch4.md docs/en/_table_ch4.md docs/jp/the-japan-breach-registry-2026_JP.md docs/en/the-japan-breach-registry-2026_EN.md README.md README_en.md llms.txt
git status
git diff --cached --stat
git commit -m "Register row 032: <organisation name> (<publication date>)"
git show --stat HEAD
git fetch origin
git log --oneline HEAD..origin/main
git push
git verify-commit HEAD
```

- Do not use `git add -A` (it sweeps in untracked files)
- `git show --stat HEAD` must not include key files or unintended files
- `git verify-commit HEAD` must return `Good signature from "Satoshi Yamauchi <s3atoshi@gmail.com>"`

---

## 2. Correcting an existing row (a follow-up changed a number, or an error was pointed out)

Rows are not rewritten. Do the following two things.

1. At the end of `notes_ja` of the row in `registry.json`, append `（YYYY年M月D日訂正）` (the Japanese correction marker), followed by what changed and how, the primary URL that supports it, and the name of the person who pointed it out (if they wish). Leave the original values of `scale_ja` and the other columns, and write the new value in `notes_ja`
2. Where the text refers to the original value, place `（YYYY年M月D日訂正）` immediately before it, then a line break, then the correction

The commit subject is `Correct row 017: <content>`.

A follow-up that changes the status from "possible" to "confirmed" is handled in the same way. The original "possible" is kept.

---

## 3. Updating the tiers of evidence (Chapter 3)

When a security company or authority reports, in a primary source, the use of AI by attackers in a case in Japan, append it to the relevant tier of Chapter 3.

- Prefix the addition with `（YYYY年M月D日追記）` (the Japanese addition marker)
- Quote verbatim in the original language, with the speaker, publication date and URL
- The tier judgement (with evidence / traces / possibility) follows the definitions in the text. "With evidence" applies only when there is material in the attacker's hands, a forensic result, or the result of an official investigation
- Review the judgements on H1 and H4 in Chapter 5 together, and if they change, append in the same way

The commit subject is `Update tier: <case>`.

---

## 4. Raising the edition

Raise the edition when the pending list moves into the registry and the row count changes substantially, or when a chapter's judgement changes. Update `version` and `snapshot_date` in `registry.json`, the update history in the README, and the head of `llms.txt`, and create the edition in GitHub Releases.

**What was done in the second edition (2026-10-16)**: the table of the 31 first-edition rows (`## 第1版の31行`) was not rewritten; immediately after it, a table of added rows was placed as "### 2026年10月16日に追加した5行" ("The 5 rows added on 16 October 2026"). The added rows are taken from row 033 onward of `docs/jp/_table_ch4.md`. In later editions too, existing tables are not corrected, and added rows are placed in a separate dated table.

---

## 5. When something fails

Apply Section 5 and Appendices A to C of `docs/UPDATE_RUNBOOK.md` in `the-ai-forecast-registry` as they stand (an error in a commit message, an error in content, a signing failure, a private key mixed in, a rejected push). One failure is specific to this book.

**The tables in the text were corrected without running the generation script.** The tables in the text and `registry.json` no longer agree. Run `python scripts/build_registry.py`, replace the text with the generated tables, and then commit. Never edit the tables in the text directly.

---

## Appendix: record of the first-edition check

The author opened and checked each notice for the 31 first-edition rows on 10 October 2026. The output of Deep Research (Claude, ChatGPT, Perplexity, Gemini) was used to discover candidates and not as grounds for admission. Of the four, the Gemini version contained assertions that contradicted the other three (a "clear denial" of an explanatory candidate, and figures based on a secondary blog), so it was not used even for discovering candidates.

The primary notices the author could not reach at the time of the first edition are the 16 items in `pending` of `registry.json`.

(Added 16 October 2026)
On 16 October 2026, five rows, 032–036, were moved from the pending list into the registry. The notices the author opened and read that day were: 032 the timely disclosure of Bookoff Group Holdings (9 October 2026), 033 the notice of Daiwa Securities (5 October 2026), 034 the second report of Sagawa Express (1 October 2026), 035 the first report of Uzabase (8 October 2026), and 036 the notice of White Essence (5 October 2026). The same day, follow-ups to seven existing rows (001, 008, 018, 019, 023, 027, 028) were checked against each notice and added or corrected, with dates, in the notes column. 11 items remain pending.

(Added 26 October 2026)
On 26 October 2026, 35 rows, 037–071, were added. Candidate discovery and drafting (extracting from the text of the notices) used web searches by AI agents and retrieval of each notice. The grounds for admission were that the author opened the `primary_url` of each row personally and checked the wording of the notice. Rows for which this check was not finished are returned to the pending list before the commit. Notices that could not be reached, PDFs and pages that require JavaScript (Bookoff's second report, Sagawa Express's fifth report, Uzabase's second report, Commune's follow-up, Rakus Light Cloud's continuously updated page, GMO Cybersecurity's blog), are stated as unread, and press-based values were marked "press-based" in the notes column and in the pending list to distinguish them. The same day, follow-ups were added or corrected in the notes column of 14 existing rows (002, 005, 007, 012, 017, 020, 023, 025, 028, 030, 031, 032, 034, 035) (007, 025 and 028 are corrections). 25 items are pending. In the third edition, the table of the 36 second-edition rows was not rewritten, and a separate table "### 2026年10月26日に追加した35行" ("The 35 rows added on 26 October 2026") was placed.

(Added 3 November 2026)
On 3 November 2026, 229 rows, 072–300, were added. As in the third edition, candidate discovery and drafting used web searches by AI agents and retrieval of each notice, and the results of several agents divided by period were merged (removal of duplicates, numbering in order of publication date). As in the third edition, the grounds for admission were that the author opened the `primary_url` of each row personally and checked the wording of the notice. Rows for which this check was not finished are returned to the pending list before the commit. In addition, at the author's instruction, AI agents retrieved the `primary_url` of each row again on 3 November 2026 and checked the scale and unit, the status wording, the route, any mention of AI and the publication date against the notice (results in Chapter 4 of the text). Rows marked "verbatim unconfirmed" in the notes column include places where it could not be confirmed that the extraction matched the original. The TDnet originals (release.tdnet.info) could not be retrieved, so timely disclosures were read from the originals on the Japan Exchange Group site (www2.jpx.co.jp) or from the identical text distributed by Yahoo! Finance and minkabu. The same day, follow-ups were added or corrected in the notes column of 19 existing rows (012, 023, 025, 026, 028, 047, 050, 051, 053, 054, 055, 059, 061, 062, 063, 064, 068, 070, 071) (023, 028, 047, 053, 070 and 071 are corrections). 67 items are pending. In the fourth edition, the tables up to the third edition were not rewritten, and a separate table "### 2026年11月3日に追加した229行" ("The 229 rows added on 3 November 2026") was placed.

(Added 3 November 2026)
The same day, after adding the rows, the book's proposition and arguments were reviewed against the fourth-edition data and new primary sources (Trend Micro, 16 October 2026; Tokyo Shoko Research, 23 October 2026). Statements that no longer held (the October count in Chapter 1, the way routes are counted in Chapter 2, the "direction of denial" of H7 in Chapter 5, and point 3 of "what can be said" and "as an observation point" in Chapter 7) were corrected by leaving the original sentence and prefixing (Corrected 3 November 2026); statements whose judgement did not change (the introduction, H1, H3 and H4 in Chapter 5, and the conclusion) were supplemented with (Added 3 November 2026). The book's question and the four items of "what this book does not write" were not changed.

(Added 8 November 2026)
On 8 November 2026, 207 rows, 301–507, were added. As in the fourth edition, candidate discovery and drafting used web searches by AI agents and retrieval of each notice, and the results of two agents split by publication date (3–5 November and 6–8 November) and one agent re-checking the 67 pending items were merged (removal of duplicates against existing rows and the pending list, numbering in order of publication date). The only retrieval method was WebFetch, and for some rows the full text of PDFs could not be read directly. As in the third and fourth editions, the grounds for admission were that the author opened the `primary_url` of each row personally and checked the wording of the notice. **Rows for which this check was not finished are returned to the pending list before the commit.** Rows marked "unconfirmed" or "author's judgement" in the notes column (rows whose publication date was inferred from a URL or a secondary source, rows whose number of records is given only in an image, rows whose notice is on the affected organisation's blog or a PR TIMES distribution, and rows whose notice does not contain the words "unauthorised access" and is written with terms such as "ransomware attack") are decided by the author as to admission. The same day, follow-ups were added or corrected in the notes column of 9 existing rows (241, 004, 215, 275, 290, 223, 195, 032, 297) (241, 004 and 215 are corrections). In re-checking the pending list, 6 of the 67 items (Shuppin, Tricycle, Generic Pharmaceutical, So-net, Saitama Prefectural Kawagoe High School, Shizuoka City Ma-a-ru) turned out to have been admitted as rows already in the fourth edition and were removed from the list. Two items outside the period and 14 items that did not meet the admission criteria were also removed, and 55 new items were added. 91 items are pending. In the fifth edition, the tables up to the fourth edition were not rewritten, and a separate table "### 2026年11月8日に追加した207行" ("The 207 rows added on 8 November 2026") was placed. Judgements from Chapter 5 onward were not reviewed. Of the 207 added rows, 30 were re-checked by a separate AI agent that had not seen the drafts, which retrieved the primary notices again and compared them; the values of 4 rows were corrected (318, 345, 365, 476). The remaining 177 rows were not re-checked.

(Added 10 November 2026)
On 10 November 2026, before publication of the fifth edition, 77 rows, 508–584, were added. The 207 rows added on 8 November were not changed. As on 8 November, candidate discovery and drafting used web searches by AI agents and retrieval of each notice, and the results of five agents split by publication date (first half of 6 November, second half of 6 November, 7–9 November, 9 November, and a sweep of 8–9 November plus follow-ups to chain starting points) were merged (removal of duplicates against existing rows and the pending list, numbering in order of publication date). Candidate discovery used the daily list of an aggregator site (jouhourouei.clipmaster.jp) and press reports. The only retrieval method was WebFetch, and for some rows the full text of PDFs could not be read directly. Rows marked "unconfirmed" or "verbatim unconfirmed" in the notes column, rows whose notice is outside the affected organisation's domain (519, 527, 538, 582), a row whose number of records is shown only in an image (565), and rows on the boundary of admission criterion 2 (513, 528, 550) are decided by the author as to admission. For 6 November, only 13 rows had been picked up as of 8 November, so 47 rows were added. Differences from the aggregator site's counts remain for 3–5 November, but they were not investigated this time. The same day, follow-ups were added to the notes column of 2 existing rows (275, 055). Five items from the pending list (JERA Sunday, Okazaki City, Hatoya, Aioi Nissay Dowa Insurance, Mitsui Sumitomo Insurance) were moved into the registry, and four items (Sony Life Insurance, the Metropolitan Police Department, Osaka City, SBC Shinetsu Broadcasting) were retried but could not be reached. 24 new items were added, and 110 items are pending. Three items were not admitted because they did not meet the admission criteria (Japan Society for the Promotion of Science, Meijiza, Fukui Prefecture "291JOBS"). Of the 77 added rows, 30 (16 large ones and 14 chosen at random) were re-checked by a separate AI agent that had not seen the drafts, which retrieved the primary notices again and compared them; the values of 2 rows were corrected (554, 561). Only a note was added to the notes column of 4 rows (509, 546, 571, 577). The remaining 47 rows were checked against the primary notices in a later check. In Chapter 4, the table of the 207 rows added on 8 November was not rewritten, and a separate table "### 2026年11月10日に追加した77行" ("The 77 rows added on 10 November 2026") was placed. Judgements from Chapter 5 onward were not reviewed.

(Added 10 November 2026)
The same day, at the author's instruction, the procedure for checking the 284 rows added in the fifth edition (301–584) was changed from what it had been. The rows for which the author personally opened and read the primary notice are the 9 rows 301–309 (none differed from the registry values). For the 275 rows 310–584, AI agents retrieved the `primary_url` of each row again and compared the scale and unit, the status wording, the route, any mention of AI, the publication date and the admission criteria against the notice. The sentences of the notice used as the basis for each decision were recorded verbatim. The results for 245 rows were: 180 rows matched, 6 rows had values corrected (323, 352, 376, 398, 479, 566), 53 rows received a note only, 2 rows (320, 508) were rows where the page at the primary URL was not a report giving the number of records, and 3 rows (404, 466, 565) could not be retrieved again. For the remaining 30 rows, the re-check described above corrected the values of 2 rows (554, 561) and added notes to 4 rows. For 9 of the checker's decisions, the AI that did the editing opened the notice again and verified them, and did not adopt only the proposed correction for 398. The author decides the admission of rows on the boundary of the admission criteria (322, 369, 441, 513, 528, 550). The same day, at the author's judgement, rule 1, Section 1-1, the admission criteria in the text and the README, and `scope` and `rules` in `registry.json` were corrected to match this procedure (`primary_notice_opened_by_author` in `rules` was replaced with `primary_notice_verified` and `verification`).

(Added 14 November 2026)
On 14 November 2026, 260 rows, 585–844, were added (sixth edition). The 584 rows of the fifth edition were not changed. As in the fifth edition, AI agents were used for candidate discovery and drafting, and for retrieving and checking the primary notices. The results of seven agents divided by publication date and role were merged (A: new notices of 10–11 November; B: new notices of 12–14 November; C: omissions of 3–9 November; D: retry of the 110 pending items; E: follow-ups to existing rows; F and G: organisations whose first report is not in the registry, found by A and B in the aggregator site's list of follow-ups). In the merge, duplicates were removed by primary URL and organisation name (Nasushiobara City in A and B, Kanagawa Prefecture and Fukushima Prefecture in C and F, ENSAPIA Tokyo "Hangame" and the Ministry of Health, Labour and Welfare JANIS in C and G), and numbering followed publication date. Each agent made rows only of those for which it had opened the affected organisation's primary notice with WebFetch and confirmed the admission criteria in the body, and recorded verbatim in the notes column the sentences used as the basis for the decision. WebFetch does not always return the full text verbatim, and places where verbatim wording could not be confirmed were marked "verbatim unconfirmed". Candidate discovery used the monthly lists and individual case pages of the aggregator site (jouhourouei.clipmaster.jp) and WebSearch. The aggregator site has no page with a daily list, and retrieval from the shell was refused by the proxy, so omissions may remain in reading the lists. Notices of 14 November had not been picked up at the time of the work (the morning of 14 November).

Of the 260 added rows, 30 (16 large ones and 14 chosen at random) were re-checked by a separate AI agent that had not seen the drafts and retrieved the primary notices again. The results: 21 rows matched, 1 row had its value corrected (724 Kirin: "approx." was removed from the scale column), 8 rows received a note only (586, 589, 592, 629, 668, 725, 746, 789), and 0 rows could not be retrieved. Of the notes, those for 586, 589, 592, 606 and 629 were written in the notes column as (re-check of 14 November 2026); 668 (misuse of an API authentication key, which could be classified as unauthorised login), 725 and 746 (descriptions of precautionary measures, with the route left undisclosed) and 789 (another case in the same notice) were not reclassified. The remaining 230 rows were not re-checked. **The author's spot-check is to be done before the commit.** Rows on the boundary of the admission criteria (five rows whose follow-up said "no leakage was confirmed", the publication date of Osaka Metropolitan University, rows whose publication date is not in the body, notices outside the affected organisation's domain, rows whose number of records is the value for a whole chain, rows whose subject overlaps an existing row, and Keio Corporation and Iore, which were excluded) are listed in (Added 14 November 2026) in Chapter 4 of the text, and the author decides their admission. For 445 Tokio Marine Direct, the version of the page differs from the 10 November re-check, so the author will open the notice and confirm.

The same day, follow-ups were added or corrected in the notes column of 20 existing rows (053, 059, 119, 236, 339, 346, 361, 371, 418, 425, 436, 445, 528, 549, 556, 558, 560, 569, 575, 583) (053, 119, 361, 445 and 549 are corrections). The 110 pending items were retried: 23 were moved into the registry (Nasushiobara City was moved separately in the survey of 10–13 November), Meiji Gakuin University (outside the criteria) and Hasegawa (the same case as existing row 372) were removed, and 35 were added. 120 items are pending. In Chapter 4, the table of the 77 rows added on 10 November was not rewritten, and a separate table "### 2026年11月14日に追加した260行" ("The 260 rows added on 14 November 2026") was placed. Judgements from Chapter 5 onward were not reviewed.

(Added 21 November 2026)
On 21 November 2026, 389 rows (845–1233) were added (seventh edition; v7.0, 1,233 rows, 126 pending). The 844 sixth-edition rows are unchanged. Eleven AI agents split by publication date and role were merged: fields, vector classes and date range were checked mechanically, duplicates removed by primary URL, joint notices made one row, and IDs assigned by publication date. The two Tokyo rows were retrieved at integration because the Tokyo site was under scheduled maintenance during checking. In the retry of pending cases, notices unreadable by WebFetch were opened in a browser, and PDFs and images were read on screen (a departure from section 1-1; stated in the notes of those rows). Thirty of the 257 rows (the 16 largest and 14 at random) were re-checked against the primary notices by a separate AI agent that had not seen the drafts: 21 matched, none needed a value changed, 4 received notes only (937, 991, 1017, 1054), 4 raise an admission question though their values match the notices (902, 971, 1049, 1052), and 1 could not be retrieved again (854). Notes marked (Re-check of 21 November 2026) were added to 971, 991, 1054, 937 and 854. The other 227 rows were not re-checked. **The author's spot check precedes the commit.** Boundary rows and the 98 reached cases not admitted (45 of them university co-ops) are listed in Chapter 4 under (Added 21 November 2026).

The same day, follow-ups were added to the notes of 17 existing rows (022, 028, 037, 049, 051, 053, 059, 063, 072, 121, 241, 246, 280, 320, 484, 589, 754; corrections in 022, 028, 037, 049, 072, 589, 754). The 120 pending cases were retried: 55 moved into the ledger, 7 removed, 52 added; 110 remain. In Chapter 4 the table of 260 rows added on 14 November is unchanged and the new rows are in a separate table. Facts as of 21 November 2026 were also added to Chapters 2, 5 and 7 and the Epilogue (the first additions to Chapters 5 and 7 and the Epilogue since the fourth edition).

(Added 21 November 2026)
Because candidates were chosen from the aggregator's list, cases the aggregator misses were absent from the ledger. The same day, 19–20 November and 14–18 November were therefore searched again from the routes of the organisations' own notices, without the aggregator or press reports. The four routes were the service names at chain origins, timely disclosures, public bodies, municipalities, universities and hospitals, and the own sites and press releases of unlisted companies and organisations; eight AI agents were split by route and period. 132 rows were added (1102–1233). The aggregator is compared only after the search is finished.

Procedure for next time. (1) Do not use the aggregator (jouhourouei.clipmaster.jp) to find candidates. It lags publication by 2–3 days; use it only to cross-check after searching, and record any case not found by the primary routes as a gap in the search method. (2) For timely disclosures, the TDnet daily list cannot be opened (robots); search the IR BANK disclosure list (irbank.net/td) and per-company lists (irbank.net/E + code/tdnet), and read the text in the identical PDF on assets.minkabu.jp. Tracing back from a final or second report to the first notice found omissions in the ledger. (3) PR TIMES has a keyword search API in date order (prtimes.jp/api/keyword_search.php/search?keyword=…&page=N). Unlisted companies rarely use PR TIMES; they publish on their own sites or on Rakuten Ichiba, Yahoo! Shopping and Shopify store pages. (4) For municipalities and universities, putting the chain name (Lukumy, ANPIC, teket, Arara and so on) in the query reaches the primary notice more reliably than searching by date. (5) In standard mode WebSearch is dominated by press and aggregator sites; exact-match terms with a date (for example "2026年11月19日" 不正アクセス) and extended mode with press and aggregator domains excluded worked. (6) WebSearch has a limit for the whole conversation (200 searches). Splitting among agents that share it makes them stop partway, so narrow the routes and ration searches by priority. (7) For pages with no posting date, the publication date is the update date; say so in the notes.


Of the 78 rows added in the first re-search pass, 30 were independently re-checked by three other AI agents against the primary notices: 18 matched, 10 carry notes only, 0 needed a value correction, 1 raised a doubt about admission (1121 iORE: the words for unauthorised access were not confirmed in the text; admitted at the author's decision), and 1 could not be fetched again (1113). The notes concern rows whose wording could not be confirmed verbatim (1159, 1167), a row whose posting date and notice date differ (1139), and rows whose vector could be read differently (1126, 1140: a contractor case whose notice says a vulnerability was exploited). The fetched text was often a summary, not the full wording. The other 48 rows of the first pass and the 54 rows of the second pass were not re-checked.

(Added 26 November 2026)  
On 26 November 2026, 82 rows (1234–1315) were added (eighth edition; v8.0, 1,315 rows, 129 pending). The 1,233 seventh-edition rows are unchanged. The results of nine AI agents split by route and role (two searching from chain origins, timely disclosures, government bodies, local governments, universities and hospitals, two for companies' and organisations' own sites and PR TIMES, two retrying the 126 pending cases, and one for follow-ups to existing rows) were merged, and candidates the agents had named without reading were checked by two more agents; duplicates were removed by primary URL (rows 1234–1306). Of rows 1234–1306, 30 (the 16 largest and 14 at random) were independently re-checked by three other AI agents that had not seen the drafts; no value was changed and the notes of one row (1263) were corrected. After the search was finished, the aggregator's list for 21–25 November was cross-checked; 13 domestic cases missed by the primary routes were checked against their primary notices by another agent, and 8 were admitted (1307–1314, not re-checked). Tower Records Japan, which had been pending, was checked in the author's browser (Claude in Chrome) and moved into the ledger as 1315. About 140 web searches were used in all.

Additions to the search method. (8) IR BANK timely disclosures: a date-shaped URL (irbank.net/td/2026-11-24) is treated as a keyword search and returns nothing. Daily lists open as time pages (irbank.net/td?y=<UNIX seconds of the JST time>, 30 per page, &p= when many share a time). Keyword pages (/td/不正アクセス, /td/情報漏, /td/サイバー) help check for misses. (9) WebSearch hardly indexes municipal and university pages within a few days of publication; opening the list of affected parties in a chain origin's notice, and each organisation's news list, reaches the primary notice more reliably. (10) Organisations that publish only on their own domain appear neither on PR TIMES nor in timely disclosures and can be missed by every route; in the eighth edition, 1242 Bic Camera, Kojima and Sofmap (2 November, 15,204,757 records in total) had been missed through the seventh edition. Many of the 13 cases found in the aggregator cross-check are of the same kind; Miki City's notice could be reached only from the city's list of new items, and Research Panel's only from its login page. (11) GoQSystem puts the affected stores at 1,694 companies, while 36 ledger rows contain its name; covering store pages on Rakuten Ichiba and elsewhere needs a dedicated agent. (12) Pages that render their text with JavaScript (sites built with Studio, teket and others) and sites that refuse robots (tower.jp and others) cannot be read with WebFetch; only the author's browser can read them. In the eighth edition, tower.jp was opened in the author's browser to check row 1315.
