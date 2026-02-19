---
topic_id: 36864
title: "What Method Comes Closest To Region Growing"
date: 2024-06-18
url: https://discourse.slicer.org/t/36864
---

# What method comes closest to region growing?

**Topic ID**: 36864
**Date**: 2024-06-18
**URL**: https://discourse.slicer.org/t/what-method-comes-closest-to-region-growing/36864

---

## Post #1 by @koenterheegde (2024-06-18 13:24 UTC)

<p>I have developed my own region growing algorithm for segmentation and wanted to compare it to region growing in this software, but there is no region growing method available? The Local threshold option comes close, but which algorithm for the flood filling would come most close to region growing? Masking, grow cut or watershed?</p>
<p>The grow from seeds method sounds similar, but you have to select foreground and background and also for a lot of slices in order to make it work. This is not the same as a region growing algorithm.</p>
<p>Any other ideas?</p>

---

## Post #2 by @chir.set (2024-06-18 13:42 UTC)

<aside class="quote no-group" data-username="koenterheegde" data-post="1" data-topic="36864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/67e7ee/48.png" class="avatar"> koenterheegde:</div>
<blockquote>
<p>my own region growing algorithm</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="koenterheegde" data-post="1" data-topic="36864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/k/67e7ee/48.png" class="avatar"> koenterheegde:</div>
<blockquote>
<p>compare it to region growing in this software</p>
</blockquote>
</aside>
<p>May be you could compare with the algorithms used in the ‘Simple region growing segmentation’ module. I used this of old, before the ‘Segment editor’ matured, with the ‘Segment editor extra effects’ extension above all.</p>

---

## Post #3 by @koenterheegde (2024-06-18 13:50 UTC)

<p>Oh wow, I didn’t even know this module existed! I can’t really find any video’s about however. How could I now place seed points?</p>

---
