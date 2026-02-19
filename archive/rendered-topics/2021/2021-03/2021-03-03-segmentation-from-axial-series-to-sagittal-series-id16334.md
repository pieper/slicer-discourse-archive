---
topic_id: 16334
title: "Segmentation From Axial Series To Sagittal Series"
date: 2021-03-03
url: https://discourse.slicer.org/t/16334
---

# Segmentation from axial series to sagittal series

**Topic ID**: 16334
**Date**: 2021-03-03
**URL**: https://discourse.slicer.org/t/segmentation-from-axial-series-to-sagittal-series/16334

---

## Post #1 by @linhu (2021-03-03 15:34 UTC)

<p>Operating system: Windows 10<br>
Slicer version: Slicer 4.11.20200930</p>
<p>Hi guys,</p>
<p>I have both the axial and sagittal DICOM series with the same Frame of Reference UID, so they are spatially related. I also have an .nrrd file that contains the segmentation of an organ using the axial series as the volume. This segmentation was completed by ITK-SNAP. My question is how do I resample the axial segmentation on slicer so that it matches the sagittal series volume? I want to export an .nrrd file in the same size as the sagittal series.</p>
<p>Thank you for your help!</p>

---

## Post #2 by @pieper (2021-03-03 20:48 UTC)

<p>I think you should be able to do that with the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html">Segmentation geometry</a> option.  Load the axial version and then switch it to use the sagittal.  If the axial and sagittal have different spacing between the slices (e.g. 3mm up and down and 3mm side to side but 1mm in plane) then you may get data loss, so you’ll need to experiment.</p>

---
