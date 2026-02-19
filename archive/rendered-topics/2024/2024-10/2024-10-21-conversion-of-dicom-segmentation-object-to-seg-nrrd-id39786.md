---
topic_id: 39786
title: "Conversion Of Dicom Segmentation Object To Seg Nrrd"
date: 2024-10-21
url: https://discourse.slicer.org/t/39786
---

# Conversion of DICOM Segmentation object to .seg.nrrd

**Topic ID**: 39786
**Date**: 2024-10-21
**URL**: https://discourse.slicer.org/t/conversion-of-dicom-segmentation-object-to-seg-nrrd/39786

---

## Post #1 by @DaanB (2024-10-21 23:33 UTC)

<p>Hey everyone,<br>
For the past couple of days I have been in the process of trying to convert a set of DICOM Segmentation object files to .seg.nrrd. I have a custom Slicer extension where users need to iterate through some cases to review; using DICOMs this is incredibly slow and therefore, I have tried to figure out a way to automatically convert these DICOM Segmentation objects to .seg.nrrd with Python, but so far I have not had any success. The DICOMs contain overlapping segments, which seems to be the biggest issue. Anyone with any experience on this matter on how to do this neatly? Thank you so much in advance.</p>

---

## Post #2 by @lassoan (2024-10-21 23:35 UTC)

<p>DICOM Segmentation objects are loaded as segmentations if you install the QuantitativeReporting extension. Overlapping segments should be handled without any issues. You can find code snippets to automate all the steps in Python in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>.</p>

---
