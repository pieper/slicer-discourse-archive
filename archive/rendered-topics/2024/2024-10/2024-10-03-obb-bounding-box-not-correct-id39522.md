---
topic_id: 39522
title: "Obb Bounding Box Not Correct"
date: 2024-10-03
url: https://discourse.slicer.org/t/39522
---

# OBB bounding Box not correct

**Topic ID**: 39522
**Date**: 2024-10-03
**URL**: https://discourse.slicer.org/t/obb-bounding-box-not-correct/39522

---

## Post #1 by @G_Tom (2024-10-03 14:11 UTC)

<p>I use this code to compute and visualize the bounding box but it is not correct. Not sure why:</p>
<blockquote>
<pre><code># Compute bounding boxes
import SegmentStatistics
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.obb_origin_ras.enabled",str(True))
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.obb_diameter_mm.enabled",str(True))
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.obb_direction_ras_x.enabled",str(True))
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.obb_direction_ras_y.enabled",str(True))
segStatLogic.getParameterNode().SetParameter("LabelmapSegmentStatisticsPlugin.obb_direction_ras_z.enabled",str(True))
segStatLogic.computeStatistics()
stats = segStatLogic.getStatistics()

# Draw ROI for each oriented bounding box
import numpy as np
for segmentId in stats["SegmentIDs"]:
  # Get bounding box
  obb_origin_ras = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_origin_ras"])
  obb_diameter_mm = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_diameter_mm"])
  obb_direction_ras_x = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_direction_ras_x"])
  obb_direction_ras_y = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_direction_ras_y"])
  obb_direction_ras_z = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_direction_ras_z"])
  # Create ROI
  segment = segmentationNode.GetSegmentation().GetSegment(segmentId)
  roi=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
  roi.SetName(segment.GetName() + " OBB")
  roi.GetDisplayNode().SetHandlesInteractive(False)  # do not let the user resize the box
  roi.SetSize(obb_diameter_mm)
  # Position and orient ROI using a transform
  obb_center_ras = obb_origin_ras+0.5*(obb_diameter_mm[0] * obb_direction_ras_x + obb_diameter_mm[1] * obb_direction_ras_y + obb_diameter_mm[2] * obb_direction_ras_z)
  boundingBoxToRasTransform = np.row_stack((np.column_stack((obb_direction_ras_x, obb_direction_ras_y, obb_direction_ras_z, obb_center_ras)), (0, 0, 0, 1)))
  boundingBoxToRasTransformMatrix = slicer.util.vtkMatrixFromArray(boundingBoxToRasTransform)
  roi.SetAndObserveObjectToNodeMatrix(boundingBoxToRasTransformMatrix)
</code></pre>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b980b9d8e221c35da7db39ce16f1c0d409f2a971.png" data-download-href="/uploads/short-url/qt27OThH1CenTkpyAhbpRGlYEAF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b980b9d8e221c35da7db39ce16f1c0d409f2a971_2_690x329.png" alt="image" data-base62-sha1="qt27OThH1CenTkpyAhbpRGlYEAF" width="690" height="329" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b980b9d8e221c35da7db39ce16f1c0d409f2a971_2_690x329.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b980b9d8e221c35da7db39ce16f1c0d409f2a971_2_1035x493.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b980b9d8e221c35da7db39ce16f1c0d409f2a971_2_1380x658.png 2x" data-dominant-color="36323C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1401×669 23.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks for your suggestions on how to correct this ?</p>

---
