---
topic_id: 40324
title: "3D Dose Visualization From Rtdose Dicom File"
date: 2024-11-21
url: https://discourse.slicer.org/t/40324
---

# 3D dose visualization from RTdose DICOM file

**Topic ID**: 40324
**Date**: 2024-11-21
**URL**: https://discourse.slicer.org/t/3d-dose-visualization-from-rtdose-dicom-file/40324

---

## Post #1 by @wlstraube (2024-11-21 22:26 UTC)

<p>Is it possible to show a 3D dose distribution with a 3D view of CTs and Contours?</p>

---

## Post #2 by @lassoan (2024-11-21 22:27 UTC)

<p>Yes, sure. If you install SlicerRT extension then DICOM RT structure sets, RT dose volumes, RT images, RT plans should show up when you load an RT study in the DICOM browser.</p>

---

## Post #3 by @wlstraube (2024-11-21 22:31 UTC)

<p>Andre,</p>
<p>Thank you for your assistance.</p>
<p>I was hoping to generate dose clouds for the 3D view, but it appears that only Isodose lines can be plotted in the 3D view. Is that correct?</p>
<p>Bill</p>

---

## Post #4 by @lassoan (2024-11-21 22:43 UTC)

<p>You can display the dose volume as a cloud in the 3D view by drag-and-dropping the dose volume to a 3D view. You can further tune its visualization settings in Volume Rendering module.</p>

---
