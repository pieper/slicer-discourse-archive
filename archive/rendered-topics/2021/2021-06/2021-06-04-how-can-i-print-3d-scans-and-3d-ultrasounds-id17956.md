---
topic_id: 17956
title: "How Can I Print 3D Scans And 3D Ultrasounds"
date: 2021-06-04
url: https://discourse.slicer.org/t/17956
---

# How can I print 3d scans and 3d ultrasounds

**Topic ID**: 17956
**Date**: 2021-06-04
**URL**: https://discourse.slicer.org/t/how-can-i-print-3d-scans-and-3d-ultrasounds/17956

---

## Post #1 by @MANUANGO1102 (2021-06-04 15:46 UTC)

<p>Hi, I want to print on 3D human joint scanners and 3D/4D ultrasounds of pregnant women after the third trimester of pregnancy. Can you help me how can I do it?</p>

---

## Post #2 by @lassoan (2021-06-04 21:04 UTC)

<p>First you need to import the images. This is the most tricky part. SlicerHeart extensiom can load 3D/4D ultrasound images from a number of vendors, but not all. See details <a href="https://github.com/SlicerHeart/SlicerHeart#importing-dicom-files">here</a>.</p>
<p>Then, you need to segment the image n Segment Editor module. Thresholding followed by smoothing, manual corrections using Paint and Scissors effect should produce good result. Maybe you can also use SurfaceWrapSolidify extension (it adds WrapSolidify effect to the segment editor) to remove internal holes from the segmentation.</p>
<p>You can also export the segmentation as STL for 3D printing.</p>

---

## Post #3 by @MANUANGO1102 (2021-06-04 22:04 UTC)

<p>Thank you very much, friend!</p>

---
