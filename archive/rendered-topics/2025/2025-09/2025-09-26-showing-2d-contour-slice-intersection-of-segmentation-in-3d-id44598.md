---
topic_id: 44598
title: "Showing 2D Contour Slice Intersection Of Segmentation In 3D"
date: 2025-09-26
url: https://discourse.slicer.org/t/44598
---

# Showing 2D contour (slice intersection) of segmentation in 3D viewport

**Topic ID**: 44598
**Date**: 2025-09-26
**URL**: https://discourse.slicer.org/t/showing-2d-contour-slice-intersection-of-segmentation-in-3d-viewport/44598

---

## Post #1 by @hfri (2025-09-26 15:54 UTC)

<p>Dear forum,</p>
<p>I would like to display my segmentations as 2D outlines in the 3D view port. I have the NIfTI segmentations, but currently, I can only show the outlines in the 2D views (red, yellow, green). In the 3D viewport, I can only display the segmentations as solid 3D objects, not as outlines.</p>
<p>Any help is very appreciated!</p>

---

## Post #2 by @chir.set (2025-09-26 16:32 UTC)

<p>If your NifTI segmentation can be identified as a vtkMRMLSegmentationNode, you may use <a href="https://gitlab.com/chir-set/Tools7/-/tree/master/Silhouette/" rel="noopener nofollow ugc">this</a> module to generate the outline as a Model visible in the first 3D view.</p>

---

## Post #3 by @lassoan (2025-09-26 19:26 UTC)

<p>You can convert the segmentation to labelmap and then display the labelmap as coloring or contour in the slice that is visible also in 3D.</p>
<p>This need has not come up often enough to justify implementing it for segmentations. Usually people showing the segmentation in 3D as a 3D object (often with some transparency), not just the intersection. Can you tell a bit about your workflow and why do you need to display the segmentation just as a contour?</p>

---
