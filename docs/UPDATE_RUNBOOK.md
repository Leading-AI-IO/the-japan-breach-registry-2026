# The Japan Breach Registry 2026 — 更新手順書

このファイルは公開されている。台帳に書くのは著者一人であり（README「Governance」参照）、その一人が実際にどの手順で追記・訂正を行っているかを、読者が検証できる状態に置くためである。本書が読者に求める検証可能性を、著者自身の運用手順にも適用している。

**対象リポジトリ**：`https://github.com/Leading-AI-IO/the-japan-breach-registry-2026`
**署名鍵**：`3DD95BA9EC194524`（`Satoshi Yamauchi <s3atoshi@gmail.com>`・ed25519）。`the-ai-forecast-registry` と同じ鍵。公開鍵はGitHubの著者アカウントに登録済みで、各コミットの `Verified` バッジと照合できる。秘密鍵はここに含まれない。
**最終更新**：2026-10-16（v2.0・36行・照合待ち11件。続報の追記・訂正を7行に反映し、照合待ちから032〜036を収載）

---

## この手順書が守っているもの

本書が本文で宣言している運用は5つある。**手順はすべてこの5つを実装するために存在する。**

1. **一次公表文を著者が開いて読んだ行だけを載せる** ── 報道・二次資料・他のAIの出力だけで行を起こさない
2. **単位と表現を公表文のまま保つ** ── 件を人に換算しない。「可能性」を「確認」に書き換えない。経路が書かれていなければ「不正アクセス（経路未公表）」と書く
3. **追記専用** ── 行を削除も書き換えもしない。訂正は、訂正である旨と日付を明記して追記する
4. **正本と派生物は同時更新** ── `data/registry.json` を編集し、`scripts/build_registry.py` で `registry.csv` と本文の表を生成し、同じコミットに入れる
5. **全コミットに署名、秘密鍵はリポジトリに入れない** ── `the-ai-forecast-registry` の手順書（付録A・B）と同じ

手順の途中で迷ったら、その操作が上の5つのどれを守るためのものかに戻ること。

---

## 0. 作業前の確認（毎回）

```powershell
cd <リポジトリのクローン先>
git remote -v
git fetch origin
git log --oneline HEAD..origin/main
git status
git config --get pull.rebase
Get-ChildItem -Recurse -File -Include *.asc,*.rev,*.gpg,*.key,*.pgp
```

- `git remote -v` に `the-japan-breach-registry-2026.git` が表示されること
- `git log --oneline HEAD..origin/main` の出力が空であること（空でなければ `git pull --no-rebase --no-edit`）
- `git status` が `nothing to commit, working tree clean` であること
- `pull.rebase` が `false` であること
- 最後のコマンドが何も表示しないこと

---

## 1. 行を追加する場合（照合待ちから台帳へ、または新規の事案）

### 1-1. 一次公表文に到達する

当事組織のドメイン上の公表文（HTMLまたはPDF）、または適時開示（TDnet配信の同文）を、著者が自分で開いて読む。報道記事、まとめサイト、他のAIの要約は、到達の根拠にしない。

到達できない場合は、行を起こさない。`registry.json` の `pending` に、組織名・公表日・報道ベースの規模・未収載の理由・参照URLを書く（既に `pending` にある場合はそのまま）。

### 1-2. 記録する内容を揃える

公表文から、次を公表文の表現のまま抜き出す。

| フィールド | 規律 |
|---|---|
| `published` | 公表文の日付。続報がある場合は初報の日付を `published` にし、続報の日付は `scale_ja` または `notes_ja` に書く |
| `scale_ja` | 公表文の数字と単位を逐語で（鉤括弧で囲む）。「最大」「約」「件」「名」「アカウント」をそのまま。内訳があれば括弧内に |
| `status_ja` | 「確認」「可能性」「おそれ」「最大」「否定できない」など、公表文の語をそのまま |
| `vector` | `脆弱性`／`VPNの脆弱性`／`委託先`／`設定不備`／`不正ログイン`／`複合`／`不正アクセス（経路未公表）` のいずれか。公表文に経路の記述がなければ最後のもの |
| `dates_ja` | 侵入日・検知日・判明日・遮断日のうち公表文にあるもの。なければ「記載なし」 |
| `ai_mention` | 公表文本文に攻撃側のAIに関する語があれば逐語、なければ `なし`。社名・製品名の「AI」は数えない |
| `primary_url` | 開いた公表文のURL |
| `retrieved` | 開いた日 |
| `notes_ja` | 経路の逐語、続報のURL、他の行との関係など |

### 1-3. ファイルを編集して生成する

```powershell
# data/registry.json の rows 末尾に行を追加（IDは連番）。pending にあった場合はそこから削除
python scripts/build_registry.py
```

生成された `docs/jp/_table_ch4.md` の内容を、本文 `docs/jp/the-japan-breach-registry-2026_JP.md` の「## 第1版の31行」（版が上がれば見出しの行数も更新）の表と置き換える。英語版も同様に `docs/en/_table_ch4.md` で置き換える。

本文の「## 数えると」「## 照合待ち（台帳の外）」、第1章の「100万を超える行」の表、第2章の経路の集計、READMEのRowsバッジと更新履歴、`llms.txt` の行数を、新しい行数に合わせて更新する。**第1版の数字に触れる箇所は、（YYYY年M月D日追記）を前置して追記し、第1版の記述は残す。**

### 1-4. コミットして push

```powershell
git add data/registry.json data/registry.csv docs/jp/_table_ch4.md docs/en/_table_ch4.md docs/jp/the-japan-breach-registry-2026_JP.md docs/en/the-japan-breach-registry-2026_EN.md README.md README_en.md llms.txt
git status
git diff --cached --stat
git commit -m "Register row 032: <組織名>（<公表日>）"
git show --stat HEAD
git fetch origin
git log --oneline HEAD..origin/main
git push
git verify-commit HEAD
```

- `git add -A` は使わない（追跡されていないファイルを巻き込むため）
- `git show --stat HEAD` に鍵ファイルや意図しないファイルが含まれていないこと
- `git verify-commit HEAD` が `Good signature from "Satoshi Yamauchi <s3atoshi@gmail.com>"` を返すこと

---

## 2. 既存の行を訂正する場合（続報で数字が変わった、誤りを指摘された）

行は書き換えない。次の2つを行う。

1. `registry.json` の該当行の `notes_ja` 末尾に、`（YYYY年M月D日訂正）` に続けて、何がどう変わったか、根拠の一次URL、指摘者の名（本人の希望があれば）を追記する。`scale_ja` などの元の値は残し、新しい値は `notes_ja` に書く
2. 本文中で元の値に触れている箇所の直前に `（YYYY年M月D日訂正）` を置き、改行して訂正文を書く

コミット件名は `Correct row 017: <内容>`。

続報で状態が「可能性」から「確認」に変わった場合も同じ扱いとする。元の「可能性」は残す。

---

## 3. 証拠の段階（第3章）を更新する場合

日本の事案で、セキュリティ企業・当局が攻撃側のAI使用を一次資料で報告した場合、第3章の該当段階に追記する。

- 追記は `（YYYY年M月D日追記）` を前置する
- 逐語は原語のまま、発言者・公表日・URLを添える
- 段階の判定（証拠つき／痕跡／可能性）は、本文の定義に従う。「証拠つき」は、攻撃者の手元の資料、フォレンジックの結果、当局の捜査結果のいずれかがあるときだけ
- 第5章のH1・H4の判定を併せて見直し、変える場合は同様に追記する

コミット件名は `Update tier: <事案>`。

---

## 4. 版を上げる場合

照合待ちが台帳に移って行数が大きく変わったとき、または章の判定が変わったときに版を上げる。`registry.json` の `version`・`snapshot_date`、READMEの更新履歴、`llms.txt` の冒頭を更新し、GitHubのReleasesに版を作る。

**第2版（2026-10-16）での実施**：第1版の31行の表（`## 第1版の31行`）は書き換えず、その直後に「### 2026年10月16日に追加した5行」として追加行の表を置いた。追加行は `docs/jp/_table_ch4.md` の033行目以降から取る。以後の版でも、既存の表を直さず、追加行を日付つきの別表に置く。

---

## 5. 失敗時の対応

`the-ai-forecast-registry` の `docs/UPDATE_RUNBOOK.md` 第5節と付録A〜Cを、そのまま適用する（コミットメッセージの誤り、内容の誤り、署名の失敗、秘密鍵の混入、pushの拒否）。本書に固有の失敗は次の1つである。

**生成スクリプトを実行せずに本文の表だけを直した。** 本文の表と `registry.json` が一致しなくなる。`python scripts/build_registry.py` を実行し、生成された表で本文を置き換えてからコミットする。本文の表を直接編集してはならない。

---

## 付録：第1版の照合の記録

第1版の31行は、2026年10月10日に著者が各公表文を開いて確認した。Deep Research（Claude・ChatGPT・Perplexity・Gemini）の出力は候補の発見に使い、収載の根拠には使っていない。4本のうちGemini版は、他の3本と矛盾する断定（説明候補の「明確に否定」、二次ブログに基づく数値）を含んでいたため、候補の発見にも使っていない。

第1版の時点で、著者が到達できなかった一次公表文は、`registry.json` の `pending` 16件のとおりである。

（2026年10月16日追記）  
2026年10月16日に、032〜036の5行を照合待ちから台帳に移した。著者が同日に開いて読んだ公表文は、032 ブックオフグループホールディングスの適時開示（2026年10月9日）、033 大和証券の公表文（2026年10月5日）、034 佐川急便の第2報（2026年10月1日）、035 ユーザベースの第一報（2026年10月8日）、036 ホワイトエッセンスの公表文（2026年10月5日）である。同日、既存7行（001・008・018・019・023・027・028）の続報を各公表文で確認し、補足欄に日付つきで追記・訂正した。照合待ちは11件である。
