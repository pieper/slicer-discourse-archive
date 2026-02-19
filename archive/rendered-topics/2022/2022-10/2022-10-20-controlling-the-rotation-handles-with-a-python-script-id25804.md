---
topic_id: 25804
title: "Controlling The Rotation Handles With A Python Script"
date: 2022-10-20
url: https://discourse.slicer.org/t/25804
---

# Controlling the rotation handles with a python script

**Topic ID**: 25804
**Date**: 2022-10-20
**URL**: https://discourse.slicer.org/t/controlling-the-rotation-handles-with-a-python-script/25804

---

## Post #1 by @AMK (2022-10-20 10:56 UTC)

<p>Hi,</p>
<p>Is it possible to programitically control the rotation handles to rotate the plane.</p>
<p>I have created a plane.</p>
<p>B = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLMarkupsPlaneNode”)<br>
B.SetOrigin([0,0,0])<br>
B.SetNormal([0,0,-1])<br>
B.SetAxes([1,0,0],[0,1,0],[0,0,1])</p>
<p>The rotation handles are visible. I was wondering if it is possible to control the rotation angles with a slider with say a ctkslider. I would have used the qmrmlTransformslider, but as I only need to control two angles, I wanted to switch to ctkSlider.</p>
<p>Thanks</p>

---
