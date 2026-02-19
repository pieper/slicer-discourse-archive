---
topic_id: 45426
title: "Deformable Model Registration Prototype"
date: 2025-12-09
url: https://discourse.slicer.org/t/45426
---

# Deformable model registration prototype

**Topic ID**: 45426
**Date**: 2025-12-09
**URL**: https://discourse.slicer.org/t/deformable-model-registration-prototype/45426

---

## Post #1 by @muratmaga (2025-12-09 17:47 UTC)

<p>I have enabled deformable model registration as fourth level of registration (scaling, rigid, affine) in <strong>FastModelAlign</strong> module of <strong>SlicerMorph</strong> extension. Like ALPACA, it uses the point cloud based registration via Coherent Point Drift (CPD) algorithm. Then pointwise deformations are interpolated for every vertex. In its default mode it works quite fast.</p>
<p>You can also output an interpolated grid transform (up to 256x256x256 grid size, default is 128^3) so that you can apply the resultant transform to an object other the model.</p>
<p>It is new and not tested a lot, but if you want to give it a try it is available starting todays preview builds.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd779bd8ed23f4376ec7a9a9a034aa65378d50e8.jpeg" data-download-href="/uploads/short-url/tjE8O6XoEZndORrnrbPd8J3f19u.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd779bd8ed23f4376ec7a9a9a034aa65378d50e8_2_400x500.jpeg" alt="image" data-base62-sha1="tjE8O6XoEZndORrnrbPd8J3f19u" width="400" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd779bd8ed23f4376ec7a9a9a034aa65378d50e8_2_400x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd779bd8ed23f4376ec7a9a9a034aa65378d50e8_2_600x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd779bd8ed23f4376ec7a9a9a034aa65378d50e8_2_800x1000.jpeg 2x" data-dominant-color="EDEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1023×1276 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
