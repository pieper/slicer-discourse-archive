# Totalsegmentation hardware requirements

**Topic ID**: 44870
**Date**: 2025-10-24
**URL**: https://discourse.slicer.org/t/totalsegmentation-hardware-requirements/44870

---

## Post #1 by @alex_He (2025-10-24 13:05 UTC)

<p>Hi I am running 3d slicer 5.8 windows 11 with nvidia gpu, when I run totalsegmentation, it takes 45 mins to process. May i ask what is the minimum gpu requirement to run it in just a few minutes?</p>

---

## Post #2 by @lassoan (2025-10-25 14:11 UTC)

<p>It can be confuaing that they put low-performance NVIDIA GPUs in laptops that are somewjat useful for gaming but insufficient for inference on 3D images (may work slower than just using the CPU).</p>
<p>What NVIDIA GPU do you use?</p>
<p>What torch version is installed? (you can see it in PyTorch Utils module in Slicer)</p>

---

## Post #3 by @alex_He (2025-10-26 06:55 UTC)

<p>Gpu geforce mx250<br>
Torch version 2.8.0</p>

---

## Post #4 by @muratmaga (2025-10-26 19:04 UTC)

<aside class="quote no-group" data-username="alex_He" data-post="3" data-topic="44870">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/alex_he/48/67616_2.png" class="avatar"> alex_He:</div>
<blockquote>
<p>mx250</p>
</blockquote>
</aside>
<p>That’s a very low end GPU from 7 years ago. I am actually surprised it works…</p>
<p>If you want the total segmentator to work just take few minutes, you need something far more recent, like maybe geforce 3000 series or newer (they are up to 5000s).</p>

---

## Post #5 by @alex_He (2025-10-27 02:53 UTC)

<p>Do I need rtx 4000 or something like that?</p>

---

## Post #6 by @muratmaga (2025-10-27 04:49 UTC)

<p>Nvidia have a few different generations of products called RTX 4000 going back 4-5 years. However, even the earliest one (which has 8GB of RAM) should work much better than what you have right now.</p>

---

## Post #7 by @alex_He (2025-10-28 05:28 UTC)

<p>Thanks you for your reply , I will try to upgrade to faster gpu</p>

---

## Post #8 by @alex_He (2025-11-06 05:42 UTC)

<p>Hi</p>
<p>is nvidia rtx 4060 12gb vram good enough for full totalsegmentator hd segmentation?</p>

---

## Post #9 by @lassoan (2025-11-06 14:39 UTC)

<p>Yes, an RTX 4060 with 12GB VRAM is sufficient to run the “total” TotalSegmentator model at full quality. It might be possible that for very large images (e.g., head-to-toe CTs) more resources are needed or certain models need more memory, but it should work well for most models and most images.</p>

---

## Post #10 by @alex_He (2025-11-08 06:18 UTC)

<p>Thx, I will try that, BTW  which laptop brand and model do you recommend? By budget is arround S$3000 to S$3500</p>

---
