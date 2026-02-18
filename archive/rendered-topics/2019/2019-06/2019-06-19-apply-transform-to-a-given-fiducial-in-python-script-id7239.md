# Apply transform to a given fiducial in Python script

**Topic ID**: 7239
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/apply-transform-to-a-given-fiducial-in-python-script/7239

---

## Post #1 by @Eloise (2019-06-19 13:51 UTC)

<p>Hi all,</p>
<p>I have a vtkMRMLMarkupsFiducialNode that contains multiple fiducials corresponding to distinct labels and I would like to apply a specific vtkMRMLTransform to each given fiducial depending on its label.<br>
I have found how to apply a given transform to the vtkMRMLMarkupsFiducialNode using<br>
FiducialsNode.SetAndObserveTransformNodeID(localTransformNode.GetID()) but I don’t know how to do it for each fiducial independently.</p>
<p>Can someone point me in the right direction? Thanks!</p>

---

## Post #2 by @lassoan (2019-06-19 14:07 UTC)

<p>If you need to apply a different transform to each point then you need to iterate through the points, get the point position, compute transformed position, and set the modified value.</p>
<p>If you only have linear transforms then you can use <a href="https://apidocs.slicer.org/v4.8/classvtkMRMLTransformNode.html#a5d2d93382aa7da7ec3d9a27987305bce" rel="nofollow noopener">GetMatrixTransformToWorld</a> method to get the transformation matrix and use its <a href="https://vtk.org/doc/nightly/html/classvtkMatrix4x4.html#a63b1e05c7e106bbee9cc606c27d6260d" rel="nofollow noopener">MultiplyPoint</a> method to get the transformed coordinates (input and output are homogeneous coordinates: <code>[x, y, z, 1.0]</code>)</p>

---

## Post #3 by @Eloise (2019-07-24 08:19 UTC)

<p>Hi,</p>
<p>I’m re-opening the question. The solution works perfectly when I only have linear transforms, then, what can I do when vtkMRMLTransform is a composite of Bspline and linear transforms, since I cannot get the transformation matrix (GetMatrixTransformToWorld returns 0) ?<br>
Thanks for your help!</p>

---

## Post #4 by @lassoan (2019-07-25 03:39 UTC)

<p>For general (non-linear, potentially composite) transforms you can get it using <code>slicer.vtkMRMLTransformNode.GetTransformBetweenNodes</code> and use its <code>TransformPoint</code> method to transform point coordinates. See complete example in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" rel="nofollow noopener">script repository</a>.</p>

---
