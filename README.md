# The Japan Breach Registry 2026

**2026年秋、日本の企業・組織を襲った個人情報漏えいの波 ── 事実台帳から分かる客観的分析結果**

"Fourteen years produced three breaches of ten million records. The autumn of 2026 produced three in a month." <br>
（14年間で3回しか起きなかった1,000万件規模の漏えいが、2026年の秋には1か月に3回起きた）

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Language](https://img.shields.io/badge/Language-Japanese%20%7C%20English-blue)](docs/)
[![Rows](https://img.shields.io/badge/Rows-300-informational)](data/registry.csv)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--10--26-brightgreen)](https://github.com/Leading-AI-IO/the-japan-breach-registry-2026)

<p align="left">
  <img src="./assets/ogp_design.png" width="80%">
</p>

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

（2026年10月16日追記）  
照合待ちのうち5件（ブックオフ、大和証券、佐川急便、ユーザベース、ホワイトエッセンス）を、著者が一次公表文を読んで台帳に収載した。台帳は36行、照合待ちは11件である。**100万を超える行は10行。経路を具体的に書いた行は16行、書いていない行は20行。攻撃側のAIに言及した公表文は0行のまま。** あわせて、既存7行の続報（GMOリサーチ＆AIの件数確定、IDCフロンティアの「外部へのデータの流出はなかったと判断」など）を、行の値を変えずに補足欄へ日付つきで追記・訂正した。

（2026年10月26日追記）  
照合待ちから6件（集英社、日本原子力研究開発機構、スタディサプリ、日本経済新聞社、ビューカード、JR九州）と、10月16日以降に公表された29件（ソースネクスト 22,519,960件、カプコン 11,774,247件、ユミルリンク 延べ約900万件、トラストバンク 4,454,097件、リンツ 3,147,469件、アンドエスティ 約250万件、日本経済新聞社 約183万件、デジタル庁、国土交通省、大阪大学、東京都など）を収載した。台帳は71行、照合待ちは25件である。**100万を超える行は21行、1,000万を超える行は5行。経路を具体的に書いた行は36行、書いていない行は35行。攻撃側のAIに言及した公表文は0行のまま。** 委託先を起点とする連鎖は2系統から7系統に増え、新しい5系統はすべてメール配信またはWeb構築のSaaS（Studio、ユミルリンク、ブラストメール、NEC、フューチャーショップ）である。既存14行の続報（タイムズモビリティの確定値と経路の初公表、ローソンの対象項目の訂正、skyticketのカード情報の訂正、佐川急便の第5報〈未読・報道ベースで最大約5323万件〉など）を補足欄に追記・訂正した。

（2026年11月3日追記）  
照合待ちから14件と、10月9日〜11月2日に公表された215件を収載した。台帳は300行、照合待ちは67件である。新しい行の大規模なものは、良品計画 最大約2,726万件、ノジマ 約700万件、プレステージ・インターナショナル 最大約550万件、クラブツーリズム 約432万件、花キューピット 4,238,242件、リクルート カーセンサーnet 最大3,709,551件、アイスタイル 約300万人、松屋フーズHD 2,377,127件、So-net 2,141,986件など。**100万を超える行は38行、1,000万を超える行は6行。経路を具体的に書いた行は226行、書いていない行は74行。追加した229行のうち163行（71%）が委託先経由である。** 委託先の連鎖は7系統から20系統を超え、ブラストメール（29行）、Studio（26行）、コミューン（18行）、ユミルリンク（18行）、アララ（11行）、NTTデータの社債特典サービス、Amadeus（航空7社）などが加わった。既存19行の続報（ユミルリンクの延べ51,628,280件・49システム、skyticketの銀行口座32,341件の流出、IDCフロンティアの経路の判明など）を補足欄に追記・訂正した。

（2026年11月3日訂正）  
**第1章の「件数ではなく、大きさが変わった」を、10月について訂正した。** トレンドマイクロの10月16日の記事（一次）は、10月1日〜9日だけで52件（1日約5.8件、1〜9月平均の2.6倍）と書いた。10月は件数も増えた。ただし台帳の10月の268行のうち170行は委託先経由で、増えた分の多くは侵入の数ではなく、1つの侵入を公表した組織の数である。委託先の連鎖を1件にまとめると、台帳300行は約144件の独立した侵入になり、経路が公表文で分かるのはその約3分の1である。東京商工リサーチは10月23日、上場企業の1,000万件以上の事故を「すでに8件（速報値）」とした（10月5日時点は3回）。

### 証拠の4段階

「攻撃者がAIを使った」という言明を4段階に分けた。

- **証拠つき**：韓国の金融機関（CrowdStrike）の1件のみ。日本には0件
- **痕跡**：報道が引用したトレンドマイクロの言葉は、同社の原文では「現状、必ずしもこれらの攻撃がAIを直接的に用いたものであるという証拠があるわけではありませんが、ログだけ見ても『これまでとは違う挙動』を捉えていることは事実です」
- **可能性**：韓国当局の発言（報道ベース）。当局自身の公表文には出てこない
- **言及なし**：日本の公表文31通すべて

（2026年10月16日追記）  
追加した5行を含め、言及なしは日本の公表文36通すべてである。

（2026年10月26日追記）  
**証拠つきに、日本の事案が入った。** JPCERT/CCは10月15日、攻撃元サーバーの調査で「攻撃者がAIを利用して、既知の脆弱性のスキャンやAPI経由での攻撃などを実施していたことを確認しました」と書いた。NorForgeは10月19日、露出したCairnの管理パネルから、日本の小売業者を含む標的を報告した。**痕跡**には、JPCERT/CCの10月23日の注意喚起（「CairnやCyberStrikeAI、ARTEXなどのAIを用いたペネトレーションテスト基盤を悪用した攻撃試行が確認されています」）、セキュアスカイ・テクノロジー（10月14日）、GMOサイバーセキュリティ byイエラエ（10月19日・報道ベース）が入った。**言及なし**は、日本の公表文71通すべてである。証拠は攻撃者の側に出た。被害者の側の公表文は、まだ何も言っていない。

（2026年11月3日追記）  
**被害者の側の公表文に、初めて1通、攻撃側のAIが出た。** 079 ちとせグループ（委託先コミューン）は「攻撃は、複数のIPアドレスから短時間に大量の操作を同時に行うものでした。このことから、AI等を用いて自動化された攻撃であったと推定されます。」と書いた。根拠は攻撃の形だけで、推定の主体も書かれていないため、本書は段階3（可能性）に置いた。言及なしは、台帳300行のうち299行である。

### 8つの説明候補

なぜ日本に集中したのか。攻撃側のAI、公表義務、日本固有の弱点、同一攻撃者、ツールの拡散、守る側のAIの脆弱性公開、認証情報市場、偶然の8つを同じ基準で検査した。**日本について支持されたものは1つもない。** 本書はそれを「判定不能」と書く。

（2026年10月26日追記）  
H1（攻撃側のAI）とH5（ツールの拡散）は、日本について判定が分かれた。**攻撃者の側の事実（攻撃元サーバーでのAI利用、公開ツールによる攻撃試行）は支持。台帳の行の漏えいとの結びつきは判定不能。** H3は、10月後半について委託先（SaaS）への偏りが支持された。他は変わらない。

（2026年11月3日訂正）  
**H7（認証情報市場）の「大規模事案については否定の方向」を取り下げた。** skyticket（約1,464万件）の第3報が「不正に取得された認証情報が悪用され」と書き、プレステージ・インターナショナル（最大約550万件）とユミルリンクも認証情報の悪用を書いた。いずれも侵入の過程で取得されたもので、市場との結びつきは判定不能である。H3（日本固有の弱点）の委託先への偏りは、10月後半に限らず台帳の全期間について支持に広げた。8つのうち「否定の方向」の候補はなくなり、台帳の行の漏えいの原因として支持できる候補は、まだない。

### 2つの年表

守る側（Project Glasswing：4/7発表 → 5/22初期報告・1万件超 → 10/6「at least 129,000 verified software vulnerabilities」）と、攻撃側（ARTEX：7/26にv0.1.0公開、星17 → 9月下旬に韓国で使用）を並べた。守る側は公開しない最上位モデルを選ばれた組織に渡し、攻撃側は公開されたツールと安価なモデルを使った。この2つの年表のあいだの距離が、本書の問いである。

---

## 📊 台帳データ

| ファイル | 位置づけ | 内容 |
| --- | --- | --- |
| [registry.json](./data/registry.json) | **正本** | 収載基準・列定義・運用規則を先頭に含む。31行＋照合待ち16件（2026-10-16時点で36行＋照合待ち11件） |
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
| 2026-10-16 | v1.0（追記） | 続報の追記。7行の補足欄に日付つきで追記・訂正（018・019・023・027は訂正）。第2章・第4章に追記。照合待ち16件の到達状況を更新。照合待ちから5行を収載（032 ブックオフ、033 大和証券、034 佐川急便、035 ユーザベース、036 ホワイトエッセンス）。台帳36行、照合待ち11件 |
| 2026-10-16 | v2.0 | 第2版。台帳36行、照合待ち11件。第1版の31行は変更せず、032〜036を追加。以後の追記は第2版に対して行う |
| 2026-10-26 | v3.0 | 第3版。台帳71行、照合待ち25件。第2版の36行は変更せず、037〜071を追加（照合待ちから6行、10月16日以降の公表から29行）。既存14行の補足欄に続報を追記・訂正（007・025・028は訂正）。第3章に日本の証拠つき（JPCERT/CC 10月15日）・痕跡（JPCERT/CC 10月23日ほか）を追記。第5章のH1・H3・H4・H5・H7の判定を日付つきで追記。第6章にCairn・CyberStrikeAIの年表を追記 |
| 2026-11-03 | v4.0 | 第4版。台帳300行、照合待ち67件。第3版の71行は変更せず、072〜300を追加（照合待ちから14行、10月9日〜11月2日の公表から215行）。既存19行の補足欄に続報を追記・訂正（023・028・047・053・070・071は訂正）。第1章・第2章・第4章に追記。第3章に、日本の公表文で初めて攻撃側のAIに触れた079（段階3）を追記。第1章の件数の記述（10月について）、第2章の経路の数え方、第5章H7の判定、第7章の言えること3を訂正し、序章・第5章H1・H3・H4・終章に追記 |

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

**② 一次資料の所在。** 本書が「照合待ち」としている25件（2026年10月26日時点。第2版では11件。（2026年11月3日追記）第4版では67件）について、当事組織の一次公表文のURLをご存知の方からの情報提供を歓迎する。著者が到達し、確認のうえで行を起こす。**収載基準を満たすものは例外なく載せる。**

「AIが原因だ」「AIは関係ない」という判定を含むIssueは、その部分を除いて受け付ける。本書は、一次資料にある記述だけを記録する。

とくに、2026年10月16日時点で著者が読めていない以下について、情報提供を歓迎する。

- ブックオフグループHDの第2報（2026-10-13）、佐川急便の第3報・第4報、ユーザベースの第二報の本文
- ビューカード（2026-10-09）、JR九州（2026-10-09）、ムラウチドットコム（第二報）、さくらインターネット、Fines、日本経済新聞社、集英社、リクルート、日本原子力研究開発機構の公表文の収載（著者が読んだ後に行にする）
- トレンドマイクロの国内不正アクセス件数集計（年別・月別）の一次ページ
- 韓国金融委員会・金融監督院・大統領府による攻撃側AIへの言及の一次原文
- ARTEX開発元（Autumn-27）のクローズドソース化声明の一次所在

（2026年10月26日追記）  
2026年10月26日時点で著者が読めていない以下についても、情報提供を歓迎する。

- GMOサイバーセキュリティ byイエラエの2026年10月19日のブログ（ARTEXの確認）と10月14日頃のブログの本文（同社サイトが簡易版運用のため到達できず）
- 佐川急便の第5報（2026-10-23）、ブックオフグループHDの第2報・訂正・10月23日のPDF、ユーザベースの第二報、コミューン株式会社の続報（2026-10-21）、ラクスライトクラウドの継続更新ページの本文
- 照合待ち25件の一次公表文（ニフティ、リクルート カーセンサーnet、阪急阪神百貨店、ゼビオ、ヤマダホールディングス、カカオピッコマ、新潟日報、バーガーキングなど）
- ARTEXリポジトリの現在の状態（公開・非公開・削除）

（2026年11月3日追記）  
2026年11月3日時点で著者が読めていない以下についても、情報提供を歓迎する。

- コミューン株式会社の公表文（2026-10-09、10-21）の本文。079 ちとせグループの「AI等を用いて自動化された攻撃であったと推定されます」がコミューン社の調査に由来するかを確かめるため
- アララの第2報（2026-11-02）とペイクラウドホールディングスの適時開示の本文、アララの委託元の公表文
- 照合待ち67件の一次公表文（ソニー生命保険、ネットマイル、毎日新聞社、朝日新聞社、インプレス、さとふる、ドン・キホーテ、TBSグロウディアなど）

---

## 📝 License

本書は [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) の下で公開されている。出典を明記すれば、自由に引用・転載・改変できる。

Copyright (c) 2026 Leading.AI
