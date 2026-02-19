---
topic_id: 11356
title: "How To Get The Color Of Segments From The Segmentation Node"
date: 2020-04-29
url: https://discourse.slicer.org/t/11356
---

# How to get the color of segments from the segmentation node

**Topic ID**: 11356
**Date**: 2020-04-29
**URL**: https://discourse.slicer.org/t/how-to-get-the-color-of-segments-from-the-segmentation-node/11356

---

## Post #1 by @xlucox (2020-04-29 23:33 UTC)

<p>Hello,</p>
<p>I wonder how can I get the colors of the segments which belong to a segmentation node.</p>
<p>Thank you very much.</p>

---

## Post #2 by @Sunderlandkyl (2020-04-30 00:38 UTC)

<p>Try this:</p>
<pre><code class="lang-auto">segmentationNode = getNode("Segmentation")
segment = segmentationNode.GetSegmentation().GetSegment("Segment_1")
segment.GetColor()
</code></pre>

---
