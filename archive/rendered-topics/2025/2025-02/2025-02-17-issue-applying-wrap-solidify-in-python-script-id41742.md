---
topic_id: 41742
title: "Issue Applying Wrap Solidify In Python Script"
date: 2025-02-17
url: https://discourse.slicer.org/t/41742
---

# Issue Applying Wrap Solidify in Python Script

**Topic ID**: 41742
**Date**: 2025-02-17
**URL**: https://discourse.slicer.org/t/issue-applying-wrap-solidify-in-python-script/41742

---

## Post #1 by @Miri_Trope (2025-02-17 14:37 UTC)

<p>Dear community,</p>
<p>I’m trying to apply <strong>Wrap Solidify</strong> in a Python script following the instructions provided <a href="https://lassoan.github.io/SlicerSegmentationRecipes/SkinSurface2/" rel="noopener nofollow ugc">here</a>. I’ve attached the code:</p>
<blockquote>
<h1>Create a segmentation node</h1>
<p>segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)<br>
segmentationNode.CreateDefaultDisplayNodes()<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)</p>
<h1>Create segment editor</h1>
<p>segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentEditorNode”)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)</p>
</blockquote>
<blockquote>
<h1>Configure segment editor for thresholding</h1>
<p>segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setSourceVolumeNode(masterVolumeNode)</p>
<h1>Apply Threshold Effect</h1>
<p>segmentEditorWidget.setActiveEffectByName(“Threshold”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“MinimumThreshold”, 30)<br>
effect.setParameter(“MaximumThreshold”, 800)<br>
effect.self().onApply()<br>
print(“Threshold effect applied successfully.”)</p>
<h1>Apply Islands Effect</h1>
<p>segmentEditorWidget.setActiveEffectByName(“Islands”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“MinimumSize”, 1000)  # Minimum size in mm³ for islands to keep (adjust as needed)<br>
effect.setParameter(“MaxIslandCount”, 0)  # Set to 0 to remove all islands smaller than the size threshold<br>
effect.self().onApply()<br>
print(“Islands effect applied successfully.”)</p>
<h1>Apply Wrap Solidify Effect</h1>
<p>segmentEditorWidget.setActiveEffectByName(“Wrap Solidify”)<br>
effect = segmentEditorWidget.activeEffect()<br>
effect.setParameter(“OuterSurface”, True)<br>
effect.setParameter(“CarveHoles”, True)<br>
effect.setParameter(“SmoothingFactor”, 25)  # Corrected parameter<br>
effect.self().onApply()<br>
print(“Wrap Solidify effect applied successfully.”)</p>
</blockquote>
<p>However, I’m encountering the following error:</p>
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
<p>Does anyone have suggestions on how to resolve it?</p>

---

## Post #2 by @Miri_Trope (2025-05-27 12:41 UTC)

<p>Hi again, I found the cause of the error: it seems WrapSolidify needs a separate region segment from the one being wrapped. I was using the same segment, which triggered the <code>ValueError: Region segment cannot be the same segment as the current segment</code>.</p>
<p>I’d appreciate a working Python snippet that demonstrates how to properly define and assign the region segment programmatically (e.g., using <code>effect.setParameter(RegionSegmentID)</code>). Is there a recommended way to set this parameter reliably from code?</p>
<p>Thank you!</p>

---
