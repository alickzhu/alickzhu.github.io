# 📝 Publications

(* Equal contribution, † Corresponding author)

## 🤔 Reasoning

### Reasoning Methods

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML-2025 Spotlight</div><img src='/images/soft.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Soft Reasoning: Navigating Solution Spaces in Large Language Models through Controlled Embedding Exploration](https://www.arxiv.org/abs/2505.24688) [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/alickzhu/Soft-Reasoning)  <br>
**Qinglin Zhu**, Runcong Zhao, Hanqi Yan, Yulan He, Yudong Chen, Lin Gui.

- Proposes an embedding-based search framework that guides LLM generation by optimising the first token's embedding.<br>
- Combines embedding perturbation for controlled exploration with Bayesian optimisation via a verifier-guided objective, balancing exploration and exploitation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP-2025</div><img src='/images/SPARSE_.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Sparse Activation Editing for Reliable Instruction Following in Narratives](https://arxiv.org/abs/2505.16505) <br>
Runcong Zhao, Chengyu Cao, **Qinglin Zhu**, Xiucheng Lv, Shun Shao, Lin Gui, Ruifeng Xu, Yulan He.

- We introduce Concise-SAE, a training-free method that improves instruction following by editing relevant neurons using natural language instructions.
- Tested on our new FreeInstruct benchmark of 1,212 narrative-rich examples, it achieves state-of-the-art results without training or labelled data.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL-2024</div><img src='/images/mirror.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mirror: A Multiple-perspective Self-Reflection Method for Knowledge-rich Reasoning](https://arxiv.org/abs/2402.14963) <br>
Hanqi Yan\*, **Qinglin Zhu**\* , Xinyu Wang, Lin Gui, Yulan He. [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/hanqi-qi/Mirror)
- Proposes Mirror, enabling LLMs to reflect from multiple perspectives via Navigator–Reasoner cooperation.<br>
- Encourages both diverse and consistent reasoning to overcome self-reflection traps.<br>
</div>
</div>

### Decoding & Generation

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/LRD_fit.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Latent Refinement Decoding: Enhancing Diffusion-Based Language Models by Refining Belief States](https://arxiv.org/abs/2510.11052) <br>
**Qinglin Zhu**, Yizhen Yao, Runcong Zhao, Yanzheng Xiang, Amrutha Saseendran, Chen Jin, Philip Alexander Teare, Bin Liang, Yulan He, Lin Gui.
- Proposes Latent Refinement Decoding (LRD), a two-stage framework that tackles information loss and premature commitment in diffusion-based language models via latent refinement and predictive feedback.<br>
- Enables faster, globally consistent parallel generation as a principled alternative to autoregressive decoding.<br>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/Stop the Flip-Flop.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Stop the Flip-Flop: Context-Preserving Verification for Fast Revocable Diffusion Decoding](https://arxiv.org/abs/2602.06161) <br>
Yanzheng Xiang, Lan Wei, Yizhen Yao, **Qinglin Zhu**, Hanqi Yan, Chen Jin, Philip Alexander Teare, Dandan Zhang, Lin Gui, Amrutha Saseendran, Yulan He.

- Proposes COVER, a context-preserving verification method that uses KV cache overriding for leave-one-out verification and stability-aware scoring.<br>
- Eliminates flip-flop oscillations in revocable diffusion decoding, enabling faster and more stable parallel text generation.
</div>
</div>

### Retrieval & Hallucination

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI-2026 Oral</div><img src='/images/aaai25.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Spectrum Projection Score: Aligning Retrieved Summaries with Reader Models in Retrieval-Augmented Generation](https://ojs.aaai.org/index.php/AAAI/article/view/40371) <br>
Zhanghao Hu, **Qinglin Zhu**, Siya Qi, Yulan He, Hanqi Yan, Lin Gui.
- Proposes SPS, a supervision-free metric to assess semantic alignment between retrieved summaries and LLM representations.<br>
- Introduces xCompress, an inference-time controller that ranks and compresses retrievals to improve generation and clarify retrieval–generation interaction.<br>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL-2025</div><img src='/images/beyond_prompt.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Beyond Prompting: An Efficient Embedding Framework for Open-Domain Question Answering](https://arxiv.org/abs/2503.01606)  <br>
Zhanghao Hu, Hanqi Yan, <b>Qinglin Zhu†</b>, Zhenyi Shen, Yulan He, Lin Gui.
- Proposes EmbQA, an embedding-level framework for open-domain QA that optimizes retrieval with unsupervised contrastive
  learning and improves answer diversity via exploratory embeddings.<br>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/Beyond RAG for Agent Memory.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Beyond RAG for Agent Memory: Retrieval by Decoupling and Aggregation](https://arxiv.org/abs/2602.02007) <br>
Zhanghao Hu, **Qinglin Zhu**, Hanqi Yan, Yulan He, Lin Gui.

- Proposes xMemory, which decouples agent memories into semantic components and organises them hierarchically.<br>
- Retrieves via top-down aggregation to capture diverse themes, outperforming standard RAG on long-horizon agent tasks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/Detecting Contextual Hallucinations in Large Language Models.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Detecting Contextual Hallucinations in LLMs with Frequency-Aware Attention](https://arxiv.org/abs/2602.18145) <br>
Siya Qi, Yudong Chen, Runcong Zhao, **Qinglin Zhu**, Zhanghao Hu, Wei Liu, Yulan He, Zheng Yuan, Lin Gui.

- Models attention patterns as discrete signals and extracts high-frequency components to detect contextual hallucinations.<br>
- Builds a lightweight, training-free detector that outperforms existing baselines on RAGTruth and HalluRAG benchmarks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/Beyond Static Cropping.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Beyond Static Cropping: Layer-Adaptive Visual Localization and Decoding Enhancement](https://arxiv.org/abs/2602.04304) <br>
Zipeng Zhu, Zhanghao Hu, **Qinglin Zhu**, Yuxi Hong, Yijun Liu, Jingyong Su, Yulan He, Lin Gui.

- Proposes LASER, a training-free layer-adaptive visual localization method with a VAQ metric for selecting query-relevant layers at inference time.<br>
- Enhances vision–language model decoding without additional training, improving fine-grained visual understanding.
</div>
</div>

## 💻 Code Intelligence

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/Pull Requests as a Training Signal for Repo-Level Code Editing.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Pull Requests as a Training Signal for Repo-Level Code Editing](https://arxiv.org/abs/2602.07457) <br>
**Qinglin Zhu**, Tianyu Chen, Shuai Lu, Lei Ji, Runcong Zhao, Murong Ma, Xiangxiang Dai, Yulan He, Lin Gui, Yeyun Gong.

- Introduces Clean-PR, a pipeline that converts noisy PR diffs into structured edit blocks, yielding 2M training samples across 12 languages.<br>
- Achieves +13.6% on SWE-bench Lite and +12.3% on SWE-bench Verified, demonstrating the value of real-world PRs for repo-level code editing.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/Synthesizing File-Level Data for Unit Test Generation with.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Synthesizing File-Level Data for Unit Test Generation with Chain-of-Thoughts via Self-Debugging](https://arxiv.org/abs/2602.03181) <br>
Ziyue Hua, Tianyu Chen, Yeyun Gong, Shuai Lu, Peng Cheng, **Qinglin Zhu**, Yibo He, Yingjie Fu, Wenpin Jiao, Wei Yang, Tao Xie.

- Proposes a self-debugging pipeline with guided test repair and CoT compression, synthesising 74K high-quality file-level unit test examples.<br>
- Fine-tuned models outperform o4-mini on unit test generation, showing that synthetic data with iterative debugging can match frontier-model quality.
</div>
</div>


## 📚 Narrative Understanding

<div class='paper-box'><div class='paper-box-image'><div class="badge">ACL-2024 Findings</div><div><img src='/images/conan.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Large Language Models Fall Short: Understanding Complex Relationships in Detective Narratives](https://arxiv.org/abs/2402.11051)<br>
Runcong Zhao\*, **Qinglin Zhu**\* , Hainiu Xu, Jiazheng Li, Yuxiang Zhou, Yulan He, Lin Gui. [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/BLPXSPG/Conan/tree/main)

- Existing datasets for narrative understanding often fail to represent the complexity and uncertainty of relationships in real-life social scenarios. 
- To address this gap, we introduce a new benchmark, Conan, designed for extracting and analysing intricate character relation graphs from detective narratives. 
</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/PLAYER.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PLAYER*: Enhancing LLM-based Multi-Agent Communication and Interaction in Murder Mystery Games](https://arxiv.org/abs/2404.17662) <br>
**Qinglin Zhu**, Runcong Zhao, Jinhua Du, Lin Gui, Yulan He. [![](https://img.shields.io/github/stars/alickzhu/PLAYER?style=social)](https://github.com/alickzhu/PLAYER)

- We propose PLAYER*, a novel framework for Murder Mystery Games (剧本杀) using an anytime sampling-based planner and a questioning-driven search framework. 
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='/images/symbolicthought.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SymbolicThought: Integrating Language Models and Symbolic Reasoning for Consistent and Interpretable Human Relationship Understanding](https://arxiv.org/abs/2507.04189) <br>
Runcong Zhao, **Qinglin Zhu**\*, Hainiu Xu, Bin Liang, Yulan He, Lin Gui.

- Proposes SymbolicThought, a human-in-the-loop system combining LLM extraction and symbolic reasoning for character relationship understanding.
- Supports editable relationship graphs, logical constraints, and interactive conflict resolution.
</div>
</div>


## 😆 Sentiment Analysis and Stance Detection

- ``ACL-2022`` [JointCL: A Joint Contrastive Learning Framework for Zero-Shot Stance Detection](https://aclanthology.org/2022.acl-long.7/) <br>
  Bin Liang\*, **Qinglin Zhu**\* , Xiang Li, Min Yang, Lin Gui, Yulan He, and Ruifeng Xu. [![GitHub](https://img.shields.io/badge/GitHub--blue?logo=github&style=social)](https://github.com/HITSZ-HLT/JointCL) <br>
- ``SIGIR-2022`` [Enhancing Zero-Shot Stance Detection via Targeted Background Knowledge](https://dl.acm.org/doi/10.1145/3477495.3531807) <br>
  **Qinglin Zhu**, Bin Liang, Jingyi Sun, Jiachen Du, Lanjun Zhou, and Ruifeng Xu.
- ``CCL-2020`` [Attention-based Recurrent Network Combined with Financial Lexicon for Aspect-level Sentiment Classification](https://aclanthology.org/2020.ccl-1.63/) <br>
  **Qinglin Zhu**, Bin Liang, Liuyu Han, Yi Chen, Ruifeng Xu, and Ruibin Mao.
- ``LREC-2020`` [Target-based sentiment annotation in Chinese financial news](https://aclanthology.org/2020.lrec-1.620/#:~:text=The%20clause%20reflecting%20the%20profitability,expression%20for%20determining%20the%20polarity.) <br>
  Chaofa Yuan, Yuhan Liu, Rongdi Yin, Jun Zhang, **Qinglin Zhu**, Ruibin Mao, Ruifeng Xu.

## 🗣️ Argumentation Mining and Sequence Labeling

- ``ACL-2022`` [Have my arguments been replied to? Argument Pair Extraction as Machine Reading Comprehension](https://aclanthology.org/2022.acl-short.4/) <br>
  Jianzhu Bao, Jingyi Sun, **Qinglin Zhu**, and Ruifeng Xu.
- ``SemEval-2021`` [HITSZ-HLT at SemEval-2021 Task 5: Ensemble Sequence Labeling and Span Boundary Detection for Toxic Span Detection](https://aclanthology.org/2021.semeval-1.63/) <br>
  **Qinglin Zhu**, Zijie Lin, Yice Zhang, Jingyi Sun, Xiang Li, Qihui Lin, Yixue Dang, and Ruifeng Xu.
- ``NLPCC-2021`` [A Hierarchical Sequence Labeling Model for Argument Pair Extraction](https://link.springer.com/chapter/10.1007/978-3-030-88483-3_38) <br>
  Jingyi Sun, **Qinglin Zhu**, Jianzhu Bao, Jipeng Wu, Caihua Yang, Rui Wang, and Ruifeng Xu.
