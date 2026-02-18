# How to fast check if a voxel is part of a visible segment

**Topic ID**: 15068
**Date**: 2020-12-15
**URL**: https://discourse.slicer.org/t/how-to-fast-check-if-a-voxel-is-part-of-a-visible-segment/15068

---

## Post #1 by @Niels (2020-12-15 08:27 UTC)

<p>For my paintbrush module I am making continuously making adjustments to a volume . I use this same volume as a reference volume in my segmentation.<br>
In my adjustment script I would like to keep my adjustments limited to the segments I have set visible in the segmentation.</p>
<p>I know that I can export the segmentation to a labelmap. But is it also possbile to directly access a binairy map to check if a certain location is part of a visible segment or not?</p>
<p>I found GetBinaryLabelmapInternalRepresentation in the vtkMRMLSegmentationNode but that seems to work for only one segmentID and not an array of segments.</p>

---
