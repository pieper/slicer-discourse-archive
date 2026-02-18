# Setting segmentation in SegmentEditor without changing volumes in slice views

**Topic ID**: 22977
**Date**: 2022-04-15
**URL**: https://discourse.slicer.org/t/setting-segmentation-in-segmenteditor-without-changing-volumes-in-slice-views/22977

---

## Post #1 by @vanossj (2022-04-15 17:48 UTC)

<p>I’ve setup 3DSlicer to load different volumes in different slice views, red, green, etc. There are also a separate segmentation node for each of these volumes. These segmentation nodes are displayed only on the slice views that display the master volume for the segmentation.</p>
<p>If I use the SegmentEditor module UI to change the segmentation node, all the slice views are changed have the background volume changed to the master volume for the newly selected segmentation node. If I programmatically use slicer.util.getNode(“SegmentEditor”).SetAndObserveSegmentationNode(segmentationNode), it has the same effect of changing all the view volumes.</p>
<p>How can I change the active segmentation in the SegmentEditor module without changing all the setup I’ve done to the slice views?</p>

---

## Post #2 by @lassoan (2022-04-15 18:18 UTC)

<p>The new master volume is only shown in those views where the segmentation node is visible (based on view node IDs set in the segmentation’display node).</p>
<p>You can also disable automatic showing of the matter volume in slice views by turning off<br>
<a href="http://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a107962cc9a61cd6353b15284e427d646">autoShowMasterVolumeNode</a> property of the segment editor widget.</p>

---

## Post #3 by @vanossj (2022-04-15 19:47 UTC)

<p>Thanks, That works. I was running into the issue where if you switch to a segmentation that is not visible in any views, 3DSlicer will change all the views to that master volume node</p>

---

## Post #4 by @lassoan (2022-04-16 12:59 UTC)

<aside class="quote no-group" data-username="vanossj" data-post="3" data-topic="22977">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vanossj/48/15008_2.png" class="avatar"> vanossj:</div>
<blockquote>
<p>you switch to a segmentation that is not visible in any views</p>
</blockquote>
</aside>
<p>Not seeing any view IDs means the segmentation appears in every views. If you want a segmentation to not appear in any view then you can set some non-existing view node ID in the display node (or turn off visibility in all its display nodes, or remove all its display nodes).</p>

---
