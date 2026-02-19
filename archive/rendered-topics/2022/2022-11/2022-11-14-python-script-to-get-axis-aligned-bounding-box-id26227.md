---
topic_id: 26227
title: "Python Script To Get Axis Aligned Bounding Box"
date: 2022-11-14
url: https://discourse.slicer.org/t/26227
---

# Python script to get axis-aligned bounding box

**Topic ID**: 26227
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/python-script-to-get-axis-aligned-bounding-box/26227

---

## Post #1 by @xackey (2022-11-14 13:37 UTC)

<p>Could you tell me how to get an axis-aligned bounding box that fits a segment using python interactor? The script repository describes how to create an oriented bounding box, but not an axis-aligned bounding box. I would like to know a script to make a roi like attached image.<br>
Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04d9d9b3d38c873656992e4faa7f35ab365d0c0a.jpeg" data-download-href="/uploads/short-url/GUEr6hFoh0B2daAfk0tsF2SBjc.jpeg?dl=1" title="axis-aligned bounding box" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04d9d9b3d38c873656992e4faa7f35ab365d0c0a_2_354x500.jpeg" alt="axis-aligned bounding box" data-base62-sha1="GUEr6hFoh0B2daAfk0tsF2SBjc" width="354" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04d9d9b3d38c873656992e4faa7f35ab365d0c0a_2_354x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04d9d9b3d38c873656992e4faa7f35ab365d0c0a_2_531x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04d9d9b3d38c873656992e4faa7f35ab365d0c0a.jpeg 2x" data-dominant-color="444C44"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axis-aligned bounding box</span><span class="informations">699×987 79.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-11-14 18:32 UTC)

<p>Probably the easiest is to get the segment as a numpy array as shown <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">here</a> and then use basic numpy function to get index range of non-zero elements.</p>

---

## Post #3 by @xackey (2022-11-14 22:41 UTC)

<p>Could you give a sample script because I am new to python.<br>
Thank you in advance.</p>

---

## Post #4 by @lassoan (2022-11-14 22:59 UTC)

<p>You can use the code snippet that I linked to get the numpy array, then search on Google/StackOverflow for code snippets to get range of non-zero elements in a numpy array.</p>

---

## Post #5 by @xackey (2022-11-15 09:59 UTC)

<p>I was able to make a script but it is very long. Can you make it simpler?</p>
<pre><code class="lang-auto">#Get volume and segmentation
volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
segmentationNode = slicer.mrmlScene. GetFirstNodeByClass ("vtkMRMLSegmentationNode")

# Export "Segment_1" to LabelmapNode
labelmapVolumeNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
segmentIds = vtk.vtkStringArray()
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName("Segment_1")
segmentIds.InsertNextValue(segmentId)
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolumeNode, volumeNode)

#Get 3 axis length and center coordinate (kJI coordinate) of a bounding box
import numpy as np
label = array("LabelMapVolume")
points  = np.where( label == 1 )
length_z=np.max(points[0])- np.min(points[0])+1
length_y=np.max(points[1])- np.min(points[1])+1
length_x=np.max(points[2])- np.min(points[2])+1
center=[(np.max(points[0])+ np.min(points[0]))/2, (np.max(points[1])+ np.min(points[1]))/2, (np.max(points[2])+ np.min(points[2]))/2]

#Transform KJI to RAS coordinate
ijkToRasMatrix = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(ijkToRasMatrix)
ijkPoint = np.array([center[2], center[1], center[0]])  # This is IJK, opposite order compared to KJI.
rasPoint = ijkToRasMatrix.MultiplyFloatPoint(np.append(ijkPoint,1))

#Make an axis-alinged bounding box of "Segment_1". 
roi=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLAnnotationROINode")
roi.SetXYZ(rasPoint[0], rasPoint[1], rasPoint[2])
spacing = volumeNode.GetSpacing()
roi.SetRadiusXYZ(length_x*spacing[0]/2, length_y*spacing[1]/2, length_z*spacing[2]/2)
</code></pre>

---

## Post #6 by @lassoan (2022-11-15 17:58 UTC)

<p>This looks simple enough. Note that the Annotations module is deprecated and will be removed in Slicer-5.4, so I would recommend to use Markups module instead.</p>

---

## Post #7 by @xackey (2022-11-16 08:28 UTC)

<p>I changed to use markups module and leave the script below for other users.<br>
Thank you for your help.</p>
<pre><code class="lang-auto">#Get volume and segmentation. 
volumeNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLScalarVolumeNode")
segmentationNode = slicer.mrmlScene. GetFirstNodeByClass ("vtkMRMLSegmentationNode")

# Export “Segment_1” to LabelmapNode
labelmapVolumeNode=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
segmentIds = vtk.vtkStringArray()
segmentId = segmentationNode.GetSegmentation().GetSegmentIdBySegmentName("Segment_1")
segmentIds.InsertNextValue(segmentId)
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(segmentationNode, segmentIds, labelmapVolumeNode, volumeNode)

#Get three axis length and center coordinate (kJI coordinate) of a bounding box
import numpy as np
label = array("LabelMapVolume")
points  = np.where( label == 1 )
length_z=np.max(points[0])- np.min(points[0])+1
length_y=np.max(points[1])- np.min(points[1])+1
length_x=np.max(points[2])- np.min(points[2])+1
center=[(np.max(points[0])+ np.min(points[0]))/2, (np.max(points[1])+ np.min(points[1]))/2, (np.max(points[2])+ np.min(points[2]))/2]

#Transform KJI to RAS coordinate
ijkToRasMatrix = vtk.vtkMatrix4x4()
volumeNode.GetIJKToRASMatrix(ijkToRasMatrix)
ijkPoint = np.array([center[2], center[1], center[0]])  # This is IJK, opposite order compared to KJI.
rasPoint = ijkToRasMatrix.MultiplyFloatPoint(np.append(ijkPoint,1))
print(rasPoint)

#Make an axis-alinged bounding box of "Segment_1". 
roi=slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsROINode")
roi.SetXYZ(rasPoint[0], rasPoint[1], rasPoint[2])
spacing = volumeNode.GetSpacing()
roi.SetRadiusXYZ(length_x*spacing[0]/2, length_y*spacing[1]/2, length_z*spacing[2]/2)
</code></pre>

---

## Post #8 by @SummerZ2020 (2025-03-26 12:17 UTC)

<aside class="quote no-group" data-username="xackey" data-post="7" data-topic="26227">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/xackey/48/10860_2.png" class="avatar"> xackey:</div>
<blockquote>
<p><code>label = array("LabelMapVolume")</code></p>
</blockquote>
</aside>
<p>In version 5.6.2, the method for obtaining the array needs to be updated as follows. Otherwise, an error will occur: “slicer.util.MRMLNodeNotFoundException: could not find nodes in the scene by name or id ‘LabelMapVolume’”.<br>
label =  slicer.util.arrayFromVolume(labelmapVolumeNode)</p>

---
