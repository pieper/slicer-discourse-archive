---
topic_id: 23960
title: "Cross Sectional Image View Along 3D Curve E G Vessel Center"
date: 2022-06-20
url: https://discourse.slicer.org/t/23960
---

# Cross-sectional image view along 3D-curve (e.g. vessel center line)

**Topic ID**: 23960
**Date**: 2022-06-20
**URL**: https://discourse.slicer.org/t/cross-sectional-image-view-along-3d-curve-e-g-vessel-center-line/23960

---

## Post #1 by @DocJoe (2022-06-20 11:40 UTC)

<p>Hello all,<br>
I would love to get a hint, if there is already a tool that allows me to display a cross-section image perpendicular to a 3D-curve (e.g.e center line).<br>
So far, I found great tools for detecting center lines - but not for cross-sectional images along a curve.<br>
My goal is to produce a video along the a 3D-curve.<br>
Thanks for any hints or help to get started.<br>
Joachim</p>

---

## Post #2 by @chir.set (2022-06-20 12:36 UTC)

<p>Have you extracted the centerline in Slicer or externally ?</p>
<p>In any case, if you have a surface and a corresponding centerline, you can install SlicerVMTK extension using the ‘Extensions manager’, and display a slice view perpendicular to the centerline using ‘Cross-section analysis’ module.</p>
<p>To make a video, you may need to record a ‘Sequence’ first, then the ‘Screen capture’ module.</p>

---

## Post #3 by @lassoan (2022-06-21 04:37 UTC)

<p>To get a list of cross-sectional images as a 3D array (that you can play as a movie using “Screen Capture” module’s slice sweep mode; or just save as a numpy array) you can use <a href="https://github.com/PerkLab/SlicerSandbox#curved-planar-reformat">Curved Planar Reformat module</a> in Sandbox extension.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="yi07mjr3JeU" data-video-title="New vessel branch extraction module for 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=yi07mjr3JeU" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/yi07mjr3JeU/maxresdefault.jpg" title="New vessel branch extraction module for 3D Slicer" width="" height="">
  </a>
</div>


---

## Post #4 by @DocJoe (2022-06-21 04:40 UTC)

<p>Thanks… that will help!</p>

---

## Post #5 by @lassoan (2023-03-21 02:05 UTC)



---
