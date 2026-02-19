---
topic_id: 13827
title: "How To Overwrite Part Of The Selected Label Map"
date: 2020-10-02
url: https://discourse.slicer.org/t/13827
---

# How to overwrite part of the selected label map

**Topic ID**: 13827
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/how-to-overwrite-part-of-the-selected-label-map/13827

---

## Post #1 by @yuantinghsieh (2020-10-02 20:12 UTC)

<p>I am working on AIAA slicer plugin right now.</p>
<p>I want to overwrite just part of the selected label map. (As our model only inference on a specific bounding box so I don’t want to modify the label map that is outside this bounding box.)</p>
<p>I think the following code works but it is extremely slow, can you suggest a faster/cleaner way of doing this?</p>
<pre><code class="lang-auto"># Just update segment label map within the crop box
selectedSegmentLabelmap = self.scriptedEffect.selectedSegmentLabelmap()
count = 0
for x in range(cropBox[0][0], cropBox[0][1]):
    for y in range(cropBox[1][0], cropBox[1][1]):
        for z in range(cropBox[2][0], cropBox[2][1]):
            v = selectedSegmentLabelmap.GetScalarComponentAsDouble(x, y, z, 0)
            if v:
                count = count + 1
            selectedSegmentLabelmap.SetScalarComponentFromDouble(x, y, z, 0, 0)

# Clear the box
if count:
    self.scriptedEffect.modifySelectedSegmentByLabelmap(
        selectedSegmentLabelmap,
        slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeSet)

# Union label map
self.scriptedEffect.modifySelectedSegmentByLabelmap(
    labelmap,
    slicer.qSlicerSegmentEditorAbstractEffect.ModificationModeAdd)
</code></pre>
<p>The label map is given by the following code (in_file is our returned result):</p>
<pre><code class="lang-auto">segmentationNode = self.scriptedEffect.parameterSetNode().GetSegmentationNode()
segmentation = segmentationNode.GetSegmentation()
currentSegment = self.currentSegment()

labelImage = sitk.ReadImage(in_file)
labelmapVolumeNode = sitkUtils.PushVolumeToSlicer(labelImage, None, className='vtkMRMLLabelMapVolumeNode')

numberOfExistingSegments = segmentation.GetNumberOfSegments()
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, segmentationNode)
slicer.mrmlScene.RemoveNode(labelmapVolumeNode)

# Copy labelmap representation to the current segment then remove the imported segment
labelmap = slicer.vtkOrientedImageData()
segmentationNode.GetBinaryLabelmapRepresentation(segmentId, labelmap)
</code></pre>
<p>Similar to the 2D implementation in here: <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/slicer-plugin/NvidiaAIAA/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py#L263-L286" rel="noopener nofollow ugc">https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/slicer-plugin/NvidiaAIAA/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py#L263-L286</a><br>
But we want a 3D way.</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-10-03 00:11 UTC)

<p>Wow, this implementation is extremely inefficient. It may be 1000x slower than it should be normally. In Python, processing should never be done by iterating through each voxel. Instead, you can get the image as numpy array and operate on the entire 3D region at once.</p>

---

## Post #3 by @yuantinghsieh (2020-10-07 05:41 UTC)

<p>Thanks for the hint.<br>
After some search here and there I’ve found a way that works for my application.</p>
<pre><code>        labelmapArray = slicer.util.arrayFromVolume(labelmapVolumeNode)
        new_array = np.zeros_like(labelmapArray)
        # because numpy is in KJI
        # https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_centroid_of_a_segment_in_world_.28RAS.29_coordinates
        box_slice = tuple([slice(x[0], x[1]) for x in cropBox][::-1])
        currentLabelmapArray = slicer.util.arrayFromSegmentBinaryLabelmap(segmentationNode,
                                                                          self.currentSegmentID())
        currentLabelmap = slicer.vtkOrientedImageData()
        segmentationNode.GetBinaryLabelmapRepresentation(self.currentSegmentID(), currentLabelmap)
        segImageExtent = currentLabelmap.GetExtent()
        if np.sum(currentLabelmapArray) != 0:
            extent_slice = tuple([slice(segImageExtent[i], segImageExtent[i+1] + 1) for i in range(0, 5, 2)][::-1])
            new_array[extent_slice] = currentLabelmapArray
        new_array[box_slice] = labelmapArray[box_slice]
        slicer.util.updateVolumeFromArray(labelmapVolumeNode, new_array)
        slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(labelmapVolumeNode, segmentationNode)
        slicer.mrmlScene.RemoveNode(labelmapVolumeNode)</code></pre>

---
