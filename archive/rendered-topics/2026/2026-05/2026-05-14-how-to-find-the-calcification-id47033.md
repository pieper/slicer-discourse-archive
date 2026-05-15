---
topic_id: 47033
title: "How To Find The Calcification"
date: 2026-05-14
url: https://discourse.slicer.org/t/47033
---

# How to find the calcification?

**Topic ID**: 47033
**Date**: 2026-05-14
**URL**: https://discourse.slicer.org/t/how-to-find-the-calcification/47033

---

## Post #1 by @liam26 (2026-05-14 18:38 UTC)

<p>Hi, I’m looking for some help with finding arterial calcification. I’m working from MRIs, looking for illiac, portal, vena cava, etc. My current process looks something like:</p>
<p>Subtract all vertebrae from the artery (In case of segmentation overlap errors)<br>
Add segment → name = calcification_“segment” → Threshold = 130 to max → editable area = inside segment “segment”  →  modify other segments = allow overlap</p>
<p>Any advice would be greatly appreciated. Thanks!</p>

---
