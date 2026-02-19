---
topic_id: 8976
title: "From Tomosynthesis Images Can 3D Slicer Create A Good 3D Ima"
date: 2019-10-31
url: https://discourse.slicer.org/t/8976
---

# From tomosynthesis images, can 3D Slicer create a good 3D image?

**Topic ID**: 8976
**Date**: 2019-10-31
**URL**: https://discourse.slicer.org/t/from-tomosynthesis-images-can-3d-slicer-create-a-good-3d-image/8976

---

## Post #1 by @leemailbox (2019-10-31 19:24 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.10.2<br>
Expected behavior: Clean 3D rendering of structures (e.g., bones, body contour)<br>
Actual behavior: Fuzzy, indistinct rendering of structures</p>
<p>I have a set of DICOM images obtained on a tomosynthesis unit. Slicer 3D imports the dataset. However, the 3D Slicer renders a 3D image that is poor quality. What are the tricks to handling data obtained from tomosynthesis. Thanks!</p>

---

## Post #2 by @lassoan (2019-11-04 04:27 UTC)

<p>Do you expect to see better quality image? Does the imaging system’s own software show less noisy image? Can you post a few example screenshots? What would you like to do with the image: segment, register, 3D print, …?</p>
<p>If there is no image export or import errors then probably the best you can do is to apply noise filtering on the image; or segment structures using Segment Editor module and smooth the segmentation result.</p>

---
