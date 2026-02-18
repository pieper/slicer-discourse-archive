# From labelmap to model and from model to labelmap python scripts

**Topic ID**: 15833
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/from-labelmap-to-model-and-from-model-to-labelmap-python-scripts/15833

---

## Post #1 by @brhoom (2021-02-04 09:35 UTC)

<p>Dear all,</p>
<p>I wrote these to functions to convert between labelmap and model nodes. Is there a similar simple non-slicer solution e.g. using only itk and vtk?</p>
<pre><code> def lbl2model(lblNode,lblName):
     segNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
     segNode.SetName(lblName)
     slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(lblNode, segNode)
     modelHNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLModelHierarchyNode")
     slicer.modules.segmentations.logic().ExportAllSegmentsToModelHierarchy(segNode, modelHNode)
     vColls = vtk.vtkCollection()
     modelHNode.GetChildrenModelNodes(vColls)
     modelNode = vColls.GetItemAsObject(0)
     return modelNode

def model2lbl(modelNode,modelName,refNode):
     segNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
     segNode.SetName(modelName)
     slicer.modules.segmentations.logic().ImportModelToSegmentationNode(modelNode,segNode)
     labelmapVolumeNode = 
     slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
     labelmapVolumeNode.SetName(modelName)
     ids = vtk.vtkStringArray()
     segNode.GetDisplayNode().GetVisibleSegmentIDs(ids)
     slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segNode, ids,labelmapVolumeNode, refNode)
     return labelmapVolumeNode</code></pre>

---

## Post #2 by @lassoan (2021-02-04 14:22 UTC)

<p>All these methods use VTK filters - about 5-10 processing steps, including various smoothing, cleaning, simplification, etc. to make the conversion more robust and accurate. You can find the exact steps in “conversion rule” classes <a href="https://github.com/Slicer/Slicer/tree/master/Libs/vtkSegmentationCore">here</a>. ITK does not have that many surface mesh processing filters, but it can do basic conversion between labelmaps and surfaces.</p>
<p>Note that you can run Slicer scripts from the command-line and you can use any Python package in Slicer’s virtual Python environment as you would use any other Python virtual environments.</p>

---

## Post #3 by @brhoom (2021-02-04 15:27 UTC)

<blockquote>
<p>All these methods use VTK filters - about 5-10 processing steps, including various smoothing, cleaning, simplification, etc. to make the conversion more robust and accurate. You can find the exact steps in “conversion rule” classes <a href="https://github.com/Slicer/Slicer/tree/master/Libs/vtkSegmentationCore" rel="noopener nofollow ugc">here</a>. ITK does not have that many surface mesh processing filters, but it can do basic conversion between labelmaps and surfaces.</p>
</blockquote>
<p>Thanks for your informative and quick reply, I will have a look at the link.</p>
<blockquote>
<p>Note that you can run Slicer scripts from the command-line and you can use any Python package in Slicer’s virtual Python environment as you would use any other Python virtual environments</p>
</blockquote>
<p>This is what I am using now.</p>

---
