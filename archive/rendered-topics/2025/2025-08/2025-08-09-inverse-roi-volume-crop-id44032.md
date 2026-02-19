---
topic_id: 44032
title: "Inverse Roi Volume Crop"
date: 2025-08-09
url: https://discourse.slicer.org/t/44032
---

# Inverse ROI volume crop

**Topic ID**: 44032
**Date**: 2025-08-09
**URL**: https://discourse.slicer.org/t/inverse-roi-volume-crop/44032

---

## Post #1 by @JaredAmudeo (2025-08-09 09:17 UTC)

<p>Hi! Is there a simple way to do a volume crop that selects everything outside the ROI, basically erasing everything inside?</p>

---

## Post #2 by @muratmaga (2025-08-09 16:39 UTC)

<p>Not through crop volume because it is not meaningul to have a void in a 3d volume. But you can accomplish setting those voxels to background value (e.g 0) through segmentation, specifically MaskVolume effect.</p>

---
