# Get POINTS and Polydata?

**Topic ID**: 2512
**Date**: 2018-04-04
**URL**: https://discourse.slicer.org/t/get-points-and-polydata/2512

---

## Post #1 by @MGM (2018-04-04 10:33 UTC)

<p>Hello,</p>
<p>I’m working on vtk, and I’m looking for a solution, to generate a vtk file, which contains, POINTS and Polydata.</p>
<p>in others way, no need to SCALARS and NORMALS.</p>
<p>I used " vtkPolyDataWriter ", to generate the vtk file.</p>
<p>any suggestion</p>

---

## Post #2 by @lassoan (2018-04-04 18:29 UTC)

<p>This is a general VTK question and not specific to Slicer, but here is the solution anyway:</p>
<pre><code>while mypolydata.GetPointData().GetNumberOfArrays()&gt;0:
  mypolydata.GetPointData().RemoveArray(0)</code></pre>

---
