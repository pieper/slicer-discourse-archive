---
topic_id: 31215
title: "When Adjusting The Shift Toggle For The Fetal Preset In Volu"
date: 2023-08-18
url: https://discourse.slicer.org/t/31215
---

# When adjusting the shift toggle for the fetal preset in volume rendering, what does it filter out?

**Topic ID**: 31215
**Date**: 2023-08-18
**URL**: https://discourse.slicer.org/t/when-adjusting-the-shift-toggle-for-the-fetal-preset-in-volume-rendering-what-does-it-filter-out/31215

---

## Post #1 by @Seasapro (2023-08-18 07:19 UTC)

<p>Hello,<br>
I have been using the 3D Slicer software for sediment core CT scans and found that the easiest to view is typically the fetal preset in volume rendering. I am trying to find wood or terrestrial debris and was wondering, how does the shift adjuster/toggle filter out items within the CT scan, or is there a better way to filter for something like this (such as a density filter)? Also if you know of a preset that may work better feel free to let me know! Thanks in advance</p>

---

## Post #2 by @lassoan (2023-08-18 20:57 UTC)

<p>By moving the shift slider to the right, you make regions that are less dense to appear more transparent. You can achieve richer, more nuanced visualization by editing the transfer functions in the “Advanced” section of the Volume rendering module.</p>

---

## Post #3 by @Seasapro (2023-08-24 20:19 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="31215">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>e shift slider to the right, you make regions that are less dense to appear more transparent. You can achieve richer, more nuanced visualization by editing the transfer functions in the “Advanced” section of the Volume rendering module.</p>
</blockquote>
</aside>
<p>Is there a way to make the higher density areas appear more transparent? Maybe even a function that would invert the original properties and then I could run it through the volume rendering again and that way when I move the shift slider to the right I am making the lower density areas become more apparent.</p>

---
