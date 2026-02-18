# Default center of rotation

**Topic ID**: 14584
**Date**: 2020-11-13
**URL**: https://discourse.slicer.org/t/default-center-of-rotation/14584

---

## Post #1 by @janneke_slicer (2020-11-13 09:04 UTC)

<p>Hello,</p>
<p>I am rotating an image in the Transforms module. I am wondering what the default center of rotation point is, and if I can extract that point in world coordinates? Or is this simply the image origin?</p>
<p>Thank you.</p>
<p>Janneke</p>

---

## Post #2 by @Fernando (2020-11-13 12:47 UTC)

<p>Hi, Janneke. The default center of rotation is the origin of the physical coordinates, where (R, A, S) = (0, 0, 0) mm. This is typically not the voxel with index (0, 0, 0) of the image, which is where the image origin is.</p>

---

## Post #3 by @janneke_slicer (2020-11-13 13:46 UTC)

<p>Hi Fernando,</p>
<p>Thank you for your quick response.<br>
That makes sense and solves my problems, thank you.</p>
<p>Janneke</p>

---
