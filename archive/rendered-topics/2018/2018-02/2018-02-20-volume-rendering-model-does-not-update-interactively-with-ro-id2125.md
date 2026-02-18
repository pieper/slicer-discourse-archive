# Volume Rendering model does not update interactively with ROI

**Topic ID**: 2125
**Date**: 2018-02-20
**URL**: https://discourse.slicer.org/t/volume-rendering-model-does-not-update-interactively-with-roi/2125

---

## Post #1 by @chir.set (2018-02-20 15:14 UTC)

<p>Noticed in commit f649868e1. When a ROI is resized in the red view for example, the Volume rendering model is not refreshed interactively. It gets refreshed if the Display ROI button is next toggled off. When the latter is toggled on again, the 3D model gets badly displayed.</p>
<p>A screen capture video <a href="https://mega.nz/#!xE8TUY4a!WWV4d30cUCyhv2IewCMYTmFQlb9siYEJlz2iDDXf52o" rel="nofollow noopener">here</a> (39.3 MB).</p>
<p>Commit 0f398d948 is known to work normally.</p>
<p>On linux, Qt5, VTK9.</p>

---

## Post #2 by @lassoan (2018-02-21 02:14 UTC)

<p>I can reproduce the issue on Windows with latest preview (4.9) version. Cropping is broken (the same way as it is shown in the attached video above) if GPU raycasting method is selected and depth peeling is enabled.</p>
<p>Workarounds: use CPU raycasting method or disable depth peeling (by unchecking “Use depth peeling” checkbox in 3D view controller).</p>

---

## Post #3 by @lassoan (2018-02-21 02:17 UTC)

<p>I’ve added a ticket on the issue tracker: <a href="https://issues.slicer.org/view.php?id=4510">https://issues.slicer.org/view.php?id=4510</a></p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> Do you know if somebody is working on this already?</p>

---
