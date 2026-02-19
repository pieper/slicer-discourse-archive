---
topic_id: 28147
title: "How Can I Create 3D Dcm File With 2D Image"
date: 2023-03-02
url: https://discourse.slicer.org/t/28147
---

# How can I create 3D dcm file with 2d image?

**Topic ID**: 28147
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/how-can-i-create-3d-dcm-file-with-2d-image/28147

---

## Post #1 by @annkyotou (2023-03-02 21:14 UTC)

<p>Hi, everyone.<br>
I am from the field of civil engineering. I would like to create 3D continuous .dcm files from a series of 2d .tiff files. How should I do this?<br>
Are .dcm files only generated from specific devices (e.g. CT scans)?</p>

---

## Post #2 by @lassoan (2023-03-03 05:55 UTC)

<p>I would recommend to load the series of 2D TIFF files using ImageStacks module of SlicerMorph extension. You can then save the image as a volume file (nrrd, mha, nii, … formats).</p>
<p>Exporting to DICOM image is possible but can lead to complications. Why would you like to export your 3D image into DICOM?</p>

---
