---
topic_id: 15769
title: "Export Segmentation"
date: 2021-02-01
url: https://discourse.slicer.org/t/15769
---

# Export Segmentation

**Topic ID**: 15769
**Date**: 2021-02-01
**URL**: https://discourse.slicer.org/t/export-segmentation/15769

---

## Post #1 by @oliversaldanha (2021-02-01 10:48 UTC)

<p>Operating system: Windows 10<br>
Slicer version:3D Slicer 4.11.20200930<br>
I am very new to the 3D slicer software. I need support to decide which format should I export the segmentation if I need to train the 2D slice with the segmentation to extract the features.<br>
I would prefer to export the segmentation in the .csv format.<br>
Can I get some guidance on how can I proceed?<br>
Thanks in advance</p>

---

## Post #2 by @lassoan (2021-02-01 14:30 UTC)

<p>CSV format for storing an image would be extremely inefficient (probably reading the file would take 100x longer time than reading it from a binary file format). For saving an save preprocessed (resample, cropped, aligned, etc.) segmentations for AI training, you can use .npy (numpy save).</p>
<p>For archiving - permanent storage of the segmentation and images, preserving all essential metadata - I would recommend .nrrd (for sharing between projects within the same group) or DICOM (for sharing between different institutions).</p>

---

## Post #3 by @oliversaldanha (2021-02-01 14:49 UTC)

<p>Hello,<br>
I tried using .nrrd file format and it was really useful and server my purpose.<br>
Thanks a lot for the support.<br>
Regards<br>
Oliver</p>

---
