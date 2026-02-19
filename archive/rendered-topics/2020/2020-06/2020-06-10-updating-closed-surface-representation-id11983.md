---
topic_id: 11983
title: "Updating Closed Surface Representation"
date: 2020-06-10
url: https://discourse.slicer.org/t/11983
---

# Updating Closed Surface Representation

**Topic ID**: 11983
**Date**: 2020-06-10
**URL**: https://discourse.slicer.org/t/updating-closed-surface-representation/11983

---

## Post #1 by @Queen_Rei (2020-06-10 18:43 UTC)

<p>Heya! I am trying to work with the closed surface representation. Manually I can get the results I want. With code it seems as if some of the steps I want it to perform are lost or never occur.</p>
<p><strong>Steps</strong><br>
1. Create a segmentation, set name/color<br>
2. Using the SegmentationEditor set threshold min/max<br>
3. Closed Surface Representation (1.5x Oversampling, 0 joint smoothing, 0 smoothing factor, 0 decimation)<br>
4. Using the SegmentationEditor set median smoothing 2mm to this segmentation<br>
5. Update the Closed Surface Representation (1.5x Oversampling, 1 joint smoothing, 1 smoothing factor, 0.9 decimation)</p>
<p>Essentially, I want to smooth the representation that isn’t decimated. After smoothing, decimate it. I imagine there must be a way to update the surface representation, but I can’t seem to find the necessary snippet to do this. I would appreciate any and all direction on the approach</p>
<pre><code># Access segmentation module
slicer.util.selectModule('Segment Editor')
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(seriesVolumeNode)

# Create spine segment
segmentTypeID = "Spine"
newSegment = slicer.vtkSegment()
newSegment.SetName(segmentTypeID)
newSegment.SetColor([0.89, 0.85, 0.78])
segmentationNode.GetSegmentation().AddSegment(newSegment,segmentTypeID)

# Create segment editor widget to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)

# Access segment editor node
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
slicer.mrmlScene.AddNode(segmentEditorNode)
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(seriesVolumeNode)

# Segment Editor Effect: Thresholding
segmentEditorWidget.setActiveEffectByName("Threshold")
thresholdEffect = segmentEditorWidget.activeEffect()
thresholdEffect.setParameter("MinimumThreshold","90")
thresholdEffect.self().onApply()
thresholdEffect.setParameter("MaximumThreshold","1600")
thresholdEffect.self().onApply()

# Create Closed Surface Representation
segmentationNode.GetSegmentation().SetConversionParameter("Oversampling factor", "1.5")
segmentationNode.GetSegmentation().SetConversionParameter("Joint smoothing", "0.00")
segmentationNode.GetSegmentation().SetConversionParameter("Smoothing factor", "0.00")
segmentationNode.GetSegmentation().SetConversionParameter("Decimation factor", "0.00")
segmentationNode.CreateClosedSurfaceRepresentation()

# Segment Editor Effect: Smoothing
segmentEditorWidget.setActiveEffectByName("Smoothing")
smoothingEffect = segmentEditorWidget.activeEffect()
# 2mm MEDIAN Smoothing
smoothingEffect.setParameter("SmoothingMethod", "MEDIAN")
smoothingEffect.self().onApply
smoothingEffect.setParameter("KernelSizeMm", 2)
smoothingEffect.self().onApply

# Update Closed Surface Representation
segmentationNode.GetSegmentation().SetConversionParameter("Oversampling factor", "1.5")
segmentationNode.GetSegmentation().SetConversionParameter("Joint smoothing", "1.00")
segmentationNode.GetSegmentation().SetConversionParameter("Smoothing factor", "1.00")
segmentationNode.GetSegmentation().SetConversionParameter("Decimation factor", "0.90")
# Update the smoothed closed surface representation some how</code></pre>

---

## Post #2 by @Queen_Rei (2020-06-11 15:49 UTC)

<p>Any advice helps &lt;3 Even a pointer to where to find out what functions could update the surface representation would come a long way!</p>

---

## Post #3 by @lassoan (2020-06-11 16:18 UTC)

<aside class="quote no-group" data-username="Queen_Rei" data-post="1" data-topic="11983">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/queen_rei/48/6348_2.png" class="avatar"> Queen_Rei:</div>
<blockquote>
<p>I want to smooth the representation that isn’t decimated. After smoothing, decimate it.</p>
</blockquote>
</aside>
<p>It looks like your code already does what you need. Whenever you change the binary labelmap representation (smoothing, etc.), the binary labelmap representation is re-converted to closed surface representation (including smoothing and decimation).</p>
<p>For final export, you can do additional combination of smoothing and decimation using VTK filters (in just a few lines of code, using vtkQuadricDecimation, vtkDecimatePro, vtkWindowedSincPolyDataFilter etc.). Decimate CLI module has an additional FastQuadric method that you may try, too.</p>

---
