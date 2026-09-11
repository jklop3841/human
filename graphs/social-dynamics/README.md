# HUMAN-SOCIAL-DYNAMICS-001

## Time / State Overlay — 人类社会状态叠加层

Status: active_experimental  
Created: 2026-09-11  
Author: Lu Cheng / 卢成 / Jack Lu

## Purpose

`HUMAN-INSTITUTION-TOPOLOGY-001` 描述“哪些机构之间存在什么类型的关系”。本层继续回答：

> **当社会从正常、扩张、危机、紧急、改革、恢复等不同状态切换时，同一张关系图如何变形？**

这不是另起一套宏大理论，而是给现有 Human 加一个时间维度。

基础表达：

`静态拓扑 + 状态变量 + 触发条件 + 边变化 + 节点变化 + 反馈 → 状态化社会结构`

与既有框架兼容：

`关系 → 结构 → 场 → 可行路径集合 → 选择/反馈 → 结果`

状态叠加层不改变 canonical node identity，而改变：

- 哪些边变强、变弱、出现或暂停；
- 哪些节点获得更多/更少权限；
- 哪些资源从平时配置切换到应急配置；
- 信息速度、验证深度、反馈周期如何变化；
- 哪些临时机制应在恢复期退出；
- 哪些危机中形成的有效纠错机制应被制度化。

## Six base states

1. `NORMAL` — 正常态：既定规则、预算、权限和反馈机制稳定运行。
2. `EXPANSION` — 扩张态：需求、投资、组织规模或任务边界快速扩大。
3. `CRISIS` — 危机态：现有机制仍在，但资源、信任、时间或依赖承受高压。
4. `EMERGENCY` — 紧急态：常规机制不足以应对，需要临时权限、快速协调或规则弹性。
5. `REFORM` — 改革态：制度主动重写激励、权限、接口或监督关系。
6. `RECOVERY` — 恢复态：从危机/紧急状态返回稳定运行，并决定哪些临时机制退出、哪些改进固化。

这些是分析标签，不是现实世界中互斥、离散、自动可观测的自然类别。一个系统可以同时具有多个状态特征。

## State variables

统一使用：

- `authority_shift`
- `resource_pressure`
- `information_velocity`
- `verification_depth`
- `coordination_density`
- `discretion_level`
- `feedback_latency`
- `rule_flexibility`
- `public_trust`
- `dependency_exposure`

变量默认不赋虚构数字。除非有外部数据支持，只允许使用 `lower / baseline / higher / mixed / unknown`。

## Dynamic edge operations

状态变化只能使用以下操作描述边：

- `strengthen`
- `weaken`
- `activate`
- `suspend`
- `reroute`
- `accelerate`
- `slow`
- `centralize`
- `decentralize`
- `increase_verification`
- `decrease_verification`

禁止把这些标签直接解释成道德评价。

## Core safeguards

1. `CRISIS != collapse`
2. `EMERGENCY != authoritarianism`
3. `authority_shift != abuse`
4. `rule_flexibility != lawlessness`
5. `more coordination != better outcome`
6. `faster information != more accurate information`
7. `recovery != return_to_old_state`
8. `temporary power != permanent legitimacy`
9. 同一危机可同时增强 drift vector 与 correction vector。
10. 具体国家、时间和制度下的状态变化必须重新验证。

## Initial overlays

- `overlays/healthcare.yaml`
- `overlays/justice.yaml`
- `overlays/finance.yaml`
- `overlays/science.yaml`
- `overlays/infrastructure.yaml`
- `overlays/information-platforms.yaml`

每个 overlay 至少描述：

`NORMAL → stress transition → CRISIS/EMERGENCY → RECOVERY`

并同时记录：

`drift_risks + correction_opportunities + exit_conditions`

## What this is not

这不是预测引擎，也不是“危机发生后必然怎样”的剧本。它是一套结构化提问接口，用于强迫 Agent 在谈论危机、改革或恢复时显式说明：

- 哪些节点变了；
- 哪些边变了；
- 为什么变；
- 什么证据支持；
- 哪些变化应当退出；
- 哪些判断仍然未知。
