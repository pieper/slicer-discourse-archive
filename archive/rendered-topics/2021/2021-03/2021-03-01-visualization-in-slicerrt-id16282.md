---
topic_id: 16282
title: "Visualization In Slicerrt"
date: 2021-03-01
url: https://discourse.slicer.org/t/16282
---

# Visualization in SlicerRT

**Topic ID**: 16282
**Date**: 2021-03-01
**URL**: https://discourse.slicer.org/t/visualization-in-slicerrt/16282

---

## Post #1 by @loubna (2021-03-01 10:27 UTC)

<p>Is there a specific type of medical images that must be used in SlicerRT,  because  the segmentation performed in 3D slicer and exported as DICOM-RT for other purposes like 3D reconstruction often fails especially with intricate geometries.</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2021-03-01 13:03 UTC)

<p>DICOM RT structure set is not suitable for storing arbitrarily complex shapes (especially with lots of holes or concavities), because the standard mandates the use of keyhole technique for specifying holes in a cross-section and correspondence between contour points in neighbor cross-sections is poorly defined.</p>
<p>For general-purpose segmentation storage, yiu can use DICOM Segmentation Object.</p>

---
