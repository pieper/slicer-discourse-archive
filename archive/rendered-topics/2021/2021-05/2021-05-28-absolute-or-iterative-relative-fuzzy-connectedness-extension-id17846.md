---
topic_id: 17846
title: "Absolute Or Iterative Relative Fuzzy Connectedness Extension"
date: 2021-05-28
url: https://discourse.slicer.org/t/17846
---

# (Absolute or Iterative Relative) Fuzzy Connectedness Extension?

**Topic ID**: 17846
**Date**: 2021-05-28
**URL**: https://discourse.slicer.org/t/absolute-or-iterative-relative-fuzzy-connectedness-extension/17846

---

## Post #1 by @bdottinger (2021-05-28 19:09 UTC)

<p>Hi all,</p>
<p>I was wondering if there were any plans to ever create a segmentation module that uses the Iterative Relative Fuzzy Connectedness Algorithm (or Absolute FC). The only existing dedicated software for IRFC is CAVASS, created by the UPenn MIPG about 20 years ago. I’d love to see this algorithm revisited in a more modern program. The source code for the module in CAVASS is available, if that would help bring it to Slicer. I’m unfortunately not versed enough in computer programming to do it myself.</p>
<p>Would love if somebody could help me out!</p>

---

## Post #2 by @lassoan (2021-05-28 21:18 UTC)

<p>We have experimented with many similar region growing methods (grow cut, graph cut, watershed, random walk, fast marching, etc. variants) over the years. Fast growcut method stood out by far among all, with its fast initialization and incremental update capability. It has gone through several iteration of performance optimizations and got features such as masking and seed locality constraints. It is made available in the “Grow from seeds” effect in Segment Editor. It is very likely that this region growing implementation works much better than some old implementation of a fuzzy connectedness filter.</p>

---

## Post #3 by @bdottinger (2021-06-02 13:40 UTC)

<p>Thank you for your response.</p>
<p>I have had great success with the “Grow from seeds” effect in the past. As I understood, fuzzy connectedness takes positional information in addition to intensity to help delineate between similarly-intense objects that are nearby. Does the grow from seeds effect work this way? I often have trouble trying to separate arteries and veins using this effect, for example, due to the proximity and similar intensities in the scans I am working with. Are there parameters in this effect that you recommend I adjust for greater success?</p>
<p>Thank you.</p>

---

## Post #4 by @lassoan (2021-06-02 13:50 UTC)

<aside class="quote no-group" data-username="bdottinger" data-post="3" data-topic="17846">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bdottinger/48/11095_2.png" class="avatar"> bdottinger:</div>
<blockquote>
<p>in addition to intensity to help delineate between similarly-intense objects that are nearby. Does the grow from seeds effect work this way?</p>
</blockquote>
</aside>
<p>Yes. It takes into account both spatial proximity and intensity difference. You can set “Seed locality” to higher value to add penalty for being farther from a seed. However, for separating arterial/venous tree you can expect better results from adding more seeds wherever corrections are needed.</p>

---

## Post #5 by @bdottinger (2021-06-02 14:08 UTC)

<p>Understood, thank you for your help!</p>

---
