---
topic_id: 37312
title: "How To Register Donut Shaped Markers"
date: 2024-07-10
url: https://discourse.slicer.org/t/37312
---

# How to register donut-shaped markers

**Topic ID**: 37312
**Date**: 2024-07-10
**URL**: https://discourse.slicer.org/t/how-to-register-donut-shaped-markers/37312

---

## Post #1 by @lxedk (2024-07-10 18:38 UTC)

<p>I have several DICOM volumes containing scans with 7 donut shaped markers arranged in a known pattern. Is there a module to register each donut, to ultimately determine the 6 DOF pose of the pattern?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2024-07-11 02:36 UTC)

<p>It could be implemented the same way as described for sphere markers <a href="https://discourse.slicer.org/t/automatic-fiducial-registration/7099/4">here</a>. Details depend on whether the doughnut is fluid-filled (if yes then you need a robust registration algorithm for subpixel accuarcy matching in presence of an air bubble, for example, reslice along the doughnut axis of rotation and fit circles), whether the pivot point is in the center of gravity, etc.</p>
<p>Fiducial registration wizard module can automatically match two unsorted point lists up to 7 or so points, so once you have the point position, the registration should be fully automatic.</p>

---

## Post #3 by @lxedk (2024-07-17 19:15 UTC)

<p>Thank you for your response. I was previously considering general registration of a synthetic volume (created from a model of the donuts) to the scan itself. Would that be more robust in the potential case of a donut failing to be registered through the aforementioned techniques?</p>

---
