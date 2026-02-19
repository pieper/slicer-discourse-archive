---
topic_id: 38257
title: "Adding New Segments From Multiple Numpy Arrays"
date: 2024-09-06
url: https://discourse.slicer.org/t/38257
---

# Adding new segments from multiple numpy arrays

**Topic ID**: 38257
**Date**: 2024-09-06
**URL**: https://discourse.slicer.org/t/adding-new-segments-from-multiple-numpy-arrays/38257

---

## Post #1 by @roboted (2024-09-06 10:16 UTC)

<p>Hello,</p>
<p>I am working on importing numpy arrays into a segmentation so that they are shown in the segment editor as new segments.</p>
<p>What I have now after seeing some examples is:</p>
<pre><code class="lang-auto">label_map_volume = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode")
slicer.util.updateVolumeFromArray(label_map_volume, segmentation_mask)
slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(label_map_volume, segmentation_node)
slicer.util.updateSegmentBinaryLabelmapFromArray(
            segmentation_mask, 
            segmentation_node, 
            label_map_volume.GetName(), 
            self.volume_node)
slicer.mrmlScene.RemoveNode(label_map_volume)
</code></pre>
<p>Where <code>segmentation_node</code> is the numpy array with the new segment to be added to the segmentation and self.volume_node.</p>
<p>The problem is that every segment adds to memory about as much as the volume size, as if the whole array is saved and shown, so after ~20 to 30 segments Slicer slows down. I considered using a single array to store all the segmentations because overlapping is not a problem, but I do not know if Slicer works more efficiently than this under the hood and this approach is not optimal. I assume this is not a memory leak because the label map node is deleted once the segmentation has been updated. What is the best option from here?</p>
<p>Thank you for the help.</p>

---

## Post #2 by @cpinter (2024-09-06 10:51 UTC)

<p>Slicer is in fact more efficient than storing the entire extent as many times as the number of segments. Originally, each segment only took as much space as its actual content. Later, a “layer” mechanism was introduced to make this even more efficient, however, I am not super familiar with the implementation of this part. I assume the numpy importer takes the simplest approach possible, and the effective extents and layers are not considered. I’d try to call <code>segmentation_node.GetSegmentation().CollapseBinaryLabelmaps()</code> and see if it solves the issue.</p>

---

## Post #3 by @roboted (2024-09-06 11:20 UTC)

<p>This seems to solve the issue. Now only a very small amount of memory is taken for each new segment. Thank you!</p>

---
