# Prevent a segment from changing when editing other segments

**Topic ID**: 19433
**Date**: 2021-08-31
**URL**: https://discourse.slicer.org/t/prevent-a-segment-from-changing-when-editing-other-segments/19433

---

## Post #1 by @Saima (2021-08-31 08:16 UTC)

<p>Hi Andras,<br>
I am trying to do the following<br>
import segment to segmentationNode<br>
create a new segment<br>
copy the import segment to new segment<br>
grow the newsegment with margin</p>
<p>When I do all this I do not retain the old imported segment. I could not find mistake. I am pasting code here. Could you please help me in this. Thank you</p>
<pre><code class="lang-python">outputVolume.SetName("brain")
    segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
    #segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolume)
    
    # Create temporary segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    #segmentEditorWidget.setMasterVolumeNode(inputVolume)
    
    #import volume to labelmap     
    slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(outputVolume, segmentationNode) 
    segmentationNode.CreateClosedSurfaceRepresentation()
    segmentEditorWidget.setCurrentSegmentID(segmentationNode.GetSegmentation().GetNthSegmentID(0))
    
    segmentation = segmentationNode.GetSegmentation()
    segmentation.AddEmptySegment("Skull")
    
    #copy brain into this new segment
    segmentEditorWidget.setActiveEffectByName("Logical operators")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation", "UNION")
    brain = segmentation.GetSegmentIdBySegmentName("brain")
    skull = segmentation.GetSegmentIdBySegmentName("skull")
    effect.setParameter("SelectedSegmentID", skull) 
    effect.setParameter("ModifierSegmentID", brain) 
    #segmentEditorWidget.setCurrentSegmentID(skull)
    effect.self().onApply()
    
    #grow the skull
    
    segmentEditorWidget.setActiveEffectByName("Margin")
    effect = segmentEditorWidget.activeEffect()
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    #segmentEditorWidget.setCurrentSegmentID(skull)
    segmentEditorWidget.setActiveEffectByName("Margin")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MarginSizeMm","4")
    effect.setParameter("SelectedSegmentID", skull) 

    effect.self().onApply()
</code></pre>

---

## Post #2 by @lassoan (2021-08-31 13:38 UTC)

<p>You need to enable segments to overlap. Otherwise segments overwrite each other when being edited.</p>

---

## Post #3 by @Saima (2021-09-01 05:44 UTC)

<p>Hi Andras,<br>
Sorry I do not know how to do that.</p>
<p>I searched in examples <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#segmentations" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>
<p>I found this<br>
defaultSegmentEditorNode = slicer.vtkMRMLSegmentEditorNode()<br>
defaultSegmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)<br>
slicer.mrmlScene.AddDefaultNode(defaultSegmentEditorNode)</p>
<p>is this what you are taking about.</p>
<p>but I put this in code still doesnt work. The segment disappears</p>
<p>Any help.</p>
<p>Thanks</p>

---

## Post #4 by @lassoan (2021-09-02 23:41 UTC)

<p>You need to modify the segment editor node that is associated with your segment editor widget.</p>

---

## Post #5 by @Saima (2021-09-03 05:42 UTC)

<p>yes got this</p>
<p>thank you so much</p>

---
