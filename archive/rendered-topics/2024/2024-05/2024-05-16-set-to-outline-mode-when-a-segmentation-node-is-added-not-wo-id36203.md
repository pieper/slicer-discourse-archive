---
topic_id: 36203
title: "Set To Outline Mode When A Segmentation Node Is Added Not Wo"
date: 2024-05-16
url: https://discourse.slicer.org/t/36203
---

# Set to outline mode when a segmentation node is added, NOT WORKING

**Topic ID**: 36203
**Date**: 2024-05-16
**URL**: https://discourse.slicer.org/t/set-to-outline-mode-when-a-segmentation-node-is-added-not-working/36203

---

## Post #1 by @mrlongzhang (2024-05-16 08:35 UTC)

<p>I used the follow code in .slicerrc.py to modify the default behavior of slicer 2D slice (up to 5.6.x)  to display in outline mode instead of in filled mode for a segmentation.</p>
<pre><code class="lang-auto">def SetOutline(caller,event):
  for node in slicer.util.getNodes("*").values():
    if node.IsA("vtkMRMLSetmentationDisplayNode"):
      node.SetAllSegmentsVisibility2DOutline(1)
      node.SetAllSegmentsVisibility2DFill(0)

slicer.mrmlScene.AddObserver(slicer.mrmlScene.NodeAddedEvent, SetOutline)
</code></pre>
<p>However, I noticed that it always failed to switch to outline mode when drag-n-drop a segmentation file into the client area after a scalar volume file. However, it may switch to outline mode if I first drop a segmentation and then a volume file.</p>
<p>What is the root cause of such behavior? And what is the solution to this issue? A workaround is also highly appreciated!</p>
<p>Thx in advance!</p>

---

## Post #2 by @cpinter (2024-05-16 08:39 UTC)

<aside class="quote no-group" data-username="mrlongzhang" data-post="1" data-topic="36203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrlongzhang/48/15286_2.png" class="avatar"> mrlongzhang:</div>
<blockquote>
<p>vtkMRMLSetmentationDisplayNode</p>
</blockquote>
</aside>
<p>First of all, there is a typo in this, ‘t’ =&gt; ‘g’</p>

---

## Post #3 by @lassoan (2024-05-16 12:37 UTC)

<p>I would recommend to change this in the default segmentation display node. You can find examples in the script repository how to change default nodes in the scene.</p>

---

## Post #4 by @mrlongzhang (2024-05-17 02:50 UTC)

<p>The code posted here was wrong. But this is not the root cause as I mentioned in the text, it works when you first drop a seg instead of a vol.</p>

---

## Post #6 by @mrlongzhang (2024-05-17 02:59 UTC)

<p>this is not working. in 4.13, there is no any hints. however, in 5.6, it nicely gives a hint: [VTK] vtkMRMLSegmentationDisplayNode::GetSegmentIDs: No segmentation node is associated to this display node</p>
<p>it looks like that segmentation display node has dependency issues on data: it can not be correctly constructed/configured w/o a segmentation node.</p>

---

## Post #7 by @cpinter (2024-05-17 09:00 UTC)

<aside class="quote no-group" data-username="mrlongzhang" data-post="6" data-topic="36203">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mrlongzhang/48/15286_2.png" class="avatar"> mrlongzhang:</div>
<blockquote>
<p>display node has dependency issues on data: it can not be correctly constructed/configured w/o a segmentation node</p>
</blockquote>
</aside>
<p>Correct. A display node controls the display properties of a data node, so without a data node it has no reason to exist. Usually you can make sure a display node exists after creating/accessing the data node by calling <code>CreateDefaultDisplayNodes()</code> on the data node, and then you can get it by calling <code>GetDisplayNode()</code>.</p>

---
