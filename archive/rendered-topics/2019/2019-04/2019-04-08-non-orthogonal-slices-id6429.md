# Non orthogonal slices

**Topic ID**: 6429
**Date**: 2019-04-08
**URL**: https://discourse.slicer.org/t/non-orthogonal-slices/6429

---

## Post #1 by @pervin_huseyinova (2019-04-08 09:32 UTC)

<p>Hi, I was wondering if I can reslice my volume data in non orthogonal directions. So for example if axial is 0 degree slice and coronal is 90 degree slice, i would like to have 45 degree slices.</p>

---

## Post #2 by @stephan (2019-04-08 12:00 UTC)

<p>You can use the “Reformat” module (Modules drop down -&gt; all modules -&gt; Reformat) to set the slice viewers to arbitrary orientations.<br>
It is helpful to have the Slice intersections visible while doing so. Show them by clicking the arrow next to the crosshair icon and check “Slice intersections” in the menu.</p>

---

## Post #3 by @pervin_huseyinova (2019-04-15 08:33 UTC)

<p>Thank you for answer. This method shows me non-orthogonal slices i want, but is there a way to download this new dicom slices and corresponding labels?</p>

---

## Post #4 by @lassoan (2019-04-15 15:05 UTC)

<p>You can resample the volume if you need to reformat the image slices. See <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" rel="nofollow noopener">oblique slice segmentation recipe</a> - section: Create resampled volume with rotated axes.</p>

---
