---
topic_id: 18878
title: "Model To Model Distance Question"
date: 2021-07-22
url: https://discourse.slicer.org/t/18878
---

# model to model distance question

**Topic ID**: 18878
**Date**: 2021-07-22
**URL**: https://discourse.slicer.org/t/model-to-model-distance-question/18878

---

## Post #1 by @byli2223 (2021-07-22 16:07 UTC)

<p>Operating system: Windows<br>
Slicer version: SlicerSALT 3.0.0</p>
<p>For the corresponding point mode, is there any way we can get the information about which pair of points on the two models were considered corresponding?</p>
<p>I don’t see that in the output model vtk file.</p>
<p>Thank you!</p>

---

## Post #2 by @Maxibers (2021-07-26 08:28 UTC)

<p>After the SPHARM method if you want to know which specific points of the two meshes are considered corresponding you should check the code of the Pick and Paint or Model to Model distance extensions and write some code yourself to extrapolate the informations you need.<br>
Instead, if you are just willing to check if the correspondency is present the fastest way i found is to place a landmark on the first mesh, use the pick and paint extension to propagate it to the second mesh and then use the Shape Population viewer extension to check the correspondency visually.</p>
<p>Hope this helps</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc49b9204db0364911a49ba5486c072a77b1720a.png" data-download-href="/uploads/short-url/zZQgXZE8Qng4QMnJxQXMfLIMRgS.png?dl=1" title="example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc49b9204db0364911a49ba5486c072a77b1720a_2_690x388.png" alt="example" data-base62-sha1="zZQgXZE8Qng4QMnJxQXMfLIMRgS" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc49b9204db0364911a49ba5486c072a77b1720a_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc49b9204db0364911a49ba5486c072a77b1720a_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc49b9204db0364911a49ba5486c072a77b1720a_2_1380x776.png 2x" data-dominant-color="3A3342"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">example</span><span class="informations">1920×1080 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
