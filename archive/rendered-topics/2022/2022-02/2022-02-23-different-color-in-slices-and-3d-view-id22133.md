# Different color in slices and 3D view

**Topic ID**: 22133
**Date**: 2022-02-23
**URL**: https://discourse.slicer.org/t/different-color-in-slices-and-3d-view/22133

---

## Post #1 by @bserrano (2022-02-23 16:14 UTC)

<p>Hi all,</p>
<p>Is it posible to use different colors for the same segment (one for the slices and one for the 3D view)?</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2022-02-24 07:13 UTC)

<p>There are several ways to achieve showing the same segmentation with different colors in different views.</p>
<ul>
<li>Option A: If you don’t want to do any Python scripting then you need to clone the segmentation, drag-and-drop a different node in the slice and the 3D view and change the color of one of the nodes.</li>
<li>Option B: Create a new segmentation display node, add it as a display node to the segmentation node (the segmentation will have two display nodes), set the override color for the segment, and set the view node ID of the 3D view (to make this secondary display node only show the segmentation in the 3D view).</li>
</ul>

---

## Post #3 by @bserrano (2022-02-25 09:45 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>and change the color of one of the nodes</p>
</blockquote>
</aside>
<p>I tryied the first option. I can see the segmentations in different colors but I cannot edit both at the same time. That is, I change the segmentation in slice view but the change is not in 3D view. I thought that the cloned segmentation would be modified aswell.</p>
<p>Am I doing something wrong or it is not possible to edit the cloned segmentation at the same time?</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2022-02-25 14:59 UTC)

<p>Option A is simple but changes are not automatically applied. You need Option B if you keep changing the segmentation.</p>

---

## Post #5 by @bserrano (2022-02-28 12:01 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="22133">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Create a new segmentation display node, add it as a display node to the segmentation node (the segmentation will have two display nodes), set the override color for the segment, and set the view node ID of the 3D view (to make this secondary display node only show the segmentation in the 3D view).</p>
</blockquote>
</aside>
<p>Now it works!<br>
The code i have used is:</p>
<pre><code class="lang-auto"># Create a new segmentation display node
slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationDisplayNode")

# Add it as a display node to the segmentation node
segmentationNode.AddAndObserveDisplayNodeID(displayNode_copy.GetID())

# Set the override color for the segment
segmentID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName("coronary")
displayNode_copy.SetSegmentOverrideColor(segmentID, 1, 0.7, 0)
displayNode_copy.SetVisibility2D(0)

# Set the view node ID of the 3D view
viewNode_new = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLViewNode")
displayNode_copy.SetViewNodeIDs(viewNode_new)
slicer.app.layoutManager().threeDWidget(0).setMRMLViewNode(viewNode_new)

</code></pre>

---

## Post #6 by @Fokatu (2023-12-16 12:43 UTC)

<p>Hi Iassoan,<br>
Could you please help me check the code below? I want to show the data in both Red and Green view, with different displaynode, such that I can change the display seperately. But it does not work.</p>
<pre><code class="lang-auto">import numpy as np
x = np.random.randn(512, 512)
volumeNode = slicer.mrmlScene.AddNewNodeByClassWithID("vtkMRMLScalarVolumeNode", "ScanData", "vtkMRMLScalarVolumeNodeScanData")
slicer.util.updateVolumeFromArray(volumeNode, x)

d1 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeDisplayNode")
d2 = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeDisplayNode")

volumeNode.AddAndObserveDisplayNodeID(d1.GetID())
volumeNode.AddAndObserveDisplayNodeID(d2.GetID())

v1 = slicer.util.getNode("Red Display")
v2 = slicer.util.getNode("Green Display")
d1.SetViewNodeIDs(v1)
d2.SetViewNodeIDs(v2)
</code></pre>

---
