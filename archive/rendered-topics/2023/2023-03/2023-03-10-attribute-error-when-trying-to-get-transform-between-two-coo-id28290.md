# Attribute error when trying to get transform between two coords

**Topic ID**: 28290
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/attribute-error-when-trying-to-get-transform-between-two-coords/28290

---

## Post #1 by @yshi (2023-03-10 20:19 UTC)

<p>Hello Slicer Community,</p>
<p>I created a simple plane P with 3 points and am hoping to get the transform between its coordinate system and the system default coord.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc227e4913da0b7be74f4bbf5f3ce5e9f3b51630.png" alt="planeP" data-base62-sha1="qQjFi7uaPAUHUS4Pwrz0w6IOHkY" width="427" height="405"></p>
<p>I tried this script:</p>
<blockquote>
<p>planeToWorld = vtk.vtkMatrix4x4()<br>
getNode(‘P’).GetObjectToWorldMatrix(planeToWorld)<br>
print(planeToWorld)</p>
</blockquote>
<p>and got the error message saying “AttributeError: ‘vtkSlicerMarkupsModuleMRMLPython.vtkMRMLMarkupsPla’ object has no attribute ‘GetObjectToWorldMatrix’”. Any advice would be greatly appreciated!</p>
<p>Operating system: Windows 11<br>
Slicer version: 4.11</p>
<p>Thanks,<br>
Yuan</p>

---

## Post #2 by @lassoan (2023-03-11 06:58 UTC)

<p>Your Slicer version is several years old. It does not have the method you are looking for.</p>

---

## Post #3 by @yshi (2023-03-16 00:24 UTC)

<p>Thank you! I updated to v5.2.2 and the issue is solved.</p>

---
