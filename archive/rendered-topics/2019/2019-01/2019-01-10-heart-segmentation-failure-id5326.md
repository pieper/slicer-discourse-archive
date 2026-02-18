# Heart segmentation failure

**Topic ID**: 5326
**Date**: 2019-01-10
**URL**: https://discourse.slicer.org/t/heart-segmentation-failure/5326

---

## Post #1 by @opetne (2019-01-10 15:08 UTC)

<p>I have a cardiac CT series from pigs. I did hear segmentation before using segment editor following the steps of the video, created by <a class="mention" href="/u/lassoan">@lassoan</a> without any problem, having good results.<br>
This series contains a whole cardiac phase from 0 to 100% from diastole to systole. After loading the series I checked the exact phase of diastole and systole using the Multivolume explorer module, made a copy of the frame I needed. Then I croped the series for the heart. I used this frames for the segment editor. I placed the seeds (only left vetnricle and outer segments). After finishing this part I initialized the growing from seeds command. Then I used the segment preview for creating the closed surface. After that going beack to segment editor and used the show 3D command. Here it only showed any opaque surface model of the left ventricle without the outer segment. I could export the model of the left ventricle and check it’s volume. I checked the volume of the segmentation with the segment statistic module. THe volume of the model was different than the model of the segmentation (approx. 10 cm3 more).<br>
Where did I make a mistake?</p>

---

## Post #2 by @lassoan (2019-01-10 18:09 UTC)

<aside class="quote no-group" data-username="opetne" data-post="1" data-topic="5326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/71e660/48.png" class="avatar"> opetne:</div>
<blockquote>
<p>Here it only showed any opaque surface model of the left ventricle without the outer segment</p>
</blockquote>
</aside>
<p>The outer segment gets hidden by default after you complete Grow from seeds. You can click the eye icon in the segment list to make it visible again.</p>
<aside class="quote no-group" data-username="opetne" data-post="1" data-topic="5326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/o/71e660/48.png" class="avatar"> opetne:</div>
<blockquote>
<p>I could export the model of the left ventricle and check it’s volume. I checked the volume of the segmentation with the segment statistic module. THe volume of the model was different than the model of the segmentation (approx. 10 cm3 more).</p>
</blockquote>
</aside>
<p>What you described seems to be correct. There may be small differences (&lt;1%) between volume computed from labelmap representation vs. computed from closed surface representation, due to surface smoothing. What is the volume difference in percentage of total volume?</p>
<p>Segment statistics computes volume both from labelmap and surface representations. How much were those volumes? How much was the volume computed from the exported model?</p>

---

## Post #3 by @lassoan (2019-01-11 15:09 UTC)

<p>The problem was that the user did not click “Apply” to finalize segmentation. Until “Grow from seeds” is applied, two segmentations are visible: one showing the seeds (this one is edited in the segment editor), and another preview segmentation that is only used for showing a preview of the final result based on the current seeds. Clicking apply replaces the seeds with the final segmentation result and removes the temporary preview segmentation node.</p>

---
