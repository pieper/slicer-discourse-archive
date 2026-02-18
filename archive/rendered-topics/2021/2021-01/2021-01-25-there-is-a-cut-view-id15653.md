# There is a "cut view"?

**Topic ID**: 15653
**Date**: 2021-01-25
**URL**: https://discourse.slicer.org/t/there-is-a-cut-view/15653

---

## Post #1 by @Polyynom (2021-01-25 13:37 UTC)

<p>Hello dear users!</p>
<p>I need to modify model inside. There is a “cut view” to deside this? Can I slice my model, modify it futher and and then return the sliced part.</p>
<p>Thank you for your attention!</p>

---

## Post #2 by @slicer365 (2021-01-25 13:42 UTC)

<p>You can convert the model into segmentation, and then use logical operations and scissors</p>

---

## Post #3 by @lassoan (2021-01-25 21:09 UTC)

<p>If you don’t want to modify a model, just temporarily clip it with a plane (or multiple planes) then you can use clipping feature in <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Models">Models module</a>. Select models you want to clip, enable “Clip selected model” in Clipping planes section, and move slice view planes (either using sliders or the Reformat widget).</p>

---
