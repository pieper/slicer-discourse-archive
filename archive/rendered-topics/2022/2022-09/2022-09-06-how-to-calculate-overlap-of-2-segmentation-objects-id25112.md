# How to calculate %overlap of 2 segmentation objects

**Topic ID**: 25112
**Date**: 2022-09-06
**URL**: https://discourse.slicer.org/t/how-to-calculate-overlap-of-2-segmentation-objects/25112

---

## Post #1 by @n3ubie (2022-09-06 00:22 UTC)

<p>Hi! I am new to Slicer, and am trying to do segmentation of objects in MRI head. I would like to compare the overlap of 2 manual segmentation objects, how should I go about in doing it in the segmentation statistics?</p>
<p>Also would you recommend working with dicom or nii for best result?</p>

---

## Post #2 by @cpinter (2022-09-06 12:27 UTC)

<p>You can use the Logical operators tool in the Segment Editor module then get the volume in Segment Statistics.</p>

---

## Post #3 by @lassoan (2022-09-06 14:01 UTC)

<p>You can also find some segment comparison metrics in Segment Comparison module (provided by SlicerRT extension).</p>

---
