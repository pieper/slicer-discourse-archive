---
topic_id: 28714
title: "Joint Smoothing For Only Selected Segments"
date: 2023-04-02
url: https://discourse.slicer.org/t/28714
---

# Joint Smoothing for only Selected segments

**Topic ID**: 28714
**Date**: 2023-04-02
**URL**: https://discourse.slicer.org/t/joint-smoothing-for-only-selected-segments/28714

---

## Post #1 by @KSL (2023-04-02 08:44 UTC)

<p>Hello dear friends,<br>
Is it possible to conduct “Joint smoothing” for only “selected segments” e.g. spleen only, from the Total Segmentator module?</p>

---

## Post #2 by @rbumm (2023-04-03 00:15 UTC)

<p>Yes, you could make the ones invisibly that you do not have to smooth. Only visible segments undergo the process.</p>

---

## Post #3 by @KSL (2023-04-03 09:25 UTC)

<p>Sir, I feel that the amount of time it takes to “Joint smooth” the whole segments and the “only visible segments” is not significantly different. Could it be because I am running the module in CPU mode? Thank you.</p>

---

## Post #4 by @rbumm (2023-04-03 09:34 UTC)

<p>In my test just now with Slicer 5.2.2 smoothing 3 visible segments only takes less time than all 15 segments.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66ef1d8308a085bbc74beeb5644c94c954880c97.png" data-download-href="/uploads/short-url/eGB0fNZ4tTqxHOhNyuioe5dlghN.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66ef1d8308a085bbc74beeb5644c94c954880c97_2_376x500.png" alt="image" data-base62-sha1="eGB0fNZ4tTqxHOhNyuioe5dlghN" width="376" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66ef1d8308a085bbc74beeb5644c94c954880c97_2_376x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66ef1d8308a085bbc74beeb5644c94c954880c97.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66ef1d8308a085bbc74beeb5644c94c954880c97.png 2x" data-dominant-color="E6E7EA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">486×646 45.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @KSL (2023-04-03 09:53 UTC)

<p>Sir, I tried rerunning the joint smoothing, which took less time. My mistake was that I did not check the “Apply to visible segments” box. Thank you very much, Sir.</p>

---
