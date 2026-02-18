# 3D Visualization in Slicerde

**Topic ID**: 30025
**Date**: 2023-06-14
**URL**: https://discourse.slicer.org/t/3d-visualization-in-slicerde/30025

---

## Post #1 by @DzungDinh (2023-06-14 03:48 UTC)

<p>Hello!</p>
<p>I have a question regarding the best practice for visualizing the MRI scans and their segmentation. When I import the MRI scans and segmentations, it doesn’t align (they are in different locations). Moreover, the segmentation can only be viewed in 3D and not in 2D slices using the subwindow.</p>
<p>So my question is, how should I save both MRI and segmentation after getting the segmentation from a PyTorch model? Like, what should the shape be? What should the format be?</p>
<p>Thank you for your help!</p>

---

## Post #2 by @lassoan (2023-06-16 14:31 UTC)

<p>It seems that when you saved the segmentation to file you did not copy the image origin, spacing, and axis directions from the input image to the output segmentation.</p>

---
