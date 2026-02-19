---
topic_id: 25884
title: "3Dview Linkedcontrolon Off Behavior Issue"
date: 2022-10-25
url: https://discourse.slicer.org/t/25884
---

# 3DView LinkedControlOn/Off behavior issue

**Topic ID**: 25884
**Date**: 2022-10-25
**URL**: https://discourse.slicer.org/t/3dview-linkedcontrolon-off-behavior-issue/25884

---

## Post #1 by @Long_Zhang (2022-10-25 03:14 UTC)

<p>I am rendering two (different) volumes in two 3DView using python in an extension module. Each volume was configured with its own camera settings.</p>
<p>My intended behavior is the two 3DView has a linked behavior, e.g. the same rotation (only) operated using mouse in the 1st 3DView is applied to the 2nd 3DView (without mouse interaction there). However, I found that an extra translational transformation is added in the second 3Dview. So the volume showing in the 2nd 3DView become invisible in the display port.</p>
<p>Any hints or suggestions to make this working as I expected?</p>

---

## Post #2 by @lassoan (2022-10-25 03:14 UTC)

<p>I cannot reproduce the behavior that you describe. Could you please provide a screen capture video or at least a few screenshots?</p>

---

## Post #3 by @Long_Zhang (2022-10-25 03:45 UTC)

<p>Sorry, my fault: my version is 4.13.0-2022-01-16-linux, a previouse release version.</p>
<p>This is the initial views (different volumes centered in the views):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa85d83c7f5f81a2062935bcbfb4376cd763e280.jpeg" data-download-href="/uploads/short-url/zKe7XXBasYdNRhm22SYN3wY34TS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa85d83c7f5f81a2062935bcbfb4376cd763e280_2_690x351.jpeg" alt="image" data-base62-sha1="zKe7XXBasYdNRhm22SYN3wY34TS" width="690" height="351" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa85d83c7f5f81a2062935bcbfb4376cd763e280_2_690x351.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa85d83c7f5f81a2062935bcbfb4376cd763e280_2_1035x526.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa85d83c7f5f81a2062935bcbfb4376cd763e280.jpeg 2x" data-dominant-color="111211"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1372×698 104 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After click in the right upper view (the two views were LinkedControlOn). The volume dispeared:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d5bd313425492cf3373a2712015687569e07bae.jpeg" data-download-href="/uploads/short-url/6tgdAUQiASDAPoDXU0Fs7Yrdax0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d5bd313425492cf3373a2712015687569e07bae_2_689x349.jpeg" alt="image" data-base62-sha1="6tgdAUQiASDAPoDXU0Fs7Yrdax0" width="689" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d5bd313425492cf3373a2712015687569e07bae_2_689x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/d/2d5bd313425492cf3373a2712015687569e07bae_2_1033x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d5bd313425492cf3373a2712015687569e07bae.jpeg 2x" data-dominant-color="151615"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1371×695 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After rotation (volume shows up in the right bottom view):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad946ea2e9d3ce8900702ffc75fc5752272962f0.jpeg" data-download-href="/uploads/short-url/oLyCfbcZweVUIYkUgSkIzKIZDiw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad946ea2e9d3ce8900702ffc75fc5752272962f0_2_690x346.jpeg" alt="image" data-base62-sha1="oLyCfbcZweVUIYkUgSkIzKIZDiw" width="690" height="346" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad946ea2e9d3ce8900702ffc75fc5752272962f0_2_690x346.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad946ea2e9d3ce8900702ffc75fc5752272962f0_2_1035x519.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad946ea2e9d3ce8900702ffc75fc5752272962f0.jpeg 2x" data-dominant-color="272B22"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1369×688 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>My guess is that the volume was translated by the first click in the right top view.</p>

---

## Post #4 by @lassoan (2022-10-25 04:01 UTC)

<p>Please always test the latest Slicer Stable Release before you ask a question or report an issue. The behavior may have been improved since your version was built.</p>
<p>If I understand well, you would like to synchronize the camera orientation only. The built-in linking feature links all the camera parameters, including camera and focal point positions, so you cannot focus on different points in 3D space. Instead, you can either translate all the volumes to be centered at the same physical position. Or, you can add an observer to a camera and whenever a camera parameter changes update the other 3D view’s camera accordingly.</p>

---

## Post #5 by @Long_Zhang (2022-10-25 04:08 UTC)

<p>OK. Got the point. And thank you very much for the alternatives. I will try and report their results later.</p>

---

## Post #6 by @Long_Zhang (2022-10-25 04:15 UTC)

<p>It looks that the camera way is better as it self-constrained in current issue. The modification of volumes might have consequences somewhere else.</p>

---
