# Volume calculations are inconsistent on Bone CTs

**Topic ID**: 45919
**Date**: 2026-01-26
**URL**: https://discourse.slicer.org/t/volume-calculations-are-inconsistent-on-bone-cts/45919

---

## Post #1 by @Nat (2026-01-26 10:35 UTC)

<p>I am using slicer to separate cortical and trabecular bone in CT scans from morphosource. I use the threshold effect to first identify the cortical bone then use the wrap solidify tool to creat a segment with all bone volume. Then I go to quantification → segment statistics to obtain the volumes in mm^3.</p>
<p>However, on some bone scans the total volume comes out at 5700 mm^3 and then another scan of a bone the same length will give a volume of only 1800.</p>
<p>Any ideas of what I am doing wrong? The segments are cleaned up to ensure no background measurement. The ratio between the two is always roughly correct so i do nbot think it is a measurement error but rather a scaling one.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @muratmaga (2026-01-26 18:21 UTC)

<aside class="quote no-group" data-username="Nat" data-post="1" data-topic="45919">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/8c91f0/48.png" class="avatar"> Nat:</div>
<blockquote>
<p>then another scan of a bone</p>
</blockquote>
</aside>
<p>Is this the same species?</p>
<aside class="quote no-group" data-username="Nat" data-post="1" data-topic="45919">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/n/8c91f0/48.png" class="avatar"> Nat:</div>
<blockquote>
<p>The ratio between the two is always roughly correct so i do nbot think it is a measurement error but rather a scaling one</p>
</blockquote>
</aside>
<p>Make sure you import the data with the correct scale.</p>

---
