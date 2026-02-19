---
topic_id: 5232
title: "Model Does Not Close After Hollowing"
date: 2018-12-30
url: https://discourse.slicer.org/t/5232
---

# Model does not close after hollowing

**Topic ID**: 5232
**Date**: 2018-12-30
**URL**: https://discourse.slicer.org/t/model-does-not-close-after-hollowing/5232

---

## Post #1 by @feng (2018-12-30 18:51 UTC)

<p>￼Anyone konws why this happens? I chose inside surface in this case</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/f/9f3ba6acd73b28006ba3daaa7c209148d87f779b.jpeg" data-download-href="/uploads/short-url/mIDICijUVI7Z7QOvRAdC3afsmMj.jpeg?dl=1" title="43347DB6-3CCE-4B84-B76E-521E69FE3881" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f3ba6acd73b28006ba3daaa7c209148d87f779b_2_498x500.jpeg" alt="43347DB6-3CCE-4B84-B76E-521E69FE3881" data-base62-sha1="mIDICijUVI7Z7QOvRAdC3afsmMj" width="498" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f3ba6acd73b28006ba3daaa7c209148d87f779b_2_498x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f3ba6acd73b28006ba3daaa7c209148d87f779b_2_747x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9f3ba6acd73b28006ba3daaa7c209148d87f779b_2_996x1000.jpeg 2x" data-dominant-color="5F6169"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">43347DB6-3CCE-4B84-B76E-521E69FE3881</span><span class="informations">1522×1528 419 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-12-30 19:11 UTC)

<p>The shell is very thin. Either make it thicker (in number of voxels; if you d to decrease physical thickness then you may need to decrease voxel spacing of the segmentation by clicking the button next to master volume selector) or disable surface smoothing (option available in the dropdown menu of the Show 3D button).</p>

---

## Post #3 by @feng (2018-12-30 19:40 UTC)

<p>Solved. Thank you very much professor!</p>

---
