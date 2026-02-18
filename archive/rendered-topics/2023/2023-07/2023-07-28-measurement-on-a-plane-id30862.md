# Measurement on a plane

**Topic ID**: 30862
**Date**: 2023-07-28
**URL**: https://discourse.slicer.org/t/measurement-on-a-plane/30862

---

## Post #1 by @mohammed_alshakhas (2023-07-28 19:12 UTC)

<p>is it possible to snap drawing points / measurements on a plane made in markups?</p>
<p>if not any suggestion</p>

---

## Post #2 by @chir.set (2023-07-28 20:12 UTC)

<p>Here’s one way to do that, there may be simpler ways.</p>
<p>Reformat a slice view to the plane, i.e., the slice view and the plane have the same normal.</p>
<p>You can get the first control point of the plane with GetNthControlPointPositionWorld(), and the plane’s normal with GetNormalWorld(). Next is to get a tangent for this normal, you can use vtkMath::Perpendiculars() for that. With these information, you can reformat a slice view using SetSliceToRASByNTP().</p>
<p>The slice view will reorient itself such that it contains the plane. It’s then trivial to place points in the slice view for whatever purpose.</p>
<p>You can then script all these for future needs. Such a script lies <a href="https://github.com/chir-set/RcHacks7" rel="noopener nofollow ugc">here</a>.</p>

---

## Post #3 by @mohammed_alshakhas (2023-07-28 20:34 UTC)

<p>Thank you for feedback . I’m working with stl model only . No Dicom . Trying to measurement some pre post surgery.  Because nature of the models I needed to measure  on a plane  but point won’t snap to it</p>

---
