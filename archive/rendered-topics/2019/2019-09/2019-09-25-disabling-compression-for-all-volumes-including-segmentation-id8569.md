# Disabling compression for all volumes (including segmentations)

**Topic ID**: 8569
**Date**: 2019-09-25
**URL**: https://discourse.slicer.org/t/disabling-compression-for-all-volumes-including-segmentations/8569

---

## Post #1 by @muratmaga (2019-09-25 19:46 UTC)

<p>I am trying to use the sample script <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_file_type_for_nodes_.28that_have_never_been_saved_yet.29" class="inline-onebox">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></p>
<p>to disable compression for all volume types by putting this example to my .slicerrc.py</p>
<blockquote>
<p><span class="hashtag-raw">#set</span> the default volume storage to not compress by default<br>
defaultVolumeStorageNode = slicer.vtkMRMLVolumeArchetypeStorageNode()<br>
defaultVolumeStorageNode.SetUseCompression(0)<br>
slicer.mrmlScene.AddDefaultNode(defaultVolumeStorageNode)<br>
logging.info(“Volume nodes will be stored uncompressed by default”)</p>
</blockquote>
<p>But this doesn’t disable compression for segmentation nodes (download MrHead.nrrd, create a segment and see in the save as dialog box that while compression is unchecked for MRHead.nrrd, it is still enabled for _seg.nrrd segmentation volume).</p>
<p>There is another snippet that disables compression specifically for segmentations,</p>
<blockquote>
<p><span class="hashtag-raw">#set</span> the default volume storage to not compress by default<br>
defaultVolumeStorageNode = slicer.vtkMRMLSegmentationStorageNode()<br>
defaultVolumeStorageNode.SetUseCompression(0)<br>
slicer.mrmlScene.AddDefaultNode(defaultVolumeStorageNode)<br>
logging.info("Segmentation nodes will be stored uncompressed</p>
</blockquote>
<p>But I want to do it for both volumes and segmentation, is that possible?</p>

---

## Post #2 by @lassoan (2019-09-25 19:48 UTC)

<p>Yes, of course, you can define default nodes for any number of node types.</p>

---

## Post #3 by @muratmaga (2019-09-25 20:01 UTC)

<p>Yes, actually just including both snippets in the same .slicerrc.py worked. I thought the second setting defaultVolumeStorageNode  a second time would overwrite. But works great.</p>

---
