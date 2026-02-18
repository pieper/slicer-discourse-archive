# Magnify one part of segmentation

**Topic ID**: 17719
**Date**: 2021-05-21
**URL**: https://discourse.slicer.org/t/magnify-one-part-of-segmentation/17719

---

## Post #1 by @Aep93 (2021-05-21 05:58 UTC)

<p>Hello,<br>
Consider a segmentation that has multiple parts. Is it possible to magnify one or two of these parts by a specific factor (1.1, 1.2, etc.)? If yes, what is the command for it?<br>
Any help is greatly appreciated.</p>

---

## Post #2 by @lassoan (2021-05-21 12:42 UTC)

<p>You can apply a transform to a segmentation node, not to individual segments. So, if you only want to scale selected segments then you can temporarily move them out to a separate segmentation, apply a transform to that, and then move those back to the original segmentation.</p>
<p>Alternatively, you can simply grow a segment in a segmentation by using Margin effect.</p>

---

## Post #3 by @Aep93 (2021-05-22 02:00 UTC)

<p>Thank you so much <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---
