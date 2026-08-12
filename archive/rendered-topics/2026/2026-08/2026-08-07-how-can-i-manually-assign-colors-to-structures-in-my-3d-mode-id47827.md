---
topic_id: 47827
title: "How can I manually assign colors to structures in my 3D Model?"
date: 2026-08-07
url: https://discourse.slicer.org/t/47827
last_bumped: 2026-08-11T14:02:38.620Z
---

# How can I manually assign colors to structures in my 3D Model?

**Topic ID**: 47827
**Date**: 2026-08-07
**URL**: https://discourse.slicer.org/t/how-can-i-manually-assign-colors-to-structures-in-my-3d-model/47827

---

## Post #1 by @Nonso (2026-08-07 14:38 UTC)

<p>Operating system: Windows 11 Pro<br>
Slicer version: 5.10.0<br>
Expected behavior:<br>
Actual behavior: I imported a segmented model in .nrrd format, from MIB. After creating a model in 3D Slicer, using the model maker, most of the structures of interest were red in color (automatically assigned). This makes it difficult to comprehend the structures of interest. Is there any way I can manually assign colors to the structures in the 3D model?</p>

---

## Post #2 by @viktoriyanavrotskaya (2026-08-10 09:53 UTC)

<p>Yeah, this usually happens because Model Maker keyed the colors off label values that mostly collapsed to one. Easiest fix: go to the Models module, select each model node in the list, and change the color under Display. You can set each structure individually there. If they’re all merged into one model, you may need to re-run Model Maker with a proper color table so each label gets its own color.</p>

---

## Post #3 by @viktoriyanavrotskaya (2026-08-11 12:09 UTC)

<aside class="quote no-group quote-modified" data-username="viktoriyanavrotskaya" data-post="2" data-topic="47827" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/59ef9b/48.png" class="avatar"> viktoriyanavrotskaya:</div>
<blockquote>
<p>Yeah, this usually happens because Model Maker keyed the colors off label values that mostly collapsed to one. Easiest fix: go to the <a href="https://tropical-casino.com/" rel="noopener nofollow ugc">website </a>Models module, select each model node in the list, and change the color under Display. You can set each structure individually there. If they’re all merged into one model, you may need to re-run Model Maker with a proper color table so each label gets its own color.</p>
</blockquote>
</aside>
<p>Solid fix. One thing worth adding for the re-run case: if all the structures collapsed into one model, it’s often because the input labelmap actually has a single label value rather than distinct integers per structure, so Model Maker had nothing to split on. Worth checking the labelmap’s scalar range first, if it’s all 1s, the fix is upstream in the segmentation, not the color table. When labels are properly distinct, applying a color table (or using the Segmentations module to export) gives each its own color automatically.</p>

---

## Post #4 by @Nonso (2026-08-11 14:02 UTC)

<p>Thank you very much. I was able to resolve the issue following the guideline you provided. <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=15" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
