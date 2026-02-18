# Problem setting output node for the mask volume effect in python

**Topic ID**: 30858
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/problem-setting-output-node-for-the-mask-volume-effect-in-python/30858

---

## Post #1 by @Anthony.Lombardi (2023-07-28 15:03 UTC)

<p>Hi all,</p>
<p>I am trying to set the output volume node from the <code>Mask Volume</code> effect in Python. However, I am not having much luck trying to do this. I am just using the default parameters for the <code>Mask Volume</code> effect as they were described in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#mask-volume" rel="noopener nofollow ugc">documentation</a>. However, the <code>Mask volume.OutputVolume</code> parameter fails to put the results into the provided volume node and instead, a new volume node <code>{inputvolname} masked</code> is created with the results. I have tried passing the volume node ID and the volume node itself but both failed to populate the passed node.</p>
<p>I am not sure what I need to be doing differently to get this to work, so any guidance would be extremely appreciated.</p>
<p>Below is an example showing off the issue I am running into:</p>
<pre><code class="lang-python">import slicer
import SampleData

# Load in some sample data
sampleDataLogic = SampleData.SampleDataLogic()
mrHead = sampleDataLogic.downloadMRHead()

# Create the segmentation node
segmentationNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
segmentationNode.CreateDefaultDisplayNodes() # only needed for display
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(mrHead)
segmentationNode.GetSegmentation().AddEmptySegment("Segment_1")

# Create temporary segment editor to get access to effects
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)
segmentEditorNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentEditorNode")
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)
segmentEditorWidget.setSegmentationNode(segmentationNode)
segmentEditorWidget.setSourceVolumeNode(mrHead)

# Apply a threshold to get the mask
segmentEditorWidget.setActiveEffectByName("Threshold")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("MinimumThreshold","70")
effect.setParameter("MaximumThreshold","280")
effect.self().onApply()

# Create a new volume to hold the mask
nodeName = "MyNewVolume"
imageSize = [512, 512, 512]
voxelType=vtk.VTK_UNSIGNED_CHAR
imageOrigin = [0.0, 0.0, 0.0]
imageSpacing = [1.0, 1.0, 1.0]
imageDirections = [[1,0,0], [0,1,0], [0,0,1]]
fillVoxelValue = 0
# Create an empty image volume, filled with fillVoxelValue
imageData = vtk.vtkImageData()
imageData.SetDimensions(imageSize)
imageData.AllocateScalars(voxelType, 1)
imageData.GetPointData().GetScalars().Fill(fillVoxelValue)
# Create volume node
volumeNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", nodeName)
volumeNode.SetOrigin(imageOrigin)
volumeNode.SetSpacing(imageSpacing)
volumeNode.SetIJKToRASDirections(imageDirections)
volumeNode.SetAndObserveImageData(imageData)
volumeNode.CreateDefaultDisplayNodes()
volumeNode.CreateDefaultStorageNode()

# Apply the mask effect
segmentEditorWidget.setActiveEffectByName("Mask volume")
effect = segmentEditorWidget.activeEffect()
effect.setParameter("Mask volume.InputVolume",mrHead.GetID()) # Input volume
effect.setParameter("Mask volume.OutputVolume",volumeNode.GetID()) # Expected result to be stored here, but it is not
effect.self().onApply()
</code></pre>

---

## Post #2 by @lassoan (2023-07-28 21:31 UTC)

<p>Setting of <code>noderef</code> parameter types was not described in the documentation. I’ve added it now: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/segmenteditor.html#effect-parameters" class="inline-onebox">Segment editor — 3D Slicer documentation</a></p>
<p>Something like this should work:</p>
<pre><code class="lang-python">inputVolume = effect.parameterSetNode().SetNodeReferenceID("Mask volume.InputVolume", mrHead.GetID)
</code></pre>

---

## Post #3 by @Anthony.Lombardi (2023-07-28 22:53 UTC)

<p>Awesome, thank you so much this worked!</p>
<p>For those interested the working snippet for the mask effect is as follows:</p>
<pre><code class="lang-python"># Apply the mask effect
segmentEditorWidget.setActiveEffectByName("Mask volume")
effect = segmentEditorWidget.activeEffect()
inputVolume = effect.parameterSetNode().SetNodeReferenceID("Mask volume.InputVolume", mrHead.GetID())
effect.self().onApply()
outputVolumeID = effect.parameterSetNode().GetNodeReferenceID("Mask volume.OutputVolume")
outputVolume = slicer.mrmlScene.GetNodeByID(outputVolumeID)
</code></pre>

---
