# Remove parts of volume outside the segmentation

**Topic ID**: 31925
**Date**: 2023-09-27
**URL**: https://discourse.slicer.org/t/remove-parts-of-volume-outside-the-segmentation/31925

---

## Post #1 by @Windy (2023-09-27 03:21 UTC)

<p>I have a dataset containing unwanted particles, and I’ve created a segmentation mask to identify and exclude them. Is it possible to utilize this segmentation mask to effectively remove the unwanted particles from the original dataset and thereby clean it?</p>

---

## Post #2 by @muratmaga (2023-09-27 03:35 UTC)

<p>Yes, you need to use the MaskVolume effect of the segment editor.</p>

---
