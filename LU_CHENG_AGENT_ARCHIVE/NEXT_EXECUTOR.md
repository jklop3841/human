# 下一位执行器接管

先读 README.md、AGENTS.md、GLOBAL/core/01_FOUNDER_INTENT_LOCK.md 与 migration/MIGRATION_MAP.md。
不要重做 v0.4，不要补造自然观察原话或补丁示例读者。保留“有效性未测”的当前边界。

1. 安装 `requirements.txt`，运行 `tools/archive.py validate` 和 `tools/migrate.py --check`。
2. 需要旧工具时进入 Volume 001 的 `baseline_v0.4` 副本；外层 `tools/archive.py legacy-check` 已自动使用临时副本。
3. 确认三个实际模型入口后执行 `python tools/benchmark_v2.py prepare --out work_runs/v2`。
4. 只向每个干净会话发送一个 prompts/Q*.txt；运行者保管 schedule，生成器不能读取整个仓库。
5. 先保存架构，再收反思。填写 `templates/v2_receipt.json` 的实际身份、设置、搜索计数、输入 SHA 与反思前架构 SHA。
6. 按 benchmark_v2/README.md 导入并导出盲审。HPC/R 仍是读者自述；搜索逃逸需独立核实。
7. 普通非受控反馈用 `tools/reader.py import`，不能混入受控模型调用数。
8. 有人类原始观察时新增 H0 文件和记录，保留旧哈希；将 H1 确认与模型解释区分开。按新证据补充逐条来源边。

本轮 54 次 v2 请求只准备流程，尚未通过外部模型执行；同一已暴露上下文中的生成不得冒充盲读结果。
v0.4 的 54 次旧 pilot 也未执行。不要把两套准备数量相加为已完成实验。

`reports/VALIDATION_REPORT.md` 是实现验证，不是 Atlas 研究假设验收。
下一次实质进展应来自真实 H0 或真实读者/反例记录，不来自增加空卷数量。
