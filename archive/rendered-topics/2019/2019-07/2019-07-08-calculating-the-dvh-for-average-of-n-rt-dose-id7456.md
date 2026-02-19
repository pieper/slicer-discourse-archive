---
topic_id: 7456
title: "Calculating The Dvh For Average Of N Rt Dose"
date: 2019-07-08
url: https://discourse.slicer.org/t/7456
---

# Calculating the DVH for average of n RT Dose

**Topic ID**: 7456
**Date**: 2019-07-08
**URL**: https://discourse.slicer.org/t/calculating-the-dvh-for-average-of-n-rt-dose/7456

---

## Post #1 by @aseman (2019-07-08 08:42 UTC)

<p>Slicer version: 4.10.1<br>
Hi 3D Slicer experts and all<br>
I have some RT Dose (for n patients) and I want to calculate DVH for average of these RT Doses. is it possible that I calculate a mean DVH instead of n DVH with 3D Slicer?<br>
Thanks a lot</p>

---

## Post #2 by @cpinter (2019-07-08 14:33 UTC)

<p>Instead of averaging the DVH, I’d average the dose volumes and then calculate a DVH on those.</p>
<p>First, obviously you need to make sure that your dose volumes are registered (register the CTs and apply transform on dose, see the SlicerRT IGRT tutorial for example). Then you can usethe Dose Accumulation module to average the doses. You can do this by setting equal weights that add up to one.</p>

---
