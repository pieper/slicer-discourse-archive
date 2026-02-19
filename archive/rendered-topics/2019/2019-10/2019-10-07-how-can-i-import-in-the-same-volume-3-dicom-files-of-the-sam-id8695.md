---
topic_id: 8695
title: "How Can I Import In The Same Volume 3 Dicom Files Of The Sam"
date: 2019-10-07
url: https://discourse.slicer.org/t/8695
---

# How can I import in the same volume 3 DICOM files of the same volume

**Topic ID**: 8695
**Date**: 2019-10-07
**URL**: https://discourse.slicer.org/t/how-can-i-import-in-the-same-volume-3-dicom-files-of-the-same-volume/8695

---

## Post #1 by @valeriofaraone (2019-10-07 16:42 UTC)

<p>Hi I am having a problem with the DICOM import, I have 3 DICOM files: the coronal, the axial and the sagittal MRI of the same patient.<br>
The problem is that when I add these 3 DICOM files, Slicer3D dislpays them in 3 different volumes while i have to see them in 1 volume so I can start to segment.</p>

---

## Post #2 by @lassoan (2019-10-07 17:51 UTC)

<p>Quite often 3 anisotropic MRI images are acquired (high resolution along two axes, very low resolution along a third axis) to reduce time spent in the MRI scanner. However, these images are not well suited for 3D segmentation. See more information here: <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">Combining volumes - what am I missing? </a>. To reduce artifacts caused by low-resolution third axis you can follow the technique explained here: <a href="https://discourse.slicer.org/t/segmenting-issue-i-cant-remove-ridges-in-3-d-model/4792/5">Segmenting Issue: I Can’t Remove “ridges” in 3-D model </a></p>

---
