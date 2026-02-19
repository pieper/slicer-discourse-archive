---
topic_id: 4318
title: "Import Contours Dicom From Medis Into Slicer"
date: 2018-10-08
url: https://discourse.slicer.org/t/4318
---

# Import contours/dicom from Medis into Slicer

**Topic ID**: 4318
**Date**: 2018-10-08
**URL**: https://discourse.slicer.org/t/import-contours-dicom-from-medis-into-slicer/4318

---

## Post #1 by @Savine (2018-10-08 12:05 UTC)

<p>I have drawn my contours already with Medis suite and saved these contours as .con flie or .dicom file. Can I import these contours into slicer to create a 3D volume?</p>

---

## Post #2 by @lassoan (2018-10-08 14:34 UTC)

<p>Slicer can read segmentation/contours from DICOM RT structure sets (using SlicerRT extension) and DICOM segmentation object (using Quantitative Reporting extension). If Medis can save segmentation into one of these formats then you should be able to read it into Slicer using DICOM module.</p>

---
