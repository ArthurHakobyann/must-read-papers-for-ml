# Must-Read Papers for Machine Learning

A curated reading map for data science, machine learning, deep learning, and modern foundation models.

The goal is not to list every famous paper. It is to keep a compact path through ideas that still shape practice: statistical thinking, optimization, tree models, neural networks, transformers, LLMs, retrieval, vision, recommenders, interpretability, and responsible ML.

## How to use this list

| Mark | Meaning |
| --- | --- |
| `- [ ]` | Not read yet. Change to `- [x]` when done. |
| `Core` | Read this first. Foundational or unusually high leverage. |
| `Deepen` | Read after the core papers in that area. |
| `Classic` | Historically important; still useful context, but not always current practice. |
| `Survey` | Good map of a subfield. |
| `Modern` | Important post-2020 update. |

Tip: for each paper, write a one-line note in the `Notes` column after reading it. This keeps progress manual, portable, and GitHub-friendly.

## Fast Tracks

| Goal | Suggested path |
| --- | --- |
| Data science foundations | Tidy Data -> Two Cultures -> Frequentism and Bayesianism -> Model Evaluation |
| Classical ML practice | Model Evaluation -> XGBoost -> LightGBM -> Bayesian Optimization -> ICE plots |
| Deep learning foundations | Deep Learning review -> Matrix Calculus -> Dropout -> BatchNorm -> Adam -> ResNet |
| Modern NLP and LLMs | Attention -> BERT -> GPT-3 -> Scaling Laws -> Chinchilla -> InstructGPT -> RAG -> DPO |
| Modern vision/generation | AlexNet -> ResNet -> ViT -> CLIP -> DDPM -> Latent Diffusion -> Segment Anything |
| Recommender systems | Collaborative Filtering survey -> Netflix -> Amazon -> Deep recommender survey -> Explainable recommendation |

---

## Data Science and Statistical Thinking

### Preprocessing and EDA

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf) | A clean mental model for tabular data organization and reproducible analysis. |  |

### Modeling Culture and Uncertainty

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [Statistical Modeling: The Two Cultures](https://projecteuclid.org/download/pdf_1/euclid.ss/1009213726) | Explains the split between data modeling and algorithmic modeling. Still one of the best framing papers for ML practitioners. |  |
| - [ ] | Core | [Frequentism and Bayesianism: A Python-driven Primer](https://arxiv.org/pdf/1411.5018.pdf) | Practical introduction to two major statistical worldviews. |  |
| - [ ] | Deepen | [A Study in Rashomon Curves and Volumes](https://arxiv.org/pdf/1908.01755.pdf) | Useful for thinking about model simplicity, multiplicity, and why many models can fit the same data well. |  |

### Model Evaluation

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning](https://arxiv.org/pdf/1811.12808.pdf) | Strong practical guide to validation, selection, and evaluation traps. |  |
| - [x] | Classic | [A Brief Introduction into Machine Learning](https://events.ccc.de/congress/2004/fahrplan/files/105-machine-learning-paper.pdf) | Good historical overview. Kept as read, but no longer the best first ML introduction. |  |
| - [ ] | Deepen | [On Model Stability as a Function of Random Seed](https://arxiv.org/pdf/1909.10447) | Shows why single-run results can mislead. |  |

---

## Classical Machine Learning

### Boosting and Tree Ensembles

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [Greedy Function Approximation: A Gradient Boosting Machine](https://projecteuclid.org/download/pdf_1/euclid.aos/1013203451) | The conceptual foundation behind gradient boosting. |  |
| - [ ] | Core | [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/pdf/1603.02754.pdf) | Still central for tabular ML and production baselines. |  |
| - [ ] | Core | [LightGBM: A Highly Efficient Gradient Boosting Decision Tree](https://papers.nips.cc/paper/6907-lightgbm-a-highly-efficient-gradient-boosting-decision-tree.pdf) | Explains speed and scale improvements used heavily in practice. |  |
| - [ ] | Classic | [AdaBoost and the Super Bowl of Classifiers](http://www.inf.fu-berlin.de/inst/ag-ki/adaboost4.pdf) | Friendly tutorial on boosting before modern gradient boosted trees. |  |

### Dimensionality Reduction

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [A Tutorial on Principal Component Analysis](https://arxiv.org/pdf/1404.1100.pdf) | PCA remains essential for data understanding and linear algebra intuition. |  |
| - [ ] | Core | [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) | Best practical explanation of t-SNE interpretation pitfalls. |  |
| - [ ] | Deepen | [Visualizing Data using t-SNE](https://lvdmaaten.github.io/publications/papers/JMLR_2008.pdf) | Original method paper. |  |

### Optimization and Search

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [A Tutorial on Bayesian Optimization](https://arxiv.org/abs/1807.02811) | Practical starting point for expensive black-box optimization. |  |
| - [ ] | Deepen | [Taking the Human Out of the Loop: A Review of Bayesian Optimization](https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf) | Broader survey of automated model search and experiment design. |  |
| - [ ] | Deepen | [An Introduction to the Conjugate Gradient Method Without the Agonizing Pain](http://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf) | Excellent optimization math explainer. |  |

### Anomaly Detection

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Survey | [Outlier Detection: A Survey](https://pdfs.semanticscholar.org/912b/0b7879ca99bf654a26bbb0d50d4b8e0ed6c0.pdf) | Kept as a broad classical overview. Pair with newer domain-specific papers when needed. |  |

---

## Interpretability, Data Value, and Responsible ML

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [Peeking Inside the Black Box: Individual Conditional Expectation Plots](https://arxiv.org/pdf/1309.6392.pdf) | Practical interpretability technique that remains useful for tabular models. |  |
| - [ ] | Core | [Data Shapley: Equitable Valuation of Data for Machine Learning](https://arxiv.org/pdf/1904.02868.pdf) | Important framing for data valuation and dataset contribution. |  |
| - [ ] | Modern | [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258) | Defines the foundation-model framing and its technical/social risks. |  |

Recommended talk: [Cynthia Rudin's KDD 2019 keynote](https://youtu.be/wL4X4lG20sM)

---

## Deep Learning Foundations

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [The Matrix Calculus You Need For Deep Learning](https://arxiv.org/pdf/1802.01528.pdf) | Makes backpropagation math much less mysterious. |  |
| - [x] | Core | [Deep Learning](https://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf) | Classic LeCun, Bengio, and Hinton review. Still the best historical overview. |  |
| - [ ] | Core | [Dropout: A Simple Way to Prevent Neural Networks from Overfitting](https://www.cs.toronto.edu/~hinton/absps/JMLRdropout.pdf) | Classic regularization paper. |  |
| - [ ] | Core | [Batch Normalization](https://arxiv.org/pdf/1502.03167v3) | Foundational normalization paper. |  |
| - [ ] | Core | [Adam: A Method for Stochastic Optimization](https://arxiv.org/pdf/1412.6980) | Still a default optimizer baseline and worth understanding. |  |
| - [ ] | Deepen | [Generalization in Deep Learning](https://arxiv.org/pdf/1710.05468.pdf) | Useful theory context for why deep nets generalize. |  |
| - [ ] | Deepen | [AutoML: A Survey of the State-of-the-Art](https://arxiv.org/pdf/1908.00709v1) | Good survey, but newer AutoML systems have evolved; treat as background. |  |

---

## Transformers, NLP, and LLMs

### Core Transformer Era

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [x] | Core | [Attention Is All You Need](https://arxiv.org/pdf/1706.03762) | The transformer paper. Read before almost everything modern. |  |
| - [ ] | Core | [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805) | Key encoder-only pretraining paper. |  |
| - [ ] | Classic | [A Primer on Neural Network Models for Natural Language Processing](https://arxiv.org/pdf/1510.00726.pdf) | Great pre-transformer neural NLP map. |  |
| - [ ] | Classic | [LSTM: A Search Space Odyssey](https://arxiv.org/pdf/1503.04069.pdf) | Good if you want RNN/LSTM context before transformers. |  |
| - [ ] | Classic | [Empirical Evaluation of Gated Recurrent Neural Networks on Sequence Modeling](https://arxiv.org/pdf/1412.3555.pdf) | Kept for historical sequence-model context. |  |

### Modern LLMs and Alignment

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Modern | [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | GPT-3 paper; made prompting and few-shot use central. |  |
| - [ ] | Modern | [Scaling Laws for Neural Language Models](https://arxiv.org/abs/2001.08361) | Explains empirical scaling behavior for LMs. |  |
| - [ ] | Modern | [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) | Chinchilla paper; corrected the field's intuition about model size versus tokens. |  |
| - [ ] | Modern | [Training Language Models to Follow Instructions with Human Feedback](https://arxiv.org/abs/2203.02155) | InstructGPT/RLHF paper; key for assistant-style LLMs. |  |
| - [ ] | Modern | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) | Foundational prompting paper for reasoning tasks. |  |
| - [ ] | Modern | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | Core RAG paper; important for factual, source-grounded generation. |  |
| - [ ] | Modern | [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685) | Efficient fine-tuning method used across modern LLM workflows. |  |
| - [ ] | Modern | [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314) | Makes large-model fine-tuning feasible on much smaller hardware. |  |
| - [ ] | Modern | [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) | Simpler alternative to PPO-style RLHF for preference tuning. |  |
| - [ ] | Modern | [Constitutional AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073) | Important RLAIF/alignment paper. |  |
| - [ ] | Modern | [LLaMA: Open and Efficient Foundation Language Models](https://arxiv.org/abs/2302.13971) | Important open-weights foundation-model milestone. |  |
| - [ ] | Modern | [Mixtral of Experts](https://arxiv.org/abs/2401.04088) | Strong sparse mixture-of-experts reference. |  |
| - [ ] | Modern | [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) | Important non-transformer sequence-model direction for long contexts. |  |

---

## Computer Vision and Multimodal Learning

### CNNs and Detection

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) | AlexNet; the modern deep vision turning point. |  |
| - [ ] | Core | [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385) | ResNet; still a core architecture idea. |  |
| - [ ] | Deepen | [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/pdf/1409.1556v6.pdf) | VGG; useful architecture history. |  |
| - [ ] | Classic | [R-CNN](https://arxiv.org/pdf/1311.2524.pdf) | Historical detection foundation. |  |
| - [ ] | Classic | [Fast R-CNN](https://arxiv.org/pdf/1504.08083.pdf) | Detection pipeline improvement. |  |
| - [ ] | Core | [Faster R-CNN](https://arxiv.org/pdf/1506.01497v3.pdf) | Still important for understanding two-stage detectors. |  |
| - [ ] | Core | [Mask R-CNN](https://arxiv.org/pdf/1703.06870.pdf) | Key instance-segmentation model. |  |
| - [ ] | Classic | [YOLO: You Only Look Once](https://arxiv.org/pdf/1506.02640) | One-stage detection milestone. |  |
| - [ ] | Classic | [Microsoft COCO: Common Objects in Context](https://arxiv.org/pdf/1405.0312) | Dataset paper behind much of modern detection/segmentation evaluation. |  |
| - [ ] | Modern | [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872) | DETR; reframed detection as set prediction with transformers. |  |

### Vision Transformers, Multimodal Models, and Segmentation

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Modern | [An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929) | Vision Transformer paper; essential for modern vision. |  |
| - [ ] | Modern | [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | CLIP; central for zero-shot vision and image-text models. |  |
| - [ ] | Modern | [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193) | Strong modern self-supervised vision representation paper. |  |
| - [ ] | Modern | [Segment Anything](https://arxiv.org/abs/2304.02643) | Promptable segmentation and a major vision foundation-model reference. |  |

### Image Captioning and Vision-Language Classics

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Classic | [Show and Tell: A Neural Image Caption Generator](https://arxiv.org/abs/1411.4555) | Early neural captioning baseline. |  |
| - [ ] | Classic | [Show, Attend and Tell](https://arxiv.org/abs/1502.03044) | Visual attention for captioning. |  |
| - [ ] | Classic | [Neural Machine Translation by Jointly Learning to Align and Translate](https://arxiv.org/pdf/1409.0473v7) | Attention before transformers; still valuable context. |  |

---

## Generative Models

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [Generative Adversarial Nets](https://arxiv.org/pdf/1406.2661v1.pdf) | Original GAN paper. |  |
| - [ ] | Modern | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | Core diffusion-model paper. |  |
| - [ ] | Modern | [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752) | Latent diffusion; key text-to-image generation foundation. |  |

Rabbit hole: [GAN Papers](https://github.com/zhangqianhui/AdversarialNetsPapers)

---

## Graph Neural Networks

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Survey | [A Comprehensive Survey on Graph Neural Networks](https://arxiv.org/pdf/1901.00596.pdf) | Broad GNN overview. Kept as a starting survey rather than a complete modern GNN path. |  |

---

## Recommender Systems

### Surveys and Foundations

| Status | Priority | Paper | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [A Survey of Collaborative Filtering Techniques](http://downloads.hindawi.com/archive/2009/421425.pdf) | Classical collaborative-filtering overview. |  |
| - [ ] | Core | [Collaborative Filtering Recommender Systems](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.130.4520&rep=rep1&type=pdf) | Another strong classical recommender reference. |  |
| - [ ] | Survey | [Deep Learning Based Recommender System: A Survey and New Perspectives](https://arxiv.org/abs/1707.07435) | Replaced the old Sci-Hub link with an arXiv-accessible version. |  |
| - [ ] | Survey | [Explainable Recommendation: A Survey and New Perspectives](https://arxiv.org/abs/1804.11192) | Useful bridge between recommendation quality and interpretability. |  |

### Industry Case Studies

| Status | Priority | Paper / Article | Why read it | Notes |
| --- | --- | --- | --- | --- |
| - [ ] | Core | [The Netflix Recommender System](https://dl.acm.org/doi/10.1145/2843948) | Business and system view of recommendation at scale. |  |
| - [ ] | Core | [Two Decades of Recommender Systems at Amazon.com](https://pdfs.semanticscholar.org/0f06/d328f6deb44e5e67408e0c16a8c7356330d1.pdf) | Classic Amazon case study. |  |
| - [ ] | Deepen | [Netflix Recommendations: Beyond the 5 Stars](https://netflixtechblog.com/netflix-recommendations-beyond-the-5-stars-part-1-55838468f429) | More readable product/engineering context. |  |
| - [ ] | Deepen | [How Does Spotify Know You So Well?](https://medium.com/s/story/spotifys-discover-weekly-how-machine-learning-finds-your-new-music-19a41ab76efe) | Product-facing recommender explanation. |  |

Book: [Recommender Systems Handbook](https://www.amazon.com/Recommender-Systems-Handbook-Francesco-Ricci/dp/1489976361)

---

## Specialized and Applied Areas

These are useful rabbit holes, but they are no longer part of the core first-pass reading path.

| Area | Papers and resources |
| --- | --- |
| Medical AI | [Machine learning classifiers and fMRI: a tutorial overview](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2892746/pdf/nihms100405.pdf) |
| Pose detection | [DensePose](https://arxiv.org/pdf/1802.00434v1.pdf), [Parsing R-CNN](https://arxiv.org/pdf/1811.12596v1.pdf) |
| Creative AI | [Creative Adversarial Networks](https://arxiv.org/pdf/1706.07068), [Deep Painterly Harmonization](https://arxiv.org/pdf/1804.03189), [Everybody Dance Now](https://arxiv.org/pdf/1808.07371) |
| Low-light photography | [Handheld Mobile Photography in Very Low Light](https://arxiv.org/pdf/1910.11336v1) |
| Scene recognition | [Learning Deep Features for Scene Recognition using Places Database](http://places.csail.mit.edu/places_NIPS14.pdf) |
| Tracking | [High-Speed Tracking with Kernelized Correlation Filters](https://arxiv.org/pdf/1404.7584) |
| Audio | [SoundNet](http://soundnet.csail.mit.edu/) |
| Implementations | [labml.ai Annotated PyTorch Paper Implementations](https://nn.labml.ai/) |

---

## Blogs and Learning Resources

| Resource | Best for |
| --- | --- |
| [Distill](https://distill.pub/) | Visual explanations of ML concepts. |
| [Colah's Blog](http://colah.github.io/) | Intuitive deep learning explanations. |
| [Andrej Karpathy](https://karpathy.github.io/) | Neural networks, software, and ML craft. |
| [Sebastian Raschka](https://sebastianraschka.com/blog/index.html) | Practical ML and deep learning. |
| [Chip Huyen](https://huyenchip.com/blog/) | ML systems and production thinking. |
| [Sebastian Ruder](https://ruder.io/) | NLP and transfer learning. |
| [Jay Alammar](http://jalammar.github.io/) | Visual transformer/NLP explanations. |
| [Stanford UFLDL Tutorial](http://ufldl.stanford.edu/tutorial/) | Older but useful deep learning basics. |

---

## Changes in This Refresh

### Added because the field changed

- Foundation models: [On the Opportunities and Risks of Foundation Models](https://arxiv.org/abs/2108.07258)
- LLM scaling and training: [Scaling Laws](https://arxiv.org/abs/2001.08361), [Chinchilla](https://arxiv.org/abs/2203.15556), [GPT-3](https://arxiv.org/abs/2005.14165)
- LLM behavior and adaptation: [InstructGPT](https://arxiv.org/abs/2203.02155), [Chain-of-Thought](https://arxiv.org/abs/2201.11903), [LoRA](https://arxiv.org/abs/2106.09685), [QLoRA](https://arxiv.org/abs/2305.14314), [DPO](https://arxiv.org/abs/2305.18290), [Constitutional AI](https://arxiv.org/abs/2212.08073)
- Retrieval: [RAG](https://arxiv.org/abs/2005.11401)
- Modern vision: [ViT](https://arxiv.org/abs/2010.11929), [CLIP](https://arxiv.org/abs/2103.00020), [DETR](https://arxiv.org/abs/2005.12872), [DINOv2](https://arxiv.org/abs/2304.07193), [Segment Anything](https://arxiv.org/abs/2304.02643)
- Modern generative modeling: [DDPM](https://arxiv.org/abs/2006.11239), [Latent Diffusion](https://arxiv.org/abs/2112.10752)
- New architecture directions: [Mamba](https://arxiv.org/abs/2312.00752), [Mixtral](https://arxiv.org/abs/2401.04088)

### Demoted from core to classic/background

- Many RNN, GRU, LSTM, CNN-for-sentence-classification, capsule-network, and early image-captioning papers are still historically useful, but transformers and foundation models are now the center of most modern NLP and multimodal practice.
- Several older “cool stuff” application papers were moved into a specialized section so they do not distract from the main learning path.
- The old GPT-2 Papers with Code link was replaced by GPT-3, scaling, instruction tuning, and preference-optimization papers because they better represent the current LLM era.

### Link and maintenance cleanup

- Replaced ad hoc repeated checkmarks with standard Markdown task boxes.
- Replaced the recommender survey Sci-Hub link with a maintainable arXiv-style link.
- Fixed several typos, duplicated links, and inconsistent formatting.
- Converted long emoji-heavy lists into tables that are easier to scan and edit.

---

## Original Changelog

| Date | Change |
| --- | --- |
| 2019-10-28 | Started `must-read-papers-for-ml` repo. |
| 2019-10-29 | Added Analytics Vidhya use-case study links. |
| 2019-10-30 | Added anomaly detection, boosting, CNN, object detection, NLP, and image-captioning papers. |
| 2019-10-31 | Added famous ML/deep-learning blogs. |
| 2019-11-01 | Fixed Markdown issues and added contribution guidance. |
| 2019-11-20 | Added recommender surveys and papers. |
| 2019-12-12 | Added R-CNN variants, pose papers, and GNNs. |
| 2020-02-23 | Added GRU paper. |
| 2026-08-10 | Refreshed curation, added modern foundation-model papers, and redesigned README with manual read tracking. |
