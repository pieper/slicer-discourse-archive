# Brain volume using CT images

**Topic ID**: 16349
**Date**: 2021-03-04
**URL**: https://discourse.slicer.org/t/brain-volume-using-ct-images/16349

---

## Post #1 by @Gonzalo_Rojas_Costa (2021-03-04 03:27 UTC)

<p>How can I compute the brain volume (brain segmentation) using CT images?</p>

---

## Post #2 by @lassoan (2021-03-04 03:39 UTC)

<p>First you need to segment the brain. For example, you can use SwissSkullStripper extension for this. Then you can use Label statistics module (for labelmap volumes) or Segment statistics module (for segmentations) to get the volume.</p>

---
