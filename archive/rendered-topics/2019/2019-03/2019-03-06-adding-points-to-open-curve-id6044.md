---
topic_id: 6044
title: "Adding Points To Open Curve"
date: 2019-03-06
url: https://discourse.slicer.org/t/6044
---

# Adding points to open curve

**Topic ID**: 6044
**Date**: 2019-03-06
**URL**: https://discourse.slicer.org/t/adding-points-to-open-curve/6044

---

## Post #1 by @muratmaga (2019-03-06 16:46 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>. I just tried the new markup features, and looks great. Thank you very much for all the hardwork. Quick question, is it possible to modify the curve after it is created, i.,e to add points between already existing ones to   adjust the curvature more closely to the outline I am tracing?</p>

---

## Post #2 by @jamesobutler (2019-03-06 17:32 UTC)

<p>I believe the correct key action is Ctrl-left click to add an additional point to the curve.</p>

---

## Post #3 by @Davide_Punzo (2019-03-06 19:00 UTC)

<p>yes! <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/VTKWidgets/vtkSlicerCurveWidget.cxx#L51" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Markups/VTKWidgets/vtkSlicerCurveWidget.cxx#L51</a></p>

---

## Post #4 by @muratmaga (2019-03-06 22:05 UTC)

<p>Thank you that worked well. Couple more comments/issues: Fiducial projection doesn’t seem to do anything. I have these error messages in the log file, whether they are related or not: Last message repeated a bunch of times for each fiducial created.</p>
<blockquote>
<p>class QColor __cdecl qSlicerSubjectHierarchyMarkupsPlugin::getDisplayColor(__int64,class QMap&lt;int,class QVariant&gt; &amp;) const : No display node<br>
vtkMRMLMarkupsNode::GetNthControlPointSelected failed: control point 1 does not exist</p>
</blockquote>

---

## Post #5 by @Davide_Punzo (2019-03-06 22:22 UTC)

<p>thanks for reporting. Fiducial projection is still not implemented.</p>
<p>For reference here there are all the known reaming bugs and missing features:<br>
<a href="https://1drv.ms/x/s!Arm_AFxB9yqHtvxAsyBDU_3C1IxfGA" class="onebox" target="_blank" rel="nofollow noopener">https://1drv.ms/x/s!Arm_AFxB9yqHtvxAsyBDU_3C1IxfGA</a></p>

---
