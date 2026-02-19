---
topic_id: 258
title: "Threshold On Segment"
date: 2017-05-03
url: https://discourse.slicer.org/t/258
---

# Threshold on Segment

**Topic ID**: 258
**Date**: 2017-05-03
**URL**: https://discourse.slicer.org/t/threshold-on-segment/258

---

## Post #1 by @basti (2017-05-03 18:59 UTC)

<p>I’m trying to threshold a volume to a created segment. Unfortunately the segment will be empty. What did I forget?</p>
<pre><code>    # create SegmentationNode and Segment #

    self.segmentationNode = slicer.vtkMRMLSegmentationNode()
    slicer.mrmlScene.AddNode(self.segmentationNode)
    self.segmentPrintId = self.segmentationNode.GetSegmentation().AddEmptySegment("ThresholdSegment", "Segment_Threshold", [4,4,4])

    # threshold #

    import vtkSegmentationCorePython as vtkSegmentationCore
    segmentationsLogic = slicer.vtkSlicerSegmentationsModuleLogic()

    volumeNode = self.inputSelector.currentNode()  #volumeNode of a selector
    inputImageData = volumeNode.GetImageData()

    outputImageData = vtkSegmentationCore.vtkOrientedImageData()

    thresh = vtk.vtkImageThreshold()
    thresh.SetInputData(volumeNode.GetImageData())
    thresh.ThresholdBetween(self.imageThresholdSliderWidget.minimumValue, self.imageThresholdSliderWidget.maximumValue)
    thresh.SetInValue(1000)
    thresh.SetOutValue(0)
    thresh.SetOutputScalarType(outputImageData.GetScalarType())
    thresh.Update()
    outputImageData.DeepCopy(thresh.GetOutput())

    segmentationsLogic.SetBinaryLabelmapToSegment(outputImageData, self.segmentationNode, self.segmentPrintId)
</code></pre>
<p>Thank you again!</p>

---

## Post #2 by @cpinter (2017-05-04 20:08 UTC)

<p>Hi Basti,</p>
<p>Thanks for the detailed report!</p>
<p>First of all, it is best to use the actual module logic, that has the MRML scene and everything:<br>
<code>segmentationsLogic = slicer.modules.segmentations.logic()</code></p>
<p>Second, I’d check if the output image actually contains a meaningful image, just for the sake of debugging. For example like this:<br>
<code>acc = vtk.vtkImageAccumulate() acc.SetInputData(outputImageData) acc.SetIgnoreZero(1) acc.Update() acc.GetVoxelCount() # Get number of non-zero voxels (should be &gt;0) acc.SetIgnoreZero(0) acc.Update() acc.GetVoxelCount() # Get number of all voxels (should be different than the non-zero one) acc.GetMin() # Should be 0 acc.GetMax() # Should be 1000</code></p>
<p>Third, what is the return value of the last call? True or False? if it’s false, is there any error in the log? Circle button with X in it in bottom right corner, or whole log in Help/Report a bug.</p>
<p>Fourth, I think I found a bug that might explain the problem if the above three are all good. I did this to get the IDs in the segmentation:<br>
<code>ids=vtk.vtkStringArray() segmentationNode.GetSegmentation().GetSegmentIDs(ids) ids.GetValue(0)</code><br>
and it is not the same as segmentPrintId, which should be. It seems that the names and IDs are not handled correctly by vtkSegmentation::AddEmptySegment. I will debug into it and see what the exact problem is.</p>
<p>For a short term solution you can just get the IDs the same way I did for testing.</p>

---

## Post #3 by @cpinter (2017-05-04 20:22 UTC)

<p>The bug should be fixed in the commit below. Please download tomorrow’s nightly and try again.<br>
<aside class="onebox githubcommit">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/commit/84f11249053c6da1c4f3abcb3edd9d20d226ef44" target="_blank" rel="nofollow noopener">github.com/Slicer/Slicer</a>
  </header>
  <article class="onebox-body">
    
<h4>
  <a href="https://github.com/Slicer/Slicer/commit/84f11249053c6da1c4f3abcb3edd9d20d226ef44" target="_blank" rel="nofollow noopener">BUG: Use segment ID in AddEmptySegment</a>
</h4>

  <pre class="message" style="white-space: pre-wrap;">Even if segment ID was specified, that argument was not used, and the segment name became the actual segment ID.

git-svn-id: http://svn.slicer.org/Slicer4/trunk@25998 3bd1e089-480b-0410-8dfb-8563597acbee</pre>

<div class="date">
  by <a href=""></a>
  on <a href="https://github.com/Slicer/Slicer/commit/84f11249053c6da1c4f3abcb3edd9d20d226ef44" target="_blank" rel="nofollow noopener">08:20PM - 04 May 17</a>
</div>

<div class="github-commit-stats">
  changed <strong>1 files</strong>
  with <strong>1 additions</strong>
  and <strong>1 deletions</strong>.
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #4 by @lassoan (2017-05-04 21:02 UTC)

<p>In tomorrow’s nightly version (that contains Csaba’s fixes) this will work:</p>
<pre><code>import vtkSegmentationCorePython as vtkSegmentationCore

segmentationNode = slicer.vtkMRMLSegmentationNode()
slicer.mrmlScene.AddNode(segmentationNode)
segmentPrintId = segmentationNode.GetSegmentation().AddEmptySegment("ThresholdSegment", "Segment_Threshold", [1.0,1.0,0.0])

segmentationsLogic = slicer.modules.segmentations.logic()

volumeNode = getNode('MRHead')
inputImageData = segmentationsLogic.CreateOrientedImageDataFromVolumeNode(volumeNode)
inputImageData.UnRegister(None)

minThreshold = 20
maxThreshold = 80
thresh = vtk.vtkImageThreshold()
thresh.SetInputData(volumeNode.GetImageData())
thresh.ThresholdBetween(minThreshold, maxThreshold)
thresh.SetInValue(1000)
thresh.SetOutValue(0)
thresh.Update()

outputImageData = vtkSegmentationCore.vtkOrientedImageData()
outputImageData.ShallowCopy(thresh.GetOutput())
imageToWorldMatrix = vtk.vtkMatrix4x4()
inputImageData.GetImageToWorldMatrix(imageToWorldMatrix)
outputImageData.SetImageToWorldMatrix(imageToWorldMatrix)

segmentationsLogic.SetBinaryLabelmapToSegment(outputImageData, segmentationNode, segmentPrintId)</code></pre>

---

## Post #5 by @basti (2017-05-07 22:01 UTC)

<p>Thank you very much, now it works! I also added</p>
<pre><code>segmentationNode.CreateDefaultDisplayNodes()
</code></pre>
<p>to display the Node.</p>

---
