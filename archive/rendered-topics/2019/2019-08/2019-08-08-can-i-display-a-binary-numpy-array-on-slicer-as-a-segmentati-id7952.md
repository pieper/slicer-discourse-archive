# Can I display a binary numpy array on Slicer as a segmentation volume?

**Topic ID**: 7952
**Date**: 2019-08-08
**URL**: https://discourse.slicer.org/t/can-i-display-a-binary-numpy-array-on-slicer-as-a-segmentation-volume/7952

---

## Post #1 by @ISJ0392 (2019-08-08 21:43 UTC)

<p>I have a numpy array with dimensions 512 * 512 * 64 * 5. This represents 5 3D arrays, and the arrays have only 1 or 0 values representing voxels in a segmentation volume. Is there anyway I can display this saved .npy file to see the 3D segmentations in Slicer? Is there a way for me todo this without slicer?</p>
<p>Apologies if this is a simple and has been asked elsewhere but im relatively new to slicer and from what I can see people have asked questions todo the opposite (convert segmentation to npy and not the other way around)</p>

---

## Post #2 by @ISJ0392 (2019-08-09 01:39 UTC)

<p>The question I have is the opposite to the question in : <a href="https://discourse.slicer.org/t/segment-binarylabelmap-to-numpy-array/778" class="inline-onebox">Segment / BinaryLabelMap to numpy array</a></p>
<p>I think this user is asking how to get the numpy array from the .seg.nrrd. I want to know how to get a numpy array and convert it to a .sseg.nrrd format that slicer can work with</p>

---

## Post #3 by @lassoan (2019-08-10 18:09 UTC)

<p>The simplest is probably to create a <a href="https://apidocs.slicer.org/master/classvtkMRMLLabelMapVolumeNode.html" rel="nofollow noopener">labelmap volume node</a>, set its voxels from a numpy array using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray" rel="nofollow noopener">slicer.util.updateVolumeFromArray</a>, and convert into a segmentation node using <a href="https://discourse.slicer.org/t/import-labelmap-to-segmentation-node-in-batch-processing/2360/10">ImportLabelmapToSegmentationNode</a>.</p>

---
