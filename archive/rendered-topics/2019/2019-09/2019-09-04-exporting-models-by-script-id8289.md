# Exporting models by script

**Topic ID**: 8289
**Date**: 2019-09-04
**URL**: https://discourse.slicer.org/t/exporting-models-by-script/8289

---

## Post #1 by @Ihsan_MUTLU (2019-09-04 13:16 UTC)

<p>Hi!<br>
I am having a problem exporting models as obj files.<br>
I have created a model hierarcy node and filled it as follows:<br>
exportedModelsNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLModelHierarchyNode’)<br>
slicer.modules.segmentations.logic().ExportAllSegmentsToModelHierarchy(seg, exportedModelsNode)<br>
Now I want to get model nodes under newly created model hierarcy node with a for loop using below code.<br>
slicer.modules.models.logic().SaveModel(‘C:/Users/Desktop/aaa.obj’, <strong>modelNode</strong>)<br>
How can I get model nodes inside <strong>exportedModelsNode</strong> ??</p>

---

## Post #2 by @lassoan (2019-09-04 13:50 UTC)

<p>I would recommend to use <a href="https://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a4b5328985b2d98cbbc93a5b2ae7fde6b" rel="nofollow noopener">slicer.modules.segmentations.logic().ExportSegmentsClosedSurfaceRepresentationToFiles()</a> method directly.</p>

---

## Post #3 by @Ihsan_MUTLU (2019-09-04 18:12 UTC)

<p>Thanks, that did the job.<br>
Also, I managed to get nodes by:<br>
modelNodes = slicer.mrmlScene.GetNodesByClass(‘vtkMRMLModelNode’)</p>

---
