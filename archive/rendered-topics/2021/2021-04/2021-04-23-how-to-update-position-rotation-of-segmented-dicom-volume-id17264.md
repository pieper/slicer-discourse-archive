---
topic_id: 17264
title: "How To Update Position Rotation Of Segmented Dicom Volume"
date: 2021-04-23
url: https://discourse.slicer.org/t/17264
---

# How to update position, rotation of segmented Dicom volume?

**Topic ID**: 17264
**Date**: 2021-04-23
**URL**: https://discourse.slicer.org/t/how-to-update-position-rotation-of-segmented-dicom-volume/17264

---

## Post #1 by @msimonc (2021-04-23 01:27 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.13.0</p>
<p>I have:<br>
Imported a Dicom file<br>
Segmented by painting slices<br>
(a rotatable shape renders on the stage)</p>
<p>Created a Py Extension using Developer Tools | Wizard<br>
added a callback to a Qt control:</p>
<p>volumeNode = slicer.util.getNode(‘volName’)<br>
print(volumeNode)	# vtkMRMLScalarVolumeNode properties as expected</p>
<p>I have been unable to:<br>
reposition or rotate the volume on the stage in code<br>
set the color of the volume<br>
cause any change to the staged volume, ex.<br>
volumeNode.GetDisplayNode().SetColor(1,0,1)<br>
slicer.app.processEvents()</p>
<p>all help appreciated!</p>

---

## Post #2 by @roozbehshams (2021-04-23 02:04 UTC)

<p>Depending on what your goal is this may not be the optimum path but you can start by converting the scalar volume node to a label map volume and create a segmentation node from it. You can then change the color of certain segments.<br>
For rotating and translation you can create a transform node and set that node as the parent transform for the segmentation node.<br>
There are examples in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Create_a_segmentation_from_a_labelmap_volume_and_display_in_3D" rel="noopener nofollow ugc">script repository</a> to do the above and a lot more.</p>

---

## Post #3 by @msimonc (2021-04-23 05:17 UTC)

<p>Thanks <a class="mention" href="/u/roozbehshams">@roozbehshams</a><br>
If the volume is already rotatable using the mouse on the stage, why does a transform node need to be created?<br>
Also if I run util.getNodes(), I already have a vtkMRMLSegmentationNode, vtkMRMLSegmentationStorageNode and vtkMRMLSegmentationDisplayNode.  Do I still need Labelmap-&gt; segment and if so why, thank you.</p>

---

## Post #4 by @roozbehshams (2021-04-23 14:40 UTC)

<p>Technically you’re moving the camera in the scene, not the volume. Like this you can create transforms for each node in the scene when you have more than one node in it.<br>
If you already have a SegmentationNode with your segments in it, then you’re set, no need for conversion.</p>

---
