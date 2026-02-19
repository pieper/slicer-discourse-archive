---
topic_id: 7363
title: "Define Default Layers For All Ct Scans"
date: 2019-06-30
url: https://discourse.slicer.org/t/7363
---

# define default layers for all CT scans 

**Topic ID**: 7363
**Date**: 2019-06-30
**URL**: https://discourse.slicer.org/t/define-default-layers-for-all-ct-scans/7363

---

## Post #1 by @a.tavallaie (2019-06-30 13:21 UTC)

<p>I have almost 800 brain CT scan that I should label them same as segmentation, so define segments for each of them is too time-consuming. is there any approach to make default segments ( tissue, bone, etc) for all files?</p>

---

## Post #2 by @pieper (2019-06-30 15:05 UTC)

<p>There’s nothing out of the box for that right now.  You’d need to write some kind of batch script and maybe use some of the segment editor effects to do things like thresholding.  You could start by looking at the case iterator extension.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Extensions/SlicerCaseIterator</a></p>

---
