# Editing of segmentation on slices of arbitrary orientation

**Topic ID**: 19977
**Date**: 2021-10-03
**URL**: https://discourse.slicer.org/t/editing-of-segmentation-on-slices-of-arbitrary-orientation/19977

---

## Post #1 by @sronen71 (2021-10-03 13:45 UTC)

<p>Hi,<br>
Segment Editor allows editing of segmentation on slices of arbitrary orientation -<br>
according to <a href="https://lassoan.github.io/SlicerSegmentationRecipes/ObliqueSliceSegmentation/" class="inline-onebox" rel="noopener nofollow ugc">Overview | 3D Slicer segmentation recipes</a>.<br>
The above recipe describes a potential issue of stripe artifacts, and offers two solutions. I’m interested in solution A, ignore stripes.<br>
My question is more basic, though: how do I control the orientation of the segmentation slices in the first place (without resampling the volume)?<br>
Note I’m less interested in option B (Create resampled volume with rotated axes).<br>
Thank you.</p>

---

## Post #2 by @lassoan (2021-10-03 20:11 UTC)

<p>You can set the segmentation geometry (sey the axis orientation) in a number of different ways, but using the Crop volume module is probably the simplest method. Note that you don’t need to keep the resampled volume around: you can delete it right after you used it to specify the segmentation geometry.</p>
<p>You can also use the “Specify geometry” button to set origin, spacing, axis direction, and extents using other volume, segmentation, or ROI nodes as reference.</p>

---

## Post #3 by @hherhold (2021-10-03 20:49 UTC)

<p>If you have slice intersections turned on in the Axial/Saggital/Coronal views, you can hold option and command on a Mac (I think likely alt &amp; control on windows?) and click and drag in the slice view to rotate the slice axes interactively and arbitrarily. You can switch back to the original view by selecting “Axial”, “Saggital”, or “Coronal” in the drop down toolbar of each view - it will say “Reformat” for the view once you’ve rotated the slice axis.</p>

---
