---
topic_id: 7963
title: "A Quick Easy Method To Segment Individual Muscles"
date: 2019-08-09
url: https://discourse.slicer.org/t/7963
---

# A quick/easy method to segment individual muscles 

**Topic ID**: 7963
**Date**: 2019-08-09
**URL**: https://discourse.slicer.org/t/a-quick-easy-method-to-segment-individual-muscles/7963

---

## Post #1 by @tsjamo (2019-08-09 13:01 UTC)

<p>Good afternoon.</p>
<p>I have MR images from a research study of the human thigh before and after an intervention which induces muscle atrophy.</p>
<p>I wish to quantify this atrophy by looking at changes in muscle volume. I have used the threshold feature on segment editor to threshold muscle which has worked well to provide a whole muscle volume. However, I also which to look at quadriceps and hamstring volume independently. I have tried to use the scissor tool to cut out the muscle of interest, however this applies the same cut area to every slice and therefore as you move up the leg, the cut area is no longer representative of the muscle of interest. From my understating, you cant apply the scissor function to a single slice.</p>
<p>The only solution I can come up with is to manually paint each muscle of interest on each individual slice, which is going to take an enormous amount of time based on the number of cases I have.</p>
<p>Please can anyone advise if there is an alternative method I could use to do this?</p>
<p>Thank you,<br>
Tom</p>

---

## Post #2 by @pieper (2019-08-09 20:25 UTC)

<p>Hi Tom -</p>
<p>With the current Slicer version your best bet is probably the Fill between slices tool in the Segment Editor.  Did you try that?</p>
<p>Some of us worked on doing <a href="https://www.dropbox.com/s/0fmy8mp2hps5b35/ECR2013_C-0361.pdf?dl=0" rel="nofollow noopener">thigh-muscle segmentation a while back</a> but the tool is only available for the Slicer 3.6.4 or so (e.g. from <a href="https://www.slicer.org/slicer3-downloads/Snapshots/" rel="nofollow noopener">back in 2011</a> and was never ported to Slicer 4.x and I can’t make any promises about old versions working or not on new computers.</p>

---

## Post #3 by @lassoan (2019-08-09 20:47 UTC)

<aside class="quote no-group" data-username="tsjamo" data-post="1" data-topic="7963">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/8edcca/48.png" class="avatar"> tsjamo:</div>
<blockquote>
<p>From my understating, you cant apply the scissor function to a single slice.</p>
</blockquote>
</aside>
<p>You can restrict scissors to current slice, certain distance around the current slice, or one side of the current slice.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d8a248fb5f3c73a3fb207ccbed26f09cec18d35.png" data-download-href="/uploads/short-url/4djOBIRWsNthSi9AOqcza4DKgD3.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d8a248fb5f3c73a3fb207ccbed26f09cec18d35.png" alt="image" data-base62-sha1="4djOBIRWsNthSi9AOqcza4DKgD3" width="690" height="278" data-dominant-color="EEEDEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1011×408 24.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="7963">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>With the current Slicer version your best bet is probably the Fill between slices tool in the Segment Editor.</p>
</blockquote>
</aside>
<p>I agree, “Fill between slices” effect was used successfully for muscle segmentation in other projects (should work better than Scissors effect, even if you restrict to operate only around the current slice).</p>

---
