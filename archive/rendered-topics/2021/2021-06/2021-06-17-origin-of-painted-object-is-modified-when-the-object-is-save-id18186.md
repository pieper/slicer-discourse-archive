---
topic_id: 18186
title: "Origin Of Painted Object Is Modified When The Object Is Save"
date: 2021-06-17
url: https://discourse.slicer.org/t/18186
---

# Origin of painted object is modified when the object is saved to dicom and loaded into Slicer

**Topic ID**: 18186
**Date**: 2021-06-17
**URL**: https://discourse.slicer.org/t/origin-of-painted-object-is-modified-when-the-object-is-saved-to-dicom-and-loaded-into-slicer/18186

---

## Post #1 by @Federico (2021-06-17 12:43 UTC)

<p>Hi all, I have the following situation when working with a dataset where a MR has been fused to the base CT scan:</p>
<ol>
<li>
<p>In the MR, I paint a segmentation object in the segment editor via the sphere brush and print the origin of the object (see below for code)</p>
</li>
<li>
<p>I save the segmentation object to my local machine and load it again into slicer via the DICOM module. The origin of the loaded object does not coincide with the origin of the painted object, although the objects are shown on top of each other in the views.</p>
</li>
</ol>
<p>This is the code to retrieve the origin:</p>
<pre><code class="lang-auto">segm = node.GetSegmentation()
binaryLabelmapPresent = segm.CreateRepresentation(
            slicer.vtkSegmentationConverter.GetSegmentationBinaryLabelmapRepresentationName())

segment = segm.GetNthSegment(0)
labelMapName = vtkSegmentationCore.vtkSegmentationConverter.GetSegmentationBinaryLabelmapRepresentationName() 
vtkOrientedImageData = segment.GetRepresentation(labelMapName)
origin = vtkOrientedImageData.GetOrigin()
</code></pre>
<p>Do you see a problem with the code or can you please explain why the two origins differ?</p>

---

## Post #2 by @lassoan (2021-06-17 13:26 UTC)

<p>Origin of an segment representation inside a segmentation is an internal implementation detail. What is guaranteed that the physical location of voxels remain the same. Extent, origin, and axis directions may change as you manipulate segment or you save the file (as you need to consolidate all segments into a single 3D/4D array).</p>
<p>If you want a voxel array in a particular geometry then specify a reference geometry (volume node) when you <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-labelmap-node-from-segmentation-node">export the segment into a labelmap</a>.</p>

---
