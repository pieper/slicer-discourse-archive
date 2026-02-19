---
topic_id: 35268
title: "Cross Sectional Image To Reconstruct"
date: 2024-04-03
url: https://discourse.slicer.org/t/35268
---

# cross-sectional image to reconstruct

**Topic ID**: 35268
**Date**: 2024-04-03
**URL**: https://discourse.slicer.org/t/cross-sectional-image-to-reconstruct/35268

---

## Post #1 by @ypd04474 (2024-04-03 22:27 UTC)

<p>Hello.<br>
I have a cross-sectional image of some nanostructure.<br>
Cross-sectional images were taken continuously at equal intervals in a direction perpendicular to the cross-section.<br>
I would like to do 3D reconstruction using these jpg files.<br>
I was wondering where to start and if there would be a suitable module.</p>

---

## Post #2 by @muratmaga (2024-04-03 22:55 UTC)

<p>You can use ImageStacks module of SlicerMorph extension to import a sequence of bitmap files. You do need to enter the spacing information of the voxels (x, y, z axes)</p>
<p>See the tutorial here: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks">Tutorials/ImageStacks at main · SlicerMorph/Tutorials (github.com)</a></p>

---

## Post #3 by @ypd04474 (2024-04-04 14:04 UTC)

<p>Thank you for your quick and informative answer.<br>
In addition, I would like to ask how I can export the data made in 3d to a cad file (ex.stl).</p>

---

## Post #4 by @muratmaga (2024-04-04 14:15 UTC)

<p>You need to segment your structure. Please read the segmentation section of the Slicer user manual at <a href="https://slicer.readthedocs.io">https://slicer.readthedocs.io</a></p>

---

## Post #5 by @ypd04474 (2024-04-08 02:40 UTC)

<p>Thanks a lot<br>
First, i tried to follow the tutorial but i cannot find the video tutorial at all…<br>
(<a href="https://discourse.slicer.org/t/new-video-tutorial-for-segment-editor-lumbar-spine-segmentation-for-3d-printing/700" class="inline-onebox">New video tutorial for Segment editor - lumbar spine segmentation for 3D printing</a>)</p>
<p>So I was going to refer to a few youtube. But the bar setting of threshold range is not active. I’m curious about the reason why it is not active…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/62a3f74016f7e131e4c19cf7986007572aafb64a.png" data-download-href="/uploads/short-url/e4C5ppJQVRK1ejcMqeg4NOQKe14.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62a3f74016f7e131e4c19cf7986007572aafb64a_2_403x500.png" alt="image" data-base62-sha1="e4C5ppJQVRK1ejcMqeg4NOQKe14" width="403" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62a3f74016f7e131e4c19cf7986007572aafb64a_2_403x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62a3f74016f7e131e4c19cf7986007572aafb64a_2_604x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/2/62a3f74016f7e131e4c19cf7986007572aafb64a_2_806x1000.png 2x" data-dominant-color="C7C7D0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">856×1061 110 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>have a nice day!</p>

---

## Post #6 by @pieper (2024-04-08 21:16 UTC)

<p>Practice first with the data from the tutorials.  Then if there’s a step that you can get to work, share the exact steps you did together with the data needed to reproduce any issues.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a></p>

---
