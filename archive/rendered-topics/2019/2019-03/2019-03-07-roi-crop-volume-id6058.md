---
topic_id: 6058
title: "Roi Crop Volume"
date: 2019-03-07
url: https://discourse.slicer.org/t/6058
---

# ROI ,Crop volume

**Topic ID**: 6058
**Date**: 2019-03-07
**URL**: https://discourse.slicer.org/t/roi-crop-volume/6058

---

## Post #1 by @prorai (2019-03-07 12:06 UTC)

<p>How can i set ROI and Crop volume setting from python code?</p>

---

## Post #2 by @pieper (2019-03-07 20:48 UTC)

<p>Yes, all that you need is exposed via python and it should be the same as manipulating any other mrml nodes and calling module logics (<a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.h#L65" rel="nofollow noopener">https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/CropVolume/Logic/vtkSlicerCropVolumeLogic.h#L65</a>)</p>

---
