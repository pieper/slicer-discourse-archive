---
topic_id: 2094
title: "Qlabel That Prints The Current Number Of Markups That Have B"
date: 2018-02-15
url: https://discourse.slicer.org/t/2094
---

# QLabel that prints the current number of markups that have been placed

**Topic ID**: 2094
**Date**: 2018-02-15
**URL**: https://discourse.slicer.org/t/qlabel-that-prints-the-current-number-of-markups-that-have-been-placed/2094

---

## Post #1 by @lgroves (2018-02-15 22:20 UTC)

<p>I am trying to have a QLabel widget that prints the number of fiducials that have been placed.<br>
I have a function called onMarkupAdded that was previously created to execute some other code when a mark up is placed. I have added to that a self.numFid = self.fiducialNode.GetNumberOfMarkupsAdded() which prints the correct number if you print the variable. I am unsure how to return this value back to setup each time a new fiducial is added.</p>
<p>Any help is appreciate.</p>
<p>Thanks!</p>

---

## Post #2 by @cpinter (2018-02-16 21:26 UTC)

<p>If I understand your question correctly (I’m struggling to understand the “return this value back to setup” part), then you need to observe the MarkupAddedEvent event of self.fiducialNode.</p>
<pre><code>self.addObserver(self.fiducialNode, slicer.vtkMRMLMarkupsNode.MarkupAddedEvent, self.onMarkupAdded)
</code></pre>
<p>Then in onMarkupAdded you can get the number of markups the way you describe and set it as text to the QLabel.</p>
<p>I hope this helps!</p>

---

## Post #3 by @cpinter (2018-02-16 21:29 UTC)

<p>I didn’t mention but there are a few things to know, such as inheriting VTKObservationMixin in your class that has the onMarkupAdded function, and the argument list of that function (self,caller,event). See examples:</p>
<ul>
<li>
<a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py</a> (here the inheritance happens on the module widget level)</li>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMWidgets.py">https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOMLib/DICOMWidgets.py</a></li>
</ul>

---
