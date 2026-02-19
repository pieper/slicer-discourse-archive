---
topic_id: 9592
title: "Point Inside A Closed Surface Centre"
date: 2019-12-23
url: https://discourse.slicer.org/t/9592
---

# Point inside a closed surface/centre

**Topic ID**: 9592
**Date**: 2019-12-23
**URL**: https://discourse.slicer.org/t/point-inside-a-closed-surface-centre/9592

---

## Post #1 by @Jainey (2019-12-23 13:54 UTC)

<p>I m trying to get the centre inside a closed surface/model.<br>
Is there a code for this please</p>
<p>Thanks</p>

---

## Post #2 by @Jainey (2019-12-23 14:16 UTC)

<p>I tried using this document- did not work</p>
<pre><code class="lang-python">segmentationNode = getNode('Segmentation')
segmentId = 'Segment_1'

# Get array voxel coordinates
import numpy as np
seg=arrayFromSegment(segmentation_node, segmentId)
# numpy array has voxel coordinates in reverse order (KJI instead of IJK)
# and the array is cropped to minimum size in the segmentation
mean_KjiCropped = [coords.mean() for coords in np.nonzero(seg)]

# Get segmentation voxel coordinates
segImage = segmentationNode.GetBinaryLabelmapRepresentation(segmentId)
segImageExtent = segImage.GetExtent()
# origin of the array in voxel coordinates is determined by the start extent
mean_Ijk = [mean_KjiCropped[2], mean_KjiCropped[1], mean_KjiCropped[0]] + np.array([segImageExtent[0], segImageExtent[2], segImageExtent[4]])

# Get segmentation physical coordinates
ijkToWorld = vtk.vtkMatrix4x4()
segImage.GetImageToWorldMatrix(ijkToWorld)
mean_World = [0, 0, 0, 1]
ijkToRas.MultiplyPoint(np.append(mean_Ijk,1.0), mean_World)
mean_World = mean_World[0:3]

# If segmentation node is transformed, apply that transform to get RAS coordinates
transformWorldToRas = vtk.vtkGeneralTransform()
slicer.vtkMRMLTransformNode.GetTransformBetweenNodes(segmentationNode.GetParentTransformNode(), None, transformWorldToRas)
mean_Ras = transformWorldToRas.TransformPoint(mean_World)

# Show mean position value and jump to it in all slice viewers
print(mean_Ras)
slicer.modules.markups.logic().JumpSlicesToLocation(mean_Ras[0], mean_Ras[1], mean_Ras[2], True
</code></pre>
<p>Thanks</p>

---

## Post #3 by @lassoan (2019-12-23 14:20 UTC)

<p>What do you mean by “center”?</p>
<p>Center of gravity, center of coordinate system axis aligned bounding box, center of oriented bounding box, center of largest largest sphere that fits inside the model, etc.?</p>
<p>Most of these center points are not guaranteed to be inside the closed surface.</p>
<p>What would you like to use this for?</p>
<p>The code above is for segmentation nodes. If you have a model node then you need to import to segmentation node first. Note that segmentation nodes already have a “jump to segment” feature (you can try it by right clicking on the segment in Segmentations or Segment Editor module).</p>

---

## Post #4 by @Jainey (2019-12-23 14:44 UTC)

<p>I am looking to calculate the centre of mass, Thanks</p>

---
