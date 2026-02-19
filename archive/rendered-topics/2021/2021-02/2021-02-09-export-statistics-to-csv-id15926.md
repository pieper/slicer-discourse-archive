---
topic_id: 15926
title: "Export Statistics To Csv"
date: 2021-02-09
url: https://discourse.slicer.org/t/15926
---

# Export Statistics to CSV

**Topic ID**: 15926
**Date**: 2021-02-09
**URL**: https://discourse.slicer.org/t/export-statistics-to-csv/15926

---

## Post #1 by @Pete (2021-02-09 21:47 UTC)

<p>Hi,</p>
<p>I am trying to export the calculated statistics/table from the following code to CSV, but obviously the exportToCSVFile isn’t working properly. I don’t know what to replace self with or how to structure this function. Any help greatly appreciated!</p>
<pre><code>## Set masterVolumeNode to first volume node, similar to export Script
masterVolumeNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLScalarVolumeNode')

segmentationNode = getNode('Segmentation')

# Compute segment volumes
resultsTableNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLTableNode')
import SegmentStatistics
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
segStatLogic.getParameterNode().SetParameter("ScalarVolume", masterVolumeNode.GetID())
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.enabled","False")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.voxel_count.enabled","False")
segStatLogic.getParameterNode().SetParameter("ScalarVolumeSegmentStatisticsPlugin.volume_mm3.enabled","False")
segStatLogic.computeStatistics()
segStatLogic.exportToTable(resultsTableNode)
segStatLogic.showTable(resultsTableNode)

testCSV = "/Users/pete/Desktop/test.csv"

segStatLogic.exportToCSVFile(self, testCSV)</code></pre>

---

## Post #2 by @lassoan (2021-02-10 02:33 UTC)

<p>Everything is correct except the last line. The correct syntax is:</p>
<pre><code>segStatLogic.exportToCSVFile(testCSV)</code></pre>

---

## Post #3 by @Pete (2021-02-11 21:54 UTC)

<p>So obvious, thank you again!</p>

---
