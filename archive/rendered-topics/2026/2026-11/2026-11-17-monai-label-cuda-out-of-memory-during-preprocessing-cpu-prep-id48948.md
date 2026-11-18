---
topic_id: 48948
title: "MONAI Label, CUDA Out of Memory during preprocessing: CPU preprocessing and scalable training"
date: 2026-11-17
url: https://discourse.slicer.org/t/48948
last_bumped: 2026-11-17T22:21:10.132Z
---

# MONAI Label, CUDA Out of Memory during preprocessing: CPU preprocessing and scalable training

**Topic ID**: 48948
**Date**: 2026-11-17
**URL**: https://discourse.slicer.org/t/monai-label-cuda-out-of-memory-during-preprocessing-cpu-preprocessing-and-scalable-training/48948

---

## Post #1 by @RDLmomo (2026-11-17 20:53 UTC)

<p>Hi everyone,</p>
<p>I’m using MONAI Label Radiology with 3D Slicer to train a custom 3D medical image segmentation model.</p>
<p>During dataset loading, the process stopped before training started with the following error:</p>
<pre><code class="lang-plaintext">torch.cuda.OutOfMemoryError:
CUDA out of memory.
Tried to allocate 1.45 GiB.

RuntimeError:
applying transform Spacingd
</code></pre>
<p>I’m currently using <code>SmartCacheDataset</code> with a <strong>training batch size of 1</strong>.</p>
<p>I suspect that preprocessing is being performed on the GPU, causing excessive VRAM consumption.</p>
<p>My proposed solution would be:</p>
<ol>
<li>
<p>Move preprocessing operations (particularly <code>Spacingd</code>) to the CPU by changing <code>EnsureTyped(..., device=context.device)</code> to <code>device="cpu"</code> in <code>segmentation.py</code>.</p>
</li>
<li>
<p>Keep the actual model training on the GPU.</p>
</li>
<li>
<p>Initially test with the standard <code>Dataset</code> implementation to verify that training can run successfully.</p>
</li>
<li>
<p>Consider switching to <code>PersistentDataset</code> for disk-based caching instead of <code>SmartCacheDataset</code>.</p>
</li>
<li>
<p>Optimize caching, batch size, and data-loading settings to support a progressively growing dataset.</p>
</li>
</ol>
<p>Would this be a correct and recommended approach?</p>
<p>I would also appreciate clarification on two points:</p>
<ul>
<li>
<p>Are any additional code modifications required to ensure that preprocessing runs on the CPU while training remains on the GPU, without affecting image-label alignment or segmentation accuracy?</p>
</li>
<li>
<p>How can I ensure that all eligible annotated images are eventually included in training, even when using a limited caching strategy?</p>
</li>
</ul>
<p>My goal is to establish a stable and scalable training pipeline capable of handling an increasing number of annotated 3D images without exhausting GPU memory.</p>
<p>Any suggestions or example code would be greatly appreciated.</p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2026-11-17 22:21 UTC)

<aside class="quote no-group" data-username="RDLmomo" data-post="1" data-topic="48948">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/b38774/48.png" class="avatar"> RDLmomo:</div>
<blockquote>
<p>My goal is to establish a stable and scalable training pipeline capable of handling an increasing number of annotated 3D images without exhausting GPU memory.</p>
</blockquote>
</aside>
<p>Memory consumptions in the models I am familiar with are affected by the model architecture choices (number of convolution layers, image dimensions, etc), not by sample size. If your training model works for 20 samples, it should work for 2000 samples as well.</p>
<p>That CUDA OOM reported number is not very large, it is only 1.5GB. When I run into OOMs that usually an order of magnitude larger than that. What GPU and model are you using?</p>
<p>Going back between CPU and GPU and loading/offloading data usually kills your training speed. It might be better if you run the preprocessing at once, save the output and have model run directly on the processed data, as opposed to do preprocessing on the fly.</p>
<p>If you put you architecture and code to an LLM, these are kinds of things that they are very good at optimizing or finding solution to.</p>

---
