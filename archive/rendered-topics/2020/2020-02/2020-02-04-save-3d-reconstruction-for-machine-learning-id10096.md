# Save 3D reconstruction for machine learning

**Topic ID**: 10096
**Date**: 2020-02-04
**URL**: https://discourse.slicer.org/t/save-3d-reconstruction-for-machine-learning/10096

---

## Post #1 by @manu1991 (2020-02-04 02:00 UTC)

<p>hi there,<br>
Im using Slice 3D for identification of the Urethra in prostate cancer. I’m making few sets of training data that I’ll export in python for the machine learning and deep learning. How should I save the format of the segmentation?</p>

---

## Post #2 by @lassoan (2020-02-04 04:25 UTC)

<p>In general, I would recommend to use .nrrd format for storing image volumes (simple format that can properly save image geometry, it has human-readable header, and reader/writer in most development environment). You can use <code>slicer.util.saveNode()</code> to save a volume node to file.</p>

---
