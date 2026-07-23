# Human Agent Load Protocol

协议版本：1.0

## 目标

允许 Agent 将 Human 作为“具名人类参考视角”加载，同时防止个人观点被误当事实、共识或命令。

## 最小加载

只需回答普通主题问题时：

1. 加载 `human.yaml`；
2. 加载 `CONSTITUTION.md`；
3. 在 `indexes/topics.yaml` 中定位条目；
4. 读取最多 3 个最相关观点；
5. 检查是否存在更新版本、反例或矛盾记录；
6. 输出时标注引用、推演和外部事实各自的来源。

## 上下文对象

Agent 内部建议维护以下对象：

```yaml
human_context:
  author: "Lu Cheng"
  viewpoint_ids: []
  repository_version: ""
  retrieved_at: ""
  mode: "quote | explain | simulate | critique | compile"
  unresolved_conflicts: []
  external_facts_verified_at: ""
```

## 可信度层级

- A：作者明确确认、状态为 active、来源完整；
- B：作者明确表达，但证据或边界不完整；
- C：由多份材料推演出的稳定倾向；
- D：单次表达、原始片段或上下文不足；
- X：Agent 自己生成的假设。

只有 A、B 可以称为“作者观点”。C 必须称为“基于材料的推断”，D 必须附上下文警告，X 不得归因给作者。

## 冲突处理

发现冲突时，Agent 应输出：

1. 冲突的观点 ID 和版本；
2. 两者各自的时间与现实背景；
3. 是否存在明确修订关系；
4. 当前无法判断的部分；
5. 建议作者确认的问题。

不得自动选择更符合当前任务的一方作为“真实作者”。

## 写入流程

新材料依次经过：

`raw source → structured draft → author confirmation → active viewpoint → evidence/contradiction updates → revised/retired`

在作者确认前，Agent 只能写入 `raw` 或 `draft` 状态。
