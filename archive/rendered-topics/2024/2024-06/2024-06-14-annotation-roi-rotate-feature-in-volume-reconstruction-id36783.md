# Annotation ROI rotate feature in Volume Reconstruction

**Topic ID**: 36783
**Date**: 2024-06-14
**URL**: https://discourse.slicer.org/t/annotation-roi-rotate-feature-in-volume-reconstruction/36783

---

## Post #1 by @MariaGraf (2024-06-14 14:35 UTC)

<p>I’m working on 3D freehand ultrasounds, creating volumes of muscles. I’ve been told to use the module 'Volume Reconstruction" and when completing the ‘ROI node’ step, the annotationROI is unable to be rotated to adjust for positioning. To allow for a better volume reconstruction, a smaller annotation ROI would be helpful. I noticed that using the markups ROI you are able to rotate, however not with the annotation ROI. Can anyone help me rotate the annotation ROI, or use the markup ROI in the volume reconstruction module? Thank you!</p>

---

## Post #2 by @lassoan (2024-06-14 14:36 UTC)

<p>Annotation module is deprecated, please use Markups mosule instead. You can use Markups ROI everywhere that previously used Annotation ROI.</p>

---
