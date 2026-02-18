# Get parent of segmentation Node

**Topic ID**: 16010
**Date**: 2021-02-16
**URL**: https://discourse.slicer.org/t/get-parent-of-segmentation-node/16010

---

## Post #1 by @LaurennLam (2021-02-16 15:00 UTC)

<p>Hi there,<br>
I’d like to k now how I can get the parent of a segmentation.<br>
I have a vtkMRMLScalarVolumeNode and created a Segmentation for this scalarVolume (With the user interface). But I’d like to know how I can get the vtkMRMLScalarVolumeNode from the vtkMRMLSegmentationNode programatically ?<br>
I thought it was the storageNode but it doesn’t seem to be this.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-02-16 15:16 UTC)

<p>You can use many scalar volumes to create a segmentation, so there is no strict correspondence between segmentation and one scalar volume.</p>
<p>You can <a href="http://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html#ae7dbe89f755f115624dc1c701e9dcf80">get the current master volume</a> that is selected in the segment editor node.</p>
<p>You can also get the volume node that was used to initialize geometry of the segmentation (typically the first volume you selected as master volume):</p>
<pre><code class="lang-python">referenceVolumeNode = segmentationNode.GetNodeReferenceID(
  slicer.vtkMRMLSegmentationNode.GetReferenceImageGeometryReferenceRole())
</code></pre>

---

## Post #3 by @LaurennLam (2021-02-16 15:29 UTC)

<p>I just tried the second solution but it returns an empty node.<br>
I don’t want to use the segment editor node as I can have the situation where I load a mrmlScene with segmentation.<br>
But when we are in the data panel and you click on a segmentation, it highlights the volume used to create the segmentation. Is it what the second solution should do ?</p>

---

## Post #4 by @LaurennLam (2021-02-16 15:31 UTC)

<p>My bad! I used bad data to test it. It perfectly works and does what I want. Thanks !</p>

---

## Post #5 by @pieper (2021-02-16 16:58 UTC)

<p>We should consider tracking all the volumes that were used as master volumes during creation of a segmentation so that all could be listed in a dicom export.</p>

---
