---
topic_id: 18802
title: "Iterating Through Segments In A Segmentation Node"
date: 2021-07-19
url: https://discourse.slicer.org/t/18802
---

# Iterating through segments in a segmentation Node

**Topic ID**: 18802
**Date**: 2021-07-19
**URL**: https://discourse.slicer.org/t/iterating-through-segments-in-a-segmentation-node/18802

---

## Post #1 by @Griffin (2021-07-19 19:26 UTC)

<p>I know this has got to be something obvious that I’m not getting but I’ve spent a really long time longer for the answer and I can’t seem to find it. If I have a segmentation node loaded in and saved as a variable, how can I iterate through its segments in python? Thank you</p>

---

## Post #2 by @jamesobutler (2021-07-19 20:33 UTC)

<p>You can get a segment object if you know the segment index in the segmentation node that you want.  This <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array" rel="noopener nofollow ugc">example</a> includes a way to get a segment id by segment name.</p>
<p>You could also use methods available in the vtkSegmentation object such as <code>GetNumberOfSegments</code> as a way to get the number of indices to then use with <code>getNthSegment</code>. See <a href="https://apidocs.slicer.org/master/classvtkSegmentation.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer: vtkSegmentation Class Reference</a>.</p>

---

## Post #3 by @Griffin (2021-07-19 20:35 UTC)

<p>Great! Thank you, the GetNumberOfSegments method is exactly the type of thing I was looking for!</p>

---

## Post #4 by @Griffin (2021-07-20 16:55 UTC)

<p>I’m sorry but for the life of me I cannot figure out how to use the vtkSegmentation class in my python code. Do you have any advice for how to implement it? Thank you</p>

---

## Post #5 by @rbumm (2021-07-20 17:28 UTC)

<p>Hi,</p>
<p>Just a short example: This fragment of python code will iterate through all currently loaded segment nodes and delete each one containing the string “MaskSegmentation”</p>
<pre><code class="lang-auto">allSegmentNodes = slicer.util.getNodes('vtkMRMLSegmentationNode*').values()
for ctn in allSegmentNodes:
  teststr = ctn.GetName()
  if 'MaskSegmentation' in teststr:
      slicer.mrmlScene.RemoveNode(ctn)
</code></pre>
<p>please  handle with care <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @jamesobutler (2021-07-20 17:58 UTC)

<p>A segmentation node (vtkMRMLSegmentationNode) object contains a Segmentation (vtkSegmentation) that contains Segments (vtkSegment).</p>
<pre><code class="lang-auto">&gt;&gt;&gt; segmentation_node = slicer.util.getNode("Segmentation")
&gt;&gt;&gt; segmentation_node
(MRMLCore.vtkMRMLSegmentationNode)00000162D42FA1C8
&gt;&gt;&gt; segmentation = segmentation_node.GetSegmentation()
(vtkSegmentationCore.vtkSegmentation)00000162D42FA648
&gt;&gt;&gt; segmentation.GetNumberOfSegments()
1
&gt;&gt;&gt; segmentation.GetNthSegment(0)
(vtkSegmentationCore.vtkSegment)00000162D42FAE88
</code></pre>

---

## Post #7 by @Griffin (2021-07-20 18:51 UTC)

<p>Thank you! I appreciate the examples! I got it now</p>

---
