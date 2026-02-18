# How to get 'Axes.vtp'?

**Topic ID**: 28572
**Date**: 2023-03-25
**URL**: https://discourse.slicer.org/t/how-to-get-axes-vtp/28572

---

## Post #1 by @jumbojing (2023-03-25 13:50 UTC)

<p>I want to use the orientation marker ‘Axes.vtp’, but Howto to get the ‘Axes.vtp’?</p>
<p>like👇:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/feef6315af064a36fe38b741904d7b8818e38511.png" alt="image" data-base62-sha1="Anga2h7I7RcSD7sYyjoBrJgSzDz" width="212" height="202"></p>

---

## Post #2 by @lassoan (2023-03-26 03:23 UTC)

<p>There is no such thing in Slicer as <code>Axes.vtp</code>. The coordinate system axes is a complex object consisting of 3D actors (lines and cones) and 2D actors (labels that always face the camera), therefore it could not be stored in a single 3D polydata file. Instead, this object is generated in code.</p>

---
