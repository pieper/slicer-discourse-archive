---
topic_id: 27160
title: "Vtkmrmlcameranodes Coordinate System"
date: 2023-01-10
url: https://discourse.slicer.org/t/27160
---

# vtkMRMLCameraNode's coordinate system

**Topic ID**: 27160
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/vtkmrmlcameranodes-coordinate-system/27160

---

## Post #1 by @dsa934 (2023-01-10 12:17 UTC)

<p>Operating system: window 11<br>
Slicer version: 4.13.0</p>
<p>Hi, everyone</p>
<p>I want to calculate the z-buffer of an object based on the camera position.<br>
As far as I know, the z buffer is calculated based on the camera coordinate system.</p>
<p>cameraNode = slicer.modules.cameras.logic().GetViewActiveCameraNode()</p>
<p>pos_camera = [0,0,0]</p>
<p>cameraNode.GetPosition(pos_camera)</p>
<p>Given the above situation, I have two questions.</p>
<p>Q1. What’s the camera’s position coordinate system ?</p>
<ul>
<li>Is the coordinate system of ‘pos_camera’  a Camera(View) coordinate system or a RAS (World Coordinate system) coordinate system?</li>
</ul>
<p>Q2. Does the camera default to perspective projection?</p>
<ul>
<li>I made a depth map for the parallel projection method, but if the camera settings are different, I would like to implement it again, so I ask a question.</li>
</ul>

---

## Post #2 by @pieper (2023-01-10 18:30 UTC)

<p>Camera position will be in RAS.  The default camera is perspective, but it can be set to parallel if that works better for you.</p>

---
