# How do I take linear measurements on 3D Volume rendered surface?

**Topic ID**: 26230
**Date**: 2022-11-14
**URL**: https://discourse.slicer.org/t/how-do-i-take-linear-measurements-on-3d-volume-rendered-surface/26230

---

## Post #1 by @KSL (2022-11-14 14:27 UTC)

<p>I have tried taking measurements on the skull after volume rendering as done from the tutorial <a href="https://youtu.be/xZwyW6SaoM4" class="inline-onebox" rel="noopener nofollow ugc">New "Surface cut" and "Mask volume" tools for 3D Slicer segment editor - YouTube</a> but my control points cannot be fixed onto the bone surface.</p>
<p>Operating system: windows 11<br>
Slicer version: 5.0.3<br>
Expected behavior: to be able to take linear measurements with the control points fixed onto the bone surface<br>
Actual behavior: the control points (the lines) get scattered in the 3D space even after locking the control points</p>

---

## Post #2 by @lassoan (2022-11-15 12:15 UTC)

<p>Is “Snap to visible surface” option is selected Markups module → Display → Advanced → 3D display → Placement mode?</p>
<p>What volume rendering technique do you use (CPU, GPU, multi-volume)?</p>
<p>Did the volume-rendered surface appear opaque or semi-transparent? Could you provide a screenshot?</p>

---

## Post #3 by @KSL (2022-11-16 05:27 UTC)

<p>Thank you, Sir</p>
<p>My problem gets resolved after following your instructions.<br>
Placement mode (Snap to Visible surface)</p>
<p>Volume rendering technique (GPU)</p>

---
