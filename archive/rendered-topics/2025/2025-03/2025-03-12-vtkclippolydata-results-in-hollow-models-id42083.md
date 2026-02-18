# vtkClipPolyData results in hollow models

**Topic ID**: 42083
**Date**: 2025-03-12
**URL**: https://discourse.slicer.org/t/vtkclippolydata-results-in-hollow-models/42083

---

## Post #1 by @huwqchn (2025-03-12 08:41 UTC)

<p>Hello All,</p>
<p>I’m trying to use <code>vtkClipPolyData()</code> to split a model into two separate segments within a scripted segment editor effect. The operation itself works, but the resulting models are hollow shells (open surfaces) rather than closed, solid segments. I need these segments to be closed surfaces after clipping.</p>
<p>Here is my current code snippet:</p>
<pre><code class="lang-auto">def cutSurfaceWithModel(self, segmentMarkupNode, segmentModel):
    parameterSetNode = self.scriptedEffect.parameterSetNode()
    segmentationNode = parameterSetNode.GetSegmentationNode()
    if not segmentationNode:
        logging.warning("No segmentation node is available.")
        return

    segmentID = parameterSetNode.GetSelectedSegmentID()
    if not segmentID:
        logging.warning("No selected segment to cut.")
        return

    segmentIDs = vtk.vtkStringArray()
    segmentIDs.InsertNextValue(segmentID)

    shNode = slicer.mrmlScene.GetSubjectHierarchyNode()
    exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), "TempExportFolder")
    slicer.modules.segmentations.logic().ExportSegmentsToModels(segmentationNode, segmentIDs, exportFolderItemId)

    modelItemIDs = vtk.vtkIdList()
    shNode.GetItemChildren(exportFolderItemId, modelItemIDs)
    if modelItemIDs.GetNumberOfIds() &lt; 1:
        logging.warning("No segment was exported to model.")
        return

    sourceNode = slicer.mrmlScene.GetNodeByID(shNode.GetItemDataNode(modelItemIDs.GetId(0)).GetID())
    sourcePolyData = vtk.vtkPolyData()
    sourcePolyData.DeepCopy(sourceNode.GetPolyData())
    shNode.RemoveItem(exportFolderItemId)

    segmentPolyData = segmentModel.GetPolyData()
    clipFunction = vtk.vtkImplicitPolyDataDistance()
    clipFunction.SetInput(segmentPolyData)

    clipper = vtk.vtkClipPolyData()
    clipper.SetInputData(sourcePolyData)
    clipper.SetClipFunction(clipFunction)
    clipper.GenerateClippedOutputOn()
    clipper.InsideOutOn()
    clipper.Update()

    insidePolyData = vtk.vtkPolyData()
    insidePolyData.DeepCopy(clipper.GetOutput())

    outsidePolyData = vtk.vtkPolyData()
    outsidePolyData.DeepCopy(clipper.GetClippedOutput())

    segmentationNode.AddSegmentFromClosedSurfaceRepresentation(insidePolyData, "TPSCut_Inside")
    segmentationNode.AddSegmentFromClosedSurfaceRepresentation(outsidePolyData, "TPSCut_Outside")
</code></pre>

---
