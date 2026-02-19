---
topic_id: 19900
title: "Shifting Segmentation Image Or 2D Image"
date: 2021-09-28
url: https://discourse.slicer.org/t/19900
---

# Shifting Segmentation image or 2D Image

**Topic ID**: 19900
**Date**: 2021-09-28
**URL**: https://discourse.slicer.org/t/shifting-segmentation-image-or-2d-image/19900

---

## Post #1 by @MachadoL (2021-09-28 18:58 UTC)

<p>Hello, Friends.</p>
<p>I am dealing with a very peculiar situation. A segmentation was made over an image, but probably, in a cropped version of the image. Now, naturally, when I load the segmentation and the non-cropped image, I get this shift.<br>
The segmentation is correct and precise, however it is shifted.</p>
<p>Is there any way to re align that by hand that I am missing?</p>
<p>I tried changing 2D grey level image origin, but no success.<br>
Down here, you can find a shot on how it looks.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8237edc8df4bc6921c3de5e6d58457c7e257ff74.jpeg" data-download-href="/uploads/short-url/izXTGwqNMHCp5xz3kHAPRutFz1y.jpeg?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8237edc8df4bc6921c3de5e6d58457c7e257ff74_2_690x452.jpeg" alt="Screenshot" data-base62-sha1="izXTGwqNMHCp5xz3kHAPRutFz1y" width="690" height="452" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8237edc8df4bc6921c3de5e6d58457c7e257ff74_2_690x452.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8237edc8df4bc6921c3de5e6d58457c7e257ff74_2_1035x678.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8237edc8df4bc6921c3de5e6d58457c7e257ff74_2_1380x904.jpeg 2x" data-dominant-color="555B4A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">1386×909 74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks.</p>

---

## Post #2 by @mikebind (2021-09-28 23:54 UTC)

<p>I would recommend the Fiducial Registration module.  Choose a small set of corresponding points on the image and the segmentation, use the Fiducial Registration module to find the transform which aligns those point sets, and apply that transform to either the segmentation or the image (whichever landmarks you put as the “Moving” landmarks).</p>

---

## Post #3 by @MachadoL (2021-09-29 12:25 UTC)

<p>All right. Sounds Good. I’ll try that. Thanks</p>

---
