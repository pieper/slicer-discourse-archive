---
topic_id: 42637
title: "Inverse Methods Of Curved Planar Reformat"
date: 2025-04-20
url: https://discourse.slicer.org/t/42637
---

# Inverse Methods of Curved Planar Reformat

**Topic ID**: 42637
**Date**: 2025-04-20
**URL**: https://discourse.slicer.org/t/inverse-methods-of-curved-planar-reformat/42637

---

## Post #1 by @Yanhong (2025-04-20 19:56 UTC)

<p>Hi, everyone, I have been using the CPR method in my project but I got some problem of its inverse. According to the document, the transformation is invertible when there is no self-cross. But the curve I want to process will cause this problem. I am wondering if there is some way to solve this problem?</p>
<p>I have tryed to modity the curved factors and the slicer spacing, but it seems the matrix is still not invertible. Since the forward transformation perform well even encounting the intercross of slices, if there any possibility to create a inverse displacement transformation rather than use the invert. I try to do this, but find that the forward transformation uses a sparse matrix for tranformation with a shape like (n,2,2) controling the corner of each slice. But this seems not applicable for the inverse tranformation.</p>
<p>Is there any possible solution I can try with to solve this problem?  Thanks.</p>

---

## Post #2 by @Yanhong (2025-04-25 09:00 UTC)

<p>I have make some progress, I am not quite familar with 3d Slicer but getting used to it. When I apply the Invert, which is a vtkGridTransfotm as used in the CPR methods, it show in 3d formate correct but went wrong when I want to harden it. Why such problem will happen?</p>

---

## Post #3 by @mikebind (2025-04-25 16:58 UTC)

<p>I think the general problem is that crossing planes in CPR creates a one-to-many mapping (a voxel location at the intersection of two slicing planes ends up present on two different slices in the reformat), but such a transformation is not smoothly invertible. The inverse would be many-to-one, which is problematic.  I imagine there may be ways people have tried to work around this, but I think this is why there isn’t an easy/obvious general solution.</p>

---

## Post #4 by @pieper (2025-04-25 18:10 UTC)

<p>The CPR transforms are typically invertible over a defined area, such as close to the centerline but then become singular as you get further away (i.e. you are good at the teeth but not at the center of the tongue).</p>

---

## Post #5 by @lassoan (2025-04-26 12:34 UTC)

<p><a class="mention" href="/u/mikebind">@mikebind</a> and <a class="mention" href="/u/pieper">@pieper</a> are exactly right. I’ve also explained this in detail, with illustrations, with description of what parameters to change to avoid the ambiguous mapping in the <a href="https://github.com/PerkLab/SlicerSandbox?tab=readme-ov-file#adjust-reformatting-parameters-for-robust-mapping">module’s documentation</a>.</p>

---

## Post #6 by @Yanhong (2025-04-26 13:34 UTC)

<p>Thank you all for your kind replies and valuable insights.<br>
I have already adjusted the parameters, but I am still encountering the issue. Since I am working with the colon, which has a highly curved and complex structure, the problem during the inverse transformation seems inevitable.</p>
<p>I have come up with a possible method, although I am not entirely sure if it is correct. I process the cpr slice by slice, ensuring the transformation is invertible at each slice (although this may slightly affect the quality by adjusting the slice corners). I found that, in some cases, this approach allows the inverse transformation to correctly align with the ground truth in 3D display.</p>
<p>However, the problem arises when I try to harden the transform: the corrected structure disappears. In my current method, I try to fix the problem within each individual slice, the transform is a vtkGridTransform with a shape of (2,2,2,3). I suspect this is due to many-to-one causing the harden incorrect, since before the harden it is still connect with the transform but resampling will be done after the harden.</p>
<p>Does anyone have experience with this kind of issue or insights into why the hardening step might cause the corrected volume become wrong? The two images is the inverse transform before the harden which seem correct.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d72186540d36cee1756dd038097ccc2604bac11.jpeg" data-download-href="/uploads/short-url/1UWECquGDm9Iis9WzCiAKWTGguJ.jpeg?dl=1" title="屏幕截图 2025-04-26 221706" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d72186540d36cee1756dd038097ccc2604bac11_2_690x294.jpeg" alt="屏幕截图 2025-04-26 221706" data-base62-sha1="1UWECquGDm9Iis9WzCiAKWTGguJ" width="690" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d72186540d36cee1756dd038097ccc2604bac11_2_690x294.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d72186540d36cee1756dd038097ccc2604bac11_2_1035x441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/d/0d72186540d36cee1756dd038097ccc2604bac11_2_1380x588.jpeg 2x" data-dominant-color="B6BADC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2025-04-26 221706</span><span class="informations">1920×819 49.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c216ca72292bc18a96d000f07c92d03dc2fa21fa.jpeg" data-download-href="/uploads/short-url/rGZspRmIY9n8SHVWyJLevtojtqO.jpeg?dl=1" title="屏幕截图 2025-04-26 221810" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c216ca72292bc18a96d000f07c92d03dc2fa21fa_2_690x307.jpeg" alt="屏幕截图 2025-04-26 221810" data-base62-sha1="rGZspRmIY9n8SHVWyJLevtojtqO" width="690" height="307" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c216ca72292bc18a96d000f07c92d03dc2fa21fa_2_690x307.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c216ca72292bc18a96d000f07c92d03dc2fa21fa_2_1035x460.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c216ca72292bc18a96d000f07c92d03dc2fa21fa_2_1380x614.jpeg 2x" data-dominant-color="B0B4D4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">屏幕截图 2025-04-26 221810</span><span class="informations">1920×857 59 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank you all again for your kind support and suggestions!</p>

---

## Post #7 by @lassoan (2025-04-26 13:49 UTC)

<p>Ambiguity in the displacement field can be always avoided by modifying the two parameters as described in the module documentation.</p>
<p>It should be no problem at all to compute inverse for the colon, as long as you keep the slice size small enough. There is no need for guessing, if you visualize the displacement field as described in the module documentation then you can see exactly what’s happening in your grid transform.</p>
<aside class="quote no-group" data-username="Yanhong" data-post="6" data-topic="42637">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/yanhong/48/80044_2.png" class="avatar"> Yanhong:</div>
<blockquote>
<p>However, the problem arises when I try to harden the transform: the corrected structure disappears.</p>
</blockquote>
</aside>
<p>When you harden a transform, the extents of the transformed volume is computed based on sparse sampling on the volume’s bounding box. In this very special case this sparse sampling may not end up capturing the entire volume extent, so you may need to do the resampling manually using <code>Resample Scalar/Vector/DWI Volume</code> module, using the original CT as reference volume.</p>

---

## Post #8 by @Yanhong (2025-04-28 05:02 UTC)

<p>Thank you very much for your advise, I will try them!</p>

---

## Post #9 by @Mimi1 (2025-04-30 16:55 UTC)

<p>Hi, I also have a problem with the inverse of the CPR. I’m measuring muscles along the cervical spine of horses and because I can’t align the anatomy with the scan, my segmentations end up in multiple slices making them inaccurate and jagged. My solution to this was to use CPR and do the segmentation and then I wanted to reverse the CPR it so I can use it for an AI learning system. My problem is that I can’t reverse the CPR. The lines are not crossing, it’s only a slight curve.</p>

---

## Post #10 by @lassoan (2025-05-01 15:23 UTC)

<p><a class="mention" href="/u/mimi1">@Mimi1</a> You can fix the inversion problem by reducing the <code>Slice size</code> and/or slightly increase the <code>Curve resolution</code> value. If you still have any issues then please post some more details, screenshots, and visualization of the deformed grid in slice and 3D views as shown in the <a href="https://github.com/PerkLab/SlicerSandbox?tab=readme-ov-file#adjust-reformatting-parameters-for-robust-mapping">module documentation</a>.</p>

---
