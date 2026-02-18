# Computing skull symmetry from DICOM

**Topic ID**: 20245
**Date**: 2021-10-19
**URL**: https://discourse.slicer.org/t/computing-skull-symmetry-from-dicom/20245

---

## Post #1 by @Tvinet (2021-10-19 17:01 UTC)

<p>Hi, is there any functionality available in 3D slicer or any other tools to find the symmetric plane of skulls (after segmentation) from DICOM files?</p>

---

## Post #2 by @lassoan (2021-10-19 23:58 UTC)

<p>There a number of ways to achieve this in Slicer. The basic idea is that you cut out a surface patch, mirror it, and register it to the other side of the skull. If you need a reflection plane then you can fit a plane on midpoints of the original and transformed points of the surface patch.</p>
<p>What is the clinical goal? Correction of facial deformity, assessment of facial symmetry, …?</p>

---

## Post #3 by @Tvinet (2021-10-23 13:17 UTC)

<p>Thanks for the reply. The goal is to assess the symmetry of the skull using some metric (ex: Hausdorff distance).  For this, I first want to extract the reflection plane. Is there a way to automate this for a large number of skulls?</p>

---

## Post #4 by @lassoan (2021-10-23 14:23 UTC)

<p>Ok, this simplifies things. You don’t need the plane of symmetry then. You can simply register the mirrored surface to the original and then compute surface distance using “Model to model distance extension”. You can get the distances as a numpy array and compute any metrics you need - min/max/mean/95th percentile of the distance etc.</p>

---

## Post #5 by @lili-yu22 (2021-11-23 04:36 UTC)

<p>hi，would you tell me that in 3d slicer which extension to register the mirror surface patch to the other side of the skull，thank you</p>

---

## Post #6 by @lassoan (2021-11-23 06:48 UTC)

<p>You can use Surface Registration module in SlicerIGT extension for registering two models.</p>

---

## Post #7 by @lili-yu22 (2021-11-24 12:39 UTC)

<p>thank you very much，l will try.</p>

---
