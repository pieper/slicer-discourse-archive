# The volume of segmentation changes

**Topic ID**: 29760
**Date**: 2023-05-31
**URL**: https://discourse.slicer.org/t/the-volume-of-segmentation-changes/29760

---

## Post #1 by @Andrey_22 (2023-05-31 23:58 UTC)

<p>Good afternoon. The patient took a different depth of inspiration on the studies. The volume and size of segmentation has changed. How can I change it without marking up a new one? Is it possible to rotate it or change the volume? What tool can I use to do this? Thank you.<br>
Operating system: WIN10_64<br>
Slicer version:5.2.1</p>

---

## Post #2 by @lassoan (2023-06-02 23:39 UTC)

<p>You can compute the warping transform between the two images using Elastix or ANTs extension. Then you can apply the computed transform to the segmentation.</p>

---
