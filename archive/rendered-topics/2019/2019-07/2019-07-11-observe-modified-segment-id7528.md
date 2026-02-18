# Observe modified segment

**Topic ID**: 7528
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/observe-modified-segment/7528

---

## Post #1 by @EricM (2019-07-11 12:15 UTC)

<p>Hello community,<br>
I am trying to add an observer to a segmentation node to keep track of any modifications to any segment (by modifications I mean manual changes to the contouring). The idea is to have a marker of any modifications so if the user changes subject (for which I have a QComboBox in my module), I can prompt the user to save before changing patients. This is to avoid any accidental subject changes and losing unsaved work.</p>
<p>I have been trying many different things. Something close is this:</p>
<p><code>segmentationNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode') segmentationNode.AddObserver(segmentationNode.GetSegmentation().SegmentModified,onSegmentModified)</code></p>
<p>But this only activates onSegmentModified() when I add, remove, rename, change color of, etc… a Segment. What is the signal produced when the actual contouring changes? Is this something that can be done?<br>
Thanks,<br>
Eric</p>

---

## Post #2 by @lassoan (2019-07-26 03:16 UTC)

<p><code>SegmentModified</code> event is invoked if segment metadata is modified. You need to observe <code>MasterRepresentationModified</code> or <code>RepresentationModified</code> to get notified about segmentation content changes. See list of events <a href="https://apidocs.slicer.org/master/classvtkSegmentation.html#a1a387d4572ce52ab0c0babbecbd5a4daa82679724b676d81cd4393b6a4a388db9" rel="nofollow noopener">here</a>.</p>

---

## Post #3 by @EricM (2019-08-05 12:51 UTC)

<p>Thank you!<br>
This perfectly answers my question. And thank for the list of events!</p>
<p>Eric</p>

---
