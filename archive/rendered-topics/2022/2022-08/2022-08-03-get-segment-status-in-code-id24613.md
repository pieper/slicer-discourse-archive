---
topic_id: 24613
title: "Get Segment Status In Code"
date: 2022-08-03
url: https://discourse.slicer.org/t/24613
---

# Get segment status in code

**Topic ID**: 24613
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/get-segment-status-in-code/24613

---

## Post #1 by @Karthik (2022-08-03 06:31 UTC)

<p>I have multiple segments in Segment Editor. I set the segment status flag to ‘Flagged’ if I think there is some problem with the output displayed on screen. I would then like to apply  the effect based on if the segment status has been flagged or not.<br>
How can I know the status of a segment through python code. “vtkSegment” class doesn’t seem to have any GetStatus method</p>

---

## Post #2 by @Sunderlandkyl (2022-08-03 14:46 UTC)

<p>The code to get the segment status is in vtkSlicerSegmentationsModuleLogic:</p>
<pre><code class="lang-python">segment = getNode("Segmentation").GetSegmentation().GetNthSegment(0)
logic = slicer.modules.segmentations.logic()
logic.GetSegmentStatus(segment)

# Status enum:
# slicer.vtkSlicerSegmentationsModuleLogic.NotStarted
# slicer.vtkSlicerSegmentationsModuleLogic.InProgress
# slicer.vtkSlicerSegmentationsModuleLogic.Completed
# slicer.vtkSlicerSegmentationsModuleLogic.Flagged
</code></pre>

---

## Post #3 by @Karthik (2022-08-04 03:16 UTC)

<p>Hi Kyle Sunderland,<br>
Thanks for the help.<br>
Slicer has by default segment status of four types.<br>
0 - Not Started<br>
1 - In Progress<br>
2 - Completed<br>
3 - Flagged<br>
I was wondering if its possible for me to add my own segment status flags through code changes which could then be selected through the UI. If changes to the segment status were to be made, would they be done at python effect level (or) C++ level?</p>

---

## Post #4 by @Sunderlandkyl (2022-08-04 14:54 UTC)

<p>The changes would have to be made in C++.</p>
<p>What additional status flags were you planning to add?</p>

---

## Post #5 by @lassoan (2022-08-04 15:50 UTC)

<p><a class="mention" href="/u/karthik">@karthik</a> You can use the “flagged” state for any purpose. You can also store any custom metadata in each segment as tag:value pairs (by using <code>vtkSegment.SetTag()</code>, <code>vtkSegment.GetTag()</code>, etc.).</p>

---
