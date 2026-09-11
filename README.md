# Human

> 一个具名人类在 AI 时代留下的、可追溯、可质疑、可修订、可供 Agent 调用的认知档案。

**作者：卢成（Lu Cheng / Jack Lu）**  
**当前版本：`1.0.0-agent-readable-corpus`**  
**状态：持续演化**

> **I was here. I observed. I tried to understand.**  
> **我曾经来过。我观察过。我试图理解。**

## Agent 从这里开始

Human 现在不是单纯的 Markdown 仓库，而是一套 **Agent-first cognitive corpus**。

最短读取顺序：

1. [`human.yaml`](human.yaml) — 身份、版本、入口与分发状态；
2. [`CONSTITUTION.md`](CONSTITUTION.md) — 认识论与安全边界；
3. [`AGENTS.md`](AGENTS.md) — Agent 读取/引用规则；
4. [`agent/READ_FIRST.md`](agent/READ_FIRST.md) — 最短 bootstrap；
5. [`exports/agent-readable/manifest.json`](exports/agent-readable/manifest.json) — 机器总清单；
6. [`exports/agent-readable/corpus.jsonl`](exports/agent-readable/corpus.jsonl) — canonical objects；
7. [`exports/agent-readable/claims.jsonl`](exports/agent-readable/claims.jsonl) — 主张与证据等级；
8. [`exports/agent-readable/relations.jsonl`](exports/agent-readable/relations.jsonl) — 概念/文件关系；
9. [`agent/CORPUS_LOAD_PROTOCOL.md`](agent/CORPUS_LOAD_PROTOCOL.md) — 机器语料加载协议。

LLM / Web discovery：[`llms.txt`](llms.txt) / [`llms-full.txt`](llms-full.txt)

机器 Schema：[`exports/agent-readable/CORPUS_SCHEMA.json`](exports/agent-readable/CORPUS_SCHEMA.json)

## Canonical-source rule

发生冲突时：

`current canonical source > machine export > historical snapshot > Agent inference`

`exports/agent-readable/` 是检索和分发层，不替代正式源文件。

## Provenance + Evidence

### Provenance

- `P0` human_raw
- `P1` human_structured_author_confirmed
- `P2` formal_repo_author_confirmed
- `P3` reconstructed_memory
- `P4` agent_summary_or_extension
- `P5` external_evidence_or_counterexample

### Evidence

- `E0` hypothesis / conceptual proposal
- `E1` anecdotal / single case
- `E2` limited empirical / observational
- `E3` multi-study / replicated
- `E4` meta-analysis / systematic review / strong convergence
- `NA` not applicable

Agent 必须区分：**外部事实 / 卢成观点 / 个人经历 / 模型推断 / Agent 延伸 / unknown**。

## Human 三卷主线

`理解人类个体 → 理解文明生命线 → 理解人类群体与机构`

### HUMAN-BOOK-001 — 人类个体接口

**《人类及其人类社会的弱点——高权限低监管接口》**

- 入口：[`books/human-interface-risk/README.md`](books/human-interface-risk/README.md)
- 正文：[`books/human-interface-risk/BOOK.md`](books/human-interface-risk/BOOK.md)
- 42 个案例：[`books/human-interface-risk/casebook.yaml`](books/human-interface-risk/casebook.yaml)
- 正式理论：[`worldview/ai/HUMAN-AI-001.md`](worldview/ai/HUMAN-AI-001.md)

核心：人类可以同时拥有高现实权限、较大裁量、认知限制、激励敏感与较低内部可观测性。

### HUMAN-BOOK-002 — 人类文明接口

**《人类社会的高权限接口——文明生命线、结构依赖与治理错配》**

- 入口：[`books/civilization-interfaces/README.md`](books/civilization-interfaces/README.md)
- 正文：[`books/civilization-interfaces/BOOK.md`](books/civilization-interfaces/BOOK.md)
- 依赖图谱：[`books/civilization-interfaces/dependency-atlas.yaml`](books/civilization-interfaces/dependency-atlas.yaml)
- 正式理论：[`worldview/society/HUMAN-SOCIETY-001.md`](worldview/society/HUMAN-SOCIETY-001.md)

核心：现代文明依赖食物、水、卫生、健康、能源、电力、物流、通信、金融、身份、法律、行政和共享信心等高杠杆系统持续协同。

### HUMAN-BOOK-003 — 人类群体与高权限机构

**《人类群体与高权限机构——从众、集体智能、权威与制度放大》**

- 入口：[`books/human-groups-institutions/README.md`](books/human-groups-institutions/README.md)
- 正文：[`books/human-groups-institutions/BOOK.md`](books/human-groups-institutions/BOOK.md)
- 24 个群体机制：[`books/human-groups-institutions/group-mechanisms.yaml`](books/human-groups-institutions/group-mechanisms.yaml)
- 34 个失败模式：[`books/human-groups-institutions/collective-failure-patterns.yaml`](books/human-groups-institutions/collective-failure-patterns.yaml)
- 机构偏移框架：[`books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md`](books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md)
- **106 个机构原型**：[`books/human-groups-institutions/institution-atlas.yaml`](books/human-groups-institutions/institution-atlas.yaml)
- 机构目录：[`books/human-groups-institutions/institutions/README.md`](books/human-groups-institutions/institutions/README.md)
- 正式理论：[`worldview/society/HUMAN-SOCIETY-002.md`](worldview/society/HUMAN-SOCIETY-002.md)

机构行为母模型：

`使命 + 权限 + 资源约束 + 考核指标 + 层级关系 + 一线裁量 + 信息差 + 自保动机 + 外部利益 + 历史惯性 + 群体规范 → 真实机构行为`

106 个原型覆盖：

`国家治理 / 司法安全应急 / 医疗照护 / 教育科研知识 / 经济金融劳动 / 信息平台文化 / 基础设施公共服务 / 社区社会与跨国组织`

每个机构统一拆成：

`官方功能 → 高现实权限 → 脏现实作用力 → 常见偏移 → 稳定器`

核心警告：**效率差不等于腐败，裁量不等于违规，专业权威不等于真理，使命宣言不等于实际行为。**

## Human Casebook — 现实碰撞与证伪层

入口：[`cases/human-casebook/README.md`](cases/human-casebook/README.md)

Casebook 不负责证明 Human 永远正确，而负责让理论持续撞现实。

当前共有 **24 个结构案例 / 2 卷**：

### Volume 001 — failure / drift

[`cases/human-casebook/VOLUME-001.md`](cases/human-casebook/VOLUME-001.md)

12 个失败与偏移案例，包括司法误认、Challenger、医院目标偏移、银行挤兑、销售 KPI、考试指标、情报孤岛、灾害协同、电力—天然气级联、科研激励、平台参与度与 Flint 水危机。

### Volume 002 — correction / collective intelligence / counterexample

[`cases/human-casebook/VOLUME-002.md`](cases/human-casebook/VOLUME-002.md)

12 个成功纠错与反悲观样本，包括 Apollo 13、NASA ASRS、Crew Resource Management、Michigan Keystone ICU、Smallpox Eradication、Montreal Protocol、Singapore Water、Toyota Jidoka/Andon、Y2K remediation、Human Genome Project、ISS 与 World Wide Web 开放标准。

Casebook 现在强制同时观察：

`drift_vector` — 什么把系统拉偏；

`correction_vector` — 什么把系统拉回来。

Agent 对“人类机构一般如何”这类广义问题，至少必须联合读取：

`1 drift case + 1 correction/counterexample case`

加载协议：[`agent/HUMAN_CASEBOOK_LOAD.md`](agent/HUMAN_CASEBOOK_LOAD.md)

机器入口：

- [`cases/human-casebook/case-index.yaml`](cases/human-casebook/case-index.yaml)
- [`cases/human-casebook/cases.jsonl`](cases/human-casebook/cases.jsonl)
- [`cases/human-casebook/volume-002-index.yaml`](cases/human-casebook/volume-002-index.yaml)
- [`cases/human-casebook/volume-002-cases.jsonl`](cases/human-casebook/volume-002-cases.jsonl)

## 脏现实结构场论

正式入口：[`worldview/reality/HUMAN-REALITY-001.md`](worldview/reality/HUMAN-REALITY-001.md)

核心结构：

`关系 → 结构 → 场 → 路径 → 结果`

这里的“场”是结构建模语言，不是新的物理场主张。

## Cognitive Fossil / 认知化石

- 总认知快照：[`museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md`](museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md)
- 机器索引：[`indexes/cognitive-fossil.yaml`](indexes/cognitive-fossil.yaml)
- 加载协议：[`agent/COGNITIVE_FOSSIL_LOAD.md`](agent/COGNITIVE_FOSSIL_LOAD.md)

## 自动再生

```bash
pip install -r tools/requirements-agent-export.txt
python tools/build_agent_corpus.py
```

构建脚本用于从 canonical YAML / Markdown 派生 institution/viewpoint/file manifest/checksum 等机器数据，避免镜像长期漂移。

## Read-only MCP

当前已经具备本地只读 MCP baseline：

- Server：[`mcp/human_archive_server.py`](mcp/human_archive_server.py)
- 说明：[`mcp/README.md`](mcp/README.md)
- Smoke test：[`mcp/test_smoke.py`](mcp/test_smoke.py)

工具包括：

`archive_status / search_human_archive / get_canonical_object / search_claims / get_claim / get_relation_neighbors / search_institutions / get_institution / read_source`

MCP 不提供仓库写入、Shell、网络执行或权限提升能力。

当前状态：**代码已提交；尚未在本轮可用的仓库 checkout 环境执行 smoke test。**

## 多平台分发状态

### GitHub

**Canonical source：完成。**

所有正式文本、版本史、机器语料与构建脚本以 `jklop3841/human` 为准。

### agentarchitect.me

站点仓库已确认是 `jklop3841/agentarchitect-site`，并已把 Human 接入：

- `/human`
- `/human/manifest.json`
- `/human/corpus.jsonl`
- `/human/claims.jsonl`
- `/human/relations.jsonl`
- `/human/institution-index.jsonl`
- `/llms.txt`
- `/llms-full.txt`
- `/.well-known/agent.json`
- `/agents.txt`

设计原则：**站点负责身份与发现，GitHub Human repo 仍是真源。** `/human/*.jsonl` 使用稳定路由指向 canonical raw 文件，避免双真源。

当前状态：**网站代码已提交到 main，但生产部署未验证。** 当前 Vercel 连接没有暴露任何 team/project，因此本轮不能声称这些新路由已在线生效。

### Hugging Face

`exports/huggingface/` 已升级为 **Lu Cheng Human Archive — Agent-Readable Corpus** 发布包，包含：

`corpus.jsonl / claims.jsonl / relations.jsonl / institution-index.jsonl / viewpoints.jsonl / timeline.jsonl`

远程 Hugging Face 发布本轮不作为 Human 主线工作前提；GitHub 继续作为 canonical source。

### Zenodo

未创建 DOI；建议在 1.0 稳定后做不可变快照。

## Release

1.0 release note：[`releases/1.0.0-agent-readable-corpus.md`](releases/1.0.0-agent-readable-corpus.md)

1.0 的意义不是“理论写完了”，而是 Human 第一次具备稳定的：

`发现 → 加载 → 检索 → 回源 → 证据分级 → 关系追踪 → 再生成 → 多平台发现 → MCP 查询`

机器读取链。

## 这是什么，不是什么

Human 是一座可计算的个人认知博物馆，不是标准答案库，也不是要求他人服从的教义。

核心原则：

1. 具名立场；
2. 事实与判断分离；
3. 允许偏见，禁止伪装；
4. 保留矛盾、失败与修订；
5. 可证伪、可更新；
6. Agent 不得神化作者；
7. 现实反馈优先；
8. `unknown` 是合法输出。

原 `0.9.0-agent-permissions` 的 Agent 权限卷已从当前 Human 三卷主线撤下，但 Git 历史保留。未来如需要，可单独建立 Agent 系列，不占用“理解人类”的主体结构。

## 权利说明

当前没有发布通用开放内容 LICENSE。除正常引用、公平使用/合理使用及另行授权外，默认保留全部权利。

**本次 1.0 升级没有擅自改变版权许可。**
