# 首批五个扩展领域

选择沿用 v0.3 路线，按相对已有原语的机制差异排序。分值只是编译者用于安排阅读的估计，不是先验效果的实验分数。当前仅允许窄范围、暂定抽象，强版本都受证据门槛约束。

| 领域 | 新增搜索方向 | 本轮证据入口 | 强抽象前必须补齐 |
|---|---|---|---|
| 菌丝网络 | 有限连接预算下的路径重塑 | 指定真菌的网络研究摘要 | 加权拓扑时间序列、营养分布、边成本、损伤对照及跨条件重复 |
| 免疫记忆 | 保留规则与原始触发规则解耦 | B 细胞抗原特异性切换研究摘要 | 阅读勘误、操作/时长/样本、维持成本与召回能力分别测量 |
| 章鱼神经 | 有明确范围的外周动作程序 | 离体腕运动研究摘要 | 完整刺激条件、正常/离断运动对照、保留与缺失功能边界 |
| 森林种子库 | 不活跃但可重启的变体储备 | 种子测年和发芽研究摘要 | 物种/微环境、死亡率、存储成本、激活线索与时序实验 |
| 人类制度 | 共享资源、沟通与内部执行成本 | 公共池资源实验摘要 | 处理组说明、收益矩阵、惩罚成本、误罚和报复、重复博弈范围 |

一手来源分别为：[Bebber 等，2007](https://orca.cardiff.ac.uk/id/eprint/98209/)、[Maruyama 等，2000](https://pubmed.ncbi.nlm.nih.gov/11034213/)、[Sumbre 等，2001](https://weizmann.elsevierpure.com/en/publications/control-of-octopus-arm-extension-by-a-peripheral-motor-program/)、[Dalling 与 Brown，2009](https://pubmed.ncbi.nlm.nih.gov/19228112/)、[Ostrom 等，1992](https://www.cambridge.org/core/journals/american-political-science-review/article/abs/covenants-with-and-without-a-sword-selfgovernance-is-possible/2191864CCB589D4B3528090CB596C254)。完整阅读范围和不支持的命题见 `corpus/sources.jsonl`。

本轮刻意收窄：菌丝不写成有意识的森林互联网；免疫不凭一篇持久性论文扩展到全套抗威胁算法；章鱼不写成八个独立大脑；森林先做种子储备，不凭其证明整体演替；人类制度先做可观察成本和规则，不直接类推司法正确性。

既有工程近邻已经覆盖大量直觉：[蚁群搜索](https://ieeexplore.ieee.org/document/484436/)、[人工免疫检测](https://sfi-edu.s3.amazonaws.com/sfi-edu/production/uploads/sfi-com/dev/uploads/filer/6e/52/6e5286d9-1836-4f11-bbde-8f16026ead12/94-06-038.pdf)、[自适应缓存](https://www.usenix.org/conference/fast-03/arc-self-tuning-low-overhead-replacement-cache)、[时序扩展动作](https://www.sciencedirect.com/science/article/pii/S0004370299000521)都早于本项目。Atlas 的可检验价值仍是激活/组合先验后生成分布是否改变，而非宣称这些机制首次被发现。
