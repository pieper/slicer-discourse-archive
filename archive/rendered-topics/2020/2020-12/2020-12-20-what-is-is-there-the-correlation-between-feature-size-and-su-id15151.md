# What is/is there the correlation between feature size and surface area?

**Topic ID**: 15151
**Date**: 2020-12-20
**URL**: https://discourse.slicer.org/t/what-is-is-there-the-correlation-between-feature-size-and-surface-area/15151

---

## Post #1 by @zaina_moussa (2020-12-20 02:21 UTC)

<p>I am attempting to automate the segmentation of the aorta from a series of CT scans. Although changing the feature size did result in a change in surface area, I am not seeing a consistent correlation. In one image, when I increased the feature size, more structures were included (the surface area increased). (feature size was increased from left to right)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2bd1ee787e758debd674f6e3eb244fe18d0b18b1.png" alt="Screen Shot 2020-12-19 at 4.11.20 PM" data-base62-sha1="6fEj3PQPCtatkYe6nehtiSMCohz" width="576" height="262"><br>
However, in the example below, as I increased the featuresize, less structures were included. Is there a reason for this? (again, feature size was increased from left to right)<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/97a3fad503b909197afabc0cc94fe762620f6d0a.png" alt="Screen Shot 2020-12-19 at 4.12.15 PM" data-base62-sha1="lDtqeEqQwhX5CX9IGebTX2wCkNc" width="560" height="224"></p>

---

## Post #2 by @lassoan (2020-12-20 23:28 UTC)

<p>I added a bit more details to the effect’s documentation: <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/README.md#local-threshold">https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/README.md#local-threshold</a></p>
<p>Let us know if it still does not answer your questions.</p>

---

## Post #3 by @zaina_moussa (2020-12-21 17:23 UTC)

<p>Thank you, the extra details are helpful! I did want to get more info on the feature size parameters specifically. I would expect that larger feature size means that less structures would be included (but this is shown not to always be true by my screenshots above).<br>
I also see you mentioned a parameter called minimum diameter, is minimum diameter the same as featuresize, and if not how can minimum diameter be altered?<br>
Right now I am using GrowCut, what is the difference between using that and Watershed?<br>
Thanks!</p>

---

## Post #4 by @lassoan (2020-12-21 17:34 UTC)

<aside class="quote no-group" data-username="zaina_moussa" data-post="3" data-topic="15151">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zaina_moussa/48/9275_2.png" class="avatar"> zaina_moussa:</div>
<blockquote>
<p>I would expect that larger feature size means that less structures would be included</p>
</blockquote>
</aside>
<p>Feature size is an additional parameter for Watershed method. It is not directly related to the size of the added region, but it controls how fine small details are allowed in the region.</p>
<p>Watershed is good for enforcing extraction of simpler shapes, but for vessel trees I would recommend to use “Grow from seeds” segmentation algorithm instead.</p>
<aside class="quote no-group" data-username="zaina_moussa" data-post="3" data-topic="15151">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zaina_moussa/48/9275_2.png" class="avatar"> zaina_moussa:</div>
<blockquote>
<p>I also see you mentioned a parameter called minimum diameter, is minimum diameter the same as featuresize, and if not how can minimum diameter be altered?</p>
</blockquote>
</aside>
<p>If you don’t see the minimum diameter it means that you use a very old version of Slicer. You need to upgrade to at least the latest stable release.</p>

---
