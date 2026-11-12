# Ingest 自我檢查紀錄

`lint_wiki.py` 只能確認「引用的章節真的存在」，不能確認「這句話真的是那個章節說的」。
下面記錄 ingest 時，agent 寫完頁面後回頭對照原文、在跑 lint 之前自己改掉的句子。
這些都是 lint 抓不到的錯誤類型，所以另外留紀錄。

## S1（2026-11-12）

| 頁面 | 原本寫的 | 問題 | 改成 |
|---|---|---|---|
| `stages/floorplanning.md` Purpose | 列出 die／core、pins、macros、tap cells、power grid，出處只標 log 檔名那一節 | 把 log 檔名（`2_6_floorplan_pdn` 等）解讀成功能，超出該節內容 | 只列出六個 log 名稱；「pre-placement stage」另標 §Tapcell insertion |
| `stages/layout-finishing.md` Purpose | 一句話同時講 `clean_finish` 和 log 檔名，只標一個出處 | 兩件事出自不同章節 | 拆成兩句，各標各的章節 |
| `stages/placement.md` What happens | 「這個階段背後的工具包含 global placement、timing analysis…」 | 原文只是全流程的元件清單，沒說這些屬於 placement 階段 | 改成「流程的步驟清單包含…」 |
| `stages/routing.md` Checks | 「per routing grid cell」 | 原文只寫 GCell，沒有解釋它是什麼 | 直接用 GCell |
| `stages/logic-synthesis.md` What happens | 「synthesis 由 Yosys 執行，log 是 `1_1_yosys.log`」標同一節 | 「由 Yosys 執行」和 log 檔名出自不同章節 | 拆成兩條，各標各的章節 |
| `concepts/placement-density.md` Definition | 「core utilization 是設計預計使用的 core 面積百分比」 | 原文只寫 "The core utilization percentage"，這是我自己補的解釋 | 改成只說它是用 `CORE_UTILIZATION` 設定的百分比 |
| `formats/odb.md` What it is | 「`.odb` 是設計在資料庫中的存檔狀態」 | S1 沒有這句定義 | 改成 S1 實際寫到的內容，定義留缺口（後來由 S2 補上） |
| `tools/openroad.md` Role | 「它的 power grid generator」「它的 pad placement utility」 | S1 沒明說這些工具屬於 OpenROAD | 改成直接寫工具名稱（Pdngen、PDNSim、ICeWall…），並標出清單所在章節 |

## S2（2026-11-12）

| 頁面 | 原本寫的 | 問題 | 改成 |
|---|---|---|---|
| `concepts/asic-design-flow.md` | 「engineering change orders」 | S2 只寫 ECO，沒有展開縮寫；展開是外部知識 | 改回 ECOs |
| `concepts/static-timing-analysis.md` Definition | 「…will perform its function at the intended speed」 | 「at the intended speed」原文沒有 | 刪掉 |
| `concepts/drc.md` Why it matters | 「…which makes them easier to locate」 | 原文只說可以圖形化檢視 | 刪掉後半句 |
| `tools/openroad.md` Role | 「floorplan、timing analysis、antenna check 都是 OpenROAD steps」標 §Run directory | antenna check 的 step 名稱不在那一節 | 只留 floorplan 和 timing analysis |

## 觀察

- 兩次 ingest 的 lint 都是第一輪就通過（見 `lint-history.md`），但上面 12 處問題都發生在 lint 之前，而且 lint 一條都抓不到。
- 錯誤集中在兩類：(1) 把外部知識或自己的推論寫成來源說的；(2) 一句話混了兩個章節的內容卻只標一個出處。
- 這些是 agent 檢查自己的作品，依講義的原則並不可靠。是否在 ingest 階段加一道獨立的忠實度審查，待 Roger 決定。
