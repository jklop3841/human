# Changelog

## 0.9.1-human-groups-institutions — 2026-09-11

- 根据作者最新判断，将 Human 主线重新限定为“理解人类”，撤下 `0.9.0-agent-permissions` 中作为第三卷的《Agent进入人类文明后的权限原则》；
- 删除当前 active tree 中的 `HUMAN-AI-002`、`books/agent-civilization-permissions/` 与 `agent/AGENT_CIVILIZATION_PERMISSION_LOAD.md`；相关思想仍保留于 Git 历史，未来可作为独立 Agent 权限卷重新建立；
- 新增正式观点 `HUMAN-SOCIETY-002`《人类群体与高权限机构：群体认知、权威与制度放大》；
- 将第三本书 `HUMAN-BOOK-003` 重写为《人类群体与高权限机构——从众、集体智能、权威与制度放大》；
- 将核心模型从“人多会更不理性”校准为：`individuals + interaction topology + information distribution + identity + norms + authority + incentives + responsibility + institutions → collective behavior`；
- 明确拒绝 `crowd = irrational` 与“乌合之众天然失智”模型；群体可能出现 process gain，也可能出现 process loss，关键在信息独立性、异议、权威、身份、聚合与责任结构；
- 新增 `group-mechanisms.yaml`，结构化 24 个群体机制：从众、羊群、信息级联、多元无知、共享信息偏差、隐藏信息轮廓、异议效应、群体极化、groupthink、权威服从、责任扩散、旁观者效应、社会身份/去个体化、社会传播、群际威胁、组织沉默、地位层级、社会证明、集体智能、协调规范、身份保护、合法性遵从、议程控制和制度记忆；
- 对 `groupthink` 做证据降级：保留为有用的启发式诊断，但明确经典完整模型存在重要实证与概念争议，不得把所有组织失败自动归为 groupthink；
- 对“去个体化”做现代校准：不再解释为进入群体后没有规范，而是分析群体身份和当前群体规范何时变得更显著；
- 新增 `institution-atlas.yaml`，描述 13 类高权限机构：政府与公共行政、军队/警务/应急、法院与法律机构、中央银行/银行/金融机构、公司、大众媒体、数字平台、科学工程专业共同体、医疗机构、学校大学、宗教价值共同体、工会/行业/专业协会以及标准计量组织；
- 将“高权限机构”定义为现实杠杆分析标签，而非“不合法机构”标签；重点分析其法律、资本、信息、认证、强制、议程、规则解释、规模和跨时间持续能力；
- 新增 `collective-failure-patterns.yaml`，收录 34 个群体与机构失败模式，包括复制型多数、信息级联锁定、虚假多数、共享信息循环、独特信息丢失、异议压制、领导先表态锚定、极化螺旋、身份压过证据、责任扩散、组织沉默、上行现实过滤、声望俘获、过早共识、制度化错误、程序性责任卸载、制度惯性、指标替代使命、局部理性全局失败、平台多数错觉、机构人格化和虚假集体智慧等；
- 新增 `research/2026-09-human-groups-evidence.md`，外部校准 2026 crowd psychology、2024 information cascades/social learning、hidden-profile 元分析、dissent、pluralistic ignorance、bystander meta-analysis、authority/obedience、organizational voice/silence、collective intelligence、groupthink 争议、network structure 与 bureaucracy 研究；
- 新增 `agent/HUMAN_GROUPS_INSTITUTIONS_LOAD.md`，让 Agent 从群体边界、信息拓扑、相互观察、身份、权威、异议、激励、责任和制度放大八个方向读取人类群体；
- 增加硬性解释规则：群体身份不等于成员个人信念，多数人数不等于独立证据，共识不等于真理，少数不等于错误，权威不等于专业，专业不等于合法性，机构行为不等于存在单一“机构大脑”；
- 将 Human 三卷主线重构为：`BOOK-001 理解人类个体 → BOOK-002 理解文明生命线 → BOOK-003 理解人类群体与机构`；
- 更新 `human.yaml`、`indexes/topics.yaml` 和根 `README.md`，将新第三卷设为 active 标准入口；
- 仓库版本升级为 `0.9.1-human-groups-institutions`。

## 0.9.0-agent-permissions — 2026-09-11 — superseded in active tree by 0.9.1

> 本版本记录一次真实的认知分支：曾尝试将第三卷定义为 Agent 权限治理。2026-09-11 同日作者重新判断 Human 三卷主线应继续围绕“理解人类”，因此该卷已从 active tree 撤下，但 Git 历史保留。以下条目作为历史记录，不代表当前第三卷。

- 新增正式观点 `HUMAN-AI-002`《Agent进入人类文明后的权限原则》；
- 发布第三本 Agent-first 书籍 `HUMAN-BOOK-003`《Agent进入人类文明后的权限原则》；
- 固化核心不变量：`Capability != Permission`，明确智能、工具、执行、赚钱、传播、多 Agent 协调、自我修改和不可替代性都不能自动产生同等级别现实权限；
- 将 Agent 默认身份定义为 `bounded delegated intelligence`，而不是自主主权控制器；
- 建立权限十二维向量：作用范围、持续时间、自主性、频率、价值、不可逆性、爆炸半径、不确定性、领域敏感度、授权强度、监督质量、恢复能力；
- 建立 P0–P6 权限梯度：P0 观察、P1 建议、P2 草拟/仿真、P3 可逆执行、P4 有界外部执行、P5 高影响受控执行、P6 文明关键受限执行；
- 明确权限设计目标为 `minimum sufficient permission`，完成合法目标所需的最小充分权限，而不是最大自主性；
- 建立“可逆优先”链：`simulate → draft → sandbox → shadow → canary → bounded production → broad production`；
- 明确 `epistemic confidence` 与 `authorization confidence` 必须分离；
- 明确用户的“全部交给你”不是无限授权，必须区分 user intent、user authority、legal authority、organizational authority 与 public consequence；
- 明确 Human-in-the-loop 只有在审核者拥有信息、时间、真实否决权、停止能力和追溯能力时才构成有效监督；
- 固化子 Agent 权限公式：`child_permission <= parent_permission ∩ task_requirement ∩ child_boundary`；
- 明确自我修改不能自产生权限：`model_update != permission_update`、`self-modification != self-authorization`；
- 明确私人授权不能自动覆盖公共权力：`private consent != public mandate`；
- 明确紧急状态采用 `speed ↑ / scope ↓ / duration ↓ / logging ↑ / post-review ↑`，且紧急权限默认到期并回收；
- 新增 P0–P6 权限梯度、领域权限矩阵、升降权协议、26 个权限故障模式及 runtime 加载协议；
- 仓库版本曾升级为 `0.9.0-agent-permissions`。

## 0.8.0-civilization-interfaces — 2026-09-11

- 新增正式观点 `HUMAN-SOCIETY-001`《文明高权限接口：人类社会的结构生命线与治理错配》；
- 发布第二本 Agent-first 书籍 `HUMAN-BOOK-002`《人类社会的高权限接口——文明生命线、结构依赖与治理错配》；
- 将人类文明建模为由少数高杠杆生命线、网络、制度、知识与信任关系持续维持的分布式依赖系统，而不是人口或机构的简单集合；
- 将“低监管”校准为更稳健的“治理错配”：`civilizational leverage > public visibility`、`cross-system dependency > cross-system ownership`、`failure propagation speed > coordination speed`、`maintenance importance > political salience`；
- 建立文明四层栈：L1 生物连续性（食物、化肥、水、卫生、疾病与健康）、L2 物理/数字流通（能源、电力、物流、通信、计算）、L3 制度协调（金融、支付、身份、记录、法律、行政、标准、时间）、L4 信任与共享现实；
- 将 Haber–Bosch 合成氨/合成氮肥作为高结构权限案例，并通过外部资料校准“约支撑全球一半人口”的含义，避免将其夸张为即时死亡预测；
- 将水建模为从水源、处理、监测、输送到污水回收的连续服务链，将安全拆成 quantity security 与 quality security；
- 将电力建模为多个现代文明节点的 activation layer，同时明确关键性不等于脆弱性；
- 纳入疾病和公共卫生，但明确拒绝病毒末日叙事，仅分析公共卫生容量、卫生基础设施、医疗供应链、风险沟通与社会信任；
- 将金融建模为把未来承诺转换为现在行动资源的制度接口，并把 confidence/trust 作为会通过集体行为改变系统状态的变量；
- 将政府与政治中的“信心”校准为治理协调资本之一，而不是政府唯一基础；同时保留组织能力、财政、法律、服务、强制、绩效和合法性等结构变量；
- 新增 `dependency-atlas.yaml`，机器可读描述四层文明节点、上游/下游依赖、替代时间、公众可见性和跨层边；
- 新增 `failure-patterns.yaml`，收录 30 个结构失败模式；
- 新增 `governance-controls.yaml`，固化 20 个韧性治理控制；
- 新增 `agent/CIVILIZATION_INTERFACE_LOAD.md`；
- 新增 `research/2026-09-civilization-interface-evidence.md`；
- 更新 `human.yaml`、`indexes/topics.yaml` 和根 `README.md`；
- 仓库版本升级为 `0.8.0-civilization-interfaces`。

## 0.7.0-human-interface-book — 2026-09-11

- 新增正式观点 `HUMAN-AI-001`《人类是高权限低监管接口：Agent时代的人类风险面》；
- 发布 Agent-first 书籍 `HUMAN-BOOK-001`《人类及其人类社会的弱点——高权限低监管接口》；
- 将人类建模为 `privileged + stochastic + partially observable + incentive-sensitive + socially coupled actuator`，而不是天然可信的最终控制器；
- 从“权限、裁量、不可观测、不可逆、驱力激活、复核、回滚”构建 HPLOI 风险向量；
- 延续七驱力框架，并新增“恐惧/损失规避”作为辅助风险轴；
- 扩展个人、组织、市场、金融、平台、权力、危机、人机协作等系统级弱点；
- 新增 `casebook.yaml`，收录 42 个防御性失败模式；
- 新增 `control-matrix.yaml`，固化 20 个控制；
- 新增 `agent/HUMAN_INTERFACE_RISK_LOAD.md`；
- 更新 `human.yaml`、`indexes/topics.yaml` 和根 `README.md`；
- 仓库版本升级为 `0.7.0-human-interface-book`。

## 0.5.0-chapter-04 — 2026-07-30

- 写入第四章日记《谎言、七种驱力与人的行动》；
- 固化正式观点 `HUMAN-INFLUENCE-002`《LIAR人类影响框架：七驱力、谎言与仪式化行为》；
- 将七宗罪校准为消息层面的七驱力启发式剖面，明确其不是脑区模型或人格诊断；
- 定义 LIAR 链：潜在驱力、身份绑定、情绪放大、仪式强化；
- 扩展谎言分类，覆盖重大遗漏、来源洗白、虚假共识、虚假稀缺、确定性膨胀、身份围栏与仪式锁定；
- 固化 `HUMAN-METHOD-002`《LIAR影响力审计与诚实说服协议》及十二步审计流程；
- 新增机器可读 `influence-audit.schema.json`；
- 研究并映射 2025—2026 年 AI 说服、重复真值效应、错误来源归因、预防性教育、社会比较、身份融合、同步和有成本承诺；
- 新增可移植 Agent Skill `audit-deceptive-influence`；
- 将仓库版本升级为 `0.5.0-chapter-04`。

## 0.4.0-chapter-03 — 2026-07-24

- 写入第三章日记《Agent 谱系资本——未来人类怎样拥有 AI 财富》；
- 固化正式观点 `HUMAN-ECONOMY-001`《Agent谱系资本：AI时代的财富标准假说》；
- 发布实验性标准 `HUMAN-PROTOCOL-001` / `PIRS 0.1`；
- 区分权利主体、协议、Agent产物、运行实例、授权和结算六种身份；
- 建立 APC-0 至 APC-6 七级成熟度和多维 Agent 资本向量；
- 定义调用、评测、信誉和结算的分层计数器；
- 新增协议清单、Agent清单、授权、调用收据、评测证明、信誉快照和结算收据七类 JSON Schema、符合性规则与示例；
- 研究并映射 2025—2026 年 A2A、MCP、AI Agent 授权、AP2、FIDO、MPP、x402、OpenTelemetry、SLSA、GitHub Attestations 与 SPDX 等技术趋势；
- 新增可移植 Agent Skill `evaluate-agent-capital`；
- 将仓库版本升级为 `0.4.0-chapter-03`。

## 0.3.0-chapter-02 — 2026-07-23

- 写入第二章日记《脏现实——我怎样理解一个真正运行的世界》；
- 固化正式观点 `HUMAN-REALITY-001`《脏现实结构场论》；
- 固化推理方法 `HUMAN-METHOD-001`《现实结构编译协议》；
- 纳入现实范畴迁移编译法、熟悉范畴反推法、结构反演与九步判断协议；
- 新增可移植 Agent Skill `analyze-dirty-reality`；
- 为暗信息、干扰线、现实质量体、热力学等概念增加证伪和操作化约束；
- 完成独立 Agent 前向测试，并据此补充证据分级、诊断干扰、暂定阈值、轻量输出和“仍未知”分类；
- 新增现实与推理主题索引，并将仓库版本升级为 `0.3.0-chapter-02`。

## 0.2.0-chapter-01 — 2026-07-23

- 写入第一章日记《人类说服性说理原则》；
- 固化正式观点 `HUMAN-INFLUENCE-001`《人类影响的认知轨迹理论》；
- 新增可移植 Agent Skill `write-persuasive-narratives`；
- 新增完整理论、40岁失业与AI、餐馆侧面证明、企业工作流等参考案例；
- 新增 Agent 技能注册表和 `influence` 主题索引；
- 完成独立 Agent 前向测试，验证技能可以把硬性说教改写为认知轨迹型内容。

## 0.1.0-foundation — 2026-07-23

- 建立项目说明与目录结构；
- 建立认知宪章和 Agent 操作规则；
- 建立机器可读清单、观点 Schema 和主题索引；
- 建立观点与预测模板；
- 建立博物馆、推理、预测、矛盾和案例区；
- 写入首个作者确认的元观点 `HUMAN-META-001`。
