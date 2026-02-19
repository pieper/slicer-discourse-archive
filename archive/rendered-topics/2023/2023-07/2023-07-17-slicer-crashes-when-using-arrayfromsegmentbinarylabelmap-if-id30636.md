---
topic_id: 30636
title: "Slicer Crashes When Using Arrayfromsegmentbinarylabelmap If"
date: 2023-07-17
url: https://discourse.slicer.org/t/30636
---

# Slicer crashes when using arrayFromSegmentBinaryLabelmap if segment is too small

**Topic ID**: 30636
**Date**: 2023-07-17
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-using-arrayfromsegmentbinarylabelmap-if-segment-is-too-small/30636

---

## Post #1 by @kkkkkkk123 (2023-07-17 11:22 UTC)

<p>Hello, I am trying to use arrayFromSegmentBinaryLabelmap, but when my segmentation is too small (e.g. just a few voxels), 3D Slicer crashes. Is there any way to prevent this? Can I extract information about the size of segmentation before converting it to an array?</p>

---

## Post #2 by @lassoan (2023-07-17 17:51 UTC)

<p>Could you provide sample data and/or more detailed instructions that would allow us to reproduce this?</p>

---

## Post #3 by @kkkkkkk123 (2023-07-18 14:34 UTC)

<p>I seem to have fixed the issue! I did not include these two lines before converting the segmentation to an array</p>
<pre><code class="lang-auto">segmentationNode.CreateDefaultDisplayNodes()
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)
</code></pre>

---
