# Free Form Deformation

**Topic ID**: 4503
**Date**: 2018-10-23
**URL**: https://discourse.slicer.org/t/free-form-deformation/4503

---

## Post #1 by @Abdelkhalek (2018-10-23 14:38 UTC)

<p>Hi,<br>
How can I perform an interaction with widgets consistently in 2D Widgets based on a fast free-form deformation model ?<br>
Thank you in advance</p>

---

## Post #2 by @lassoan (2018-10-23 15:04 UTC)

<p>You can define a free-form deformation field (thin-plate spline transform) by using Fiducial Registration Wizard module in SlicerIGT extension. You can define corresponding landmarks using markup fiducials in 2D and 3D views. You can move around points and the transformation is updated in real-time.</p>

---

## Post #3 by @Abdelkhalek (2018-10-28 12:23 UTC)

<p>Thank you Andras for your support.<br>
I tried to adopt the SlicerIGT extension but it does not fill my request.<br>
Actually, my idea is to perform a mouse press event for the mesh(attached) and to drag and drop it based on the FFdeformation. This drag and drop should update the 3D mesh in real-time.</p>

---
