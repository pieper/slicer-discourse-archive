---
topic_id: 13231
title: "Get Labelmap From Each Segment Separately"
date: 2020-08-29
url: https://discourse.slicer.org/t/13231
---

# Get labelmap from each segment separately?

**Topic ID**: 13231
**Date**: 2020-08-29
**URL**: https://discourse.slicer.org/t/get-labelmap-from-each-segment-separately/13231

---

## Post #1 by @44REAM (2020-08-29 10:57 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54a105a5d38492dfa6aac90791e556a750dc9ab7.png" data-download-href="/uploads/short-url/c4F5VQrT9Y9MKG22k1jLiReq5pB.png?dl=1" title="label" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54a105a5d38492dfa6aac90791e556a750dc9ab7_2_690x59.png" alt="label" data-base62-sha1="c4F5VQrT9Y9MKG22k1jLiReq5pB" width="690" height="59" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54a105a5d38492dfa6aac90791e556a750dc9ab7_2_690x59.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/4/54a105a5d38492dfa6aac90791e556a750dc9ab7_2_1035x88.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/4/54a105a5d38492dfa6aac90791e556a750dc9ab7.png 2x" data-dominant-color="303230"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">label</span><span class="informations">1255×109 9.57 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I try to convert segmentation to labelmap separately from cli (eg labelmap of body, lung_L and lung_R separately). I found that this code below can export visable segment to labelmap.</p>
<pre><code>seg = getNode(‘Segmentation’)
reference = getNode (‘InputVolume’) # this will be the volume the segmentation was drawn on
labelmapVolumeNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLLabelMapVolumeNode’)

ids = vtk.vtkStringArray()
seg.GetDisplayNode().GetVisibleSegmentIDs(ids)
slicer.modules.segmentations.logic().ExportSegmentsToLabelmapNode(seg, ids, labelmapVolumeNode, reference)
</code></pre>
<p>But how can I turn visible on or off from cli, or there other method to export labelmap separately from cli?.</p>

---

## Post #2 by @lassoan (2020-08-29 14:11 UTC)

<p>You can change visibility of a segment by using <a href="https://github.com/Slicer/Slicer/blob/master/Libs/MRML/Core/vtkMRMLSegmentationDisplayNode.h#L205"><code>SetSegmentVisibility</code></a> method of the segmentation display node.</p>
<p>However, it is probably easier and faster to get all segments at once, as a numpy array, and then use standard numpy operations to extract/recolor a chosen all voxel that have a particular value (see for <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Mask_volume_using_segmentation">this example</a> to mask a scalar volume - you can mask a labelmap volume the same way).</p>

---

## Post #3 by @mangotee (2020-08-31 10:49 UTC)

<p>There is another simple way to accomplish this with an in-built function from <code>vtkSlicerSegmentationsModuleLogic</code>, which I’ve been using recently, and which circumvents segment visibilites entirely. Example code is below - if you need to convert regions one-by-one and separately, use lists of length 1 (e.g. [“background”], [“prostate”], [“tumor”]) instead of a list with multiple regions ([“background”, “prostate”, “tumor”]):</p>
<pre><code># nseg ... segmentation node
# nvol ... volume reference node of the segmentation 
# nlab ... node of the target labelmap (will adopt the geometry of nvol)
# listSegmentNames ... a list of strings with segment names to be included
#                      in the labelmap (for single-region: a string list of len 1)

# Convert list of segment names to a vtkStringArray of segment IDs
strarr = vtk.vtkStringArray()
for sname in listSegmentNames:
    sid = nseg.GetSegmentation().GetSegmentIdBySegmentName(sname)
    strarr.InsertNextValue(sid)
# Export the list of segments to a labelmap
slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsToLabelmapNode(nseg, strarr, nlab, nvol)</code></pre>

---
