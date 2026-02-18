# After I got the cross-sectional area of a ROI, How can I measure its HU values?

**Topic ID**: 23162
**Date**: 2022-04-28
**URL**: https://discourse.slicer.org/t/after-i-got-the-cross-sectional-area-of-a-roi-how-can-i-measure-its-hu-values/23162

---

## Post #1 by @lyk-snail (2022-04-28 07:46 UTC)

<p>Hello!<br>
I’ve been using 3D slicer for a while. I have got the cross-sectional area of a muscle after I used the “segment editor” module AND the " Segment Cross-Section Area" module. But I don’t know how to measure the HU values of the ROI. How can I get the average, median, max，min HU value of it. I used CT image datas.<br>
Thank you!</p>

---

## Post #2 by @lassoan (2022-04-28 17:06 UTC)

<p>You can use Segment Statistics module to get these statistics for each segment.</p>
<p>If you need the values separately for each slice then you may use <a class="mention" href="/u/jmhuie">@jmhuie</a>’s <a href="https://github.com/jmhuie/Slicer-SegmentGeometry">SegmentGeometry</a> extension. Currently it provides only average, but would not be hard to add other statistics as well if there is a good reason. Note that min/max are extremely fragile metrics (a single voxel could throw off your results), probably you would want to use percentiles (1st and 99th or 5th and 95th) instead.</p>

---

## Post #3 by @jmhuie (2022-05-01 20:17 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="23162">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Currently it provides only average, but would not be hard to add other statistics as well if there is a good reason.</p>
</blockquote>
</aside>
<p>Yep, wouldn’t be difficult at all to add extra calculations if you decide there are certain ones you’d like</p>

---
