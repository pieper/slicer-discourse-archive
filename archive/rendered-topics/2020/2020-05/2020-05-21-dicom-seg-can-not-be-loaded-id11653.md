---
topic_id: 11653
title: "Dicom Seg Can Not Be Loaded"
date: 2020-05-21
url: https://discourse.slicer.org/t/11653
---

# DICOM SEG can not be loaded 

**Topic ID**: 11653
**Date**: 2020-05-21
**URL**: https://discourse.slicer.org/t/dicom-seg-can-not-be-loaded/11653

---

## Post #1 by @chiarapalu (2020-05-21 17:04 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11 or 4.10<br>
Expected behavior: Loading of Dicom Segmentation Objects exported from Commercial software BrainLab (Elements)<br>
Actual behavior: Error message: Could not load objects as DicomSegmentation slicer.<br>
I already have the following extension installed: SlicerRT, Quantitative Reporting, DCMQI, SlicerDevelopmentToolbox, PETDICOMExtension.</p>
<p>Thanks for any help!</p>

---

## Post #2 by @pieper (2020-05-31 22:17 UTC)

<p>Quantitative Reporting extension should be able to handle that.  We have tested back-and-forth segmentation before with BrainLab, but I’m not sure the exact software version.</p>
<p>It would be great if you could generate some segmentations using public sample data and share them for debugging.</p>

---
