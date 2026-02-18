# Slice thickness and kernel preference for 3D reconstruction

**Topic ID**: 34890
**Date**: 2024-03-14
**URL**: https://discourse.slicer.org/t/slice-thickness-and-kernel-preference-for-3d-reconstruction/34890

---

## Post #1 by @D_Dand (2024-03-14 14:53 UTC)

<p>Hello everyone,</p>
<p>Hope this post finds you well. We are planning to start a project for reconstructing human airways. And thus, we need to prepare a proposal for project to request CT-scan images.<br>
<strong>Would anyone please advice me what is the slice thickness and kernel preference for 3D slicer?</strong></p>

---

## Post #2 by @pieper (2024-03-15 19:26 UTC)

<p>Slicer should be able to process images acquired with any kernel and thickness; the better the images the better the reconstruction - higher resolution and more tissue contrast is better.  Probably you should consult the radiology literature to see what gives the best accuracy for your target tissues given any radiation dose constraints.</p>

---
