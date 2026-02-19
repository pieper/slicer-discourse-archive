---
topic_id: 43239
title: "Estimating Memory Required For Nninteractive"
date: 2025-06-05
url: https://discourse.slicer.org/t/43239
---

# Estimating memory required for NNinteractive

**Topic ID**: 43239
**Date**: 2025-06-05
**URL**: https://discourse.slicer.org/t/estimating-memory-required-for-nninteractive/43239

---

## Post #1 by @muratmaga (2025-06-05 17:54 UTC)

<p>Is there a way to predictably calculate the memory required to segment a volume using NNinteractive? For example given the 400x400x400 16 bit volume how much GPU memory would I need. I</p>
<p>Trying to figure out via trial and experiment is a  fairly frustrating experience, as you have to wait until it fails…</p>

---

## Post #2 by @pieper (2025-06-05 18:12 UTC)

<p>I was running with <a href="https://github.com/Syllo/nvtop">nvtop</a> installed and seeing how high the bar gets for different scenarios.  This could give you a feel for the size vs memory tradeoffs but I’m not sure if there are other factors involved (like the autozoom).</p>

---

## Post #3 by @muratmaga (2025-06-05 21:19 UTC)

<p>I do that but I was hoping some sort of a deterministic method I can use to decide what’s the largest volume chunk I can fit in, in one go. Our segmentations are too big as is, so I am trying to figure out how to crop them into managable regions (4 or 8 or 16 ROIs, the fewer the better from data management purpose).</p>

---
