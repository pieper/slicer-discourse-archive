# Merging two different segmentations/models

**Topic ID**: 30047
**Date**: 2023-06-15
**URL**: https://discourse.slicer.org/t/merging-two-different-segmentations-models/30047

---

## Post #1 by @umgpy (2023-06-15 09:18 UTC)

<p>I have surface model along with it’s segmentation to this I want to merge another segmentation which is not in the same segmentation node. Due to this the merge function in segmentation editor model does not work.</p>
<p>Is there a way to either move the segmentation within the other so that the merge operation can take place. Or is there another way to this?</p>
<p>Additionally I would like to process this as a batch operation.</p>
<p>I am unable to attach a screenshot to provide a little more context, if needed I can do so through other image services.</p>
<p>Thanks in advance and a greetings to everyone at the Project week!</p>

---

## Post #2 by @S_Arbabi (2023-06-15 09:38 UTC)

<p>I think you can do this by:<br>
1-converting each segmentation into a labelmap<br>
segmentationLblmap = slicer.mrmlScene.AddNewNodeByClass(“vtkMRMLLabelMapVolumeNode”)<br>
slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(segmentationNode, segmentationLblmap,  reference_volume_node)<br>
2-getting the array of each segmentation<br>
array1 = slicer.util.arrayFromVolume(segmentationLblmap)<br>
3-do a boolean OR operation between two arrays<br>
arrayOR = np.logical_or(array1.astype(bool), array2.astype(bool)).astype(int)<br>
4- update a labelmap volume from the new array<br>
slicer.util.updateVolumeFromArray(segmentationLblmap, arrayOR)<br>
5- save the labelmap node as a segmentation<br>
slicer.util.saveNode(segmentationLblmap, “d:/…nii.gz”)</p>
<p>Saeed</p>

---

## Post #3 by @cpinter (2023-06-19 13:03 UTC)

<p>If the previous answer is not satisfactory to you, can you please tell us more about the exact data objects? It is not clear to me. A screenshot of the Data module would suffice. No need to use an image service, just drag&amp;drop the screenshot here.</p>

---
