---
topic_id: 16581
title: "How To Programmatically Use Logical Operator Add Function Fr"
date: 2021-03-16
url: https://discourse.slicer.org/t/16581
---

# How to programmatically use logical operator add function from segment editor?

**Topic ID**: 16581
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/how-to-programmatically-use-logical-operator-add-function-from-segment-editor/16581

---

## Post #1 by @akshay_pillai (2021-03-16 17:00 UTC)

<p>Operating system:windows 10<br>
Slicer version:4.11</p>
<p>I want to programmatically use the add operator in the logical operators segment editor effect. Is there any way to do this? I want to use the existing segments in the segmentation nodes and add them with a button click. How do I access this with code?</p>

---

## Post #2 by @mikebind (2021-03-17 07:21 UTC)

<p>Here are a couple python functions I have which I use to copy or subtract segments, adding would be a simple variation:</p>
<pre><code>def setup_segment_editor(segmentationNode=None, masterVolumeNode=None):
  '''Runs standard setup of segment editor widget and segment editor node'''
  if segmentationNode is None:
    # Create segmentation node
    segmentationNode = slicer.vtkMRMLSegmentationNode()
    slicer.mrmlScene.AddNode(segmentationNode)
    segmentationNode.CreateDefaultDisplayNodes()
  segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
  segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
  slicer.mrmlScene.AddNode(segmentEditorNode)
  segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
  segmentEditorWidget.setSegmentationNode(segmentationNode)
  segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
  if masterVolumeNode:
    segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
  return segmentEditorWidget, segmentEditorNode, segmentationNode

def copy_segment(newSegmentName, segmentationNode, segmentIDToCopy):
  """ Copy an existing segment into a new segment without overwriting """
  import SegmentEditorEffects
  segmentEditorWidget, segmentEditorNode, segmentationNode = setup_segment_editor(segmentationNode)
  newSegmentID =  segmentationNode.GetSegmentation().AddEmptySegment(newSegmentName)
  segmentEditorNode.SetSelectedSegmentID(newSegmentID)
  segmentEditorWidget.setActiveEffectByName('Logical operators')
  effect = segmentEditorWidget.activeEffect()
  effect.setParameter("Operation", SegmentEditorEffects.LOGICAL_COPY)
  effect.setParameter("ModifierSegmentID", segmentIDToCopy)
  # Masking Settings
  effect.setParameter("BypassMasking",1) # probably not necessary since I adjust masking settings next
  segmentEditorNode.SetMaskMode(segmentEditorNode.PaintAllowedEverywhere)
  segmentEditorNode.MasterVolumeIntensityMaskOff()
  segmentEditorNode.SetOverwriteMode(segmentEditorNode.OverwriteNone)
  # Do the copy
  effect.self().onApply()
  slicer.mrmlScene.RemoveNode(segmentEditorNode)
  return newSegmentID

def subtract_segment(segmentationNode, segmentID, to_subtract_segmentID):
  '''Perform logical subtraction of to_subtract_segmentID from segmentID'''
  import SegmentEditorEffects
  segmentEditorWidget, segmentEditorNode, segmentationNode = setup_segment_editor(segmentationNode)
  segmentEditorNode.SetSelectedSegmentID(segmentID)
  segmentEditorWidget.setActiveEffectByName('Logical operators')
  effect = segmentEditorWidget.activeEffect()
  effect.setParameter("Operation", SegmentEditorEffects.LOGICAL_SUBTRACT)
  effect.setParameter("BypassMasking",1)
  effect.setParameter("ModifierSegmentID",to_subtract_segmentID)
  effect.self().onApply()
  slicer.mrmlScene.RemoveNode(segmentEditorNode)</code></pre>

---

## Post #3 by @Saima (2021-08-31 07:40 UTC)

<p>I used ADD in the operation name but it says<br>
Processing started</p>
<p>Unknown operation: Add</p>
<p>I used ADD but it still dont recognise</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #4 by @mikebind (2021-08-31 15:59 UTC)

<p>The operation for adding is “SegmentEditorEffects.LOGICAL_UNION” rather than LOGICAL_ADD.</p>

---

## Post #5 by @lassoan (2021-08-31 19:31 UTC)

<p>See description of all parameters in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#effect-parameters">Developer manual</a>.</p>

---
