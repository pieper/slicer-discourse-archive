---
topic_id: 11114
title: "3D Element Is Not Filling Out The Whole Cube"
date: 2020-04-14
url: https://discourse.slicer.org/t/11114
---

# 3D element is not filling out the whole cube

**Topic ID**: 11114
**Date**: 2020-04-14
**URL**: https://discourse.slicer.org/t/3d-element-is-not-filling-out-the-whole-cube/11114

---

## Post #1 by @zeliair (2020-04-14 13:35 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.2<br>
Expected behavior: When I load my Data into 3D-Slicer I expect the object to be in ) the “centre” of the cube.<br>
Actual behavior: Sometimes it happens, that my object is very “far away” in one corner of the cube, in my case in the lower right corner, and i have to zoom a lot to get there. It’s not easy to move the object because it’s not in the centre.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f95feb98b8c16fd81d42addc63ed2dedc58a6c50.jpeg" alt="HelpCube" data-base62-sha1="zA4oHAb2xNfKLZsMh4nMHJomQzm" width="658" height="380"></p>

---

## Post #2 by @manjula (2020-04-14 13:52 UTC)

<p>I think you should press the “center the 3D view” button to center the object</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/98acc716e08cf8cc7112744c57370819d89e3482.png" alt="Screenshot from 2020-04-14 15-51-20" data-base62-sha1="lMCKv1SV7LKoj30E2YCENDyQygW" width="549" height="412"></p>

---

## Post #3 by @zeliair (2020-04-14 14:07 UTC)

<p>I already did that. When I press “Center the 3D view” button it appears as I’ve sent it to you.</p>

---

## Post #4 by @pieper (2020-04-14 16:07 UTC)

<p>That means you have something else in the scene.  Maybe even just a small point in the opposite corner of the cube.</p>

---

## Post #5 by @manjula (2020-04-14 20:51 UTC)

<p>Just a though on visualizing if there is a very small point/points in the opposite corner,</p>
<p>Segment the object you want, and create a second segment , selecting everything else, even if you do not see anything.</p>
<p>then use the the script repository code,</p>
<p>segmentationNode = getNode(‘Segmentation’)</p>
<h1>Compute bounding boxes</h1>
<p>import SegmentStatistics<br>
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()<br>
segStatLogic.getParameterNode().SetParameter(“Segmentation”, segmentationNode.GetID())<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_origin_ras.enabled”,str(True))<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_diameter_mm.enabled”,str(True))<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_direction_ras_x.enabled”,str(True))<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_direction_ras_y.enabled”,str(True))<br>
segStatLogic.getParameterNode().SetParameter(“LabelmapSegmentStatisticsPlugin.obb_direction_ras_z.enabled”,str(True))<br>
segStatLogic.computeStatistics()<br>
stats = segStatLogic.getStatistics()</p>
<h1>Draw ROI for each oriented bounding box</h1>
<p>import numpy as np<br>
for segmentId in stats[‘SegmentIDs’]:<br>
# Get bounding box<br>
obb_origin_ras = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_origin_ras”])<br>
obb_diameter_mm = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_diameter_mm”])<br>
obb_direction_ras_x = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_direction_ras_x”])<br>
obb_direction_ras_y = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_direction_ras_y”])<br>
obb_direction_ras_z = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.obb_direction_ras_z”])<br>
# Create ROI<br>
segment = segmentationNode.GetSegmentation().GetSegment(segmentId)<br>
roi=slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLAnnotationROINode”)<br>
roi.SetName(segment.GetName()+’ bounding box’)<br>
roi.SetXYZ(0.0, 0.0, 0.0)<br>
roi.SetRadiusXYZ(<em>(0.5</em>obb_diameter_mm))<br>
# Position and orient ROI using a transform<br>
obb_center_ras = obb_origin_ras+0.5*(obb_diameter_mm[0] * obb_direction_ras_x + obb_diameter_mm[1] * obb_direction_ras_y + obb_diameter_mm[2] * obb_direction_ras_z)<br>
boundingBoxToRasTransform = np.row_stack((np.column_stack((obb_direction_ras_x, obb_direction_ras_y, obb_direction_ras_z, obb_center_ras)), (0, 0, 0, 1)))<br>
boundingBoxToRasTransformMatrix = slicer.util.vtkMatrixFromArray(boundingBoxToRasTransform)<br>
transformNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLTransformNode’)<br>
transformNode.SetAndObserveMatrixTransformToParent(boundingBoxToRasTransformMatrix)<br>
roi.SetAndObserveTransformNodeID(transformNode.GetID())</p>
<p>which will help you in visualizing where the other segment is.</p>
<p>or maybe there are better way of locating it.</p>

---
