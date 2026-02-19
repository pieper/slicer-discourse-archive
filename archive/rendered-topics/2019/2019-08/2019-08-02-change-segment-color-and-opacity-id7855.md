---
topic_id: 7855
title: "Change Segment Color And Opacity"
date: 2019-08-02
url: https://discourse.slicer.org/t/7855
---

# Change segment color and opacity

**Topic ID**: 7855
**Date**: 2019-08-02
**URL**: https://discourse.slicer.org/t/change-segment-color-and-opacity/7855

---

## Post #1 by @jazlynn21100 (2019-08-02 18:06 UTC)

<p>Ok 2 ,more questions and I promise I’m done</p>
<p>If you want to set a segmentation’s color, my assumption is that it would be an addition to this line:</p>
<p>addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(“brain”)</p>
<p>to the AddEmptySegment portion; so you have <span class="hashtag">#faf9e3</span> as the color HTML, what would the line change to to add color?</p>
<p>2nd question:<br>
If you wanted to change the opacity of the segmentations, that’s in the Segmentations module, so would you have to load that model in order to change the opacity?</p>

---

## Post #2 by @lassoan (2019-08-02 21:33 UTC)

<p>You can adjust most display properties by modifying the segmentation’s <a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html" rel="nofollow noopener">display node</a>. The only exception is the segment color, which can be overridden in the display node but recommended to be set in the segmentation node instead.</p>
<pre><code class="lang-python">segmentationNode=slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
segmentationDisplayNode=segmentationNode.GetDisplayNode()
segmentation=segmentationNode.GetSegmentation()

# Change overall segmentation display properties
segmentationDisplayNode.SetOpacity3D(0.5)

# Change one segment display properties
segmentId = segmentation.GetSegmentIdBySegmentName("Segment_1")
segmentationDisplayNode.SetSegmentOpacity2DOutline(segmentId, 0.0)
segmentation.GetSegment(segmentId).SetColor(1,0,0)  # color should be set in segmentation node
</code></pre>

---

## Post #3 by @CB1 (2020-09-23 14:00 UTC)

<p>I’m trying to change the opacity of everything but a small range of intensities on my model. Can I do that with this method? I’m completely new to slicer.</p>

---

## Post #4 by @cpinter (2020-09-23 14:04 UTC)

<p>Please create a new topic and in that give us more information. Describe exactly what you’d like to achieve, what kind of data you have, what tools you want to use, etc. Thanks!</p>

---
