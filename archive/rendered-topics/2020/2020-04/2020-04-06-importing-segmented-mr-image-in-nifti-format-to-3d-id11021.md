# Importing segmented MR image in NIfTI format to 3D

**Topic ID**: 11021
**Date**: 2020-04-06
**URL**: https://discourse.slicer.org/t/importing-segmented-mr-image-in-nifti-format-to-3d/11021

---

## Post #1 by @Bassam (2020-04-06 21:03 UTC)

<p>Hi,</p>
<p>I am experiencing a problem in importing mask file in NIfTI format, which is segmented using ITK SNAP, to the 3D slicer for extracting the features. I converted the extension to DICOM format, but unfortunately the problem still exist.</p>
<p>Please any idea on how to  sort this problem out ? and thanks</p>

---

## Post #2 by @lassoan (2020-04-06 23:15 UTC)

<p>If you use a recent Slicer Preview Release, then you can choose Description-&gt;Segmentation in the Add data dialog to load the file directly as segmentation.</p>
<p>In older Slicer versions, you can load the nifti file as labelmap volume (check “Show options” and check “Labelmap” to force loading the image as a labelmap image instead of a grayscale image) and then convert it to segmentation (by right-clicking on it in Data module).</p>

---

## Post #3 by @lassoan (2020-05-12 18:52 UTC)

<p>A post was split to a new topic: <a href="/t/misalignment-between-nifti-image-and-mask/11507">Misalignment between Nifti image and mask</a></p>

---
