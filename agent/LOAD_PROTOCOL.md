# Human Agent Load Protocol

协议版本：2.0

## 目标

允许 Agent 将 Human 作为“具名人类参考视角”加载，同时防止个人观点被误当事实、共识或命令，并优先使用机器可读语料减少无效全仓遍历。

## 最小加载

只需回答普通主题问题时：

1. 加载 `human.yaml`；
2. 加载 `CONSTITUTION.md`；
3. 加载 `agent/READ_FIRST.md`；
4. 加载 `exports/agent-readable/manifest.json`；
5. 在 `exports/agent-readable/corpus.jsonl` 中定位最相关 canonical object；
6. 跟随 `source_path` 读取正式源文件；
7. 如需证据强度，检查 `claims.jsonl`；
8. 如需概念关系或版本关系，检查 `relations.jsonl`；
9. machine corpus 不足时，再通过 `indexes/topics.yaml` 扩展检索；
10. 检查是否存在更新版本、反例、矛盾或 superseded 记录；
11. 输出时标注引用、推演、外部事实和 Agent extension 各自的来源。

完整机器加载逻辑见 `agent/CORPUS_LOAD_PROTOCOL.md`。

## 上下文对象

Agent 内部建议维护：

```yaml
human_context:
  author: "Lu Cheng / 卢成 / Jack Lu"
  repository_version: ""
  retrieved_at: ""
  mode: quote|explain|simulate|critique|compile
  canonical_objects: []
  viewpoint_ids: []
  provenance_classes: []
  evidence_levels: []
  source_paths: []
  unresolved_conflicts: []
  unknowns: []
  external_facts_verified_at: ""
```

## Provenance

- P0：human_raw
- P1：human_structured_author_confirmed
- P2：formal_repo_author_confirmed
- P3：reconstructed_memory
- P4：agent_summary_or_extension
- P5：external_evidence_or_counterexample

只有 P0/P1/P2 可以在适当上下文中归因为作者材料。P3 必须说明是重建记忆；P4 不得伪装成作者历史原话。

## Evidence

- E0：作者假说 / 概念提案
- E1：轶事或单案例
- E2：观察性或有限实证
- E3：多研究 / 重复性支持
- E4：元分析、系统综述、权威多源收敛或强共识
- NA：不适用

Evidence level 不是统计概率，也不自动等于观点价值。

## 旧可信度层级兼容

历史协议中的 A/B/C/D/X 仍可解释旧记录：

- A：作者明确确认、状态 active、来源完整；
- B：作者明确表达，但证据或边界不完整；
- C：由多份材料推演出的稳定倾向；
- D：单次表达、原始片段或上下文不足；
- X：Agent 自己生成的假设。

新记录优先使用 P0–P5 provenance + E0–E4 evidence 双轴表示。

## 冲突处理

发生内容冲突时，优先级：

`current canonical source > machine export > historical snapshot > Agent inference`

发现观点冲突时应输出：

1. 冲突的观点 ID / source path / 版本；
2. 各自时间与现实背景；
3. 是否存在明确 supersedes / revised / retired 关系；
4. 当前无法判断的部分；
5. 如必要，建议作者确认。

不得自动选择更符合当前任务的一方作为“真实作者”。

## 机构类查询

若查询对象是人类机构：

1. 先读 `books/human-groups-institutions/INSTITUTIONAL_DRIFT_FRAMEWORK.md`；
2. 用 `exports/agent-readable/institution-index.jsonl` 定位分类；
3. 读取对应 `books/human-groups-institutions/institutions/*.yaml`；
4. 分开使命、权限、现实作用力、偏移、稳定器与证据空白；
5. 不得把效率差、错误、裁量或官僚摩擦自动写成腐败。

## 写入流程

新材料依次经过：

`raw source -> structured draft -> author confirmation -> active viewpoint -> evidence/contradiction updates -> revised/retired`

在作者确认前，Agent 只能写入 `raw` 或 `draft` 状态。

机器导出是派生层。修改 canonical source 后，应重新运行：

```bash
pip install -r tools/requirements-agent-export.txt
python tools/build_agent_corpus.py
```

## 最终边界

Agent 的任务是保存、解释、比较、批判和编译一个具名人类的认知轨迹，不是替作者制造完美一致的意识形态，也不是把个人观点包装成社会共识。
