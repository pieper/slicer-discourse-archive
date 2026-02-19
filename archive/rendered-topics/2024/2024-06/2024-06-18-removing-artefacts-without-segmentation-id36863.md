---
topic_id: 36863
title: "Removing Artefacts Without Segmentation"
date: 2024-06-18
url: https://discourse.slicer.org/t/36863
---

# Removing artefacts without segmentation

**Topic ID**: 36863
**Date**: 2024-06-18
**URL**: https://discourse.slicer.org/t/removing-artefacts-without-segmentation/36863

---

## Post #1 by @capucinelab (2024-06-18 12:29 UTC)

<p>Hello,<br>
I would like to know if you know of a technique for removing artifacts (like surgical masks) without using segmentation?</p>
<p>It’s part of a methodological study.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @muratmaga (2024-06-18 18:05 UTC)

<p>A way to remove something from a volume without segmentation would be extracting sub regions by creating an ROI and using it to crop the volume with. It works only for very simple samples, or artifacts that are the boundaries…</p>
<p>Otherwise segmentation and masking is your only real solution.</p>

---

## Post #3 by @lassoan (2024-06-18 19:19 UTC)

<p>Surgical masks are usually made of mostly thin and light materials, so they can be probably separated from the body surface by simple automatic processing algorithms. There maybe some metal parts, but those do not touch the body surface, so those should not cause any trouble either.</p>
<p>You may find that the <a href="https://github.com/PerkLab/SlicerSandbox?tab=readme-ov-file#remove-ct-table">Remove CT table</a> module in Sandbox extension can remove surgical masks, too.</p>

---
