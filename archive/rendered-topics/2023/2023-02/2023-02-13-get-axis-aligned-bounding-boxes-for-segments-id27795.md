---
topic_id: 27795
title: "Get Axis Aligned Bounding Boxes For Segments"
date: 2023-02-13
url: https://discourse.slicer.org/t/27795
---

# Get axis-aligned bounding boxes for segments

**Topic ID**: 27795
**Date**: 2023-02-13
**URL**: https://discourse.slicer.org/t/get-axis-aligned-bounding-boxes-for-segments/27795

---

## Post #1 by @Caetox (2023-02-13 14:47 UTC)

<p>I created a segmentation with some segments and want to get an axis-aligned bounding box for each segment. As far as i know, with the segment statistics module we can compute oriented bounding boxes, but i couldn’t find an option to get axis-aligned bounding boxes. I tried to get the segments as numpy arrays and use numpy functions to find the required values as suggested <a href="https://discourse.slicer.org/t/python-script-to-get-axis-aligned-bounding-box/26227/5">here</a>. But since i rotated the segments before, the segments do not match with the original scalar volume anymore. Do I need to rotate and resample the volume as well? Or is there another way to get axis-aligned bounding boxes for segments?</p>

---

## Post #2 by @cpinter (2023-02-13 15:42 UTC)

<p>There is the <code>SegmentAxisAlignment</code> module in this extension:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/EBATINCA/SlicerSpine">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/EBATINCA/SlicerSpine" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/f1c63eb6af44ee26cbafa593549f13824acd1f36704582bab5482b55de4183d6/EBATINCA/SlicerSpine" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/EBATINCA/SlicerSpine" target="_blank" rel="noopener">GitHub - EBATINCA/SlicerSpine: 3D Slicer extension for spine research</a></h3>

  <p>3D Slicer extension for spine research. Contribute to EBATINCA/SlicerSpine development by creating an account on GitHub.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The extension is not yet added to the Extension Manager so for now you can clone this repository and point to the module in Edit / Application Settings / Additional module directories.</p>

---

## Post #4 by @hk_y (2024-08-11 02:42 UTC)

<p>Dear professor, I downloaded a zip file from GitHub to my local machine and then dragged the folder into “Additional module paths,” but the module still doesn’t appear. Did I understand “clone” correctly? Where should the folder be downloaded to?</p>

---

## Post #5 by @cpinter (2024-08-12 10:06 UTC)

<p>The folder you need to drag&amp;drop to Additional module paths is that of the module<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/4/c49aad4c6cac6fe08a28a9db9d60f19e86062c8a.png" alt="image" data-base62-sha1="s3eYDAbljzJ4MYvsHiapyNEIod4" width="638" height="251"></p>

---

## Post #6 by @hk_y (2024-08-12 15:53 UTC)

<p>Thank you very much! I successfully added the module. Can this module measure the length, width, and height of the  axis-aligned bounding box (AABB)?</p>

---

## Post #7 by @cpinter (2024-08-13 09:12 UTC)

<p>Sadly, no. But here is a function that does it using the above module</p>
<pre><code class="lang-auto">def computeAlignedROIForSegment(self, volumeNode, segmentationNode, segmentId, initialAngleLR = 0, initialAnglePA = 0):
  # Use SegmentAxisAlignment module
  saaw = slicer.modules.segmentaxisalignment.widgetRepresentation().self()
  saaw.initializeParameterNode()

  # Get segment name
  segmentName = segmentationNode.GetSegmentation().GetSegment(segmentId).GetName()

  # Create output ROI node
  roi = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsROINode')
  roi.SetName(segmentName + '_ROI')

  # Create output aligned volume node
  if volumeNode:
    alignedVolume = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLScalarVolumeNode')
    alignedVolume.SetName(volumeNode.GetName() + '_' + segmentName)
  else:
    alignedVolume = None

  # Create temporary nodes to store intermediate results
  alignmentTransform = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLinearTransformNode')
  outputSegmentation = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')

  # Set parameters for segment alignment
  saaw._parameterNode.SetNodeReferenceID("InputSegmentationNode", segmentationNode.GetID())
  saaw._parameterNode.SetParameter("InitialAlignmentAngleLR", str(initialAngleLR))
  saaw._parameterNode.SetParameter("InitialAlignmentAnglePA", str(initialAnglePA))
  saaw._parameterNode.SetParameter("InputSegmentID", segmentId)
  saaw._parameterNode.SetNodeReferenceID("OutputTransform", alignmentTransform.GetID())
  saaw._parameterNode.SetNodeReferenceID("OutputSegmentationNode", outputSegmentation.GetID())

  # Set parameters for volume alignment
  if volumeNode:
    saaw._parameterNode.SetNodeReferenceID("InputVolume", volumeNode.GetID())
    saaw._parameterNode.SetNodeReferenceID("OutputVolume", alignedVolume.GetID())

  # Calculate alignment
  saaw.onCalculateButtonClicked()

  # Get alignment angles
  angleLR = float(saaw._parameterNode.GetParameter("OutputAlignmentAngleLR"))
  anglePA = float(saaw._parameterNode.GetParameter("OutputAlignmentAnglePA"))
  print('Computed alignment angles for segment = ', segmentId)
  print('   - Alignment angle LR = ', angleLR)
  print('   - Alignment angle PA = ', anglePA)

  # Get aligned volume
  if volumeNode:
    saaw.onAlignVolumeButtonClicked()

  # Get output segmentation polydata
  outputSegmentation.HardenTransform() # harden alignment transform
  outputSegmentation.CreateClosedSurfaceRepresentation()
  outputSegmentIds = outputSegmentation.GetSegmentation().GetSegmentIDs()
  outputSegmentPolyData = outputSegmentation.GetClosedSurfaceInternalRepresentation(outputSegmentIds[0])

  # Get bounding box for segment
  bounds = outputSegmentPolyData.GetBounds()
  roiCenter = [(bounds[0]+bounds[1])/2, (bounds[2]+bounds[3])/2, (bounds[4]+bounds[5])/2]
  roiSize = [abs(bounds[1]-bounds[0]), abs(bounds[3]-bounds[2]), abs(bounds[5]-bounds[4])]
  roi.SetCenterWorld(roiCenter)
  roi.SetSizeWorld(roiSize)
  roi.SetLocked(True)
  roi.GetDisplayNode().SetGlyphScale(0) # hide control point in the roi center
  roi.GetDisplayNode().SetSelectedColor([1,1,0]) # yellow
  roi.GetDisplayNode().SetFillOpacity(0.0)
  roi.GetDisplayNode().SetHandlesInteractive(False)
  roi.GetDisplayNode().SetPropertiesLabelVisibility(False)

  # Apply inverse transform to align bounding boxes to original segments
  alignmentTransform.Inverse()
  roi.SetAndObserveTransformNodeID(alignmentTransform.GetID())
  roi.HardenTransform()

  # Delete temporary nodes
  slicer.mrmlScene.RemoveNode(outputSegmentation)
  slicer.mrmlScene.RemoveNode(alignmentTransform)

  return [roi, alignedVolume, angleLR, anglePA]
</code></pre>
<p>You can decide if you run the module and then only some lines from this function to get the ROI, or try to use the function, which executes the module and creates the ROI node too. If you have trouble figuring out how to use this let me know.</p>

---

## Post #8 by @hk_y (2024-08-14 02:40 UTC)

<p>I think I need to paste it into the Python Interactor in 3D Slicer? Do I need to open my file in Slicer first before pasting this code? However, it seems to not work.</p>

---

## Post #9 by @lassoan (2024-08-15 13:26 UTC)

<p>You need to edit the code a bit to tailor to your needs and then copy-paste into the Python console.</p>
<p>To avoid the need for copy-pasting code, you could add computation of bounding boxes aligned to various coordinate system axes by enhancing any existing Segment Statistics plugins or adding a new plugin. Note that there are several coordinate system axes that you may want to align to:</p>
<ul>
<li>the world coordinate system (RAS)</li>
<li>the segmentation’s parent coordinate system</li>
<li>the binary labelmap’s image coordinate system (if the segmentation contains a binary labelmap representation)</li>
</ul>
<p>You may need to clone the segmentation and harden the transform that moves the segmentation to the desired coordinate system; and then get RAS bounds (for closed surface representation) or IJK bounds for each segment (for labelmap representation). Depending on what you need exactly, you may be able to use the code that <a class="mention" href="/u/cpinter">@cpinter</a> referred to above with some small changes.</p>

---
