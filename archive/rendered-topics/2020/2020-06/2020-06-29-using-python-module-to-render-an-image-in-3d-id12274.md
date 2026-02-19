---
topic_id: 12274
title: "Using Python Module To Render An Image In 3D"
date: 2020-06-29
url: https://discourse.slicer.org/t/12274
---

# Using Python Module to Render an Image in 3D

**Topic ID**: 12274
**Date**: 2020-06-29
**URL**: https://discourse.slicer.org/t/using-python-module-to-render-an-image-in-3d/12274

---

## Post #1 by @vertebrae (2020-06-29 16:19 UTC)

<p>Hello,</p>
<p>I am looking to use a 3D slicer python module to render thresholded spinal data in 3D and to potentially save as an STL file. Does anyone know how to do this?</p>

---

## Post #2 by @vertebra (2020-06-29 17:19 UTC)

<p>Hey! I would take a look at this repository. It has the code: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository</a></p>

---

## Post #3 by @lassoan (2020-06-29 18:03 UTC)

<p>More specifically, these examples show how to automatically segment structures, display it in 3D and save as STL file: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #4 by @vertebra (2020-06-29 19:42 UTC)

<p>One more question Andras!</p>
<p>Whenever I attempt to run my code with any slicer.util or other commands, it says slicer is not defined. Even though I have imported slicer.</p>
<p>What’s going on?</p>

---

## Post #5 by @vertebra (2020-06-29 19:45 UTC)

<p>One more question Andras. Also, do you have any sources for coding the keepLargestIsland function?</p>

---

## Post #6 by @lassoan (2020-06-29 19:51 UTC)

<aside class="quote no-group" data-username="vertebra" data-post="4" data-topic="12274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>Whenever I attempt to run my code with any slicer.util or other commands, it says slicer is not defined. Even though I have imported slicer.</p>
</blockquote>
</aside>
<p>How do you run your script?</p>

---

## Post #7 by @vertebra (2020-06-29 19:55 UTC)

<p>I have a module in 3D Slicer but the code is just written in IDLE. When running it from IDLE to print something, it says you have to import from slicer.</p>

---

## Post #8 by @vertebrae (2020-06-29 20:16 UTC)

<p>I also have the same question regarding the islands function.</p>

---

## Post #9 by @lassoan (2020-06-30 00:17 UTC)

<aside class="quote no-group" data-username="vertebrae" data-post="8" data-topic="12274" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/v/dec6dc/48.png" class="avatar"> vertebrae:</div>
<blockquote>
<p>I also have the same question regarding the islands function.</p>
</blockquote>
</aside>
<p>Entire source code of Slicer is open. Implementaitno of all built-in Segment editor effects are available here: <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Segmentations/EditorEffects" class="inline-onebox">Slicer/Modules/Loadable/Segmentations/EditorEffects at main · Slicer/Slicer · GitHub</a></p>
<aside class="quote no-group" data-username="vertebra" data-post="7" data-topic="12274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>When running it from IDLE to print something, it says you have to import from slicer.</p>
</blockquote>
</aside>
<p>You need to run Python scripts that use Slicer classes from Slicer’s Python environment.</p>

---

## Post #10 by @vertebra (2020-06-30 14:47 UTC)

<p>I’m running my python module through slicer. Even when I import slicer before the class, an error saying there is no module named slicer appears. What should I do about this?</p>
<p>Also, kind of a long shot… Do you have or could you create a completed python module for vertebra segmentation using flood fill, threshold, smoothing, and fiducial nodes selected by the user? That would be a great help especially if you have comments explaining each function.</p>

---

## Post #11 by @vertebra (2020-06-30 14:48 UTC)

<p>Thanks Andras once again for all the help!</p>

---

## Post #12 by @lassoan (2020-06-30 15:10 UTC)

<aside class="quote no-group" data-username="vertebra" data-post="10" data-topic="12274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>I’m running my python module through slicer. Even when I import slicer before the class, an error saying there is no module named slicer appears. What should I do about this?</p>
</blockquote>
</aside>
<p>I still don’t have a clear idea of what scripts you are trying to run where. Maybe you could record a screen capture video and share that, but probably it would be even better to follow steps described in Slicer programming tutorials, such as <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">this</a>.</p>
<aside class="quote no-group" data-username="vertebra" data-post="10" data-topic="12274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>Do you have or could you create a completed python module for vertebra segmentation using flood fill, threshold, smoothing, and fiducial nodes selected by the user? That would be a great help especially if you have comments explaining each function.</p>
</blockquote>
</aside>
<p>Slicer community members has been working a lot on vertebra segmentation, so we know quite a lot about potential approaches and capabilities and limitations of each.</p>
<p>There is no such thing as a perfect segmentation. The right solution depends on what is the clinical goal, expertise and time constraints of users, input image modality, quality, resolution, computational resources, amount of data sets, etc. If you can tell more about your project then we can give advice on potential approaches.</p>

---

## Post #13 by @vertebra (2020-06-30 15:46 UTC)

<p>So the general approach we have decided upon is:</p>
<ol>
<li>The user would mark a fiducial point on the lumbar vertebra</li>
<li>The code creates a segment naming it lumbar vertebra</li>
<li>The threshold segment editor is used to set it between (150, 400) to isolate the bone</li>
<li>The islands segment editor is used to keep the largest island</li>
<li>Around the fiducial point, the flood fill segment editor is used to encompass the singular lumbar vertebra</li>
<li>The smoothing/median segment editor is used to smooth the image</li>
<li>Render the image in 3D and save to an STL file</li>
</ol>
<p>We are open to any suggestions on how to improve the code or alter the algorithm</p>

---

## Post #14 by @lassoan (2020-06-30 17:43 UTC)

<aside class="quote no-group" data-username="vertebra" data-post="13" data-topic="12274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>The threshold segment editor is used to set it between (150, 400) to isolate the bone</p>
</blockquote>
</aside>
<p>Isolation of vertebrae is the most challenging problem. If you are so to have so high-quality, high-resolution images that you can separate a vertebra by simple thresholding then the whole segmentation process can be very easy (potentially easier than the steps you described). Do you segment human clinical CTs? What is the image resolution? Can you post a few screenshots?</p>
<p>The two main improvements that I would consider:</p>
<ul>
<li>use local thresholding effect (provided by SegmentEditorExtraEffect extension): it implements step 3-5 and it allows using GrowFromSeed or Watershed transforms for more robust connectivity computation</li>
<li>solidify the bone (fill in internal holes caused by lower density of cancellous bone) using Wrap Solidify effect (provided by SurfaceWrapSolidify extension), as it fill all holes without risk of leaking or missing some holes</li>
</ul>

---

## Post #15 by @vertebra (2020-06-30 17:46 UTC)

<p>I mean we have been experimenting on CT Chest and CT Cardio from the sample data. If we only use one segment, how would grow from seeds or watershed be implemented? We will definitely try the wrap solidify effect. And we will start experimenting with localized thresholding.</p>

---

## Post #16 by @vertebrae (2020-06-30 17:51 UTC)

<p>Hello Andras,</p>
<p>I cannot find the SurfaceWrapSolidify extension in the extension manager. How can I access this?</p>

---

## Post #17 by @lassoan (2020-06-30 17:59 UTC)

<aside class="quote no-group" data-username="vertebra" data-post="15" data-topic="12274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>If we only use one segment, how would grow from seeds or watershed be implemented?</p>
</blockquote>
</aside>
<p>For Grow from seeds and Watershed effects you always need to specify at least two segments. In case of vertebra segmentation, it would be a “bone” and “other” segment. Local thresholding effect automatically creates a temporary “other” segment from regions that have different intensity or they are disconnected.</p>
<aside class="quote no-group" data-username="vertebra" data-post="15" data-topic="12274">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>we have been experimenting on CT Chest and CT Cardio from the sample data</p>
</blockquote>
</aside>
<p>On these images, you cannot separate a single vertebra by simple thresholding (but of course, as I mentioned, there is no such things “perfect segmentation”, so maybe what you can get from these images is good enough).</p>
<p>Here is an example of what you can get with a single-click segmentation using Local thresholding effect on CTACardio example (threshold range of 265-1009, features size = 6mm, segmentation algorithm = growcut):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f078075bdf235078273b8370767492656ed7403.jpeg" data-download-href="/uploads/short-url/kpilKtio9NXlchs6r8Cb36z9RZ1.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f078075bdf235078273b8370767492656ed7403_2_690x416.jpeg" alt="image" data-base62-sha1="kpilKtio9NXlchs6r8Cb36z9RZ1" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f078075bdf235078273b8370767492656ed7403_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f078075bdf235078273b8370767492656ed7403.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f078075bdf235078273b8370767492656ed7403.jpeg 2x" data-dominant-color="676B7B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">991×598 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #18 by @vertebra (2020-06-30 18:26 UTC)

<p>Thank you so much! This helps astoundingly. The localized threshold will be implemented instead of steps 3-5. You’re the greatest!</p>

---

## Post #19 by @vertebra (2020-07-01 14:49 UTC)

<p>Hello! We are still beginners at the coding process in python. Of course, this doesn’t work yet. We compiled some of the codes from different resources on GitHub that we identified. Could you please give us some tips or edits? We don’t have the rendering in yet.</p>
<p>import os<br>
import vtk, qt, ctk, slicer<br>
import logging<br>
from SegmentEditorEffects import *<br>
import vtkITK<br>
import SimpleITK as sitk<br>
import sitkUtils<br>
import math<br>
import vtkSegmentationCorePython as vtkSegmentationCore<br>
import vtkSlicerSegmentationsModuleLogicPython as vtkSlicerSegmentationsModuleLogic<br>
import SampleData</p>
<p>class VertebraSegmentation()</p>
<h1>Load master volume</h1>
<p>sampleDataLogic = SampleData.SampleDataLogic()<br>
masterVolumeNode = sampleDataLogic.downloadCTACardio()</p>
<p>#<span class="hashtag">#gets</span> the node coordinates to run the grow cut from later<br>
hierarchy = slicer.vtkMMRLSubjectHierarchyNode(slicer.mmrlScene)<br>
sceneItemID = hierarchy.GetSceneItemID()<br>
subjectItemID = hierarchy.GetItemChildWithName(sceneItemID,‘Fiducial Nodes’)<br>
fidList = slicer.util.getNode(‘FiducialNodes’)</p>
<h1>Create segmentation</h1>
<p>segmentationNode = slicer.vtkMRMLSegmentationNode()<br>
slicer.mrmlScene.AddNode(segmentationNode)<br>
segmentationNode.CreateDefaultDisplayNodes() # only needed for display<br>
segmentationNode.name = ‘Lumbar’<br>
segmentationNode.SetReferenceImageGeometryParameterFromVolumeNode(masterVolumeNode)</p>
<h1>Create seed segment inside lumbar and name</h1>
<p>lumbarSeed = fidList[0]<br>
lumbarSeed.SetRadius(3)<br>
lumbarSeed.Update()<br>
segmentationNode.AddSegmentFromClosedSurfaceRepresentation(lumbarSeed.GetOutput(), “Lumbar Vertebra”, [1.0,0.0,0.0])</p>
<p>def <strong>init</strong>(self, scriptedEffect):<br>
SegmentEditorThresholdEffect.<strong>init</strong>(self, scriptedEffect)<br>
scriptedEffect.name = ‘Local Threshold’<br>
self.previewSteps = 4</p>
<p>def updateMRMLFromGUI(self): ## sets the parameters for local threshold - grow cut at 6mm for feature size and 265.00 to 1009.00 for threshold range<br>
SegmentEditorThresholdEffect.updateMRMLFromGUI(self)<br>
featureSizeMm = 6.000 #<span class="hashtag">#self</span>.minimumMinimumFeatureSize.value<br>
self.scriptedEffect.setParameter(MINIMUM_FEATURE_MM_PARAMETER_NAME, featureSizeMm)</p>
<pre><code>segmentationAlgorithm = "GrowCut" ##self.segmentationAlgorithmSelector.currentText
self.scriptedEffect.setParameter(SEGMENTATION_ALGORITHM_PARAMETER_NAME, segmentationAlgorithm)
</code></pre>
<p>def runGrowCut(self, masterImageData, seedLabelmap, outputLabelmap): ## runs the grow cut - local threshold on the segment</p>
<pre><code>self.clippedMaskImageData = slicer.vtkOrientedImageData()
intensityBasedMasking = self.scriptedEffect.parameterSetNode().GetMasterVolumeIntensityMask()
segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()
success = segmentationNode.GenerateEditMask(self.clippedMaskImageData,
  self.scriptedEffect.parameterSetNode().GetMaskMode(),
  masterImageData, # reference geometry
  "", # edited segment ID
  self.scriptedEffect.parameterSetNode().GetMaskSegmentID() if self.scriptedEffect.parameterSetNode().GetMaskSegmentID() else "",
  masterImageData if intensityBasedMasking else None,
  self.scriptedEffect.parameterSetNode().GetMasterVolumeIntensityMaskRange() if intensityBasedMasking else None)

import vtkSlicerSegmentationsModuleLogicPython as vtkSlicerSegmentationsModuleLogic
self.growCutFilter = vtkSlicerSegmentationsModuleLogic.vtkImageGrowCutSegment()
self.growCutFilter.SetIntensityVolume(masterImageData)
self.growCutFilter.SetSeedLabelVolume(seedLabelmap)
self.growCutFilter.SetMaskVolume(self.clippedMaskImageData)
self.growCutFilter.Update()
outputLabelmap.ShallowCopy(self.growCutFilter.GetOutput())
</code></pre>
<p>def apply(self, ijkPoints):<br>
kernelSizePixel = self.getKernelSizePixel()<br>
if kernelSizePixel[0]&lt;=0 and kernelSizePixel[1]&lt;=0 and kernelSizePixel[2]&lt;=0:<br>
return</p>
<pre><code>qt.QApplication.setOverrideCursor(qt.Qt.WaitCursor)

# Get parameter set node
parameterSetNode = self.scriptedEffect.parameterSetNode()

# Get parameters
minimumThreshold = self.scriptedEffect.doubleParameter("MinimumThreshold")
maximumThreshold = self.scriptedEffect.doubleParameter("MaximumThreshold")

# Get modifier labelmap
modifierLabelmap = self.scriptedEffect.defaultModifierLabelmap()

# Get master volume image data
masterImageData = self.scriptedEffect.masterVolumeImageData()

# Set intensity range
oldMasterVolumeIntensityMask = parameterSetNode.GetMasterVolumeIntensityMask()
parameterSetNode.MasterVolumeIntensityMaskOn()
oldIntensityMaskRange = parameterSetNode.GetMasterVolumeIntensityMaskRange()
intensityRange = [265.00, 1009.00]
if oldMasterVolumeIntensityMask:
  intensityRange = [max(oldIntensityMaskRange[0], minimumThreshold), min(oldIntensityMaskRange[1], maximumThreshold)]
parameterSetNode.SetMasterVolumeIntensityMaskRange(intensityRange)

roiNode = lumbarSeed ##self.roiSelector.currentNode()
clippedMasterImageData = masterImageData
if roiNode is not None:
  worldToImageMatrix = vtk.vtkMatrix4x4()
  masterImageData.GetWorldToImageMatrix(worldToImageMatrix)

  bounds = [0,0,0,0,0,0]
  roiNode.GetRASBounds(bounds)
  corner1RAS = [bounds[0], bounds[2], bounds[4], 1]
  corner1IJK = [0, 0, 0, 0]
  worldToImageMatrix.MultiplyPoint(corner1RAS, corner1IJK)

  corner2RAS = [bounds[1], bounds[3], bounds[5], 1]
  corner2IJK = [0, 0, 0, 0]
  worldToImageMatrix.MultiplyPoint(corner2RAS, corner2IJK)

  extent = [0, -1, 0, -1, 0, -1]
  for i in range(3):
      lowerPoint = min(corner1IJK[i], corner2IJK[i])
      upperPoint = max(corner1IJK[i], corner2IJK[i])
      extent[2*i] = int(math.floor(lowerPoint))
      extent[2*i+1] = int(math.ceil(upperPoint))

  imageToWorldMatrix = vtk.vtkMatrix4x4()
  masterImageData.GetImageToWorldMatrix(imageToWorldMatrix)
  clippedMasterImageData = slicer.vtkOrientedImageData()
  self.padder = vtk.vtkImageConstantPad()
  self.padder.SetInputData(masterImageData)
  self.padder.SetOutputWholeExtent(extent)
  self.padder.Update()
  clippedMasterImageData.ShallowCopy(self.padder.GetOutput())
  clippedMasterImageData.SetImageToWorldMatrix(imageToWorldMatrix)

# Pipeline
self.thresh = vtk.vtkImageThreshold()
self.thresh.SetInValue(LABEL_VALUE)
self.thresh.SetOutValue(BACKGROUND_VALUE)
self.thresh.SetInputData(clippedMasterImageData)
self.thresh.ThresholdBetween(minimumThreshold, maximumThreshold)
self.thresh.SetOutputScalarTypeToUnsignedChar()
self.thresh.Update()

self.erode = vtk.vtkImageDilateErode3D()
self.erode.SetInputConnection(self.thresh.GetOutputPort())
self.erode.SetDilateValue(BACKGROUND_VALUE)
self.erode.SetErodeValue(LABEL_VALUE)
self.erode.SetKernelSize(
  kernelSizePixel[0],
  kernelSizePixel[1],
  kernelSizePixel[2])

self.erodeCast = vtk.vtkImageCast()
self.erodeCast.SetInputConnection(self.erode.GetOutputPort())
self.erodeCast.SetOutputScalarTypeToUnsignedInt()
self.erodeCast.Update()

# Remove small islands
self.islandMath = vtkITK.vtkITKIslandMath()
self.islandMath.SetInputConnection(self.erodeCast.GetOutputPort())
self.islandMath.SetFullyConnected(False)
self.islandMath.SetMinimumSize(125)  # remove regions smaller than 5x5x5 voxels

self.islandThreshold = vtk.vtkImageThreshold()
self.islandThreshold.SetInputConnection(self.islandMath.GetOutputPort())
self.islandThreshold.ThresholdByLower(BACKGROUND_VALUE)
self.islandThreshold.SetInValue(BACKGROUND_VALUE)
self.islandThreshold.SetOutValue(LABEL_VALUE)
self.islandThreshold.SetOutputScalarTypeToUnsignedChar()
self.islandThreshold.Update()

# Points may be outside the region after it is eroded.
# Snap the points to LABEL_VALUE voxels,
snappedIJKPoints = self.snapIJKPointsToLabel(ijkPoints, self.islandThreshold.GetOutput())
if snappedIJKPoints.GetNumberOfPoints() == 0:
  qt.QApplication.restoreOverrideCursor()
  return

# Convert points to real data coordinates. Required for vtkImageThresholdConnectivity.
seedPoints = vtk.vtkPoints()
origin = masterImageData.GetOrigin()
spacing = masterImageData.GetSpacing()
for i in range(snappedIJKPoints.GetNumberOfPoints()):
  ijkPoint = snappedIJKPoints.GetPoint(i)
  seedPoints.InsertNextPoint(
    origin[0]+ijkPoint[0]*spacing[0],
    origin[1]+ijkPoint[1]*spacing[1],
    origin[2]+ijkPoint[2]*spacing[2])

segmentationAlgorithm = self.scriptedEffect.parameter(SEGMENTATION_ALGORITHM_PARAMETER_NAME)
if segmentationAlgorithm == SEGMENTATION_ALGORITHM_MASKING:
  self.runMasking(seedPoints, self.islandThreshold.GetOutput(), modifierLabelmap)

else:
  self.floodFillingFilterIsland = vtk.vtkImageThresholdConnectivity()
  self.floodFillingFilterIsland.SetInputConnection(self.islandThreshold.GetOutputPort())
  self.floodFillingFilterIsland.SetInValue(SELECTED_ISLAND_VALUE)
  self.floodFillingFilterIsland.ReplaceInOn()
  self.floodFillingFilterIsland.ReplaceOutOff()
  self.floodFillingFilterIsland.ThresholdBetween(LABEL_VALUE, LABEL_VALUE)
  self.floodFillingFilterIsland.SetSeedPoints(seedPoints)
  self.floodFillingFilterIsland.Update()

  self.maskCast = vtk.vtkImageCast()
  self.maskCast.SetInputData(self.thresh.GetOutput())
  self.maskCast.SetOutputScalarTypeToUnsignedChar()
  self.maskCast.Update()

  self.imageMask = vtk.vtkImageMask()
  self.imageMask.SetInputConnection(self.floodFillingFilterIsland.GetOutputPort())
  self.imageMask.SetMaskedOutputValue(OUTSIDE_THRESHOLD_VALUE)
  self.imageMask.SetMaskInputData(self.maskCast.GetOutput())
  self.imageMask.Update()

  imageMaskOutput = slicer.vtkOrientedImageData()
  imageMaskOutput.ShallowCopy(self.imageMask.GetOutput())
  imageMaskOutput.CopyDirections(clippedMasterImageData)

  imageToWorldMatrix = vtk.vtkMatrix4x4()
  imageMaskOutput.GetImageToWorldMatrix(imageToWorldMatrix)

  segmentOutputLabelmap = slicer.vtkOrientedImageData()
  if segmentationAlgorithm == SEGMENTATION_ALGORITHM_GROWCUT:
    self.runGrowCut(clippedMasterImageData, imageMaskOutput, segmentOutputLabelmap)
  elif segmentationAlgorithm == SEGMENTATION_ALGORITHM_WATERSHED:
    self.runWatershed(clippedMasterImageData, imageMaskOutput, segmentOutputLabelmap)
  else:
    logging.error("Unknown segmentation algorithm: \"" + segmentationAlgorithm + "\"")

  segmentOutputLabelmap.SetImageToWorldMatrix(imageToWorldMatrix)

  self.selectedSegmentThreshold = vtk.vtkImageThreshold()
  self.selectedSegmentThreshold.SetInputData(segmentOutputLabelmap)
  self.selectedSegmentThreshold.ThresholdBetween(SELECTED_ISLAND_VALUE, SELECTED_ISLAND_VALUE)
  self.selectedSegmentThreshold.SetInValue(LABEL_VALUE)
  self.selectedSegmentThreshold.SetOutValue(BACKGROUND_VALUE)
  self.selectedSegmentThreshold.SetOutputScalarType(modifierLabelmap.GetScalarType())
  self.selectedSegmentThreshold.Update()
  modifierLabelmap.ShallowCopy(self.selectedSegmentThreshold.GetOutput())

self.scriptedEffect.saveStateForUndo()
self.scriptedEffect.modifySelectedSegmentByLabelmap(modifierLabelmap, slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeAdd)

parameterSetNode.SetMasterVolumeIntensityMask(oldMasterVolumeIntensityMask)
parameterSetNode.SetMasterVolumeIntensityMaskRange(oldIntensityMaskRange)

qt.QApplication.restoreOverrideCursor()</code></pre>

---

## Post #20 by @lassoan (2020-07-01 14:52 UTC)

<p>This code is way too long to be discussed here. If you need feedback, then create an extension using Extension Wizard module, upload it to github and just post links here. Give a high-level overview of what you are trying to achieve and ask specific questions related to specific parts of the code.</p>

---

## Post #22 by @vertebrae (2020-07-01 15:57 UTC)

<p>Here is the link to the GitHub Page:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="16" height="16">
      <a href="https://github.com/kbehlmirusmed/VertebraSegmentation" target="_blank" rel="nofollow noopener">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/67699725?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/kbehlmirusmed/VertebraSegmentation" target="_blank" rel="nofollow noopener">kbehlmirusmed/VertebraSegmentation</a></h3>

<p>Contribute to kbehlmirusmed/VertebraSegmentation development by creating an account on GitHub.</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>We are open to any suggestions. We are trying to use a pre-placed seed point and use the local threshold function to segment individual lumbar vertebrae, render it in 3D, and save it as an stl file. Thank you for all of your help.</p>

---
