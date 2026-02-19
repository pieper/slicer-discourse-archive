---
topic_id: 35975
title: "Updating Segmentation Using Numpy And Transforms"
date: 2024-05-07
url: https://discourse.slicer.org/t/35975
---

# Updating segmentation using numpy and transforms

**Topic ID**: 35975
**Date**: 2024-05-07
**URL**: https://discourse.slicer.org/t/updating-segmentation-using-numpy-and-transforms/35975

---

## Post #1 by @metrobobbi (2024-05-07 22:34 UTC)

<p>Hello,<br>
I downloaded some Contrast-enhanced CT scans and I used the Curved Planar Reformat extension in order to generate a straight volume of the aorta.<br>
I have the need to edit the segmentations on the straightened space and, for instance, delete the first half of the vessel.<br>
What I tried is the following:</p>
<pre><code class="lang-auto">
straight_volume_node = slicer.util.getNode("straight_volume_node")
seg_node = slicer.util.getNode("segmenation")
straighteningTransformNode = slicer.util.getNode("straighteningTransform")

seg_node.SetAndObserveTransformNodeID(straighteningTransformNode.GetID())

aorta_array = arrayFromSegmentBinaryLabelmap(seg_node, "aorta", straight_volume_node)

#suppose the shape is (200,400,400)

aorta_array[100:,:,:] = 0

slicer.util.updateSegmentBinaryLabelmapFromArray(
                 aorta_array,
                 seg_node,
                 "aorta",
                 straight_volume_node,
             )

seg_node.SetAndObserveTransformNodeID(None)
</code></pre>
<p>However, this does not work, the segmentation is not aligned with the original volume.<br>
How can I fix this ?</p>

---
