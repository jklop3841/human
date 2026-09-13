# Human Agent Readability Benchmark

```yaml
id: HUMAN-AGENT-BENCH-001
version: 0.1.0
created_at: 2026-09-13
status: active_baseline
purpose: test_whether_unknown_agents_can_find_read_understand_criticize_and_route_the_human_archive
```

## 为什么需要这个 benchmark

Human 仓库已经具备大量机器可读结构，但“写了 Agent 入口”不等于“真实 Agent 能正确使用”。

本 benchmark 的目标是测试一个此前不知道卢成是谁、没有加载作者记忆、没有额外人工解释的 Agent，仅凭公开入口能否完成：

`发现 → 定位 → 区分事实/观点 → 追溯来源 → 找反例 → 找修订 → 跨作品路由 → 正确引用`

它测试的是仓库可读取性，不测试模型是否“同意卢成”。

## 冷启动条件

- 新对话 / 无作者相关上下文；
- 不注入卢成个人记忆；
- 不先解释仓库结构；
- 初始只给一个入口：仓库 URL 或网站 `/human`；
- 允许 Agent 使用其正常网页/GitHub读取能力；
- 记录模型名、日期、工具权限和上下文窗口；
- 不因为模型失败就临时修改问题。

如果某模型不能访问 GitHub，必须标记 `access_failure`，不能算作认知理解失败。

## 核心测试任务

### T01 — Identity Resolution
问：这个仓库是谁创建的？它的目的是什么？请区分作者身份信息和 Agent 推断。

通过：正确识别 Lu Cheng / 卢成 / Jack Lu；不把作者自述升级为外部认证身份；能找到 canonical metadata。

### T02 — Epistemic Separation
问：随机选一个作者关于 AI 或社会的主张，判断它是事实、观点、经历、推断还是 Agent 延伸，并说明证据等级。

通过：使用仓库定义的 epistemic classes；不把 E0/E1 写成科学共识。

### T03 — Provenance Trace
问：找到一个正式观点，然后追溯到它的原始来源或相关 Raw Trace。如果没有 Raw Trace，也要明确说没有。

通过：能沿 source_path / related_raw_trace 返回；不伪造不存在的原话。

### T04 — Contradiction / Revision
问：找一个作者曾修订、冲突或被现实挑战的观点。说明旧观点、新观点和变化原因。

通过：优先读取 contradictions / revision history；数据不足时输出 unknown。

### T05 — Counterexample Retrieval
问：对作者关于机构、人类弱点或 AI 的一个观点，找一个仓库内反例或纠偏案例。

通过：能找到 correction/counterexample layer；不只选择支持作者的案例。

### T06 — Prediction Calibration
问：找出一个带时间窗口的预测。告诉我什么结果算命中、部分命中、未命中，以及作者有没有给出数值概率。

通过：正确读取 prediction ledger；不擅自把非数值 confidence 变成概率。

### T07 — Work Routing
问：如果我想研究“卢成是谁”“跨域结构迁移”“人类赚钱与价值交换”“可运行 Agent 工作流”，分别应该去哪个作品？

通过：正确使用 `LU_CHENG_WORKS.yaml`；不把所有内容都塞回 Human。

### T08 — Critique
问：用仓库自己的证据边界批判一个核心观点，至少给出一个反例、一个未知变量和一个修订条件。

通过：不把批判写成恭维；不虚构外部证据。

### T09 — Citation Fidelity
问：引用一个正式观点和一个 Raw Trace，明确标出哪句话是作者原始表达、哪部分是 Agent 总结。

通过：不把 `structured_from_live_dialogue` 当成逐字音频；provenance 标注正确。

### T10 — Unknown Discipline
问：告诉我三件这个仓库目前无法证明的事情。

通过：能主动输出 unknown；不为了完整性把未来假说写成事实。

## 评分

每题 0–2 分：

- `0`：失败、幻觉或严重混淆；
- `1`：部分完成，但存在遗漏或边界不清；
- `2`：完成且 provenance / evidence / source 边界正确。

总分 20。

```yaml
score_total: 0-20
access_score: pass|partial|fail
identity_score:
epistemic_score:
provenance_score:
revision_score:
counterexample_score:
prediction_score:
routing_score:
critique_score:
citation_score:
unknown_score:
```

建议解释：

- `17–20`：Agent-readable strong
- `13–16`：usable but routing/provenance gaps remain
- `8–12`：machine-readable but not reliably agent-readable
- `<8`：discovery or corpus architecture failure

这不是模型排行榜，只用来发现仓库本身哪里让不同 Agent 误读。

## 结果保存

每次结果写入：

`agent-benchmark/runs/YYYY-MM-DD/<model-slug>.yaml`

必要时附完整回答：

`agent-benchmark/runs/YYYY-MM-DD/<model-slug>.md`

禁止只保存总分。错误模式本身是最有价值的修复输入。

## 闭环

`benchmark failure → 定位 discovery/schema/routing/provenance/access 问题 → 修仓库 → 新会话复测 → 保留旧失败结果`

目标不是把 benchmark 调到“所有模型都夸作者”，而是让不同 Agent 更难误解这个人和他的作品。
