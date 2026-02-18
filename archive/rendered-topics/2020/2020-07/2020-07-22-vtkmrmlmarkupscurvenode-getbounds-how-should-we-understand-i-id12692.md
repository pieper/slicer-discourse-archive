# vtkMRMLMarkupsCurveNode.GetBounds() : how should we understand it?

**Topic ID**: 12692
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/vtkmrmlmarkupscurvenode-getbounds-how-should-we-understand-it/12692

---

## Post #1 by @chir.set (2020-07-22 16:19 UTC)

<p>I expected the bounds from vtkMRMLMarkupsCurveNode.GetBounds() to stop at the extreme XYZ values in both directions on each axis. It seems that the returned bounds exceed these values, with greater excess as the length is on an axis.</p>
<p>This code creates an annotation ROI, positioned at the center of the returned bounds, and extending the ROI as per the computed length on each axis.</p>
<blockquote>
<p>bounds = numpy.zeros(6)<br>
inputCurve.GetRASBounds(bounds)<br>
roi=slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLAnnotationROINode”)<br>
box = vtk.vtkBoundingBox(bounds)<br>
center = [0.0, 0.0, 0.0]<br>
box.GetCenter(center)<br>
roi.SetXYZ(center)<br>
roi.SetRadiusXYZ(box.GetLength(0), box.GetLength(1), box.GetLength(2))</p>
</blockquote>
<p>The result is as shown below.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf84412b2213a334ca2e5e58bc4a3c2b2188ecc2.png" alt="boundsByCode" data-base62-sha1="rkey9RzBOpzOeMWa7fnDGR7Yq9Y" width="605" height="449"></p>
<p>The expected result would be as below.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/4/e4c4481141fa142ac42222fc9e907f83e02150a7.png" alt="boundsIdealized" data-base62-sha1="wDLosk6L2GBVERyilaMvS3BZQID" width="605" height="449"></p>
<p>How should we then expect, intreprete and use the returned value of GetBounds()? Is there a way to calculate the excess margins on each axis ?</p>
<p>Thank you.</p>

---

## Post #2 by @lassoan (2020-07-22 16:22 UTC)

<blockquote>
<p>roi.SetRadiusXYZ(box.GetLength(0), box.GetLength(1), box.GetLength(2))</p>
</blockquote>
<p><code>SetRadiusXYZ</code> method expects radius. Divide box side length by 2.0 to get the radius.</p>

---

## Post #3 by @chir.set (2020-07-22 17:22 UTC)

<p>Yes… radius… the function name was clear enough ! Thanks.</p>

---
