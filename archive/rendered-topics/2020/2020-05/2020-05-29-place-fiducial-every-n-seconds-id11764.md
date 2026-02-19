---
topic_id: 11764
title: "Place Fiducial Every N Seconds"
date: 2020-05-29
url: https://discourse.slicer.org/t/11764
---

# Place fiducial every n seconds

**Topic ID**: 11764
**Date**: 2020-05-29
**URL**: https://discourse.slicer.org/t/place-fiducial-every-n-seconds/11764

---

## Post #1 by @mms25 (2020-05-29 00:15 UTC)

<p>Hi, I am new to programming in 3D slicer. I am trying to place a fiducial at the tip of the pointer tool every five seconds. I have tried using the timer function but it doesn’t seem to work. This is the code I am using:</p>
<p>from threading import Timer</p>
<p>def test():<br>
fidMatrix = vtk.vtkMatrix4x4()<br>
Transform.GetMatrixTransformToWorld(fidMatrix)</p>
<p>slicer.modules.markups.logic().AddFiducial(fidMatrix.GetElement(0,3),fidMatrix.GetElement(1,3),fidMatrix.GetElement(2,3))<br>
Timer(5,test).start()</p>
<p>test</p>

---

## Post #2 by @lassoan (2020-05-29 00:54 UTC)

<p>QTimer works well, see for example <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/Endoscopy/Endoscopy.py#L58">Endoscopy module</a>.</p>
<p>However, before implementing anything, consider these existing point recording options:</p>
<p>You can use “Collect Points” module in SlicerIGT extension. It supports sampling based on minimum distance, can record points in arbitrary coordinate system, control labeling (base name and counter), etc. It does not sample by elapsed time, but if you are sure you want to sample by time then we might consider adding it.</p>
<p>You can also record points into sequence nodes by going to Sequences module, click the green ‘+’ button to create a new sequence, choose the transform node as “Proxy node” in the table, then hit the red “Record” button. After recording, you can also replay, and access recorded point positions as a sequence node. By default maximum recording rate is limited to the current playback rate, so to achieve sampling at every 5s, set playback rate to 0.2fps.</p>

---

## Post #3 by @mms25 (2020-06-08 21:13 UTC)

<p>Thanks thats great!<br>
I used the Qtimer and it is working perfectly.</p>

---
