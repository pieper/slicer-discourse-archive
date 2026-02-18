# Making 2D measurements of a segmentation on an individual slice

**Topic ID**: 7886
**Date**: 2019-08-05
**URL**: https://discourse.slicer.org/t/making-2d-measurements-of-a-segmentation-on-an-individual-slice/7886

---

## Post #1 by @Yozer (2019-08-05 19:28 UTC)

<p>Hi everybody,</p>
<p>I am currently developing an extension for 3D Slicer. As part of this extension, I need to programatically make measurements of a segmentation on each individual layer of my volume (ie. vertical/horizontal diameter). I can do this for a single layer manually by placing a ruler across the segmentation, but that is obviously not a good solution for the entire segmentation. Can anyone show me a better way forward?</p>
<p>This is my first time posting on this forum. If there is any more information that you need to help me, please ask and I’ll edit my post.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2019-08-05 20:08 UTC)

<p>Would knowing the bounding box size (its axes aligned with segmentation axes) be enough for you? Or you would need bounding box size for each slice?</p>

---

## Post #3 by @Yozer (2019-08-05 20:58 UTC)

<p>I’m trying to find the minimum and maximum diameters. Eventually I’d also like to find other statistics like the area of each slice. I tried using bounding box size for the whole segment, but it introduced too much error to be really useful.</p>

---

## Post #4 by @lassoan (2019-08-06 01:18 UTC)

<p>If you need number of voxels (cross-section area by slice) then you can find a readily usable solution here: <a href="https://discourse.slicer.org/t/using-numpy-reslice-to-get-slices-of-segment/2257/3">Using numpy reslice to get slices of segment</a>. With small modifications of the script, you can compute extents, diameters, etc. for each slice.</p>

---

## Post #5 by @Yozer (2019-08-06 16:10 UTC)

<p>This is exactly what I’m looking for. Thanks for your help!</p>

---
