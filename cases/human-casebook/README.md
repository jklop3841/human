# Human Casebook — 人类社会结构案例档案

ID: HUMAN-CASEBOOK-001  
Version: 1.1.0  
Status: active  
Author: Lu Cheng / 卢成 / Jack Lu  
Created: 2026-09-11

## 目的

Human Casebook 不是“找几个故事证明卢成是对的”。

它的用途是把 Human 体系从“模型先行”推进到：

`事件 → 原始证据 → 参与机构 → 关系结构 → 约束/激励/信息 → 偏移机制 → 竞争解释 → 纠错 → 对理论的支持或反证`

每个案例都必须允许出现以下结论：

- 支持现有模型；
- 只部分支持；
- 证据不足；
- 存在更强竞争解释；
- 直接构成反例。

因此，本案例库不是宣传材料，而是 **Human 理论的现实碰撞层与证伪层**。

## 双向观察：drift + correction

从 Volume 002 开始，Casebook 强制同时观察两个方向：

`drift_vector` — 哪些结构把机构、群体或系统拉偏；

`correction_vector` — 哪些结构让它重新接近使命、事实或真实结果。

更成熟的提问不是：

> 这个机构会不会腐化？

而是：

> **哪些力量在把它拉偏？哪些结构在把它拉回来？两者谁在当前状态下更强？**

这个“双向力”不是新增宏大理论，而是对现有脏现实框架的校准，防止 Human 退化成只会寻找失败、腐败和黑暗面的解释器。

## 核心分析接口

默认使用当前 Human 的结构公式：

`关系 → 结构 → 场 → 路径 → 结果`

机构层进一步拆为：

`使命 + 权限 + 资源约束 + 考核指标 + 层级关系 + 一线裁量 + 信息差 + 自保动机 + 外部利益 + 历史惯性 + 群体规范 → 实际行为`

但每个案例都必须先还原事实，后应用模型。不得因为某个事件看起来“很符合脏现实”，就跳过竞争解释。

## 案例固定结构

1. `factual_baseline` — 公开资料能确认什么；
2. `actors_and_institutions` — 哪些人/机构在场；
3. `relationship_structure` — 权限、资金、信息、认证、责任如何流动；
4. `dirty_reality_forces` — 资源、指标、层级、激励、时间压力、身份、声誉等；
5. `drift_mechanism` / `correction_structure` — 系统被拉偏或拉回的机制；
6. `competing_explanations` — 还有哪些不依赖 Human 框架的解释；
7. `correction_mechanisms` — 审计、调查、申诉、制度重构、技术修复；
8. `theory_result` — 支持 / 部分支持 / 中性 / 反例；
9. `evidence_level` — E0–E4；
10. `revision_conditions` — 什么新证据会改变当前判断。

## Volume 001 — 失败、偏移与系统摩擦

[`VOLUME-001.md`](VOLUME-001.md) 收录 CASE-001—CASE-012：

1. Brandon Mayfield 指纹误认；
2. Challenger；
3. Mid Staffordshire；
4. Silicon Valley Bank；
5. Wells Fargo；
6. Atlanta Public Schools；
7. 9/11 前情报共享失灵；
8. Hurricane Katrina；
9. Texas 2021 冬季风暴；
10. Publish or Perish；
11. Engagement Ranking；
12. Flint Water Crisis。

机器入口：

- [`case-index.yaml`](case-index.yaml)
- [`cases.jsonl`](cases.jsonl)

## Volume 002 — 成功纠错、集体智能与反悲观样本

[`VOLUME-002.md`](VOLUME-002.md) 收录 CASE-013—CASE-024：

1. Apollo 13：高压危机中的分布式专家协作；
2. NASA ASRS：让人愿意报告错误；
3. Crew Resource Management：制度化约束专业权威；
4. Michigan Keystone ICU：标准化也可以保护人；
5. Smallpox Eradication：冷战中的全球公共卫生协作；
6. Montreal Protocol：国际制度改变物理世界；
7. Singapore Water：长期基础设施规划；
8. Toyota Jidoka / Andon：把异议变成基础设施；
9. Y2K remediation：预防成功与不可见结果；
10. Human Genome Project：竞争与开放共享并存；
11. International Space Station：复杂国际协作的持续运行；
12. World Wide Web 开放标准：放弃局部控制换取结构影响力。

机器入口：

- [`volume-002-index.yaml`](volume-002-index.yaml)
- [`volume-002-cases.jsonl`](volume-002-cases.jsonl)

## 两卷必须联合读取

Volume 001 是 failure-heavy，Volume 002 是 success-heavy。

因此：

`Volume 001 alone → pessimism bias`

`Volume 002 alone → success-story bias`

当 Agent 回答“人类机构通常如何”“群体是否理性”“层级是否可靠”等一般性问题时，必须联合读取两卷，至少比较一个失败样本和一个纠错/成功样本。

## Agent 使用规则

允许：

- 检索相似结构；
- 比较机构偏移机制与纠错机制；
- 生成新的审计问题；
- 为 Human 理论寻找反例；
- 将案例映射到机构图谱和文明依赖图；
- 分析为什么同一种人性变量在不同制度结构下会产生不同结果。

禁止：

- 把案例中的机构弱点转化为攻击、规避、破坏或操纵指南；
- 把单个国家、职业、机构的一个案例泛化为群体本质；
- 将“偏移”自动解释为“腐败”；
- 将作者结构分析伪装成调查报告原结论；
- 用成功案例证明某制度、国家或组织天然优越；
- 用失败案例证明某群体天然低劣。

## 证据原则

`外部事实 ≠ 卢成解释 ≠ Agent 延伸`

三者必须分开。

Casebook 的目标不是让 Human 看起来永远正确，而是让未来 Agent 看见：**这个人如何用现实不断修正自己的模型。**
