---
topic_id: 25503
title: "How To Create New Segmentation From Growing Margins"
date: 2022-09-30
url: https://discourse.slicer.org/t/25503
---

# How to create new segmentation from growing margins

**Topic ID**: 25503
**Date**: 2022-09-30
**URL**: https://discourse.slicer.org/t/how-to-create-new-segmentation-from-growing-margins/25503

---

## Post #1 by @Ana_Neves (2022-09-30 14:34 UTC)

<p>Operating system: MacOS Monterey 12.2.1<br>
Sliver version: 5.0.2</p>
<p>Hello. I am currently using 3D slicer for cardiac CT analysis. I’ve been currently struggling with trying to create a new segmentation for periatrial fat.<br>
At this moment I have segmented the left atrium with the paint tool and filled between slices to gain a model of the left atrium, then I applied the margin tool to grow the segment with the editable intensity range with the hounsfield units for fat to select the periatrial fat.<br>
However, I would like to create a separate segmentation for the periatrial fat (as in the image below), without including the left atrial segment. How can I “exclude” the left atrium from the periatrial fat segmentation?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/022788f91116a9ee7d5c9db7ddacbfdd96aaa5a7.jpeg" data-download-href="/uploads/short-url/j3EOSamrzdRzVGxkkXXN5fdU0v.jpeg?dl=1" title="segmentation example" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/022788f91116a9ee7d5c9db7ddacbfdd96aaa5a7_2_547x500.jpeg" alt="segmentation example" data-base62-sha1="j3EOSamrzdRzVGxkkXXN5fdU0v" width="547" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/2/022788f91116a9ee7d5c9db7ddacbfdd96aaa5a7_2_547x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/022788f91116a9ee7d5c9db7ddacbfdd96aaa5a7.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/2/022788f91116a9ee7d5c9db7ddacbfdd96aaa5a7.jpeg 2x" data-dominant-color="474846"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation example</span><span class="informations">801×731 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-09-30 19:34 UTC)

<p>You can either prevent going inside left atrium during segmentation by masking (Editable area → Outside al segments), or subtract one segment from the other using “Logical operators” effect.</p>

---

## Post #3 by @Ana_Neves (2022-09-30 20:35 UTC)

<p>Thank you! That is a much better (and simpler) solution than what I was trying to do <img src="https://emoji.discourse-cdn.com/twitter/smile.png?v=12" title=":smile:" class="emoji" alt=":smile:" loading="lazy" width="20" height="20"></p>

---
