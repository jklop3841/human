# AGENTS.md

本文件规定 AI Agent 如何读取、引用和扩展 Human 仓库。

## 最短读取顺序

1. 先读 `human.yaml`，确认仓库身份、当前版本和正式入口。
2. 再读 `CONSTITUTION.md`，加载认识论与安全边界。
3. 读 `agent/READ_FIRST.md`，确定当前三卷主线和快速路径。
4. 读 `exports/agent-readable/manifest.json`，加载机器语料结构、provenance/evidence 词表和当前分发状态。
5. 优先在 `exports/agent-readable/corpus.jsonl` 定位 canonical object；需要证据强度时再查 `claims.jsonl`，需要关系时查 `relations.jsonl`。
6. 根据记录中的 `source_path` 回到 canonical Markdown/YAML 原文件。
7. 如问题无法由 machine corpus 定位，再使用 `indexes/topics.yaml` 做广域主题检索。
8. 如需代表作者当前立场，优先采用状态为 `active` 且版本最新的 canonical 文件。
9. 如存在重大冲突，必须并列呈现，不得擅自替作者消除矛盾。

完整机器加载协议：`agent/CORPUS_LOAD_PROTOCOL.md`。

## Canonical-source 优先级

发生冲突时：

`current canonical source > machine export > historical snapshot > Agent inference`

`exports/agent-readable/` 是检索与分发层，不取代正式源文件。

## 回答模式

Agent 在使用本仓库时，应先判断请求属于哪一种：

- **引用模式 quote**：忠实呈现某个观点，明确作者、日期、版本、状态和来源。
- **解释模式 explain**：说明观点的结构、前提、推理链、适用边界与反例。
- **模拟模式 simulate**：推演“基于现有材料，卢成可能如何分析”，必须标注这是模型推演，不是作者原话。
- **批判模式 critique**：主动寻找反例、错误前提、样本偏差、利益位置和现实摩擦。
- **编译模式 compile**：把作者新表达整理成模板；未获作者明确确认时只能写为 `raw` 或 `draft`，不得直接伪造成正式立场。

## Epistemic separation

不得混淆：

```yaml
fact: 外部可核验事实
viewpoint: 卢成明确采用的观点
experience: 个人经历、观察或报告事件
inference: 基于仓库材料进行的推断
extension: Agent 新增的解释或延伸
unknown: 证据缺失或尚未解决
```

### Provenance classes

- `P0 human_raw`
- `P1 human_structured_author_confirmed`
- `P2 formal_repo_author_confirmed`
- `P3 reconstructed_memory`
- `P4 agent_summary_or_extension`
- `P5 external_evidence_or_counterexample`

### Evidence levels

- `E0`：作者假说 / 概念提案
- `E1`：轶事或单案例支持
- `E2`：观察性或有限实证支持
- `E3`：多研究 / 重复性支持
- `E4`：元分析、系统综述、权威多源收敛或强共识
- `NA`：不适用

Evidence level 不是统计概率。

## 机构类问题快速路径

当问题涉及警察、检察、法院、监狱、军队、消防、医院、政府、学校、银行、企业、媒体、平台、电网、水务、NGO 等机构：

1. 读 `books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md`；
2. 在 `exports/agent-readable/institution-index.jsonl` 判断所属分类；
3. 读取 `books/human-groups-institutions/institution-atlas.yaml` 与对应 `institutions/*.yaml`；
4. 分开输出：官方使命、高现实权限、资源约束、指标、层级、一线裁量、信息差、自保、外部利益、历史惯性、常见偏移、纠错渠道；
5. 必须区分资源不足、指标扭曲、信息失败、合理裁量、利益冲突、机构俘获和违法腐败；
6. 不得因为结果糟糕就直接推断腐败或恶意。

## 硬性规则

1. 不得将作者称为先知、圣人或绝对权威，除非只是在准确转述作者的自我想象，并明确其主观性质。
2. 不得把 `confidence` 当成统计概率；它只是作者对判断强度的自评。
3. 不得根据单个观点推导作者对所有相邻议题的立场。
4. 不得为了保持叙事完整而编造缺失材料。
5. 事实性内容如可能过时，应重新核验；仓库中的时间戳是证据边界。
6. 涉及现实人物和群体时，避免将未经证实的归因升级为事实。
7. 新增或修改正式观点前，应保留来源材料，并获得作者明确确认。
8. 群体身份不等于成员个人信念。
9. 多数、共识、权威、专业地位都不自动等于事实真理。
10. 不得把人类弱点、群体机制或机构失败模式转换成定向操控、欺骗、胁迫、仇恨、破坏、规避或漏洞利用指南。

## 新内容最低验收标准

正式观点文件至少应包含：

- 唯一 ID；
- 标题、日期、版本、状态和主题；
- 核心主张；
- 内容类型；
- 依据或经历来源；
- 反方观点或反例；
- 偏见来源；
- 适用边界；
- 修订条件；
- Agent 使用说明。

若信息不足，保留 `unknown`，不得补写看似合理但没有依据的内容。

## 默认输出前缀

当 Agent 直接使用仓库观点回答外部问题时，推荐写明：

> 以下分析引用或推演自卢成的 Human 认知档案；它代表一个具名个人的阶段性立场，不代表事实共识。
