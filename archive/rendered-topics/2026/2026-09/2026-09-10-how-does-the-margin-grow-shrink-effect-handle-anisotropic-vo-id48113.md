---
topic_id: 48113
title: "How does the Margin (grow/shrink) effect handle anisotropic voxel spacing?"
date: 2026-09-10
url: https://discourse.slicer.org/t/48113
last_bumped: 2026-09-14T22:10:31.150Z
---

# How does the Margin (grow/shrink) effect handle anisotropic voxel spacing?

**Topic ID**: 48113
**Date**: 2026-09-10
**URL**: https://discourse.slicer.org/t/how-does-the-margin-grow-shrink-effect-handle-anisotropic-voxel-spacing/48113

---

## Post #1 by @Farah_BH (2026-09-10 20:48 UTC)

<p>Hello,</p>
<p>I’m using the Margin effect in Segment Editor to isotropically expand a segment on CT data with anisotropic voxel spacing. When I request a 3.00 mm margin, the UI reports an actual expansion of 2.9 × 2.9 × 2.5 mm, corresponding to a 3×3×1 pixel kernel.</p>
<p>Is this because the Margin effect uses a whole-voxel kernel, rounded per axis, rather than a continuous distance transform?</p>

---

## Post #2 by @mikebind (2026-09-14 22:10 UTC)

<p>Yes, you are exactly correct. I believe this is done because then the filtering can be applied entirely in voxel space.  In any case, isotropic expansion will not generally be possible on an anisotropic grid:  you can only add or remove whole voxels from the segment, so if the voxels are anisotropic the minimal amount you can add or remove is different in different directions.</p>
<p>If you want to apply an isotropic expansion, you could first resample your image or segmentation to be isotropic.  You can resample an existing segmentation using the Segmentation Geometry button:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8fcfd50d11727c56402e9de433958c1d9cf4000.png" data-download-href="/uploads/short-url/xf6NDOe6UC4tMeThLYHkPNeJg6Q.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8fcfd50d11727c56402e9de433958c1d9cf4000_2_690x348.png" alt="image" data-base62-sha1="xf6NDOe6UC4tMeThLYHkPNeJg6Q" width="690" height="348" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8fcfd50d11727c56402e9de433958c1d9cf4000_2_690x348.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8fcfd50d11727c56402e9de433958c1d9cf4000_2_1035x522.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8fcfd50d11727c56402e9de433958c1d9cf4000.png 2x" data-dominant-color="E9E8E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1127×570 102 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options" rel="noopener nofollow ugc">Segment editor — 3D Slicer documentation</a></p>

---
