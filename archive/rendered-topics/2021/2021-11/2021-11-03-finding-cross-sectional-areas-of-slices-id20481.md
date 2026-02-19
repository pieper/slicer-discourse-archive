---
topic_id: 20481
title: "Finding Cross Sectional Areas Of Slices"
date: 2021-11-03
url: https://discourse.slicer.org/t/20481
---

# Finding Cross-Sectional Areas of Slices

**Topic ID**: 20481
**Date**: 2021-11-03
**URL**: https://discourse.slicer.org/t/finding-cross-sectional-areas-of-slices/20481

---

## Post #1 by @Katie_V (2021-11-03 17:56 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11</p>
<p>Hello! I am trying to see if I can slice a 3d vessel reconstruction within 3D slicer, and then find the cross-sectional areas of each of those slices.</p>
<p>I am aware that I can extract the centerline and then find the centerline metrics to get the diameter of each slice, but is it possible to do this for cross-sectional area instead? I heard that the Sandbox extension may work for this, but I’m not sure how to use it.</p>
<p>Thank you for the help.</p>

---

## Post #2 by @chir.set (2021-11-03 19:08 UTC)

<aside class="quote no-group" data-username="Katie_V" data-post="1" data-topic="20481">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/katie_v/48/12991_2.png" class="avatar"> Katie_V:</div>
<blockquote>
<p>is it possible to do this for cross-sectional area instead</p>
</blockquote>
</aside>
<p>If you install Slicer preview 4.13, you could do that with SlicerVMTK ‘Cross section analysis’ module. Former ‘Centerline metrics’ module has been merged with it.</p>
<p>Slicer 4.13 is tagged ‘preview’ but is as stable as 4.11.</p>
<p>Alternatively, you could download <a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">SlicerVMTK</a> as a zip file, unpack it and point to the different modules in applications settings.</p>
<p>But all here would advise to use Slicer 4.13.</p>

---
