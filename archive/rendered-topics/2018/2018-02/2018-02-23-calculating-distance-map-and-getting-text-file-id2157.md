---
topic_id: 2157
title: "Calculating Distance Map And Getting Text File"
date: 2018-02-23
url: https://discourse.slicer.org/t/2157
---

# calculating distance map and getting text file

**Topic ID**: 2157
**Date**: 2018-02-23
**URL**: https://discourse.slicer.org/t/calculating-distance-map-and-getting-text-file/2157

---

## Post #1 by @nodi (2018-02-23 02:40 UTC)

<p>hello.<br>
I’m new to Slicer. I want to use this filter: ApproximateSignedDistanceMapImageFilter. to calculate the distance of each point to the boundary after doing segmentation.<br>
How can I get the distance map as a text file to recall it again for other purposes?</p>
<p>Thank you.</p>

---

## Post #2 by @nodi (2018-02-23 22:10 UTC)

<p>Can somebody help please?</p>

---

## Post #3 by @pieper (2018-02-23 22:36 UTC)

<p>Hi -</p>
<p>You can run that filter through SimpleFilters</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SimpleFilters" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SimpleFilters</a></p>
<p>You can save the result as an regular volume file that you can reload (in binary not in ascii text, but you could convert it outside slicer if you want text).</p>
<p>Hope that helps,<br>
Steve</p>

---

## Post #4 by @lassoan (2018-02-23 22:45 UTC)

<p>Also note that you can get Hausdorff distance and even full surface error distribution from Segment Comparison module in SlicerRT extension:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/SegmentComparison</a></p>

---

## Post #5 by @nodi (2018-02-25 21:57 UTC)

<p>Thank you for respond but what do you mean by</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="2157">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>convert it outside slicer if you want text</p>
</blockquote>
</aside>
<p>?</p>

---

## Post #6 by @nodi (2018-02-25 21:59 UTC)

<p>Thank you Lasso.</p>
<p>How can I use the maximum distance value as a radius to draw a sphere?</p>

---

## Post #7 by @lassoan (2018-02-25 23:08 UTC)

<p>You can expand your segment by a specified margin in Segment Editor module, using Margin effect.</p>

---

## Post #8 by @nodi (2018-02-26 20:58 UTC)

<p>I have read about the Segment Comparison. it compare between 2 models or segments. but I want to find the max distance for each voxel on tumor to the edge (boundary) of the tumor.</p>

---

## Post #9 by @lassoan (2018-02-26 22:51 UTC)

<p>That’s a distance map that you can compute using Simple Filters module as described above.</p>
<p>Why do you need the distance map? For segmentation or registration accuracy assessment?</p>

---

## Post #10 by @nodi (2018-02-27 22:43 UTC)

<p>for drawing spheres based on the distances.</p>

---

## Post #11 by @lassoan (2018-02-27 22:59 UTC)

<aside class="quote no-group" data-username="nodi" data-post="10" data-topic="2157" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/57b2e6/48.png" class="avatar"> nodi:</div>
<blockquote>
<p>for drawing spheres based on the distances.</p>
</blockquote>
</aside>
<p>I mean what is the end goal - the clinical problem and the solution that you are working towards?</p>

---

## Post #12 by @nodi (2018-02-28 17:23 UTC)

<p>to define the position of the shot (radiotherapy)</p>

---
