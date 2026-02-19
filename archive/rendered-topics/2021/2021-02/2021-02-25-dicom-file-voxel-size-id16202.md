---
topic_id: 16202
title: "Dicom File Voxel Size"
date: 2021-02-25
url: https://discourse.slicer.org/t/16202
---

# DICOM file, voxel size

**Topic ID**: 16202
**Date**: 2021-02-25
**URL**: https://discourse.slicer.org/t/dicom-file-voxel-size/16202

---

## Post #1 by @jhostage (2021-02-25 05:31 UTC)

<p>Hello - wondering if anyone knows if voxel size in DICOM file of US images will be maintained if the DICOM file is converted to a NIfTI file using slicer.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2021-02-25 05:34 UTC)

<p>It depends on the ultrasound image. 3D volumes and single-region 2D image sequences should be good.</p>
<p>Unless you work with brain images, I would recommend to use the general-purpose nrrd file format instead of nifti, which is mainly intended for storing brain MRI.</p>

---
