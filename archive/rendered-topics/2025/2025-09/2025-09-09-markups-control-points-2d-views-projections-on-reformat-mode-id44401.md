---
topic_id: 44401
title: "Markups Control Points 2D Views Projections On Reformat Mode"
date: 2025-09-09
url: https://discourse.slicer.org/t/44401
---

# Markups control Points 2D Views projections on Reformat Mode

**Topic ID**: 44401
**Date**: 2025-09-09
**URL**: https://discourse.slicer.org/t/markups-control-points-2d-views-projections-on-reformat-mode/44401

---

## Post #1 by @sarafv (2025-09-09 11:22 UTC)

<p>Hello,</p>
<p>Following and correcting previous topic about hiding projections of control points, I’v juste realize that the problem with displayNode.SetSliceProjection happens only when 2D  views are on Reformat Mode, the projection of all the control points are visibles and there is no way to hide them with displayNode.SetSliceProjection, whether  in the 5.9  or 5.8 version</p>
<p>Sara</p>

---

## Post #2 by @sarafv (2025-09-10 14:41 UTC)

<p>Hi,</p>
<p>Here an update of my topic. This is not a problem of 3D Slicer, but a weird behavior of a module that I’m upgrading on Slicer 5.8.</p>
<p>I never modify directly in my module “<strong>SliceProjection</strong>” property of Markups display node. But when I reformat the views with the method “<strong>setSliceToRASToMatrix</strong>” (see bellow) and I pass a fieldOfView, the markup’s controlpoints projections become persistant. That is not the case if the method do not modify the node FieldOfView</p>
<pre><code class="lang-auto">  def **setSliceToRASToMatrix**(self,scene,sliceColor,affine,fieldOfView=None,sliceVisible=None):
    """
    Assign the SliceToRAS transformation matrix for the slice corresponding to the input sliceColor.
    Optionally a field-of-view is also set. The fieldOfView is a 3-element vector (x,y,z). The actual
    field-of-view set is adjusted to to match the current slice window aspect ratio.

    :param scene: Slicer scene
    :param sliceColor: slice color like found int const.SLICE_COLOR_XXX
    :param affine: affine matrix corresponding to the SliceToRAS transformation
    :param fieldOfView: field-of-view (optional)
    """


    def getVTK4x4Matrix(matrix):
        """
        Returns a VTK4x4Matrix object corresponding to the AffineMatrix
        """
        vtkMatrix = vtk.vtkMatrix4x4()
        for row in range(4):
          for col in range(4):
            vtkMatrix.SetElement(row, col, matrix[row,col])
        return vtkMatrix

    node = self.getSliceNodeByColor(scene,sliceColor)

    if node is not None:
      modifyId = node.StartModify()

      node.GetSliceToRAS().DeepCopy(getVTK4x4Matrix(affine))
      if fieldOfView is not None:
          dimX,dimY,_dimZ = node.GetDimensions()
          fieldOfViewX = fieldOfView[1]*dimX/float(dimY)
          node.SetFieldOfView(fieldOfViewX,fieldOfView[1],fieldOfView[2])
      if sliceVisible is not None:
          node.SetSliceVisible(sliceVisible)
      node.UpdateMatrices()
      node.SetSliceOrigin([0,0,0])
      node.EndModify(modifyId)

</code></pre>
<p>So If I do a call  like</p>
<pre><code class="lang-auto"> self.setSliceToRASToMatrix(slicer.mrmlScene,color, self.getSliceReformatTransform(type))

</code></pre>
<p>All is going all right. But with this :</p>
<pre><code class="lang-auto">
def getFieldOfView(self):
    fov = [self.getLength() / 3 * 5] * 3 # trajectory occupy 3/5 of the slice view
    return fov

fieldOfView=self.getFieldOfView()

self.setSliceToRASToMatrix(slicer.mrmlScene,color,self.getSliceReformatTransform(type),fieldOfView=fieldOfView)

</code></pre>
<p>The markup control points projections become persistants in the 2D views …</p>
<p>Does anyone know what is going on?</p>

---
