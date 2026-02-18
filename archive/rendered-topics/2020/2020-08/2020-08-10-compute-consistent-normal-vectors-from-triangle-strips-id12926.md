# Compute consistent normal vectors from triangle strips

**Topic ID**: 12926
**Date**: 2020-08-10
**URL**: https://discourse.slicer.org/t/compute-consistent-normal-vectors-from-triangle-strips/12926

---

## Post #1 by @loubna (2020-08-10 13:50 UTC)

<p>Hi,</p>
<p>how can I get consistent normal vectors for each point  from triangle strips (after applying vtkStripper filter)?</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-08-10 14:11 UTC)

<p><code>vtk.vtkPolyDataNormals</code> can compute normals, and has an option to make normals consistent.</p>

---

## Post #3 by @loubna (2020-08-10 14:12 UTC)

<p>Thank you very much for answer</p>

---

## Post #4 by @loubna (2020-08-11 09:12 UTC)

<p>Hi Mr;</p>
<p>I have tried compute normal vectors by turning on some features to ensure the consistency and good orientation but It seems normals are oriented in wrong direction when incorporate them in my reconstrution method.</p>
<p>After converting contours to Ribbon model I have Apply vtkStripper filter to get triangles strips then I have applied vtkPolyDataNormals to get PointNormals like this:</p>
<p>vtkSmartPointer normalGenerator = vtkSmartPointer::New();<br>
normalGenerator-&gt;SetInputData(polydata);<br>
normalGenerator-&gt;ConsistencyOn();<br>
normalGenerator-&gt;ComputePointNormalsOn();<br>
normalGenerator-&gt;SetFlipNormals(0);<br>
normalGenerator-&gt;SetSplitting(0);<br>
normalGenerator-&gt;SetAutoOrientNormals(0);<br>
normalGenerator-&gt;SetNonManifoldTraversal(1);<br>
// normalGenerator-&gt;ComputeCellNormalsOff();<br>
normalGenerator-&gt;Update();</p>
<p>Is there another method to compute normals from triangles strips (ribbons) without passing by constructing binary labelMap? Or is it possible to construct binary labelMap from Ribbon then using vtkProbe filter to attribut consistent normals to Ribbon Model points?</p>
<p>thank’s in advance</p>

---

## Post #5 by @lassoan (2020-08-11 13:23 UTC)

<p>It is only possible to compute consistent normals for closed, watertight mesh - not for a set of ribbons.</p>

---
