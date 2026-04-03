---
topic_id: 46642
title: "Spatial Information In 2D Segmentations"
date: 2026-04-02
url: https://discourse.slicer.org/t/46642
---

# Spatial information in 2D segmentations

**Topic ID**: 46642
**Date**: 2026-04-02
**URL**: https://discourse.slicer.org/t/spatial-information-in-2d-segmentations/46642

---

## Post #1 by @Antmaker (2026-04-02 18:40 UTC)

<p>According to <a href="https://discourse.slicer.org/t/2d-segmentation-possible/33743/2">this post</a>, 2D segmentation is possible in 3D Slicer. I am trying to figure out whether it is possible to incorporate spatial information such that I may calculate “area” instead of “volume (Volume Statistics extension)”.</p>
<p>Is it possible to incorporate spatial information into an image that is being segmented in 3D Slicer? If so, how would I approach integrating it and then calculate the segmented area? If not, how may I segment and calculate the pixel counts?</p>

---

## Post #2 by @mau_igna_06 (2026-04-02 23:33 UTC)

<p>If you enter a 2D image in Slicer it will automatically converted to 3D. Then you can change the spacing (z-axis) of the scalarVolumeNode in Slicer to be 1mm. If you calculate the volume for a segmentation of this image it will be also the area just change the unit to mm2</p>

---
