---
topic_id: 3507
title: "Label Statistics Calculation Voxel Size"
date: 2018-07-17
url: https://discourse.slicer.org/t/3507
---

# Label statistics calculation (voxel size)

**Topic ID**: 3507
**Date**: 2018-07-17
**URL**: https://discourse.slicer.org/t/label-statistics-calculation-voxel-size/3507

---

## Post #1 by @tomo (2018-07-17 18:09 UTC)

<p>4.6.2 r25516, Mac OS 10.13.6, label volume file created by Freesurfer<br>
Label Statistics module: When calculate volume of segmented (labeled) structure the segmentation volume (voxel size 0.75 x 0.75 x0.75 mm3), the output voxel count and volume is identical as it is 1 x 1 x 1 mm3 voxel size. Will it affect the calculation of “actual” volume? Thank you very much for advice.</p>

---

## Post #2 by @pieper (2018-07-17 20:51 UTC)

<p>You should doublecheck that the volume and label loaded with the correct spacing information (you can look in the Volumes module under Volume Information).  If the spacing is meant to be .75^3 and the voxel count is equal to the volume in mm^3 then something is off, as you say.  Also you should use a more recent version of slicer.  If you still aren’t getting what you expect maybe you can share the data for someone else to test with.</p>

---
