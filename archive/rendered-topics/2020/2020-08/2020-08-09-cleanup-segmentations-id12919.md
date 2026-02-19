---
topic_id: 12919
title: "Cleanup Segmentations"
date: 2020-08-09
url: https://discourse.slicer.org/t/12919
---

# CleanUp segmentations

**Topic ID**: 12919
**Date**: 2020-08-09
**URL**: https://discourse.slicer.org/t/cleanup-segmentations/12919

---

## Post #1 by @loubna (2020-08-09 15:58 UTC)

<p>Hi;</p>
<p>I would clean up segmentations in order to keep only the big connected regions and remove small internal regions. how can I do that using filters.</p>
<p>Thank’s in advance</p>

---

## Post #2 by @lassoan (2020-08-09 16:45 UTC)

<p>To fill internal holes robustly, without changing external surface at all, you can use shrink-wrap method inplemented in <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify">SurfaceWrapSolidify</a> extension.</p>

---
