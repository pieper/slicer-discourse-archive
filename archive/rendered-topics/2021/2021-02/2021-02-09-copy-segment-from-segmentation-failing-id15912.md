---
topic_id: 15912
title: "Copy Segment From Segmentation Failing"
date: 2021-02-09
url: https://discourse.slicer.org/t/15912
---

# Copy Segment from Segmentation Failing

**Topic ID**: 15912
**Date**: 2021-02-09
**URL**: https://discourse.slicer.org/t/copy-segment-from-segmentation-failing/15912

---

## Post #1 by @Pete (2021-02-09 09:05 UTC)

<p>Hi,</p>
<p>Any help greatly appreciated. I am trying to copy a segment from one segmentation to another (Copy segment “Single” from segmentation “Segmentation” to new segmentation “Margin Expansion” to new segment “Margin + Expansion”). The below code seems to work perfectly until the final section and I get error “CopySegmentFromSegmentation: Failed to get segment!”</p>
<pre><code>masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')

# Create segmentation
## Can adjust segmentation name in .AddNewNodeByClass 2nd parameter String
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", "Margin Expansion")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

## Create new segment with specified name
addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("Single + Margin")
segmentEditorNode.SetSelectedSegmentID(addedSegmentID)

## Copy "Single" segment "Segmentation" to new "Margin Expansion" segmentation

sourceSegmentationNode = getNode('Segmentation')
sourceSegmentation = getNode('Segmentation').GetSegmentation()
sourceSegmentId = "Single"

sourceSegmentationNode.GetSegmentation().CopySegmentFromSegmentation(sourceSegmentation, sourceSegmentId)</code></pre>

---

## Post #2 by @Pete (2021-02-09 09:24 UTC)

<p>I just realised what my error was. I was specifying the name of the segment when it required the ID. So I have adjusted to the following:</p>
<pre><code>sourceSegmentationNode = getNode('Segmentation')
sourceSegmentation = getNode('Segmentation').GetSegmentation()
sourceSegmentId = sourceSegmentation.GetSegmentIdBySegmentName("Single")

sourceSegmentationNode.GetSegmentation().CopySegmentFromSegmentation(sourceSegmentation, sourceSegmentId)
</code></pre>
<p>However, the new segment is created in the original Segmentation, not the new one I just created (“Margin Expansion”). Is there a way to fix that?</p>
<p>Alternatively, I can keep it all in the same segmentation but need the ability to name the copied segment something original.</p>
<p>Many thanks in advance,</p>
<p>Pete</p>

---

## Post #3 by @Pete (2021-02-09 10:24 UTC)

<p>I seem to be able find the answers to all my own questions today with a lot of trial and error. In case anyone needs the solutions in the future:</p>
<pre><code>sourceSegmentationNode = getNode('Segmentation')
sourceSegmentation = getNode('Segmentation').GetSegmentation()
sourceSegmentId = sourceSegmentation.GetSegmentIdBySegmentName("Single")

segmentationNode.GetSegmentation().CopySegmentFromSegmentation(sourceSegmentation, sourceSegmentId)
</code></pre>
<p>To rename a segment:</p>
<pre><code>renamedSegmentId = getNode('Margin Expansion').GetSegmentation().GetSegmentIdBySegmentName("Single")
renamedSegment = getNode('Margin Expansion').GetSegmentation().GetSegment(renamedSegmentId)
renamedSegment.GetName()
renamedSegment.SetName('Test')</code></pre>

---
