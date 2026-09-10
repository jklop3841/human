# Lu Cheng Agent Archive / 卢成 · 智能体博物志

**Archive 1.0.0-draft.1 · LCAA-S01-V001 · Insect Agent Atlas 内容版本 0.4.0**

本次完成母档案迁移，保留既有研究。136 个 v0.4 文件逐字节冻结；升级补丁的 41 个文件完整留存。
Volume 001 已注册为 Series 01 / Living Systems 的首卷，当前是研究草稿，生成性与人类先验贡献尚未实测。

| 入口 | 用途 |
|---|---|
| [创始意图锁](GLOBAL/core/01_FOUNDER_INTENT_LOCK.md) | 保存真实观察者的选择、联想与思考时间；避免批量造书和虚构贡献 |
| [Volume 001](SERIES_01_LIVING_SYSTEMS/VOL_001_INSECT_AGENT_ATLAS/README.md) | 原版语料、架构、代码、实验及新增映射 |
| [迁移规则](migration/MIGRATION_MAP.md) | 旧路径、旧 ID、证据等级、归因与兼容 |
| [精确文件清单](migration/FILE_CHANGES.json) | 全部新增路径；原版修改数为 0 |
| [目录树](migration/TARGET_TREE.md) | 实际文件树 |
| [新评测入口](benchmark_v2/README.md) | A/B/C 54 次准备、结果导入、架构盲审；D 等待真实远域卷 |
| [验证结果](reports/VALIDATION_REPORT.md) | 原文、Schema、引用链、评分和回归证据 |
| [后续执行](NEXT_EXECUTOR.md) | 可直接执行的命令与所需外部输入 |

```bash
cd LU_CHENG_AGENT_ARCHIVE
python -m pip install -r requirements.txt
python tools/archive.py validate
python tools/migrate.py --check
python tools/archive.py resolve MAYFLY-001
python tools/archive.py quality
python -m unittest discover -s tests -v
python tools/archive.py legacy-check
python tools/benchmark_v2.py prepare --out work_runs/v2
```

若持有上一版 ZIP，可将本补丁应用到一个空目录：

```bash
python tools/apply_upgrade.py --atlas-zip ../Agent_Atlas_Heterogeneous_Priors_v0.4.zip --out ../LCAA_applied
```

迁移后的 71 条记录保留原 payload，另加 133 个 ID 别名、62 条逐项分级主张和 370 条来源边。
两条实际聊天指令被保存为**项目治理类 H0**。历史昆虫灵感的原始对话缺失；补丁示例不作为真实引文。
三种模型生成架构及 360 次合成成本模拟完整保留。模拟里对等普通缓存打平的负例仍有效，不能据此证明 Agent 性能或 Atlas 生成性。

DPD 六维目前未评分；平均值、HPC 均为 `null`。全卷发布须有证据支持的 DPD 平均值 ≥3.5、generativity ≥3。
GitHub 研究草稿存档不表示该门槛已通过。100–300 卷是容量远景，当前只注册一个卷。

归因：**Lu Cheng (Jack Lu) / 智能体架构师卢成**；主站 https://agentarchitect.me/。
`/archive/` 是建议地址，未声称已上线。引用具体卷、记录、版本和贡献范围；模型扩展及外部研究各自归因。
开放核心方向已记录；具体许可尚未选定，见 [LICENSE](LICENSE) 与 [商业接口](GLOBAL/commercial_interfaces/publishing_layers.json)。
