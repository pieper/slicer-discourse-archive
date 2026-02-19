---
topic_id: 20204
title: "How To Create Trabecular Porous Structure"
date: 2021-10-18
url: https://discourse.slicer.org/t/20204
---

# How to create trabecular-porous structure

**Topic ID**: 20204
**Date**: 2021-10-18
**URL**: https://discourse.slicer.org/t/how-to-create-trabecular-porous-structure/20204

---

## Post #1 by @slicer365 (2021-10-18 11:07 UTC)

<p>As shown in the picture below,</p>
<p>this is a piece of bone, which is randomly filled with this honeycomb-like shape.</p>
<p>This structure can be directly 3D printed.</p>
<p>This is a simulated trabecular bone.</p>
<p>Can we create this kind of Trabecular bone through Slicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b02e9b9ebe942de317e7ee20c41e6b4e37763d4.jpeg" data-download-href="/uploads/short-url/jPKBMJmIfIqDNk7kpx1S9Mad6WU.jpeg?dl=1" title="捕获.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b02e9b9ebe942de317e7ee20c41e6b4e37763d4_2_366x375.jpeg" alt="捕获.PNG" data-base62-sha1="jPKBMJmIfIqDNk7kpx1S9Mad6WU" width="366" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8b02e9b9ebe942de317e7ee20c41e6b4e37763d4_2_366x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b02e9b9ebe942de317e7ee20c41e6b4e37763d4.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b02e9b9ebe942de317e7ee20c41e6b4e37763d4.jpeg 2x" data-dominant-color="888983"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获.PNG</span><span class="informations">521×533 40.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/55f3aee79bf420b573df502a56861aef4e44d0e7.jpeg" alt="微信图片_20211018150849" data-base62-sha1="cgmFMp4WKiyEq1NIWcysdVRsNYb" width="281" height="228"></p>

---

## Post #2 by @lassoan (2021-10-19 03:31 UTC)

<p>I don’t think there is a random trabecular bone structure generator module, but if you have a microCT then you can use the actual trabecular structure of the bone. You can also copy the trabecular bone from any other image and cut it to a patient-specific shape using Mask volume effect in Segment Editor.</p>
<p>If you don’t want to copy-paste porous structure from real bones then you can train a neural network to generate such textures for you, for example, using MONAI toolkit.</p>

---
