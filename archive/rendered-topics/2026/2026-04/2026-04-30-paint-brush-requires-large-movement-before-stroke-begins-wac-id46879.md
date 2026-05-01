---
topic_id: 46879
title: "Paint Brush Requires Large Movement Before Stroke Begins Wac"
date: 2026-04-30
url: https://discourse.slicer.org/t/46879
---

# Paint brush requires large movement before stroke begins — Wacom Intuos M tablet

**Topic ID**: 46879
**Date**: 2026-04-30
**URL**: https://discourse.slicer.org/t/paint-brush-requires-large-movement-before-stroke-begins-wacom-intuos-m-tablet/46879

---

## Post #1 by @Alexander_Pfeifer (2026-04-30 17:53 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.10.0</p>
<p>When using the Paint effect in Segment Editor with a Wacom Intuos M tablet on Windows, the brush requires a large physical movement before it starts painting. A short movement is treated as a single click. With a mouse this doesn’t happen. Already tried: <code>slicer.app.startDragDistance = 1</code>, <code>effect.setMinimumPaintPointDistance(0)</code>, <code>effect.setDelayedPaint(False)</code>, Windows Ink off, Wacom driver settings adjusted where possible. The threshold appears to be in the C++ Paint effect and is not reachable from Python.</p>

---
