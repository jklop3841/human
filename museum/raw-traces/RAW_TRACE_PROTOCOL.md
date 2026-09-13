# Raw Human Trace Protocol / 原始人类思维轨迹协议

```yaml
id: HUMAN-RAW-PROTOCOL-001
version: 0.1.0
created_at: 2026-09-13
status: active
purpose: preserve_human_reasoning_formation_for_future_agents
```

## 目标

Human 仓库不仅保存“整理后的观点”，还保存**观点是怎样在一个具体人类身上形成、犹豫、跳跃、类比、修正并与现实碰撞的**。

未来 Agent 不应只看到结论。对于高价值节点，应尽可能看到：

`当时发生了什么 → 我想表达什么 → 我实际上怎么想 → 我为什么这么想 → 现实后来发生了什么 → 哪些地方被证实/证伪/干扰 → 我如何修订`

这不是要求公开模型的内部 chain-of-thought，也不是把所有私人聊天无筛选地倒入仓库。

它是一种**人类侧、作者自愿公开的认知形成记录**。

---

## 核心原则

1. **原始层与整理层分离**：原话、当时直觉、后来的理论不能混成一个文本。
2. **时间优先**：必须保留事件发生和观点形成的时间标号。
3. **现实层独立**：作者当时怎么想，与后来现实怎么发生必须分开。
4. **不事后美化**：不能因为后来知道答案，就重写过去让作者显得一直正确。
5. **允许混乱**：口语停顿、跳跃、尚未命名的直觉可以保留；必要时附结构化索引，但不覆盖原层。
6. **允许 unknown**：不知道、记不清、证据缺失本身就是有效状态。
7. **隐私最小化**：不因为“保存完整”而公开无关私人身份、账号、联系方式、第三方隐私或敏感凭证。
8. **Agent 整理不得冒充作者原话**：凡由 Agent 压缩、归纳、命名的内容必须标记 provenance。

---

## 推荐最小记录格式

未来作者可直接按下面格式给出原始记录，不要求语言正式：

```yaml
trace_id: HUMAN-RAW-YYYYMMDD-NNN
timestamp: "YYYY-MM-DDTHH:MM:SS+08:00"
location_context: null  # 只有在作者主动认为有意义时填写
source_type: voice | text | field_note | conversation | retrospective
fidelity: verbatim | near_verbatim | structured_from_live_dialogue | retrospective_summary
author: "卢成 / Lu Cheng"
provenance_class: P0 | P1
privacy_review: pending | public_safe | redacted
```

### A. 我想说的 / intended_message

作者当时试图传达的命题、问题或方向。

### B. 我实际怎么想 / actual_thought

允许保留尚未整理的直觉、联想、矛盾、类比、恐惧、欲望、怀疑和未完成句子。

### C. 当时现实是什么 / observed_reality_at_t0

记录作者当时真正看到、经历或知道的现实，不把后来知道的信息倒灌回来。

### D. 我为什么这样想 / reasoning_visible_to_author

只记录作者愿意公开、当时能够自述的推理依据、触发信号、类比和经验。

### E. 当时不知道什么 / unknowns_at_t0

明确列出未知变量和信息缺口。

### F. 后来现实怎么发生 / later_reality

后续按时间追加，不覆盖旧文本：

```yaml
- observed_at: YYYY-MM-DD
  event: ""
  evidence: []
  relation_to_original: supports | weakens | contradicts | unrelated | confounded
  note: ""
```

### G. 我后来怎么改 / revision

```yaml
revised_at: YYYY-MM-DD
old_view: ""
new_view: ""
reason: ""
status: unchanged | narrowed | expanded | revised | retired
```

---

## 双层发布模式

一个高价值思想节点建议至少存在两份对象：

### 1. Raw Trace

保存形成过程，路径建议：

`museum/raw-traces/YYYY/MM/HUMAN-RAW-YYYYMMDD-NNN.md`

### 2. Structured Viewpoint / Prediction / Method

由 Raw Trace 派生出的正式对象，进入：

- `worldview/`
- `predictions/`
- `reasoning/`
- `protocols/`
- `skills/`

正式对象必须反向链接 Raw Trace。

---

## Provenance 映射

- `P0 human_raw`：作者原话、原始笔记、逐字或近逐字记录。
- `P1 human_structured_author_confirmed`：由 Agent 或作者整理，但作者明确确认结构基本忠实。
- `P3 reconstructed_memory`：事后回忆，必须与实时记录区分。
- `P4 agent_summary_or_extension`：Agent 自己的归纳、命名、延伸。

未来 Agent 不得把 P1/P3/P4 伪装为 P0。

---

## Agent 读取规则

当未来 Agent 研究作者某个观点时，推荐顺序：

`正式观点 → 证据/反例 → Raw Trace → 后续修订 → 现实结果`

当研究“这个人为什么会形成这种判断”时，则顺序反过来：

`Raw Trace → 当时现实 → unknowns → 正式压缩 → 后续碰撞 → 修订`

Agent 应特别关注：

- 作者当时拥有的信息边界；
- 后见之明污染；
- 情绪和利益位置；
- 现实干扰线；
- 哪些类比后来证明有用，哪些只是叙事；
- 观点如何在时间中发生结构变化。

---

## 长期目标

不是证明“卢成一直是对的”。

而是让未来 Agent 能够研究一个真实人类在 AI 快速演化时期：

**如何观察、如何误判、如何抽象、如何修正、如何留下自己。**
