# Exporting DICOM and JPEG files directly from 3D slicer

**Topic ID**: 20998
**Date**: 2021-12-10
**URL**: https://discourse.slicer.org/t/exporting-dicom-and-jpeg-files-directly-from-3d-slicer/20998

---

## Post #1 by @Aisha (2021-12-10 13:18 UTC)

<p>Hi all!</p>
<p>I have annotated some brain MRI images in 3D slicer and would like to know how can I export those annotated 2D and 3D images in DICOM or any other format. I would like to know a direct method of exporting so I can use the images to train Machine Learning algorithms.</p>
<p>I hope to hear from you soon.</p>

---

## Post #2 by @Aisha (2021-12-10 13:18 UTC)

<p>Hi all!</p>
<p>I am annotating brain MRI images in 3D slicer but when I export those images to binary label maps, some overlapping layers do not convert.<br>
I would like to know how to solve this issue.</p>
<p>Thanks</p>

---

## Post #3 by @lassoan (2021-12-10 13:28 UTC)

<p>I would recommend to export to .seg.nrrd file format. It preserves the segmentation’s geometry (origin, spacing, axis directions, extents), supports overlapping labels, and can store essential metadata, such segment names, colors, terminology.</p>
<p>You can then use <a href="https://pypi.org/project/slicerio/" class="inline-onebox">slicerio · PyPI</a> package in your machine learning scripts to get the voxels of each segment as a numpy array and access all metadata.</p>

---
