---
topic_id: 13509
title: "Segmentation Size"
date: 2020-09-16
url: https://discourse.slicer.org/t/13509
---

# Segmentation size

**Topic ID**: 13509
**Date**: 2020-09-16
**URL**: https://discourse.slicer.org/t/segmentation-size/13509

---

## Post #1 by @MAM (2020-09-16 20:08 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>
<p>I’d like to save my segmentation with the same size in nifti format. When I go through Segmentation\ export\advanced and choose a reference volume, I can’t save in nifti format. And when I go through Data\export to binary labelmap it does not give me the same size. How can I save the segmentation in nifti format with the reference volume size???</p>

---

## Post #2 by @lassoan (2020-09-17 00:21 UTC)

<p>We have made this very easy in recent Slicer Preview Releases.</p>
<p>Use “Export to files” section in Segmentations module and choose nifti format. If you For convenience, the same export feature is directly available in Segment Editor module, too, in the drop-down menu of “Segmentations…” button.</p>
<p>Note that nifti format is developed specifically for brain imaging. For general-purpose image storage, I would recommend nrrd file format instead. If you want to</p>

---
