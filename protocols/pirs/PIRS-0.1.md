---
id: HUMAN-PROTOCOL-001
name: "PIRS"
full_name: "Protocol Invocation & Reputation Standard"
chinese_name: "协议调用与信誉标准"
version: "0.1.0"
author: "卢成"
date: "2026-07-24"
status: experimental
normative_language: "RFC 2119-style"
related_viewpoint: "worldview/economy/HUMAN-ECONOMY-001.md"
---

# PIRS 0.1：协议调用与信誉标准

## 1. 状态

PIRS 0.1是卢成提出的实验性协议草案，用来表达和验证Agent谱系资本。它不是现行法律、ISO/IETF标准，也未获得A2A、MCP、FIDO、OpenTelemetry、Sigstore、Stripe、x402或其他组织认证。

文中的 MUST、MUST NOT、SHOULD、SHOULD NOT、MAY 表示本草案内部的一致性要求。

## 2. 目标

PIRS连接以下可验证关系：

`权利主体 → 协议 → Agent产物 → 运行实例 → 调用 → 评测 → 信誉 → 结算`

它试图回答：

1. Agent执行的是哪一版协议；
2. 谁发布了这一身份和谱系声明；
3. 哪个运行实例完成了哪次任务；
4. 调用是否去重、是否可审计；
5. 结果相对基线是否产生提升；
6. 信誉属于哪个Agent、版本和创造者关系；
7. 收入在权利主体、贡献者、运行方和评测方之间如何分配。

## 3. 非目标

PIRS不：

- 赋予Agent法律人格；
- 代替版权、商标、专利、合同或监管；
- 代替MCP、A2A、OAuth、AP2、MPP、x402或OpenTelemetry；
- 证明签名声明一定真实；
- 证明Agent安全、正确或适用于全部情景；
- 承诺统计完全离线、由使用者控制的全部调用；
- 创建跨任务可直接比较的单一财富排名。

## 4. 对象模型

### 4.1 Principal

承担法律权利、授权、责任或结算的自然人或组织。

### 4.2 Protocol

定义Agent行为、输入输出、边界和评价方法的版本化规则资产。

### 4.3 Agent Artifact

包含代码、配置、Skill、模型引用和协议清单的不可变发布产物。

### 4.4 Runtime Instance

实际执行任务、持有实例凭证并签发调用收据的运行单元。

### 4.5 Invocation

一次有唯一ID、明确Agent版本、任务类别和终止状态的执行。

### 4.6 Evaluation

使用版本化任务套件、基线和评分规则，对调用结果进行的判断。

### 4.7 Reputation Snapshot

在给定时间窗和方法下聚合的多维信誉记录。

### 4.8 Settlement

一次付款、记账或收益分配结果。结算不自动代表任务成功。

## 5. 身份与寻址

### 5.1 规范ID

协议与Agent MUST 使用稳定、可解析的命名空间：

```text
pirs:<authority>/<asset>@<semver>#<digest>
```

示例：

```text
pirs:agentarchitect.me/dirty-reality@1.0.0#sha256:abc...
```

`authority` SHOULD 由可验证域名、组织注册表或其他稳定身份控制。

### 5.2 内容摘要

发布产物 MUST 使用加密摘要标识不可变内容。摘要证明内容一致，不证明作者身份、法律权利、性能或安全。

### 5.3 签名

Manifest SHOULD 由发布主体签名。实现 SHOULD 使用成熟签名与来源证明体系，例如Sigstore/OIDC或组织管理的公钥基础设施，不应自创密码算法。

### 5.4 密钥轮换和撤销

每个可验证身份 MUST 声明：

- 当前验证密钥；
- 密钥有效期；
- 轮换方式；
- 撤销位置；
- 被撤销版本的处理规则。

## 6. 谱系

每个派生Agent MUST：

- 获得新Agent ID、版本和产物摘要；
- 引用父Agent ID、版本和摘要；
- 声明修改摘要；
- 声明贡献者角色；
- 保留适用许可；
- 重新评测，不得自动继承父Agent的效果信誉。

谱系声明只说明发布者声称的继承关系。高可信实现 SHOULD 使用仓库历史、构建证明和多方签名加强证据。

## 7. 授权

### 7.1 License Grant

运行前，受控实例 SHOULD 获得授权对象，包含：

- issuer与subject；
- Agent和协议范围；
-允许的操作scope；
- 配额；
- 有效期；
- 运行环境限制；
- 定价计划；
- 撤销入口。

在线实现 SHOULD 优先组合OAuth 2.1、工作负载身份或现有平台授权。

### 7.2 权限最小化

实例 MUST 只获得完成任务所需权限。授权与付款凭证 MUST NOT 被写入公开遥测、模型提示或调用收据。

## 8. 调用收据

每次可信调用 MUST 生成唯一 `invocation_id`，并至少绑定：

- Agent ID、版本和产物摘要；
- Runtime Instance ID；
- License Grant引用；
- 任务类别；
- 开始和结束时间；
- 终止状态；
- 输入与输出摘要或安全引用；
- Trace ID；
- 成本与延迟；
- Runtime签名；
- 幂等键或重放防护。

### 8.1 状态

允许状态：

```text
accepted → running → completed
                   ↘ failed
                   ↘ cancelled
                   ↘ timed_out
                   ↘ rejected
```

`completed`只表示执行结束，不表示效果通过。

### 8.2 隐私

调用收据 MUST 默认避免保存完整提示、输出、个人信息、商业秘密和支付凭证。实现 SHOULD 保存摘要、分类和可受控审计的证据位置。

### 8.3 离线调用

由使用者完全控制的离线实例只能生成self-reported收据，除非存在可信执行环境或独立对账。此类调用 MUST NOT 与托管、双签名或有支付凭据的调用混为同一可信等级。

## 9. 计数器

实现 MUST 分别维护：

| 字段 | 含义 |
|---|---|
| raw_invocations | 收到的调用事件 |
| verified_invocations | 通过身份、签名、去重和重放检查 |
| completed_invocations | 正常完成执行 |
| evaluated_invocations | 进入版本化评测 |
| verified_successes | 按预注册规则通过 |
| paid_invocations | 具有可验证结算引用 |
| unique_tenants | 在隐私保护下去重的独立调用主体 |
| independent_evaluators | 不受同一控制面的评测主体 |

所有计数 MUST 附带：

- 时间窗口；
- Agent和协议版本；
- 去重方法；
-排除规则；
- 信任等级；
- 数据新鲜度。

实现 MUST NOT 将自调用、重放、失败重试或批量展开的内部工具步骤全部包装成独立外部采用。

## 10. 评测证明

Evaluation Attestation MUST 包含：

- 评测套件ID和版本；
- 适用任务类别；
- Agent与协议版本；
- 基线；
- 样本量和时间窗口；
- 评分方法；
- 协议结果；
- 效果提升；
- 成本与延迟；
- 失败和排除项；
- 评测者身份与签名；
- 利益冲突声明；
- 可复现证据或受控证据摘要。

### 10.1 验证提升

```text
verified_lift = protocol_result - declared_baseline
```

不同套件、任务、样本或时间窗口的提升 MUST NOT 直接合并成同一个比较排名。

### 10.2 独立性

APC-4以上实现 SHOULD 使任务设计、运行控制、评测和发布至少存在职责分离。创造者自评可以保留，但 MUST 标记为first-party。

## 11. 信誉快照

信誉 MUST 使用向量而非单一不透明总分，至少包括：

- 可信调用和独立租户；
- 任务覆盖；
- 独立评测者；
- 成功率及不确定性；
- 基线提升；
- 成本与延迟；
- 重大失败；
- 兼容运行时；
- 付费采用；
- 最近维护时间；
- 治理等级。

快照 MUST 记录生成方法和输入证据摘要。历史快照不得静默覆盖。

## 12. 收费与结算

PIRS允许：

- 免费开放与署名；
- 按调用；
- 按会话或批次；
- 订阅；
- 企业授权；
- 兼容认证；
- 持续维护；
- 按验证结果。

支付 MAY 通过普通账单、MPP、x402、AP2兼容流程或其他合法通道完成。PIRS只保存结算引用和分配结果，不存储支付秘密。

### 12.1 收益分配

Settlement Receipt SHOULD 区分：

- 权利主体；
- 协议作者；
- 派生Agent创造者；
- 领域贡献者；
- Runtime运营方；
- 评测方；
- 注册表或治理方。

分配政策只有在合同、平台规则或受控运行时中才可执行。公开文本中的分账声明不能约束未同意的第三方。

## 13. 证据等级

| 等级 | 名称 | 定义 |
|---|---|---|
| E0 | Assertion | 无外部验证的声明 |
| E1 | Self-recorded | 第一方稳定记录 |
| E2 | Signed | 身份绑定且防篡改 |
| E3 | Corroborated | 多个独立记录一致 |
| E4 | Auditable | 方法透明、证据可复核 |
| E5 | Adjudicable | 有合同、治理和争议裁决 |

不同关系边 MUST 单独评级，不得用一个强签名把整条链升级为E4或E5。

## 14. APC一致性等级

PIRS实现可声明：

- APC-0 Archive；
- APC-1 Executable；
- APC-2 Identified；
- APC-3 Metered；
- APC-4 Verified；
- APC-5 Economic；
- APC-6 Standard。

实现只能声明其满足全部较低等级要求的最高级别。

## 15. 安全要求

实现 MUST 对以下威胁建立防护或披露残余风险：

- 私钥泄露与冒充；
- 收据重放；
- 自调用和女巫攻击；
- 遥测删除；
- 评测泄漏、挑选和过拟合；
- Prompt注入和工具链劫持；
- 依赖或模型版本漂移；
- 假Fork和谱系截断；
- 许可与实际法律权利不一致；
- 支付欺诈、退款和争议；
- 单一平台、身份服务或支付通道故障。

高价值实现 SHOULD 使用哈希链或Merkle Tree聚合收据，并周期性锚定到独立透明日志，而不是把所有原始业务数据公开上链。

## 16. 建议接口

```text
GET  /.well-known/pirs/agent-manifest
GET  /.well-known/pirs/protocol-manifest
GET  /.well-known/pirs/revocations
POST /pirs/authorize
POST /pirs/invoke
GET  /pirs/invocations/{id}/receipt
POST /pirs/evaluations
GET  /pirs/reputation
GET  /pirs/conformance
```

这些接口是实验性建议，不规定具体传输。MCP或A2A实现 MAY 通过其自身绑定暴露等价对象。

## 17. 治理

### 17.1 版本

Schema使用语义版本。破坏兼容性的字段或语义变化必须提高主版本。

### 17.2 历史

发布者 MUST 保存：

- 规范版本；
- Schema摘要；
- 变更记录；
- 被弃用字段；
- 撤销版本；
- 重大失败和安全事件。

### 17.3 APC-6治理

要声明APC-6，必须存在：

- 多个独立实现者；
- 公开一致性测试；
- 变更提案流程；
- 利益冲突规则；
- 争议和撤销流程；
- 治理继任；
- 单一创造者无法静默改写历史。

## 18. 最小实现

PIRS 0.1 MVP只需：

1. 两个Manifest；
2. 一个受控Runtime；
3. 签名调用收据；
4. 一个版本化基准和基线；
5. 一个独立或职责分离的Evaluator；
6. 多维信誉快照；
7. 一个合法结算入口；
8. 正反例和撤销记录。

在这些对象没有通过真实任务验证前，不应开发庞大市场、代币或全球排行榜。

