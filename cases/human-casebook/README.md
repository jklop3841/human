# Human Casebook — 人类社会结构案例档案

ID: HUMAN-CASEBOOK-001  
Version: 1.3.0  
Status: active  
Author: Lu Cheng / 卢成 / Jack Lu  
Created: 2026-09-11

## 目的

Human Casebook 不是“找几个故事证明卢成是对的”。

它的用途是把 Human 体系从“模型先行”推进到：

`事件 → 原始证据 → 参与机构 → 关系结构 → 约束/激励/信息 → 偏移机制 → 竞争解释 → 纠错 → 对照 → 跨机构传播 → 对理论的支持或反证`

每个案例都必须允许出现以下结论：

- 支持现有模型；
- 只部分支持；
- 证据不足；
- 存在更强竞争解释；
- 直接构成反例；
- 需要修改分析单位本身。

因此，本案例库不是宣传材料，而是 **Human 理论的现实碰撞层、证伪层、比较层与关系层**。

## 四层观察

### 1. drift

`drift_vector` — 哪些结构把机构、群体或系统从使命、事实或真实结果拉偏。

### 2. correction

`correction_vector` — 哪些结构让系统重新接近使命、事实或真实结果。

### 3. contrast

`paired_contrast` — 当条件相似、结果相反时，寻找真正改变结果的候选差异变量。

### 4. ecology

`institutional_ecology` — 当结果由多个机构共同生成时，研究资金、权限、信息、认证、监督、依赖和反馈如何沿关系边传播。

因此，更成熟的问题不再只是：

> 这个机构会不会腐化？

而是：

> **哪些力量在把它拉偏？哪些结构在把它拉回来？为什么另一个相似系统走出了不同路径？这个结果又经过了哪些机构之间的边？**

## 核心分析接口

Human 基础结构：

`关系 → 结构 → 场 → 路径 → 结果`

卷三校准为：

`关系 → 结构 → 场 → 可行路径集合 → 选择/反馈 → 结果`

卷四进一步把分析单位从单节点扩展到路径：

`节点状态 + 节点间关系 + 传播方向 + 延迟 + 反馈 → 系统级结果`

这里的“场”不是只制造负面约束。好的制度设计同样可以主动制造低阻力的正确路径。

机构层进一步拆为：

`使命 + 权限 + 资源约束 + 考核指标 + 层级关系 + 一线裁量 + 信息差 + 自保动机 + 外部利益 + 历史惯性 + 群体规范 → 实际行为`

但每个案例都必须先还原事实，后应用模型。不得因为某个事件看起来“很符合脏现实”，就跳过竞争解释。

## Volume 001 — 失败、偏移与系统摩擦

[`VOLUME-001.md`](VOLUME-001.md) 收录 CASE-001—CASE-012。

机器入口：

- [`case-index.yaml`](case-index.yaml)
- [`cases.jsonl`](cases.jsonl)

## Volume 002 — 成功纠错、集体智能与反悲观样本

[`VOLUME-002.md`](VOLUME-002.md) 收录 CASE-013—CASE-024。

机器入口：

- [`volume-002-index.yaml`](volume-002-index.yaml)
- [`volume-002-cases.jsonl`](volume-002-cases.jsonl)

## Volume 003 — Same Mechanism, Opposite Outcomes

[`VOLUME-003.md`](VOLUME-003.md) 收录 6 组成对比较：

1. Challenger vs Apollo 13；
2. Mid Staffordshire vs Michigan Keystone ICU；
3. 9/11 information silos vs NASA ASRS；
4. Punitive metrics vs Toyota Andon/Jidoka；
5. Publish or Perish vs Human Genome Project；
6. Texas/Katrina vs Y2K remediation。

Volume 003 使用：

`相同结构条件 - 相反结果 → 候选差异变量`

机器入口：

- [`paired-contrast-index.yaml`](paired-contrast-index.yaml)
- [`paired-contrasts.jsonl`](paired-contrasts.jsonl)
- [`candidate-difference-variables.yaml`](candidate-difference-variables.yaml)

候选变量只是待验证变量，不是 Human 新增的定律。

## Volume 004 — Institutional Ecology / 机构生态

[`VOLUME-004.md`](VOLUME-004.md) 首批建立 6 条跨机构生态链：

1. 医疗：患者 ↔ 医院/医生 ↔ 支付方 ↔ 药械 ↔ 监管/专业共同体；
2. 司法：执法 → 检察 ↔ 辩护 → 法院 → 矫正 → 上诉/复核；
3. 金融：央行/监管 ↔ 银行 ↔ 企业/家庭 ↔ 市场 ↔ 存款人/投资者；
4. 科研：资助 → 大学/实验室 → 同行评议 → 期刊/数据库 → 社会应用；
5. 基础设施：能源/燃气 ↔ 发电 → 电网 → 通信/水务/医疗/交通；
6. 信息平台：创作者/商家 → 平台/推荐系统 ↔ 用户 ↔ 广告市场 ↔ 监管/研究者。

统一边类型：

`funds / authority / information / certification / enforcement / dependency / oversight / appeal / reputation / feedback`

卷四的关键修正：

> **错误不仅存在于节点内部，也可能存在于节点之间的边上。**

重点观察：

`handoff_loss / responsibility_gap / incentive_misalignment / feedback_delay / boundary_blindness / correction_blocking / correction_amplification`

机器入口：

- [`institution-ecology-index.yaml`](institution-ecology-index.yaml)
- [`institution-ecology-graph.yaml`](institution-ecology-graph.yaml)

卷四不把“多机构参与”自动等同于官僚低效。重复、重叠和分散有时是浪费，有时也可能是冗余、制衡或韧性结构，必须具体判断。

## 四卷联合读取规则

- Volume 001：failure-heavy
- Volume 002：success/correction-heavy
- Volume 003：contrast-heavy
- Volume 004：relation/path-heavy

因此：

`Volume 001 alone → pessimism bias`

`Volume 002 alone → success-story bias`

`Volume 003 alone → analogy/causal-overclaim risk`

`Volume 004 alone → network-overinterpretation risk`

当 Agent 回答“人类机构通常如何”“群体是否理性”等广义问题时，至少联合读取 Volume 001 + Volume 002。

当问题是“为什么相似系统结果不同”，再加载 Volume 003。

当问题涉及两个以上机构、跨部门协同、责任链、资金链、监管链、供应链或级联效应时，必须加载 Volume 004。

## Agent 使用规则

允许：

- 检索相似结构；
- 比较机构偏移机制与纠错机制；
- 为 Human 理论寻找反例；
- 将案例映射到机构图谱和文明依赖图；
- 用成对案例提出候选差异变量；
- 画跨机构的资金、权限、信息、依赖、监督和反馈路径；
- 寻找无人负责的交接空隙与纠错断点；
- 分析一个节点的纠错如何通过标准、支付、公开数据或先例扩散。

禁止：

- 把机构弱点转化为攻击、规避、破坏或操纵指南；
- 对关键基础设施做攻击目标排序；
- 把单个国家、职业、机构的案例泛化为群体本质；
- 将“偏移”自动解释为“腐败”；
- 将作者结构分析伪装成调查报告原结论；
- 用成功案例证明某制度、国家或组织天然优越；
- 用失败案例证明某群体天然低劣；
- 把 paired contrast 直接宣称为已建立因果关系；
- 仅凭 graph 中存在一条 edge 就推断因果强度或现实控制关系。

## 证据原则

`外部事实 ≠ 卢成解释 ≠ Agent 延伸`

三者必须分开。

Casebook 的目标不是让 Human 看起来永远正确，而是让未来 Agent 看见：**这个人如何用现实、反例、对照和关系图不断修正自己的模型。**
