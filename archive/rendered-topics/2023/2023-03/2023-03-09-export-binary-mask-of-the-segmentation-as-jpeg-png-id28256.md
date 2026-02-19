---
topic_id: 28256
title: "Export Binary Mask Of The Segmentation As Jpeg Png"
date: 2023-03-09
url: https://discourse.slicer.org/t/28256
---

# Export binary mask of the segmentation as jpeg/png

**Topic ID**: 28256
**Date**: 2023-03-09
**URL**: https://discourse.slicer.org/t/export-binary-mask-of-the-segmentation-as-jpeg-png/28256

---

## Post #1 by @yoav_benhaim (2023-03-09 09:44 UTC)

<p>hi!<br>
how can I export the segmentation as a binary image?<br>
the preference file format is jpeg or png/ but other format can also help<br>
thank you</p>

---

## Post #2 by @muratmaga (2023-03-09 17:09 UTC)

<p>Right click, and choose Export as LabelMap. Then, you can save as NRRD or Nifti basde on your usage. Slicer does not allow exporting 3D volumes as sequences of 2D formats (like JPG). You should be able to do DICOM, though.</p>

---

## Post #3 by @ahmad_alminnawi (2024-04-18 10:06 UTC)

<p>Hi Yoav,</p>
<p>Were you able to export the segmentation as binary image?<br>
Can you please share how you did it? (preferably through jupyter Notebook)</p>
<p>thanks in advance!</p>

---
