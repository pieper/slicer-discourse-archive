# What does Crop volume do to gaps between slices?

**Topic ID**: 13842
**Date**: 2020-10-03
**URL**: https://discourse.slicer.org/t/what-does-crop-volume-do-to-gaps-between-slices/13842

---

## Post #1 by @lmach (2020-10-03 17:48 UTC)

<p>Hi,</p>
<p>I have a question about the “Crop Volume” module. I have MR images where the slice thickness is 5 mm and between two slices there are is a 5mm gap (see my drawing).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d072e5ffff7dfb8ebbb85f92832f5de88e5913b6.png" data-download-href="/uploads/short-url/tK1tVbWEAO9WDrHXAW8e5ANCiwe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d072e5ffff7dfb8ebbb85f92832f5de88e5913b6.png" alt="image" data-base62-sha1="tK1tVbWEAO9WDrHXAW8e5ANCiwe" width="345" height="214" data-dominant-color="FEF0F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">773×480 2.94 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now I use the “Crop Volume” module to interpolate, such that the new slice thickness will be 0.33mm, with interpolated cropping and isotropic scaling.</p>
<p>I understand that the module will interpolate the 5mm thick slices into 0.33mm thick slices, but what happens to the gap between the slices? Does the gap also become 0.33mm or will it stay as 5mm?</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2020-10-03 19:22 UTC)

<p>Slice thickness specifies how much imaging is focused or blurred on the image plane. It does not affect image geometry or how the image is interpolated. Regardless of the slice thickness, there is no gap in the reconstructed 3D volume.</p>

---

## Post #3 by @lmach (2020-10-03 20:28 UTC)

<p>Thanks for your answer! I have a case where I want to segment a muscle and I have to go through and segment it slice by slice. For example, if I want to segment 1 cm of the muscle’s length, then would the slice thickness affect how many slices I have to segment? In this case, if slice thickness is 0.33mm and I want to segment 1cm  - am I correct in that I should segment 30 slices?</p>

---

## Post #4 by @lassoan (2020-10-03 20:33 UTC)

<aside class="quote no-group" data-username="lmach" data-post="3" data-topic="13842">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/ecae2f/48.png" class="avatar"> lmach:</div>
<blockquote>
<p>For example, if I want to segment 1 cm of the muscle’s length, then would the slice thickness affect how many slices I have to segment?</p>
</blockquote>
</aside>
<p>Not at all. Only voxel size (volume spacing) matters. You can find it in Volumes module / Volume information section.</p>
<p>In general, resolution should not matter much (as long as it is fine enough so that you can represent all relevant details), as all visualization, measurements, segmentation, etc. are performed in physical space.</p>
<p>In fact, you can decide how many slices you want to segment (skip as many slices as you want) and interpolate between them using “Fill between slices” effect. As muscles are often have elongated shape, you may obtain good segmentations by segmenting only a few slices.</p>

---

## Post #5 by @lmach (2020-10-04 06:54 UTC)

<p>Thank you for such a detailed answer!</p>

---
