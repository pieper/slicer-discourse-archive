---
topic_id: 24803
title: "Segmentstatistics Error"
date: 2022-08-17
url: https://discourse.slicer.org/t/24803
---

# SegmentStatistics error

**Topic ID**: 24803
**Date**: 2022-08-17
**URL**: https://discourse.slicer.org/t/segmentstatistics-error/24803

---

## Post #1 by @Jorge_Wagner_Esteves (2022-08-17 10:27 UTC)

<p>Hi there,</p>
<p>I am starting with 3D Slicer, using version 5.0.2. I did a segmentation on CT images and tried to process it using SegmentStatistics to get organ volumes.</p>
<p>I am running 3D Slicer on an AMD Ryzen 7 3700X with 32 GB RAM and an RTX 2700 Super GPU under Windows 11.</p>
<p>I got the following error. Does someone get the same error: Any clue about what’s happening?</p>
<p>Traceback (most recent call last):<br>
File “C:\Users\1090\AppData\Local\NA-MIC\Slicer 5.0.2\bin\Python\slicer\util.py”, line 2830, in tryWithErrorDisplay<br>
yield<br>
File “C:\Users\1090\AppData\Local\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\SegmentStatistics.py”, line 206, in onApply<br>
self.logic.computeStatistics()<br>
File “C:\Users\1090\AppData\Local\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\SegmentStatistics.py”, line 455, in computeStatistics<br>
self.updateStatisticsForSegment(segmentID)<br>
File “C:\Users\1090\AppData\Local\NA-MIC\Slicer 5.0.2\lib\Slicer-5.0\qt-scripted-modules\SegmentStatistics.py”, line 484, in updateStatisticsForSegment<br>
stats = plugin.computeStatistics(segmentID)<br>
File “C:\Users\1090\AppData\Local\NA-MIC\Slicer 5.0.2\NA-MIC\Extensions-30822\PET-IndiC\lib\Slicer-5.0\qt-scripted-modules\PETVolumeSegmentStatisticsPlugin\PETVolumeSegmentStatisticsPlugin.py”, line 79, in computeStatistics<br>
resultMap[feature]=float(newResult)<br>
ValueError: could not convert string to float: ‘’</p>

---

## Post #2 by @lassoan (2022-08-17 11:09 UTC)

<p>Most probably the PET-IndiC extension has not been updated to be fully compatible with Slicer-5, or you might use it in some unexpected way or type of input data.</p>
<p>Did you use the GUI of a module or you used the module logic via Python scripting?<br>
Which module did you use?<br>
What is your overall goal?</p>

---

## Post #3 by @Jorge_Wagner_Esteves (2022-08-17 11:27 UTC)

<p>You are right!!!<br>
I just removed the PET-IndiC extension that appeared as legacy, and the problem vanished!</p>
<p>Tanks</p>

---
