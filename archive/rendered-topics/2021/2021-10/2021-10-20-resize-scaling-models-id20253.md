# Resize / Scaling Models

**Topic ID**: 20253
**Date**: 2021-10-20
**URL**: https://discourse.slicer.org/t/resize-scaling-models/20253

---

## Post #1 by @IzzyRobb (2021-10-20 00:41 UTC)

<p>Hi, I’m trying to rescale a model to specific ratios (similar to photoshop’s image size function) and was wondering if there is a way to do this? I have been using the scale feature in slicerFab before I generate bitmaps, however this doesn’t give me the new measurements which is important to know. Is there a way to scale a model which updates the ROI measurements?</p>

---

## Post #2 by @lassoan (2021-10-20 04:54 UTC)

<p>You can apply and harden a transform (set scale factors in the diagonals); or use the Surface Toolbox module.</p>

---
