# Seperation plane following closed curve

**Topic ID**: 30995
**Date**: 2023-08-05
**URL**: https://discourse.slicer.org/t/seperation-plane-following-closed-curve/30995

---

## Post #1 by @mohammed_alshakhas (2023-08-05 11:13 UTC)

<p>I often work with complicated osteotomy geometry that doesn’t follow straight lines or curves.<br>
I need to experiment with many shapes to see the outcome.  it would be so good if I could draw a closed curve and a plane is fitted through it<br>
thanks</p>

---

## Post #2 by @lassoan (2023-08-06 23:15 UTC)

<p>This feature is already available. Your can get the curve coordinate system (plane position, tangent, normal direction) at any curve point. There is also a nice module with a convenient GUI in SlicerVMTK extension: Cross-section analysis module.</p>

---

## Post #3 by @mohammed_alshakhas (2023-08-07 04:49 UTC)

<p>Placing curve is not the issue . The request is about having a fitted plane or planes in the closed curve area to perform the cut .</p>

---

## Post #4 by @lassoan (2023-08-07 07:55 UTC)

<p>I thought you need to fit the plane orthogonally to the curve. Fitting a plane in the curve points is even simpler. Have your tried using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/markups.html#edit-plane-markups">plane fit</a> mode? It draws the plane by fitting it on all the control points that you specify.</p>

---

## Post #5 by @lassoan (2023-08-07 11:21 UTC)

<p>A post was split to a new topic: <a href="/t/failed-to-load-nifti-file/31023">Failed to load nifti file</a></p>

---

## Post #6 by @mohammed_alshakhas (2023-08-07 17:11 UTC)

<p>never noticed before, and could not figure out how to use it .<br>
not clear how to select points and initiate fitting</p>

---
