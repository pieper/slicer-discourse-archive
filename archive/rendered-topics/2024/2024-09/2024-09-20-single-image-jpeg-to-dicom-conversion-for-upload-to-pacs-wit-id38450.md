# Single image JPEG to DICOM conversion for upload to PACS with patient information

**Topic ID**: 38450
**Date**: 2024-09-20
**URL**: https://discourse.slicer.org/t/single-image-jpeg-to-dicom-conversion-for-upload-to-pacs-with-patient-information/38450

---

## Post #1 by @Brian (2024-09-20 01:55 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Looking for a replacement for K-pacs. Can 3D slicer convert single image JPEGs to DICOM, add in patient name, MRN number DOB, DOS, for upload to patients file in PACS?</p>
<p>-Brian</p>

---

## Post #2 by @pieper (2024-09-20 13:03 UTC)

<p>Yes, you can do that using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html">Slicer GUI</a> and even configure to push to PACS if your institution allows that.  If you are doing a lot of these it might be easier to do with a script.</p>

---
