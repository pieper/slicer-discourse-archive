---
topic_id: 33961
title: "Overwrite Existing Segments When Copying A New Segment"
date: 2024-01-25
url: https://discourse.slicer.org/t/33961
---

# Overwrite existing segments when copying a new segment

**Topic ID**: 33961
**Date**: 2024-01-25
**URL**: https://discourse.slicer.org/t/overwrite-existing-segments-when-copying-a-new-segment/33961

---

## Post #1 by @rphellan2210 (2024-01-25 05:16 UTC)

<p>Hello,</p>
<p>I have a vtkSegmentation with vtkSegments. When I use the method CopySegmentFromSegmentation(segmentation, segmentId), the corresponding vtkSegment is copied and overlaps the existing vtkSegments in the original vtkSegmentation.</p>
<p>Is there a way to overwrite the existing vtkSegments when copying a new vtkSegment, instead of overlapping?</p>
<p>Renzo</p>

---

## Post #2 by @lassoan (2024-01-25 14:54 UTC)

<p>Copying is different operation than painting. It will not affect any existing segments. If you want to make all segments overwrite the segments before them in the segment list, you can flatten the segmentation into a single layer. If you want to keep overlapping segments and just make some segments overwrite others then you can use the “Logical operators” effect.</p>

---

## Post #3 by @rphellan2210 (2024-01-26 02:23 UTC)

<p>Thank you, Andras. I decided to copy the vtkSegment and then subtract it from all other already existing vtkSegments.</p>

---
