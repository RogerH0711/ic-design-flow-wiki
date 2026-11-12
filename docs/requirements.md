# 需求摘要（2026-11-12 確認）

由 `docs/interview.md` 的訪談整理而成。Roger 確認這份摘要之後，才產生 `AGENTS.md` 與資料夾。
右欄標出每一項寫進 `AGENTS.md` 的哪一節，方便逐條對照。

| # | 項目 | 決定 | AGENTS.md |
|---|---|---|---|
| R1 | 主題 | 數位 IC 設計流程，全流程概覽：spec → RTL → verification → synthesis → floorplan／placement／CTS／routing → signoff → GDSII | §1 Topic |
| R2 | 深度 | 每關講輸入、輸出、在檢查什麼，不深入演算法 | §1 Depth、§4 stage 必備小節 |
| R3 | 讀者 | 資訊系大二同學：懂邏輯閘和 flip-flop，沒碰過 IC 設計流程 | §1 Reader |
| R4 | 頁面類型 | 來源摘要頁、流程階段頁、概念／名詞頁、工具／檔案格式頁 | §2、§4 |
| R5 | 語言 | Wiki 和簡報全英文 | §1 Language、§9（lint LANG） |
| R6 | 出處細度 | 每個論點標 `[來源代號 §章節標題]` | §3 規則 3、§5 |
| R7 | 來源矛盾 | 兩種說法並列、各附出處，並記進 `log.md` | §7 |
| R8 | Ingest 方式 | 一次一篇，每篇一個 commit；前兩篇做完先給 Roger 看 | §8 |
| R9 | Lint | 出處有效、連結與索引、頁面格式、術語一致，都寫成腳本 | §9、`scripts/lint_wiki.py` |
| R10 | 後續產出 | 16–20 頁教學 HTML 簡報，主題是一顆數位晶片從 RTL 到 GDSII 怎麼做出來 | §10 |
| R11 | 人工關卡 | 大綱確認一次，渲染成 HTML 後再確認一次 | §10 |
| R12 | 建置位置 | public GitHub repo，簡報用 GitHub Pages 公開 | （repo 本身） |
| R13 | 資料來源 | Claude 找開放授權資料，Roger 確認後才 ingest；Roger 補充 S8–S11 | §3 規則 1、§11 |

## 訪談沒有問到、由 Claude 提出的假設（Roger 看過後沒有提出異議）

- 簡報 workflow 採用講義的 graph 形式，每一關的產出都是檔案，錯在哪一關就退回哪一關。
- 忠實度檢查另開一個沒看過製作過程的 sub-agent，只給它簡報稿和引用的 Wiki 頁。
- Wiki 只能寫來源裡有的內容；來源沒寫的地方留下固定的缺口標記，不用外部知識補。

## 確認後的來源清單

| 代號 | 文件 | 主要涵蓋 | 授權 |
|---|---|---|---|
| S1 | OpenROAD Flow Scripts Tutorial | RTL-to-GDS 全流程 | BSD-3-Clause |
| S2 | LibreLane Newcomers' Tutorial | ASIC 流程入門、signoff | Apache-2.0 |
| S3 | LibreLane: Achieving Timing Closure | timing、STA | Apache-2.0 |
| S4 | LibreLane Glossary | 名詞定義 | Apache-2.0 |
| S5 | Yosys: A primer on digital circuit synthesis | 抽象層級、synthesis | ISC |
| S6 | SkyWater SKY130 PDK: Libraries、File Types | PDK、standard cell、檔案格式 | Apache-2.0 |
| S7 | Verilator User's Guide: Overview | RTL 模擬 | LGPL-3.0-only OR Artistic-2.0 |
| S8 | OpenTitan: Designing Hardware | 規格制定、設計階段 | Apache-2.0 |
| S9 | lowRISC Verilog Coding Style Guide | RTL 撰寫 | CC-BY-4.0 |
| S10 | Design Verification Methodology within OpenTitan | 驗證方法、coverage | Apache-2.0 |
| S11 | cocotb: Writing Testbenches | testbench | BSD-3-Clause |

每篇的上游 repo、鎖定的 commit 與授權檔位置記在 `raw/sources.json`。
