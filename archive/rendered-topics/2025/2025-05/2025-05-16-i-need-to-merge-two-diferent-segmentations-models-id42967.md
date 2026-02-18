# I need to merge two diferent segmentations models

**Topic ID**: 42967
**Date**: 2025-05-16
**URL**: https://discourse.slicer.org/t/i-need-to-merge-two-diferent-segmentations-models/42967

---

## Post #1 by @Azambuja (2025-05-16 12:52 UTC)

<p>I have two different DICOM files, and they complement each other. I made the first segmentation in Slicer using the first model, then the second one, and now I need to complete my 3D model by merging the two segmentations. The second issue I haven’t been able to resolve is that I exported some files with 15% opacity, but in the OBJ and STL models, the segmentation with 15% opacity appears as 100% opacity.</p>

---

## Post #2 by @lassoan (2025-05-16 12:54 UTC)

<p>You can drag-and-drop segments between segmentations in Data module. You can then merge the segments in Segment Editor module, using the “Logical operators” effect.</p>

---
