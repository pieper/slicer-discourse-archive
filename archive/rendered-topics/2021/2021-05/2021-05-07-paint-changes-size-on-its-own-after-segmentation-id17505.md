# Paint changes size on its own after segmentation

**Topic ID**: 17505
**Date**: 2021-05-07
**URL**: https://discourse.slicer.org/t/paint-changes-size-on-its-own-after-segmentation/17505

---

## Post #1 by @veradam (2021-05-07 13:36 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Segmentation done by Paint not to change size on its own<br>
Actual behavior: I am segmenting 2D slices of a 3D CT scan. I have been using 2D Paint which seemed to be working very well on the spot. However, after a little while, all the segmentations made with Paint kept shrinking on their own.<br>
Can you please advise ?</p>

---

## Post #2 by @lassoan (2021-05-21 18:04 UTC)

<p>Most likely the segmentation is still perfectly in sync, you just have large spacing between slices and you positioned the slice view a bit off from the slice centers. Since the underlying grayscale volume is interpolated, but segmentations are binary labelmaps, which cannot be smoothly interpolated, you can see slight difference. You can solve this by resampling (and cropping as much as possible) the input volume before segmentation to have isotropic spacing.</p>
<p>If you believe you have a different problem then please post screenshots, video, or your scene (upload somewhere and post the link here); or provide step-by-step instruction for reproducing the unexpected behavior.</p>

---
