---
topic_id: 12558
title: "Registration Of Two Scans"
date: 2020-07-15
url: https://discourse.slicer.org/t/12558
---

# Registration of two scans

**Topic ID**: 12558
**Date**: 2020-07-15
**URL**: https://discourse.slicer.org/t/registration-of-two-scans/12558

---

## Post #1 by @Tekk_ya (2020-07-15 15:30 UTC)

<p>Hi all,</p>
<p>I want to register two CBCT scans. Based on my investigation on the required registration process, first, we need to apply some affine transformation and, later, we need to apply some deformable registration methods. Among the modules, I can either select some landmarks and use “Fiducial registration wizard” or I can use some automatic deformable registrations in the 3DSlicer like “General Registration (BRAINS)”. I have used BSpline (&gt;27 DOF) for the deformable registration in “General Registration (BRAINS)”. However, I see some parameters such as “percentage of samples” and “BSpline Grid Size” and many other parameters in the “Advanced Optimization Settings” which I am not sure how to tune them for my problem as the default values could not help me to achieve a nice result.</p>
<p>I have several other questions that I have listed below:</p>
<ol>
<li>Could you please let me know which modules are the best available ones for this purpose?</li>
<li>Should the voxel sizes of these two scans be the same?</li>
<li>How much the ROIs should be selected accurately? I was wondering if the size of the ROI regions in both scans would affect the results. What about the effect of the appearance of some undesired parts in one of the ROIs? Are the algorithms robust to them or should I use some masks for this purpose? I would appreciate it if you can share some tutorials for using the masks in registration problems.</li>
</ol>
<p>Thank you in advance for your help</p>

---

## Post #2 by @lassoan (2020-07-23 02:21 UTC)

<aside class="quote no-group" data-username="Tekk_ya" data-post="1" data-topic="12558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>Could you please let me know which modules are the best available ones for this purpose?</p>
</blockquote>
</aside>
<p>If initial misalignment between the scans is small (up to a few centimeters, up to 10-15 degrees) then you can go directly to intensity-based registration. If initial misalignment is large then I would recommend an approximate (couple of mm errors is not a problem) rigid landmark registration with 4-6 points.</p>
<aside class="quote no-group" data-username="Tekk_ya" data-post="1" data-topic="12558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>Should the voxel sizes of these two scans be the same?</p>
</blockquote>
</aside>
<p>Slicer performs all image operations in physical space, so voxel size does not matter.</p>
<aside class="quote no-group" data-username="Tekk_ya" data-post="1" data-topic="12558">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tekk_ya/48/3548_2.png" class="avatar"> Tekk_ya:</div>
<blockquote>
<p>How much the ROIs should be selected accurately?</p>
</blockquote>
</aside>
<p>You only need ROI if you want to exclude certain regions of the scan from the registration. If the region that must be excluded is not in the middle of the image then I would use “Crop volume” instead (reducing the volume size you make the registration faster and more robust).</p>

---
