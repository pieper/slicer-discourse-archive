# Breaking up 3D volume segmentation

**Topic ID**: 15700
**Date**: 2021-01-27
**URL**: https://discourse.slicer.org/t/breaking-up-3d-volume-segmentation/15700

---

## Post #1 by @lekremer (2021-01-27 19:54 UTC)

<p>I have segmented a full kidney under one segmentation. I want to run texture on just 1 slice of the volume. When I run pyradiomics, it computes texture of the full 3D volume of the kidney.</p>
<p>How do a breakup a segmentation into individual segmentations it is composed of?</p>
<p>I have tried the copy in the logical operators of the segment editor, but it copies all of the segmentations and not just the one I want.</p>
<p>best</p>

---

## Post #2 by @lassoan (2021-01-27 20:52 UTC)

<p>You can use Crop volume module to crop the volume to a single slice. If you need the segmentation to be single-slice volume, too, then you can export it to a labelmap volume, choosing the cropped volume node as reference geometry.</p>

---

## Post #3 by @lekremer (2021-01-28 15:34 UTC)

<p>thank you. I have been using the crop volume module but it still is giving my the entire series of MR images. I just want to work with selected single slice/image.</p>

---

## Post #4 by @lassoan (2021-01-28 16:13 UTC)

<p>You need to edit the ROI to include only a single slice and then click Apply.</p>

---
