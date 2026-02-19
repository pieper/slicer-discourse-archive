---
topic_id: 19902
title: "Auto General Reg Elastix With Python Interface"
date: 2021-09-28
url: https://discourse.slicer.org/t/19902
---

# Auto General Reg (Elastix) with python interface

**Topic ID**: 19902
**Date**: 2021-09-28
**URL**: https://discourse.slicer.org/t/auto-general-reg-elastix-with-python-interface/19902

---

## Post #1 by @Dhruba (2021-09-28 20:01 UTC)

<p>**Hi, I want to register all my CTP images to MNI space using General Reg. (Elastix). But I have over thousands images and don’t want to do all the images manually. Can I write a python code to register all my images using a loop. **<br>
<strong>Previously I did the same for skull stripping using the following code:</strong></p>
<p>def skull_stripping():<br>
import vtkITK<br>
<span class="hashtag">#masterVolumeNode</span> = slicer.util.loadVolume(‘E:/asdgdrhss/8 CTA_1_0__H20f_5.nrrd’)<br>
for _ in range (1200):<br>
masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass(“vtkMRMLScalarVolumeNode”)<br>
threshold = 500<br>
split_cavities = 30</p>
<pre><code>    thresholdCalculator = vtkITK.vtkITKImageThresholdCalculator()
    thresholdCalculator.SetInputData(masterVolumeNode.GetImageData())
    thresholdCalculator.SetMethodToOtsu()
    thresholdCalculator.Update()
    boneThresholdValue = thresholdCalculator.GetThreshold()
    volumeScalarRange = masterVolumeNode.GetImageData().GetScalarRange()
    logging.info("Volume minimum = {0}, maximum = {1}, bone threshold = {2}".format(volumeScalarRange[0], volumeScalarRange[1], boneThresholdValue))
    slicer.app.processEvents()

    # Create segmentation
    slicer.app.processEvents()
    segmentationNode = slicer.vtkMRMLSegmentationNode()
    slicer.mrmlScene.AddNode(segmentationNode)
    segmentationNode.CreateDefaultDisplayNodes() # only needed for display
    segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

    # Create segment editor to get access to effects
    slicer.app.processEvents()
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    # To show segment editor widget (useful for debugging): segmentEditorWidget.show()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    if not segmentEditorWidget.effectByName("Wrap Solidify"):
        slicer.util.errorDisplay("Please install 'SurfaceWrapSolidify' extension using Extension Manager.")

    segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()
    slicer.mrmlScene.AddNode(segmentEditorNode)
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(segmentationNode)
    segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)

    # Create bone segment by thresholding
    slicer.app.processEvents()
    boneSegmentID = segmentationNode.GetSegmentation().AddEmptySegment("bone")
    segmentEditorNode.SetSelectedSegmentID(boneSegmentID)
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold",str(threshold))#change if needed
    effect.setParameter("MaximumThreshold",str(volumeScalarRange[1]))
    effect.self().onApply()

    # Find largest object, remove all other regions from the segment
    slicer.app.processEvents()
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameterDefault("Operation", "KEEP_LARGEST_ISLAND")
    effect.self().onApply()

    # Create Margin
#     slicer.app.processEvents()
#     segmentEditorWidget.setActiveEffectByName("Margin")
#     effect = segmentEditorWidget.activeEffect()
#     effect.setParameterDefault("Operation", "Grow")
#     effect.setParameter('Margin_Size', 1)
#     effect.self().onApply()



    # Fill holes in the segment to create a solid region of interest
    slicer.app.processEvents()
    segmentEditorWidget.setActiveEffectByName("Wrap Solidify")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("region", "largestCavity")
    effect.setParameter("splitCavities", str(split_cavities))
    effect.setParameter("outputType", "segment")
    #effect.setParameter("smoothingFactor", 0.2)  # speed up solidification by lowering resolution
    #effect.setParameter("remeshOversampling", 1.5)  # speed up solidification by lowering resolution
    #effect.setParameter("numberOfIterations", 6)  # speed up solidification by lowering resolution
    effect.self().onApply()



    # Blank out the volume outside the object segment
    slicer.app.processEvents()
    segmentEditorWidget.setActiveEffectByName('Mask volume')
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter('FillValue', -1000)
    effect.setParameter('Operation', 'FILL_OUTSIDE')
    effect.self().onApply()

    # Remove temporary nodes and widget
    segmentEditorWidget = None
    slicer.mrmlScene.RemoveNode(segmentEditorNode)
    slicer.mrmlScene.RemoveNode(segmentationNode)
    slicer.mrmlScene.RemoveNode(masterVolumeNode)

    # Show masked volume
    maskedVolume = slicer.mrmlScene.GetFirstNodeByName(masterVolumeNode.GetName()+" masked")
    slicer.util.setSliceViewerLayers(background=maskedVolume)
</code></pre>
<p>shortcuts = [(“s”, lambda: skull_stripping())]<br>
for (shortcutKey, callback) in shortcuts:<br>
shortcut = qt.QShortcut(slicer.util.mainWindow())<br>
shortcut.setKey(qt.QKeySequence(shortcutKey))<br>
shortcut.connect( “activated()”, callback)</p>
<p><strong>I need some help with the code for doing the same thing for registration.</strong></p>

---
