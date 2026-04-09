---
topic_id: 46683
title: "Viewing Analysing Rt Plans Fields"
date: 2026-04-08
url: https://discourse.slicer.org/t/46683
---

# Viewing / Analysing RT Plans / Fields

**Topic ID**: 46683
**Date**: 2026-04-08
**URL**: https://discourse.slicer.org/t/viewing-analysing-rt-plans-fields/46683

---

## Post #1 by @AlexB (2026-04-08 14:14 UTC)

<p>Greetings, dear community!</p>
<p>First off, thanks for this project–and for actively maintaining it. Now, I’d like to know if the program would cover my use-case, namely:</p>
<ul>
<li>Visualise dose distributions (in colour-wash mode)</li>
<li>Show field configurations (e.g. for VMAT, the RT extension doesn’t seem to show the arc)</li>
<li>Display normalisation values</li>
</ul>
<p>Also, I can’t seem to find a way to place the crosshair over the DVH so as to read out the exact values.</p>
<p>Any input is much appreciated!</p>

---

## Post #2 by @pieper (2026-04-08 14:20 UTC)

<p>I believe <a href="https://slicerrt.github.io/">SlicerRT</a> can do most or all of what you are looking for.</p>

---

## Post #3 by @AlexB (2026-04-08 14:37 UTC)

<p>Dear Steven,</p>
<p>Thanks a lot for your prompt response. May I ask how I best find those settings/features? The extension is installed already.</p>

---

## Post #4 by @pieper (2026-04-09 00:21 UTC)

<p>I haven’t used it extensively myself.  I think you can just read the tutorials and maybe post specific questions if things aren’t clear.  Be aware that sometime extension code is still available after the active funding is exhausted, so there may not be anyone to answer and you’ll have to see what you can figure out on your own.</p>

---

## Post #5 by @Mik (2026-04-09 03:27 UTC)

<aside class="quote no-group" data-username="AlexB" data-post="1" data-topic="46683">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/alexb/48/81261_2.png" class="avatar"> AlexB:</div>
<blockquote>
<p>Show field configurations (e.g. for VMAT, the RT extension doesn’t seem to show the arc)</p>
</blockquote>
</aside>
<p>Do you mean the beam borders (acceptance)? You can visualise your dynamic beam, if it has multiple control points by means of the sequence browser. The ARC type of beam with only two control points doesn’t work yet.</p>

---
