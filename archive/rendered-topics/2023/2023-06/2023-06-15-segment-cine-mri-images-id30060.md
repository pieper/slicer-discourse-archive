# Segment cine MRI images

**Topic ID**: 30060
**Date**: 2023-06-15
**URL**: https://discourse.slicer.org/t/segment-cine-mri-images/30060

---

## Post #1 by @KLNU (2023-06-15 19:28 UTC)

<p>Hello,<br>
Currently, I have 25 cine MRI images (25 phases within a cardiac cycle). I want to load them to the 3D Slicer as independent pictures and draw contours on them to extract radiomics features and generate report for each image. However, when I tried to load them all together, there were treated as a volume. So I have load them one by one. It is time consuming. Is it possible to load them together and handle them one by one?</p>
<p>Best,</p>
<p>Kai</p>

---

## Post #2 by @lassoan (2023-06-16 13:37 UTC)

<p>If you use a recent Slicer release then cine MRI images should be loaded as a time sequence. You can browse between time points using the play/pause/previous/next buttons on “Sequence browser” toolbar.</p>

---
