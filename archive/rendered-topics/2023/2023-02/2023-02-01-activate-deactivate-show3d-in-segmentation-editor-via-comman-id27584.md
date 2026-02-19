---
topic_id: 27584
title: "Activate Deactivate Show3D In Segmentation Editor Via Comman"
date: 2023-02-01
url: https://discourse.slicer.org/t/27584
---

# Activate/deactivate "show3d" in Segmentation Editor via command line

**Topic ID**: 27584
**Date**: 2023-02-01
**URL**: https://discourse.slicer.org/t/activate-deactivate-show3d-in-segmentation-editor-via-command-line/27584

---

## Post #1 by @Nicolas_Tempier (2023-02-01 15:23 UTC)

<p>Hello !<br>
I am trying to dispaly a segmentation in the 3D view using the python interactor but i cant find the command to activate/deactivate the equivalent of “show 3D” in segmentation Editor.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c935f837363f9b230e611d6ad352fadea7905a7.png" alt="image" data-base62-sha1="hM2X0vxbdTnzwK2WWCIXhpuyGzl" width="194" height="54"></p>
<p>for now i’ve tried :<br>
segmentation = slicer.util.getNode(‘TC4_RH_ctg_mask.nii.gz’)<br>
segmentationDisplayNode = segmentation.GetDisplayNode()<br>
segmentationDisplayNode.SetSliceIntersectionVisibility(True)<br>
segmentationDisplayNode.SetVisibility(True)</p>
<p>but it does not change the 3d display of the segment.<br>
Thanks in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Nicolas</p>

---

## Post #2 by @ebrahim (2023-02-01 15:41 UTC)

<p>The missing ingredient is <code>CreateClosedSurfaceRepresentation()</code></p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-segmentation-in-3d" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a></p>

---

## Post #3 by @Nicolas_Tempier (2023-02-01 16:04 UTC)

<p>Amazing thanks ! it works perfectely fine <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
Nicolas</p>

---

## Post #4 by @bserrano (2023-09-21 12:20 UTC)

<aside class="quote no-group" data-username="Nicolas_Tempier" data-post="1" data-topic="27584">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nicolas_tempier/48/17463_2.png" class="avatar"> Nicolas_Tempier:</div>
<blockquote>
<p>segmentationDisplayNode = segmentation.GetDisplayNode()<br>
segmentationDisplayNode.SetSliceIntersectionVisibility(True)<br>
segmentationDisplayNode.SetVisibility(True)</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>This is not working in version 5.4.0 because of:</p>
<p><code>'vtkSegmentationCorePython.vtkSegmentation' object has no attribute 'GetDisplayNode'</code></p>
<p>How can I do it in this version?</p>
<p>Thanks.</p>

---

## Post #5 by @pieper (2023-09-21 13:14 UTC)

<p><code>GetDisplayNode</code> is for <code>vtkMRMLSegmentationNode</code> (as returned by <code>getNode</code>) not <code>vtkSegmentation</code>.  There are several layers, but they make sense to keep the methods localized by dependencies (<code>vtkSegmentation</code> doesn’t know about <code>MRML</code> so it can be used more generally in the future).</p>

---
