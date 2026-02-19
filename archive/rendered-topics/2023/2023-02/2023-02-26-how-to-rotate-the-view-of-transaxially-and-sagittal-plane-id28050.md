---
topic_id: 28050
title: "How To Rotate The View Of Transaxially And Sagittal Plane"
date: 2023-02-26
url: https://discourse.slicer.org/t/28050
---

# How to rotate the view of transaxially and sagittal plane?

**Topic ID**: 28050
**Date**: 2023-02-26
**URL**: https://discourse.slicer.org/t/how-to-rotate-the-view-of-transaxially-and-sagittal-plane/28050

---

## Post #1 by @akmal871026 (2023-02-26 04:00 UTC)

<p>Dear all,</p>
<p>I want to rotate the view of my plane transaxial and sagittal plane as picture attached (the red arrow).</p>
<p>Anyone can help me?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71ab38079c09a31c423b330865d0930918e92ea8.jpeg" data-download-href="/uploads/short-url/gdyMUutgSjPzC3mvCrhz7PDNYRq.jpeg?dl=1" title="how to rotate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71ab38079c09a31c423b330865d0930918e92ea8_2_690x368.jpeg" alt="how to rotate" data-base62-sha1="gdyMUutgSjPzC3mvCrhz7PDNYRq" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71ab38079c09a31c423b330865d0930918e92ea8_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71ab38079c09a31c423b330865d0930918e92ea8_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/1/71ab38079c09a31c423b330865d0930918e92ea8_2_1380x736.jpeg 2x" data-dominant-color="A4A4B3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">how to rotate</span><span class="informations">1860×992 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-02-26 14:49 UTC)

<p>You can use the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html">Transforms module</a> to move the data, but it would be better to fix the source data to correctly describe the <a href="https://www.slicer.org/wiki/Coordinate_systems">image geometry with respect to patient</a> space (for example to make sure you know left from right and correct spacing).</p>

---

## Post #3 by @ungi (2023-02-27 15:12 UTC)

<p>You may also install the SlicerIGT extension, and use the Volume Reslice Driver module. That module allows you to rotate and translate any 2D view using any transformable node. Including transform nodes. This way your image stays in the original coordinate system. <a class="mention" href="/u/pieper">@pieper</a> 's solution is simpler, but that one moves your image.</p>

---
