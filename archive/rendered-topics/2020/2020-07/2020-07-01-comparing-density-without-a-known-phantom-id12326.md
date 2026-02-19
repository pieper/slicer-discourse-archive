---
topic_id: 12326
title: "Comparing Density Without A Known Phantom"
date: 2020-07-01
url: https://discourse.slicer.org/t/12326
---

# Comparing Density without a known phantom

**Topic ID**: 12326
**Date**: 2020-07-01
**URL**: https://discourse.slicer.org/t/comparing-density-without-a-known-phantom/12326

---

## Post #1 by @jamieawren (2020-07-01 19:01 UTC)

<p>Hello,</p>
<p>I am a very novice use of 3D Slicer, and am still working on fully understanding the conceptual side of image analysis, let alone the “how to” of specific Slicer functions… If I have a group of CT scans, all done under the same protocol (without a phantom) can I reliably use HU to compare between the scans? ie, HU of Individual A is less than the HU of Individual B? And could these units be translated to a Z-score similar to DEXA? Any thoughts or resources that you feel may be helpful would be greatly appreciated!</p>
<p>Take care!</p>

---

## Post #2 by @pieper (2020-07-01 23:46 UTC)

<p>In Slicer we try hard to preserve the original values from the file so any variability in HU would come from other effects, like scanner calibration, noise, beam hardening, partial voluming, and other purely CT related issues.</p>

---

## Post #3 by @lassoan (2020-07-02 05:16 UTC)

<aside class="quote no-group" data-username="jamieawren" data-post="1" data-topic="12326">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/da6949/48.png" class="avatar"> jamieawren:</div>
<blockquote>
<p>could these units be translated to a Z-score similar to DEXA?</p>
</blockquote>
</aside>
<p>DEXA is 2D projection only, but uses dual energy, so the results are not comparable to a 3D CT image acquired at a single energy. Therefore, there is no universal formula to convert between DEXA and CT scores, but there is a huge literature of how these scores can be interpreted or converted for particular populations and body parts.</p>

---
