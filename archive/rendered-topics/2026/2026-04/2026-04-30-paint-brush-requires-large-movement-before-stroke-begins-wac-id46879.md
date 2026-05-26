---
topic_id: 46879
title: "Paint brush requires large movement before stroke begins — Wacom Intuos M tablet"
date: 2026-04-30
url: https://discourse.slicer.org/t/46879
last_bumped: 2026-05-04T19:57:31.296Z
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

## Post #2 by @ThomasVanParys (2026-05-01 08:27 UTC)

<p>I use the same tablet as you and encounter this problem for manual segmentation. Would love to hear any solutions to this (other than manually removing the over-segmented area!)</p>

---

## Post #3 by @lassoan (2026-05-04 19:57 UTC)

<p>There is no such property as <code>startDragDistance</code> and I’m not sure how you got the effect. Anyway, the correct code snippet (from <a href="https://discourse.slicer.org/t/segmentation-drawing-tablet/842/37">this post</a>):</p>
<pre><code class="lang-auto">paint=slicer.modules.segmenteditor.widgetRepresentation().self().editor.effectByName("Paint")
paint.delayedPaint=False
paint.minimumPaintPointDistance=3
</code></pre>

---
