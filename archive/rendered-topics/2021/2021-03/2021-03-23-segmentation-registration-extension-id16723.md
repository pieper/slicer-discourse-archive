# Segmentation Registration Extension

**Topic ID**: 16723
**Date**: 2021-03-23
**URL**: https://discourse.slicer.org/t/segmentation-registration-extension/16723

---

## Post #1 by @reddington.15 (2021-03-23 16:00 UTC)

<p>Hi,</p>
<p>I am working on comparing two different segmentations and comparing their linear and rotational deformation. In another discussion it was recommended to download SlicerRegistration. I downloaded it and then ran the segment registration module where I compared the pre and post CT segmentations I had built. After the registration was complete there was a bunch of volumes and models that showed up in my data screen that I was confused as to what they meant. I was wondering if you could give me a little insight as to what these models/volumes mean and how the deformation, affine, and alignment transforms all differ from each other in their context. I have screen shots attached to help give you a better idea of what I am referring to.</p>
<p>Hope to hear back soon!<br>
Thanks.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b045b6f61ef49d85b706bc9535ada672a05459ac.png" data-download-href="/uploads/short-url/p9noFioIFBhNcNzicWVLhzTAATq.png?dl=1" title="Screen Shot 2021-03-23 at 12.04.35 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b045b6f61ef49d85b706bc9535ada672a05459ac_2_690x385.png" alt="Screen Shot 2021-03-23 at 12.04.35 PM" data-base62-sha1="p9noFioIFBhNcNzicWVLhzTAATq" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/0/b045b6f61ef49d85b706bc9535ada672a05459ac_2_690x385.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b045b6f61ef49d85b706bc9535ada672a05459ac.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b045b6f61ef49d85b706bc9535ada672a05459ac.png 2x" data-dominant-color="E9E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-23 at 12.04.35 PM</span><span class="informations">964×538 76.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-03-24 16:26 UTC)

<p>Most likely all you need is the resulting “Affine Transform” or “Deformable Transform” and you can safely ignore all the other nodes, which are intermediate working data sets or final derived data sets (deformed images and contours). If you are interested in the details then you can read the associated paper and the source code of the module (simple Python script) and if you have any specific questions you can ask them here.</p>

---

## Post #3 by @reddington.15 (2021-03-26 13:13 UTC)

<p>Awesome, thank you! That helps a lot. What is the difference between Affine Transform and Deformable Transform?</p>

---

## Post #4 by @lassoan (2021-03-29 13:38 UTC)

<p>Affine is a linear transformation (lines remain lines), deformable transformation may mean any kind of warping (lines may be transformed to curves).</p>

---
