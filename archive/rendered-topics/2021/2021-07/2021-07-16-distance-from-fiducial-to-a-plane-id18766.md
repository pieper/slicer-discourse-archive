# Distance from fiducial to a plane

**Topic ID**: 18766
**Date**: 2021-07-16
**URL**: https://discourse.slicer.org/t/distance-from-fiducial-to-a-plane/18766

---

## Post #1 by @YingHsu (2021-07-16 12:28 UTC)

<ol>
<li>I have a CBCT data, and I want to measure distance from a given fiducial to a plane. I tried extension of “Angle Planes”, but I could not add scene before continuing to manage planes.</li>
<li>Is there any extension for measuring the distance between a given fiducial to a  plane?</li>
</ol>
<p>Thank you in advance.</p>

---

## Post #2 by @lassoan (2021-07-16 22:32 UTC)

<p>You can write a script easily that gets distances of points <code>F</code> from a plane <code>P</code> (by transforming the points to the plane’s coordinate system and get the third coordinate value):</p>
<pre><code class="lang-python">planeNode = getNode('P')
fiducialNode = getNode('F')

planeToWorld = vtk.vtkMatrix4x4()
planeNode.GetObjectToWorldMatrix(planeToWorld)
points_World = arrayFromMarkupsControlPoints(fiducialNode)
points_Plane = np.dot(np.linalg.inv(arrayFromVTKMatrix(planeToWorld)), np.append(points_World, np.ones([4,1]), axis=1).T)
distances = points_Plane[2]
print(distances)
</code></pre>

---

## Post #3 by @Daniel1 (2023-02-01 11:10 UTC)

<p>Hello Prof Lasso, I am interested in finding perpendicular distance from point F to plane P as well and unfortunately that bit of code did not work. Dan</p>

---

## Post #4 by @Daniel1 (2023-02-03 21:59 UTC)

<p>I am using Slicer 5.2.1</p>
<p>After entering the code:<br>
import numpy as np<br>
planeNode = getNode(‘P’)<br>
fiducialNode = getNode(‘F’)<br>
planeToWorld = vtk.vtkMatrix4x4()<br>
planeNode.GetObjectToWorldMatrix(planeToWorld)<br>
points_World = arrayFromMarkupsControlPoints(fiducialNode)<br>
points_Plane = np.dot(np.linalg.inv(arrayFromVTKMatrix(planeToWorld)), np.append(points_World, np.ones([4,1]), axis=1).T)<br>
distances = points_Plane[2]<br>
print(distances)</p>
<p>I get the following error:<br>
File “”, line 7, in <br>
File “&lt;<strong>array_function</strong> internals&gt;”, line 180, in append<br>
File “/Applications/Slicer.app/Contents/lib/Python/lib/python3.9/site-packages/numpy/lib/function_base.py”, line 5444, in append<br>
return concatenate((arr, values), axis=axis)<br>
File “&lt;<strong>array_function</strong> internals&gt;”, line 180, in concatenate<br>
ValueError: all the input array dimensions for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 1 and the array at index 1 has size 4</p>
<p>How can this be fixed?</p>

---
