---
topic_id: 1143
title: "Segment Statistics Does Nothing"
date: 2017-09-29
url: https://discourse.slicer.org/t/1143
---

# Segment Statistics does nothing?

**Topic ID**: 1143
**Date**: 2017-09-29
**URL**: https://discourse.slicer.org/t/segment-statistics-does-nothing/1143

---

## Post #1 by @hherhold (2017-09-29 20:49 UTC)

<p>This is on the 9/28 MacOS nightly. Segment Statistics doesn’t do any calculations - just brings up quantitative window with no output. Anybody else see this or is it just me?</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @hherhold (2017-09-29 20:52 UTC)

<p>Make that 9/27 nightly, and also fails on 9/8 nightly.</p>
<p>Error traceback:</p>
<p>Traceback (most recent call last):<br>
File “/Users/hherhold/Desktop/Slicer.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SegmentStatistics.py”, line 183, in onApply<br>
self.logic.computeStatistics()<br>
File “/Users/hherhold/Desktop/Slicer.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SegmentStatistics.py”, line 420, in computeStatistics<br>
self.updateStatisticsForSegment(segmentID)<br>
File “/Users/hherhold/Desktop/Slicer.app/Contents/lib/Slicer-4.7/qt-scripted-modules/SegmentStatistics.py”, line 429, in updateStatisticsForSegment<br>
if not segmentationNode.GetSegmentation().GetSegment(segmentID):<br>
AttributeError: ‘vtkCommonCorePython.vtkObject’ object has no attribute ‘GetSegment’</p>

---

## Post #3 by @lassoan (2017-09-29 22:17 UTC)

<p>Thank you for reporting this. I could reproduce this error and fixed it.</p>
<p>The problem was that in certain scenarios it was possible to get to method in SegmentStatistics module that used vtkSegmentationCore before it was imported. We haven’t detected this issue either in our automatic tests or when manually used the feature because when you run Segment Editor then it imports the library and the error does not occur.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> - it is yet another example why fixing <a href="https://issues.slicer.org/view.php?id=4385">https://issues.slicer.org/view.php?id=4385</a> would be important. It would be great if you could have a look at it</p>

---

## Post #4 by @hherhold (2017-09-29 23:51 UTC)

<p>Got it. Thanks!!!</p>
<p>-Hollister</p>

---
