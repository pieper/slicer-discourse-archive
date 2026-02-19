---
topic_id: 39798
title: "Editing 2D Existing Segmentations"
date: 2024-10-22
url: https://discourse.slicer.org/t/39798
---

# Editing 2D existing segmentations 

**Topic ID**: 39798
**Date**: 2024-10-22
**URL**: https://discourse.slicer.org/t/editing-2d-existing-segmentations/39798

---

## Post #1 by @cscanla (2024-10-22 14:54 UTC)

<p>Hi there! I’m encountering some issues when trying to edit existing segmentations. I am importing volumes and segmentations that are only one slice thick. When I try to edit, the entire segmentation disappears. These segmentations are extracted from segmentations made on the entire scan using TotalSegmentator in 3D Slicer.</p>
<p>I have checked that my segmentations are imported as labelmaps. I understand that 3D slicer is meant for 3D data, but I’m wondering why my segmentations can’t be edited. The dimensionalities are 3D, they just have a depth of 1. Any input would be helpful. Thank you!</p>

---

## Post #2 by @lassoan (2024-10-22 14:56 UTC)

<p>We can have a look if you can share a sample data set and describe the exact steps you perform, what you expect to happen, and what happens instead.</p>

---

## Post #3 by @cpinter (2024-10-22 15:38 UTC)

<p>When you say it disappears do you mean it disappears from 3D or from 2D as well? Because it is possible that with the default settings the labelmap to closed surface conversion results in an empty polydata for 3D. If this is the case, please try turning off smoothing in Segment Editor. If it disappears also from the 2D view, then there is surely some other problem, which we need to investigate more.</p>

---
