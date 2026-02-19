---
topic_id: 2285
title: "Single Series With Multiple Frames Separate Out"
date: 2018-03-11
url: https://discourse.slicer.org/t/2285
---

# Single series with multiple frames, separate out?

**Topic ID**: 2285
**Date**: 2018-03-11
**URL**: https://discourse.slicer.org/t/single-series-with-multiple-frames-separate-out/2285

---

## Post #1 by @mgastall (2018-03-11 00:36 UTC)

<p>I uploaded a dynamic MRI with multiple frames in one series. How do I separate these out (by trigger time?) so as to only segment on one individual frame?</p>

---

## Post #2 by @lassoan (2018-03-11 02:37 UTC)

<p>You can load 4D volumes as either multivolume nodes or volume sequence nodes - you can set how it is loaded by default in application settings / DICOM section. You can also choose how a particular sequence is loaded if you open Advanced section in DICOM browser and click Examine then select one from the listed loadables.</p>
<p>Probably volume sequence is somewhat more convenient to use, as it automatically separates out a volume. You can choose which one, by using the play/pause/prev/next buttons that appear on the toolbar. You can do further processing, such as create a 4D segmentation sequence (I can give you more instructions, if needed), compute displacement fields (to propagate segmentation from one frame to all the others fully automatically; or compute landmark point positions defined in one frame in all the other frames) by using Segment registration module.</p>
<p>Multi-volumes have some nice time series plotting capabilities and you can enable separating out a single frame by using Multi-volume explorer module.</p>

---

## Post #3 by @mgastall (2018-03-11 13:26 UTC)

<p>Thank you, that helped!</p>

---

## Post #4 by @lassoan (2024-04-24 01:24 UTC)

<p>A post was split to a new topic: <a href="/t/how-can-i-create-a-4d-segmentation-sequence/35698">How can I create a 4D segmentation sequence?</a></p>

---

## Post #5 by @Aylin (2024-08-22 11:09 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="2285">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>I can give you more instructions, if needed</p>
</blockquote>
</aside>
<p>Can you please give more detailed instructions for doing that?<br>
I have 4D volume, and I want to first rigid register the volume to atlas, and the perform skull stripping using a brain mask (from the segment editor, I am doing the following</p>
<ul>
<li>Operation: Fill outside</li>
<li>Input Volume: data</li>
<li>Output Volume: “New Masked Brain”)<br>
Now, the slicer can do this for just one of the volumes, but I want it to do this for all volumes in my multivolume data<br>
first, the rigid registration must be done to make sure that the atlas and the brain are in the same orientation, otherwise this method will not work)<br>
so can you give me more detailed instructions on how I can apply this manually</li>
</ul>

---
