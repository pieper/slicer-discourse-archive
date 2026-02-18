# Saving control point phase

**Topic ID**: 31232
**Date**: 2023-08-18
**URL**: https://discourse.slicer.org/t/saving-control-point-phase/31232

---

## Post #1 by @admarques (2023-08-18 21:04 UTC)

<p>Operating system: Ubuntu 22.04.1<br>
Slicer version: 5.2.2 r31382<br>
Expected behavior: Control points save the physical position and the corresponding phase<br>
Actual behavior: Control points save only the physical position</p>
<p>I’m working with a dataset of ct images that contain different phases. I would like to select control points in the 2d view and distinguish them between phases. It looks like the default option only saves the physical position, but there is no information about which phase the point belongs to.<br>
Is it possible to include the phase information together with the physical position?</p>
<p>Thank you</p>

---

## Post #2 by @lassoan (2023-08-18 21:11 UTC)

<p>You can make markup point list to be a time sequence, using Sequences module: add a new sequence node and make the point list the proxy node of that sequence.</p>

---

## Post #3 by @admarques (2023-08-21 14:50 UTC)

<p>Thank you!<br>
In this way, the points look being stored in arrays. Do you know how I can assign these arrays to a Python variable?</p>

---
