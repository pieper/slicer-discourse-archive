---
topic_id: 47535
title: "Crop segmentations with bounding box"
date: 2026-07-02
url: https://discourse.slicer.org/t/47535
last_bumped: 2026-07-07T02:40:07.733Z
---

# Crop segmentations with bounding box

**Topic ID**: 47535
**Date**: 2026-07-02
**URL**: https://discourse.slicer.org/t/crop-segmentations-with-bounding-box/47535

---

## Post #1 by @sulli419 (2026-07-02 17:33 UTC)

<p>Are there any tools for cropping segments as readily as volumes?  Ideally, similar to volume cropping, I’d like to render my segments in 3D and adjust a bounding box where all segment labels outside are deleted.  Thanks</p>

---

## Post #2 by @cpinter (2026-07-03 09:23 UTC)

<p>I think the simplest is to use the Scissors tool with the rectangle option. Alternatively you can export the segmentation as a labelmap and then crop the volume.</p>

---

## Post #3 by @aiden.zhu (2026-07-07 02:40 UTC)

<p>Good to combine Segment-Editor (slicer.qMRMLSegmentEditorWidget()) and self.cv_roi = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsROINode”) to have a customized module. So after all segments ready, take the Source-Volume’s dimensions as ROI-node’s initial settings; manually adjust ROIs for cropping, then apply the cropping as a mask to all segments…good to keep all original segments, have those masked segments to be new ones.</p>

---
