---
topic_id: 18266
title: "Slicerigt Interface To Aimooe Aimposition Position Tracker"
date: 2021-06-22
url: https://discourse.slicer.org/t/18266
---

# SlicerIGT interface to Aimooe AimPosition position tracker

**Topic ID**: 18266
**Date**: 2021-06-22
**URL**: https://discourse.slicer.org/t/slicerigt-interface-to-aimooe-aimposition-position-tracker/18266

---

## Post #1 by @BrGiao (2021-06-22 12:44 UTC)

<p><strong>We want to connect our optical tracking device to 3Dslice’s slicerIGT module for the surgical navigation simulation shown below, but our device is not supported by Plus, how do I connect the two?</strong><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef5e2a16367f867b57538e04d6f39074d6b58e09.jpeg" alt="image" data-base62-sha1="y9xRqw2Zq1Hx8c9bvZfnaRGbQ2l" width="554" height="429"></p>

---

## Post #2 by @lassoan (2021-06-22 12:52 UTC)

<aside class="quote no-group" data-username="BrGiao" data-post="1" data-topic="18266">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/brgiao/48/11336_2.png" class="avatar"> BrGiao:</div>
<blockquote>
<p>our device is not supported by Plus</p>
</blockquote>
</aside>
<p>What optical tracker do you have?</p>

---

## Post #3 by @BrGiao (2021-06-22 13:26 UTC)

<p>AimooePosition，It’s from Guangzhou Aimooe Company, China</p>

---

## Post #4 by @lassoan (2021-06-22 13:33 UTC)

<p>We have not heard about this company. You can develop an interface yourself (starting from any other tracker example), but since both for the company and for users it is much better if they don’t reinvent a new API from scratch, I would recommend to adopt an existing interface, such as <a href="http://openigtlink.org/">OpenIGTLink</a> (open, widely supported, simple socket based interface) or maybe other commonly used interfaces, such as NDI common API (used by NDI trackers).</p>

---

## Post #5 by @BrGiao (2021-06-23 08:28 UTC)

<p>Thank you, Mr. Lassoan,  I am a newbie and I don’t understand much about the interface, I have the AimooePosition API development kit, How can I use OpenIGTLink to connect AimooePosition to slicer?</p>

---

## Post #6 by @lassoan (2021-06-23 12:52 UTC)

<p>You can implement a new device class in <a href="https://www.plustoolkit.org">Plus toolkit</a>.</p>

---

## Post #7 by @Selho (2023-12-27 22:13 UTC)

<p>I have the same problem as well, could you share the overview of your solution?</p>

---

## Post #8 by @lassoan (2024-01-02 17:28 UTC)

<p>You can contact the manufacturer, maybe they can already provide OpenIGTLink interface for their system. If not, then you can ask them to provide it (they can put it into Plus or develop and maintain themselves) or you can add it to Plus.</p>
<p>If they provide an SDK for Python then for quick prototyping you can write a short Python script that receives tracking data using that SDK and sends it via OpenIGTLink using <a href="https://pypi.org/project/pyigtl/">pyigtl</a>.</p>

---
