# Resample segments in segmentation using Python scripting

**Topic ID**: 26411
**Date**: 2022-11-18
**URL**: https://discourse.slicer.org/t/resample-segments-in-segmentation-using-python-scripting/26411

---

## Post #1 by @YousifAlKhoury (2022-11-18 23:57 UTC)

<p>Is there a way to force the segments to the common image geometry through python code?</p>
<p>I am importing segmentations from a volumelabelmap and I can’t run ‘fill between slices’ on the imported segments.</p>

---

## Post #2 by @lassoan (2022-11-20 21:38 UTC)

<p>Fill between slices should resample all segments into the same geometry. How do you know that it does not?</p>
<p>You can force resampling by applying any operation on it (e.g., paint and erase a point) or saving and loading.</p>

---

## Post #3 by @YousifAlKhoury (2022-11-21 19:02 UTC)

<p>Hi Andras,</p>
<p>I am trying to change the current segmentation node used by the segment editor programmatically. We have a drop-down menu to specify the rough mask (segmentation node) in our module.</p>
<p>We want to select another segmentation node and apply edits on that. However, let’s say for example my rough mask has a segment on slice 1 and 10. When I change to that rough mask and try to fill between slices, nothing happens. But if I apply any paint, even the tiniest bit, on those segments and run fill between slices, it works. So, I am guessing that’s what you meant by any edit forces resampling. However, this is quite time consuming if I have many slices to edit. Therefore, I was asking if this resampling can be done programmatically through python rather than manually applying an edit.</p>
<p>Here is the code I use to import a rough mask into the segment editor, we initially have the rough mask as a label map that we convert to a segmentation node:</p>
<pre><code class="lang-auto">def changeRoughMask(self, roughMaskNode, masterVolumeNode, segmentEditor):
    segmentNode = slicer.mrmlScene.GetNodeByID(self._segmentNodeId)
    slicer.mrmlScene.RemoveNode(segmentNode)

    if (roughMaskNode and masterVolumeNode):
      segmentNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
      segmentNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
      self._segmentNodeId = segmentNode.GetID()
      self.labelmapToSegmentationNode(roughMaskNode, segmentNode)
      # set segmentation node and master volume node in segmentation editor
      segmentEditor.setSegmentationNode(segmentNode)
      segmentEditor.setMasterVolumeNode(masterVolumeNode)
      # update viewer windows
      slicer.util.setSliceViewerLayers(background=masterVolumeNode,
                                      label= segmentNode,
                                      labelOpacity=0.5)
      slicer.util.resetSliceViews()

      return True
    return False
</code></pre>
<p>Thanks.</p>

---

## Post #4 by @lassoan (2022-11-23 22:09 UTC)

<p>This should resample all the segments in the segmentation using the current geometry:</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
segGeomLogic = slicer.vtkSlicerSegmentationGeometryLogic()
segGeomLogic.SetInputSegmentationNode(segmentationNode)
segGeomLogic.SetSourceGeometryNode(segmentationNode)
segGeomLogic.CalculateOutputGeometry()
segGeomLogic.ResampleLabelmapsInSegmentationNode()
</code></pre>

---
