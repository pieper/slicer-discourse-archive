# Threshold disappearing after clicking apply.

**Topic ID**: 42003
**Date**: 2025-03-07
**URL**: https://discourse.slicer.org/t/threshold-disappearing-after-clicking-apply/42003

---

## Post #1 by @Victoria_Effanga (2025-03-07 03:47 UTC)

<p>How can I fix the issue where my threshold disappears after applying it in version 5.8.0?</p>

---

## Post #2 by @lassoan (2025-03-07 03:52 UTC)

<p>Thresholding preview is shown for the entire current slice view content. However, even you click Apply, masking settings are applied and only in the extents of the current segmentation. You can change the masking settings to allow modifications in the region you want to paint; and make sure your segmentation includes the current slice (you can use the “Specify geometry” button to change the extents of the segmentation).</p>

---
