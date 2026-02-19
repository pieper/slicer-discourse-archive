---
topic_id: 6102
title: "Windows Look Blurred Compared To Other Segmentation Applicat"
date: 2019-03-11
url: https://discourse.slicer.org/t/6102
---

# Windows look blurred compared to other segmentation applications

**Topic ID**: 6102
**Date**: 2019-03-11
**URL**: https://discourse.slicer.org/t/windows-look-blurred-compared-to-other-segmentation-applications/6102

---

## Post #1 by @Leon (2019-03-11 09:58 UTC)

<p>Hello,</p>
<p>I thinking about switching over from my standard segmentation application (which is Mimics) to 3DSlicer. Normaly I’m used to see all my slices pixelated, but 3DSlicer shows them blurred.<br>
Other applications I’m using also give my pixelated views.</p>
<p>Is there some way that I can turn this off?</p>
<p>Regards,<br>
Léon</p>

---

## Post #2 by @pieper (2019-03-11 12:13 UTC)

<p>Yes, use the Interpolation button:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/MainApplicationGUI#Slice_Viewers" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/MainApplicationGUI#Slice_Viewers</a></p>

---

## Post #3 by @pieper (2019-03-11 12:14 UTC)

<p>By the way <a class="mention" href="/u/leon">@Leon</a> thanks for the feedback - let us know if there are features you liked about other packages that we should consider working on in Slicer.</p>

---

## Post #4 by @lassoan (2019-03-11 13:05 UTC)

<aside class="quote no-group" data-username="Leon" data-post="1" data-topic="6102">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>Normaly I’m used to see all my slices pixelate</p>
</blockquote>
</aside>
<p>Voxels are created from continuous signal by sampling on a grid. When the image is displayed, it is possible to reconstruct the original continuous signal without data loss from these finite samples (only those details are lost that are higher than half of the spatial frequency of the sampling).</p>
<p>Therefore, <strong>showing the raw data samples (as a pixelated image) is not the most accurate representation of the data</strong>. This becomes very apparent when you show non-axis-aligned views (you can see very obvious sampling artifacts).</p>
<p>Slicer’s default display mode, using <strong>linear interpolation, shows an image that is a much better approximation of the original image signal</strong>. “Blurring” limits the displayed details to that can be represented at the current image sampling resolution.</p>
<p>It may be tempting to turn off interpolation so that you can see the voxel size. However, if you are concerned about voxel size that indicates that the details that you are interested in may not be reliably represented at the current resolution. This situation should be avoided. Preferably, by acquiring the image at higher resolution. If that is not possible then by resampling the image (typically by using <em>Crop and Resample volume</em> module).</p>
<p>In summary: For most of the time, I would recommend working with more accurately reconstructed, continuous (“blurred”) image. Showing the discrete image samples temporarily, can be useful as a diagnostic tool.</p>

---
