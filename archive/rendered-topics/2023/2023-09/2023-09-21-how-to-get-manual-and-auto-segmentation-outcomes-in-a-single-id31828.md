---
topic_id: 31828
title: "How To Get Manual And Auto Segmentation Outcomes In A Single"
date: 2023-09-21
url: https://discourse.slicer.org/t/31828
---

# How to get manual and auto-segmentation outcomes in a single image using dash and solid lines?

**Topic ID**: 31828
**Date**: 2023-09-21
**URL**: https://discourse.slicer.org/t/how-to-get-manual-and-auto-segmentation-outcomes-in-a-single-image-using-dash-and-solid-lines/31828

---

## Post #1 by @Js165 (2023-09-21 15:25 UTC)

<p>Hello folks,<br>
I’m attempting to present both manual and auto-segmentation outcomes in a single image. I want manual segmentation edges to be represented as dashed lines, and auto segmentation edges to be represented as solid lines. I’m currently getting solid lines for both structures. Could you please walk me through the stages so that I receive the desired results? Thank you in advance.</p>

---

## Post #2 by @lassoan (2023-09-22 03:12 UTC)

<p>Segmentation outline can only be displayed as a solid line and I don’t think anybody plans to implement displaying segment outline by a dashed line. However, you can distinguish the two very similar segmentations in slice views by using different color, outline thickness, or filling opacity. For example, we often compare very similar segmentations by displaying one with outline (no filling) and the other with filling (no outline).</p>

---

## Post #3 by @Js165 (2023-09-22 03:38 UTC)

<p>Thanks for the details. I’ll follow.</p>

---
