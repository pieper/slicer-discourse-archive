# Get Centroid from Script

**Topic ID**: 13191
**Date**: 2020-08-27
**URL**: https://discourse.slicer.org/t/get-centroid-from-script/13191

---

## Post #1 by @manjula (2020-08-27 10:51 UTC)

<p>I tried to get the centroid from</p>
<p>obb_centroid = np.array(stats[segmentId,“LabelmapSegmentStatisticsPlugin.centroid_ras”])</p>
<p>but it gives KeyError.</p>
<p>Can someone help me how to do that properly ?</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2020-08-27 13:53 UTC)

<p>You need to enable the <code>LabelmapSegmentStatisticsPlugin</code> plugin and the computation of the <code>centroid_ras</code> value.</p>

---

## Post #3 by @manjula (2020-08-27 18:05 UTC)

<p>Thanks you Prof Lasso. Thi</p>

---
