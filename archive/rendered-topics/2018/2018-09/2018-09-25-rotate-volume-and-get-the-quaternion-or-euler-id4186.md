---
topic_id: 4186
title: "Rotate Volume And Get The Quaternion Or Euler"
date: 2018-09-25
url: https://discourse.slicer.org/t/4186
---

# Rotate volume and get the Quaternion (or Euler)

**Topic ID**: 4186
**Date**: 2018-09-25
**URL**: https://discourse.slicer.org/t/rotate-volume-and-get-the-quaternion-or-euler/4186

---

## Post #1 by @Niels (2018-09-25 14:12 UTC)

<p>Hello all,</p>
<p>In the transform hierarchy of my scene I added a LinearTransfromNode to rotate my volume to its correct pose. In my Python script I would like to get the value of the rotation in quaternion format. I need the value to save it to file and use it in another program.</p>
<p>I added the following code in python to get the matrix:</p>
<p>transformNodeID = inputVolume.GetTransformNodeID()<br>
if transformNodeID :<br>
transformNode = slicer.mrmlScene.GetNodeByID(transformNodeID )<br>
matrix = transformNode .GetMatrixTransformToParent()</p>
<p>Now I have the vtkMatrix4x4, but I can not find any feature to convert it to a rotation I can use. I prefer quaternions.</p>

---

## Post #2 by @lassoan (2018-09-25 17:33 UTC)

<p>You can convert using <a href="https://www.vtk.org/doc/nightly/html/classvtkQuaternion.html">vtkQuaternion</a>.</p>

---

## Post #3 by @Niels (2018-09-26 09:39 UTC)

<p>Thanks Andras, I will get the rotation part of the 4x4 and place them in a 3x3 and to see if I can get the quaternion from it.</p>

---

## Post #4 by @Niels (2018-09-27 10:08 UTC)

<p>For those interested, this is what I now use to get the quaternion from the volume transformNode.</p>
<pre><code>if inputVolume.GetTransformNodeID():
  transformNode = slicer.mrmlScene.GetNodeByID(inputVolume.GetTransformNodeID())      
  transfromMatrix = vtk.vtkMatrix4x4()
  transformNode.GetMatrixTransformToWorld(transfromMatrix)
  
  rotationMatrix = [[1,0,0],[0,1,0],[0,0,1]]
  for i in range(3):
    for j in range(3):
      rotationMatrix[i][j] = transfromMatrix.GetElement(i,j)
  
  rotationQuat = list(imageRotation)
  vtk.vtkMath.Matrix3x3ToQuaternion(rotationMatrix, rotationQuat);
  
  imageRotation = tuple( rotationQuat )</code></pre>

---
