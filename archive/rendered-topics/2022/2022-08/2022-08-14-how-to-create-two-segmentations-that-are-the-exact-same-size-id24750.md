---
topic_id: 24750
title: "How To Create Two Segmentations That Are The Exact Same Size"
date: 2022-08-14
url: https://discourse.slicer.org/t/24750
---

# How to create two segmentations that are the exact same size?

**Topic ID**: 24750
**Date**: 2022-08-14
**URL**: https://discourse.slicer.org/t/how-to-create-two-segmentations-that-are-the-exact-same-size/24750

---

## Post #1 by @MatthewVanOirschot (2022-08-14 10:19 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226<br>
Expected behavior:</p>
<p>I am working on a radiomics project that utilizes a sphere-shaped region as the input region. The goal of the study is to determine whether a region of constant shape and size can provide useful radiomic information. I am creating the spheres using a script, modified from the bounding box script provided in the Slicer script repository (see attached code clipping).</p>
<pre><code class="lang-auto">segmentationNode = slicer.mrmlScene.GetFirstNodeByClass('vtkMRMLSegmentationNode')
nodeLabel = segmentationNode.GetName()

# Compute statistics
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

# Create segmentation node
seg = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
seg.SetName(nodeLabel + "sphere")

# Draw ROI for each sphere
import numpy as np
for segmentId in stats["SegmentIDs"]:
  # Get statistics
  obb_origin_ras = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_origin_ras"])
  obb_diameter_mm = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_diameter_mm"])
  obb_direction_ras_x = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_direction_ras_x"])
  obb_direction_ras_y = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_direction_ras_y"])
  obb_direction_ras_z = np.array(stats[segmentId,"LabelmapSegmentStatisticsPlugin.obb_direction_ras_z"])
  
  # Create sphere
  sphere = vtk.vtkSphereSource()
  sphere.SetRadius(2.5)
  sphere.SetCenter(0.0, 0.0, 0.0)

  sphereNode = slicer.modules.models.logic().AddModel(sphere.GetOutputPort())

  # Position and orient ROI using a transform
  obb_center_ras = obb_origin_ras+0.5*(obb_diameter_mm[0] * obb_direction_ras_x + obb_diameter_mm[1] * obb_direction_ras_y + obb_diameter_mm[2] * obb_direction_ras_z)
  boundingSphereToRasTransform = np.row_stack((np.column_stack((obb_direction_ras_x, obb_direction_ras_y, obb_direction_ras_z, obb_center_ras)), (0, 0, 0, 1)))
  boundingSphereToRasTransformMatrix = slicer.util.vtkMatrixFromArray(boundingSphereToRasTransform)
  transformNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTransformNode")
  transformNode.SetAndObserveMatrixTransformToParent(boundingSphereToRasTransformMatrix)
  sphereNode.SetAndObserveTransformNodeID(transformNode.GetID())
  segment = segmentationNode.GetSegmentation().GetSegment(segmentId)
  if segment.GetName() == "Segment_1":
    sphereNode.SetName("pos")
  elif segment.GetName() == "Segment_2":
    sphereNode.SetName("neg")
  else:
    sphereNode.SetName("error")
    
  # Convert model to segmentation
  slicer.modules.segmentations.logic().ImportModelToSegmentationNode(sphereNode, seg)
  slicer.mrmlScene.RemoveNode(sphereNode)
  slicer.mrmlScene.RemoveNode(transformNode)

segto = seg.GetSegmentation()
segto.GetNthSegment(0).SetColor(178/255, 212/255, 242/255)
seg.CreateClosedSurfaceRepresentation()
</code></pre>
<p>Actual behavior:</p>
<p>However, when I run radiomic feature extraction, the results show that the segmentations differ in size, sometimes by a large amount. Below is an example extraction on one of the Sample Datasets (MRBrainTumor1), showing that the number of voxels differ between the two spheres, as well as the LeastAxisLength and MajorAxisLength. I have tried a few workarounds for this, such as trying to place the sphere on the intersection point of 4 voxels, but I have been unable to find information on how the RAS coordinate system and global voxel coordinate system relate to each other.</p>
<p>Any advice on how to create two geometrically congruent segmentations on different parts of an image? Any suggestions/workarounds are appreciated. Thank you!</p>
<p>Segmentation (script) results:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5046d13ad5404895919cddf6c76424485f1535be.jpeg" data-download-href="/uploads/short-url/bs9Ve36Sc5YoW9oWhlKWSN8RRnw.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5046d13ad5404895919cddf6c76424485f1535be_2_690x289.jpeg" alt="image" data-base62-sha1="bs9Ve36Sc5YoW9oWhlKWSN8RRnw" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5046d13ad5404895919cddf6c76424485f1535be_2_690x289.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/5046d13ad5404895919cddf6c76424485f1535be_2_1035x433.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/5046d13ad5404895919cddf6c76424485f1535be.jpeg 2x" data-dominant-color="A0A09E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1339×562 98.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Extraction settings:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5534ffc46bc1e616945b411bae6db99de55cd429.png" data-download-href="/uploads/short-url/c9M8n0gvxSIPsU1PH4vMyZQ0F5L.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/5534ffc46bc1e616945b411bae6db99de55cd429.png" alt="image" data-base62-sha1="c9M8n0gvxSIPsU1PH4vMyZQ0F5L" width="690" height="376" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">731×399 8.61 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Radiomic feature results:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f082ece2e37865f8e629399dcbd8a2e5e66b702.png" data-download-href="/uploads/short-url/4qwkEUBtLwSNHQrI1p3CDpNRaMO.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f082ece2e37865f8e629399dcbd8a2e5e66b702.png" alt="image" data-base62-sha1="4qwkEUBtLwSNHQrI1p3CDpNRaMO" width="690" height="259" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">829×312 6.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e70f4f4b6ecdf1229140d7862840c146c48eab25.png" data-download-href="/uploads/short-url/wY35ZwxTOmvm7imybym8y844k4Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e70f4f4b6ecdf1229140d7862840c146c48eab25.png" alt="image" data-base62-sha1="wY35ZwxTOmvm7imybym8y844k4Z" width="690" height="260" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">832×314 7.83 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2022-08-18 19:53 UTC)

<p>Without having the time to deeply look at your question (reading the core etc): would spatial registration of the inputs solve the problem? If not, look into setting the same reference geometry to the segmentation nodes.</p>

---

## Post #3 by @MatthewVanOirschot (2022-08-22 07:57 UTC)

<p>Hi Csaba,</p>
<p>Thanks for taking the time to respond. I’m interested in trying your proposed solutions, but I’m not sure where to start. How would I spatially register the inputs and/or set the reference geometry of the segmentation nodes? I assume that the nodes are currently both registered to the global coordinate system.</p>
<p>Matthew</p>

---
