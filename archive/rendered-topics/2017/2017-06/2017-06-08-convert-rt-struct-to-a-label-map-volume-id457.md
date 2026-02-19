---
topic_id: 457
title: "Convert Rt Struct To A Label Map Volume"
date: 2017-06-08
url: https://discourse.slicer.org/t/457
---

# Convert RT struct to a label map volume

**Topic ID**: 457
**Date**: 2017-06-08
**URL**: https://discourse.slicer.org/t/convert-rt-struct-to-a-label-map-volume/457

---

## Post #1 by @yannick_s (2017-06-08 13:25 UTC)

<p>Operating system: Ubuntu 16.04 LTS<br>
Slicer version: 4.7.0-2017-06-03 r26072<br>
Expected behavior: Conversion from RT Struct to a label map in segmentation module producing label map volume with nonzero entries<br>
Actual behavior: Output label map volume is zero everywhere</p>
<p>Dear all,<br>
I have RT structs with a contouring in it, after installing SlicerRT I can import these from DICOM files. I would like to convert the RT struct to a binary labelmap. This is what I tried:<br>
Segmentations module -&gt; Representations: Create binary labelmap -&gt; Export/import models and labelmaps: select export, label map and an output node. This produces a labelmap volume with no nonzero entries.<br>
Can you point me to a solution?</p>
<p>Best and thank you,<br>
Yannick</p>

---

## Post #2 by @lassoan (2017-06-08 13:28 UTC)

<p>Are the structure sets displayed correctly?<br>
If you go to Segment Editor and select a master volume, can you edit segments (for example, paint in it)?</p>

---

## Post #3 by @pwang (2017-08-30 15:31 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="457">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Are the structure sets displayed correctly?</p>
</blockquote>
</aside>
<p>Hi Lassoan, I can display correctly and be able to paint in it. And the file format of contours is changed from .seg.vtm to .seg.nrrd. However, I still need to convert the contours to label cause I assume the label can be deformed with the image during the deformable image registration. Please advice 1. if my assumption is correct and 2. if correct, how I can convert the contours to label. Thanks a lot.</p>

---

## Post #4 by @lassoan (2017-08-30 16:22 UTC)

<p>You can apply rigid or deformable transforms directly to segmentation nodes, even in real-time (change the transform and you immediately see how the segments change). No need to export it to other node type.</p>
<p>If you want to edit a deformed segmentation then you need to go to Transforms module and “harden” the transform on the segmentation by clicking <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a90682e9aeed4c641d5d1589fee56294badfb97.png" alt="image" data-base62-sha1="hufDNou2EnpMq4Nkaklr6SyGg9p" width="36" height="32"> button.</p>

---

## Post #5 by @pwang (2017-09-01 19:31 UTC)

<p>Thanks Lassoan. Please see the screen shot:<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c203fc233c0faeabca4758f479a6e20ed4027220.png" data-download-href="/uploads/short-url/rGlalzFNtRzLGkVvm7mTAJI1SUw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c203fc233c0faeabca4758f479a6e20ed4027220_2_690x376.png" alt="image" data-base62-sha1="rGlalzFNtRzLGkVvm7mTAJI1SUw" width="690" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c203fc233c0faeabca4758f479a6e20ed4027220_2_690x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c203fc233c0faeabca4758f479a6e20ed4027220_2_1035x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/c203fc233c0faeabca4758f479a6e20ed4027220_2_1380x752.png 2x" data-dominant-color="A3A4A9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×1045 259 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div>. Q1: The structure is not deformed by BSpine. Because pink contour represents heart, and it is not following heart. How to make BSpine applied on RTSTRUCT? Q2: RTSTRUCT stays at the original location. How to change its original location to the same as CBCT (the fixed image) in the work? Thanks a lot.</p>

---

## Post #6 by @lassoan (2017-09-01 22:39 UTC)

<p>I’ve just checked and Transforms are applied correctly to Segmentations nodes. See this example video: <a href="https://1drv.ms/v/s!Arm_AFxB9yqHsJ8NLVWOX6tvTNHtpw">https://1drv.ms/v/s!Arm_AFxB9yqHsJ8NLVWOX6tvTNHtpw</a></p>
<p>If you still have problems, then please reproduce the problem with a data set that you can share (for example, data sets from Slicer’s Sample Data module), save the scene, upload to dropbox/onedrive, and paste the link here.</p>

---
