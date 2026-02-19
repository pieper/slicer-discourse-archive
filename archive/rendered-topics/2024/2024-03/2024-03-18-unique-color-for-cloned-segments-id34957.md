---
topic_id: 34957
title: "Unique Color For Cloned Segments"
date: 2024-03-18
url: https://discourse.slicer.org/t/34957
---

# Unique color for cloned segments

**Topic ID**: 34957
**Date**: 2024-03-18
**URL**: https://discourse.slicer.org/t/unique-color-for-cloned-segments/34957

---

## Post #1 by @Yirzu (2024-03-18 14:48 UTC)

<p>Hello,</p>
<p>Color is assigned uniquely each time we add a new segment. However, this behavior does not apply when cloning segments; cloned segments appear to have the same color as the original one.</p>
<p>How can cloned segments have new/unique colors?</p>

---

## Post #2 by @lassoan (2024-03-18 14:53 UTC)

<p>This is intentional, as most of the time you want to use the same colors for the same things. For comparing multiple segmentations (e.g., with and without warping) it may be better to preserve color and change other style. For example, we usually compare segmentations by setting one of them to be shown as <em>slice fill</em> only and the other as <em>slice outline</em> only.</p>

---
