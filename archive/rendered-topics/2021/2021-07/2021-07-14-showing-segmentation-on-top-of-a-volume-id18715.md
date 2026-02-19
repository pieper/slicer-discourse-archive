---
topic_id: 18715
title: "Showing Segmentation On Top Of A Volume"
date: 2021-07-14
url: https://discourse.slicer.org/t/18715
---

# Showing Segmentation on Top of A Volume

**Topic ID**: 18715
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/showing-segmentation-on-top-of-a-volume/18715

---

## Post #1 by @ColdFour (2021-07-14 02:12 UTC)

<p>Hello all,</p>
<p>I’m currently making an extension that has some heart-related features, I give the currently displayed VolumeNode array to a Deep Learning model to get an array of the heart’s segmentation, then load it into a LabelMapVolume to create a segmentation node from it.</p>
<p>I want it to show the segmentation on top of the volume containing the heart, however, the only way that I get the segmentation to show is by using the GUI to hide the volume, then toggling the Label or Segmentation, unhiding the Volume hides the segmentation/label.</p>
<pre><code class="lang-auto"># Create a new LabelMapVolume
LabelMapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode', f'{Name}-Label')

# Update the LabelMapVolume from the given Segmentation array
slicer.util.updateVolumeFromArray(LabelMapVolumeNode, Segmentation)

# Create a SegmentationNode
SegNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", f'{Name}-Segmentation')

# Load the LabelMapVolume into the SegmentationNode 
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(LabelMapVolumeNode, SegNode)

# Create Closed Surface Representation
if HeartSegVis:
    SegNode.CreateClosedSurfaceRepresentation()
</code></pre>
<p>Any help will be much appreciated, sorry for the long explanation</p>
<p>Thanks,</p>

---

## Post #2 by @lassoan (2021-07-14 02:42 UTC)

<p>You have only copied the voxel data. You must also need to copy the IJKToRAS matrix from the original volume into the labelmap volume (it specifies the image origin, spacing, and axis directions).</p>

---

## Post #3 by @ColdFour (2021-07-14 22:54 UTC)

<p>This solved the problem, thanks!<br>
This is the updated code for refrence.</p>
<pre><code class="lang-auto"># Get IJKToRAS Matrix
VolumeIJKToRAS = vtk.vtkMatrix4x4()
InputVolumeNode.GetIJKToRASMatrix(VolumeIJKToRAS)

# Create a new LabelMapVolume
LabelMapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode', f'{Name}-Label')

# Set IJKToRAS Matrix To That of The Original Volume
LabelMapVolumeNode.SetIJKToRASMatrix(VolumeIJKToRAS)

# Update the LabelMapVolume from the given Segmentation array
slicer.util.updateVolumeFromArray(LabelMapVolumeNode, Segmentation)

# Create a SegmentationNode
SegNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode", f'{Name}-Segmentation')

# Load the LabelMapVolume into the SegmentationNode 
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(LabelMapVolumeNode, SegNode)

# Create Closed Surface Representation
if HeartSegVis:
    SegNode.CreateClosedSurfaceRepresentation()
</code></pre>

---
