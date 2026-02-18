# Purchasing a new workstation - what to look for?

**Topic ID**: 1805
**Date**: 2018-01-10
**URL**: https://discourse.slicer.org/t/purchasing-a-new-workstation-what-to-look-for/1805

---

## Post #1 by @losp (2018-01-10 11:57 UTC)

<p>Hi,</p>
<p>Hoping to pick some brains about workstation specs - I’m tasked with purchasing a new one for our lab. We’ll be working with large DICOM data sets (up 2 - 2.5GB). These are full-body scans and we’re planning to do lots of bone rendering.</p>
<p>I’m thinking 16GB+ RAM; i7 processor (someone recommended 3GHz+); but I’m a little lost with what to look for in a graphics card. Any help or thoughts appreciated!</p>
<p>Thanks</p>

---

## Post #2 by @muratmaga (2018-01-11 02:49 UTC)

<p>16GB is on the low-end for memory for 3D graphics workstations. Depending on what you want to do it might be enough, but you might consider getting 64GB, especially if your datasets are that big and if you are going to apply some image filters or do segmentation. Nvidia’s GeForce line of (e.g. Geforce 1080) will be sufficient (unless you want to do stereo rendering). A high end SSD for storage will help you load your datasets more quickly.</p>

---

## Post #3 by @lassoan (2018-01-11 04:35 UTC)

<p>I second <a class="mention" href="/u/muratmaga">@muratmaga</a>.</p>
<p>In general, I would recommend having 10x more RAM than your data set size. In your case, it would mean about 32 GB.</p>
<p>GeForce 1080 should serve you well for 1-2 years, probably even for VR applications.</p>

---

## Post #4 by @losp (2018-01-20 08:36 UTC)

<p>Thanks to you both! <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #5 by @Suhaim (2025-12-03 06:52 UTC)

<p>Hi,</p>
<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="1805">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>GeForce 1080 should serve you well for 1-2 years, probably even for VR applications.</p>
</blockquote>
</aside>
<p>I wanted to confirm one thing, as I am also looking to purchase a new machine. What I need is for the <strong>3-D render window to run as smoothly as possible</strong>. Does using a dedicated graphics card help improve the speed(frame rate) of the 3-D render window?</p>
<p>Currently, I am running on an integrated graphics card, and the 3-D render window gets slow as the scene gets more complex. I can share an example of why I am looking to upgrade my machine.</p>
<p>Let’s say I have a small sphere of diameter 6mm. If I fill the scene with 100-150 such spheres oriented and placed at several angles, the 3-D render starts lagging. I tried decreasing the sphere resolution to a minimum, but still didn’t see a visible performance gain. Would a dedicated graphics card improve the render speed?</p>
<p>If a dedicated graphics card would help, are there any specifics I should look for, like VRAM, etc for this specific application?</p>
<p>Thank you</p>
<p>P.S :<br>
My machine specs are -</p>
<p>Slicer version: 5.10.0<br>
Operating system: Ubuntu 22.04<br>
GPU hardware: Mesa Intel® UHD Graphics (TGL GT1)</p>

---

## Post #6 by @lassoan (2025-12-03 22:59 UTC)

<p>A discrete GPU (not integrated Intel graphics) makes a huge difference in rendering complex scenes.</p>
<p>If you buy a laptop with a discrete GPU it is worth investing into one that can run AI models (TotalSegmentator, MONAIAuto3DSeg, nnInteractive, etc.). I would recommend getting an NVIDIA RTX 4xxx or 5xxx series GPU with at least 12GB VRAM. I would not recommend buying low-end (xx50 or xx60) models, as they are much slower and often cannot run AI models due to lack of VRAM.</p>

---

## Post #7 by @Suhaim (2025-12-04 03:44 UTC)

<p>Thanks a lot for the quick reply<a href="https://discourse.slicer.org/u/lassoan">, @lassoan</a>. The suggestion to buy a GPU with high VRAM for segmentation is very helpful, as I will be attempting automated segmentation in the near future. Currently, I am relying solely on the semi-automated grow with seeds algorithm.</p>

---
