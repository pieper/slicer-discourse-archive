# Line Width for a centerline model has no effect in the Slice Display section

**Topic ID**: 20572
**Date**: 2021-11-10
**URL**: https://discourse.slicer.org/t/line-width-for-a-centerline-model-has-no-effect-in-the-slice-display-section/20572

---

## Post #1 by @torquil (2021-11-10 21:22 UTC)

<p>I have used the Extract Centerline module to generate a model. I would like to increase its thickness when showing it in the 2d slice view, but when go to its properties, and select Display - Slice Display, the setting for line width has no effect. I have selected Mode: intersection, but the “line width” has no effect. The one-dimensional curve is still showing as a single pixel, even when increasing the setting up to 10px. In the “3D Display” section, the line width works, but not in the “Slice display” section.</p>
<p>Btw, I also imported the centerline model into a segmentation, and then tried the “Margin: grow” segmentation tool on it, but nothing happens to the thickness of the curve then either. The “Margin: grow” tool has always worked for me before. Is there a problem with it when it acts on a “one-dimensional” structure resulting from importing a centerline model into a segmentation?</p>
<p>I’m using todays 3D Slicer preview release on Linux.</p>
<p>Best regards,<br>
Torquil Sørensen, Norway</p>

---

## Post #2 by @Nate_W (2024-01-18 22:12 UTC)

<p>Hey, ever figure it out by chance? I’m having the same issue</p>

---
