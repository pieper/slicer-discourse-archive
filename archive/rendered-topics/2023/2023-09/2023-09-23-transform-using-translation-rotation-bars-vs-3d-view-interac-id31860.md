---
topic_id: 31860
title: "Transform Using Translation Rotation Bars Vs 3D View Interac"
date: 2023-09-23
url: https://discourse.slicer.org/t/31860
---

# Transform using translation-rotation bars vs 3D view interaction

**Topic ID**: 31860
**Date**: 2023-09-23
**URL**: https://discourse.slicer.org/t/transform-using-translation-rotation-bars-vs-3d-view-interaction/31860

---

## Post #1 by @Mehran (2023-09-23 09:40 UTC)

<p>Hi all,<br>
Does anyone knows why changing a transform using translation-rotation slide bar (in transform module) make sense (small change shows reasonable change in transformation matrix), but change transformation using 3D interaction, does not make sense (very tiny change, hugely changes transformation matrix). Do they used different methods/origins? how we can convert them?<br>
Thanks for any help</p>

---

## Post #2 by @Mehran (2023-09-28 08:43 UTC)

<p>Indeed, I found that the transformation applies on objects respect to the origin of the object though I needed it respect to centre of the object.</p>

---
