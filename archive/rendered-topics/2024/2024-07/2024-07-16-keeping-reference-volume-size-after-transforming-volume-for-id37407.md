# Keeping reference volume size after transforming volume for very large images

**Topic ID**: 37407
**Date**: 2024-07-16
**URL**: https://discourse.slicer.org/t/keeping-reference-volume-size-after-transforming-volume-for-very-large-images/37407

---

## Post #1 by @wkacct_acctwk (2024-07-16 17:57 UTC)

<p>I have a deformation field I’d like to apply to my images, and I am able to do so by applying the transforms and then hardening them. However, the output volume’s extent was larger than the original volume, which is not ideal for my purposes. My understanding was the way to rectify this was to use a Resampling function instead and specify a reference volume’s extent. However, as my images are quite large, this results in OOM errors (whereas using the transform/harden pipeline does not). I am wondering if there is a difference in how the transformation is applied under the hood between the two methods, and if there is a good way to ensure my output volume can be matched to a reference size in a memory efficient manner.</p>

---

## Post #2 by @lassoan (2024-07-16 18:03 UTC)

<p>If you just a little short on physical memory then the simpest is to increase the amount of virtual memory on your computer. Depending on your computer it may be accomplished by freeing up more disk space or adjust virtual memory size in your system settings.</p>

---
