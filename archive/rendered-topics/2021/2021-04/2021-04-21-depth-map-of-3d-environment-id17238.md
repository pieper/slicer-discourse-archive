# Depth map of 3D environment

**Topic ID**: 17238
**Date**: 2021-04-21
**URL**: https://discourse.slicer.org/t/depth-map-of-3d-environment/17238

---

## Post #1 by @ifried01 (2021-04-21 19:33 UTC)

<p>Hi All,</p>
<p>Is it possible to generate a depth map of the 3D environment in Slicer? I have looked around a bit and don’t believe this exists.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2021-04-21 20:11 UTC)

<p>Do you mean of the rendered scene?  You can get it with a bit of programming (get the vtk render window and read out the depth image).  Something like <a href="https://vtk.org/Wiki/VTK/Examples/Cxx/Utilities/ZBuffer">this</a>.</p>

---

## Post #3 by @ifried01 (2021-04-21 20:56 UTC)

<p>Yes, something like a segmentation.</p>
<p>Great, thank you! I’ll take a look and reach back out if I have any questions</p>

---
