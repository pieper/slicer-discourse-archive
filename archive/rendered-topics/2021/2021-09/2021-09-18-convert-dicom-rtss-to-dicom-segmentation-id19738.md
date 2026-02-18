# Convert DICOM RTSS to DICOM segmentation

**Topic ID**: 19738
**Date**: 2021-09-18
**URL**: https://discourse.slicer.org/t/convert-dicom-rtss-to-dicom-segmentation/19738

---

## Post #1 by @piegou (2021-09-18 15:59 UTC)

<p>Hi,<br>
I want to convert structures in DICOM-RTSS format to DICOM seg format.<br>
Is it possible with Slicer-3D?If yes how<br>
thank you for helping me</p>

---

## Post #2 by @lassoan (2021-09-18 17:23 UTC)

<p>If you install the SlicerRT extension then you can import DICOM RT Structure Set, and if you install Quantitive Reporting extension then you can export it as DICOM Segmentation Object. See <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html">DICOM module documentation</a> for details.</p>

---

## Post #3 by @piegou (2021-09-20 20:21 UTC)

<p>I imported a CT scan with its segmentation in RTSS format.<br>
Despite the installation of the Slicer RT and Quantitative Reporting modules, I cannot find how to export the segmentation in DICOM segmentation format. I saw that it was possible to export it in NIFTI format for example but the viewer that I will use afterwards only allows the DICOM segmentation format.<br>
I am a beginner with Slicer3D, thank you for answering the first post and I hope this one too.</p>

---

## Post #4 by @lassoan (2021-09-23 03:00 UTC)

<p>You need to first load the segmentation into the scene and then <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/dicom.html#export-data-from-the-scene-to-dicom-database">export it to DICOM</a>. In the “DICOM export” window, choose Select export type → DICOMSegmentation.</p>

---
