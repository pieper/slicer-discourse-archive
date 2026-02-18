# Muscle Fat Segmentation

**Topic ID**: 30726
**Date**: 2023-07-21
**URL**: https://discourse.slicer.org/t/muscle-fat-segmentation/30726

---

## Post #1 by @jmathew (2023-07-21 14:00 UTC)

<p>Hello,</p>
<p>I am trying to separate fat and muscle on an MRI, and would like to be able to have a count of pixel/voxel of any muscle that I would outline. Currently I am measuring the CSA of various muscles on an Axial MRI. Any and all help is appreciated. Thank you!</p>

---

## Post #2 by @pieper (2023-07-21 14:49 UTC)

<p>The signal will vary a lot depending on the MRI sequence, but if you can visually identify a threshold that separates the two tissue types then you can use Segment Statistics to quantify the ration in a segmented muscle.</p>

---
