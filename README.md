<div align="center">

# Must-Read Papers for Machine Learning

**A deliberately curated path from statistical thinking to modern AI systems.**

[![Curated for 2026](https://img.shields.io/badge/curated-2026-0969da?style=flat-square)](#curation-principles)
[![Foundations to frontier](https://img.shields.io/badge/scope-foundations%20to%20frontier-8250df?style=flat-square)](#essential-curriculum)
<!-- progress:start -->
[![Reading progress](https://img.shields.io/badge/read-3%20of%2098-2ea44f?style=flat-square)](#reading-system)
<!-- progress:end -->

Not every famous paper belongs here. This list favors ideas that changed how people
**understand, build, evaluate, or operate** machine-learning systems.

[Start here](#essential-curriculum) · [Choose a track](#specialization-tracks) · [Reading system](#reading-system) · [What changed](#what-changed-in-2026)

</div>

---

## Reading System

The status marker is the source of truth: change `⬜` to `✅` after reading a paper.
Your existing completed papers have been preserved.

| Level | Meaning |
| --- | --- |
| **Essential** | High-leverage idea that belongs in a broad ML education. |
| **Recommended** | The next paper to read when specializing in that track. |
| **Reference** | Valuable history, survey, or implementation detail; skim when needed. |

After changing a marker, run `python3 tools/update_progress.py` to refresh the badge at the top.
For a useful reading habit, capture only three things: the problem, the key idea, and one limitation.

> **Suggested pace:** one essential paper and one track paper per week. Read the abstract,
> figures, and conclusion first; only then decide whether the full derivation is worth the time.

## Essential Curriculum

This is the opinionated core of the repository. Read it in order within each stage; the stages
can overlap. Thirty papers are enough to build a coherent map without pretending the field is small.

### 1. Think Clearly About Data and Models

| Status | Year | Paper | Why it earns a place |
| --- | ---: | --- | --- |
| ⬜ | 2014 | [Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf) | A durable model for organizing tabular data and reproducible analysis. |
| ⬜ | 2001 | [Statistical Modeling: The Two Cultures](https://projecteuclid.org/euclid.ss/1009213726) | Explains the tension between interpretable data models and predictive algorithms. |
| ⬜ | 2018 | [Model Evaluation, Model Selection, and Algorithm Selection](https://arxiv.org/abs/1811.12808) | The practical foundation for honest experiments and defensible comparisons. |
| ⬜ | 2016 | [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754) | The modern tabular baseline and a strong lesson in algorithm-system co-design. |
| ⬜ | 2014 | [A Tutorial on Principal Component Analysis](https://arxiv.org/abs/1404.1100) | Linear algebra, compression, and representation learning in their simplest useful form. |

### 2. Understand Deep Learning

| Status | Year | Paper | Why it earns a place |
| --- | ---: | --- | --- |
| ✅ | 2015 | [Deep Learning](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf) | LeCun, Bengio, and Hinton's compact historical map of the deep-learning shift. |
| ⬜ | 2018 | [The Matrix Calculus You Need for Deep Learning](https://arxiv.org/abs/1802.01528) | Makes gradients and backpropagation concrete enough to derive, not memorize. |
| ⬜ | 2014 | [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980) | The optimizer most practitioners meet first; understand both its appeal and assumptions. |
| ⬜ | 2015 | [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) | Residual connections made very deep networks trainable and became a general design pattern. |
| ✅ | 2017 | [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | The transformer architecture that reorganized sequence modeling and then most of AI. |
| ⬜ | 2018 | [BERT](https://arxiv.org/abs/1810.04805) | The canonical encoder-only pretraining paper and a bridge to foundation models. |

### 3. Follow the Foundation-Model Shift

| Status | Year | Paper | Why it earns a place |
| --- | ---: | --- | --- |
| ⬜ | 2020 | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | GPT-3 made scale, prompting, and in-context learning central research questions. |
| ⬜ | 2020 | [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | Turns model growth into an empirical resource-allocation problem. |
| ⬜ | 2022 | [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | Chinchilla corrected the field's balance between parameters and training tokens. |
| ⬜ | 2022 | [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) | The clearest foundation for instruction tuning and RLHF-style assistants. |
| ⬜ | 2020 | [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401) | Separates parametric memory from retrievable evidence and enables grounded systems. |
| ⬜ | 2023 | [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | Recasts preference learning as a simple classification-style objective. |
| ⬜ | 2025 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | A major open report on using reinforcement learning to elicit reasoning behavior. |
| ⬜ | 2020 | [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929) | Shows that the transformer recipe transfers cleanly from language to vision. |
| ⬜ | 2021 | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | CLIP established large-scale image-text pretraining as a general visual interface. |
| ⬜ | 2020 | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | The conceptual core of the modern diffusion family. |
| ⬜ | 2021 | [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) | Moves diffusion into a compressed latent space, making high-resolution generation practical. |

### 4. Build and Evaluate Complete Systems

| Status | Year | Paper | Why it earns a place |
| --- | ---: | --- | --- |
| ⬜ | 2022 | [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) | The basic loop behind tool-using language-model agents. |
| ⬜ | 2022 | [FlashAttention](https://arxiv.org/abs/2205.14135) | A precise example of hardware-aware algorithm design changing feasible model scale. |
| ⬜ | 2022 | [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110) | Treats evaluation as a multi-metric design problem rather than one leaderboard number. |
| ⬜ | 2015 | [Hidden Technical Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems) | The model is a small part of a production ML system; this paper explains the rest. |
| ⬜ | 2018 | [Datasheets for Datasets](https://arxiv.org/abs/1803.09010) | Makes dataset provenance, intended use, and limitations first-class engineering artifacts. |
| ⬜ | 2021 | [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258) | A broad technical and social framing for models reused across many downstream systems. |
| ⬜ | 2022 | [Causal Machine Learning: A Survey and Open Problems](https://arxiv.org/abs/2206.15475) | Clarifies when prediction is insufficient and interventions or counterfactuals are required. |
| ⬜ | 2017 | [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) | A compact, practical entry point to modern policy-gradient reinforcement learning. |

## Specialization Tracks

The essential curriculum gives breadth. Pick one track below for depth. Papers are ordered by
learning value, not citation count or recency.

<details open>
<summary><strong>Classical ML, Tabular Data, and Interpretability</strong></summary>

| Status | Level | Year | Paper | Read for |
| --- | --- | ---: | --- | --- |
| ⬜ | Essential | 2001 | [Greedy Function Approximation: A Gradient Boosting Machine](https://projecteuclid.org/euclid.aos/1013203451) | The conceptual foundation of gradient boosting. |
| ⬜ | Recommended | 2017 | [LightGBM](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree) | Histogram learning, leaf-wise growth, and industrial efficiency. |
| ⬜ | Recommended | 2025 | [Accurate Predictions on Small Data with a Tabular Foundation Model](https://www.nature.com/articles/s41586-024-08328-6) | TabPFN and the emerging idea of a learned tabular algorithm. |
| ⬜ | Recommended | 2016 | [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) | The most common visualization mistakes and how to avoid them. |
| ⬜ | Recommended | 2018 | [A Tutorial on Bayesian Optimization](https://arxiv.org/abs/1807.02811) | Sample-efficient search over expensive objectives. |
| ⬜ | Recommended | 2013 | [Individual Conditional Expectation Plots](https://arxiv.org/abs/1309.6392) | Instance-level inspection of feature effects. |
| ⬜ | Recommended | 2019 | [A Study in Rashomon Curves and Volumes](https://arxiv.org/abs/1908.01755) | Model multiplicity: many equally accurate models can behave differently. |
| ⬜ | Reference | 2019 | [On Model Stability as a Function of Random Seed](https://arxiv.org/abs/1909.10447) | Why one training run is not evidence. |
| ⬜ | Reference | 2019 | [Data Shapley](https://arxiv.org/abs/1904.02868) | Valuing individual training examples. |
| ⬜ | Reference | 2009 | [Anomaly Detection: A Survey](https://doi.org/10.1145/1541880.1541882) | A taxonomy of classical anomaly-detection methods. |

</details>

<details open>
<summary><strong>Language Models, Reasoning, and Agents</strong></summary>

| Status | Level | Year | Paper | Read for |
| --- | --- | ---: | --- | --- |
| ⬜ | Essential | 2022 | [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) | How intermediate reasoning traces change few-shot behavior. |
| ⬜ | Essential | 2021 | [LoRA](https://arxiv.org/abs/2106.09685) | Parameter-efficient adaptation through low-rank updates. |
| ⬜ | Recommended | 2023 | [QLoRA](https://arxiv.org/abs/2305.14314) | Fine-tuning large quantized models under tight memory budgets. |
| ⬜ | Recommended | 2022 | [Constitutional AI](https://arxiv.org/abs/2212.08073) | Preference learning with AI feedback and explicit behavioral principles. |
| ⬜ | Recommended | 2023 | [LLaMA](https://arxiv.org/abs/2302.13971) | The open-weight model wave and compute-efficient training. |
| ⬜ | Recommended | 2024 | [OLMo: Accelerating the Science of Language Models](https://arxiv.org/abs/2402.00838) | What genuine openness means: data, code, checkpoints, and logs. |
| ⬜ | Recommended | 2024 | [Mixtral of Experts](https://arxiv.org/abs/2401.04088) | Sparse mixture-of-experts design and routing. |
| ⬜ | Recommended | 2023 | [Mamba](https://arxiv.org/abs/2312.00752) | Selective state-space models as an alternative sequence architecture. |
| ⬜ | Recommended | 2023 | [Toolformer](https://arxiv.org/abs/2302.04761) | Self-supervised learning of when and how to call tools. |
| ⬜ | Recommended | 2023 | [SWE-bench](https://arxiv.org/abs/2310.06770) | Evaluation on real repository-level software tasks. |
| ⬜ | Reference | 2023 | [Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180) | The systems idea behind high-throughput LLM serving. |
| ⬜ | Reference | 2015 | [A Primer on Neural Network Models for NLP](https://arxiv.org/abs/1510.00726) | A compact map of the pre-transformer neural NLP era. |

</details>

<details>
<summary><strong>Computer Vision and Multimodal Learning</strong></summary>

| Status | Level | Year | Paper | Read for |
| --- | --- | ---: | --- | --- |
| ⬜ | Essential | 2012 | [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks) | AlexNet and the empirical turning point for deep vision. |
| ⬜ | Recommended | 2014 | [Very Deep Convolutional Networks](https://arxiv.org/abs/1409.1556) | VGG and the value of simple, repeated architectural blocks. |
| ⬜ | Recommended | 2015 | [Faster R-CNN](https://arxiv.org/abs/1506.01497) | The canonical two-stage detector. |
| ⬜ | Recommended | 2017 | [Mask R-CNN](https://arxiv.org/abs/1703.06870) | A clean extension from detection to instance segmentation. |
| ⬜ | Recommended | 2015 | [YOLO](https://arxiv.org/abs/1506.02640) | The one-stage, real-time detection viewpoint. |
| ⬜ | Reference | 2014 | [Microsoft COCO](https://arxiv.org/abs/1405.0312) | How dataset design shaped detection and segmentation research. |
| ⬜ | Recommended | 2020 | [DETR](https://arxiv.org/abs/2005.12872) | Detection as direct set prediction with transformers. |
| ⬜ | Recommended | 2023 | [DINOv2](https://arxiv.org/abs/2304.07193) | Strong self-supervised visual representations without text labels. |
| ⬜ | Recommended | 2023 | [Segment Anything](https://arxiv.org/abs/2304.02643) | Promptable segmentation and data-engine design. |
| ⬜ | Recommended | 2024 | [SAM 2](https://arxiv.org/abs/2408.00714) | Streaming memory and promptable segmentation across images and video. |
| ⬜ | Recommended | 2023 | [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485) | LLaVA and the recipe for instruction-following vision-language models. |
| ⬜ | Reference | 2014 | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/abs/1409.0473) | Attention before transformers and a useful conceptual bridge. |

</details>

<details>
<summary><strong>Generative Modeling</strong></summary>

| Status | Level | Year | Paper | Read for |
| --- | --- | ---: | --- | --- |
| ⬜ | Essential | 2013 | [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) | Latent-variable generative modeling with the reparameterization trick. |
| ⬜ | Essential | 2014 | [Generative Adversarial Nets](https://arxiv.org/abs/1406.2661) | Adversarial learning and the generator-discriminator game. |
| ⬜ | Recommended | 2022 | [Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748) | DiT: replacing the U-Net backbone with a scalable transformer. |
| ⬜ | Recommended | 2022 | [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | A simulation-free route to continuous normalizing flows. |

</details>

<details>
<summary><strong>Reinforcement Learning and Decision Making</strong></summary>

| Status | Level | Year | Paper | Read for |
| --- | --- | ---: | --- | --- |
| ⬜ | Essential | 2013 | [Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602) | DQN and the deep-RL breakthrough. |
| ⬜ | Recommended | 2016 | [Mastering the Game of Go with Deep Neural Networks and Tree Search](https://doi.org/10.1038/nature16961) | AlphaGo's integration of policy learning, value learning, and search. |
| ⬜ | Recommended | 2020 | [Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model](https://arxiv.org/abs/1911.08265) | MuZero and planning without an explicit environment model. |
| ⬜ | Recommended | 2021 | [Decision Transformer](https://arxiv.org/abs/2106.01345) | Reframes offline RL as conditional sequence modeling. |
| ⬜ | Reference | 2023 | [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) | DreamerV3 and a robust world-model recipe across domains. |

</details>

<details>
<summary><strong>Graph Neural Networks</strong></summary>

| Status | Level | Year | Paper | Read for |
| --- | --- | ---: | --- | --- |
| ⬜ | Essential | 2016 | [Semi-Supervised Classification with Graph Convolutional Networks](https://arxiv.org/abs/1609.02907) | The standard entry point to message passing on graphs. |
| ⬜ | Recommended | 2017 | [Graph Attention Networks](https://arxiv.org/abs/1710.10903) | Learned neighbor weighting with attention. |
| ⬜ | Reference | 2019 | [A Comprehensive Survey on Graph Neural Networks](https://arxiv.org/abs/1901.00596) | A broad taxonomy and map of the field. |

</details>

<details>
<summary><strong>Recommender Systems</strong></summary>

| Status | Level | Year | Paper | Read for |
| --- | --- | ---: | --- | --- |
| ⬜ | Essential | 2009 | [Matrix Factorization Techniques for Recommender Systems](https://doi.org/10.1109/MC.2009.263) | The enduring latent-factor foundation behind collaborative filtering. |
| ⬜ | Essential | 2016 | [Deep Neural Networks for YouTube Recommendations](https://doi.org/10.1145/2959100.2959190) | Candidate generation, ranking, and serving at industrial scale. |
| ⬜ | Recommended | 2016 | [Wide & Deep Learning for Recommender Systems](https://arxiv.org/abs/1606.07792) | Combining memorization with generalization for sparse features. |
| ⬜ | Recommended | 2019 | [Deep Learning Recommendation Model](https://arxiv.org/abs/1906.00091) | DLRM, embedding-heavy architectures, and system co-design. |
| ⬜ | Recommended | 2018 | [Self-Attentive Sequential Recommendation](https://arxiv.org/abs/1808.09781) | SASRec and sequence-aware user modeling. |
| ⬜ | Recommended | 2019 | [BERT4Rec](https://arxiv.org/abs/1904.06690) | Bidirectional transformer pretraining for sequential recommendation. |
| ⬜ | Reference | 2017 | [Deep Learning Based Recommender System: A Survey](https://arxiv.org/abs/1707.07435) | A taxonomy of neural recommendation methods. |
| ⬜ | Reference | 2018 | [Explainable Recommendation: A Survey](https://arxiv.org/abs/1804.11192) | The relationship between ranking quality, transparency, and trust. |

</details>

<details>
<summary><strong>Responsible ML, Documentation, and Production</strong></summary>

| Status | Level | Year | Paper | Read for |
| --- | --- | ---: | --- | --- |
| ⬜ | Essential | 2019 | [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993) | Standardized documentation of intended use and measured limitations. |
| ⬜ | Essential | 2019 | [Fairness and Abstraction in Sociotechnical Systems](https://doi.org/10.1145/3287560.3287598) | Why fairness failures often come from drawing the system boundary too narrowly. |
| ⬜ | Recommended | 2017 | [The ML Test Score](https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/) | A concrete production-readiness rubric for data, models, infrastructure, and monitoring. |
| ⬜ | Recommended | 2021 | [Data Cascades in High-Stakes AI](https://arxiv.org/abs/2010.15283) | How neglected data work creates compounding downstream failures. |
| ⬜ | Recommended | 2021 | [On the Dangers of Stochastic Parrots](https://doi.org/10.1145/3442188.3445922) | Environmental, data, and social risks of very large language models. |

</details>

## Useful Background and Rabbit Holes

These resources remain useful, but they should not compete visually with the main curriculum.

<details>
<summary><strong>Older papers preserved from the original list</strong></summary>

| Status | Area | Paper | Place in the map |
| --- | --- | --- | --- |
| ✅ | General ML | [A Brief Introduction into Machine Learning](https://events.ccc.de/congress/2004/fahrplan/files/105-machine-learning-paper.pdf) | A completed historical overview; newer readers should start with the essential curriculum. |
| ⬜ | Statistics | [Frequentism and Bayesianism: A Python-driven Primer](https://arxiv.org/abs/1411.5018) | Friendly background on two statistical worldviews. |
| ⬜ | Optimization | [An Introduction to the Conjugate Gradient Method Without the Agonizing Pain](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf) | An unusually readable mathematical tutorial. |
| ⬜ | Deep learning | [Dropout](https://jmlr.org/papers/v15/srivastava14a.html) | Historically important regularization. |
| ⬜ | Deep learning | [Batch Normalization](https://arxiv.org/abs/1502.03167) | Historically important normalization; compare with later normalization methods. |
| ⬜ | Sequence models | [LSTM: A Search Space Odyssey](https://arxiv.org/abs/1503.04069) | Pre-transformer recurrent-model context. |
| ⬜ | Sequence models | [Empirical Evaluation of Gated Recurrent Neural Networks](https://arxiv.org/abs/1412.3555) | GRU/LSTM comparison and historical context. |
| ⬜ | Vision | [R-CNN](https://arxiv.org/abs/1311.2524) and [Fast R-CNN](https://arxiv.org/abs/1504.08083) | The path toward modern two-stage detection. |
| ⬜ | Captioning | [Show and Tell](https://arxiv.org/abs/1411.4555) and [Show, Attend and Tell](https://arxiv.org/abs/1502.03044) | Early image-language generation and visual attention. |

</details>

<details>
<summary><strong>Applied paper trails</strong></summary>

| Area | Starting points |
| --- | --- |
| Medical AI | [Machine learning classifiers and fMRI: a tutorial overview](https://pmc.ncbi.nlm.nih.gov/articles/PMC2892746/) |
| Human pose | [DensePose](https://arxiv.org/abs/1802.00434), [Parsing R-CNN](https://arxiv.org/abs/1811.12596) |
| Creative AI | [Creative Adversarial Networks](https://arxiv.org/abs/1706.07068), [Deep Painterly Harmonization](https://arxiv.org/abs/1804.03189) |
| Low-light imaging | [Handheld Mobile Photography in Very Low Light](https://arxiv.org/abs/1910.11336) |
| Visual tracking | [High-Speed Tracking with Kernelized Correlation Filters](https://arxiv.org/abs/1404.7584) |
| Audio representation | [SoundNet](https://arxiv.org/abs/1610.09001) |
| Paper implementations | [labml.ai annotated PyTorch implementations](https://nn.labml.ai/) |

</details>

## Explanations Worth Keeping Nearby

| Resource | Best use |
| --- | --- |
| [Distill](https://distill.pub/) | Visual, interactive explanations of difficult ML ideas. |
| [Colah's Blog](https://colah.github.io/) | Intuitive neural-network and representation-learning essays. |
| [Andrej Karpathy](https://karpathy.github.io/) | Neural networks, language models, and ML engineering craft. |
| [Sebastian Raschka](https://sebastianraschka.com/blog/) | Careful practical explanations and paper walkthroughs. |
| [Chip Huyen](https://huyenchip.com/blog/) | ML systems, data, inference, and production thinking. |
| [Jay Alammar](https://jalammar.github.io/) | Visual explanations of transformers and language models. |
| [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) | A code-level companion to *Attention Is All You Need*. |

## Curation Principles

A paper belongs here when it satisfies at least two of these tests:

1. It introduced an idea still used or discussed across multiple subfields.
2. It is the clearest available explanation of an important concept.
3. It changed practical system design, evaluation, or deployment.
4. It represents a durable new direction rather than a short-lived leaderboard result.
5. It provides unusually strong documentation, reproducibility, or critical perspective.

Newer does not automatically mean better. A new paper should replace an older one when it teaches
the same lesson more clearly or better represents current practice; otherwise it belongs in a track.
See [CONTRIBUTING.md](CONTRIBUTING.md) before proposing an addition.

## What Changed in 2026

| Decision | Why |
| --- | --- |
| Added an essential 30-paper curriculum | The old list was broad but offered no clear answer to "what should I read first?" |
| Added DeepSeek-R1, TabPFN, SAM 2, OLMo, DiT, Flow Matching, ReAct, FlashAttention, and SWE-bench | These capture durable shifts in reasoning, tabular foundation models, video segmentation, open science, generative modeling, agents, efficient kernels, and realistic evaluation. |
| Added reinforcement learning, causal ML, ML systems, and model evaluation tracks | These were major gaps in a repository claiming broad ML coverage. |
| Rebuilt the recommender track | Classical surveys remain references, while matrix factorization, YouTube, Wide & Deep, DLRM, SASRec, and BERT4Rec form a more useful progression. |
| Moved RNNs, early detectors, captioning papers, and application demos into background sections | They remain historically useful but should not crowd the modern first-pass path. |
| Added a generated progress badge and collapsible tracks | Status markers stay easy to edit, while the README remains scannable as the collection grows. |

## History

| Date | Change |
| --- | --- |
| 2019-10 to 2020-02 | Original collection assembled across data science, ML, deep learning, vision, NLP, GNNs, and recommenders. |
| 2026-08-10 | Re-curated the collection, introduced reading tracks and manual progress tracking, repaired links, and added modern foundation-model literature. |
| 2026-08-10 | Added an essential curriculum, missing ML disciplines, current frontier papers, contribution rules, and generated progress reporting. |

---

<div align="center">

**Read for ideas, not completion.** A paper is valuable when it changes the questions you ask.

</div>
