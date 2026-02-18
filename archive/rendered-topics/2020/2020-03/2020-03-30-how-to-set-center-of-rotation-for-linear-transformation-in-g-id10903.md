# How to set center of rotation for linear transformation in GUI

**Topic ID**: 10903
**Date**: 2020-03-30
**URL**: https://discourse.slicer.org/t/how-to-set-center-of-rotation-for-linear-transformation-in-gui/10903

---

## Post #1 by @Alex_Vergara (2020-03-30 11:08 UTC)

<p>When I use transformation module there is a way to rotate one volume to match the other, but I can’t control the center of rotation. I thought that by setting a fiducial point will do the trick but no.<br>
So, is there a way to set up the center of rotation? I just need to make a fiducial point the center of rotation</p>
<p>Wow! <a href="https://mantisarchive.slicer.org/view.php?id=3155" rel="nofollow noopener">2013!!!</a> I see this is already an <a href="https://github.com/Slicer/Slicer/issues/3155" rel="nofollow noopener">issue</a></p>

---

## Post #2 by @lassoan (2020-03-31 03:23 UTC)

<p>We haven’t implemented this feature because in general you cannot achieve optimal spatial alignment by performing rotation around a single point.</p>
<p>You can rotate around a point as shown in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_point">example in the script repository</a> but I would recommend to use better registration methods (landmark registration, surface registration, intensity-based image registration, etc.).</p>

---

## Post #3 by @juday (2020-03-31 16:23 UTC)

<p>You can change the origin (around which volume rotates) of the volume in “Volume” module. Click on center volume to move the origin of the selected volume.</p>
<p>After centering the volume, linear transforms should work in expected way.</p>

---

## Post #4 by @pieper (2020-03-31 19:45 UTC)

<p>You can also set up a transform hierarchy which allows you to simulate various robot arm-like motions.</p>

---
