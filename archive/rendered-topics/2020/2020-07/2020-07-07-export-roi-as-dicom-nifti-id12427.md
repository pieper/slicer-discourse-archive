# Export ROI as DICOM & NiFTI?

**Topic ID**: 12427
**Date**: 2020-07-07
**URL**: https://discourse.slicer.org/t/export-roi-as-dicom-nifti/12427

---

## Post #1 by @esultcase (2020-07-07 19:15 UTC)

<p>Does Slicer have the ability to segment an MRI &amp; export the ROI in both DICOM &amp; NiFTI file formats?</p>
<p>I’m using Slicer version 4.10.2 on Mac.</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2020-07-07 19:18 UTC)

<p>Yes, you can segment using <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">Segment Editor module</a> and export to DICOM using <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export">DICOM module</a>.</p>
<p>I would recommend to save segmentation into nrrd format and not nifti, but if you must use nifti then you can export segmentation to labelmap volume (right-click on it in Data module) and you can save the resulting labelmap as nifti.</p>

---
