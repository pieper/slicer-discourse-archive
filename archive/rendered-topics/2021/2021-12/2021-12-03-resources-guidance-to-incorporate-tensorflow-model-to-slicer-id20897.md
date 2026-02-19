---
topic_id: 20897
title: "Resources Guidance To Incorporate Tensorflow Model To Slicer"
date: 2021-12-03
url: https://discourse.slicer.org/t/20897
---

# Resources/Guidance to incorporate tensorflow model to slicer scripted module

**Topic ID**: 20897
**Date**: 2021-12-03
**URL**: https://discourse.slicer.org/t/resources-guidance-to-incorporate-tensorflow-model-to-slicer-scripted-module/20897

---

## Post #1 by @Ganeshaaraj (2021-12-03 04:42 UTC)

<p>Hello,</p>
<p>I developed a semantic segmentation model using U-Net (Deep learning architecture) in Tensorflow. Model is fully trained. I want to develop a scripted module in which I want to import that particular model to carry out predictions for unseen future data.</p>
<p>It will be very helpful if someone can refer to any reference material which helps to build the above case from scratch or any comments./ideas/guidance regarding above case are welcome</p>
<p>Thank you</p>
<p>G.Ganeshaaraj</p>

---

## Post #2 by @pieper (2021-12-03 14:12 UTC)

<p><a class="mention" href="/u/fernando">@Fernando</a> has done some <a href="https://github.com/fepegar/SlicerParcellation">cool tools with pytorch</a>.  Tensorflow can also be added to Slicer via <code>pip_install</code> so you can probably do something similar.  I don’t have any example code I can share, but I’ve used tensorflow with Slicer volumes just by passing numpy arrays around.</p>
<p>What structures are you segmenting with the U-Net?</p>

---
