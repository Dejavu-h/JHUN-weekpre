# End-to-End Referring Video Object Segmentation with Multimodal Transformers

***

## <span style="color: #1B5E20"><span style="background-color: #f1f8e9">💡 Meta Data</span></span>

| <span style="background-color: #dbeedd">Title</span>     | <span style="background-color: #dbeedd">End-to-End Referring Video Object Segmentation with Multimodal Transformers</span>                                                                                                     |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <span style="background-color: #f3faf4">Journal</span>   |                                                                                                                                                                                                                                |
| <span style="background-color: #dbeedd">Authors</span>   | <span style="background-color: #dbeedd">Adam Botach; Evgenii Zheltonozhskii; Chaim Baskin</span>                                                                                                                               |
| <span style="background-color: #f3faf4">Pub. date</span> | <span style="background-color: #f3faf4">2022-04-03</span>                                                                                                                                                                      |
| <span style="background-color: #dbeedd">期刊标签</span>      |                                                                                                                                                                                                                                |
| <span style="background-color: #f3faf4">DOI</span>       | <span style="background-color: #f3faf4"><a href="https://doi.org/10.48550/arXiv.2111.14821" rel="noopener noreferrer nofollow">10.48550/arXiv.2111.14821</a></span>                                                            |
| <span style="background-color: #dbeedd">附件</span>        | <span style="background-color: #dbeedd"><a href="zotero://open-pdf/0_V5DTLZNT" rel="noopener noreferrer nofollow">Botach et al_2022_End-to-End Referring Video Object Segmentation with Multimodal Transformers.pdf</a></span> |

## <span style="color: #E65100"><span style="background-color: #fff8e1">📜 研究背景 &#x26; 基础 &#x26; 目的</span></span>

***

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%221%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%221%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“Referring video object segmentation.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%221%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 1</a></span>)</span> 参考视频对象分割

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%222%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%222%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“Transformers.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%222%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 2</a></span>)</span> 介绍Transformer

## 📌 研究贡献

***

### MTTR

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%222%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%222%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“We present a Transformer-based RVOS framework, dubbed Multimodal Tracking Transformer (MTTR), which models the task as a parallel sequence prediction problem and outputs predictions for all objects in the video prior to selecting the one referred to by the text.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%222%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 2</a></span>)</span> <span style="background-color: #aaaaaa80">我们提出了一个基于Transformer的 RVOS 框架，称为多模态跟踪Transformer (MTTR)，它将任务建模为并行序列预测问题，并在选择文本所指的对象之前输出视频中所有对象的预测结果。</span>

### Temporal segment voting scheme

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%222%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%222%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“Our sequence selection strategy is based on a temporal segment voting scheme, a novel reasoning scheme that allows our model to focus on more relevant parts of the video with regards to the text.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%222%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 2</a></span>)</span> <span style="background-color: #aaaaaa80">我们的序列选择策略基于时间片段投票方案，这是一种新颖的推理方案，可让我们的模型关注视频中与文本更相关的部分。</span>

### End-to-end trainable

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%222%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%222%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“The proposed method is end-to-end trainable, free of text-related inductive bias modules, and requires no additional mask refinement.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%222%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 2</a></span>)</span> <span style="background-color: #aaaaaa80">所提出的方法是端到端可训练的，不存在与文本相关的归纳偏差模块，也不需要额外的掩码改进。</span>

## <span style="color: #2E7D32"><span style="background-color: #f1f8e9">📊 研究内容</span></span>

***

#### Tsak definition

1.  <span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%223%22%2C%22position%22%3A%7B%22pageIndex%22%3A2%2C%22rects%22%3A%5B%5B126.024%2C90.803%2C286.358%2C99.829%5D%2C%5B50.112%2C76.664%2C286.359%2C90.069%5D%2C%5B308.862%2C312.583%2C520.905%2C325.764%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=3">“The input of RVOS consists of a frame sequence V = {vi}iT=1, where vi ∈ RC×H0×W0 , and a text query T = {ti}iL=1, where ti is the ith word in the text.”</a></span>

    <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 3</a></span>)</span>

    <span style="background-color: #aaaaaa80">V为单帧视频信息；T为文本信息，其中ti为第i个单词。</span>

2.  <span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%223%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“Then, for a subset of frames of interest VI ⊆ V of size TI, the goal is to segment the object referred by T in each frame in VI.”</a></span>

    <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 3</a></span>)</span>

    <span style="background-color: #aaaaaa80">然后，对于大小为 T_I 的感兴趣帧子集 V_I ⊆ V，目标是分割 V_I 中每个帧中 T 所指的对象。</span>

#### Feature extraction

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%223%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“deep spatio-temporal encoder.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 3</a></span>)</span> 首先使用deep spation-temproal encoder提取V中的每一帧图像的特征

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%223%22%2C%22position%22%3A%7B%22pageIndex%22%3A2%2C%22rects%22%3A%5B%5B431.466%2C202.446%2C545.11%2C212.658%5D%2C%5B308.862%2C190.83%2C343.016%2C199.737%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=3">“Transformer-based [42] text encoder.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 3</a></span>)</span> 同时使用Transformer based encoder 提取文本特征

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%223%22%2C%22position%22%3A%7B%22pageIndex%22%3A2%2C%22rects%22%3A%5B%5B326.287%2C178.536%2C493.905%2C188.499%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=3">“inearly projected to a shared dimension D”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 3</a></span>)</span> 将两个提取的特征线性投影到D

#### Instnce prediction

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%223%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“TI”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 3</a></span>)</span> 对每个相关帧的特征进行扁平化处理，并分别与文本嵌入进行连接，生成一组 T\_I 多模态序列

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%223%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“exchange information”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 3</a></span>)</span> 互通信息

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%223%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“Then, the decoder layers, which are fed with Nq object queries per input frame, query the multimodal sequences for entity-related information and store it in the object queries.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%223%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 3</a></span>)</span> 解码器层在每个输入帧中输入 Nq 个对象查询，查询多模态序列中与实体相关的信息，并将其存储在对象查询中。

视频中的每一帧共享训练权重，以查询到相同的instance sequence

#### Output generation

使用FPN和动态生成的条件卷积核生成相应的mask

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%224%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%224%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“novel text-reference score function”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%224%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 4</a></span>)</span> 新颖的文本参考评分函数 用此函数来确定对象查询序列与描述对象是否具有强关联性。

#### Multimodal Transformer

对于每个感兴趣的帧，时间编码器生成一个特征图

$$
f_t^{\mathcal{V}_{\mathcal{I}}} \in \mathbb{R}^{H \times W \times C_{\mathcal{V}}}
$$

文本编码器输出语言嵌入向量

$$
f_{\mathcal{T}} \in \mathbb{R}^{L \times D_{\mathcal{T}}}
$$

## <span style="color: #1565C0"><span style="background-color: #e1f5fe">🔬 理论推导</span></span>

***

![\<img alt="" data-attachment-key="R33DKXFV" width="1008" height="686" src="attachments/R33DKXFV.png" ztype="zimage">](attachments/R33DKXFV.png)

### <span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%224%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%224%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“The Instance Segmentation Process”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%224%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 4</a></span>)</span> 实例分割过程。

   给定最后一个Transformer输出的$F_E$ 提取每个序列中和视频相关的部分并将其重塑为$\mathcal{F}_E^{\mathcal{V}_{\mathcal{I}}}$ 将temporal encoder 的前n-1个输出为$\mathcal{F}_B^{\mathcal{1,...,n-1}}$ 通过类似于FPN的spatial decoder将$G_{Seg}$ 进行分层融合。产生语义丰富的高分辨率视频帧特征图$\mathcal{F}_{Seg}$  

$$
\mathcal{F}_{\text {Seg }}=\left\{f_{\text {Seg }}^t\right\}_{t=1}^{T_{\mathcal{I}}}, f_{\text {Seg }}^t \in \mathbb{R}^{D_s \times \frac{H_0}{4} \times \frac{W_0}{4}}



$$

使用双层感知器生成条件分割序列

![\<img alt="" data-attachment-key="PMYF8TGS" width="651" height="86" src="attachments/PMYF8TGS.png" ztype="zimage">](attachments/PMYF8TGS.png)

将每个分割核与其对应的帧特征进行卷积，生成mask ，双线性上采样，将mask调整为grund-truth分辨率。

### <span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%224%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%224%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“Instance Sequence Matching”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%224%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 4</a></span>)</span> 实例序列匹配

首先寻找搜索成本最低的排序![\<img alt="" data-attachment-key="2SSDGZHG" width="703" height="193" src="attachments/2SSDGZHG.png" ztype="zimage">](attachments/2SSDGZHG.png)其中，CMatch 是成对匹配成本。使用匈牙利算法可以高效计算。每个地面实况序列的形式为![\<img alt="" data-attachment-key="DSV3GB98" width="744" height="123" src="attachments/DSV3GB98.png" ztype="zimage">](attachments/DSV3GB98.png)使用一个参考预测头（用$ G_{Ref}$表示），它由一个形状为 D × 2 的线性层和一个 softmax 层组成。给定预测对象查询 q∈$\mathbb{R}^D$ 后，该预测头将 q 作为输入，并输出参考预测结果$\hat{r} \equiv G_{\mathrm{Ref}}(q)$。![\<img alt="" data-attachment-key="7QGKCXXT" width="759" height="129" src="attachments/7QGKCXXT.png" ztype="zimage">](attachments/7QGKCXXT.png)

匹配函数成本为以下函数总和

![\<img alt="" data-attachment-key="6EZEH2KD" width="1024" height="104" src="attachments/6EZEH2KD.png" ztype="zimage">](attachments/6EZEH2KD.png)

CRef 利用相应的地面实况序列对参考预测进行监督，具体如下![\<img alt="" data-attachment-key="RWHCYCUV" width="661" height="218" src="attachments/RWHCYCUV.png" ztype="zimage">](attachments/RWHCYCUV.png)

### <span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%225%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%225%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“Loss Functions”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%225%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 5</a></span>)</span> 损失函数

![\<img alt="" data-attachment-key="TV36XWMP" width="1013" height="102" src="attachments/TV36XWMP.png" ztype="zimage">](attachments/TV36XWMP.png)

#### L\_mask被定义为Dice和每个像素Focal损失函数的组合

![\<img alt="" data-attachment-key="DLW8272J" width="980" height="89" src="attachments/DLW8272J.png" ztype="zimage">](attachments/DLW8272J.png)

L\_Dice 和 L\_Focal 在每个时间步长都会应用于相应的掩码，并根据训练批次中的实例数量进行归一化处理。

#### L\_Ref为交叉熵用于监督序列参考预测

![\<img alt="" data-attachment-key="M232LXUF" width="748" height="175" src="attachments/M232LXUF.png" ztype="zimage">](attachments/M232LXUF.png)

### <span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%225%22%2C%22position%22%3A%7B%22rects%22%3A%5B%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%225%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=NaN">“Inference”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%225%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 5</a></span>)</span>

#### 输出R

#### 给定参考预测值的positive类别概率

#### 返回分段掩码序列和其得分

![\<img alt="" data-attachment-key="SCPY2QE3" width="621" height="186" src="attachments/SCPY2QE3.png" ztype="zimage">](attachments/SCPY2QE3.png)

将这种序列选择方案称为 "时间片段投票方案"（TSVS），它根据每个预测序列的术语与文本所指对象的总关联度对其进行分级。

## <span style="color: #4A148C"><span style="background-color: #f5f5f5">🚩 实验结果</span></span>

***

### 数据集

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%225%22%2C%22position%22%3A%7B%22pageIndex%22%3A4%2C%22rects%22%3A%5B%5B328.519%2C126.669%2C485.794%2C135.576%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%225%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=5">“A2D-Sentences and JHMDB-Sentences”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%225%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 5</a></span>)</span>在数据集上添加文本注释

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%226%22%2C%22position%22%3A%7B%22pageIndex%22%3A5%2C%22rects%22%3A%5B%5B263.28%2C172.223%2C288.02%2C181.13%5D%2C%5B49.534%2C160.268%2C140.777%2C169.175%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=6">“ReferYouTube-VOS dataset”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 6</a></span>)</span>每段视频每五帧都有像素级实例分割注释。

### 精度估计方法

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%226%22%2C%22position%22%3A%7B%22pageIndex%22%3A5%2C%22rects%22%3A%5B%5B49.644%2C365.334%2C288.016%2C374.241%5D%2C%5B50.112%2C353.379%2C180.385%2C362.286%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=6">“We adopt Overall IoU, Mean IoU, and precision@K to evaluate our method on these datasets.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 6</a></span>)</span>我们在这些数据集上采用总体 IoU、平均 IoU 和精度@K 来评估我们的方法。

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%226%22%2C%22position%22%3A%7B%22pageIndex%22%3A5%2C%22rects%22%3A%5B%5B183.477%2C353.379%2C286.362%2C362.286%5D%2C%5B50.112%2C341.424%2C286.357%2C350.331%5D%2C%5B50.112%2C329.468%2C145.822%2C338.375%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=6">“Overall IoU computes the ratio between the total intersection and the total union area over all the test samples.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 6</a></span>)</span>总体 IoU 计算的是所有测试样本的总交叉面积与总结合面积之间的比率。

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%226%22%2C%22position%22%3A%7B%22pageIndex%22%3A5%2C%22rects%22%3A%5B%5B148.87%2C329.468%2C286.53%2C338.375%5D%2C%5B50.112%2C317.513%2C128.315%2C326.42%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=6">“Mean IoU is the averaged IoU over all the test samples.”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 6</a></span>)</span>

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%226%22%2C%22position%22%3A%7B%22pageIndex%22%3A5%2C%22rects%22%3A%5B%5B131.439%2C317.513%2C286.362%2C326.42%5D%2C%5B50.112%2C305.558%2C287.605%2C314.465%5D%2C%5B49.753%2C293.264%2C188.409%2C303.476%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=6">“Precision@K considers the percentage of test samples whose IoU scores are <span style="background-color: #5fb23680">above a threshold K</span>, where K ∈ [0.5, 0.6, 0.7, 0.8, 0.9].”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 6</a></span>)</span>

<span class="highlight" data-annotation="%7B%22attachmentURI%22%3A%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FV5DTLZNT%22%2C%22pageLabel%22%3A%226%22%2C%22position%22%3A%7B%22pageIndex%22%3A5%2C%22rects%22%3A%5B%5B469.364%2C281.648%2C546.766%2C290.555%5D%2C%5B308.862%2C269.693%2C545.115%2C278.6%5D%2C%5B308.862%2C257.398%2C505.838%2C267.61%5D%5D%7D%2C%22citationItem%22%3A%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%7D" ztype="zhighlight"><a href="zotero://open-pdf/library/items/V5DTLZNT?page=6">“The primary evaluation metrics for this dataset are the average of the region similarity (J ) and the contour accuracy (F) [35].”</a></span> <span class="citation" data-citation="%7B%22citationItems%22%3A%5B%7B%22uris%22%3A%5B%22http%3A%2F%2Fzotero.org%2Fusers%2F12078481%2Fitems%2FJJNC6MMR%22%5D%2C%22locator%22%3A%226%22%7D%5D%2C%22properties%22%3A%7B%7D%7D" ztype="zcitation">(<span class="citation-item"><a href="zotero://select/library/items/JJNC6MMR">Botach 等, 2022, p. 6</a></span>)</span>该数据集的主要评估指标是区域相似度（J）和轮廓精度（F）的平均值 \[35]。

### 具体实施

#### 预训练

我们使用最小的（"微小"）视频 Swin 变换器 \[28] 作为时态编码器，并在 Kinetics-400 \[17] 上进行了预训练。只用swin transformer的前三个区块 第三个区块作为多模态transformer

#### 参数

w=8/w=12

320×576/360×640

#### 比较

![\<img alt="" data-attachment-key="QBYJ2TW3" width="1109" height="869" src="attachments/QBYJ2TW3.png" ztype="zimage">](attachments/QBYJ2TW3.png)
