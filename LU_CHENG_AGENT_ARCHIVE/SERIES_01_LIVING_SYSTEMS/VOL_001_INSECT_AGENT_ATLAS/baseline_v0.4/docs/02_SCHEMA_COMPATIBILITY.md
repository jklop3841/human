# Schema 兼容说明

`schemas/v0.3/` 保存三个原 Schema，不更名、不删字段、不更换原枚举。顶层三个同名 Schema 保留原必填项及语义；只有记录显式写入 `schema_version: "0.4"` 时，才要求新的 provenance、claims 等字段。

因此，原来没有版本字段的合规 v0.3 记录可以直接通过新 Schema。老 reader 允许扩展字段时也能读取新记录。未知 reader 若硬编码字段集合，需要走 compact/legacy 适配，不能声称普遍兼容。使用旧代码但读取新三种记录时，旧枚举仍保持：species.status 的 ARCHIVED 不被重新解释成认知层。

新增：source、composition、experiment、lineage 四种 Schema。旧种子组合允许 `record_status: legacy_incomplete`；新组合必须完整提供交互、涌现、证伪与沙箱。未知字段留空并解释，不为通过校验伪造历史数据。

原语 parents 只表达推导关系，必须无环；interaction_candidates 表示可能协作，不保证成功；conflicts 指条件性冲突，不是互斥类型系统。程序另外校验跨记录引用，JSON Schema 本身不负责数据库外键。

逐条 claims 承载科学状态，记录-level epistemic_status 提供概览。species.status=HYPOTHESIZED 可以同时包含一个已完成的合成成本实验 claim，这不等于完整架构经验证。

迁移不是恢复原件。当前 12 行 raw_observation 均为交接表格的逐字片段；新增定义和组合原语分配均有 reconstruction_note。拿到原始 v0.2 后应存入新的不可变来源，建立 diff 和 supersedes 关系，保留当前记录及原文哈希，不覆盖原始材料。
