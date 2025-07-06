# 📝 论文

(* 共同一作, † 通讯作者)

## 🤔 推理

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML-2025 Spotlight</div><img src='/images/soft.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://www.arxiv.org/abs/2505.24688) [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/alickzhu/Soft-Reasoning)  <br>
**Qinglin Zhu**\*, Runcong Zhao\*, Hanqi Yan, Yulan He, Yudong Chen, Lin Gui.

- 我们提出了一种基于嵌入的搜索框架，通过优化首个 token 的嵌入来引导生成。
- 该方法结合了 (1) 嵌入扰动以实现可控探索，(2) 基于验证器的贝叶斯优化目标，在探索与利用之间取得平衡。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL-2025</div><img src='/images/beyond_prompt.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering](https://arxiv.org/abs/2503.01606)  <br>
Zhanghao Hu, Hanqi Yan, <b>Qinglin Zhu†</b>, Zhenyi Shen, Yulan He, Lin Gui.
- 提出了 EmbQA，一种面向开放域问答的嵌入级框架，通过无监督对比学习优化检索，并利用探索性嵌入提升答案多样性。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL-2024</div><img src='/images/mirror.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mirror: A Multiple-perspective Self-Reflection Method for Knowledge-rich Reasoning](https://arxiv.org/abs/2402.14963) <br>
Hanqi Yan\*, **Qinglin Zhu**\* , Xinyu Wang, Lin Gui, Yulan He. [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/hanqi-qi/Mirror)
- 提出了 Mirror，使大模型能够通过导航者-推理者协作，从多视角进行自我反思。
- 鼓励多样且一致的推理，以克服自我反思陷阱。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><img src='/images/sparse.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Sparse Activation Editing for Reliable Instruction Following in Narratives](https://arxiv.org/abs/2505.16505) <br>
Runcong Zhao, Chengyu Cao, **Qinglin Zhu**, Xiucheng Lv, Shun Shao, Lin Gui, Ruifeng Xu, Yulan He.

- 我们提出了 Concise-SAE，这是一种无需训练的指令跟随方法，通过自然语言指令编辑相关神经元。
- 在我们新提出的 FreeInstruct 基准（1212 个叙事样本）上，无需训练或标注数据即可达到 SOTA。
</div>
</div>

## 📚 叙事文本理解

<div class='paper-box'><div class='paper-box-image'><div class="badge">ACL-2024 Findings</div><div><img src='/images/conan.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Large Language Models Fall Short: Understanding Complex Relationships in Detective Narratives](https://arxiv.org/abs/2402.11051)<br>
Runcong Zhao\*, **Qinglin Zhu**\* , Hainiu Xu, Jiazheng Li, Yuxiang Zhou, Yulan He, Lin Gui. [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/BLPXSPG/Conan/tree/main)

- 现有叙事理解数据集往往无法体现真实社交场景中关系的复杂性和不确定性。
- 为此我们提出了 Conan 基准，用于侦探叙事中复杂人物关系图的抽取与分析。
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><img src='/images/PLAYER.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PLAYER*: Enhancing LLM-based Multi-Agent Communication and Interaction in Murder Mystery Games](https://arxiv.org/abs/2404.17662) <br>
**Qinglin Zhu**\*, Runcong Zhao\*, Jinhua Du, Lin Gui, Yulan He. [![](https://img.shields.io/github/stars/alickzhu/PLAYER?style=social)](https://github.com/alickzhu/PLAYER)

- 我们提出了 PLAYER*，一个用于剧本杀的多智能体交互框架，结合了任意时采样规划器和提问驱动的搜索。
</div>
</div>

## 😆 情感分析与立场检测

- ``ACL-2022`` [JointCL: A Joint Contrastive Learning Framework for Zero-Shot Stance Detection](https://aclanthology.org/2022.acl-long.7/) <br>
  Bin Liang\*, **Qinglin Zhu**\* , Xiang Li, Min Yang, Lin Gui, Yulan He, and Ruifeng Xu. [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/HITSZ-HLT/JointCL) <br>
- ``SIGIR-2022`` [Enhancing Zero-Shot Stance Detection via Targeted Background Knowledge](https://dl.acm.org/doi/10.1145/3477495.3531807) <br>
  **Qinglin Zhu**\*, Bin Liang\*, Jingyi Sun, Jiachen Du, Lanjun Zhou, and Ruifeng Xu.
- ``CCL-2020`` [Attention-based Recurrent Network Combined with Financial Lexicon for Aspect-level Sentiment Classification](https://aclanthology.org/2020.ccl-1.63/) <br>
  **Qinglin Zhu**, Bin Liang, Liuyu Han, Yi Chen, Ruifeng Xu, and Ruibin Mao.
- ``LREC-2020`` [Target-based sentiment annotation in Chinese financial news](https://aclanthology.org/2020.lrec-1.620/#:~:text=The%20clause%20reflecting%20the%20profitability,expression%20for%20determining%20the%20polarity.) <br>
  Chaofa Yuan, Yuhan Liu, Rongdi Yin, Jun Zhang, **Qinling Zhu**, Ruibin Mao, Ruifeng Xu.

## 🗣️ 论辩挖掘与序列标注

- ``SemEval-2021`` [HITSZ-HLT at SemEval-2021 Task 5: Ensemble Sequence Labeling and Span Boundary Detection for Toxic Span Detection](https://aclanthology.org/2021.semeval-1.63/) <br>
  **Qinglin Zhu**\*, Zijie Lin\*, Yice Zhang\*, Jingyi Sun, Xiang Li, Qihui Lin, Yixue Dang, and Ruifeng Xu.
- ``ACL-2022`` [Have my arguments been replied to? Argument Pair Extraction as Machine Reading Comprehension](https://aclanthology.org/2022.acl-short.4/) <br>
  Jianzhu Bao, Jingyi Sun, **Qinglin Zhu**, and Ruifeng Xu.
- ``NLPCC-2021`` [A Hierarchical Sequence Labeling Model for Argument Pair Extraction](https://link.springer.com/chapter/10.1007/978-3-030-88483-3_38) <br>
  Jingyi Sun, **Qinglin Zhu**, Jianzhu Bao, Jipeng Wu, Caihua Yang, Rui Wang, and Ruifeng Xu. 