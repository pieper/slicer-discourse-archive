# Field interpolation from set of 2D slices (3D volume)

**Topic ID**: 13494
**Date**: 2020-09-15
**URL**: https://discourse.slicer.org/t/field-interpolation-from-set-of-2d-slices-3d-volume/13494

---

## Post #1 by @loubna (2020-09-15 19:06 UTC)

<p>Hi;</p>
<p>I have a stack of 2D images (3d image Data). each 2d image represent a distance field computed from contour (contour of slicerRT) , I want to interpolate pixel by pixel the 2D images  using a cubic spline interpolation? but I have no idea how can I do that?</p>
<p>any suggestion will be appreaciated</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-09-15 19:10 UTC)

<p>You can use “Resample Scalar/Vector/DWI Volume” module for this. Set interpolation type to <code>bs</code>.</p>

---

## Post #3 by @loubna (2020-09-15 19:41 UTC)

<p>thank you very much for answer. ResampleScalarVolume.cxx uses ITK filters, is it possible to use vtkImageBSplineInterpolator instead?</p>

---

## Post #4 by @lassoan (2020-09-15 20:58 UTC)

<p>You need to take care of image axis directions in some way (VTK8 only supports non-rotated axes) and proper prefiltering but it should be usable, too.</p>

---

## Post #5 by @lassoan (2021-01-30 12:34 UTC)

<p>A post was split to a new topic: <a href="/t/computer-slows-down-after-volume-is-oversampled/15743">Computer slows down after volume is oversampled</a></p>

---
