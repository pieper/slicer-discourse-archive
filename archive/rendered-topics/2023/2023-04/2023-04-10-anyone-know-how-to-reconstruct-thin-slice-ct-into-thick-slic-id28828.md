# Anyone know how to reconstruct thin-slice CT into thick-slice CT with 3D-slicer.

**Topic ID**: 28828
**Date**: 2023-04-10
**URL**: https://discourse.slicer.org/t/anyone-know-how-to-reconstruct-thin-slice-ct-into-thick-slice-ct-with-3d-slicer/28828

---

## Post #1 by @guokjdaks (2023-04-10 16:26 UTC)

<p>Operating system:windows10<br>
Slicer version:5.0.3<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @turtleizzy (2023-04-11 02:56 UTC)

<p>If you want to replicate what you get for thin-slice and thick-slice scans from CT scanners, this is generally a hard problem because they essentially underwent different reconstruction processes from the source sinogram (which is not generally available) involving parameters and algorithms proprietary to the scanner producers.</p>
<p>However, if all you want is thick-slices, you can use some projection (for example, average intensity projection) to achieve that. SimpleITK has <a href="https://simpleitk.org/doxygen/latest/html/classitk_1_1simple_1_1MeanProjectionImageFilter.html" rel="noopener nofollow ugc">MeanProjectionImageFilter</a> and <a href="https://simpleitk.org/doxygen/latest/html/classitk_1_1simple_1_1BoxMeanImageFilter.html" rel="noopener nofollow ugc">BoxMeanImageFilter</a> and you can access those from Simple Filters in the Filter menu.</p>

---

## Post #3 by @lassoan (2023-04-11 04:56 UTC)

<p>MeanProjectionImageFilter would collapse all the slices into a single slice, which may not be what <a class="mention" href="/u/guokjdaks">@guokjdaks</a> needs.</p>
<p>BoxMeanImageFilter should work well to create thick slices. After applying this filter, you can use “Resample Scalar Volume” to have slice spacing that matches the slice thickness (to avoid overlap between slices).</p>

---
