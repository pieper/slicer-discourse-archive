# Regarding the unexpected segmentation effects that occur during segmentation of lung tissue using MONAI Auto3DSeg

**Topic ID**: 36952
**Date**: 2024-06-22
**URL**: https://discourse.slicer.org/t/regarding-the-unexpected-segmentation-effects-that-occur-during-segmentation-of-lung-tissue-using-monai-auto3dseg/36952

---

## Post #1 by @lirongyaoper (2024-06-22 13:31 UTC)

<p>Operating system:ubuntu 24.04<br>
Slicer version:3D Slicer 5.7.0-2.24-06-06<br>
Expected behavior:Ensure pulmonary vascular continuity<br>
Actual behavior:I encountered the following problems when using the Lungs Segmentation model in the MONAI Auto3DSeg segmenter to automatically segment the trachea, pulmonary artery, and pulmonary veins of lung tissue:<br>
I found that the continuity of pulmonary blood vessels was interrupted in the segmented 3D renderings, especially the continuity of pulmonary veins was very serious.<br>
I would like to know if our official solution is better? Provide new already trained models? Optimize 3dslider kernel?<br>
Thank you and I look forward to your replies. Good luck to all the teachers out there.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/003d633f4f2e5e30556926437e2f78fba3d6c940.jpeg" data-download-href="/uploads/short-url/27wowiwUpFWuMz1lWrsBzpsiyI.jpeg?dl=1" title="Screenshot from 2024-06-22 21-03-02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/003d633f4f2e5e30556926437e2f78fba3d6c940_2_536x500.jpeg" alt="Screenshot from 2024-06-22 21-03-02" data-base62-sha1="27wowiwUpFWuMz1lWrsBzpsiyI" width="536" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/003d633f4f2e5e30556926437e2f78fba3d6c940_2_536x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/003d633f4f2e5e30556926437e2f78fba3d6c940_2_804x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/003d633f4f2e5e30556926437e2f78fba3d6c940.jpeg 2x" data-dominant-color="7F7AA1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2024-06-22 21-03-02</span><span class="informations">877×817 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-23 22:34 UTC)

<p>Could you manually segment what you would expect to see and post screenshots side by side with the current segmentation result?</p>
<p>Would you be able to do this enhancement on 50-100 images and share the results with us so that we can fine-tune the segmentation model?</p>

---
