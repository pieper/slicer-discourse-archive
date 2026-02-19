---
topic_id: 5916
title: "Using Input Transformation In Slicerelastix"
date: 2019-02-25
url: https://discourse.slicer.org/t/5916
---

# Using input transformation in SlicerElastix

**Topic ID**: 5916
**Date**: 2019-02-25
**URL**: https://discourse.slicer.org/t/using-input-transformation-in-slicerelastix/5916

---

## Post #1 by @Alex_Vergara (2019-02-25 14:06 UTC)

<p>The current version of SlicerElastix actually outputs a transformation, BUT it requires that both input volumes must be aligned each other, which is rarely the case. The moving volume may already have a transformation associated to align it  with the reference volume. but I cant input this transformation in the module. The only way is to create a whole new volume just to do this with the corresponding increasing memory usage (imagine doing this in batch for 500x500MB images). The solution is already available for BRAINS module, it can input the transformation and just modify it.<br>
Therefore this is a feature request: Add (optionally) the initial transformation that must be applied to the moving volume, just like the BRAINS registration functionality.<br>
This<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8.png" data-download-href="/uploads/short-url/t8cHpXM5VpQF92w9ybb32fZhMDe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8_2_504x500.png" alt="image" data-base62-sha1="t8cHpXM5VpQF92w9ybb32fZhMDe" width="504" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8_2_504x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc2c7aaf7174dfbcdafcf829981d1f3f801dd6a8.png 2x" data-dominant-color="EBEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">565×560 51.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
shall have<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e962f841a53750e182156a623e8487cbe01cd307.png" alt="imagen" data-base62-sha1="xiDi7IlbTSc1J1SxY9ytUEJzfPV" width="544" height="122"><br>
Also the output shall be like this for consistency<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/680171ff9c0bbaf424f673b79426bd8db5d33a22.png" alt="imagen" data-base62-sha1="eQ4KInMzU5Rdskgd3fUxBFCDWuK" width="551" height="100"></p>

---

## Post #2 by @lassoan (2019-02-25 14:33 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="1" data-topic="5916">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>I cant input this transformation in the module</p>
</blockquote>
</aside>
<p>You can, by hardening the transform on the moving volume before starting the registration.</p>

---

## Post #3 by @Alex_Vergara (2019-03-04 14:46 UTC)

<p>But this will create a new volume in each iteration increasing memory usage, it is ok for a couple hundreds images but not for common practice. For some practices it is forbidden to modify original input images, you can only work with transformations.</p>

---

## Post #4 by @lassoan (2019-03-04 15:24 UTC)

<p>I agree that it would be nice to be able to define additional input transforms in SlicerElastix - contributions are welcome.<br>
Until this feature is implemented you can do as I described above. If original volume should not be modified then you can clone it and harden the transform on that. There should be no perceivable performance impact of this (unless you work with very large volumes), because after registration is completed you can delete this temporary clone volume.</p>

---
