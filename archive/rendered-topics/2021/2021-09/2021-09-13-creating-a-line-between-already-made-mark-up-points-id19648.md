---
topic_id: 19648
title: "Creating A Line Between Already Made Mark Up Points"
date: 2021-09-13
url: https://discourse.slicer.org/t/19648
---

# Creating a line between already made mark up points

**Topic ID**: 19648
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/creating-a-line-between-already-made-mark-up-points/19648

---

## Post #1 by @mohammed_alshakhas (2021-09-13 19:01 UTC)

<p>I’m trying to draw lines exactly where I placed some markup points</p>
<p>is there a  way to define a line or plane according to already placed mark-up points?</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2021-09-13 19:08 UTC)

<p>You can copy-paste markup control points from a markups fiducial list to a markups line in Markups module. Select the markups fiducial list, in Control points section select the two control points, hit Ctrl-C to copy them to the clipboard, select the markups line, and hit Ctrl-V to past the control points into the line).</p>

---

## Post #3 by @ImreBarabas (2023-10-26 23:00 UTC)

<p>Dear Andras!</p>
<p>Is it possible to make automatic? I mean I have two markup points and get a line between these two points, without Ctrl-C and Ctrl-V?</p>
<p>Thanks a lot,<br>
Imre</p>

---

## Post #4 by @muratmaga (2023-10-27 02:30 UTC)

<p>Thats like three clicks; one to create the empty line markups object, one to copy and one to paste.</p>
<p>Is it too complicated? You can probably do it by scripting it.</p>

---

## Post #5 by @mikebind (2023-10-27 06:37 UTC)

<p>Yes, this is easily scriptable.  Here is an example function you could paste in the python interactor</p>
<pre><code class="lang-auto">def connectPoints(markupsNode1, markupsNode2):
    '''Simple function which connects the first control
    point of markupsNode1 to the first control point of 
    markupsNode2 with a line'''
    pt1 = markupsNode1.GetNthControlPointPositionWorld(0)
    pt2 = markupsNode2.GetNthControlPointPositionWorld(0)
    newCurveNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsCurveNode')
    newCurveNode.AddControlPoint(*pt1)
    newCurveNode.AddControlPoint(*pt2)
    return newCurveNode
</code></pre>
<p>Then you could use it like this:</p>
<pre><code class="lang-auto">connectingLineNode = connectPoints(getNode('myFirstPoint'), getNode('mySecondPoint'))
</code></pre>
<p>where you would need to replace ‘myFirstPoint’ and ‘mySecondPoint’ with the names of the markups which contain the two points you want to connect.</p>

---

## Post #6 by @ImreBarabas (2023-10-27 06:56 UTC)

<p>Dear Mike Bindschadler!</p>
<p>Thank you so much it works!</p>
<p>With best regards,<br>
Imre</p>

---
