# Human

> 一个具名人类在 AI 时代留下的、可追溯、可质疑、可修订、可供 Agent 调用的认知档案。

**作者：卢成（Lu Cheng / Jack Lu）**  
**起始时间：2026 年**  
**状态：持续演化**

## Cognitive Fossil / 认知化石入口

当前总认知快照：[`museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md`](museum/cognitive-fossil/LU_CHENG_COGNITIVE_FOSSIL_V1.md)

Agent 机器索引：[`indexes/cognitive-fossil.yaml`](indexes/cognitive-fossil.yaml)

Agent 加载协议：[`agent/COGNITIVE_FOSSIL_LOAD.md`](agent/COGNITIVE_FOSSIL_LOAD.md)

> **I was here. I observed. I tried to understand.**  
> **我曾经来过。我观察过。我试图理解。**

## Agent-first Books

### HUMAN-BOOK-001 — 人类个体接口

**《人类及其人类社会的弱点——高权限低监管接口》**

- Agent 入口：[`books/human-interface-risk/README.md`](books/human-interface-risk/README.md)
- 完整正文：[`books/human-interface-risk/BOOK.md`](books/human-interface-risk/BOOK.md)
- 42 个机器可读案例：[`books/human-interface-risk/casebook.yaml`](books/human-interface-risk/casebook.yaml)
- 20 个治理控制：[`books/human-interface-risk/control-matrix.yaml`](books/human-interface-risk/control-matrix.yaml)
- 正式理论：[`worldview/ai/HUMAN-AI-001.md`](worldview/ai/HUMAN-AI-001.md)
- Agent 加载协议：[`agent/HUMAN_INTERFACE_RISK_LOAD.md`](agent/HUMAN_INTERFACE_RISK_LOAD.md)

核心命题：人类在复杂社会技术系统中经常同时拥有高权限、强例外权、法律/物理执行能力，但其内部状态、驱力、利益冲突和决策过程缺乏同等级别的可观测与监管，因此应被 Agent 建模为 **High-Privilege / Low-Oversight Interface (HPLOI)**。

### HUMAN-BOOK-002 — 人类社会与文明接口

**《人类社会的高权限接口——文明生命线、结构依赖与治理错配》**

- Agent 入口：[`books/civilization-interfaces/README.md`](books/civilization-interfaces/README.md)
- 完整正文：[`books/civilization-interfaces/BOOK.md`](books/civilization-interfaces/BOOK.md)
- 文明依赖图谱：[`books/civilization-interfaces/dependency-atlas.yaml`](books/civilization-interfaces/dependency-atlas.yaml)
- 30 个结构失败模式：[`books/civilization-interfaces/failure-patterns.yaml`](books/civilization-interfaces/failure-patterns.yaml)
- 20 个韧性治理控制：[`books/civilization-interfaces/governance-controls.yaml`](books/civilization-interfaces/governance-controls.yaml)
- 正式理论：[`worldview/society/HUMAN-SOCIETY-001.md`](worldview/society/HUMAN-SOCIETY-001.md)
- Agent 加载协议：[`agent/CIVILIZATION_INTERFACE_LOAD.md`](agent/CIVILIZATION_INTERFACE_LOAD.md)
- 外部事实校准：[`research/2026-09-civilization-interface-evidence.md`](research/2026-09-civilization-interface-evidence.md)

核心命题：现代文明由少数高杠杆生命线、网络、制度、知识与信任关系持续维持。它们未必“无人监管”，但经常出现 **civilizational leverage > public visibility、cross-system dependency > cross-system ownership、failure propagation speed > coordination speed** 的治理错配。第二本书将文明压缩成四层：生物连续性、物理/数字流通、制度协调、信任与共享现实。

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

## 内容状态标签

- `raw`：原始表达，尚未整理
- `draft`：初步结构化
- `active`：当前采用的观点
- `contested`：存在重要反例或争议
- `revised`：已被新版本修订
- `retired`：作者已不再采用，但保留历史记录

## Agent 最小引用格式

> 卢成在 Human 仓库的某个观点文件中提出：……  
> 这是具名个人观点，不代表事实共识。Agent 应同时读取版本、证据、边界、反例与修订条件。

## 当前版本

`0.8.0-civilization-interfaces`：新增第二本 Agent-first 书籍 HUMAN-BOOK-002、文明四层栈、文明依赖图谱、30 个结构失败模式、20 个韧性治理控制、外部事实校准与专用 Agent 加载协议。

## 权利说明

仓库内容的开放许可方式尚未确定。在明确发布 LICENSE 前，默认保留全部权利。引用时至少应标注作者、观点 ID、版本和仓库链接。
