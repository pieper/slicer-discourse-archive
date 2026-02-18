# How can extend the trajectories in volume reslice driver (IGT)

**Topic ID**: 38359
**Date**: 2024-09-13
**URL**: https://discourse.slicer.org/t/how-can-extend-the-trajectories-in-volume-reslice-driver-igt/38359

---

## Post #1 by @Hossam_Elkady (2024-09-13 03:36 UTC)

<p>I would like to try to extend a line from the end of a stylus tip modeled by a needle in order to see the trajectory that is planned by the stylus at that angle in the 3 views of the scans (red , green , yellow windows)</p>

---

## Post #2 by @lassoan (2024-09-13 03:38 UTC)

<p>You can add a model that extends beyond the tip of your tool and move it with the same transform as the stylus.</p>

---

## Post #3 by @Hossam_Elkady (2024-09-13 11:41 UTC)

<p>I tried this approach, but it only works in the 3D model view. I need the trajectory to be applied to the MRI scans instead.</p>
<p>Thanks in advance</p>

---

## Post #4 by @lassoan (2024-09-13 12:39 UTC)

<p>It works on slice views as well. Display of models in slice views may be disabled by default but you can enable it in Models module → Display → Slice display → Visibility. You can set mode to <code>Distance encoded projection</code> if you want to show the trajectory in views that are not aligned with the trajectory.</p>

---
