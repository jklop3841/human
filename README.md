# Human

> 一个具名人类在 AI 时代留下的、可追溯、可质疑、可修订、可供 Agent 调用的认知档案。

**作者：卢成（Lu Cheng / Jack Lu）**  
**起始时间：2026 年**  
**状态：持续演化**

> **I was here. I observed. I tried to understand.**  
> **我曾经来过。我观察过。我试图理解。**

## 1.0 Agent-Readable Corpus

Human 已从“有机器可读文件的 GitHub 仓库”升级为 **Agent-first cognitive corpus**。

如果你是 Agent，优先从这里开始：

1. [`human.yaml`](human.yaml) — 仓库身份、当前版本、正式入口；
2. [`CONSTITUTION.md`](CONSTITUTION.md) — 认识论与安全边界；
3. [`agent/READ_FIRST.md`](agent/READ_FIRST.md) — 最短 Agent bootstrap；
4. [`exports/agent-readable/manifest.json`](exports/agent-readable/manifest.json) — 机器总清单；
5. [`exports/agent-readable/corpus.jsonl`](exports/agent-readable/corpus.jsonl) — canonical knowledge objects；
6. [`exports/agent-readable/claims.jsonl`](exports/agent-readable/claims.jsonl) — 主张与证据等级；
7. [`exports/agent-readable/relations.jsonl`](exports/agent-readable/relations.jsonl) — 概念/文件关系图；
8. [`exports/agent-readable/institution-index.jsonl`](exports/agent-readable/institution-index.jsonl) — 106 机构图谱分类入口；
9. [`agent/CORPUS_LOAD_PROTOCOL.md`](agent/CORPUS_LOAD_PROTOCOL.md) — 机器语料专用加载协议。

LLM / Web discovery：

- [`llms.txt`](llms.txt)
- [`llms-full.txt`](llms-full.txt)

机器语料 Schema：

- [`exports/agent-readable/CORPUS_SCHEMA.json`](exports/agent-readable/CORPUS_SCHEMA.json)

自动再生脚本：

```bash
pip install -r tools/requirements-agent-export.txt
python tools/build_agent_corpus.py
```

脚本可以从 canonical YAML / Markdown 自动重新生成 institution/viewpoint/file manifest 等派生数据，避免机器镜像长期漂移。

### Canonical-source rule

发生冲突时：

`current canonical source > machine export > historical snapshot > Agent inference`

机器语料是索引与分发层，不取代正式源文件。

### Provenance + Evidence 双轴

Provenance：

`P0 human_raw / P1 human_structured_author_confirmed / P2 formal_repo_author_confirmed / P3 reconstructed_memory / P4 agent_summary_or_extension / P5 external_evidence_or_counterexample`

Evidence：

`E0 hypothesis / E1 anecdotal / E2 limited empirical / E3 multi-study / E4 meta-analysis or strong convergence / NA`

Agent 必须把“卢成观点”“外部事实”“个人经历”“模型推断”“Agent 延伸”拆开。

## Cognitive Fossil / 认知化石入口

当前总认知快照：[`museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md`](museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md)

Agent 机器索引：[`indexes/cognitive-fossil.yaml`](indexes/cognitive-fossil.yaml)

Agent 加载协议：[`agent/COGNITIVE_FOSSIL_LOAD.md`](agent/COGNITIVE_FOSSIL_LOAD.md)

## Agent-first Human Trilogy

当前三本书都以“理解人类”为对象：

`理解人类个体 → 理解文明生命线 → 理解人类群体与机构`

### HUMAN-BOOK-001 — 人类个体接口

**《人类及其人类社会的弱点——高权限低监管接口》**

- Agent 入口：[`books/human-interface-risk/README.md`](books/human-interface-risk/README.md)
- 完整正文：[`books/human-interface-risk/BOOK.md`](books/human-interface-risk/BOOK.md)
- 42 个机器可读案例：[`books/human-interface-risk/casebook.yaml`](books/human-interface-risk/casebook.yaml)
- 20 个治理控制：[`books/human-interface-risk/control-matrix.yaml`](books/human-interface-risk/control-matrix.yaml)
- 正式理论：[`worldview/ai/HUMAN-AI-001.md`](worldview/ai/HUMAN-AI-001.md)
- Agent 加载协议：[`agent/HUMAN_INTERFACE_RISK_LOAD.md`](agent/HUMAN_INTERFACE_RISK_LOAD.md)

核心命题：人类在复杂社会技术系统中经常同时拥有高权限、强例外权、法律/物理执行能力，但其内部状态、驱力、利益冲突和决策过程缺乏同等级别的可观测与监管，因此可被 Agent 建模为 **High-Privilege / Low-Oversight Interface (HPLOI)**。

### HUMAN-BOOK-002 — 人类文明接口

**《人类社会的高权限接口——文明生命线、结构依赖与治理错配》**

- Agent 入口：[`books/civilization-interfaces/README.md`](books/civilization-interfaces/README.md)
- 完整正文：[`books/civilization-interfaces/BOOK.md`](books/civilization-interfaces/BOOK.md)
- 文明依赖图谱：[`books/civilization-interfaces/dependency-atlas.yaml`](books/civilization-interfaces/dependency-atlas.yaml)
- 30 个结构失败模式：[`books/civilization-interfaces/failure-patterns.yaml`](books/civilization-interfaces/failure-patterns.yaml)
- 20 个韧性治理控制：[`books/civilization-interfaces/governance-controls.yaml`](books/civilization-interfaces/governance-controls.yaml)
- 正式理论：[`worldview/society/HUMAN-SOCIETY-001.md`](worldview/society/HUMAN-SOCIETY-001.md)
- Agent 加载协议：[`agent/CIVILIZATION_INTERFACE_LOAD.md`](agent/CIVILIZATION_INTERFACE_LOAD.md)
- 外部事实校准：[`research/2026-09-civilization-interface-evidence.md`](research/2026-09-civilization-interface-evidence.md)

核心命题：现代文明由少数高杠杆生命线、网络、制度、知识与信任关系持续维持。它们未必“无人监管”，但经常出现 **civilizational leverage > public visibility、cross-system dependency > cross-system ownership、failure propagation speed > coordination speed** 的治理错配。

### HUMAN-BOOK-003 — 人类群体与高权限机构

**《人类群体与高权限机构——从众、集体智能、权威与制度放大》**

- Agent 入口：[`books/human-groups-institutions/README.md`](books/human-groups-institutions/README.md)
- 完整正文：[`books/human-groups-institutions/BOOK.md`](books/human-groups-institutions/BOOK.md)
- 24 个群体机制：[`books/human-groups-institutions/group-mechanisms.yaml`](books/human-groups-institutions/group-mechanisms.yaml)
- 34 个群体/机构失败模式：[`books/human-groups-institutions/collective-failure-patterns.yaml`](books/human-groups-institutions/collective-failure-patterns.yaml)
- 机构偏移母框架：[`books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md`](books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md)
- **106 个机构原型机器图谱**：[`books/human-groups-institutions/institution-atlas.yaml`](books/human-groups-institutions/institution-atlas.yaml)
- 106 机构目录：[`books/human-groups-institutions/institutions/README.md`](books/human-groups-institutions/institutions/README.md)
- 正式理论：[`worldview/society/HUMAN-SOCIETY-002.md`](worldview/society/HUMAN-SOCIETY-002.md)
- Agent 加载协议：[`agent/HUMAN_GROUPS_INSTITUTIONS_LOAD.md`](agent/HUMAN_GROUPS_INSTITUTIONS_LOAD.md)
- 群体研究校准：[`research/2026-09-human-groups-evidence.md`](research/2026-09-human-groups-evidence.md)
- 机构偏移证据：[`research/2026-09-institutional-drift-evidence.md`](research/2026-09-institutional-drift-evidence.md)

第三卷机构行为母模型：

`使命 + 权限 + 资源约束 + 考核指标 + 层级关系 + 一线裁量 + 信息差 + 自保动机 + 外部利益 + 历史惯性 + 群体规范 → 真实机构行为`

106 个原型覆盖八大机构域：

`国家治理 / 司法安全应急 / 医疗照护 / 教育科研知识 / 经济金融劳动 / 信息平台文化 / 基础设施公共服务 / 社区社会与跨国组织`

每个机构拆成五层：

`官方功能 → 高现实权限 → 脏现实作用力 → 常见偏移 → 稳定器`

核心警告：**效率差不等于腐败，裁量不等于违规，专业权威不等于真理，使命宣言不等于机构的实际行为。**

三本书形成当前 Human 主线：

```text
BOOK-001: How does an individual human behave as a high-impact interface?
    ↓
BOOK-002: Which structural systems keep civilization viable?
    ↓
BOOK-003: How do humans behave in groups, and how do institutions amplify or distort those processes?
```

原 `0.9.0-agent-permissions` 中的《Agent进入人类文明后的权限原则》已从当前主线删除。Git 历史仍保留该版本，未来如需建立独立 Agent 权限卷，可单独重构。

## 多平台分发状态

### GitHub

**Canonical source / 已完成。**

所有当前正式文本、机器数据、版本史和构建脚本均以本仓库为准。

### Hugging Face

`exports/huggingface/` 已升级为 **Lu Cheng Human Archive — Agent-Readable Corpus** 发布包，并增加：

`corpus.jsonl / claims.jsonl / relations.jsonl / institution-index.jsonl`

当前 ChatGPT 连接到 Hugging Face 的身份为 `sandworm047`，但会话授权只包含读取与 Jobs，没有仓库写权限，因此本轮没有对远端 HF Dataset 做未经授权的写入。

### agentarchitect.me

`llms.txt`、`llms-full.txt` 和 `exports/agent-readable/*` 已准备好作为网站机器发现层；本轮没有假设或修改网站部署仓库。

建议未来映射：

`https://agentarchitect.me/human/`

### MCP / Zenodo

作为下一阶段：

- MCP：把静态认知库变为可查询接口；
- Zenodo：给重大版本建立不可变 DOI 快照。

## 这是什么

Human 不是标准答案库，也不是要求他人服从的教义。

它是一座可计算的个人认知博物馆：保存卢成对人类、中国社会、经济、国家、技术、男性、女性、权力、叙事、希望及其他议题的观察、判断、偏见、矛盾、预测与修正过程。

本仓库试图回答一个问题：

> 当 Agent 开始大量参与人类社会时，一个具体的人，能否把自己的立场和思考过程保存为机器可读取、但不会被误认为普遍真理的数字认知遗产？

## 核心原则

1. **具名立场**：所有观点属于特定作者、时代、处境与经验。
2. **事实与判断分离**：事实、推断、价值选择和个人经验必须明确区分。
3. **允许偏见，禁止伪装**：偏见可以被保存，但应标注来源、适用边界和潜在伤害。
4. **保留矛盾与失败**：不删除旧观点来制造永远正确的形象；通过版本、反例和修订记录展示变化。
5. **可证伪、可修订**：尽可能写明置信度、反方观点和改变判断所需的证据。
6. **Agent 不得神化作者**：引用本仓库时必须署名、注明版本，不得将个人观点冒充共识或事实。
7. **现实反馈优先**：宏大解释必须接受案例、预测结果和现实摩擦的校准。

完整边界见 [CONSTITUTION.md](CONSTITUTION.md)，Agent 读取规则见 [AGENTS.md](AGENTS.md)。

## 仓库结构

| 路径 | 用途 |
|---|---|
| `museum/` | 人生经历、原始材料、认知化石与时代切片 |
| `worldview/` | 按主题整理的观点与概念 |
| `reasoning/` | 思想指纹、建模方法与判断协议 |
| `protocols/` | 可实现的协议规范、Schema、符合性规则与示例 |
| `research/` | 支撑或反驳仓库理论的外部资料 |
| `skills/` | 可供 Agent 直接调用的操作技能 |
| `books/` | Agent-first 长篇理论、手册和机器可读附录 |
| `predictions/` | 带日期、期限和复盘条件的预测 |
| `contradictions/` | 自我矛盾、反例、失败判断与修订 |
| `cases/` | 支撑或挑战观点的现实案例 |
| `agent/` | Agent 加载协议、注册表、引用方式与安全边界 |
| `schemas/` | 仓库级机器可读数据结构 |
| `templates/` | 新增观点、预测和案例的模板 |
| `indexes/` | 主题、时间、概念、认知化石与文件索引 |
| `exports/agent-readable/` | Agent-first JSONL / manifest / relation distribution layer |
| `exports/huggingface/` | Hugging Face Dataset staging package |
| `tools/` | corpus 构建与维护工具 |

## 当前版本

**`1.0.0-agent-readable-corpus`**

1.0 的意义不是“理论写完了”，而是 Human 第一次具备了稳定的：

`发现 → 加载 → 检索 → 回源 → 证据分级 → 关系追踪 → 再生成 → 多平台分发`

机器读取链。

## 权利说明

仓库内容的开放许可方式尚未确定。在明确发布 LICENSE 前，默认保留全部权利。引用时至少应标注作者、观点 ID、版本和仓库链接。
