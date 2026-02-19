---
topic_id: 2625
title: "Fixing The Distorted Shape Of Segmented Organs"
date: 2018-04-18
url: https://discourse.slicer.org/t/2625
---

# fixing the distorted shape of segmented organs

**Topic ID**: 2625
**Date**: 2018-04-18
**URL**: https://discourse.slicer.org/t/fixing-the-distorted-shape-of-segmented-organs/2625

---

## Post #1 by @mmansouri (2018-04-18 14:11 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9e27aa9a469f7dfbaed2f97d49a4fc9457ca019.png" data-download-href="/uploads/short-url/xn2tKXoJitQzTDOgMfUZLUYciG5.png?dl=1" title="Kidneys" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9e27aa9a469f7dfbaed2f97d49a4fc9457ca019_2_413x500.png" alt="Kidneys" data-base62-sha1="xn2tKXoJitQzTDOgMfUZLUYciG5" width="413" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e9e27aa9a469f7dfbaed2f97d49a4fc9457ca019_2_413x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9e27aa9a469f7dfbaed2f97d49a4fc9457ca019.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9e27aa9a469f7dfbaed2f97d49a4fc9457ca019.png 2x" data-dominant-color="363E3B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Kidneys</span><span class="informations">508×615 174 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>we need to segment all the body organs using a pediatric whole body MRI. I know that my MRI quality is highly anisotropic (0.781250, 0.781250, 3.900000). When I use the segmentation tool, the quality of outcome 3D models are not good, the organs look very distorted. I’ve attached images of the segmented organs. Could you please help with improving the quality of our models? Any recommendations?</p>

---

## Post #2 by @lassoan (2018-04-18 14:24 UTC)

<p>To eliminate staircase artifacts, you can use Crop volume module to resample the volume to have isotropic spacing, and use this volume as input for segmentation. It is also recommended to reduce the region of interest (ROI) to the minimum necessary, to compensate for the increased number of voxels caused by resampling.</p>

---
