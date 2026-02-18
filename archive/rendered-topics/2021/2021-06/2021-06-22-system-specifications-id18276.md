# System specifications

**Topic ID**: 18276
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/system-specifications/18276

---

## Post #1 by @sarvpriya1985 (2021-06-22 18:03 UTC)

<p>Hi all,</p>
<p>I am trying to update my windows system for 3D processing, segmentation and virtual reality. I would like to know your opinion on graphics card. I am considering RTX5000 16 GB versus RTX600024 GB. Would like to know if spending about 2000 extra on RTX6000 is worth.<br>
Would appreciate your opinion.</p>
<p>Thanks<br>
Sarv</p>

---

## Post #2 by @lassoan (2021-06-22 23:16 UTC)

<p>The performance difference between the RTX 5000 and 6000 seems to be very significant (about 20-30% in many metrics). The 1.5x more memory may make a difference in training complex deep learning models. If you have the money to buy the 6000 then it would be a safer bet.</p>

---

## Post #3 by @sarvpriya1985 (2021-06-22 23:24 UTC)

<p>Thanks Andras. I am not planning deep learning training. My work is for multiphase CT segmentation. In the past I ran into issues of low memory when trying to register multiple Ct Series. So I decided to upgrade ram to 64 GB and update processor to i9. Graphics card was the thing that I wanted the opinion if usual segmentation, registration, volume rendering and virtual reality can be run efficiently on RTX 5000. Since I don’t perform any deep learning, want to make sure if I spend about 2k more for RTX 6000.</p>
<p>Sarv</p>

---

## Post #4 by @lassoan (2021-06-23 00:04 UTC)

<p>20-30% faster rendering may make a perceivable difference, so if money does not matter (e.g., there is a grant that pays for it and you are not tight on budget) then it may make sense to buy a 6000. If you have limited hardware budget then it is up to you to find a good balance between what you need and what you can afford.</p>

---

## Post #5 by @sarvpriya1985 (2021-06-23 00:07 UTC)

<p>Thanks Andras. I guess I would go for RTX 6000 in that case.</p>
<p>Sarv</p>

---

## Post #6 by @muratmaga (2021-06-23 01:50 UTC)

<p>Two things:</p>
<ol>
<li>GPUs have no bearing on your segmentation, registration tasks.</li>
<li>RTX 6000 is previous generation. From the current generation for the same specs you can get the RTX A5000 about the same price (or even cheaper). Or  get RTX A6000, which is equivalent to RTX 8000 of that line up in specs, which has  48GB of RAM.</li>
</ol>

---

## Post #7 by @sarvpriya1985 (2021-06-23 03:20 UTC)

<p>Thanks Muratmaga. It does help to know GPU has no bearing on segmentation stuff. I will keep that in mind and will look for the new A5000 card. This helps a lot since I don’t need to go over budget now and can come down on graphics card a little bit</p>

---

## Post #8 by @lassoan (2021-06-23 04:31 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="6" data-topic="18276">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>GPUs have no bearing on your segmentation, registration tasks.</p>
</blockquote>
</aside>
<p>All new automatic/semi-automatic segmentation methods use deep learning. So, if somebody buys a GPU with the intent of using it for a couple of years, then getting a stronger GPU may pay off.</p>
<p>I agree that not much going on in image registration, so significant utilization of GPUs for registration is not very likely in the next few years.</p>
<p><a class="mention" href="/u/sarvpriya1985">@sarvpriya1985</a> also needs very fast volume rendering (for replay of 4D images in virtual reality), where a faster GPU may make a difference, too.</p>

---
