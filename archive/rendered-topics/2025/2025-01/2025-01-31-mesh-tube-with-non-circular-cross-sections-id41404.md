# Mesh tube with non circular cross sections

**Topic ID**: 41404
**Date**: 2025-01-31
**URL**: https://discourse.slicer.org/t/mesh-tube-with-non-circular-cross-sections/41404

---

## Post #1 by @Paula_Feldman (2025-01-31 11:28 UTC)

<p>Hi! I´m using vmtkCenterlineModeller and vmtkMarchingCubes to mesh a tubular centerline. Now instead of circular cross sections I have several radius values(a spline) for each centerline point. is there a vmtk script to model it instead of CenterlineModeller?</p>

---

## Post #2 by @chir.set (2025-04-03 21:24 UTC)

<p>I am not sure to have a full understanding of your requirement. It seems that you have a centerline with radius values at each point of the centerline and you expect a tube from a script.</p>
<p>You may consider <a href="https://gitlab.com/chir-set/RcHacks7/-/blob/900664b75fca04210a065f1324d7fae0214eb559/13-MISToTube.py.txt#L62" rel="noopener nofollow ugc">this script</a>.</p>
<p>Alternatively, you may consider the ‘Edit centerline’ module in the ‘SlicerVMTK’ extension.</p>

---
