---
topic_id: 2296
title: "Fiber Count Limitation"
date: 2018-03-12
url: https://discourse.slicer.org/t/2296
---

# Fiber count limitation

**Topic ID**: 2296
**Date**: 2018-03-12
**URL**: https://discourse.slicer.org/t/fiber-count-limitation/2296

---

## Post #1 by @Heiko_Stark (2018-03-12 12:58 UTC)

<p>Is there a way to limit the number of fibres tracked from a labelmap?<br>
Random seed points are also available.</p>
<p>Best regards,<br>
Heiko</p>

---

## Post #2 by @ihnorton (2018-03-19 16:19 UTC)

<p>The only way to restrict the result bundle during seeding is to make the seeding criteria more stringent (e.g. stopping values). After seeding, you can sub-sample a (randomly selected) percentage in the Tractography Display module, or use a selection ROI – and then export to a new bundle, if needed.</p>

---
