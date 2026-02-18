# 3D small intestine reconstruction

**Topic ID**: 11365
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/3d-small-intestine-reconstruction/11365

---

## Post #1 by @edmontontutor (2020-04-30 14:55 UTC)

<p>Hello,</p>
<p>Has anyone reconstructed a 3D image of the small intestine using 3D Slicer and CT scans? Can anyone provide some suggestions please? I’m having some issues segmenting the small intestine.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2020-04-30 14:58 UTC)

<p>You can visualize the intestines using Volume rendering module or you can use Segment Editor module to segment the region you are interested in and do some more analysis from there (centerline extraction, radius, curvature computation, etc.).</p>

---

## Post #3 by @zhang_ming (2023-02-18 05:38 UTC)

<p>Would you initiate a plugin that automatically splits the small intestine? I’m interested in</p>

---

## Post #4 by @rbumm (2023-02-18 06:43 UTC)

<p>You can try the <a href="https://github.com/lassoan/SlicerTotalSegmentator">TotalSegmentator extension</a>. TotalSegmentator includes many abdominal organs/structures. It works best with data from healthy subjects.</p>

---

## Post #5 by @zhang_ming (2023-02-20 11:00 UTC)

<p>good job, I will try it out</p>

---
