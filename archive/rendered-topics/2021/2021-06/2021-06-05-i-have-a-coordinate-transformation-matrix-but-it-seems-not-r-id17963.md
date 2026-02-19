---
topic_id: 17963
title: "I Have A Coordinate Transformation Matrix But It Seems Not R"
date: 2021-06-05
url: https://discourse.slicer.org/t/17963
---

# I have a coordinate transformation matrix, but it seems not right when i apply it to the coordinate model in the transform module

**Topic ID**: 17963
**Date**: 2021-06-05
**URL**: https://discourse.slicer.org/t/i-have-a-coordinate-transformation-matrix-but-it-seems-not-right-when-i-apply-it-to-the-coordinate-model-in-the-transform-module/17963

---

## Post #1 by @yulaomao (2021-06-05 09:38 UTC)

<p>The original coordinate system is the world coordinate system, and the new coordinate system takes the center of two balls as the Y axis. I use Python to do linear transform for a coordinate system shape model, and it works well. The Y-axis of the transformed model passes through two ball centers, as shown in the first figure. However, I filled the matrix into the transform module and did not get the expected result after applying the transform, just like the second figure.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74f1cca7e7d7356b52fca442c8fc803b4b4de3ed.png" data-download-href="/uploads/short-url/gGxrflBtO7WUTM8xuhteXlrIYY5.png?dl=1" title="TH@7PW2AMYT8GLC02THI`K" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74f1cca7e7d7356b52fca442c8fc803b4b4de3ed_2_612x500.png" alt="TH@7PW2AMYT8GLC02THI`K" data-base62-sha1="gGxrflBtO7WUTM8xuhteXlrIYY5" width="612" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74f1cca7e7d7356b52fca442c8fc803b4b4de3ed_2_612x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74f1cca7e7d7356b52fca442c8fc803b4b4de3ed_2_918x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74f1cca7e7d7356b52fca442c8fc803b4b4de3ed.png 2x" data-dominant-color="0F405A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">TH@7PW2AMYT8GLC02THI`K</span><span class="informations">1202×982 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68f6b9516ce574561626a57e5391cdd2f3428c2b.png" data-download-href="/uploads/short-url/eYyg98zefuglCUp1YMTmrrgLjZN.png?dl=1" title="C6DSQA9JXR4U%$3%~FZF(P" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68f6b9516ce574561626a57e5391cdd2f3428c2b_2_680x500.png" alt="C6DSQA9JXR4U%$3%~FZF(P" data-base62-sha1="eYyg98zefuglCUp1YMTmrrgLjZN" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68f6b9516ce574561626a57e5391cdd2f3428c2b_2_680x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/8/68f6b9516ce574561626a57e5391cdd2f3428c2b_2_1020x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/68f6b9516ce574561626a57e5391cdd2f3428c2b.png 2x" data-dominant-color="9396CD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">C6DSQA9JXR4U%$3%~FZF(P</span><span class="informations">1031×757 14.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-09-07 19:03 UTC)

<p>Let us know if you still need help with this. Provide an example scene and transformation matrix.</p>

---
