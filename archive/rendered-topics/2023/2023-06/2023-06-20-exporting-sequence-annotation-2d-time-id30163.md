# Exporting sequence annotation (2d + time)

**Topic ID**: 30163
**Date**: 2023-06-20
**URL**: https://discourse.slicer.org/t/exporting-sequence-annotation-2d-time/30163

---

## Post #1 by @cams2b (2023-06-20 18:26 UTC)

<p>I am a new user of 3d slicer and I am working on segmenting 2d + time sequences. I have successfully annotated the sequences and I have saved the annotations as sequence files. I am now trying to export the annotations to either DICOM, NIFTI, or nrrd files however when I export the annotation it appears to export only a single point in the sequence.</p>
<p>I have previously read that this can be accomplished using a python script which I have attempted to do, however I am unaware of how I can access the segmentation sequence node using the API. I will include the python code that I am currently using below. It</p>
<pre><code class="lang-auto">import numpy as np
sequenceNode = slicer.mrmlScene.GetFirstNodeByClass("vtkMRMLSequenceNode") 
dims = slicer.util.arrayFromVolume(sequenceNode.GetNthDataNode(0)).shape
print(dims)
print(sequenceNode.GetNumberOfDataNodes())

voxelArray = np.zeros([dims[0], dims[1], dims[2], sequenceNode.GetNumberOfDataNodes()])
print(voxelArray.shape)
for volumeIndex in range(sequenceNode.GetNumberOfDataNodes()):
    voxelArray[:, :, :, volumeIndex] = slicer.util.arrayFromVolume(sequenceNode.GetNthDataNode(volumeIndex))

print("Done")
</code></pre>
<p>Any help is greatly appreciated</p>

---
