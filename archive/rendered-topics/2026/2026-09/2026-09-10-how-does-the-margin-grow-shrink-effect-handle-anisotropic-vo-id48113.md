---
topic_id: 48113
title: "How does the Margin (grow/shrink) effect handle anisotropic voxel spacing?"
date: 2026-09-10
url: https://discourse.slicer.org/t/48113
last_bumped: 2026-09-10T20:48:21.204Z
---

# How does the Margin (grow/shrink) effect handle anisotropic voxel spacing?

**Topic ID**: 48113
**Date**: 2026-09-10
**URL**: https://discourse.slicer.org/t/how-does-the-margin-grow-shrink-effect-handle-anisotropic-voxel-spacing/48113

---

## Post #1 by @Farah_BH (2026-09-10 20:48 UTC)

<p>Hello,</p>
<p>I’m using the Margin effect in Segment Editor to isotropically expand a segment on CT data with anisotropic voxel spacing. When I request a 3.00 mm margin, the UI reports an actual expansion of 2.9 × 2.9 × 2.5 mm, corresponding to a 3×3×1 pixel kernel.</p>
<p>Is this because the Margin effect uses a whole-voxel kernel, rounded per axis, rather than a continuous distance transform?</p>

---
