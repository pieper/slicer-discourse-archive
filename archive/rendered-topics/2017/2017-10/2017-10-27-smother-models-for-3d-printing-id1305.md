---
topic_id: 1305
title: "Smother Models For 3D Printing"
date: 2017-10-27
url: https://discourse.slicer.org/t/1305
---

# Smother models for 3D Printing?

**Topic ID**: 1305
**Date**: 2017-10-27
**URL**: https://discourse.slicer.org/t/smother-models-for-3d-printing/1305

---

## Post #1 by @Jeff (2017-10-27 14:02 UTC)

<p>1st… I have to say that I love this software.  I’ve been using it to make STLs from CTs.</p>
<p>Is there a way to get smoother models for 3D Printing?  The models I’ve printed have a topographic map quality to them on large flat surfaces.</p>

---

## Post #2 by @ihnorton (2017-10-27 14:03 UTC)

<p>Please see suggestions here:</p>
<aside class="quote quote-modified" data-post="2" data-topic="301">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/stl-file-created-from-segmentation-is-not-smooth-enough/301/2">STL file created from segmentation is not smooth enough</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    You have three options, you can use all, but the first one is the most important: 

crop your input volume to the region of interest &amp; resample to have sufficiently high resolution using the Crop volume module: specify your ROI, select Isotropic spacing, select sufficiently low spacing scale value (the lower the value, the more details you can preserve during segmentation, but more memory and processing time you will need; typically 0.5 … 0.2 should work), select bspline interpolator
smooth the …
  </blockquote>
</aside>


---
