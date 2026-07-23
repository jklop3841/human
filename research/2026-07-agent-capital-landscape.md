# 2025—2026 Agent身份、调用、支付与来源证明研究矩阵

更新时间：2026-07-24  
用途：为 `HUMAN-ECONOMY-001` 和 `PIRS 0.1` 提供外部事实边界。

## 结论

截至2026年7月，Agent经济的通信、发现、身份、授权、支付、遥测、许可和软件来源证明已经分别出现开放规范或产业实现；但尚未发现一个被广泛采用的统一标准，把“创造者—协议—Agent版本—运行调用—独立效果—信誉—收入分配”完整绑定。

PIRS属于对这一空白的前瞻性组合设计，不是已有标准的事实描述。

## 来源矩阵

| 模块 | 2025—2026一手来源 | 已经证明 | 没有证明 |
|---|---|---|---|
| Agent协作 | [A2A项目](https://github.com/a2aproject/A2A) | 跨框架Agent需要共同通信语言 | 某Agent能力真实有效 |
| Agent身份 | [A2A 1.0 Signed Agent Cards](https://a2a-protocol.org/latest/announcing-1.0/) | 身份与能力元数据可签名验证 | 元数据中的能力声明为真 |
| 工具发现 | [MCP Registry](https://github.com/modelcontextprotocol/registry) | MCP服务可通过统一注册表发现 | 注册即代表安全、付费或高质量 |
| MCP授权 | [MCP OAuth授权规范](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization) | MCP可组合OAuth保护资源 | 解决创造者归属和效果信誉 |
| Agent身份框架 | [IETF AI Agent Authentication and Authorization草案，2026-07-06](https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/) | Agent应被视为有身份和凭证的工作负载，应组合现有标准 | 已经形成正式RFC或统一行业实施 |
| 用户意图和委托 | [Google AP2](https://developers.googleblog.com/developers-guide-to-ai-agent-protocols/) | 可用签名Mandate表达授权边界，并用Payment Receipt闭环 | 任务结果具有价值 |
| Agent认证趋势 | [FIDO Agentic Authentication Working Group](https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/) | 行业正在处理可验证用户指令、Agent认证和可信委托 | 规范已经最终完成 |
| 机器支付 | [Stripe MPP，2026-03-18](https://stripe.com/blog/machine-payments-protocol) | Agent可通过开放标准进行微支付、周期支付和机器支付 | 付款等于成功或归属成立 |
| HTTP原生支付 | [x402](https://docs.x402.org/introduction) | HTTP 402可承载按请求付款 | 适合所有司法辖区和离线调用 |
| MPP协议流 | [MPP Challenge–Credential–Receipt](https://mpp.dev/protocol) | 支付可以形成挑战、凭证和收据流程 | 取代调用评测和信誉证明 |
| Agent可观测 | [OpenTelemetry GenAI，2026-05-14](https://opentelemetry.io/blog/2026/genai-observability/) | 模型、Token、工具调用、延迟和事件可使用统一遥测语义 | 所有Agent均已稳定采用，或遥测不可伪造 |
| 产物来源 | [GitHub Artifact Attestations](https://docs.github.com/en/actions/concepts/security/artifact-attestations) | Sigstore可签署仓库、提交和构建来源并写入透明日志 | 产物安全、正确或有效 |
| 供应链来源 | [SLSA Provenance](https://slsa.dev/provenance/v1) | 软件产物可描述从何处、何时、如何产生 | 证明作者拥有全部法律权利 |
| 机器许可 | [SPDX Overview](https://spdx.dev/learn/overview/) | 软件和内容可以使用标准许可标识及表达式 | 自定义商业条件自动获得全球执行力 |
| 公开内容许可边界 | [Creative Commons：Human Content to Machine Data，2025](https://creativecommons.org/wp-content/uploads/2025/06/Human-Content-to-Machine-Data_Final.pdf) | 不受技术限制的公开内容难仅靠合同约束下游 | 公开协议可以普遍按次收费 |

## 对PIRS的设计约束

1. 不重新发明Agent通信、OAuth、支付或软件签名。
2. 使用引用和组合方式连接现有证明。
3. 把“身份声明”“来源证明”“调用事实”“效果判断”“法律权利”“支付”分开。
4. 不承诺完全离线环境中的可信计数。
5. 不把A2A Agent Card、GitHub Attestation或Payment Receipt误写成能力证明。
6. PIRS自己的新增对象应尽量收敛为：
   - 协议与Agent Manifest；
   - 调用收据；
   - 评测证明；
   - 信誉快照；
   - 谱系与收益关系。

## 研究状态

- 外部规范变化很快，所有接口在实现前必须重新核验最新版本；
- IETF草案和FIDO工作均处发展阶段；
- OpenTelemetry GenAI语义在2026年仍存在演进；
- PIRS 0.1只用于概念验证和Schema实验，不应声称兼容认证已经获得行业认可。

