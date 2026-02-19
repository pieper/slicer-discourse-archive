---
topic_id: 25122
title: "Segment Geometry Number Of Slices Truncated"
date: 2022-09-06
url: https://discourse.slicer.org/t/25122
---

# Segment Geometry - number of slices truncated?

**Topic ID**: 25122
**Date**: 2022-09-06
**URL**: https://discourse.slicer.org/t/segment-geometry-number-of-slices-truncated/25122

---

## Post #1 by @hherhold (2022-09-06 12:42 UTC)

<p>This question is likely for <a class="mention" href="/u/jmhuie">@jmhuie</a>, as it is a question with the Segment Geometry extension. I noticed that the number of rows in the table for computed values (area in my instance) is the number of slices in the segment, not the number of slices in the volume. I’m actually comparing the slice-by-slice surface area of two separate segments, which have different geometries, so one has fewer rows than the other and if I plot them next to each other, they don’t line up. Is there an option to use the geometry of the volume, rather than the segment, so each computation has the same number of slices?</p>
<p>I’m also happy to take a stab at implementing this if it sounds generally useful and if you could point me in the right general direction.</p>
<p>Thank you!</p>

---

## Post #2 by @jmhuie (2022-09-07 23:29 UTC)

<aside class="quote no-group" data-username="hherhold" data-post="1" data-topic="25122">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hherhold/48/12199_2.png" class="avatar"> hherhold:</div>
<blockquote>
<p>Is there an option to use the geometry of the volume, rather than the segment, so each computation has the same number of slices?</p>
</blockquote>
</aside>
<p>Unfortunately not intuitively. A segment is required otherwise the area will just be the dimensions of the volume. I have two suggestive work arounds that may provide the results you want</p>
<ol>
<li>
<p>You could add dummy slices to the ends of the actual segments that extend to the length of the volume. This way, the outputs of your different structures will be the same length. You could just add a single pixel per slice so it’s obvious as to which which slices are the dummy slices.</p>
</li>
<li>
<p>You could perform the computations on every slice of the structures and not downsample to just 100. That’ll preserve the number of slices that make up each structure.</p>
</li>
</ol>

---
