---
topic_id: 14579
title: "Best Computer For Running Slicer"
date: 2020-11-13
url: https://discourse.slicer.org/t/14579
---

# Best computer for running Slicer

**Topic ID**: 14579
**Date**: 2020-11-13
**URL**: https://discourse.slicer.org/t/best-computer-for-running-slicer/14579

---

## Post #1 by @ebryson (2020-11-13 01:20 UTC)

<p>Hi All!</p>
<p>I’m buying a new computer and have noticed that my Mac is struggling to run (very slow and fan kicks on) when I’m landmarking my segmentations. Does anyone have advice for a computer that is strong enough to power Slicer?</p>
<p>I’m using it to do research from home while we can’t work in the lab so it’s pretty important I get something that works quickly.</p>
<p>Thanks,<br>
Rose</p>

---

## Post #2 by @lassoan (2020-11-13 15:07 UTC)

<p>This page should help: <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements">https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#system-requirements</a></p>

---

## Post #3 by @ebryson (2020-11-13 16:23 UTC)

<p>Thank you, I was using it on a brand new Mac and it was still struggling. But I’ll look at the Memory and Graphics card, maybe it just wasn’t big enough. That or maybe my dataset was too big, but it was a cropped volume of a skull so I didn’t think it should be too bad.</p>
<p>I do have to have a volume loaded and volume rendering on to correctly find my landmarks, maybe that’s what’s slowing everything down?</p>

---

## Post #4 by @lassoan (2020-11-13 16:37 UTC)

<p>Volume rendering is done by the CPU by default (for best compatibility), which hugely slows down all interactions. You can switch to GPU volume rendering in Volume rendering module -&gt; Display -&gt; Rendering -&gt; VTK GPU Ray Casting.</p>
<p>Probably we’ll make GPU volume rendering the default in the next Slicer version to avoid such issues in the future.</p>

---

## Post #5 by @muratmaga (2020-11-13 16:45 UTC)

<aside class="quote no-group quote-modified" data-username="lassoan" data-post="4" data-topic="14579">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can switch to GPU volume rendering in Volume rendering module → Display → Rendering → VTK GPU Ray Casting.</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/ebryson">@ebryson</a> And also under the Techniques tab adjust the quality from Adaptive to Normal.</p>

---

## Post #6 by @ebryson (2020-11-23 02:53 UTC)

<p>THANK YOU, this cut my processing time by 2/3rds! It went from taking 3 hours to collect landmarks to 1.<br>
I really appreciate the suggestion!</p>

---
