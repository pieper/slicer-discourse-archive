---
topic_id: 19264
title: "The Image Dimension Changes After Segment Editting The Segme"
date: 2021-08-19
url: https://discourse.slicer.org/t/19264
---

# The image dimension changes after segment editting the segment in 3d slicer

**Topic ID**: 19264
**Date**: 2021-08-19
**URL**: https://discourse.slicer.org/t/the-image-dimension-changes-after-segment-editting-the-segment-in-3d-slicer/19264

---

## Post #1 by @parvaneh.a (2021-08-19 00:54 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior: saving the edited segment in the same dimension<br>
Actual behavior:The image dimension changes after segment editing the segment in 3d slicer</p>
<p>I have a nii.gz segment image (containing 0 and 1) which I need to edit that. So, I opened it in slicer as segment and in Segment editor I used island, and scissors. Then, I clicked on save button at the top but the resultant edited segment dimension is 450, 269, 228 while the original segment dimension was 512,512,236. I need to save it in original dimension. How can I do it?</p>

---

## Post #2 by @pieper (2021-08-19 10:51 UTC)

<aside class="quote no-group" data-username="parvaneh.a" data-post="1" data-topic="19264">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/parvaneh.a/48/14462_2.png" class="avatar"> parvaneh.a:</div>
<blockquote>
<p>Operating system:<br>
Slicer version:</p>
</blockquote>
</aside>
<p>Please include the version and os when posting questions; it helps us help you.</p>
<p>I guess you are using an older Slicer.  I believe the current nightly preserves the original dimensions by default.</p>

---
