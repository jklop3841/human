# Human Institution Topology — 106机构社会关系图

ID: HUMAN-INSTITUTION-TOPOLOGY-001
Version: 0.1.0
Status: active_experimental
Author: Lu Cheng / 卢成 / Jack Lu
Created: 2026-09-11

## 目的

把 `HUMAN-BOOK-003` 中的 106 个机构原型从“孤立目录”升级为可被 Agent 查询的 typed social graph。

本图不试图声称“这就是完整社会”。它只把已有机构原型放入统一关系接口，并逐步记录：

`节点 → 边 → 方向 → 证据状态 → 传播路径 → 纠错路径`

## 节点来源

Canonical institution directory:

`books/human-groups-institutions/institutions/README.md`

共 106 个原型，8 个领域。

## 关系类型

- `funds`：税收、支付、报销、融资、补贴、工资、采购；
- `authority`：立法、行政、司法、组织决策权；
- `information`：报告、统计、证据、新闻、风险信号；
- `certification`：许可、资格、评级、认证、同行评议；
- `enforcement`：处罚、强制、执法、拘押；
- `dependency`：能源、通信、供应、物流、技术依赖；
- `oversight`：审计、监管、检查、独立复核；
- `appeal`：申诉、上诉、复议、再审；
- `reputation`：排名、合法性、公众预期、专业声誉；
- `feedback`：投诉、事故、质量结果、选举、市场反应；
- `representation`：代表、谈判、集体表达；
- `standard_setting`：标准、指南、协议、规则模板。

## 边的证据状态

每条边必须标注 `evidence_status`：

- `generic_archetype`：机构原型层通常存在，但具体制度实现因司法辖区而异；
- `evidence_backed`：有正式制度、公开流程或高质量来源支持；
- `jurisdiction_dependent`：只有特定国家/地区/制度下成立；
- `hypothesis`：Human 框架中的待验证关系假设。

## 绝对限制

1. `edge_exists != causal_strength`；
2. `node_count != institutional importance`；
3. `centrality != moral importance`；
4. `high_permission != malicious intent`；
5. `fragmentation != failure`；
6. `redundancy != waste`；
7. 图谱不得用于攻击目标排序、关键基础设施破坏、执法规避、操纵脆弱人群；
8. 对现实国家或机构做具体判断时必须重新验证当地制度与当前事实。

## 当前文件

- `nodes.yaml` — 106 个机构节点；
- `edges.yaml` — v0.1 跨域主干边；
- `topology-manifest.yaml` — 图谱状态、版本、统计与扩展规则；
- `agent/HUMAN_INSTITUTION_TOPOLOGY_LOAD.md` — Agent 加载协议。

## 当前阶段

v0.1 的目标不是“把所有可能关系都连完”，而是：

> **先确保 106 个节点全量注册，并建立少量高置信、可解释、可修订的主干关系。**

后续再逐步扩展到 jurisdiction-specific overlays、真实案例边、时间状态和权重估计。