# Connecting two or more volumes

**Topic ID**: 9922
**Date**: 2020-01-23
**URL**: https://discourse.slicer.org/t/connecting-two-or-more-volumes/9922

---

## Post #1 by @tkt8 (2020-01-23 15:56 UTC)

<p>I am developing an extension for slicer. I wanted to compare the original volume and the modified volume. Is there a way to link the two so that I can mimic the action such as say segmentation done in original volume is reflected in the new volume so that i can compare them side by side.<br>
Thanks</p>

---

## Post #2 by @lassoan (2020-01-28 04:45 UTC)

<p>Sorry for the late answer, many of us very very busy at the Slicer project week last week.</p>
<aside class="quote no-group" data-username="tkt8" data-post="1" data-topic="9922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tkt8/48/5758_2.png" class="avatar"> tkt8:</div>
<blockquote>
<p>I wanted to compare the original volume and the modified volume</p>
</blockquote>
</aside>
<p>Would you like to just show the two volumes side-by-side and pan/zoom them in sync? You can do that by enabling hot-link by long-click on the slice view link icon.</p>
<aside class="quote no-group" data-username="tkt8" data-post="1" data-topic="9922">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tkt8/48/5758_2.png" class="avatar"> tkt8:</div>
<blockquote>
<p>Is there a way to link the two so that I can mimic the action such as say segmentation done in original volume is reflected in the new volume</p>
</blockquote>
</aside>
<p>The two volume nodes and the segmentation node are three separate nodes. Would you like to just show the same segmentation over two different volumes?</p>

---

## Post #3 by @tkt8 (2020-02-04 16:13 UTC)

<p>Thanks for help. Yes I would like to show the same segmentation over 2 or more different volumes</p>

---

## Post #4 by @lassoan (2020-02-04 16:35 UTC)

<p>Segmentations are shown by default in all views. To show different volumes in each slice view, click the push-pin icon in the top-left corner of the slice view then choose a volume to be shown in that view by using the node selector on the right. See more details in the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Data_Loading_and_3D_Visualization">Data loading and visualization tutorial</a>.</p>

---

## Post #5 by @tkt8 (2020-02-26 17:26 UTC)

<p>I want to have the same segmentation in two different volumes. Is there a way to do this?</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2020-02-26 18:07 UTC)

<p>Segmentation nodes are independent from volume nodes, so they are not “in volumes”. You can export segmentations to labelmap volumes that match geometry (origin, spacing, axis directions, extents) of an existing volume using Segmentations module, Import/Export section. Choose the reference volume to be the volume that you want to match the geometry of.</p>

---

## Post #7 by @tkt8 (2020-02-28 13:10 UTC)

<p>Thank you for helping me. Is there a tutorial I can follow for this?</p>

---

## Post #8 by @lassoan (2020-02-28 16:38 UTC)

<p>You can find segmentation tutorials here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation</a></p>

---
