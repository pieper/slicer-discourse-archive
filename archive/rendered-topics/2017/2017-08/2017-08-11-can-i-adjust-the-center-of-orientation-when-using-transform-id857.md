# Can I adjust the center of orientation when using 'transform module'?

**Topic ID**: 857
**Date**: 2017-08-11
**URL**: https://discourse.slicer.org/t/can-i-adjust-the-center-of-orientation-when-using-transform-module/857

---

## Post #1 by @Ramttoong (2017-08-11 16:08 UTC)

<p>Casue I don’t know where the center of rotation is, I can’t predict the movement of them. (When using ‘transform module’)</p>

---

## Post #2 by @pieper (2017-08-11 19:50 UTC)

<p>True, we don’t have that feature now.  Best suggestion might be to write a small python script to implement rotation around a point (the necessary math is in any computer graphics book).</p>
<p>It could be generally useful to allow people to select a mrml node to use as the rotation point.  You could add this as a feature request at <a href="http://issues.slicer.org">issues.slicer.org</a>.</p>

---

## Post #3 by @lassoan (2017-08-11 20:13 UTC)

<p>Manual alignment with subsequent rotations and translations is a long, iterative process. We have not invested time into trying to make it a bit less painful because there are much better methods for manual registration.</p>
<p>I recommend using landmark-based registration: you specify corresponding point locations in the objects that you need to align and Slicer computes the optimal transform automatically, in real-time. It is not an iterative process, but a fast, direct method that optimizes translation and rotation simultaneously (and you may also allow scaling, shearing, or local warping).</p>
<p>If you need to register slightly misaligned images then use <code>Landmark registration</code> module. If you need to register highly misaligned images or other objects then use <code>Fiducial registration wizard</code> module in <code>SlicerIGT</code> extension.</p>

---

## Post #4 by @Michael_Hardisty (2017-08-11 20:48 UTC)

<p>Hi Woo-ram,</p>
<p>We have done something similar to what you are suggesting by nesting<br>
transforms.  We created ‘local’ rotations by rotating an object that was<br>
already translated to the origin.  We then put the rotating transform<br>
within another transform that translated it back to position.  The effect<br>
is that rotations appear to be local, when adjusting the sliders in the<br>
transform editor.</p>
<p>Michael</p>

---
