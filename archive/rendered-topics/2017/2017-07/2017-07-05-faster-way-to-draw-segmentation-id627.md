---
topic_id: 627
title: "Faster Way To Draw Segmentation"
date: 2017-07-05
url: https://discourse.slicer.org/t/627
---

# Faster way to draw Segmentation?

**Topic ID**: 627
**Date**: 2017-07-05
**URL**: https://discourse.slicer.org/t/faster-way-to-draw-segmentation/627

---

## Post #1 by @jks1995 (2017-07-05 13:41 UTC)

<p>Hello,</p>
<p>I am trying to draw a segmentation in the slicer scene based on user clicks, but I find that the process of rendering the segment takes too long. I am using the code below to turn my label map into a segmentation, but I find that it runs quite slowly. Does anyone have an idea how I can speed this process up or different methods I could use to accomplish the same goal?</p>
<code>
segmentation = segment.GetSegmentation()
while segmentation.GetNumberOfSegments() &gt; 0:
segmentation.RemoveSegment(segmentation.GetNthSegment(0))
<p>slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(label_map, segment)<br>
segmentation = self.view_seg.GetSegmentation()<br>
segment = segmentation.GetSegment(segmentation.GetNthSegmentID(0))<br>
</p></code>

---

## Post #2 by @lassoan (2017-07-05 19:51 UTC)

<p>What is taking too long time? Interactive editing or the code snippet that you included?</p>
<p>You can make interactive editing faster by deleting the closed surface representation disable smoothing (click Update button in the representation list, closed surface representation row, set smoothing to 0).</p>

---
