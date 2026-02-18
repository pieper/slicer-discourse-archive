# Threshold segmentation of intracranial hemorrhage foci

**Topic ID**: 29017
**Date**: 2023-04-20
**URL**: https://discourse.slicer.org/t/threshold-segmentation-of-intracranial-hemorrhage-foci/29017

---

## Post #1 by @duan (2023-04-20 03:32 UTC)

<p>Excuse me,May I confirm that the threshold for segmenting intracranial hemorrhage lesions using threshold segmentation in the segment editor is 40-100?</p>

---

## Post #2 by @lassoan (2023-04-20 03:41 UTC)

<p>In clinical CT images that Slicer loads the voxel values are in Hounsfield Unit, so the value range of 40-100 sounds about right for hemorrhage. However, due to image noise, partial volume effect, and other image artifacts, you will not be able to clearly separate hemorrhage from surrounding structures that all have very similar intensity range.</p>
<p>If you cannot acquire better images (e.g., using MRI and/or contrast agent) then you can use semi-automatic segmentation tools, such as “Grow from seeds” effect in Segment Editor to segment the hemorrhage.</p>

---
