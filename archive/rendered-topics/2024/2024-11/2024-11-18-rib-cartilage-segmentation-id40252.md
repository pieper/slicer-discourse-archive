# rib cartilage segmentation

**Topic ID**: 40252
**Date**: 2024-11-18
**URL**: https://discourse.slicer.org/t/rib-cartilage-segmentation/40252

---

## Post #1 by @Vanessa (2024-11-18 18:16 UTC)

<p>How can I do the segmentation of the rib cartilage and measure the volume of the 7th and 8th rib cartilage? I need the volume to measure the degree of calcification for a study.</p>

---

## Post #2 by @pieper (2024-11-18 18:40 UTC)

<p>If you are working from CT the TotalSegmentator module or Auto3DSeg module should give you a start.</p>
<p>e.g. this model: <a href="https://github.com/lassoan/SlicerMONAIAuto3DSeg/releases/tag/ModelsTestResults#:~:text=Entire%20costal%20cartilage-,Ribs%20TS2%20(v2.0.0),-class_map_part_ribs%3A%20Trained%20on" class="inline-onebox">Release 3D Slicer MONAI Auto3DSeg models · lassoan/SlicerMONAIAuto3DSeg · GitHub</a></p>

---

## Post #3 by @Vanessa (2025-01-20 08:39 UTC)

<p>Thank you, now I have the total volume. Do you have an idea how I get the calcification volume in between the cartilage? Because for my study I need the total volume of each rib cartilage and the volume of the calcification in the cartilage?</p>

---
