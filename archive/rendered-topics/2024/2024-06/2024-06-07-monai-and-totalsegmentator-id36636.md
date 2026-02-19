---
topic_id: 36636
title: "Monai And Totalsegmentator"
date: 2024-06-07
url: https://discourse.slicer.org/t/36636
---

# MONAI and TotalSegmentator

**Topic ID**: 36636
**Date**: 2024-06-07
**URL**: https://discourse.slicer.org/t/monai-and-totalsegmentator/36636

---

## Post #1 by @khajta (2024-06-07 08:27 UTC)

<p>What is the difference between using MONAI Auto3DSeg and TotalSegmentor for automatic segmentation? There is also TotalSegmentator in MONAI Auto3DSeg.</p>

---

## Post #2 by @pieper (2024-06-07 09:56 UTC)

<p>That’s a good point and I can see why there’s confusion.  TotalSegmentator refers to both the ground-truth dataset and the nnU-Net based model trained on that data.  Since the data was released freely, the team working on MONAI Auto3DSeg also trained a model using that data.  For most purposes they should give very similar results, although the memory usage and GPU efficiency might be different.</p>
<p>I don’t think anyone has done an exhaustive comparison, and in fact both tools are evolving rapidly so you should maybe try both and see what works best for you.  Report back if you learn anything interesting.</p>

---

## Post #3 by @mangotee (2024-06-07 10:13 UTC)

<p>Hi <a class="mention" href="/u/khajta">@khajta</a>,</p>
<p>that’s a great question. I’m gonna answer it a bit more detailed manner, perhaps this will also help others who have questions in this direction. Pinging also <a class="mention" href="/u/diazandr3s">@diazandr3s</a> for his opinion. And I just saw that <a class="mention" href="/u/pieper">@pieper</a> just posted an answer as well, much more concise, but I already typed everything, so I’m also gonna send it <img src="https://emoji.discourse-cdn.com/twitter/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
<p>First of all, TotalSegmentator is two things (as Steven said): a dataset and a model. Important to keep the 2 apart.</p>
<p>When TotalSegmentator came out, the authors released both the data and the pre-trained model under the same name. The model was trained with <a href="https://github.com/MIC-DKFZ/nnUNet" rel="noopener nofollow ugc">nnUnet</a> - in case you’re not familiar with it, it’s an automatic model training framework, highly sophisticated and still state-of-the-art. nnUnet is a custom framework based on PyTorch which was built by researchers from German Cancer Research Center (DKFZ)/Helmholtz Research.</p>
<p>The dataset was also used to train a model with <a href="https://github.com/Project-MONAI/tutorials/tree/main/auto3dseg" rel="noopener nofollow ugc">Auto3DSeg</a>. This tool is <em>also</em> an automatic model training framework, but built on top of the <a href="https://monai.io/" rel="noopener nofollow ugc">MONAI</a> ecosystem. It was inspired by nnUnet and fulfills a similar purpose, but it is using native MONAI transforms, dataloaders, models, training/inference workflows etc.To my knowledge, there is no open-source model yet which was trained with Auto3DSeg on TotalSegmentator data. If you know one, please send me the link, happy to look into it.</p>
<p>However, there is a model which was trained with <a href="https://github.com/project-monai/monailabel" rel="noopener nofollow ugc">MONAI Label</a> on TotalSegmentator <em>data</em>. This model is available in the MONAI Model Zoo, it is called <a href="https://github.com/Project-MONAI/model-zoo/tree/dev/models/wholeBody_ct_segmentation" rel="noopener nofollow ugc">wholeBody_ct_segmentation</a>. MONAI Label is a third tool which you can freely use. It’s purpose is slightly different: while Auto3DSeg and nnUnet assume that you already have annotated data (images+segmentations), MONAI Label assumes that you only very few segmentations. It provides you with an online model training framework, with which you can simultaneously annotate data in batches, and incrementally train a model to get better and better at supporting you during the annotation. Important to note: the purpose of MONAI Label is <em>not</em> to train models that achieve challenge-winning performance - this would require cross-validation, ensembling, HPO etc (these things are done under the hood in nnUnet/Auto3DSeg). The focus is rather interactive annotation via integration into UI frontends like Slicer. But the models are still good enough to help you annotate.</p>
<p>If you’re asking which model/tool to use:</p>
<ul>
<li><strong>nnUnet:</strong> Allows you to train and run inference on state-of-the-art models. You can get to the level of challenge-winning accuracy with very little effort. It assumes you have annotated training data. The official model trained on and shipped with the TotalSegmentator data is the reference model, and should be used for comparisons and benchmarks.</li>
<li><strong>Auto3DSeg:</strong> Another auto-training framework, with similar performance and ease of use as nnUnet, but natively in the MONAI ecosystem (and as Steven said, different optimization of memory/GPU usage). To my knowledge, there’s no open-source model yet trained on TotalSegmentator data, but given sufficient compute, it would be easy to do so.</li>
<li><strong>MONAI Label:</strong> Great tool to help you use AI assistance to interactively annotate your data, or quickly train models and view their performance in 3D Slicer. The model performance will likely not reach the quality of nnUnet/Auto3DSeg model ensembles though.</li>
</ul>
<p>By the way, you don’t even have to decide between nnUnet and MONAI - there’s a <a href="https://github.com/Project-MONAI/tutorials/tree/main/nnunet" rel="noopener nofollow ugc">MONAI wrapper</a> of the nnUnet API, which allows you to trigger training and inference of nnUnet models directly from MONAI.</p>

---

## Post #4 by @khajta (2024-06-07 11:47 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/mangotee">@mangotee</a> Thank you for your great information.</p>

---

## Post #5 by @mau_igna_06 (2024-06-07 12:16 UTC)

<p>Very nice summary</p>
<aside class="quote no-group" data-username="mangotee" data-post="3" data-topic="36636">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>To my knowledge, there’s no open-source model yet trained on TotalSegmentator data, but given sufficient compute, it would be easy to do so.</p>
</blockquote>
</aside>
<p>Apparently, a <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/blob/74e0f79bf96a8e67b7f6c2b98dd143cf7f7e570b/MONAIAuto3DSeg/Resources/Models.json#L618-L628" rel="noopener nofollow ugc">Auto3DSeg model</a> was indeed trained with TotalSegmentator data</p>

---

## Post #6 by @khajta (2024-06-08 04:37 UTC)

<p>I have one more question. If I have CT dataset and I would like the to obtain the organ segmentation information for evaluating the absorbed dose, is it the same result using nnUnet, Auto3DSeg, or MONAI Label?</p>

---

## Post #7 by @pieper (2024-06-08 20:45 UTC)

<aside class="quote no-group" data-username="khajta" data-post="6" data-topic="36636">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/khajta/48/76581_2.png" class="avatar"> khajta:</div>
<blockquote>
<p>is it the same result using nnUnet, Auto3DSeg, or MONAI Label</p>
</blockquote>
</aside>
<p>What I meant in my answer above is that I don’t think anyone has researched that yet.  If the answer is important to you, then you should run the experiment.  Please report back what you learn.</p>

---

## Post #8 by @diazandr3s (2024-06-17 10:11 UTC)

<p>Good question, <a class="mention" href="/u/khajta">@khajta</a>.</p>
<p>And great answers already from <a class="mention" href="/u/pieper">@pieper</a>  and <a class="mention" href="/u/mangotee">@mangotee</a>.</p>
<p>I’d like to comment on this part:</p>
<blockquote>
<p>To my knowledge, there is no open-source model yet which was trained with Auto3DSeg on TotalSegmentator data. If you know one, please send me the link, happy to look into it.</p>
</blockquote>
<p>We trained the Autro3DSeg on both TotalSegmentator V1 and TotalSegmentator V2 and made available on the Slicer MONAI Auto3DSeg: <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg" class="inline-onebox" rel="noopener nofollow ugc">GitHub - lassoan/SlicerMONAIAuto3DSeg: Extension for 3D Slicer for running MONAI Auto3DSeg models</a></p>
<p>Please download the latest Slicer and install the Auto3DSeg via the Extension Manager.</p>
<p>It’d be great to hear your thoughts on these models <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Hope this helps,</p>

---

## Post #9 by @Sandra_Garcia (2024-06-29 07:34 UTC)

<p>Hi! Taking advantage of what you have mentioned about this, both <a class="mention" href="/u/pieper">@pieper</a> and <a class="mention" href="/u/mangotee">@mangotee</a> , I wanted to ask you a question.</p>
<p>First, I want to say that I don’t know much about this topic. But this question came to mind and I wanted to ask you.</p>
<p>Why are the segmentation results obtained from both TotalSegmentator and Monai Auto3dSeg not completely identical? I understand that if they are trained with the same data, they should offer identical results… But as I said, this topic is not my strong suit and maybe I am wrong.</p>
<p>I have been testing both, and there is a very small variation, but there is a variation in the results.</p>
<p>I look forward to your response, and thank you in advance.</p>

---

## Post #10 by @lassoan (2024-07-02 02:25 UTC)

<aside class="quote no-group" data-username="Sandra_Garcia" data-post="9" data-topic="36636">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sandra_garcia/48/77036_2.png" class="avatar"> Sandra_Garcia:</div>
<blockquote>
<p>Why are the segmentation results obtained from both TotalSegmentator and Monai Auto3dSeg not completely identical?</p>
</blockquote>
</aside>
<p>These are two different models (nnunet/segresnet), trained on not exactly the same data, so it is pretty amazing that they provide so similar results.</p>

---
