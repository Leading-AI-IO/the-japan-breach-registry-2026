#!/usr/bin/env python3
"""registry.json（正本）から registry.csv・registry_en.csv と第4章の本文表（Markdown）を生成する。

使い方:
    python3 scripts/build_registry.py

生成物:
    data/registry.csv       （日本語だけの12列）
    data/registry_en.csv    （英語だけの12列。引用は日本語の公表文からの翻訳）
    docs/jp/_table_ch4.md   （第4章に貼り込む本文表・日本語）
    docs/en/_table_ch4.md   （同・英語）
"""
import csv
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "registry.json"

# 日本語版（registry.csv）：(キー, 見出し)
COLS_JA = [
    ("id", "ID"),
    ("published", "公表日"),
    ("org_ja", "企業・組織"),
    ("scale_ja", "規模（公表文の単位のまま）"),
    ("status_ja", "状態"),
    ("data_ja", "対象情報"),
    ("vector", "経路"),
    ("dates_ja", "侵入日・確認日"),
    ("ai_mention", "AIへの言及"),
    ("primary_url", "一次URL"),
    ("retrieved", "到達日"),
    ("notes_ja", "補足"),
]

# 英語版（registry_en.csv）：(キー, 見出し)。vector は VECTOR_EN で訳す
COLS_EN = [
    ("id", "ID"),
    ("published", "Published"),
    ("org_en", "Organisation"),
    ("scale_en", "Scale (as stated)"),
    ("status_en", "Status"),
    ("data_en", "Data affected"),
    ("vector", "Vector"),
    ("dates_en", "Intrusion / detection dates"),
    ("ai_mention_en", "AI mentioned"),
    ("primary_url", "Primary URL"),
    ("retrieved", "Retrieved"),
    ("notes_en", "Notes"),
]

VECTOR_EN = {
    "脆弱性": "vulnerability",
    "不正アクセス（経路未公表）": "unauthorised access (vector not disclosed)",
    "委託先": "contractor / third-party service",
    "設定不備": "misconfiguration",
    "不正ログイン": "unauthorised login",
    "VPNの脆弱性": "VPN vulnerability",
    "複合": "multiple vectors",
}


def load():
    with SRC.open(encoding="utf-8") as f:
        return json.load(f)


def write_csv(data):
    out = ROOT / "data" / "registry.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow([h for _, h in COLS_JA])
        for r in data["rows"]:
            w.writerow([r[k] for k, _ in COLS_JA])
    return out


def write_csv_en(data):
    out = ROOT / "data" / "registry_en.csv"
    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow([h for _, h in COLS_EN])
        for r in data["rows"]:
            w.writerow([VECTOR_EN[r[k]] if k == "vector" else r[k] for k, _ in COLS_EN])
    return out


def md_escape(s):
    return str(s).replace("|", "｜").replace("\n", " ")


def write_table(data, lang):
    rows = data["rows"]
    if lang == "ja":
        head = "| ID | 公表日 | 企業・組織 | 規模（公表文の単位のまま） | 状態 | 経路 | AI言及 | 一次URL |"
        sep = "|---|---|---|---|---|---|---|---|"
        lines = [head, sep]
        for r in rows:
            lines.append(
                "| {id} | {published} | {org} | {scale} | {status} | {vector} | {ai} | [公表文]({url}) |".format(
                    id=r["id"], published=r["published"], org=md_escape(r["org_ja"]),
                    scale=md_escape(r["scale_ja"]), status=md_escape(r["status_ja"]),
                    vector=md_escape(r["vector"]), ai=md_escape(r["ai_mention"]),
                    url=r["primary_url"]))
        out = ROOT / "docs" / "jp" / "_table_ch4.md"
    else:
        head = "| ID | Published | Organisation | Scale (as stated, original unit) | Status | Vector | AI mentioned | Primary source |"
        sep = "|---|---|---|---|---|---|---|---|"
        lines = [head, sep]
        for r in rows:
            lines.append(
                "| {id} | {published} | {org} | {scale} | {status} | {vector} | {ai} | [notice]({url}) |".format(
                    id=r["id"], published=r["published"], org=md_escape(r["org_en"]),
                    scale=md_escape(r.get("scale_en", r["scale_ja"])),
                    status=md_escape(r["status_en"]),
                    vector=VECTOR_EN.get(r["vector"], r["vector"]),
                    ai="none" if r["ai_mention"] == "なし" else md_escape(r["ai_mention"]),
                    url=r["primary_url"]))
        out = ROOT / "docs" / "en" / "_table_ch4.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def summary(data):
    rows = data["rows"]
    from collections import Counter
    c = Counter(r["vector"] for r in rows)
    print(f"rows: {len(rows)}")
    for k, v in c.most_common():
        print(f"  {k}: {v}")
    print(f"AI mentioned (not なし): {sum(1 for r in rows if r['ai_mention'] != 'なし')}")
    print(f"pending (not in ledger): {len(data.get('pending', []))}")


if __name__ == "__main__":
    data = load()
    print("csv  ->", write_csv(data))
    print("csv  ->", write_csv_en(data))
    print("ja   ->", write_table(data, "ja"))
    print("en   ->", write_table(data, "en"))
    summary(data)
