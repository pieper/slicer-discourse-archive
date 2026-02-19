---
topic_id: 35157
title: "Segment Statistics Out Of Frame Regions"
date: 2024-03-28
url: https://discourse.slicer.org/t/35157
---

# Segment Statistics - Out of Frame regions

**Topic ID**: 35157
**Date**: 2024-03-28
**URL**: https://discourse.slicer.org/t/segment-statistics-out-of-frame-regions/35157

---

## Post #1 by @speled (2024-03-28 17:41 UTC)

<p>Hello,<br>
My segment ROI is the whole brain white matter (from a brain atlas). In some cases the scalar volume MRI data is not whole brain (limited # of slices). Will the statistics exclude the ‘Out of Frame’ areas of the ROI, or assume they are zeros?<br>
Thank you!</p>

---

## Post #2 by @lassoan (2024-04-09 03:14 UTC)

<p>Scalar volume statistics only computes statistics on that part of the segmentation that overlaps the volume. See details in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html">documentation</a>.</p>

---
