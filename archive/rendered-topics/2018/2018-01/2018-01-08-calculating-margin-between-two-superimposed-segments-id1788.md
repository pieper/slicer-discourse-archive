# Calculating margin between two superimposed segments

**Topic ID**: 1788
**Date**: 2018-01-08
**URL**: https://discourse.slicer.org/t/calculating-margin-between-two-superimposed-segments/1788

---

## Post #1 by @tnguyen (2018-01-08 21:02 UTC)

<p>Hi,</p>
<p>I was wondering if there is a way to find the smallest margin between two superimposed 3D-segments, especially in an automatic fashion?</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2018-01-09 01:47 UTC)

<p>You can use the Hausdorff distances in Segment Comparison module in the SlicerRT extension. You can get the average, maximum, and 95th percentile distance from the GUI, and you can get the histogram through python, which will give you the minimum. Although I find the minimum to be an unusual metric, because usually they intersect at some point, so the minimum will be 0.</p>

---
