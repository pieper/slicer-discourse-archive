# Isodose model is only 1 file for all of them

**Topic ID**: 34395
**Date**: 2024-02-19
**URL**: https://discourse.slicer.org/t/isodose-model-is-only-1-file-for-all-of-them/34395

---

## Post #1 by @LukasKnybel (2024-02-19 12:10 UTC)

<p>Dear Slicer Users,<br>
I have Slicer 5.6.0 now with Radiotherapy module. When I generate isodoses from RTdose dicom file, only 1 model for all isodoses is created (looks like sum of all).<br>
In previous version of Slicer it was possible to see each isodose separately and also to export isodoses to models separately.<br>
I am not sure if I have a chance to do something differently or there is no longer possibility to generate isodoses separately.</p>
<p>Thank you!</p>
<p>Lukas</p>

---

## Post #2 by @cpinter (2024-02-19 13:15 UTC)

<p>It has been a conscious decision to change the output of the Isodose module to a single model, where the isodose levels are indicated as scalars in that model. If you need separate models, you can use VTK to separate the surfaces for each scalar value. You can use a function like this:</p>
<pre><code class="lang-auto">#----------------------------------------------------------------------------
def getPolyDataFromScalarValue(modelPolyData, targetScalarValue, scalarName):
  """
  Get polydata based on the value of the scalar array.
  :param modelPolyData: input polydata
  :param scalarValue: points with this scalar value will be kept
  :param scalarName: name of the scalar array
  :return vtkPolyData: output polydata
  """
  # Select points in polydata
  selectedPointIds = vtk.vtkIdTypeArray()
  numPoints = modelPolyData.GetNumberOfPoints()
  modelPointValues = modelPolyData.GetPointData().GetArray(scalarName)
  for pointId in range(numPoints):
    scalarValue = modelPointValues.GetTuple(pointId)[0]
    if scalarValue == targetScalarValue:
      loc = selectedPointIds.InsertNextValue(pointId)
  # Extract selected points
  selectionNode = vtk.vtkSelectionNode()
  selectionNode.SetFieldType(vtk.vtkSelectionNode.POINT)
  selectionNode.SetContentType(vtk.vtkSelectionNode.INDICES)
  selectionNode.SetSelectionList(selectedPointIds)
  selectionNode.GetProperties().Set(vtk.vtkSelectionNode.CONTAINING_CELLS(), 1)
  selection = vtk.vtkSelection()
  selection.AddNode(selectionNode)
  extractSelection = vtk.vtkExtractSelection()
  extractSelection.SetInputData(0, modelPolyData)
  extractSelection.SetInputData(1, selection)
  extractSelection.Update()
  convertToPolydata = vtk.vtkDataSetSurfaceFilter()
  convertToPolydata.SetInputConnection(extractSelection.GetOutputPort())
  convertToPolydata.Update()
  return convertToPolydata.GetOutput()
</code></pre>

---

## Post #3 by @LukasKnybel (2024-02-20 15:55 UTC)

<p>Thanks a lot for this! I will try.</p>
<p>Best regards</p>
<p>Lukas</p>

---
