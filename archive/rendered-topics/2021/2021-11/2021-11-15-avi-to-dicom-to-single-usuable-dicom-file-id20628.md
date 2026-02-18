# AVI to DICOM to single usuable DICOM file

**Topic ID**: 20628
**Date**: 2021-11-15
**URL**: https://discourse.slicer.org/t/avi-to-dicom-to-single-usuable-dicom-file/20628

---

## Post #1 by @Chuns_SS (2021-11-15 19:53 UTC)

<p>HI I received 3 AVI files of a CT scan, one axial and one coronal etc. I am able to convert the AVI files to crude DICOM files but is there anyway to combine them to a single DICOM file.</p>

---

## Post #2 by @lassoan (2021-11-15 21:52 UTC)

<p>Single-file CT volumes (Enhanced CT Image information objects) are very rare. For better compatibility, it is probably better to export in the usual one slice per file format. You can do that as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">here</a>.</p>

---

## Post #3 by @Chuns_SS (2021-11-17 01:03 UTC)

<p>As always many thanks for the guidance.</p>

---
