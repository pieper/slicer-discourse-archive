# Repeated Segment Comparison Metric Calculations

**Topic ID**: 43648
**Date**: 2025-07-08
**URL**: https://discourse.slicer.org/t/repeated-segment-comparison-metric-calculations/43648

---

## Post #1 by @vmcjmk (2025-07-08 12:46 UTC)

<p>Hi there, I’m very new to 3D Slicer and was wondering about going through multiple pairs of segments in the segment comparison module.</p>
<p>For each patient I have, I have one “reference segment” for each cancer nodule as a point of reference and multiple “compare segments” for successive contours of those same nodules throughout the treatment process. Is it possible to iterate through sets of reference segments and compare segments to get all of their Hausdorff distance and dice similarity metrics without having to manually choose each segment in the Segment Comparison module in 3D slicer and click on the compute buttons and then manually enter the data into a spreadsheet?</p>
<p>I have tried using the python console and have been able to set up an array of the pairs of reference and compare segments I want to get the metrics for, but have not found a way to calculate the metrics through python. I tried multiple solutions that Copilot gave me, but none work. Importing the SegmentComparison library/module in python and using its calculation functions does not work (I have Slicer RT installed as an extension in 3D Slicer), and using any sort of segment comparison logic function in python doesn’t get me anywhere.</p>
<p>Thanks</p>

---
