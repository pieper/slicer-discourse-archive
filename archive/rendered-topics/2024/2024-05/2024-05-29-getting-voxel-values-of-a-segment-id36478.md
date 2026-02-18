# Getting voxel values of a segment

**Topic ID**: 36478
**Date**: 2024-05-29
**URL**: https://discourse.slicer.org/t/getting-voxel-values-of-a-segment/36478

---

## Post #1 by @Pierre_Lemois (2024-05-29 19:57 UTC)

<p>I have an MRI image and a segmentation of an area. I need to obtain the values of each voxel in a segment. I’ve followed the documentation, in particular the section: Get histogram of a segmented region. But I can’t find a way of obtaining the gray level values of each voxel in my segmentation. Is there a way of doing this?</p>
<p>Thanks,<br>
Pierre</p>

---

## Post #2 by @lassoan (2024-05-29 20:01 UTC)

<p>You can use Segment Statistics module to get basic statistics (min, max, mean) on gray level values of an image for each segment.</p>
<p>If you want to implement some custom computations then you can add it to the <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/SegmentStatistics/SegmentStatisticsPlugins/ScalarVolumeSegmentStatisticsPlugin.py">scalar volume plugin</a> (it is just a simple Python file, you edit it, reload the module or restart Slicer; and you get the new metrics). If you think that your additional computations may be useful for others, too, then you can submit a pull request with your changes.</p>

---
