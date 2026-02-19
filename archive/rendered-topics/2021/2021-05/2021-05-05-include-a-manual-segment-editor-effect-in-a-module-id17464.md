---
topic_id: 17464
title: "Include A Manual Segment Editor Effect In A Module"
date: 2021-05-05
url: https://discourse.slicer.org/t/17464
---

# Include a manual Segment Editor effect in a module

**Topic ID**: 17464
**Date**: 2021-05-05
**URL**: https://discourse.slicer.org/t/include-a-manual-segment-editor-effect-in-a-module/17464

---

## Post #1 by @Guglielmo_Baccani (2021-05-05 11:23 UTC)

<p>I’m building a semi-automatic segmentation module by combining some effects from the Segment Editor. Simplifying the problem, in my module I would like to use the following effects in sequence: Threshold, Scissors (which requires manual user interaction) and Islands. During the Scissors effect, after setting some parameters, I would like to use the shortcut of the space bar of the Segment Editor to switch between the Scissors effect and None so that I can more easily rotate the segmentation in the 3d view.</p>
<p>This is the simplified version of the process function of the Logic class (called from the onApplyButton function):</p>
<pre><code class="lang-auto">  def process(self, inputVolume, outputSegmentationNode):

    segmentation = outputSegmentationNode.GetSegmentation()
    outputSegmentationNode.CreateDefaultDisplayNodes() # only needed for display
    outputSegmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(inputVolume)

    # Create segment editor to get access to effects
    segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
    segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
    segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
    segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget.setSegmentationNode(outputSegmentationNode)
    segmentEditorWidget.setMasterVolumeNode(inputVolume)

    # Create RoiSegment
    RoiSegmentID = segmentation.AddEmptySegment("ROI")
    segmentEditorNode.SetSelectedSegmentID(RoiSegmentID)

    # Threshold
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MaximumThreshold","-250")
    effect.setParameter("MinimumThreshold","-950")
    effect.self().onApply()

    # Scissor
    slicer.util.selectModule('SegmentEditor')
    segmentEditorWidget2 = slicer.modules.SegmentEditorWidget.editor
    segmentEditorWidget2.setMRMLSegmentEditorNode(segmentEditorNode)
    segmentEditorWidget2.setActiveEffectByName('Scissors')
    effect = segmentEditorWidget2.activeEffect()
    effect.setParameter("Operation","EraseOutside")

    outputSegmentationNode.CreateClosedSurfaceRepresentation()

    try:
      input("Select the ROI from the 3d view, then press Enter to continue...")
    except EOFError:
      pass

    outputSegmentationNode.RemoveClosedSurfaceRepresentation()

    # Keep largest island
    segmentEditorWidget.setActiveEffectByName("Islands")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("Operation","KEEP_LARGEST_ISLAND")
    effect.self().onApply()

    # Delete temporary segment editor
    segmentEditorWidget = None
    segmentEditorWidget2 = None
    slicer.mrmlScene.RemoveNode(segmentEditorNode)</code></pre>
<p>Once the module is finished running, after switching to the Segment Editor module, the spacebar shortcut no longer works and this leads me to think that I have made some mistake in the code. I guess I got confused with the two segmentEditorWidgets (of which I don’t understand the difference).<br>
What is the best way to do the above?</p>

---

## Post #2 by @lassoan (2021-05-21 18:33 UTC)

<p>You need to call <code>self.editor.installKeyboardShortcuts()</code> / <code>self.editor.uninstallKeyboardShortcuts()</code> to enable/disable keyboard shortcuts.</p>

---
