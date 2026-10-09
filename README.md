# The Japan Breach Registry 2026

**2026年秋、日本の企業・組織を襲った個人情報漏えいの波 ── 事実台帳から分かる客観的分析結果**

"Fourteen years produced three breaches of ten million records. The autumn of 2026 produced three in a month." <br>
（14年間で3回しか起きなかった1,000万件規模の漏えいが、2026年の秋には1か月に3回起きた）

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Language](https://img.shields.io/badge/Language-Japanese%20%7C%20English-blue)](docs/)
[![Rows](https://img.shields.io/badge/Rows-31-informational)](data/registry.csv)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--10--10-brightgreen)](https://github.com/Leading-AI-IO/the-japan-breach-registry-2026)

*Read this in other languages: [English](README_en.md)*

---

> **定義｜What is The Japan Breach Registry 2026**
>
> **本書とは**、山内怜史（Satoshi Yamauchi）による、2026年9月1日以降に日本の企業・組織が
> 公表した個人情報漏えいを、**当事組織の一次公表文を著者が自ら開いて読んだ事案だけ**、
> 公表文の単位と表現のまま並べた追記専用の台帳である。件数を人数に換算せず、
> 「可能性」を「確認」に書き換えず、経路が書かれていなければ「未公表」と書く。
> 台帳に加え、本書は「攻撃者がAIを使った」という言明を**証拠つき・痕跡・可能性・言及なし**
> の4段階に分けて誰がいつ何と言ったかを原語で記録し、「なぜ2026年秋の日本に集中したか」
> についての**8つの説明候補を同じ基準で検査**する。第1版（31行）の時点で、日本の事案に
> 「証拠つき」は1件もなく、8候補のうち日本について支持されたものも1つもない。
> 本書は、AIが原因であるとも、Claude Mythosが使われたとも、Glasswingが公開した脆弱性が
> 悪用されたとも、日韓の攻撃者が同じであるとも書かない。一次資料にないからである。
> 中心の問い：**AIが脆弱性を見つける費用を崩した世界で、守る側の先行は成り立つのか。**
> 本書はこの問いに答えず、答えを出すための台帳を更新し続ける。
>
> **This registry** records personal-data breaches disclosed by Japanese companies and
> organisations on or after 1 September 2026 — only those whose primary notice the author
> opened and read — keeping each notice's own unit and wording. It never converts records
> into persons, never upgrades "possible" to "confirmed," and writes "not disclosed" where
> the notice is silent on the vector. Alongside the ledger, it sorts every claim that
> "attackers used AI" into four tiers — **evidence, trace, possibility, no mention** — with
> the speaker, date and original-language wording, and tests **eight candidate explanations**
> for why the autumn of 2026 concentrated in Japan on identical criteria. As of the first
> edition (31 rows), no Japanese case reaches the "evidence" tier and none of the eight
> explanations is supported for Japan. The book does not claim that AI caused the wave, that
> Claude Mythos was used, that Glasswing-disclosed vulnerabilities were exploited, or that
> the Japanese and Korean attackers are the same — because no primary source says so.
> Central question: **in a world where AI has collapsed the cost of finding vulnerabilities,
> does the defender's head start hold?** The book does not answer; it keeps the ledger that
> would.
>
> **管理と責任 / Governance**：台帳に書くのは著者一人である。収載基準は「当事組織の一次公表文を
> 著者が開いて読めたこと」の1つであり、満たすものは例外なく載せ、満たさないものは規模が
> 大きくても載せない。載せるかどうかに著者の裁量はない。読者ができるのは、台帳を検証すること、
> 誤りを指摘すること、一次資料の所在を知らせることである。The author is the sole writer.
> Admission has one criterion — the author opened and read the primary notice — applied
> without discretion. Readers verify, report errors, and point to primary sources.
>
> *著者・全書籍一覧 / Author & full catalog: [github.com/Leading-AI-IO](https://github.com/Leading-AI-IO)*

---

## 📖 概要

2026年10月7日、2つの文書が同じ日に出た。

1つは東京商工リサーチの「上場企業『個人情報漏えい』、過去最悪ペース」。100万件以上の漏えいは2026年に10件（2025年は6件）、1,000万件以上は「2025年までの14年間で3回」だったものが2026年だけで3回。

もう1つはCrowdStrike Intelligenceの報告。韓国の金融機関を狙った攻撃者が管理するサーバーの公開ディレクトリから、「Claude Code session histories」と侵入テストツールARTEXの設定ファイルが見つかった。攻撃者がAIを使った証拠が、攻撃者自身の手元から出た。

この2つは別の国の別の出来事である。だが日本の報道は翌日から、2つを1つの文脈で語り始めた。「AIを悪用したサイバー攻撃が急増し、個人情報の大量漏えいが相次ぐ」。

**本書は、この2つの文書のあいだにある距離を測る。**

### 台帳

2026年9月1日以降に日本の企業・組織が公表した個人情報漏えいのうち、著者が当事組織の一次公表文を自分で開いて読んだ31件を、公表文の単位と表現のまま並べた。報道だけで知られている16件（ブックオフ、ムラウチドットコム、ビューカードなど、台帳に入れば規模の上位に入る事案を含む）は「照合待ち」として台帳の外に置いた。

**公表文の単位で100万を超える行は8行。経路を公表文が具体的に書いた行は14行、書いていない行は17行。攻撃側のAIに言及した公表文は0行。**

### 証拠の4段階

「攻撃者がAIを使った」という言明を4段階に分けた。

- **証拠つき**：韓国の金融機関（CrowdStrike）の1件のみ。日本には0件
- **痕跡**：報道が引用したトレンドマイクロの言葉は、同社の原文では「現状、必ずしもこれらの攻撃がAIを直接的に用いたものであるという証拠があるわけではありませんが、ログだけ見ても『これまでとは違う挙動』を捉えていることは事実です」
- **可能性**：韓国当局の発言（報道ベース）。当局自身の公表文には出てこない
- **言及なし**：日本の公表文31通すべて

### 8つの説明候補

なぜ日本に集中したのか。攻撃側のAI、公表義務、日本固有の弱点、同一攻撃者、ツールの拡散、守る側のAIの脆弱性公開、認証情報市場、偶然の8つを同じ基準で検査した。**日本について支持されたものは1つもない。** 本書はそれを「判定不能」と書く。

### 2つの年表

守る側（Project Glasswing：4/7発表 → 5/22初期報告・1万件超 → 10/6「at least 129,000 verified software vulnerabilities」）と、攻撃側（ARTEX：7/26にv0.1.0公開、星17 → 9月下旬に韓国で使用）を並べた。守る側は公開しない最上位モデルを選ばれた組織に渡し、攻撃側は公開されたツールと安価なモデルを使った。この2つの年表のあいだの距離が、本書の問いである。

---

## 📊 台帳データ

| ファイル | 位置づけ | 内容 |
| --- | --- | --- |
| [registry.json](./data/registry.json) | **正本** | 収載基準・列定義・運用規則を先頭に含む。31行＋照合待ち16件 |
| [registry.csv](./data/registry.csv) | 派生 | 表計算ソフトで開ける形式（UTF-8 BOM付き・14列） |
| [build_registry.py](./scripts/build_registry.py) | 生成スクリプト | 正本から CSV と本文の第4章の表を生成する |

**本文の表と2ファイルは、同じコミットで更新される。** 読者は本文を読まずに `data/registry.csv` だけを開いてもよい。

---

## 📄 ドキュメント

| ファイル | 言語 | 内容 |
| --- | --- | --- |
| [the-japan-breach-registry-2026_JP.md](./docs/jp/the-japan-breach-registry-2026_JP.md) | 🇯🇵 日本語 | 本文（日本語版） |
| [the-japan-breach-registry-2026_EN.md](./docs/en/the-japan-breach-registry-2026_EN.md) | 🇺🇸 English | 本文（英語版） |
| [UPDATE_RUNBOOK.md](./docs/UPDATE_RUNBOOK.md) | 🇯🇵 日本語 | 更新手順書。台帳に書くのは著者一人であり、その運用手順を公開している |

---

## 🔄 更新履歴

| 日付 | 版 | 内容 |
| --- | --- | --- |
| 2026-10-10 | v1.0 | 第1版。台帳31行、照合待ち16件 |

---

## 📑 目次

- 序章: 10月7日、2つの文書が同じ日に出た
- 第1章: 規模の異常 ── 件数ではなく、大きさが変わった
- 第2章: 経路の地図 ── 1つの穴ではなく、ばらばらの穴
- 第3章: 証拠の4段階 ── 誰が、何を、どこまで言ったか
- 第4章: 台帳
- 第5章: 8つの説明 ── 支持、否定、判定不能
- 第6章: 先行の賭け ── Glasswingの年表と、ARTEXの年表
- 第7章: 観測点としての日本 ── 言えることと、言えないこと
- 終章: 台帳は閉じない

---

## 🔗 Related Projects

本書は、以下のOSSプロジェクトと相互に接続されている。

| プロジェクト | 概要 | リンク |
| --- | --- | --- |
| **The AI Forecast Registry**        | AIをめぐる予測を決着の前に記録し、帰結を発言者自身の言葉で追う台帳。名簿シリーズ第2弾 | [GitHub](https://github.com/Leading-AI-IO/the-ai-forecast-registry)       |
| **The China AI Registry**           | 中国のAI産業を当局の登録名簿988件を母集団として読む。名簿シリーズ第1弾 | [GitHub](https://github.com/Leading-AI-IO/the-china-ai-registry)          |
| **The Anatomy of Anthropic**        | Anthropicの戦略・製品・研究・安全性を包括的に解剖 | [GitHub](https://github.com/Leading-AI-IO/anatomy-of-anthropic)           |
| **The Silence of Intelligence**     | Anthropic CEO ダリオ・アモディの思想を体系化 | [GitHub](https://github.com/Leading-AI-IO/the-silence-of-intelligence)    |
| **Frontier-Grade Open Weights**     | フロンティア級のオープンウェイトモデルは、開かれたのか | [GitHub](https://github.com/Leading-AI-IO/frontier-grade-open-weights)    |
| **US-China AI Competition**         | 米中AI競争の多層構造 | [GitHub](https://github.com/Leading-AI-IO/us-china-ai-competition)        |
| **Earned AI Model Optionality**     | AIモデルは選べる。選べるのは、選べるようにした企業だけだ | [GitHub](https://github.com/Leading-AI-IO/earned-ai-model-optionality)    |
| **The AI Strategist**               | AIストラテジストという職業を定義する | [GitHub](https://github.com/Leading-AI-IO/the-ai-strategist)              |

その他の書籍は [github.com/Leading-AI-IO](https://github.com/Leading-AI-IO) を参照。

---

## 👤 著者

**Satoshi Yamauchi** (山内 怜史)

* **AI Strategist & Business Designer at Sun Asterisk Inc.**
* **Founder / AI Strategist at [Leading.AI](https://www.leading-ai.io/)**
* 15年以上にわたりBusiness・Technology・Creativeの3領域を越境。フューチャーアーキテクトでITコンサルタントとして40案件のPL/PMを推進後、リクルートで事業戦略・新規事業開発に従事。Sun Asteriskでビジネスデザイナー兼AIストラテジストとして、新規事業×生成AIの方法論「Depth & Velocity」を体系化。
* This project is part of the research by Leading.AI.
* [📒 Read my insights on Note](https://note.com/satoshi_yamauchi)
* [🌐 Visit Leading.AI Official Website](https://www.leading-ai.io/)

---

## 🤝 Contributing

**本書は Pull Request を受け付けない。** 台帳に書くのは著者一人であり、これは本書の設計の一部である。単位を換算しない、状態を書き換えない、経路を埋めないという制約は、書き手が増えるほど揺れる。揺れた台帳は、検証に使えない。

Issues は歓迎する。受け付けるのは次の二種である。

**① 誤りの指摘。** 規模の数字や単位が公表文と一致しない。日付が違う。URLが到達しない。経路の分類が公表文の記述と合っていない。著者は一次公表文に照らして確認し、誤りであれば訂正を追記する。**元の行は消さない。** 指摘した方の名は、補足欄に記す。

**② 一次資料の所在。** 本書が「照合待ち」としている16件について、当事組織の一次公表文のURLをご存知の方からの情報提供を歓迎する。著者が到達し、確認のうえで行を起こす。**収載基準を満たすものは例外なく載せる。**

「AIが原因だ」「AIは関係ない」という判定を含むIssueは、その部分を除いて受け付ける。本書は、一次資料にある記述だけを記録する。

とくに、第1版で一次到達できていない以下について、情報提供を歓迎する。

- ブックオフグループHD（2026-10-09）の適時開示PDFの本文
- 佐川急便（2026-09-30／10-01）、ユーザベース（2026-10-08）、大和証券（2026-10-05）、ビューカード（2026-10-09）、JR九州（2026-10-09）の一次公表文
- ムラウチドットコム、さくらインターネット、Fines、ホワイトエッセンスの一次公表文
- トレンドマイクロの国内不正アクセス件数集計（年別・月別）の一次ページ
- 韓国金融委員会・金融監督院・大統領府による攻撃側AIへの言及の一次原文
- ARTEX開発元（Autumn-27）のクローズドソース化声明の一次所在

---

## 📝 License

本書は [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) の下で公開されている。出典を明記すれば、自由に引用・転載・改変できる。

Copyright (c) 2026 Leading.AI
