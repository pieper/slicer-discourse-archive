# Python automation of 'constrain to model' for markups curve

**Topic ID**: 31768
**Date**: 2023-09-18
**URL**: https://discourse.slicer.org/t/python-automation-of-constrain-to-model-for-markups-curve/31768

---

## Post #1 by @Jeff_Zeyl (2023-09-18 05:42 UTC)

<p>I would like to automate the ‘constrain to model’ setting for a markup curve node using python. I have found the c++ function ConstrainPointsToSurface() in the markup curves documentation, with the following parameters:</p>
<p>originalPoints	The points to constrain. (vtkpoints)<br>
normalVectors	The normals for the originalPoints. (vtkpoints)<br>
surfacePolydata	The surface to constrain to. (vtkpolydata)<br>
[out]	surfacePoints	The points data structure to put the constrained points in. (vtkpoints)<br>
maximumSearchRadiusTolerance	Maximum distance a point can be constrained, specified as a percentage of the model’s bounding box diagonal in world coordinate system. Valid range for this is 0 to 1.</p>
<p>Is the following the correct way to interpret these parameters, and how to access them (in brackets)?<br>
-originalPoints refers to model points (i.e. modelnode.GetPolyData().GetPoints())<br>
-normalVectors refers to model normals (i.e. modelnode.GetPolyData().GetPointData().GetNormals()) returns vtkfloatarray*<br>
-surface polydata refers to the model polydata (i.e. modelnode.GetPolyData()<br>
-surfacePoints refers to any vtk points object to hold the new data (e.g. out = vtk.vtkPointData())</p>
<p>If that is correct I guess my next question would be how to get the normals in the vtkpoints format rather than as a vtkfloatarray</p>

---

## Post #2 by @lassoan (2023-09-18 13:42 UTC)

<p>You can use a higher-level API for this:</p>
<pre><code class="lang-python">someMarkupsNode.SetAndObserveSurfaceConstraintNode(someModelNode)
</code></pre>

---
