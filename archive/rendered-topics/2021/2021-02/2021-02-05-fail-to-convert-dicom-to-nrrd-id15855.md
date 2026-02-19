---
topic_id: 15855
title: "Fail To Convert Dicom To Nrrd"
date: 2021-02-05
url: https://discourse.slicer.org/t/15855
---

# Fail to convert DICOM to nrrd

**Topic ID**: 15855
**Date**: 2021-02-05
**URL**: https://discourse.slicer.org/t/fail-to-convert-dicom-to-nrrd/15855

---

## Post #1 by @ecgt (2021-02-05 02:46 UTC)

<p>Operating system:Windows<br>
Slicer version:4.11.20200930 r29402 / 002be18</p>
<p>Expected behavior:convert to nrrd<br>
Actual behavior<br>
E: can’t determine ‘PhotometricInterpretation’ of decompressed image<br>
E: mandatory attribute ‘PhotometricInterpretation’ is missing or can’t be determined<br>
E: can’t change to unencapsulated representation for pixel data</p>

---

## Post #2 by @lassoan (2021-02-05 03:19 UTC)

<p>This DICOM object does not seem to contain valid image data. Do you expect this file to contain valid image data? What software generated this file?</p>

---
