---
topic_id: 2223
title: "Roi Movement Points"
date: 2018-03-02
url: https://discourse.slicer.org/t/2223
---

# ROI movement points

**Topic ID**: 2223
**Date**: 2018-03-02
**URL**: https://discourse.slicer.org/t/roi-movement-points/2223

---

## Post #1 by @stevenagl12 (2018-03-02 01:39 UTC)

<p>Is there any way that the future Slicer download could have either larger ROI control dots or at least the option for them. It is exceptionally challenging to be able to move them with the current settings when the user has poor vision.</p>

---

## Post #2 by @stevenagl12 (2018-03-02 01:41 UTC)

<p>Potentially also an option to automatically fit an ROI to the vertical, horizontal, and depth dimensions of a segmentation.</p>

---

## Post #3 by @lassoan (2018-03-02 14:45 UTC)

<p>The problem is not your vision, but high-resolution screens. ROI widget handle size is defined in pixels. I’ll update the code to size the handle relative to the window size.</p>
<p>You can fit a ROI to a volume using <code>Crop volume</code> module.</p>

---

## Post #4 by @lassoan (2018-03-02 20:10 UTC)

<p>I’ve updated the ROI widget handle sizing logic, it’ll be available in tomorrow’s build. It is now relative to the window size, independent from screen resolution. If you make the window larger then the handle gets larger, too, so it becomes even easier to hit.</p>

---

## Post #5 by @stevenagl12 (2018-03-06 02:49 UTC)

<p>What I meant wasn’t fitting the ROI to a volume, but to the dimensions of a segmentation before it is converted to a labelmap. Like if it were possible for the system to parse the file to determine the dimensions of a segmentation then apply the distances and angles to obtain an ROI for easier volume cropping.</p>

---

## Post #6 by @lassoan (2018-03-06 03:53 UTC)

<aside class="quote no-group" data-username="stevenagl12" data-post="5" data-topic="2223">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/stevenagl12/48/3391_2.png" class="avatar"> stevenagl12:</div>
<blockquote>
<p>What I meant wasn’t fitting the ROI to a volume, but to the dimensions of a segmentation before it is converted to a labelmap.</p>
</blockquote>
</aside>
<p>If you don’t specify a reference volume for exporting to labelmap (in Advanced section, set Reference volume to None), then the labelmap will be automatically cropped to the necessary size on export.</p>

---

## Post #7 by @lassoan (2023-03-21 02:56 UTC)



---
