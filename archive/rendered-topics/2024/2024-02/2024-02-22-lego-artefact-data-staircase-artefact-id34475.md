# Lego artefact data/staircase artefact

**Topic ID**: 34475
**Date**: 2024-02-22
**URL**: https://discourse.slicer.org/t/lego-artefact-data-staircase-artefact/34475

---

## Post #1 by @dr_usman_sani (2024-02-22 15:03 UTC)

<p>Problem report for Slicer 5.2.2 win-amd64: Hi I am having trouble as soon as i put data in the 4view screen it show one data is smooth while others have leggo shaped margins and inner content .here is a snap shot of what I am experiencing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92a66c630546a769a7f4fe7993bbbabc27e3b5d2.png" data-download-href="/uploads/short-url/kVkgOhyPf0izfU31fgZgakCN4Rk.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92a66c630546a769a7f4fe7993bbbabc27e3b5d2_2_689x457.png" alt="Screenshot" data-base62-sha1="kVkgOhyPf0izfU31fgZgakCN4Rk" width="689" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92a66c630546a769a7f4fe7993bbbabc27e3b5d2_2_689x457.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/92a66c630546a769a7f4fe7993bbbabc27e3b5d2_2_1033x685.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/92a66c630546a769a7f4fe7993bbbabc27e3b5d2.png 2x" data-dominant-color="4B4B57"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1346×893 191 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-02-22 16:48 UTC)

<p>This means you have an order of magnitude less resolution in Z dimension, very typical in medical imaging. You can use CropVolume and choose to “isotropic” option to resample the image to get rid off this artifact.</p>

---

## Post #3 by @dr_usman_sani (2024-02-23 04:12 UTC)

<p>Thank you Muratmaga for your guidance I will check and will let you know if I can get better resolution.</p>

---

## Post #4 by @dr_usman_sani (2024-02-24 06:16 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/3919a7b5301881226b0984e729d9c7a00fe14853.jpeg" data-download-href="/uploads/short-url/898bgbYY1n5w5sbj23ZgxzT33xh.jpeg?dl=1" title="SceneView" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3919a7b5301881226b0984e729d9c7a00fe14853_2_690x441.jpeg" alt="SceneView" data-base62-sha1="898bgbYY1n5w5sbj23ZgxzT33xh" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3919a7b5301881226b0984e729d9c7a00fe14853_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3919a7b5301881226b0984e729d9c7a00fe14853_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/9/3919a7b5301881226b0984e729d9c7a00fe14853_2_1380x882.jpeg 2x" data-dominant-color="53595C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SceneView</span><span class="informations">1404×899 126 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
its not getting any better</p>

---

## Post #5 by @lassoan (2024-02-24 15:26 UTC)

<p>If you have already created a low-resolution segment then you need to smooth it or segment it again. See detailed instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">here</a>.</p>

---
