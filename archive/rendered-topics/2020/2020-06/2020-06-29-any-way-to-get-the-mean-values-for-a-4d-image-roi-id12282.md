# Any way to get the mean values for a 4D image ROI

**Topic ID**: 12282
**Date**: 2020-06-29
**URL**: https://discourse.slicer.org/t/any-way-to-get-the-mean-values-for-a-4d-image-roi/12282

---

## Post #1 by @xlucox (2020-06-29 20:10 UTC)

<p>Hi!!!</p>
<p>I’m trying to get and array with the mean values of a 4D volume based in a segmentation. I’ve been reading the plugins which use the module segment statistics but I couldn’t find anything helpful.</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2020-07-01 02:03 UTC)

<p>There is currently no automated module that would run Segment Statistics for each time point of a time sequence. If you are familiar with Python programming then it should be very easy to write a script or Slicer module for this (few-hour work for someone who already knows Slicer well; couple of days for a newcomer).  You can use <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/CropVolumeSequence/CropVolumeSequence.py">CropVolumeSequence module</a> as a template.</p>
<p>Let us know if you are willing to try this. If not, then right now the only option is to do it manually (click Apply in Segment Statistics module to compute results, hit Ctr+Shift+Right to go to the next frame, hit Apply again, etc.).</p>

---

## Post #3 by @xlucox (2020-07-01 16:49 UTC)

<p>Yes, I solved it.</p>
<p>I used qSlicerMultiVolumeExplorerModuleHelper.extracFrame to create a new scalar volume node for each frame and then used SegmentStatistics.SegmentStatisticsLogic() to extract the features which I wanted (Mean, Std) for each frame and segment.</p>

---

## Post #4 by @lassoan (2020-07-01 17:19 UTC)

<p>Would you mind sharing the script so that others can learn from it? Thank you!</p>

---

## Post #5 by @xlucox (2020-07-01 19:11 UTC)

<p>from qSlicerMultiVolumeExplorerModuleHelper import qSlicerMultiVolumeExplorerModuleHelper as Helper<br>
import SegmentStatistics<br>
import numpy as np</p>
<p>self.bgMultiVolumeSelector = slicer.qMRMLNodeComboBox()<br>
self.bgMultiVolumeSelector.nodeTypes = [‘vtkMRMLMultiVolumeNode’]</p>
<p>self.segmentationSelector = slicer.qMRMLNodeComboBox()<br>
self.segmentationSelector.nodeTypes = [“vtkMRMLSegmentationNode”]</p>
<p>def GetStatisticsOfSegments(self):</p>
<pre><code>Seg = self.segmentationSelector.currentNode()
self.logic = SegmentStatistics.SegmentStatisticsLogic()
self.parameterNode = self.logic.getParameterNode()
self.parameterNode.SetParameter("Segmentation", Seg.GetID())
self.parameterNode.SetParameter('ClosedSurfaceSegmentStatisticsPlugin.enabled','False')
self.parameterNode.SetParameter('LabelmapSegmentStatisticsPlugin.enabled','False')
### All the plugins are set as a default True.
self.parameterNode.SetParameter('ScalarVolumeSegmentStatisticsPlugin.enabled','True')
self.parameterNode.SetParameter('ScalarVolumeSegmentStatisticsPlugin.max.enabled','False')
self.parameterNode.SetParameter('ScalarVolumeSegmentStatisticsPlugin.mean.enabled','True')
self.parameterNode.SetParameter('ScalarVolumeSegmentStatisticsPlugin.median.enabled','False')
self.parameterNode.SetParameter('ScalarVolumeSegmentStatisticsPlugin.min.enabled','False')
self.parameterNode.SetParameter('ScalarVolumeSegmentStatisticsPlugin.stdev.enabled','True')
self.parameterNode.SetParameter('ScalarVolumeSegmentStatisticsPlugin.volume_cm3.enabled','False')
self.parameterNode.SetParameter('ScalarVolumeSegmentStatisticsPlugin.volume_mm3.enabled','False')
self.parameterNode.SetParameter('ScalarVolumeSegmentStatisticsPlugin.voxel_count.enabled','False')

self.Stats = {}

if self.bgMultiVolumeSelector.currentNode():
  for Frame in range(self.bgMultiVolumeSelector.currentNode().GetNumberOfFrames()):
    self.FrameNode = Helper.extractFrame(self.FrameNode, self.bgMultiVolumeSelector.currentNode(), Frame)
    self.parameterNode.SetParameter("ScalarVolume", self.FrameNode.GetID())
    visibleSegmentIds = vtk.vtkStringArray()
    Seg.GetSegmentation().GetSegmentIDs(visibleSegmentIds)
    for segmentIndex in range(visibleSegmentIds.GetNumberOfValues()):
      segmentID = visibleSegmentIds.GetValue(segmentIndex)
      self.logic.updateStatisticsForSegment(segmentID)
    statistics = self.logic.getStatistics()
    keys = self.logic.getNonEmptyKeys()
    longname, names = self.logic.getHeaderNames(keys)
    for key in keys:
      measurements = [statistics[segmentID, key] for segmentID in statistics["SegmentIDs"] if
                      (segmentID, key) in statistics] 
      if not self.Stats.get(names[key],None):
        self.Stats[names[key]] = [measurements]
      else:
        if names[key] != 'Segment':
          self.Stats[names[key]].append(measurements)
      
  self.NumberOfSegments = len(self.Stats['Segment'][0])
  self.Mean = np.array(self.Stats['Mean'])
  self.Std = np.array(self.Stats['Standard Deviation'])
</code></pre>
<p>It is something like this</p>

---
