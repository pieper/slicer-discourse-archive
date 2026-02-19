---
topic_id: 11944
title: "Is The Rotation Of The 3D Slicers Transform Module Euler Or"
date: 2020-06-09
url: https://discourse.slicer.org/t/11944
---

# Is the rotation of the 3D Slicer's Transform module Euler or Quaternion?

**Topic ID**: 11944
**Date**: 2020-06-09
**URL**: https://discourse.slicer.org/t/is-the-rotation-of-the-3d-slicers-transform-module-euler-or-quaternion/11944

---

## Post #1 by @kscript (2020-06-09 05:51 UTC)

<p>Hello everybody.<br>
I am in the process of matching using the 3D Slicer and the program I configured.<br>
In my program, I use quaternion for rotation.<br>
3D Slicer also converted to Euler angle to rotate as much as the corresponding value, but it was not matched.<br>
When I looked at other issues on the Forum, I confirmed that 3D Slicer uses quaternions.</p>
<ol>
<li>Can I enter the values of LR = x, PA=y, and IS=z among quaternion variables (w,x,y,z) into Rotation?</li>
<li>Where can I enter the value of quaternian variable w?</li>
</ol>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-06-09 06:35 UTC)

<p>Transforms module only uses 4x4 homogeneous transformation matrix for linear transforms. You can convert between these representations easily, for example by using <code>vtk.vtkMath.QuaternionToMatrix3x3()</code> and <code>vtk.vtkMath.Matrix3x3ToQuaternion()</code> methods.</p>
<p>Rotation angles in the Transforms module GUI simply allow incremental rotation along LR, AP, IS axes. The values displayed next to the sliders only show angle of the last rotation, therefore the displayed values do not represent the total rotation. See some more explanation at the end of <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms#Transform_editing_and_application">this section</a> in Transforms module documentation.</p>

---
