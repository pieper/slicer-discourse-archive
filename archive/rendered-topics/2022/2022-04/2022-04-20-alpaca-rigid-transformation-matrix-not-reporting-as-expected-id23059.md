---
topic_id: 23059
title: "Alpaca Rigid Transformation Matrix Not Reporting As Expected"
date: 2022-04-20
url: https://discourse.slicer.org/t/23059
---

# ALPACA rigid transformation matrix not reporting as expected

**Topic ID**: 23059
**Date**: 2022-04-20
**URL**: https://discourse.slicer.org/t/alpaca-rigid-transformation-matrix-not-reporting-as-expected/23059

---

## Post #1 by @Erik.Meilak (2022-04-20 19:03 UTC)

<p>Hello,<br>
I am using the Slicermorph module ALPACA to register one surface to another. It is important that I export and use the rigid transformation matrix that is written out during the “Run rigid alignment” process. If I use the tutorial example of the mouse skulls, I would expect that when I apply the rigid transformation matrix to the aligned A_J_ skull (Shown in red in the attached screenshot), it should have aligned with the prealigned A_J mouse skull (shown in yellow). Instead, as you can see although the translation may be correct, the rotation is totally off. Can anyone give any further information to what this Rigid Transformation Matrix is actually reporting? And how would I find the rigid transformation that aligns the source mesh with the target prior to elastic registration? Many thanks in advance.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee023c054fcfc152f7c6fd24b2867872335b52cf.jpeg" data-download-href="/uploads/short-url/xXwqmJ0nVyYQNIVkd6X82IbThU3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee023c054fcfc152f7c6fd24b2867872335b52cf_2_690x405.jpeg" alt="image" data-base62-sha1="xXwqmJ0nVyYQNIVkd6X82IbThU3" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee023c054fcfc152f7c6fd24b2867872335b52cf_2_690x405.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee023c054fcfc152f7c6fd24b2867872335b52cf_2_1035x607.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ee023c054fcfc152f7c6fd24b2867872335b52cf_2_1380x810.jpeg 2x" data-dominant-color="BEC2D8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1129 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @agporto (2022-04-26 21:48 UTC)

<p>Hi Erik<br>
As you mentioned, the surfaces should align given that the rigid transformation matrix follows Slicer convention (Transforms Module). So, it is surprising that they do not. On my computer, these models align just fine, so I need to track down what is the source of the problem. Are these meshes the same as the ones Murat has provided as part of SlicerMorph? And just to be sure, are you applying the transformation matrix to the source mesh? (and not the target one). Since ALPACA transforms the source mesh to match the target one, it is the initial source mesh the ones in which you would apply the transformation.</p>

---
