---
topic_id: 37196
title: "Aligning Segmented Tumor Volumes Across Mri Sequences"
date: 2024-07-04
url: https://discourse.slicer.org/t/37196
---

# Aligning Segmented Tumor Volumes Across MRI Sequences 

**Topic ID**: 37196
**Date**: 2024-07-04
**URL**: https://discourse.slicer.org/t/aligning-segmented-tumor-volumes-across-mri-sequences/37196

---

## Post #1 by @Matthias_Anders (2024-07-04 15:21 UTC)

<p>Hello everyone,</p>
<p>I work with MRI data using different contrast sequences (referred to as sequences). I’m facing an issue with aligning segmented tumor volumes across these sequences. Initially, I loaded and segmented tumors on one sequence where they were clearly visible. I saved these segmentations along with the corresponding volume as ‘Segmentation.seg.nrrd’ and ‘0000.nrd’ respectively.</p>
<p>When I load these files, the segmentations overlay perfectly on the anatomical image as expected. However, when I load the segmentations with other sequences (which were not active during segmentation), there is a significant offset.</p>
<p>Manually registering these segmentations to each sequence is impractical due to the large number of patients in my dataset. While I know tools like BRAINS can perform registration, I believe the spatial relationship among all sequences should be stored somwhere in the data. Is there a method or tool in 3D Slicer that can extract and apply this spatial information to align the segmented tumor volumes across different sequences automatically?</p>
<p>Any help or advice would be greatly appreciated!</p>
<p>Best regards,<br>
Matthias</p>

---

## Post #2 by @pieper (2024-07-05 16:58 UTC)

<p>If you import via dicom, your MRI sequences should relate to Series in dicom terminology.  They should generally be in the same space if the share the Frame of Reference UID.  If they still don’t line up it’s probably due to patient movement or that they come from different studies.</p>

---
