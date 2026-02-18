# Extract brain cavity using script

**Topic ID**: 17270
**Date**: 2021-04-23
**URL**: https://discourse.slicer.org/t/extract-brain-cavity-using-script/17270

---

## Post #1 by @park (2021-04-23 08:43 UTC)

<p>Hi everyone</p>
<p>I would like to extract the cavity of brain space using “Wrap solidify” and Python script.</p>
<p>This is my code to implement what I thought<br>
Before performing the “Wrap solidify”, the segmentation using "Threshold " works well. However, “Wrap solidify” gives the error “ValueError: Region segment cannot be the same segment as the current segment”</p>
<p>Could I get a solution to this error?</p>
<blockquote>
<h1>Compute</h1>
<p>masterVolumeNode = getNode(“InputVolume”)</p>
<h1>Create segmentation</h1>
<p>segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
<span class="hashtag-raw">#segmentationNode</span> = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLSegmentationNode”)<br>
<span class="hashtag-raw">#segmentationNode</span> = slicer.util.getNode(‘Segmentation_1’)<br>
segmentationNode.CreateDefaultDisplayNodes() # only needed for display<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)</p>
<h1>Create temporary segment editor to get access to effects</h1>
<p>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentEditorNode”)</p>
<h1>Do masking</h1>
<p>addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(“skull”)<br>
segmentEditorNode.SetMaskSegmentID(addedSegmentID)<br>
segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteAllSegments)<br>
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedInsideSingleSegment)</p>
<p>segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)<br>
segmentationDisplayNode=segmentationNode.GetDisplayNode()<br>
segmentation=segmentationNode.GetSegmentation()</p>
<p>segmentEditorWidget.setActiveEffectByName(“Threshold”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“MinimumThreshold”, 250)<br>
effect.setParameter(“MaximumThreshold”, 3000)<br>
effect.self().onApply()</p>
<p>segmentEditorWidget.setActiveEffectByName(“Wrap Solidify”)<br>
effect2 = segmentEditorWidget.activeEffect()<br>
effect2.setParameter(“Largest cavity”, True)<br>
effect2.setParameter(“Carve holes”, True)<br>
effect2.setParameter(“Carve holes”, 25)</p>
<p>effect2.self().onApply()</p>
</blockquote>

---

## Post #2 by @Miri_Trope (2025-02-15 18:10 UTC)

<p>I’ve implemented something similar to this <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9" rel="noopener nofollow ugc">approach</a> and encountered the same error. I noticed that there hasn’t been a response yet—maybe someone can help now?</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-33216/SurfaceWrapSolidify/lib/Slicer-5.8/qt-scripted-modules/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py”, line 252, in onApply<br>
self.logic.applyWrapSolidify()<br>
File “/Applications/Slicer.app/Contents/Extensions-33216/SurfaceWrapSolidify/lib/Slicer-5.8/qt-scripted-modules/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py”, line 338, in applyWrapSolidify<br>
regionPd = self._getInitialRegionPd()<br>
File “/Applications/Slicer.app/Contents/Extensions-33216/SurfaceWrapSolidify/lib/Slicer-5.8/qt-scripted-modules/SegmentEditorWrapSolidifyLib/SegmentEditorEffect.py”, line 526, in _getInitialRegionPd<br>
raise ValueError(“Region segment cannot be the same segment as the current segment”)<br>
ValueError: Region segment cannot be the same segment as the current segment</p>
</blockquote>

---
