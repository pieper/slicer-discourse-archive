---
topic_id: 25961
title: "Wrapsolidify Is Amazing For Preprocessing Before Volumetric"
date: 2022-10-29
url: https://discourse.slicer.org/t/25961
---

# WrapSolidify is amazing for preprocessing before volumetric mesh generation

**Topic ID**: 25961
**Date**: 2022-10-29
**URL**: https://discourse.slicer.org/t/wrapsolidify-is-amazing-for-preprocessing-before-volumetric-mesh-generation/25961

---

## Post #1 by @avarghes24 (2022-10-29 04:52 UTC)

<p>Sorry I just realized I never responded to this. I was able to segment out the entire hip joint from the sample abdomen/pelvis CT in Slicer. Previously, I was trying to run TetGen in FeBioStudio and it kept on failing because my segmentations weren’t homogenous. The WrapSolidify effect solved this issue for me and TetGen ran perfectly on the .vtk’s I exported from Slicer. The result from the WrapSolidify effect was amazing and exactly what I needed! I wish the module worked as smoothly for MRIs but I imagine auto-segmenting MRIs is quite the ongoing challenge</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2670d20745d52c5970d740947c96a42ca2d80523.png" data-download-href="/uploads/short-url/5u3RlPUk7sG3gzycrrrK7aA7C4b.png?dl=1" title="Screen Shot 2022-10-29 at 12.45.18 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2670d20745d52c5970d740947c96a42ca2d80523_2_616x500.png" alt="Screen Shot 2022-10-29 at 12.45.18 AM" data-base62-sha1="5u3RlPUk7sG3gzycrrrK7aA7C4b" width="616" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/2670d20745d52c5970d740947c96a42ca2d80523_2_616x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2670d20745d52c5970d740947c96a42ca2d80523.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2670d20745d52c5970d740947c96a42ca2d80523.png 2x" data-dominant-color="5A5A5E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-10-29 at 12.45.18 AM</span><span class="informations">818×663 334 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-10-29 05:58 UTC)

<p>Great, thanks for the feedback and nice images. I would recommend to also check out SegmentMesher extension, which can generate volumetric meshes directly from segmentations. It can use TetGen or Cleaver (which I usually find working more robustly and faster than tetgen). Soon it’ll also be able to use NetGen and TetWild.</p>

---
