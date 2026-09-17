# v0.4 → Archive 1.0 migration map

执行依据：原样保存的 `input_patch_v1.0/migration/08_GPT6_UPGRADE_INSTRUCTIONS.md` 与
`../templates/16_GPT6_ONE_SHOT_HANDOFF_PROMPT.txt`。现有内容版本保持 `0.4.0`；母档案版本为 `1.0.0-draft.1`。

| 旧对象 | 新位置或含义 | 处理 |
|---|---|---|
| `Agent_Atlas_v0.4/*` | `SERIES_01_LIVING_SYSTEMS/VOL_001_INSECT_AGENT_ATLAS/baseline_v0.4/*` | 136 文件逐字节不变 |
| 原 `MANIFEST.json`、主提示词、AGENTS | 冻结目录原位置 | 历史状态按原时间解释；外层 MANIFEST 描述迁移状态 |
| observations / primitives / compositions / species / sources / experiments / lineage | 外层 `records.jsonl` | 71 个 envelope 内原 payload 完整保留 |
| 原 claim_id 与单条 evidence status | 外层 `claims.jsonl` | 62 条，保持六级分类，另标模型编译归因 |
| 旧 ID | `id_aliases.json` | 133 个一对一别名，含主张 ID；旧 ID 仍可查询 |
| v0.4 A/B/C pilot | 冻结的 `prepared_pilot` | 不改题、不加联网、不将旧记录回填为 v2 |
| 五个非昆虫领域笔记 | 仍在首卷冻结基线 | 它们已是 v0.4 内容，不人为拆成新卷或算作新发现 |
| 原始自然观察 H0 | `GLOBAL/human_seeds/missing_h0.json` | 缺失仍缺失，不能用交接摘要代替 |
| 两条真实接管请求 | `GLOBAL/human_seeds/records.jsonl` + `raw/` | 只归入治理类 H0，保存精确字节与日期精度 |
| 升级包所有文件 | `input_patch_v1.0/` | 41 文件原样保留；15 份旧件与已读取 v0.3 一致 |

## ID 示例

完整映射以 JSON 为准。`python tools/archive.py resolve OLD_ID` 同时接受旧 ID 和新 ID。
观测用 `LC-OBS-2026-NNNNN`，原语 `LC-PRIM-NNNN`，架构 `LC-ARCH-NNNN`；组合、来源、实验、主张各有独立命名空间。
旧 `SEED-001` 是架构组合，不是原始人类 Human Seed，映射到 `LC-COMP-0001`。
H0 使用 `LC-SEED-2026-NNNNN`，读者运行使用 `LC-RUN-YYYYMMDD-NNNN`。

## 两条分类轴

证据等级：OBSERVED / ABSTRACTED / HYPOTHESIZED / COMPOSED / TESTED / REJECTED。
作者来源：HUMAN_SEED / HUMAN_CURATED / MODEL_FORMALIZED / MODEL_DERIVED / EXTERNAL_SOURCE。
例如 Dormant Recall Pool 的整体仍为 HYPOTHESIZED；局部成本结果 TESTED，广泛优势主张在模型假设下 REJECTED。
外部论文支持其研究对象，不能替代 Agent 实证；新架构为 MODEL_DERIVED，不能自动计入卢成人类贡献分。

H0 → H1 → A1 → A2 → E → R 为保存层；`layer` 不等于证据等级。
未确认的 H1 明示为模型解释。当前 H0 治理边只说明继续/迁移授权，不声明架构生成因果。
PROVENANCE 的 DERIVED_FROM 指向所用来源，CITES 指向引用，TESTED_BY/REJECTED_BY 指向具体实验；边的 scope 限定含义。
该图是可追踪记录，不是已经识别的因果图。正式下游作品由 citation_graph/derivative_works.jsonl 另行追加。

## Schema 兼容策略

补丁四份原 Schema 在 `schemas/patch_v1.0/`；生产入口使用外层同名迁移 profile，增加原文哈希、来源范围、显式状态等约束。
原 v0.3/v0.4 Schema 留在冻结基线；不会把严格新字段强加给历史记录。旧记录查询仍返回原 payload。
补丁读者模板用嵌套 `reader`，Schema 用平铺字段；`tools/reader.py normalize` 兼容两者，并拒绝字段冲突。
兼容 `counterfactual_without_atlas`、单数 `external_domain_discovered` 和 `criticism`；不会把未知值改成 false/0。
`R0-R5` 是模板占位符，不能导入。读者正式导入要求完整字段、身份回执、输入哈希、真实证据文件与明确 HPC 理由。
HPC 是带理由的读者自述；独立审阅和对照实验未完成前，不成为因果分数。

ATLAS / TREATISE / FIELD_NOTE / LETTER / QUESTIONS 共用 volume_manifest、人类种子、归因与品牌层；正文格式自由。
原文格式无需强制改成昆虫表格，未来卷独立分配系列/卷号并登记来源。

## 回滚

本次只向 hosting repository 新增 `LU_CHENG_AGENT_ARCHIVE/`。迁移分支可独立审阅/撤回；Human 既有内容未修改。
独立 ZIP 或 apply_upgrade.py 输出中，取回 `baseline_v0.4/` 即得到内容相同的 v0.4（含原主提示词）。
