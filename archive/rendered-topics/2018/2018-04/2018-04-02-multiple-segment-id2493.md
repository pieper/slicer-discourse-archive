# Multiple segment

**Topic ID**: 2493
**Date**: 2018-04-02
**URL**: https://discourse.slicer.org/t/multiple-segment/2493

---

## Post #1 by @anandmulay3 (2018-04-02 14:53 UTC)

<p>i’m adding 2nd segment under same masterNode, But whenever i try to apply effects on it’s getting applied on 1st segment only,<br>
How to select 2nd segment as active segment???</p>

---

## Post #2 by @cpinter (2018-04-02 16:05 UTC)

<p>You need to select the second segment in the segment list. It’s always the highlighted one that is edited by the selected effect.</p>

---

## Post #3 by @lassoan (2018-04-02 17:23 UTC)

<p>Programmetically you can select a segment using <a href="http://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a1537f275ab7571d8b330dfb5afdfe5ed">setCurrentSegmentID</a> method of the segment editor widget.</p>

---

## Post #4 by @anandmulay3 (2018-04-03 13:21 UTC)

<p>addsegID = segmentationNode.GetSegmentation().AddEmptySegment(“bone”)<br>
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentEditorNode”)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)<br>
segmentEditorWidget.setCurrentSegmentID(‘addsegID’)<br>
segmentEditorWidget.setActiveEffectByName(“Threshold”)<br>
Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Slicer-4.9\qt-scripted-modules\SegmentEditorEffects\SegmentEditorEffects\SegmentEditorThresholdEffect.py”, line 54, in activate<br>
self.segment2DFillOpacity = displayNode.GetSegmentOpacity2DFill(segmentID)<br>
TypeError: GetSegmentOpacity2DFill argument 1: string is required</p>
<p>i’m getting this error when i try to switch on 2nd segment to apply effect</p>

---

## Post #5 by @cpinter (2018-04-03 15:17 UTC)

<p>Based on the code snippet you posted there is no variable named <code>segmentID</code>, so getting the error is expected. You have one variable storing a segment ID called <code>addsegID</code>. Maybe you wanted to use that?</p>

---

## Post #6 by @lassoan (2018-04-03 22:23 UTC)

<aside class="quote no-group" data-username="anandmulay3" data-post="4" data-topic="2493">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/ac8455/48.png" class="avatar"> anandmulay3:</div>
<blockquote>
<p>segmentEditorWidget.setCurrentSegmentID(‘addsegID’)</p>
</blockquote>
</aside>
<p>Another issue is that here you probably wanted to set the string that is stored in addSegID variable, so the quotes around addSegID must be removed.</p>

---

## Post #7 by @anandmulay3 (2018-04-04 07:42 UTC)

<p>ohh yes that was the fault, thanks</p>

---
