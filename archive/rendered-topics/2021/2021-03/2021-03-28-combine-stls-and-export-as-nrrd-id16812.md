---
topic_id: 16812
title: "Combine Stls And Export As Nrrd"
date: 2021-03-28
url: https://discourse.slicer.org/t/16812
---

# Combine STLs and export as NRRD

**Topic ID**: 16812
**Date**: 2021-03-28
**URL**: https://discourse.slicer.org/t/combine-stls-and-export-as-nrrd/16812

---

## Post #1 by @sulaimanvesal (2021-03-28 18:16 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I am able to export .stl file to a single binary label map (nrrd file) very well.</p>
<p>However, I have two .stl files (gland and tumor) that I need to combine them first and then export them as NRRD file.</p>
<p>I wrote the code based on the help from the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_labelmap_node_from_segmentation_node" rel="noopener nofollow ugc">segmentation examples in script repo</a> and my understandings. However, I get this error and I think I am missing something.</p>
<p>I would appreciate, if you help me out with this.</p>
<pre><code>import SampleData
import numpy as np
import SimpleITK as sitk
import sitkUtils

outputPath ="/Volumes/Mac_Partition/output_dir/"
# Input nodes
volumeNode   = slicer.util.loadVolume('/Volumes/Mac_Partition/files/MRI_0001.nii.gz')
prostateNode = slicer.util.loadSegmentation('/Volumes/Mac_Partition/files/STLs/GlandSurface.STL')

# Write segmentation to labelmap volume node with a geometry that matches the volume node
labelmapVolumeNode1 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(prostateNode, labelmapVolumeNode1, volumeNode)

targetNode   = slicer.util.loadSegmentation('/Volumes/Mac_Partition/files/STLs/Target.STL')
# Write segmentation to labelmap volume node with a geometry that matches the volume node
labelmapVolumeNode2 = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(targetNode, labelmapVolumeNode2, volumeNode)

# 'a' and 'b' are numpy arrays,
a = slicer.util.arrayFromVolume(labelmapVolumeNode1)
b = slicer.util.arrayFromVolume(labelmapVolumeNode2)
# combined using any numpy array operations to produce the result array 'c'
c = b-a

segmentationNode = slicer.modules.volumes.logic().CloneVolume(volumeNode, "Difference")
slicer.util.updateVolumeFromArray(segmentationNode, c)
setSliceViewerLayers(background=segmentationNode)

# Write segmentation to labelmap volume node with a geometry that matches the volume node
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
print(segmentationNode)
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, labelmapVolumeNode, volumeNode)

# Masking
voxels = slicer.util.arrayFromVolume(volumeNode)
mask = slicer.util.arrayFromVolume(labelmapVolumeNode)
maskedVoxels = np.copy(voxels)  # we don't want to modify the original volume
maskedVoxels[mask==0] = 0

# Write masked volume to volume node and save it to disk.
maskedVolumeNode = slicer.modules.volumes.logic().CloneVolume(volumeNode, "Masked")
slicer.util.updateVolumeFromArray(maskedVolumeNode, maskedVoxels)
slicer.util.setSliceViewerLayers(maskedVolumeNode)
filepath = outputPath + "/" + volumeNode.GetName()+"-label.nrrd"
slicer.util.saveNode(labelmapVolumeNode, filepath)
</code></pre>
<p>This is the error:<br>
---------------------------------------------------------------------------<br>
TypeError                                 Traceback (most recent call last)<br>
In  [19]:<br>
Line 32:</p>
<pre><code>TypeError: ExportVisibleSegmentsToLabelmapNode argument 1: method requires a vtkMRMLSegmentationNode, a vtkMRMLScalarVolumeNode was provided.
---------------------------------------------------------------------------</code></pre>

---

## Post #2 by @sulaimanvesal (2021-03-28 23:40 UTC)

<p>Never mind, I figured out the solution and corrected the code. Now I am able to combine STLs and export  them as NRRD.</p>

---

## Post #3 by @SabrinaVerga (2021-12-09 10:31 UTC)

<p>Hi <a class="mention" href="/u/sulaimanvesal">@sulaimanvesal</a>, I am trying to perform the same task as the one you shared in this post. I am still getting the same errors as yours, but I saw you solved the problem.<br>
Do you mind share your code with the solution ?<br>
thanks in advande for helping,<br>
Sabrina</p>

---

## Post #4 by @lassoan (2021-12-11 15:31 UTC)

<p>The code above is incorrect. It sets a volume node in the variable called <code>segmentationNode</code>. Then this volume node is used as an input in <code>ExportVisibleSegmentsToLabelmapNode</code>, which expects a segmentation node as input. I would recommend to complete the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Scripting and module development tutorial</a>, study the <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">segmentation section in the documentation</a> and examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>, which all work correctly. Then, once you have a good understanding of what’s happening, you can have a look at the script above and make it work.</p>

---
