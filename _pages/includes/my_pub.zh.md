<span class='anchor' id='publications-zh'></span>
# 📝 论文

(* 共同一作, † 通讯作者)

## 🤔 LLM Reasoning, Decoding & Code Intelligence

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML-2025 Spotlight</div><img src='/images/soft.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://www.arxiv.org/abs/2505.24688) [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/alickzhu/Soft-Reasoning)  <br>
**Qinglin Zhu**, Runcong Zhao, Hanqi Yan, Yulan He, Yudong Chen, Lin Gui.

- 提出了一种基于Embedding的搜索框架，通过优化首个token的Embedding来引导大模型生成。
- 结合Embedding扰动实现可控探索，并利用基于验证器的贝叶斯优化目标，在探索与利用之间取得平衡。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL-2026 Demo</div><img src='/images/symbolicthought.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SymbolicThought: Integrating Language Models and Symbolic Reasoning for Consistent and Interpretable Human Relationship Understanding](https://arxiv.org/abs/2507.04189) <br>
Runcong Zhao, **Qinglin Zhu**\*, Hainiu Xu, Bin Liang, Yulan He, Lin Gui.

- 提出SymbolicThought框架，融合大语言模型关系抽取与符号推理，实现高效、可解释的人物关系理解。
- 支持关系图可编辑、逻辑约束校验和交互式冲突解决。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL-2024</div><img src='/images/mirror.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mirror: A Multiple-perspective Self-Reflection Method for Knowledge-rich Reasoning](https://arxiv.org/abs/2402.14963) <br>
Hanqi Yan\*, **Qinglin Zhu**\* , Xinyu Wang, Lin Gui, Yulan He. [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/hanqi-qi/Mirror)
- 我们提出了 Mirror，使大模型能够通过导航者-推理者协作，从多视角进行自我反思。
- 鼓励多样且一致的推理，以克服自我反思陷阱。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div class="badge">ACL-2024 Findings</div><div><img src='/images/conan.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Large Language Models Fall Short: Understanding Complex Relationships in Detective Narratives](https://arxiv.org/abs/2402.11051)<br>
Runcong Zhao\*, **Qinglin Zhu**\* , Hainiu Xu, Jiazheng Li, Yuxiang Zhou, Yulan He, Lin Gui. [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/BLPXSPG/Conan/tree/main)

- 现有叙事理解数据集往往无法体现真实社交场景中关系的复杂性和不确定性。
- 为此我们提出了 Conan 基准，用于侦探叙事中复杂人物关系图的抽取与分析。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/LRD_fit.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Latent Refinement Decoding: Enhancing Diffusion-Based Language Models by Refining Belief States](https://arxiv.org/abs/2510.11052) <br>
**Qinglin Zhu**, Yizhen Yao, Runcong Zhao, Yanzheng Xiang, Amrutha Saseendran, Chen Jin, Philip Alexander Teare, Bin Liang, Yulan He, Lin Gui.
- 提出潜变量优化解码（LRD）框架，通过潜变量优化与预测反馈两阶段机制，解决扩散式语言模型中的信息丢失与过早决策问题。<br>
- 实现更高效且全局一致的并行生成，为自回归解码提供了一种更具理论依据的替代方案。<br>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/Pull Requests as a Training Signal for Repo-Level Code Editing.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Pull Requests as a Training Signal for Repo-Level Code Editing](https://arxiv.org/abs/2602.07457) <br>
**Qinglin Zhu**, Tianyu Chen, Shuai Lu, Lei Ji, Runcong Zhao, Murong Ma, Xiangxiang Dai, Yulan He, Lin Gui, Yeyun Gong.

- 提出 Clean-PR 流水线，将含噪声的 PR diff 转化为结构化编辑块，跨 12 种编程语言生成 200 万训练样本。<br>
- 在 SWE-bench Lite 上提升 13.6%，SWE-bench Verified 上提升 12.3%，验证了真实 PR 数据在仓库级代码编辑中的价值。
</div>
</div>

- ``EMNLP-2025`` [Sparse Activation Editing for Reliable Instruction Following in Narratives](https://arxiv.org/abs/2505.16505) <br>
  Runcong Zhao, Chengyu Cao, **Qinglin Zhu**, et al.
- ``Preprint`` [Stop the Flip-Flop: Context-Preserving Verification for Fast Revocable Diffusion Decoding](https://arxiv.org/abs/2602.06161) <br>
  Yanzheng Xiang, Lan Wei, Yizhen Yao, **Qinglin Zhu**, Hanqi Yan, et al.
- ``Preprint`` [Synthesizing File-Level Data for Unit Test Generation with Chain-of-Thoughts via Self-Debugging](https://arxiv.org/abs/2602.03181) <br>
  Ziyue Hua, Tianyu Chen, Yeyun Gong, Shuai Lu, Peng Cheng, **Qinglin Zhu**, et al.

## 🔍 Retrieval-Augmented Generation & Agent

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI-2026 Oral</div><img src='/images/aaai25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Spectrum Projection Score: Aligning Retrieved Summaries with Reader Models in Retrieval-Augmented Generation](https://ojs.aaai.org/index.php/AAAI/article/view/40371) <br>
Zhanghao Hu, **Qinglin Zhu**, Siya Qi, Yulan He, Hanqi Yan, Lin Gui.
- 提出 SPS，一种无监督指标，用于评估检索摘要与LLM表示之间的语义对齐。<br>
- 引入 xCompress，一种推理时控制器，用于排序和压缩检索结果，以提升生成效果。<br>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL-2025</div><img src='/images/beyond_prompt.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering](https://arxiv.org/abs/2503.01606)  <br>
Zhanghao Hu, Hanqi Yan, <b>Qinglin Zhu†</b>, Zhenyi Shen, Yulan He, Lin Gui.
- 我们提出了 EmbQA，一种面向开放域问答的嵌入级框架，通过无监督对比学习优化检索，并利用探索性Embedding提升答案多样性和准确率。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/Beyond RAG for Agent Memory.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation](https://arxiv.org/abs/2602.02007) <br>
Zhanghao Hu, **Qinglin Zhu**, Hanqi Yan, Yulan He, Lin Gui.

- 提出 xMemory，将智能体记忆解耦为语义组件并进行层次化组织。<br>
- 通过自顶向下的聚合检索捕捉多样化主题，在长时序智能体任务上优于标准 RAG 方法。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/PLAYER.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PLAYER*: Enhancing LLM-based Multi-Agent Communication and Interaction in Murder Mystery Games](https://arxiv.org/abs/2404.17662) <br>
**Qinglin Zhu**, Runcong Zhao, Jinhua Du, Lin Gui, Yulan He. [![](https://img.shields.io/github/stars/alickzhu/PLAYER?style=social)](https://github.com/alickzhu/PLAYER)

- 我们提出了 PLAYER*，一个用于剧本杀的多智能体交互框架，结合了采样规划器和提问驱动的搜索。
</div>
</div>

- ``Preprint`` [Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention](https://arxiv.org/abs/2602.18145) <br>
  Siya Qi, Yudong Chen, Runcong Zhao, **Qinglin Zhu**, Zhanghao Hu, et al.
- ``Preprint`` [Beyond Static Cropping: Layer-Adaptive Visual Localization and Decoding Enhancement](https://arxiv.org/abs/2602.04304) <br>
  Zipeng Zhu, Zhanghao Hu, **Qinglin Zhu**, et al.

## 😆 情感分析与立场检测

- ``ACL-2022`` [JointCL: A Joint Contrastive Learning Framework for Zero-Shot Stance Detection](https://aclanthology.org/2022.acl-long.7/) <br>
  Bin Liang\*, **Qinglin Zhu**\* , Xiang Li, Min Yang, Lin Gui, Yulan He, and Ruifeng Xu. [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/HITSZ-HLT/JointCL) <br>
- ``SIGIR-2022`` [Enhancing Zero-Shot Stance Detection via Targeted Background Knowledge](https://dl.acm.org/doi/10.1145/3477495.3531807) <br>
  **Qinglin Zhu**, Bin Liang, Jingyi Sun, Jiachen Du, Lanjun Zhou, and Ruifeng Xu.
- ``CCL-2020`` [Attention-based Recurrent Network Combined with Financial Lexicon for Aspect-level Sentiment Classification](https://aclanthology.org/2020.ccl-1.63/) <br>
  **Qinglin Zhu**, Bin Liang, Liuyu Han, Yi Chen, Ruifeng Xu, and Ruibin Mao.
- ``LREC-2020`` [Target-based sentiment annotation in Chinese financial news](https://aclanthology.org/2020.lrec-1.620/#:~:text=The%20clause%20reflecting%20the%20profitability,expression%20for%20determining%20the%20polarity.) <br>
  Chaofa Yuan, Yuhan Liu, Rongdi Yin, Jun Zhang, **Qinglin Zhu**, Ruibin Mao, Ruifeng Xu.

## 🗣️ 论辩挖掘与序列标注

- ``ACL-2022`` [Have my arguments been replied to? Argument Pair Extraction as Machine Reading Comprehension](https://aclanthology.org/2022.acl-short.4/) <br>
  Jianzhu Bao, Jingyi Sun, **Qinglin Zhu**, and Ruifeng Xu.
- ``SemEval-2021`` [HITSZ-HLT at SemEval-2021 Task 5: Ensemble Sequence Labeling and Span Boundary Detection for Toxic Span Detection](https://aclanthology.org/2021.semeval-1.63/) <br>
  **Qinglin Zhu**, Zijie Lin, Yice Zhang, Jingyi Sun, Xiang Li, Qihui Lin, Yixue Dang, and Ruifeng Xu.
- ``NLPCC-2021`` [A Hierarchical Sequence Labeling Model for Argument Pair Extraction](https://link.springer.com/chapter/10.1007/978-3-030-88483-3_38) <br>
  Jingyi Sun, **Qinglin Zhu**, Jianzhu Bao, Jipeng Wu, Caihua Yang, Rui Wang, and Ruifeng Xu. 
