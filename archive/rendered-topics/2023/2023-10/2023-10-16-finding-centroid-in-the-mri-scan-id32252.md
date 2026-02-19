---
topic_id: 32252
title: "Finding Centroid In The Mri Scan"
date: 2023-10-16
url: https://discourse.slicer.org/t/32252
---

# Finding centroid in the MRI scan

**Topic ID**: 32252
**Date**: 2023-10-16
**URL**: https://discourse.slicer.org/t/finding-centroid-in-the-mri-scan/32252

---

## Post #1 by @Michaela (2023-10-16 14:17 UTC)

<p>Hello everybody,</p>
<p>First of all, I am completely new to the 3D Slicer. My data consists of MRI scans of long bones.<br>
I need to measure cross sections of bones. I imagine something like this on the picture,but I did not figure out how to find centroid of cross sections. Can someone help me with this problem please?.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8eb8fde97deb7ee8fc38e749f0088531d5d02b4c.png" alt="image" data-base62-sha1="kmA8VxE0KXnYK59nazKkRuV0cNK" width="384" height="378"></p>

---

## Post #2 by @lassoan (2023-10-17 01:50 UTC)

<p>What would you like to measure?</p>
<p>There are modules specifically for analyzing long bones, such as SegmentGeometry module in SlicerBiomech extension by <a class="mention" href="/u/jmhuie">@jmhuie</a>.</p>

---

## Post #3 by @jmhuie (2023-10-17 02:20 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="32252">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>There are modules specifically for analyzing long bones, such as SegmentGeometry module in SlicerBiomech extension by <a class="mention" href="/u/jmhuie">@jmhuie</a>.</p>
</blockquote>
</aside>
<p>Yep. The SegmentGeometry module can find the centroid of long bones, but how it is reported may not be useful. What do you plan to do with the centroids coordinates?</p>
<p>More about SegmentGeometry: <a href="https://github.com/jmhuie/SlicerBiomech/tree/main/Docs/SegmentGeometry" rel="noopener nofollow ugc">https://github.com/jmhuie/SlicerBiomech/tree/main/Docs/SegmentGeometry</a></p>

---
