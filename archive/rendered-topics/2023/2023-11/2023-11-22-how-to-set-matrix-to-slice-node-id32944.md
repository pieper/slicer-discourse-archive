# How to set matrix to slice node?

**Topic ID**: 32944
**Date**: 2023-11-22
**URL**: https://discourse.slicer.org/t/how-to-set-matrix-to-slice-node/32944

---

## Post #1 by @derekcbr (2023-11-22 05:34 UTC)

<p>matrix_transform = np.array([<br>
[1, 0, 0, 0.2],<br>
[0, 1, 0, 0.3],<br>
[0, 0, 1, 0.4],<br>
[0, 0, 0, 1]<br>
])</p>
<p>viewNode = ‘Green’<br>
sliceNode = slicer.app.layoutManager().sliceWidget(viewNode).mrmlSliceNode()<br>
sliceNode.SetSliceTORAS(slicer.util.vtkMatrixFromArray(matrix_transform))<br>
sliceNode.UpdateMatrices()<br>
AttributeError: ‘MRMLCore.vtkMRMLSliceNode’ object has no attribute ‘SetSliceTORAS’</p>

---
