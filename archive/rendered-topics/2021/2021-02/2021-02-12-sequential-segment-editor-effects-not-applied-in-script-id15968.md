# Sequential Segment Editor Effects not applied in script

**Topic ID**: 15968
**Date**: 2021-02-12
**URL**: https://discourse.slicer.org/t/sequential-segment-editor-effects-not-applied-in-script/15968

---

## Post #1 by @Pete (2021-02-12 13:41 UTC)

<p>Hi,</p>
<p>I have written a script to apply thresholds to a segment and then to apply median smoothing. Both these actions work exactly as expected separately, but when chained together in the script only the first (thresholding) is applied. Anyone able to help with this?</p>
<pre><code># Create new segments in Segmentation
segmentationNode = getNode('Segmentation')

SingleSegment = segmentationNode.GetSegmentation().AddEmptySegment('Single')
MultiSegment = segmentationNode.GetSegmentation().AddEmptySegment('Multi')

# OPTIONAL -- Set masterVolumeNode to first volume node
masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')

segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# OPTIONAL -- Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

# OPTIONAL -- Create segments by thresholding
### This will show available effects and parameters: print(slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentEditorNode"))
segmentsFromHounsfieldUnits = [
    ["Mask", -200, -50] ]
for segmentName, thresholdMin, thresholdMax in segmentsFromHounsfieldUnits:
    # Create segment
    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)
    segmentEditorNode.SetSelectedSegmentID(addedSegmentID)
    # Fill by thresholding
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold",str(thresholdMin))
    effect.setParameter("MaximumThreshold",str(thresholdMax))
    effect.self().onApply()



# OPTIONAL -- Apply smoothing to threshold mask
smoothSegments = [
    ["Mask"] ]
maskSmoothID = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName("Mask")
    
for smoothSegment in smoothSegments:
    segmentEditorNode.SetSelectedSegmentID(maskSmoothID)
    segmentEditorWidget.setActiveEffectByName("Smoothing")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("KernelSizeMm",3)
    effect.self().onApply()
    
# OPTIONAL -- Delete temporary segment editor
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)</code></pre>

---

## Post #2 by @lassoan (2021-02-12 14:52 UTC)

<p>The script works well for me.</p>
<p>The only suspicious thing is in your second <code>for</code> loop. You either don’t need this loop (and just use <code>maskSmoothID</code>) or you need to change the <code>for</code> loop to use <code>smoothSegment</code>.</p>

---
