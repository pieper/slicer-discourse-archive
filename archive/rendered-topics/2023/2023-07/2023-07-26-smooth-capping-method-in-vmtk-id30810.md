# Smooth Capping Method in VMTK

**Topic ID**: 30810
**Date**: 2023-07-26
**URL**: https://discourse.slicer.org/t/smooth-capping-method-in-vmtk/30810

---

## Post #1 by @iloliveira (2023-07-26 18:50 UTC)

<p>Hi all,<br>
I am trying to come up with a function to “cap” a clipped aneurysm sac surface with the goal to compute its “ostium” surface, i.e. the minimal surface that connects its 3D neck contour. Since I haven’t found any algorithm that implements a triangulated minimal surface of a 3D contour so far (working on it, but the solutions are not quite straightforward), I am experimenting with alternatives and the ‘smooth’ cap method available in VMTK via vtkvmtk seems a fine or close alternative to a true minimal surface. However, I could not understand how it builds the smooth surface that fills the open profile. Could someone explain what exactly it uses internally? Is it some form of splines to interpolate the surface?<br>
I really appreciate any help you can provide.<br>
Regards<br>
Iago</p>

---
