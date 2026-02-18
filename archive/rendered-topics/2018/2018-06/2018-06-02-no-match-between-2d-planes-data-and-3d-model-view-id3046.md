# No match between 2D planes data and 3D model view

**Topic ID**: 3046
**Date**: 2018-06-02
**URL**: https://discourse.slicer.org/t/no-match-between-2d-planes-data-and-3d-model-view/3046

---

## Post #1 by @Ricardo_Mesquita (2018-06-02 14:34 UTC)

<p>Hi all,<br>
After perform registration the 3D model goes to a different position in the 3D viewer. This occurs due to the registration transformation matrix. Thus, if i set the slice planes visible Im not able to see where the slice planes intersect the 3D model because the slice planes and the 3D model are not in the same “origin”.<br>
Does anyone know how can i solve this?<br>
Thank you!</p>

---

## Post #2 by @lassoan (2018-06-02 15:14 UTC)

<p>The transform that is computed by registration is automatically applied to the moving volume. If there are models, markup fiducial, etc. that you would like to move along with your volume then apply the computed transform to those nodes, too (you can use Transforms or Data module to apply transforms to nodes).</p>

---
