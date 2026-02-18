# Liver visualization in 3D

**Topic ID**: 13747
**Date**: 2020-09-29
**URL**: https://discourse.slicer.org/t/liver-visualization-in-3d/13747

---

## Post #1 by @jax200 (2020-09-29 15:09 UTC)

<p>I wanted to also mention when using Threshold on an abdominal scan I can get a good 3D rendering on vasculature, but when I then add Paint/Seeding for the liver segment, the 3D view only shows slices and dots.  How to get the solid organ view?</p>

---

## Post #2 by @timeanddoctor (2020-09-30 09:24 UTC)

<p>Slicer can reconstrue any 3d image from segment.<br>
could you give some screen to explain your problem?</p>

---

## Post #3 by @cpinter (2020-09-30 09:27 UTC)

<p>Based on what you describe I have the feeling that you simply don’t click Apply. You need to do that for semi-automatic segmentation tools so that the preview is actually applied in the segment.</p>

---

## Post #4 by @jax200 (2020-09-30 18:21 UTC)

<p>Thank you <a class="mention" href="/u/timeanddoctor">@timeanddoctor</a> and <a class="mention" href="/u/cpinter">@cpinter</a>.  Indeed (new user) I did not click Apply.   All good now.</p>

---
