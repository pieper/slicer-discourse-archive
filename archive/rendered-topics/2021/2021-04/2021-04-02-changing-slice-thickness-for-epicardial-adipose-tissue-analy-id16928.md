---
topic_id: 16928
title: "Changing Slice Thickness For Epicardial Adipose Tissue Analy"
date: 2021-04-02
url: https://discourse.slicer.org/t/16928
---

# Changing slice thickness for epicardial adipose tissue analysis

**Topic ID**: 16928
**Date**: 2021-04-02
**URL**: https://discourse.slicer.org/t/changing-slice-thickness-for-epicardial-adipose-tissue-analysis/16928

---

## Post #1 by @Mark_Brahier (2021-04-02 16:16 UTC)

<p>I’m currently using 3D Slicer for manual segmentation of cardiac CTs to quantify epicardial adipose tissue. The CTs that I have are high resolution at a slice thickness of 0.5mm or less (some as small as 0.15mm). Within 3D Slicer, is there a way to “merge” segments so that the thickness is only 1mm (or perhaps even 2mm?). I know this will diminish the accuracy of the measurements to some extent, but it may be worth it to us for the time saved in analysis. I appreciate any advice on how to do this.</p>

---

## Post #2 by @pieper (2021-04-02 16:19 UTC)

<p>Yes, you can set the geometry of the segmentation independent of the background (it’s set to the background by default).  Use the segmentation geometry button next to the master volume selector.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#basic-concepts" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html#basic-concepts</a></p>

---

## Post #3 by @Mark_Brahier (2021-04-02 18:14 UTC)

<p>Thank you for this quick reply. Would you be able to provide additional details of where I need to go to adjust slice thickness? I apologize in advance, but I’m a novice at this and would appreciate any additional information. I’m using the latest version of Slicer.</p>

---

## Post #4 by @pieper (2021-04-02 21:58 UTC)

<p>Hmm, good question. I thought you could just edit this in the segmentation geometry dialog, but I can’t seem to enable that mode easily.  <a class="mention" href="/u/lassoan">@lassoan</a> or others?</p>

---

## Post #5 by @lassoan (2021-04-03 00:21 UTC)

<p>You may also choose to segment just 1 out of every 5-10 slices and use “Fill between slices” effect to create a full, high-resolution segmentation by smoothly interpolating between the segmented slices. You can insert additional slices anywhere where you find that the interpolated segmentation is not accurate enough.</p>

---

## Post #6 by @Mark_Brahier (2021-04-03 18:42 UTC)

<p>Thank you both, this is a great option. The issue I am running into now is that after “filling between slices,” the quantification of adipose tissue volume appears to be a lot lower than I would expect, approximately by a factor of 10. Because I manually segmented every 10th slice, I am wondering if the quantification is not capturing the slices that were segmented using the “fill between slices” feature. Is there a setting that I need to change?</p>

---

## Post #7 by @lassoan (2021-04-03 21:37 UTC)

<aside class="quote no-group" data-username="Mark_Brahier" data-post="6" data-topic="16928">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mark_brahier/48/5934_2.png" class="avatar"> Mark_Brahier:</div>
<blockquote>
<p>quantification of adipose tissue volume appears to be a lot lower than I would expect</p>
</blockquote>
</aside>
<p>It seems that you have not clicked “Apply” in “Fill between slices” effect to write the preview of interpolation results into the segmentation.</p>

---
