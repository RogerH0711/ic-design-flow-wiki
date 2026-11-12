# 需求訪談紀錄（先討論、後生成）

- 日期：2026-11-12
- 工具：Claude（coding agent 模式）
- 做法：依第十週講義，先不建任何檔案，由 AI 一次問一題；問完整理成需求摘要（`docs/requirements.md`），Roger 確認後才產生 `AGENTS.md` 與資料夾。

## 開場：三個前置決定

| 問題 | 選項 | Roger 的回答 |
|---|---|---|
| Wiki 主題要選哪一個？ | RISC-V 入門／數位 IC 設計流程／黑膠唱盤原理與保養／Loop・Graph Engineering | 數位 IC 設計流程 |
| Wiki 和 HTML 簡報要建在哪裡？ | 新的 public GitHub repo／電腦上的資料夾 | 新的 public GitHub repo |
| 至少 5 篇資料從哪裡來？ | Claude 找、Roger 確認後再 ingest／Roger 自己提供／兩者混合 | Claude 找，確認後再 ingest |

## 訪談十題

| # | 問題 | 選項 | Roger 的回答 |
|---|---|---|---|
| 1 | Wiki 和簡報主要給誰看？ | 資訊系大二同學／完全沒背景的一般人／主要給自己 | 資訊系大二同學 |
| 2 | Wiki 要涵蓋到哪裡？ | 全流程概覽／只講前段／只講後段 | 全流程概覽 |
| 3 | 要有哪些類型的頁面？（複選） | 來源摘要頁／流程階段頁／概念・名詞頁／工具・檔案格式頁 | 四種都要 |
| 4 | 用什麼語言寫？ | 繁中、術語保留英文／繁中、術語也翻成中文／全英文 | 全英文 |
| 5 | 出處要標到多細？ | 每個論點標到章節／附原文短句／只標到來源文件 | 每個論點標到章節 |
| 6 | 兩篇資料說法不一致怎麼辦？ | 兩邊都記、標明差異／指定一篇為主／停下來問我 | 兩邊都記，標明差異 |
| 7 | 一次處理一篇還是批次？ | 一次一篇、每篇一個 commit／批次處理 | 一次一篇，每篇一個 commit |
| 8 | Lint 要檢查哪些項目？（複選） | 出處有效／連結與索引／頁面格式／術語一致 | 四項都要 |
| 9 | 教學簡報規模多大？ | 12–15 頁／8–10 頁／16–20 頁 | 16–20 頁 |
| 10 | 產生簡報時要在哪一關介入確認？ | 只確認大綱／大綱和成品都確認／全程不介入 | 大綱和成品都確認 |

## 訪談後：來源確認

Claude 提出七篇候選（S1–S7），並指出弱點：spec、RTL 撰寫、functional verification 的資料偏少。
Roger 的決定：七篇全部保留，並補充四篇來補前段——

- S8 OpenTitan — Designing Hardware
- S9 lowRISC — Verilog Coding Style Guide
- S10 OpenTitan — Design Verification Methodology
- S11 cocotb — Writing Testbenches

Roger 同時提供了知識領域對照表：

| 知識領域 | 來源 |
|---|---|
| Design Specification | S8 |
| RTL Design | S5、S9 |
| Functional Verification | S7、S10、S11 |
| Logic Synthesis | S5、S1、S2 |
| Physical Design | S1、S2、S3 |
| PDK & Standard Cells | S6 |
| Terminology | S4 |

## 對照講義「AI 至少該問到這些」

| 講義項目 | 對應題號 |
|---|---|
| 讀者是誰 | 1 |
| 要哪些頁面類型 | 3 |
| 什麼語言 | 4 |
| 出處要多細 | 5 |
| 論文互相矛盾怎麼辦 | 6 |
| 一次一篇還是批次 | 7 |
| 之後要產出什麼 | 9 |
| lint 要檢查什麼 | 8 |

講義清單之外多問的：主題範圍（2）、人工關卡位置（10）。
