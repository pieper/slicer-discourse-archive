---
topic_id: 34887
title: "Are Measurements In Slicer Calculated By The Dicom File How"
date: 2024-03-14
url: https://discourse.slicer.org/t/34887
---

# Are measurements in slicer calculated by the DICOM file? How do you know it is accurate?

**Topic ID**: 34887
**Date**: 2024-03-14
**URL**: https://discourse.slicer.org/t/are-measurements-in-slicer-calculated-by-the-dicom-file-how-do-you-know-it-is-accurate/34887

---

## Post #1 by @bw3232 (2024-03-14 11:27 UTC)

<p>Hi All,</p>
<p>When using 3d Slicer’s ruler/ markdown tools, I was wondering how the measurement is actually calculated. Is the relative scale captured in the DICOM file? (For example, how does 3D slicer know what 1mm is on each subject).</p>

---

## Post #2 by @lassoan (2024-03-17 02:09 UTC)

<p>Yes, full 3D geometry (origin, spacing, axis directions) are specified in the DICOM files.</p>

---
