# Speed issues during segmentation

**Topic ID**: 37207
**Date**: 2024-07-05
**URL**: https://discourse.slicer.org/t/speed-issues-during-segmentation/37207

---

## Post #1 by @Istvan (2024-07-05 08:50 UTC)

<p><em>Windows version:</em> 10.0.22631 Build 22631<br>
<em>Slicer Version:</em> 4.11.20200930 r29402 / 002be18<br>
<em>Expected behavior:</em> similar slicing speed in case of a geometry and also in case of its inverse<br>
<em>Actual behavior:</em> significant difference in slicing speed</p>
<p>Hello,<br>
we are using Slicer to slice geometries stored in .stl files. The output is stored in black&amp;white .bmp-s.<br>
For each geometry we process two .stl files. If there is volume at a certain coordinate in the first file, there is no volume at the same coordinate in the second file, and vice versa. In other words, the first geometry is the inverse of the second geometry.<br>
Interestingly the processing of the first file is done in a couple of minutes, however, for the second file it can take up to an hour. As I measured the processing time of each phase, it turned out, that the most time consuming step is the<br>
<em>seg.GetSegmentation().CreateRepresentation(‘Binary labelmap’, True)</em>  for each slice.<br>
Since we have quite a few .stl-s each day, it would be a huge gain if we could reduce the processing time also for the second, inverse geometry.<br>
What do you think, what could cause the significant time difference in the processing of the two files? Do you have perhaps a recommendation how to accelerate the process?</p>

---

## Post #2 by @cpinter (2024-07-05 11:06 UTC)

<p>Such significant speed decrease reminds me of the exponentially increasing processing time as the number of segments increase.</p>
<p>If it is not implemented like that already, make sure you always start with an empty segmentation for each of your STLs.</p>

---
