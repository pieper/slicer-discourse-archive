# Create Model from segment with certain color

**Topic ID**: 14294
**Date**: 2020-10-28
**URL**: https://discourse.slicer.org/t/create-model-from-segment-with-certain-color/14294

---

## Post #1 by @Christos_Tzerefos (2020-10-28 23:39 UTC)

<p>Hello to all,<br>
I managed to create a model from a segmentation.</p>
<blockquote>
<p>shNode = slicer.mrmlScene.GetSubjectHierarchyNode()<br>
sceneItemID = shNode.GetSceneItemID()<br>
exportFolderItemId = shNode.CreateFolderItem(sceneItemID , “Models”)<br>
FinalModel = slicer.modules.segmentations.logic().ExportAllSegmentsToModels(segmentationNode, exportFolderItemId)</p>
</blockquote>
<p>How can I set the color of the model? I tried to use the following code but the final model had no details.</p>
<blockquote>
<p>FinalModel=slicer.mrmlScene.GetFirstNode(NameOfModel,‘vtkMRMLModelNode’)<br>
modelDisplayNode = FinalModel.GetDisplayNode()<br>
modelDisplayNode .SetColor(250,0,0)</p>
</blockquote>

---

## Post #2 by @lassoan (2020-10-28 23:46 UTC)

<p>Colors of the exported models are taken from the segment colors, so the easiest is to set the segment’s color before the model export.</p>

---
