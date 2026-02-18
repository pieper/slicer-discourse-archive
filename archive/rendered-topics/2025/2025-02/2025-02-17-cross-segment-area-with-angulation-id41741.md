# Cross segment area with angulation

**Topic ID**: 41741
**Date**: 2025-02-17
**URL**: https://discourse.slicer.org/t/cross-segment-area-with-angulation/41741

---

## Post #1 by @N.Maagdenberg (2025-02-17 14:33 UTC)

<p>Operating system: Windows<br>
Slicer version: 5.6.2.<br>
Expected behavior: I am using segment editor to measure the cross sectional area of the paravertebral muscles at level C3, in different angles to mimick possible head tilt variations (mostly chin to chest or neck extension). I already found the sandbox extension which makes it possible to get the cross segment area in mm2, but when I change the angle the segment gets divided over multiple slices. I’ve tried adding these up, but get outrageously high numbers, so I was wondering if the CSA as measured is still accurate when changing the<br>
rotation.</p>
<p>I’ve also tried using the segment statistics and taking the surface area, but those calculations seem even further off.</p>
<p>Is there any way of getting a cross-sectional area measurement while also changing the rotation/angulation of the scan?</p>

---

## Post #2 by @chir.set (2025-02-17 20:14 UTC)

<p>I’m not sure to have fully understood your requirement since your post is not backed by images. In case you want to cut segments with an arbitrary plane and calculate the cut surface area, you may consider the<code> 'Stenosis measurement: 2D'</code> module in the <code>SlicerVMTK</code> extension.</p>

---
