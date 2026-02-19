---
topic_id: 17020
title: "Tips For Semi Automatic Segmentation Of Fetal Brain Mri"
date: 2021-04-10
url: https://discourse.slicer.org/t/17020
---

# Tips for semi-automatic segmentation of fetal brain MRI

**Topic ID**: 17020
**Date**: 2021-04-10
**URL**: https://discourse.slicer.org/t/tips-for-semi-automatic-segmentation-of-fetal-brain-mri/17020

---

## Post #1 by @GMA (2021-04-10 15:04 UTC)

<p>Hello to all.<br>
I’m trying to segment fetal MRI brains acquired with multiplanar T2-HASTE sequences (see an example below taken from Radiopaedia).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b33945cca205f73a07caa6d3b41f37f0637afda4.jpeg" data-download-href="/uploads/short-url/pzuaKbrbNL4yq15Ftzt5Qv985Q8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b33945cca205f73a07caa6d3b41f37f0637afda4_2_486x499.jpeg" alt="image" data-base62-sha1="pzuaKbrbNL4yq15Ftzt5Qv985Q8" width="486" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b33945cca205f73a07caa6d3b41f37f0637afda4_2_486x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b33945cca205f73a07caa6d3b41f37f0637afda4_2_729x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b33945cca205f73a07caa6d3b41f37f0637afda4.jpeg 2x" data-dominant-color="707070"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">842×866 68 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I’m currently having a harsh time with manual segmentation which is really time consuming since I have to segment every slice and avoid CSF spaces and ventricles.<br>
I tried with a seed based approach, also a threshold based one without success. I also tried using a registration based approach but the coregistered images are reformatted into a different plane and I can’t get access anymore to a standard axial plane.<br>
Does anyone have any tips? Should I rely to a manual segmentation approach?</p>
<p>Thank you!</p>
<p>GMA</p>

---

## Post #2 by @lassoan (2021-04-14 05:20 UTC)

<p>What exactly you would like to segment?</p>
<p>Seed based approach should work fine, maybe you could post a few screenshots that illustrate what problems you are running into.</p>
<p>If registration-based approach works better then you can use that. You can resample the image with image planes at arbitrary orientation (using Crop module or any of the resample modules).</p>

---
