---
topic_id: 13718
title: "Seeding Basics For New User"
date: 2020-09-27
url: https://discourse.slicer.org/t/13718
---

# Seeding basics for new user

**Topic ID**: 13718
**Date**: 2020-09-27
**URL**: https://discourse.slicer.org/t/seeding-basics-for-new-user/13718

---

## Post #1 by @jax200 (2020-09-27 14:20 UTC)

<p>When painting in Segment Editor for “Grow from Seeds”, I understand you paint inside with one layer and circle around with another layer in order to segment out a structure.   Without any added specification, how does the program recognize a difference between the two?    Also, how to remove a areas that are “over painted”?   Sometimes the seeding doesn’t render accurately or with appropriate coverage despite good contrast, and get very ragged organs (eg, liver).   How to improve?</p>

---

## Post #2 by @lassoan (2020-09-27 14:29 UTC)

<p>The algorithm grows each seed simultaneously. Growing is faster in uniform areas, so boundaries between segments usually end up where there is a big step in image intensity</p>
<p>If wrong segment is grown anywhere then just paint some more seeds there, with the correct segment. Since this usually happens in low-contrast regions, typically you need to paint with two colors, at both sides of hardly-visible boundaries.</p>
<p>For liver segmentation, I would recommend the fully automatic AI-based segmentation tool provided by <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/tree/master/slicer-plugin#nvidia-ai-assisted-annotation-aiaa-for-3d-slicer">NVidia AIAA extension</a>.</p>

---

## Post #3 by @jax200 (2020-09-29 12:45 UTC)

<p>Thanks Andras.   I now better understand how the two colors are used to enhance contrast differential.</p>
<p>The extension requires 4.11.0 but unfortunately it won’t install properly on my PC.</p>

---

## Post #4 by @lassoan (2020-09-29 13:56 UTC)

<p>Slicer-4.11 requires a PC not older than about 6-8 years. If your computer is a more recent one and Slicer does not run on it then let us know.</p>

---

## Post #5 by @jax200 (2020-09-29 14:05 UTC)

<p>My “PC” is about 5-6 yrs old, but I installed a new motherboard and memory 6 mos ago. The error messages are of the form "The procedure entry point … could not be located in the dynamic link library… "</p>

---

## Post #6 by @lassoan (2020-09-29 15:26 UTC)

<p>A post was split to a new topic: <a href="/t/liver-visualization-in-3d/13747">Liver visualization in 3D</a></p>

---

## Post #7 by @lassoan (2020-09-29 15:27 UTC)

<p>What operating system do you use?<br>
Can you post the full error message?</p>

---

## Post #8 by @jamesobutler (2020-09-29 15:39 UTC)

<aside class="quote no-group" data-username="jax200" data-post="5" data-topic="13718">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/5e9695/48.png" class="avatar"> jax200:</div>
<blockquote>
<p>The error messages are of the form "The procedure entry point … could not be located in the dynamic link library… "</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/jax200">@jax200</a> this is a known issue with today’s Slicer Preview build (Slicer 4.11.0-2020-09-28) which you can follow updates for this issue at <a href="https://github.com/Slicer/Slicer/issues/5208" class="inline-onebox" rel="noopener nofollow ugc">Slicer 4.11.0-2020-09-28 does not start successfully · Issue #5208 · Slicer/Slicer · GitHub</a>.</p>
<p>Instead you can download the previous Slicer Preview build for Windows at the following link:<br>
<a href="http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.11.0-2020-09-25-win-amd64.exe&amp;checksum=5e26ad3bfdc54f3c95221a583acc655e" class="onebox" target="_blank" rel="noopener nofollow ugc">http://slicer.kitware.com/midas3/api/rest?method=midas.bitstream.download&amp;name=Slicer-4.11.0-2020-09-25-win-amd64.exe&amp;checksum=5e26ad3bfdc54f3c95221a583acc655e</a></p>

---

## Post #9 by @jax200 (2020-09-29 16:44 UTC)

<p>Windows 10 x64</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a01665614eab6d3512096fdadb271ee35ed7aac4.jpeg" alt="error" data-base62-sha1="mQcnt0HEMtHkb9o6d9HMpyOANVO" width="421" height="205"></p>

---

## Post #10 by @jax200 (2020-09-30 18:23 UTC)

<p>Thanks Andras - this extension worked quite well for me and look forward to experimenting with it further.</p>

---
