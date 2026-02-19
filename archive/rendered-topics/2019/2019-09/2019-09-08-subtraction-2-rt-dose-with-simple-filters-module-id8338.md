---
topic_id: 8338
title: "Subtraction 2 Rt Dose With Simple Filters Module"
date: 2019-09-08
url: https://discourse.slicer.org/t/8338
---

# Subtraction 2 RT Dose with Simple filters module

**Topic ID**: 8338
**Date**: 2019-09-08
**URL**: https://discourse.slicer.org/t/subtraction-2-rt-dose-with-simple-filters-module/8338

---

## Post #1 by @aseman (2019-09-08 21:44 UTC)

<p>Slicer version:4.8.1<br>
Hi 3D Slicer experts and all<br>
I have 2 RT Dose  whit different Image Dimension and Image origin, which were exported from TPS.  I want to subtract them  with Subtract image filter in simple filters module. but the following error is displayed. How can I subtract this RT Doses?<br>
Thanks a lot</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1fc5394759d59921e4ba17cccbf6c89a5ac1711e.png" alt="subtract" data-base62-sha1="4x3lNcnvPBSshCNaFpLrAkuAKvA" width="501" height="195"></p>

---

## Post #2 by @cpinter (2019-09-08 22:44 UTC)

<p>You could use the DoseAccumulation module (from the SlicerRT extension) and set the weight of the subtracted image to -1.</p>

---
