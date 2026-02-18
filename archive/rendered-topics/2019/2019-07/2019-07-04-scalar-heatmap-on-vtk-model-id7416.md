# Scalar heatmap on vtk model

**Topic ID**: 7416
**Date**: 2019-07-04
**URL**: https://discourse.slicer.org/t/scalar-heatmap-on-vtk-model/7416

---

## Post #1 by @jlaframboise (2019-07-04 17:05 UTC)

<p>I am looking to color a vtk curve model with the curvature at each point on the curve. I have working code that does this but when I save all the elements in the scene including the curve.vtk model, and reopen it in slicer, the scalar that colors the curve is not there. My current approach is below. Perhaps this is not working as expected because I am modifying the polydata not the node object? (Edit: see bottom for solution)</p>
<pre><code>polyData = curveNode.GetPolyData()
curvatureArray = vtk.vtkDoubleArray()

…get the desired curvature value for each point on the model…

# add the curvature data as a scalar to the curve model
polyData.GetPointData().AddArray(curvatureArray)
curveDisplayNode = curveNode.GetDisplayNode()

# activate this scalar in its dispay node
curveDisplayNode.SetActiveScalarName('Curvature')
curveDisplayNode.SetScalarVisibility(1)
</code></pre>
<p>Would using the void vtkMRMLModelNode.AddPointScalars(vtkDataArray) function work?</p>
<p>Thanks!</p>
<h1>Update:</h1>
<p>Display properties are not saved with the node, but the scalar is still stored in the curve.vtk node. This means that when it is loaded, you need to click edit properties and re-select the scalar and make it active. This solves my issues. Thanks to Andras Lasso.</p>

---
