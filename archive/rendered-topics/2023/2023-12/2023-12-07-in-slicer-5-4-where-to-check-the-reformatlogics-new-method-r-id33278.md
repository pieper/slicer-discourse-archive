# In Slicer 5.4, where to check the reformatLogic's new method RotateSlice()'s parameters?

**Topic ID**: 33278
**Date**: 2023-12-07
**URL**: https://discourse.slicer.org/t/in-slicer-5-4-where-to-check-the-reformatlogics-new-method-rotateslice-s-parameters/33278

---

## Post #1 by @derekcbr (2023-12-07 05:50 UTC)

<p>reformatLogic = slicer.modules.reformat.logic()<br>
Is there a way to find out the function parameters of RotateSlice()?</p>

---

## Post #2 by @pieper (2023-12-07 12:33 UTC)

<pre><code class="lang-auto">
&gt;&gt;&gt; help(reformatLogic.RotateSlice)
Help on built-in function RotateSlice:

RotateSlice(...) method of vtkSlicerReformatModuleLogicPython.vtkSlicerReformatLogic instance
    RotateSlice(node:vtkMRMLSliceNode, axisIndex:int,
        rotationAngleDeg:float) -&gt; None
    C++: static void RotateSlice(vtkMRMLSliceNode *node,
        int axisIndex, double rotationAngleDeg)
    
    Rotate slice along an axis (0 = horizontal, 1 = vertical, 2 =
    slice normal) Flip: axisIndex = 0 (vertical) or 1 (horizontal),
    rotationAngleDeg = 180. In-plane rotation: axisIndex = 2,
    rotationAngleDeg &gt; 0 for clockwise.
</code></pre>

---

## Post #3 by @derekcbr (2023-12-08 10:57 UTC)

<p>Thanks for the help. If I have calcualte the rotation from a matrix, how to calcualte the rotation?<br>
matrix_4x4 = np.array([<br>
[0.707, 0.0, 0.707, 0.2],<br>
[0.707, 0,-0.707, 0.3],<br>
[0, 1, 0.0, 0.4],<br>
[0, 0, 0, 1]<br>
])<br>
sy = math.sqrt(R[0,0] * R[0,0] +  R[1,0] * R[1,0])<br>
singular = sy &lt; 1e-6<br>
if  not singular :<br>
x = math.atan2(R[2,1] , R[2,2])<br>
y = math.atan2(-R[2,0], sy)<br>
z = math.atan2(R[1,0], R[0,0])<br>
else :<br>
x = math.atan2(-R[1,2], R[1,1])<br>
y = math.atan2(-R[2,0], sy)<br>
z = 0<br>
But it seems that it is not working. Does Slicer have a quaternion method to calcuatle the rotation? Thanks!</p>

---
