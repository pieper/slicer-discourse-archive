---
topic_id: 5510
title: "Duplicated Segmentation Error"
date: 2019-01-25
url: https://discourse.slicer.org/t/5510
---

# Duplicated Segmentation Error

**Topic ID**: 5510
**Date**: 2019-01-25
**URL**: https://discourse.slicer.org/t/duplicated-segmentation-error/5510

---

## Post #1 by @pervin_huseyinova (2019-01-25 14:05 UTC)

<p>I am working on dicom files, where i segment vessels on every slice. I crop every volume, apply curvature anisotropic diffusion and oversample the volume to get higher quality segmentation. My problem is that after a while of segmentation i start seeing the same segmentations on consecutive slices, eventough i labelled them differently. For example, as seen in the pictures below. I labeled them differently, but somehow labels ended up being duplicated and i lost the segmentation i did for the second one.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e82199bc5bf0453e258cde9697523318edb1c1a5.png" alt="Screenshot_1" data-base62-sha1="x7wLeVFhoxLRGQLlkVP1wnsuS9L" width="565" height="372"></p>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2019-01-25 14:37 UTC)

<p>See the answer in this topic:</p><aside class="quote" data-post="6" data-topic="1459">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/segmentation-editor-how-to-disable-painting-on-adjacent-slices/1459/6">Segmentation Editor - How to disable painting on adjacent slices?</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Recent versions of Slicer now show a warning button (with an exclamation mark) if any of the slice viewers are not aligned with the current segmentation axes. Click that button to snap each slice view to nearest segmentation axis.
  </blockquote>
</aside>


---

## Post #3 by @lassoan (2019-01-26 05:24 UTC)

<p>Also note that when you iterate through the image slice by slice then the current background volume spacing is used for determining step size. You can enable slice intersections (click on the down-arrow button next to the crosshair button on the toolbar and check “Slice intersections”) to see how much the slice position is offset with each step.</p>

---

## Post #4 by @pervin_huseyinova (2019-02-07 18:36 UTC)

<p>But i didn’t painted the adjacent slice. I painted them all differently, but somehow some of the labels ended up being exactly same. This is a huge problem for me since I’m losing a lot of my work, what can be causing this? Is it possible that this is happenning because i use oversampling with isotropic spacing?</p>

---

## Post #5 by @lassoan (2019-02-07 19:34 UTC)

<p>You can see the brush thickness in the orthogonal slices to verify if you indeed paint only in a single slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7c7abd9c03127d42c4fd0bdd9feb55414824b3a.png" data-download-href="/uploads/short-url/uMSrTtq330gaqNb31NKCwV2VyD8.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7c7abd9c03127d42c4fd0bdd9feb55414824b3a.png" alt="image" data-base62-sha1="uMSrTtq330gaqNb31NKCwV2VyD8" width="690" height="467" data-dominant-color="95848B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1383×937 77.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It may be confusing to edit a segmentation that has higher resolution than the master volume (because arrow keys on keyboard jump by one slice thickness distance but you may not be centered on the slice; slide offset slider above the slice viewer jumps a small amount, which is typically somewhat smaller than the slice thickness, so it may put you somewhere off the center of the slice). It may be simpler to just resample the master volume using Crop&amp;resample module before you start segmenting.</p>

---

## Post #6 by @dhquan (2020-12-28 06:36 UTC)

<p>Hi Pervin,<br>
Did you find the solution for this issue?</p>

---
