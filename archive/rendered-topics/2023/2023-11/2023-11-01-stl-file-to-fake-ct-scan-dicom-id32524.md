# STL file to fake CT scan/DICOM?

**Topic ID**: 32524
**Date**: 2023-11-01
**URL**: https://discourse.slicer.org/t/stl-file-to-fake-ct-scan-dicom/32524

---

## Post #1 by @BlakeSlicer (2023-11-01 12:34 UTC)

<p>I have a STL of a segmented bone. I would like to convert the STL back to a CT scan as a DICOM to be used in another software which processes images.</p>
<p>I’ve imported the STL files as a segmentation and can now scroll though the slices of the STL part as if it was a CT scan.</p>
<p>Can I save these slices as DICOM?</p>

---

## Post #2 by @AsliBeriL (2023-11-01 14:25 UTC)

<p>Excuse me, the topic seems very interesting. How did you do that?</p>

---

## Post #3 by @lassoan (2023-11-02 03:02 UTC)

<p>Yes, you can export the image to DICOM as described in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">DICOM module documentation</a>.</p>

---
