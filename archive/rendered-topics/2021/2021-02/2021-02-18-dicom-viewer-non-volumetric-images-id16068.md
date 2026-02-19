---
topic_id: 16068
title: "Dicom Viewer Non Volumetric Images"
date: 2021-02-18
url: https://discourse.slicer.org/t/16068
---

# DICOM viewer - non-volumetric images

**Topic ID**: 16068
**Date**: 2021-02-18
**URL**: https://discourse.slicer.org/t/dicom-viewer-non-volumetric-images/16068

---

## Post #1 by @Shai (2021-02-18 21:23 UTC)

<p>Operating system:Win 10<br>
Slicer version:4.11.20200930</p>
<p>Hi, I want to upload non-volumetric DICOM images to the viewer for ROI marking. When I upload the images , Slicer by default upload them as volumetric. How can I upload the images in their original DICOM format (i.e. with gaps). Thanks</p>

---

## Post #2 by @lassoan (2021-02-18 21:38 UTC)

<p>Slicer can reconstruct volumetric image regardless of acquisition type or slice thickness, by using nearest neighbor or linear interpolation between slices.</p>
<p>Have you been just wondering why a solid volume is displayed or do you actually need to see black bands between thin slices?</p>

---

## Post #3 by @Shai (2021-02-18 21:42 UTC)

<p>I need to view  slice by slice without the solid volume display. Can I cancel Slicer volumetric reconstruction?</p>

---

## Post #4 by @lassoan (2021-02-18 21:49 UTC)

<p>Yes, sure, you can view slice by slice: switch to “Red slice only layout”. As you browse between slices, you will jump between slice centers, so you will only see the original acquired slices.</p>
<p>If you want to avoid even the chance of ever seeing an interpolated slice (even if you use multiple orthogonal views) then you can disable interpolated view in the slice view by clicking <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#slice-view">interpolation button</a>.</p>
<p>What kind of images do you work with? What is the distance between slice centers? What is the slice thickness?</p>

---

## Post #5 by @Shai (2021-02-19 08:08 UTC)

<p>I mark the ROI on T2\T2-FLAIR images. 2-4 mm slice thickness,<br>
The “red slice only layout” works.<br>
Thanks.</p>

---
