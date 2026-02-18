# How to get the Needle model tip position in the World coordinate？

**Topic ID**: 16156
**Date**: 2021-02-23
**URL**: https://discourse.slicer.org/t/how-to-get-the-needle-model-tip-position-in-the-world-coordinate/16156

---

## Post #1 by @chenyx (2021-02-23 09:52 UTC)

<p>Dear friends， i wanna get the position of the needle model which created by the module “IGT/CreateModels”</p>

---

## Post #2 by @lassoan (2021-02-23 12:58 UTC)

<p>Coordinate of the needle tip is (0,0,0). See complete definition of the StylusTip coordinate system <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/CommonCoordinateSystems.html">here</a>.</p>

---

## Post #3 by @chenyx (2021-02-23 14:32 UTC)

<p>Thx, but i insert transform with the stylus model, so the modified position follow the changable transform. i wanna get the current position.<br>
Can you share me some method to get the stylus tip position？</p>

---

## Post #4 by @lassoan (2021-02-23 14:36 UTC)

<p>Current position of the needle tip is the translation part (4th column) of the the matrix you get from <a href="http://apidocs.slicer.org/master/classvtkMRMLTransformNode.html#a5d2d93382aa7da7ec3d9a27987305bce">GetMatrixTransformToWorld()</a> (called on the parent transform).</p>

---

## Post #5 by @chenyx (2021-02-23 14:40 UTC)

<p>Thank you very much.</p>

---
