# Mean diameter for SlicerVMTK module

**Topic ID**: 24224
**Date**: 2022-07-07
**URL**: https://discourse.slicer.org/t/mean-diameter-for-slicervmtk-module/24224

---

## Post #1 by @vyvyvyvy (2022-07-07 15:37 UTC)

<p>How can I use the SlicerVMTK module, “cross-section analysis” to show the mean diameter? Right now, I seem to only see options for “min” and “max.” Is there a way to add the mean on my end?</p>

---

## Post #2 by @lassoan (2022-07-07 19:54 UTC)

<p>You can save the “Output table” as a .csv file, open it in Excel, and get the average of the diameter column.</p>

---

## Post #3 by @chir.set (2022-07-08 06:30 UTC)

<p>‘Extract centerline’ allows to create an output table with a ‘Radius’ column. Is it the mean radius ? Calculating a mean value as specified above gives a very slightly different value than the one reported in the ‘Extract centerline’ table.</p>

---

## Post #4 by @lassoan (2022-07-09 15:16 UTC)

<p>Yes, <code>Extract Centerline</code> module reports mean radius in each branch. Some difference is expected due to different sampling, but the difference should be very small (less than a few percent).</p>

---
