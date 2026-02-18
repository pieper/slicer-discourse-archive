# 2D phase contrast MRI

**Topic ID**: 18876
**Date**: 2021-07-22
**URL**: https://discourse.slicer.org/t/2d-phase-contrast-mri/18876

---

## Post #1 by @Hamed (2021-07-22 15:33 UTC)

<p>Hi,</p>
<p>Is it possible to read and analyse 2D phase contrast MRI images in 3D Slicer?</p>
<p>Many thanks in advance.</p>

---

## Post #2 by @lassoan (2021-07-22 21:16 UTC)

<p>I’m not sure how to load phase contrast MRI images (is the flow information stored in standard  DICOM images or private fields, or research formats…), but once you have imported them into Slicer you can visualize them in many ways (for example, <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#visualization-modes">vector field visualization in transforms module</a>) and perform many computations easily using numpy or ITK, VTK, or lots of other Python packages.</p>

---
