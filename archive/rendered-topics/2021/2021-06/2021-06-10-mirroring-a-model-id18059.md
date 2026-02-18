# Mirroring a model

**Topic ID**: 18059
**Date**: 2021-06-10
**URL**: https://discourse.slicer.org/t/mirroring-a-model/18059

---

## Post #1 by @mohammed_alshakhas (2021-06-10 11:13 UTC)

<p>i have this case of facia asymmertry , my purpose is to evaluatr zygoma position<br>
steps i followed<br>
1 segment the skull<br>
2 segment zygoma<br>
3 trnasform zygoma to model<br>
4 mirrror zygoma around x axis in suface model/ advance/ mirror</p>
<p>however i got it displace and not mirrored perfectly arounf x axis , i tried transformation to 3d position before mirroring and didnot fix it</p>
<p>any idea how to fix that ?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8b66ecfccd426df9e86749cfa59adaa43e2cb3c.jpeg" data-download-href="/uploads/short-url/zudgWrjOLS3UpUvyz0tEx2DqcH2.jpeg?dl=1" title="Screen Shot 2021-06-10 at 14.08.59" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b66ecfccd426df9e86749cfa59adaa43e2cb3c_2_690x431.jpeg" alt="Screen Shot 2021-06-10 at 14.08.59" data-base62-sha1="zudgWrjOLS3UpUvyz0tEx2DqcH2" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b66ecfccd426df9e86749cfa59adaa43e2cb3c_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b66ecfccd426df9e86749cfa59adaa43e2cb3c_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f8b66ecfccd426df9e86749cfa59adaa43e2cb3c_2_1380x862.jpeg 2x" data-dominant-color="B5B5C7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-10 at 14.08.59</span><span class="informations">2880×1800 534 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-07-21 01:37 UTC)

<p>In general, x axis of the coordinate system that a mesh is defined in is not aligned with the anatomical left-right axis and the origin is not in the center, therefore after mirroring you need to register the mirrored parts to the original surface, using one of the many <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">registration methods available in Slicer.</a></p>

---
