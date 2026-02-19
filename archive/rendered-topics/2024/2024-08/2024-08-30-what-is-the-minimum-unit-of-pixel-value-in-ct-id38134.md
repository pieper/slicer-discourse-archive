---
topic_id: 38134
title: "What Is The Minimum Unit Of Pixel Value In Ct"
date: 2024-08-30
url: https://discourse.slicer.org/t/38134
---

# What is the minimum unit of pixel value in CT

**Topic ID**: 38134
**Date**: 2024-08-30
**URL**: https://discourse.slicer.org/t/what-is-the-minimum-unit-of-pixel-value-in-ct/38134

---

## Post #1 by @soil_soil (2024-08-30 18:30 UTC)

<p>The smallest unit of the fountain pen in segmentation is the smallest pixel of CT, but the distribution of brightness and darkness can be seen within a single pixel. How is the intensity value within a single pixel determined</p>

---

## Post #2 by @lassoan (2024-08-30 18:32 UTC)

<p>When the CT image is displayed, the continuous signal is reconstructed from the discrete samples. That’s why you always see a continuous gray level changes, regardless of how much you zoom in.</p>
<p>You can find voxel spacing of the image in Volumes module / Volume information section. You can find voxel spacing of the segmentation if you click the “Segment Geometry” button in Segment Editor.</p>

---
