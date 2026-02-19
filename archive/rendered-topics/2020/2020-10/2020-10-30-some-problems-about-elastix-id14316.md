---
topic_id: 14316
title: "Some Problems About Elastix"
date: 2020-10-30
url: https://discourse.slicer.org/t/14316
---

# Some problems about elastix

**Topic ID**: 14316
**Date**: 2020-10-30
**URL**: https://discourse.slicer.org/t/some-problems-about-elastix/14316

---

## Post #1 by @slicer365 (2020-10-30 00:30 UTC)

<p>Hello, teacher, during the process of using Elastix registration, according to the default settings, after the configuration is completed, a part of the new CT image is automatically cropped. For example, I use CT to match MR. MR is only half a head scan , CT is a whole brain scan, and the newly generated CT after registration is only half of the head. How to solve this problem? Can you give me detailed steps, thank you very much! In addition, I failed to use MR to register CT.</p>
<blockquote>
<p>Blockquote</p>
</blockquote>

---

## Post #2 by @lassoan (2020-10-30 04:13 UTC)

<aside class="quote no-group" data-username="slicer365" data-post="1" data-topic="14316">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>the newly generated CT after registration is only half of the head</p>
</blockquote>
</aside>
<p>If you want to transform the full volume (and not resample one volume in the other volume’s grid) then choose an output transform in Elastix module. When the registration is completed, the computed transform will be automatically applied it to the moving volume.</p>
<aside class="quote no-group" data-username="slicer365" data-post="1" data-topic="14316">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/slicer365/48/67549_2.png" class="avatar"> slicer365:</div>
<blockquote>
<p>In addition, I failed to use MR to register CT</p>
</blockquote>
</aside>
<p>Before registration, crop both volumes using Crop volume module to contain about the same region.</p>

---
