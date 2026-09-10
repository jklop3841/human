# AGENT ATLAS — Heterogeneous Priors Project · v0.4

所有者 / 发起人：Lu Cheng（Jack Lu）。本版沿 `05_GPT6_MASTER_PROMPT.md` 接管，项目定义及验收目标保持不变：把人主动选取的现实关系结构编译成可展开、可检验的异质先验资产，检验它是否改变未来 Agent 的架构生成分布。

这是 v0.4 研究执行基线，包含真实原件存档、结构化语料、兼容 Schema、五领域证据计划、三个架构种、可运行盲测工具和一个已执行的合成成本模型。真实多模型实验尚未运行；本版不证明 Atlas 有效。

阅读入口依次为：`05_GPT6_MASTER_PROMPT.md` → `docs/00_TAKEOVER_AUDIT.md` → `docs/07_RUN_REPORT.md` → `docs/06_PATCH_PLAN.md`。原 v0.3 包全量保存在 archive/v0.3，没有用重建记录覆盖原件。

| 路径 | 内容 |
|---|---|
| archive/ | 15 个输入原件、读取清单、哈希 |
| corpus/ | 17 观察、23 原语、11 组合（含8旧种子）、3 架构种、来源/实验/谱系 |
| schemas/ | 向后兼容的三种记录 Schema 与新增四类记录规范 |
| dist/ | Agent 紧凑先验入口与展开索引 |
| benchmark/ | 冻结任务、三组材料、输出 Schema、评审规则 |
| prepared_pilot/ | 已生成54个独立提示、操作顺序及首轮三个调用 |
| tools/ | 校验、导出、检索、回复导入、匿名评分、统计与合成沙箱 |
| tests/ | 协议与证据隔离的回归检查；模拟样本不进入真实结果 |
| reports/ | 实际本地校验、模拟原始结果与明确零调用的实验状态 |
| docs/ | 接管审计、编译/兼容规则、来源计划、实验协议与补丁表 |

Python 3.10+。在本目录运行；无需任何模型 Key：

```bash
python -m pip install -r requirements.txt
python tools/atlas.py validate
python tools/atlas.py export
python tools/cost_sandbox.py
python -m unittest discover -s tests -v
python tools/atlas.py query --text "memory retention" --limit 4
```

已准备的 pilot 可直接使用。新建独立运行时：

```bash
python tools/benchmark.py prepare --run work_runs/pilot_02
python tools/benchmark.py register-model --run work_runs/pilot_02 --slot M01 --provider "实际提供方" --model-id "界面或API实际标识" --surface "实际使用界面或API" --evidence "身份记录来源"
```

按该 run 的 FIRST_THREE_CALLS.md 运行三个新会话。每次只复制一个 prompts 文件。将完整回复保存为文本；根据 templates/session_metadata.json 填真实会话元信息，然后由执行 Agent 运行：

```bash
python tools/benchmark.py import --run work_runs/pilot_02 --call-id 实际Q编号 --response 实际回复.txt --metadata 实际会话.json
python tools/benchmark.py blind --run work_runs/pilot_02 --out work_runs/review_02
python tools/benchmark.py analyze --run work_runs/pilot_02 --scores reviewer_a.csv reviewer_b.csv
```

生成模型不应读取 runner_only；评审模型只读 review 导出目录。真实模型调用由外部界面/API完成，该工具不会偷偷调用或模拟任何厂商模型。未配置与未知参数保持 null。

输入新现象时使用 templates/human_observation.md。人的原话和选题权在原始层保留，模型补充单独记源。不要以“受启发的自述”、局部模拟或 Schema 通过替代真实三组实验。
