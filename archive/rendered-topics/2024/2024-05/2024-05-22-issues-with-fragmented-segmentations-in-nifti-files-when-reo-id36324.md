---
topic_id: 36324
title: "Issues With Fragmented Segmentations In Nifti Files When Reo"
date: 2024-05-22
url: https://discourse.slicer.org/t/36324
---

# Issues with Fragmented Segmentations in NIfTI Files when Reopening in 3D Slicer

**Topic ID**: 36324
**Date**: 2024-05-22
**URL**: https://discourse.slicer.org/t/issues-with-fragmented-segmentations-in-nifti-files-when-reopening-in-3d-slicer/36324

---

## Post #1 by @hfri (2024-05-22 13:33 UTC)

<p>I am using the Segmentation Editor in 3D Slicer to create multiple versions of segmentations for the same objects (rough versions, smoothed versions). After creating these overlapping segmentations, I save them as .nii (NIfTI) file. However, when I reopen the .nii file in 3D Slicer, some of the segmentations appear fragmented, showing only parts of the rim of the original segmentation instead of the complete segments.</p>

---

## Post #2 by @lassoan (2024-05-22 13:37 UTC)

<p>If you use “auto-complete” effects such as “Grow from seeds” or “Fill between slices”, you need to click “Apply” button in the effect if you want to save the results that are shown as a preview into the segmentation.</p>
<p>I would not recommend using NIFTI format. It is developed for storing brain MRI images and it has lots of issues and limitations when used for anything else. You can use NRRD file format instead, which is much simpler and more flexible.</p>

---

## Post #3 by @hfri (2024-05-22 16:30 UTC)

<p>I see, thank you very much!</p>

---
