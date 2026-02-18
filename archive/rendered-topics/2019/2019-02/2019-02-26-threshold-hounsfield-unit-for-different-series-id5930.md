# Threshold/Hounsfield unit For different series

**Topic ID**: 5930
**Date**: 2019-02-26
**URL**: https://discourse.slicer.org/t/threshold-hounsfield-unit-for-different-series/5930

---

## Post #1 by @prorai (2019-02-26 13:35 UTC)

<p>Hi i’m using the Slicer from few days , and i saw that for different series the threshold value is different for same body part. for example bone threshold value for each body part should be same but it doesn’t work similar with different series and it doesn’t match with the Housnfield unit table.<br>
Hounsfied unit table suggest for bone it is 200 and  for me it is 120-150 for skull series and 200 for foot series.<br>
Do we have any Threshold/Hounsfield table for slicer ?<br>
Does Threshold value works differently in Slicer ?</p>

---

## Post #2 by @lassoan (2019-02-26 13:47 UTC)

<aside class="quote no-group" data-username="prorai" data-post="1" data-topic="5930">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/p/e8c25b/48.png" class="avatar"> prorai:</div>
<blockquote>
<p>i saw that for different series the threshold value is different for same body part.</p>
</blockquote>
</aside>
<p>This is expected. Hounsfied unit tables contain approximate values. Actual tissue density in a patient depend on many factors and so they can be quite different from the textbook values.</p>
<p>Also note that if different tissue types appear within one voxel then the intensity of that voxel will be the average of all the contained tissue types (this is called partial volume effect). It may cause noticeable intensity difference for thin structures and at the boundary of all tissues.</p>

---
