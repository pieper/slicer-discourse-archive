# Export as a separate DICOM series the sagittal reconstruction, from axial DICOM series

**Topic ID**: 11514
**Date**: 2020-05-13
**URL**: https://discourse.slicer.org/t/export-as-a-separate-dicom-series-the-sagittal-reconstruction-from-axial-dicom-series/11514

---

## Post #1 by @Klaas (2020-05-13 05:34 UTC)

<p>Operating system: Win 10<br>
Slicer version: 4.10.2<br>
Expected behavior: I’m a novice to the tool, please help on how one can export as a separate DICOM series the sagittal/coronal reconstruction, from axial DICOM series. Thanks in advance.</p>
<p>Actual behavior:</p>

---

## Post #2 by @Tedd (2021-09-06 11:46 UTC)

<p>I was wondering and trying to figure out the same issue but I didnt find a solution.</p>

---

## Post #3 by @pieper (2021-09-07 17:39 UTC)

<p>If you start with DICOM data, you can <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/OrientScalarVolume">reorient the pixels</a> and then export the DICOM using the right-click context menu in the Data module.</p>

---
