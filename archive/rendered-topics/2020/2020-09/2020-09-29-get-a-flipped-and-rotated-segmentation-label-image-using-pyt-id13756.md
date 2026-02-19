---
topic_id: 13756
title: "Get A Flipped And Rotated Segmentation Label Image Using Pyt"
date: 2020-09-29
url: https://discourse.slicer.org/t/13756
---

# Get a flipped and rotated segmentation label image using python script

**Topic ID**: 13756
**Date**: 2020-09-29
**URL**: https://discourse.slicer.org/t/get-a-flipped-and-rotated-segmentation-label-image-using-python-script/13756

---

## Post #1 by @N_Hunter (2020-09-29 18:36 UTC)

<p>Hi, there, I recently use python script to export segmentations to labelmap and save it on the disk, to save some clicks. But instead, I get a rotated and flipped labelmap, like below:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c85afe3ea5f1c1515d4e09dd0dc128709e74654b.png" alt="9" data-base62-sha1="sAqrEqprAnUwTNptT0HmLzJ07Fh" width="320" height="320"></p>
<p>This should be a “4”, but instead, it was flipped and rotated “4”. I’ve tried both to save labelmap in nii.gz and nrrd format, all gives me the same result.</p>
<p>Here is my code:</p>
<pre><code class="lang-auto">def extract_label(mrml_fp):
   # load mrml file
   slicer.util.loadScene(mrml_fp)

    # access manually annotated label
   segs = slicer.util.getNodesByClass('vtkMRMLSegmentationNode')

   # master volume
   volume_node = slicer.util.getNodesByClass('vtkMRMLScalarVolumeNode')

   if len(segs) != 1:
       raise "the number of segmentation node shoule be 1"

   annoted_segment_node = segs[0]
   annoted_seg = annoted_segment_node.GetSegmentation()

   # iterate through all the segments
   num_segments = annoted_seg.GetNumberOfSegments()

   for idx in range(num_segments):

      # create new segmentation node
      new_segement_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLSegmentationNode')
      new_segement_node.CreateDefaultDisplayNodes()
   new_segement_node.SetReferenceImageGeometryParameterFromVolumeNode(volume_node[0])

      # add segment to new segmentation node
      segment = annoted_seg.GetNthSegment(idx)
      segment_name = segment.GetName()
      new_segement_node.GetSegmentation().AddSegment(segment)

      # export segmentation node to labelmap
      labelmap_volume_node = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLLabelMapVolumeNode')
      slicer.modules.segmentations.logic().ExportVisibleSegmentsToLabelmapNode(new_segement_node, labelmap_volume_node, volume_node[0])

      # save labelmap to disk
      dest_folder = os.path.dirname(mrml_fp)
      slicer.util.saveNode(labelmap_volume_node, os.path.join(dest_folder, "{}.nrrd".format(segment_name)))

      # remove created segmentation node
      slicer.mrmlScene.RemoveNode(labelmap_volume_node)
      slicer.mrmlScene.RemoveNode(new_segement_node)

   # clear scene
   slicer.mrmlScene.Clear(0)
</code></pre>
<p>Could you please tell me where I went wrong?</p>

---
