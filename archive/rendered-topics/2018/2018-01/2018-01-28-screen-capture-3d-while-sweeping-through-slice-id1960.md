# Screen capture 3D while sweeping through slice

**Topic ID**: 1960
**Date**: 2018-01-28
**URL**: https://discourse.slicer.org/t/screen-capture-3d-while-sweeping-through-slice/1960

---

## Post #1 by @Justin_Cramer (2018-01-28 01:35 UTC)

<p>Using Slicer 4.9.0</p>
<p>In the Screen Capture extension, is there a way to capture the 3D window (“view1”) while sweeping through another slice (e.g. Red)? I want to capture the axial slice moving through the 3D model.</p>

---

## Post #2 by @lassoan (2018-01-28 02:12 UTC)

<p>You can capture a slice view sweep in 3D by enabling <code>Capture all views</code> option and keep “Red” as master view.</p>
<p>In the nightly version of tomorrow or later, you don’t need to keep the selected slice view visible in the current layout (so you can choose have 3D-only view while sweeping the Red slice view).</p>

---

## Post #3 by @Justin_Cramer (2018-01-28 02:29 UTC)

<p>That makes sense - thank you!</p>

---
