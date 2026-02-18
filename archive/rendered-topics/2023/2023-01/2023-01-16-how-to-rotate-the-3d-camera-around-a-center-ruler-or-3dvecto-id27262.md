# How to rotate the 3d camera around a center ruler or 3dvector

**Topic ID**: 27262
**Date**: 2023-01-16
**URL**: https://discourse.slicer.org/t/how-to-rotate-the-3d-camera-around-a-center-ruler-or-3dvector/27262

---

## Post #1 by @jay1987 (2023-01-16 13:47 UTC)

<p>the basic camera action is Yaw,Azimuth,Elevation,is it possible to rotate camera around like vector line [2,1,3]?</p>

---

## Post #2 by @jay1987 (2023-01-17 01:39 UTC)

<p>use vtkTransform can do it</p>
<pre><code class="lang-auto">    transform_node = self.camera_node.GetParentTransformNode()
    if not transform_node:
      transform_node = util.AddNewNodeByNameByClass("vtkMRMLLinearTransformNode")
      self.camera_node.SetAndObserveTransformNodeID(transform_node.GetID())
      transform_node = self.camera_node.GetParentTransformNode()

    modelToParentTransform = vtk.vtkMatrix4x4()
    handleToWorldMatrix = vtk.vtkTransform()
    handleToWorldMatrix.PostMultiply()
    handleToWorldMatrix.Translate(-self.focus_point[0], -self.focus_point[1], -self.focus_point[2])
    handleToWorldMatrix.RotateWXYZ(val,self.cemera_vector_normalized)
    handleToWorldMatrix.Translate(self.focus_point)
    modelToParentTransform.DeepCopy(handleToWorldMatrix.GetMatrix())
    transform_node.SetMatrixTransformToParent(modelToParentTransform)
</code></pre>

---
