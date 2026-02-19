---
topic_id: 28242
title: "Using Segment Editor Programmatically To Perform Intersectio"
date: 2023-03-09
url: https://discourse.slicer.org/t/28242
---

# Using segment editor programmatically to perform intersection gives strange result

**Topic ID**: 28242
**Date**: 2023-03-09
**URL**: https://discourse.slicer.org/t/using-segment-editor-programmatically-to-perform-intersection-gives-strange-result/28242

---

## Post #1 by @rhodesdante (2023-03-09 00:47 UTC)

<p>I was performing <a href="https://discourse.slicer.org/t/how-to-programmatically-use-logical-operator-add-function-from-segment-editor/16581">logical operations on some segmentations programmatically</a>, when I stumbled across a bizarre occurrence: when performing intersection, I had to rerun my intersection function (with the exact same parameters) to completely perform the intersection–running it once resulted in a partially intersected output. I checked using the GUI’s segment editor, and it was able to perform the intersection in one go. I am wondering if there is a parameter I need to change in my intersection and/or setup functions.</p>
<p>For reference, I will paste my setup and intersection code below, along with the script I ran to get this strange output:</p>
<pre><code class="lang-auto">def setupSegmentEditor():
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
    slicer.mrmlScene.AddNode(segmentEditorNode)
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    workHorse = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", "workHorse")  # segmentation node that will do all processing
    masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")  # background volume (irrelevant, but necessary to define)
    assert(masterVolumeNode is not None)
    segmentEditorWidget.setSegmentationNode(workHorse)
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)
    segmentEditorWidget.setActiveEffectByName('Logical operators')
    segmentationLogic = slicer.modules.segmentations.logic()
    segmentEditorNode.SetMaskMode(workHorse.EditAllowedInsideAllSegments)
    segmentEditorNode.SetOverwriteMode(segmentEditorNode.OverwriteAllSegments)
    return segmentEditorWidget, segmentEditorNode, workHorse, masterVolumeNode, segmentationLogic

def intersectSegments(segmentEditorNode, segmentEditorWidget, baseSegmentID, toIntersectSegmentID):
  segmentEditorNode.SetSelectedSegmentID(baseSegmentID)
  segmentEditorWidget.setActiveEffectByName('Logical operators')
  effect = segmentEditorWidget.activeEffect()
  effect.setParameter("Operation", SegmentEditorEffects.LOGICAL_INTERSECT)
  effect.setParameter("BypassMasking",1)
  effect.setParameter("ModifierSegmentID",toIntersectSegmentID)
  effect.self().onApply()

# script
segmentEditorWidget, segmentEditorNode, workHorse, masterVolumeNode, segmentationLogic = setupSegmentEditor()

# works
intersectSegments(segmentEditorNode, segmentEditorWidget, baseSegmentID, toIntersectSegmentID)
intersectSegments(segmentEditorNode, segmentEditorWidget, baseSegmentID, toIntersectSegmentID)

# Does not work
intersectSegments(segmentEditorNode, segmentEditorWidget, baseSegmentID, toIntersectSegmentID)

</code></pre>
<p>If it would help, I would be happy to provide the segmentationNode and segmentIDs I was using. Thanks!</p>

---

## Post #2 by @rhodesdante (2023-03-09 21:39 UTC)

<p>I found something that may help answer this question. Changing the master volume affects the result of the intersection operation without changing other parameters. How does the choice of master volume affect, say, the logical intersection operation between two segmentations?</p>

---

## Post #3 by @rhodesdante (2023-03-09 21:56 UTC)

<p>I suppose to make this question more broadly applicable to the community, what I am trying to do is take segmentations which are registered to one another (but from different source volumes) and perform logical operations to perform a union or an intersection. In that sense, there is no “master volume”, as the segmentations are coming from separate volumes. The logical operations seem like they might depend on the master volume, but I would prefer the operation to be agnostic to the choice of master volume.</p>

---

## Post #4 by @muratmaga (2023-03-09 22:16 UTC)

<aside class="quote no-group" data-username="rhodesdante" data-post="3" data-topic="28242">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dec6dc/48.png" class="avatar"> rhodesdante:</div>
<blockquote>
<p>logical operations seem like they might depend on the master volume, but I would prefer the operation to be agnostic to the choice of master volume.</p>
</blockquote>
</aside>
<p>But the geometry of the segmentation needs to come from somewhere. That’s what the master volume provides. If you two volumes are registered, then you should be in the same physical space, and you should be able to use either one of them.</p>

---

## Post #5 by @rhodesdante (2023-03-09 22:23 UTC)

<p>I see–it makes sense that the segmentation needs a geometry as a reference. A quick clarifying question: my volumes are registered in the sense that they are in the correct location &amp; orientation in world coordinates. However, they have different relative orientations (and positions). Is it still sufficient to choose either volume as the master volume? And thank you very much!</p>

---
