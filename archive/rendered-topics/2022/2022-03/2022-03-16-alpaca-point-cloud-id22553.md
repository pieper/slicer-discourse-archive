# ALPACA point cloud 

**Topic ID**: 22553
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/alpaca-point-cloud/22553

---

## Post #1 by @carterrt (2022-03-16 23:43 UTC)

<p>When using ALPACA to place a point cloud on a bone model. Is it safe to assume that no landmarks will be placed on the surfaces of the internal cavities and spongy bone? I am only looking to analyze external bone shape, not internal anatomy.</p>

---

## Post #2 by @muratmaga (2022-03-17 10:18 UTC)

<p>If your rigid registration is quite good between your target and source model (that contains the landmarks), yes it is safe to assume the transferred landmarks will also be on the surface.</p>
<p>If the two models are very different in shape and size, and one model is inside the other at some points, you may need to pay attention to the projection parameter and double check that landmarks are not transferred to the internal surface.</p>

---
