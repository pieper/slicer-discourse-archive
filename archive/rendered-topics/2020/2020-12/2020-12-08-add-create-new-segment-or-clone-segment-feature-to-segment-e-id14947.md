---
topic_id: 14947
title: "Add Create New Segment Or Clone Segment Feature To Segment E"
date: 2020-12-08
url: https://discourse.slicer.org/t/14947
---

# Add "Create new segment" or "Clone segment" feature to Segment Editor

**Topic ID**: 14947
**Date**: 2020-12-08
**URL**: https://discourse.slicer.org/t/add-create-new-segment-or-clone-segment-feature-to-segment-editor/14947

---

## Post #1 by @muratmaga (2020-12-08 19:53 UTC)

<p>Would it be possible to modify the Segment Editor effects such that:</p>
<ol>
<li>Output of a segmentation can be set as a new segment as oppose to changing the existing one. For example a setting of “Modify other segments” can be “Create a new segment”.</li>
<li>If this is not possible or feasible, can there be a right click behavior such that a clone of a segment can be created directly from the Segment Editor (as oppose to click add and then use copy from logical operations).</li>
</ol>
<p>I think these two would make life easier for user who wants to compare how certain effects modify their data (e.g., smoothing, margin operations etc).</p>

---

## Post #2 by @lassoan (2020-12-08 20:12 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="14947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I think these two would make life easier for user who wants to compare how certain effects modify their data (e.g., smoothing, margin operations etc).</p>
</blockquote>
</aside>
<p>You can already inspect the difference with/without the last operation, without any extra steps of manually adding/removing copies of segments, by using undo/redo.</p>
<p>There is also a right-click menu option (in Data module) to clone a segmentation.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="14947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Output of a segmentation can be set as a new segment as oppose to changing the existing one. For example a setting of “Modify other segments” can be “Create a new segment”.</p>
</blockquote>
</aside>
<p>An editing operation could affect many segments, so I don’t think there is general way of creating a new segment. You would need to create a completely new segmentation (which you can already do).</p>
<aside class="quote no-group" data-username="muratmaga" data-post="1" data-topic="14947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>If this is not possible or feasible, can there be a right click behavior such that a clone of a segment can be created directly from the Segment Editor (as oppose to click add and then use copy from logical operations).</p>
</blockquote>
</aside>
<p>Adding a “Clone segment” option would not be hard, but probably this would not work well in general, because it would force the user to switch to “Allow overlap” mode. This would interfere with the segmentation editing. Instead, for comparison, it is better to create independent segmentations, by cloning the segmentation node (right-click in Data module).</p>
<p>With the new way of setting view content by drag-and-drop from Data module to viewers, it is now much easier to set up node comparison in side-by-side views.</p>

---

## Post #3 by @muratmaga (2020-12-08 20:52 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can already inspect the difference with/without the last operation, without any extra steps of manually adding/removing copies of segments, by using undo/redo.</p>
</blockquote>
</aside>
<p>But I can’t see pre/post at the same time that’s the issue using undo/redo.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Instead, for comparison, it is better to create independent segmentations, by cloning the segmentation node (right-click in Data module).</p>
</blockquote>
</aside>
<p>True, but it is harder to manipulate the visibility of individual segmentations, then it is to manipulate segments.  It also requires actively switching to different segmentations in Segment Editor when you trying to experiment with different filters.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="14947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>With the new way of setting view content by drag-and-drop from Data module to viewers, it is now much easier to set up node comparison in side-by-side views.</p>
</blockquote>
</aside>
<p>I remember your demo of this, but it is not in the latest stable. Is it in the preview?</p>

---

## Post #4 by @lassoan (2020-12-08 21:18 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="14947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>But I can’t see pre/post at the same time that’s the issue using undo/redo.</p>
</blockquote>
</aside>
<p>Undo/redo is very fast and they are available using keyboard shortcuts (z/y). Since only one version is shown at a time, you can see the difference much more clearly than on two overlapping segments.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="14947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>it is harder to manipulate the visibility of individual segmentations, then it is to manipulate segments</p>
</blockquote>
</aside>
<p>Manipulating visibility is not enough. You need to change the color or showing thick outline only. Otherwise you would not see the difference clearly. So, you need to go to Segmentations or Data module the same way as you would do for cloning the entire segmentation.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="14947">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>I remember your demo of this, but it is not in the latest stable. Is it in the preview?</p>
</blockquote>
</aside>
<p>Yes, it is in the latest preview - see <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#selecting-displayed-data">documentation</a>.<br>
<a href="https://discourse.slicer.org/tag/feature">New feature post</a> will go out tomorrow (I’ve pushed two small fixes today).</p>
<hr>
<p>I agree that it takes extra effort to go to Data module, clone the segmentation, change its display properties; and when done with the comparison then go back to Data module and delete it. So, if this comes up often and undo/redo is not sufficient then you can implement it in a Segment Editor effect. It would be similar to the preview feature in “Grow from seeds” effect and be distributed in an extension similarly to the <a href="https://github.com/lassoan/SlicerAutoscroll">Autoscroll effect</a>.</p>

---
