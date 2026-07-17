---
topic_id: 47613
title: "What is the difference between GetColor() and GetSelectedColor() in display node?"
date: 2026-07-14
url: https://discourse.slicer.org/t/47613
last_bumped: 2026-07-16T06:22:00.483Z
---

# What is the difference between GetColor() and GetSelectedColor() in display node?

**Topic ID**: 47613
**Date**: 2026-07-14
**URL**: https://discourse.slicer.org/t/what-is-the-difference-between-getcolor-and-getselectedcolor-in-display-node/47613

---

## Post #1 by @Victor_Wayne (2026-07-14 04:24 UTC)

<p>Hi,</p>
<p>The question is, as the title says, what is the difference between the color property and the selected color propertly of a display node?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @cpinter (2026-07-14 14:57 UTC)

<p>In the practical sense, the difference is that you need to use <code>GetSelectedColor</code> instead of <code>GetColor</code> for markups, otherwise <code>GetColor</code>.</p>
<p>From the Markups documentation:<br>
“Markups have `Color` and `SelectedColor` properties. `SelectedColor` is used if all control points are in “selected” state, which is the default. So, in most cases `SetSelectedColor` method must be used to change markups node color.”</p>

---

## Post #3 by @Victor_Wayne (2026-07-16 06:22 UTC)

<p>Thank you for your help</p>

---
