# View multiple label maps in one scene

**Topic ID**: 574
**Date**: 2017-06-26
**URL**: https://discourse.slicer.org/t/view-multiple-label-maps-in-one-scene/574

---

## Post #1 by @jks1995 (2017-06-26 19:16 UTC)

<p>Is it possible to maintain more than one label map volume node in a scene and if so adjust the colors to keep track of what is what? My goal is to be able to describe the shape of a label map and then describe the shape of another object and have both in the scene at the same time.</p>
<p>More specifically, I think my issue is that when a label map is created and added to the scene, I cannot view it in along side the background volume that i would like to use unless I put it into the label map slot in the slice drop down menu, which I would like to avoid.</p>
<p>e: more information on the issue</p>

---

## Post #2 by @lassoan (2017-06-26 22:08 UTC)

<p>If you want to show only one labelmap at a time (you can have multiple colors in one labelmap) and only want to show it in 2D view then labelmap should work.</p>
<p>If you want to display more then use Segmentations instead of labelmaps: you can show any number of segmentations, labels can overlap, you can display segments as contour+fill at the same time, and you can show segments in 3D as well.</p>
<p>If you have a labelmap then you can create a Segmentation node in the Segmentations module’s Import/export section.</p>

---

## Post #3 by @jks1995 (2017-06-27 13:53 UTC)

<p>Whats the best way to remove a segment from the scene? I tried<br>
<code><br>
slicer.mrmlScene.RemoveNode(segment)<br>
</code><br>
But that doesn’t seem to work. Thank you for your response!</p>
<p>e:<br>
I am able to eliminate the segments as I would like, but when I do it through the code, I get an error saying:<br>
<code><br>
vtkSlicerSegmentationsModuleLogic::GetSegmentForSegmentSubjectHierarchyItem: Segmentation does not contain segment with given ID: Segment_name<br>
</code></p>
<p>I am deleting with the following code:<br>
<code><br>
segmentation = segmentationNode.GetSegmentation()<br>
segmentation.RemoveSegment(segmentation.GetNthSegment(0))<br>
</code></p>

---

## Post #4 by @lassoan (2017-06-27 17:47 UTC)

<p>Deleting a segment:</p>
<pre><code>segmentation = segmentationNode.GetSegmentation()
segmentation.RemoveSegment(segmentation.GetNthSegment(0))
</code></pre>
<p>Deleting a segmentation node:</p>
<pre><code>slicer.mrmlScene.RemoveNode(segmentationNode)</code></pre>

---
