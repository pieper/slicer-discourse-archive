# Histogram based range selection in Segment editor's threshold option frame

**Topic ID**: 22385
**Date**: 2022-03-08
**URL**: https://discourse.slicer.org/t/histogram-based-range-selection-in-segment-editors-threshold-option-frame/22385

---

## Post #1 by @Dwij_Mistry (2022-03-08 20:13 UTC)

<p>As we are having selection (ROI) based histogram display and range selection option in Segment editor module.<br>
and<br>
histogram of volume is on Volumes module.</p>
<p>How to add histogram of Volume in Threshold option frame using Python.</p>

---

## Post #2 by @lassoan (2022-03-12 02:45 UTC)

<p>You can combine these three CTK transfer function widget implementations to get what you need:</p>
<ul>
<li>full image histogram display in Volumes module</li>
<li>interactive range editing with handles in Volume Rendering module</li>
<li>highlighting selected range of a histogram in Segment Editor’s Threshold effect</li>
</ul>

---
