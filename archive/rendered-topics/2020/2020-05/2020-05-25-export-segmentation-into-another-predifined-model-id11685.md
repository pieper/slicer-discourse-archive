# Export segmentation Into another predifined model

**Topic ID**: 11685
**Date**: 2020-05-25
**URL**: https://discourse.slicer.org/t/export-segmentation-into-another-predifined-model/11685

---

## Post #1 by @siaeleni (2020-05-25 00:44 UTC)

<p>Hi,</p>
<p>I am not sure what is the best way to export a segmentation to a predefined empty vtkMRMLModelNode?<br>
Assume that I have a vtkMRMLModelNode named “Model”.<br>
I currently use the following</p>
<blockquote>
<p>shNode = slicer.mrmlScene.GetSubjectHierarchyNode()<br>
exportFolderItemId = shNode.CreateFolderItem(shNode.GetSceneItemID(), “Segments”)<br>
slicer.modules.segmentations.logic().ExportAllSegmentsToModels(outSegmentation, exportFolderItemId)</p>
</blockquote>
<p>but I want to export directly to the node = slicer.util.getNode(“Model”)<br>
Is it possible?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-05-25 03:20 UTC)

<p>You can set vtkPolyData from a segmentation node as shown in these <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_a_representation_of_a_segment">examples in the script repository</a>.</p>

---
