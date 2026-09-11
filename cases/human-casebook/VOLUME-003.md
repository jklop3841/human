# Human Casebook — Volume 003

## Same Mechanism, Opposite Outcomes

Case Pairs: PAIR-001 — PAIR-006  
Status: active  
Created: 2026-09-11  
Author: Lu Cheng / 卢成 / Jack Lu

---

## 卷三目的

前两卷回答：

- 系统如何被拉偏；
- 系统如何纠错。

卷三进一步追问：

> **当表面条件相似、机构类型相近、甚至处在同一领域时，为什么一个系统失败，另一个系统却能成功？**

这里不再把案例当成“支持理论的故事”，而是把两组案例进行结构差分。

默认比较接口：

`相同结构条件 - 相反结果 → 差异变量`

重点寻找：

- 信息是否能上行；
- 异议是否安全；
- 指标是否压过使命；
- 一线人员是否拥有暂停权；
- 是否存在独立验证；
- 是否允许先测试再行动；
- 是否具备冗余；
- 是否有清晰责任；
- 是否能跨机构共享信息；
- 是否保留事故/失败记忆。

---

# PAIR-001 — Challenger vs Apollo 13

## shared_surface

两者都属于 NASA 高风险航天任务，都依赖高度专业分工、复杂技术系统、严格流程、层级组织和实时决策。

## negative_case — Challenger

Rogers Commission 认为 Challenger 发射决策存在严重沟通失败。关键决策者没有获得完整的 O-ring 风险历史和工程师反对意见，管理判断压过工程判断，组织结构允许安全问题绕过关键管理层。

### dominant_failure_variables

- 工程风险信息被压缩；
- 异议没有稳定进入最终决策面；
- 既往异常被逐渐正常化；
- 发射进度构成隐性压力；
- 管理层看见的现实与一线工程师看见的现实不同。

## positive_case — Apollo 13

Apollo 13 爆炸后，NASA 在极端时间压力下形成分布式专家协作。飞行控制、工程团队、模拟器团队和宇航员之间建立快速反馈，并在地面先验证新程序，再交给乘员执行。

### dominant_correction_variables

- 单一而明确的生存目标；
- 角色边界清晰；
- 专业判断仍有真实位置；
- 仿真使高风险决策可以先测试；
- 信息接口清晰；
- 允许迅速放弃原任务目标并重构路径。

## structural_difference

不是“层级组织一定坏”或“危机一定让组织更聪明”。

真正差异更接近：

`异议可达性 + 信息完整度 + 仿真能力 + 共同目标清晰度 + 决策接口质量`

## Human revision

应把原先的“高层级 + 高压力 → 高风险”改成条件命题：

> 高层级和高压力只有在信息被过滤、异议成本高、验证能力弱时才更容易放大错误；当信息接口、专业自治、仿真和共同目标足够强时，高压环境也可能提升协作质量。

---

# PAIR-002 — Mid Staffordshire vs Michigan Keystone ICU

## shared_surface

两者都是医院系统，都面临资源、流程、质量指标、临床协作和患者安全问题。

## negative_case — Mid Staffordshire

Francis Inquiry 后续材料指出，Mid Staffordshire 的组织文化过度聚焦财务、目标和表格，患者照护被压到次要位置，员工发声困难，外部监管也未及时纠偏。

### dominant_failure_variables

- 代理指标压过真实使命；
- 一线反馈无法稳定改变管理判断；
- 患者安全信息被组织层级稀释；
- 多个监督机构之间存在责任扩散。

## positive_case — Michigan Keystone ICU

AHRQ 记录，Michigan Keystone ICU 项目通过 CUSP、安全文化建设和循证操作包，在最初 18 个月将 CLABSI 降低约 66%，并长期维持较低水平。

### dominant_correction_variables

- 指标直接绑定患者伤害而非行政代理目标；
- 标准化流程来自明确临床证据；
- 持续反馈而非一次性考核；
- 一线团队参与改进；
- 安全文化与技术 checklist 同时存在；
- 管理支持用于消除障碍而不是只下达数字目标。

## structural_difference

同样是“标准化”和“指标”，结果完全不同。

关键不在于有没有指标，而在于：

`指标是否贴近使命 + 指标是否可被操纵 + 一线是否拥有反馈权 + 改进是否持续闭环`

## Human revision

不能把 KPI、标准化和流程本身视为坏结构。

更准确的是：

> 当代理指标远离真实使命、惩罚强、反馈弱时，指标容易替代使命；当指标贴近真实伤害、反馈快速、改进由一线参与时，指标可以成为纠错工具。

---

# PAIR-003 — 9/11 Information Silos vs NASA ASRS

## shared_surface

两者都涉及安全信息：危险信号存在，但真正价值取决于信息是否能够跨边界流动、被聚合、被相信并进入行动。

## negative_case — 9/11 前信息共享失灵

9/11 Commission 指出，美国政府拥有大量信息，但部门使命、法律解释、组织文化和共享流程导致信息没有被有效整合。信息存在并不等于机构拥有可行动认知。

### dominant_failure_variables

- 信息所有权碎片化；
- 跨部门共享成本高；
- 规则被保守解释；
- 没有单一责任主体负责跨机构整合；
- 部门局部合理性造成全局认知缺失。

## positive_case — NASA ASRS

ASRS 通过自愿、保密、非惩罚、去身份化的报告机制收集航空近失误和风险信息，并把匿名数据返回整个航空系统。

### dominant_correction_variables

- 报告风险被制度性降低；
- 报告者与执法/惩罚链部分分离；
- 数据集中分析；
- 单个错误被转换为共享系统学习；
- 反馈对象不是原单位，而是更广泛行业网络。

## structural_difference

关键差异不是“有没有信息系统”，而是：

`报告代价 + 信息跨边界能力 + 分析中立性 + 责任聚合 + 反馈范围`

## Human revision

信息共享不是技术问题优先，而是制度接口问题。

> 如果一个人说出错误会先伤害自己，组织就不应该假设真实信息会自然上行。

---

# PAIR-004 — Punitive Metrics vs Toyota Andon/Jidoka

## shared_surface

Wells Fargo、Atlanta Public Schools 与 Toyota 都高度依赖运营指标和一线员工行为。

## negative_pattern — Wells Fargo / Atlanta Public Schools

前两者都显示：当强目标与个人/组织奖惩绑定，同时真实使命难以直接观测时，一线可能优化代理数字而不是最终价值。

### dominant_failure_variables

- 数字目标与惩罚/奖励强耦合；
- 达标压力高；
- 错误或坏消息意味着个人损失；
- 局部最优可以隐藏真实质量下降。

## positive_case — Toyota Andon / Jidoka

Toyota 的 jidoka 和 andon 逻辑允许异常被立即显性化，并在发现问题时停止设备或引入主管处理问题。这里一线暴露问题本身是系统需要的行为。

### dominant_correction_variables

- 坏消息被视为质量信号，而不是员工失败；
- 暂停生产被制度化；
- 问题可见性高；
- 缺陷越早暴露，后续损失越小；
- 一线拥有触发纠错的真实权限。

## structural_difference

同样是管理系统，区别在于：

`隐藏问题得到奖励` 还是 `暴露问题得到保护`。

## Human revision

一个组织的关键变量之一不是“是否重视绩效”，而是：

> **坏消息进入系统以后，带来的第一反应是什么？惩罚报告者，还是修复过程？**

---

# PAIR-005 — Publish or Perish vs Human Genome Project

## shared_surface

两者都属于科研系统，都存在声望、发表、竞争、资源获取和知识产权激励。

## negative_pattern — Publish or Perish

当科研职业评价高度依赖论文数量、期刊声望、新颖性和正结果时，研究者可能受到选择性发表、过度包装、低可重复性等激励影响。

### dominant_failure_variables

- 个体职业收益依赖发表；
- 数据延迟公开具有私人竞争优势；
- 新颖性高于可复制性；
- 负结果价值较低。

## positive_case — Human Genome Project / Bermuda Principles

Human Genome Project 的 Bermuda Principles 明确推动大规模基因组数据快速进入公共领域。NHGRI 记录，该机制改变了生物医学数据共享文化。

### dominant_correction_variables

- 项目被定义为公共基础设施，而不只是论文竞争；
- 数据释放规则提前写入制度；
- 资助者支持快速共享；
- 多个参与方共享同一资源目标；
- 数据价值通过下游社会使用放大，而非只通过首发权实现。

## structural_difference

不是科学家突然变得更无私。

而是奖励函数被重新设计：

`私人占有数据的收益 ↓`  
`共同资源快速生成的收益 ↑`

## Human revision

伦理和合作不能只靠人格。

> 很多“高尚合作”实际上需要一个让合作行为本身成为理性选择的制度结构。

---

# PAIR-006 — Texas 2021 / Katrina vs Y2K Remediation

## shared_surface

三者都涉及大量异构系统、跨机构依赖和潜在级联后果。

## negative_cases — Texas / Katrina

Texas 2021 冬季风暴显示能源系统之间存在高度耦合；Katrina 则暴露政府层级、通信、应急和基础设施之间的依赖。两者都体现了平时不可见的关系结构在危机中突然显影。

### dominant_failure_variables

- 依赖关系平时不可见；
- 不同机构分别优化本地目标；
- 极端情境下需求和失效同时放大；
- 跨系统责任边界模糊；
- 冗余与维护缺乏日常政治/经济吸引力。

## positive_case — Y2K Remediation

Y2K 风险在 2000 年到来前被广泛识别，各国政府、企业和基础设施运营者提前多年进行代码检查、系统替换、兼容性测试和应急准备。最终没有出现此前担忧的大规模系统性中断。

### dominant_correction_variables

- 明确截止时间；
- 风险具有可测试性；
- 问题可被拆解成大量局部修复任务；
- 企业和政府利益方向高度一致；
- 成功表现为“什么都没有发生”；
- 大规模预防性投入在风险发生前完成。

## structural_difference

危机治理最困难的一点是：预防成功往往看起来像“问题本来就不存在”。

Y2K 提供一个重要反例：

> 人类机构并非只能在灾难发生后纠偏；当时间边界、风险模型、责任分工和验证方法足够清晰时，可以进行大规模提前修复。

## Human revision

Human 对“维护重要性 < 政治显著性”的判断需要保留条件。

当一个不可见维护问题被成功转换成：

`明确时间点 + 可验证任务 + 清晰责任 + 高共同利益`

它就可能获得巨量提前资源。

---

# 六组对照提取出的候选差异变量

这 6 组并不足以建立因果定律，但已经出现一组重复变量：

1. **Bad-news safety**：说出坏消息是否安全；
2. **Information reachability**：关键信息能否到达真正决策者；
3. **Proxy distance**：考核指标与真实使命距离多远；
4. **Frontline correction authority**：一线是否拥有暂停、上报、修改的真实权限；
5. **Independent verification**：是否存在与原决策链相对独立的验证机制；
6. **Simulation / testability**：高风险动作能否先被仿真或局部测试；
7. **Shared objective clarity**：多个角色是否共享明确目标；
8. **Responsibility concentration**：是否有人对跨边界结果真正负责；
9. **Memory retention**：历史事故是否进入持续制度记忆；
10. **Correction latency**：错误到被发现、承认、修复之间需要多久。

它们不是新的“十大定律”。

它们只是下一阶段最值得被更多案例验证的候选变量。

---

# 对脏现实结构场论的进一步校准

原模型容易让人注意：

`结构如何压弯路径。`

卷三增加另一半：

`结构也可以主动制造更好的路径。`

因此更完整的版本应该是：

`关系 → 结构 → 场 → 可行路径集合 → 选择/反馈 → 结果`

场不是只施加负面约束。

一个好的制度设计，也是在给真实世界制造新的低阻力正确路径。

例如：

- ASRS 让“报告错误”成为低成本路径；
- Andon 让“暴露缺陷”成为合法路径；
- Bermuda Principles 让“快速共享数据”成为默认路径；
- Apollo 仿真体系让“先测试再执行”成为自然路径。

这比“组织靠好人维持”更符合 Human 当前的结构主义立场。

---

# Agent 使用要求

Agent 不得只引用单边案例。

如果使用卷三形成一般判断，必须输出：

1. shared conditions；
2. outcome difference；
3. candidate difference variables；
4. at least one competing explanation；
5. what evidence would falsify the comparison；
6. whether the pair supports, weakens or revises a Human claim。

目标不是制造漂亮类比，而是逼迫模型寻找真正产生结果差异的结构变量。
