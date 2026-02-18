# Masking settings from a script on a segment editor effect in python

**Topic ID**: 14323
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/masking-settings-from-a-script-on-a-segment-editor-effect-in-python/14323

---

## Post #1 by @rbumm (2020-10-30 09:16 UTC)

<p>Hi,</p>
<p>I am stuck with this for several days now.</p>
<p>Would like to evaluate regions in a CT via a python script.<br>
Created a module, works ok.</p>
<p>Four regions should be evaluated in my script, which principally works due to the excellent source code example of Andras Lasso, but if I try to mask this work by using a “Right lung mask” or a “Left lung mask” (which I have priorly segmented and which are stored under “Segmentation”), the threshold algorithm is always using the complete data set and does not work within the mask.</p>
<p>Here is the relevant part I added for the right lung (the right lung mask is the first one stored under “Segmentation”).</p>
<code>
segmentationNode2 = slicer.util.getNode('Segmentation')
        segmentEditorNode.SetMaskSegmentID(segmentationNode2.GetSegmentation().GetNthSegmentID(0))
        segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)
        segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedInsideSingleSegment)
</code>
<p>Here is the complete source:</p>
<code>
<p>def process(self, inputVolume):</p>
<pre><code>if not inputVolume:
  raise ValueError("Input volume is invalid")

import time
startTime = time.time()
logging.info('Processing started')

# Compute 
masterVolumeNode = inputVolume
# Create segmentation
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)
#segmentationNode2 = slicer.util.getNode('Segmentation')
#slicer.util.messageBox("Seg Node:" + segmentationNode2.GetSegmentation().GetNthSegmentID(0), dontShowAgainSettingsKey = "MainWindow/DontShowSomeMessage")

# Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)  

# Create segments by thresholding
segmentsFromHounsfieldUnits = [
    ["Emphysema right", -1000, -900],
    ["Ventilated right", -900, -600],
    ["Infiltration right", -600, -50],
    ["Collapsed right", -50, 3000] ]
for segmentName, thresholdMin, thresholdMax in segmentsFromHounsfieldUnits:
    # Create segment
    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)
    segmentEditorNode.SetSelectedSegmentID(addedSegmentID) 
    # slicer.util.messageBox("Some message", dontShowAgainSettingsKey = "MainWindow/DontShowSomeMessage")
    segmentationNode2 = slicer.util.getNode('Segmentation')
    segmentEditorNode.SetMaskSegmentID(segmentationNode2.GetSegmentation().GetNthSegmentID(0))
    segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteNone)
    segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedInsideSingleSegment)
    # Fill by thresholding
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold",str(thresholdMin))
    effect.setParameter("MaximumThreshold",str(thresholdMax))        
    effect.self().onApply()

# Delete temporary segment editor
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

# Compute segment volumes
resultsTableNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTableNode')
import SegmentStatistics
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
segStatLogic.getParameterNode().SetParameter("ScalarVolume", masterVolumeNode.GetID())
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.enabled","True")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.voxel_count.enabled","False")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.volume_mm3.enabled","False")
segStatLogic.computeStatistics()
segStatLogic.exportToTable(resultsTableNode)
segStatLogic.showTable(resultsTableNode)

# Export segmentation to a labelmap
#labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
#slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, masterVolumeNode)
#slicer.util.saveNode(labelmapVolumeNode, "c:/tmp/BodyComposition-label.nrrd")
stopTime = time.time()
logging.info('Processing completed in {0:.2f} seconds'.format(stopTime-startTime))
</code></pre>
</code>
<p>Thank you for any help.<br>
Best regards<br>
rudolf</p>

---

## Post #2 by @lassoan (2020-10-30 12:40 UTC)

<p>You can only edit one segmentation node at a time, so you cannot use mask segment from SegmentationNodeA while editing SegmentationNodeB.</p>
<p>Probably the easiest is to not create a new segmentation node but just add new segments to `segmentationNode2’.</p>

---

## Post #3 by @rbumm (2020-10-30 17:00 UTC)

<p>I resolved this in part by using a masked volume (lung only) as the starting volume.</p>
<p>Also thought about better adding segmentations to an existing node, but for some reason</p>
<pre><code>segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
</code></pre>
<p>worked without error message, but the subsequent</p>
<pre><code>   effect.self().onApply()
</code></pre>
<p>hangs forever …</p>
<p>Thanks anyway, I am a big slicer fan <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #4 by @lassoan (2020-10-30 23:09 UTC)

<p>Thanks for the update. If you can provide a short script that reproduces the hang then we can investigate.</p>

---

## Post #5 by @rbumm (2020-10-31 08:42 UTC)

<p>I tried to reproduce the hang, but its gone. Thank you.</p>
<p>However, I still can not figure out why threshold is not working together with the masking effect in the code above …</p>

---

## Post #6 by @lassoan (2020-10-31 14:55 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="5" data-topic="14323">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>However, I still can not figure out why threshold is not working together with the masking effect in the code above …</p>
</blockquote>
</aside>
<p>The problem with the script above was that you tried to use mask segment from another segmentation node. The mask segment must be in the currently edited segmentation node.</p>

---

## Post #7 by @rbumm (2020-10-31 16:00 UTC)

<p>Probably true for the code above, but even if I change (your code)</p>
<p>segmentationNode = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLSegmentationNode”)</p>
<p>to</p>
<p>segmentationNode = slicer.util.getNode(‘Segmentation’)</p>
<p>Two segmentations (right lung mask, left lung mask) are defined in “Segmentation”  beforehand …<br>
I do get the new segmentations in the same node now, but do not get a masked output from “Theshold”</p>
<p>Would really like to make that work.<br>
Here is the adopted code:<br>
<code><br>
def process(self, inputVolume, showResult=True):<br>
“”"<br>
Run the processing algorithm.<br>
Can be used without GUI widget.<br>
:param inputVolume: volume to be thresholded<br>
“”"</code></p><code>
<pre><code>if not inputVolume:
  raise ValueError("Input volume is invalid")

import time
startTime = time.time()
logging.info('Processing started')

# Compute 
masterVolumeNode = inputVolume
# Create segmentation
#segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
#segmentationNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSegmentationNode")
segmentationNode = slicer.util.getNode('Segmentation')
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)

# Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")

# Do masking
segmentEditorNode.SetMaskSegmentID(segmentationNode.GetSegmentation().GetNthSegmentID(0))
segmentEditorNode.SetOverwriteMode(slicer.vtkMRMLSegmentEditorNode.OverwriteAllSegments)
segmentEditorNode.SetMaskMode(slicer.vtkMRMLSegmentEditorNode.PaintAllowedInsideSingleSegment)

segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)  
segmentationDisplayNode=segmentationNode.GetDisplayNode()
segmentation=segmentationNode.GetSegmentation()

# Create segments by thresholding
segmentsFromHounsfieldUnits = [
    ["Emphysema right", -1000, -900,0.0,0.0,0.0],
    ["Ventilated right", -900, -600,0,0.5,1.0],
    ["Infiltration right", -600, -50,1.0,0.5,0],
    ["Collapsed right", -50, 3000,1.0,0,1.0] ]
for segmentName, thresholdMin, thresholdMax, r, g, b in segmentsFromHounsfieldUnits:
    # Create segment
    logging.info('Creating segment.')
    addedSegmentID = segmentationNode.GetSegmentation().AddEmptySegment(segmentName)
    segmentEditorNode.SetSelectedSegmentID(addedSegmentID)
    # Set color
    logging.info('Setting segment color.')
    segmentId = segmentation.GetSegmentIdBySegmentName(segmentName)
    segmentationDisplayNode.SetSegmentOpacity3D(segmentId,0.2)
    segmentation.GetSegment(segmentId).SetColor(r,g,b)  # color should be set in segmentation node
    # Fill by thresholding
    logging.info('Thresholding.')
    segmentEditorWidget.setActiveEffectByName("Threshold")
    effect = segmentEditorWidget.activeEffect()
    effect.setParameter("MinimumThreshold",str(thresholdMin))
    effect.setParameter("MaximumThreshold",str(thresholdMax))        
    effect.self().onApply()



# Change overall segmentation display properties
# segmentationDisplayNode.SetOpacity3D(0.5)


# Delete temporary segment editor
segmentEditorWidget = None
slicer.mrmlScene.RemoveNode(segmentEditorNode)

logging.info('Creating statistics.')
# Compute segment volumes
resultsTableNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTableNode')
import SegmentStatistics
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
segStatLogic.getParameterNode().SetParameter("ScalarVolume", masterVolumeNode.GetID())
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.enabled","True")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.voxel_count.enabled","False")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.volume_mm3.enabled","False")
segStatLogic.computeStatistics()
segStatLogic.exportToTable(resultsTableNode)
segStatLogic.showTable(resultsTableNode)

# Export segmentation to a labelmap
#labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
#slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, masterVolumeNode)
#slicer.util.saveNode(labelmapVolumeNode, "c:/tmp/BodyComposition-label.nrrd")
stopTime = time.time()
logging.info('Processing completed in {0:.2f} seconds'.format(stopTime-startTime))
</code></pre>
<h1></h1>
<h1>CTLungAnalyzerTest</h1>
<h1></h1>
</code>

---
