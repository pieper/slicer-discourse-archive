# DVH variations after Deformable Registration

**Topic ID**: 43936
**Date**: 2025-08-03
**URL**: https://discourse.slicer.org/t/dvh-variations-after-deformable-registration/43936

---

## Post #1 by @azam (2025-08-03 05:54 UTC)

<p><strong>Hi everyone,</strong></p>
<p>I would like to register two DICOM CT images (CT FB, CT DIBH) that I exported from the treatment planning system, and then apply the resulting transformation matrix to the DICOM RT dose and RT structure data associated with the CT FB.</p>
<p>To achieve this, I followed the steps below:</p>
<p>1.     In both CT FB and CT DIBH images, the Hounsfield Unit values of the heart and CTV contours were changed to arbitrary values (for example, 500 and 100) using Segment Editor module.</p>
<p>2.     In the B-Spline deformable registration module, all registration stages were used with a maximum of 200 iterations.</p>
<p>3.     Then, in the Data module (using Transform hierarchy), the resulting transformation file was applied to the RT structure and RT dose using the “harden transform”.</p>
<p>4.     Finally, using the Dose Volume Histogram module, I extracted the DVHs for the RT dose and RT structures before and after registration.</p>
<p>As shown in the image below, the dose values differ between the two cases. Could you please help me understand the reason for this difference and how I can perform this registration correctly?</p>
<p>Thanks a lot</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c32219c7d92b8d31f37b97b1531faae9c54ca869.png" data-download-href="/uploads/short-url/rQeamzwbB15TjAieLlIcIiO7wtX.png?dl=1" title="registation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c32219c7d92b8d31f37b97b1531faae9c54ca869_2_680x500.png" alt="registation" data-base62-sha1="rQeamzwbB15TjAieLlIcIiO7wtX" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c32219c7d92b8d31f37b97b1531faae9c54ca869_2_680x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c32219c7d92b8d31f37b97b1531faae9c54ca869.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c32219c7d92b8d31f37b97b1531faae9c54ca869.png 2x" data-dominant-color="F6F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">registation</span><span class="informations">860×632 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-08-04 11:24 UTC)

<p>If I understand the workflow correctly, theoretically there should be no change in the DVH whatsoever (since you transform both the RTSS and the dose using the very same transformation). You will see some difference in practice, however, due to the limited resolution of the data. What is the resolution of the dose? The reference volume you used for the structures is the CT?</p>

---

## Post #3 by @azam (2025-08-04 16:51 UTC)

<p>hi <a href="https://discourse.slicer.org/u/cpinter">Pinter</a></p>
<p>My RT dose has the following specifications:<br>
<strong>Dimensions:</strong> 93×72×79 and <strong>Image spacing:</strong> 5×5×5 mm³</p>
<p>What do you mean by using the CT image as the reference volume — in which step?</p>

---

## Post #4 by @cpinter (2025-08-05 11:39 UTC)

<aside class="quote no-group" data-username="azam" data-post="3" data-topic="43936">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ea666f/48.png" class="avatar"> azam:</div>
<blockquote>
<p><strong>Dimensions:</strong> 93×72×79 and <strong>Image spacing:</strong> 5×5×5 mm³</p>
</blockquote>
</aside>
<p>I’d say that this is low resolution enough to see such high differences. Imagine that one voxel difference can potentially mean a displacement between 5mm and 8.6mm depending on type of neighborhood. First of all the deformed dose volume is resampled, then the voxels of the deformed dose under the deformed structure set may be different ones. Let me know if you disagree (without seeing the data I can only guess).</p>
<aside class="quote no-group" data-username="azam" data-post="3" data-topic="43936">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ea666f/48.png" class="avatar"> azam:</div>
<blockquote>
<p>What do you mean by using the CT image as the reference volume — in which step?</p>
</blockquote>
</aside>
<p>Converting the structure set contours to binary labelmap. If you export the segmentation node into labelmap node in the Data module (from the right-click menu), what resolution do you see?</p>
<p>I think you can potentially fix much of the discrepancy by resampling the dose volume to higher resolution. Then applying the deformation will be much less lossy, and the sampling of the voxels within the structures will be more accurate as well.</p>

---
