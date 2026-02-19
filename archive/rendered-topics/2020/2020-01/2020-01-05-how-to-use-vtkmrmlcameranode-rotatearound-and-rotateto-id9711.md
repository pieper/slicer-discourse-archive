---
topic_id: 9711
title: "How To Use Vtkmrmlcameranode Rotatearound And Rotateto"
date: 2020-01-05
url: https://discourse.slicer.org/t/9711
---

# How to use vtkMRMLCameraNode RotateAround and RotateTo?

**Topic ID**: 9711
**Date**: 2020-01-05
**URL**: https://discourse.slicer.org/t/how-to-use-vtkmrmlcameranode-rotatearound-and-rotateto/9711

---

## Post #1 by @apparrilla (2020-01-05 15:34 UTC)

<p>I´ve been trying to manage camera rotation around a focal point but I can´t find the right parameter to send.</p>
<p>RotateAround needs RASAxis and bool or angle. I have test without succes</p>
<blockquote>
<p>camera = slicer.mrmlScene.GetNodeByID(‘vtkMRMLCameraNode1’)<br>
camera.RotateAround(‘R’,20)</p>
</blockquote>
<p>and</p>
<blockquote>
<p>camera = slicer.mrmlScene.GetNodeByID(‘vtkMRMLCameraNode1’)<br>
camera.RotateAround(0,20)</p>
</blockquote>
<blockquote>
<p>TypeError: ambiguous call, multiple overloaded methods match the arguments</p>
</blockquote>
<p>Same problem as with “RotateTo”</p>
<p>I´ve found enums for parameters but I don´t know how to use them:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6d06e52f86de236c91fa196432b7a17f8616a1a.png" alt="image" data-base62-sha1="zdq1aZA70uvyOeClGhP8ABMZOVc" width="100" height="166"></p>
<p>Thanks on advance!</p>

---

## Post #2 by @lassoan (2020-01-05 18:59 UTC)

<p>Camera always rotates around the camera’s focal point. If you want to rotate around a different point then probably the easiest is to compute the new camera position, focal point, and ViewUp vector and set them in the camera.</p>

---

## Post #3 by @apparrilla (2020-01-05 19:24 UTC)

<p>I’m looking for exactly this camera behavior by I can’t make it work from those methods. I’m sure I’m doing something wrong with syntaxis…</p>

---

## Post #4 by @lassoan (2020-01-05 20:22 UTC)

<p>Which behavior you are referring to? What would you like to achieve?</p>
<p>VTK’s built-in camera rotation methods can only rotate around the focal point, which is the position the camera looks at (in the center of the field of view).</p>

---

## Post #5 by @apparrilla (2020-01-05 20:45 UTC)

<p>I want to look at something (fiducial point for example) from any position and rotate camera 180º in all axes to see it from de opposite side.</p>
<p>Something like:</p>
<blockquote>
<p>def LookAtFiducial(self, currentFid):<br>
position = [0,0,0]<br>
self.fiducial = self.fiducialNode()<br>
self.fiducial.GetNthFiducialPosition(currentFid,position)<br>
camera = slicer.mrmlScene.GetNodeByID(‘vtkMRMLCameraNode1’)<br>
camera.SetFocalPoint(*position)<br>
camera.SetPosition(position[0]+100,position[1]-200,position[2]+50)</p>
</blockquote>
<blockquote>
<p>def RotateOpposite(self)<br>
camera = slicer.mrmlScene.GetNodeByID(‘vtkMRMLCameraNode1’)<br>
camera.RotateAround(‘R’,180)  / camera.RotateTo(position[0]-100,position[1]+200,position[2]-50)</p>
</blockquote>

---

## Post #6 by @lassoan (2020-01-05 22:01 UTC)

<p>To look at a point from the other side, mirror the camera position on the focal point position (cp_new = cp_old + 2 * (fp-cp_old)).</p>

---
