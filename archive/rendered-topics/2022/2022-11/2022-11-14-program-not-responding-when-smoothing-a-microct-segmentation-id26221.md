---
topic_id: 26221
title: "Program Not Responding When Smoothing A Microct Segmentation"
date: 2022-11-14
url: https://discourse.slicer.org/t/26221
---

# Program not responding when smoothing a microCT segmentation

**Topic ID**: 26221
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/program-not-responding-when-smoothing-a-microct-segmentation/26221

---

## Post #1 by @Tahara (2022-11-14 08:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3b2d1b00f048f185ad8135355a2f017d54989200.jpeg" data-download-href="/uploads/short-url/8ruO93EZLadlDp170GIEpEVE3mg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b2d1b00f048f185ad8135355a2f017d54989200_2_666x500.jpeg" alt="image" data-base62-sha1="8ruO93EZLadlDp170GIEpEVE3mg" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b2d1b00f048f185ad8135355a2f017d54989200_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b2d1b00f048f185ad8135355a2f017d54989200_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/b/3b2d1b00f048f185ad8135355a2f017d54989200_2_1332x1000.jpeg 2x" data-dominant-color="979992"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1440 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-11-14 14:26 UTC)

<p>It looks like you have loaded a microCT or microscopy image, with about a 3 micron voxel size, and then you used the default 1mm kernel size for smoothing, which resulted in a very large kernel size (301x301x301 voxels; while normally the kernel is 3-7 voxels). Smoothing with this big kernel may take many hours and the result is probably not what you want (it would blur 300 voxels into one).</p>
<p>You could adjust the kernel size to be about 100x smaller (0.01mm) to get meaningful smoothing. However, you would run into similar issues (unusually small voxel size) in other Segment Editor effects and other modules. Therefore, I would suggest to temporarily change your volume spacing values to 100x larger (if it was 0.0035 then set it to 0.35) in Volumes module’s Information section. Once you finished editing/processing your volume, you can set the spacing values back to the original values.</p>

---

## Post #3 by @lassoan (2022-12-06 16:06 UTC)

<p>2 posts were split to a new topic: <a href="/t/curved-line-profile-of-a-volume/26606">Curved line profile of a volume</a></p>

---
