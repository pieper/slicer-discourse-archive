---
topic_id: 29415
title: "Methods Of Registration For Two Images"
date: 2023-05-11
url: https://discourse.slicer.org/t/29415
---

# Methods of Registration for Two Images 

**Topic ID**: 29415
**Date**: 2023-05-11
**URL**: https://discourse.slicer.org/t/methods-of-registration-for-two-images/29415

---

## Post #1 by @riro3277 (2023-05-11 21:24 UTC)

<p>We have two images where one is of the carotid arteries from the head to the aorta and another set that is below this carotid imaging capturing only the heart and aorta. We want to register these two sets to where we can see the entire pathway from the head to the heart. This picture shows what the two images sets spatially look like without registration. I want to remove that space through registration and have the images aligned to see the entire pathway, what would be the best registration method for this and how would I complete it?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e11c9baf975e54be9383d1e679db196d76290b9.jpeg" data-download-href="/uploads/short-url/myly9Uo8XvFpRDsGa5a06eg7fF7.jpeg?dl=1" title="slicerimages" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e11c9baf975e54be9383d1e679db196d76290b9_2_521x500.jpeg" alt="slicerimages" data-base62-sha1="myly9Uo8XvFpRDsGa5a06eg7fF7" width="521" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e11c9baf975e54be9383d1e679db196d76290b9_2_521x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e11c9baf975e54be9383d1e679db196d76290b9_2_781x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e11c9baf975e54be9383d1e679db196d76290b9_2_1042x1000.jpeg 2x" data-dominant-color="515771"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicerimages</span><span class="informations">1662×1592 111 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-05-13 12:27 UTC)

<p>This should be no problem at all. You may be able to do it fully automatically, by cropping both images to approximately the same region, computing the transform using automatic intensity-based image registration, then using the transform to align the full images. This page is a good starting point: <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html" class="inline-onebox">Registration — 3D Slicer documentation</a></p>

---
