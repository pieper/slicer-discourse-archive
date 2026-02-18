# How to switch transform from global to local

**Topic ID**: 5539
**Date**: 2019-01-28
**URL**: https://discourse.slicer.org/t/how-to-switch-transform-from-global-to-local/5539

---

## Post #1 by @timeanddoctor (2019-01-28 13:39 UTC)

<p>How to switch transform from global to local with python script. Are there any example codes?<br>
By the way, where can I found the setting of the transform attribute in python code?</p>

---

## Post #2 by @timeanddoctor (2019-01-29 14:25 UTC)

<p>I can create a transform and set translation on local manually. But are there any code could change translation from global to Local with python code?<br>
I checked github code found: <code>setCoordinateReference(LOCAL)</code>, while a error happen as follows:<br>
‘vTransformr.setCoordinateReference(LOCAL)<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
AttributeError: ‘vtkCommonTransformsPython.vtkTransform’ object has no attribute 'setCoordinateReference’</p>

---

## Post #3 by @lassoan (2019-01-30 01:21 UTC)

<p>Local/global means if translation is performed before or after the rotation. You can achieve this by decomposing transformation into a translation and rotation part and changing up their order.</p>

---
