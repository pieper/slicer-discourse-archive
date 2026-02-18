# Save a binary segmentation of the surface voxels of a segment.

**Topic ID**: 22542
**Date**: 2022-03-16
**URL**: https://discourse.slicer.org/t/save-a-binary-segmentation-of-the-surface-voxels-of-a-segment/22542

---

## Post #1 by @Steven_A (2022-03-16 17:15 UTC)

<p>Hello, I am wondering if there is a method to save a binary labelmap of the surface voxels of a segment? If I’m not mistaken, there was a method to do this, but I don’t remember how.</p>

---

## Post #2 by @lassoan (2022-03-16 19:46 UTC)

<p>You can use “Hollow” effect to keep boundary voxels (up to the specified thickness). If you need to extract position of boundary points then the closed surface representation is probably more appropriate.</p>

---

## Post #3 by @Steven_A (2022-03-17 07:09 UTC)

<p>Thank you very much.</p>

---
