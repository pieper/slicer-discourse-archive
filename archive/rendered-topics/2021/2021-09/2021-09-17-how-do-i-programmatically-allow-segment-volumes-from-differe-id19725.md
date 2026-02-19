---
topic_id: 19725
title: "How Do I Programmatically Allow Segment Volumes From Differe"
date: 2021-09-17
url: https://discourse.slicer.org/t/19725
---

# How do I programmatically allow segment volumes from different segmentations to be shown in one table in the segment statistics module?

**Topic ID**: 19725
**Date**: 2021-09-17
**URL**: https://discourse.slicer.org/t/how-do-i-programmatically-allow-segment-volumes-from-different-segmentations-to-be-shown-in-one-table-in-the-segment-statistics-module/19725

---

## Post #1 by @akshay_pillai (2021-09-17 13:38 UTC)

<p>I know that we can use the segment statistics, module to get the volume of individual segments inside a segmentation in a table. How do I programmatically make it add volumes of segments in different segmentations? I would want the segment volume from a second or third segmentation to be added to the segment statistics table. So just one table for comparing volumes across segmentations. Is this possible? Any help is appreciated thanks.</p>

---

## Post #2 by @lassoan (2021-09-17 14:15 UTC)

<p>It should be no problem at all. You can create a summary table (with an extra column to identify the segmentation node) and copy each cell of the segment statistics output table to this summary table using <a href="http://apidocs.slicer.org/master/classvtkMRMLTableNode.html">vtkMRMLTableNode</a> methods (<code>GetCellText</code>, <code>AddEmptyRow</code>, <code>SetCellText</code>, etc.).</p>

---

## Post #3 by @akshay_pillai (2021-09-21 16:18 UTC)

<p>Hey, I still haven’t been able to implement this. Is there an example code so I can see it and understand or implement it?</p>

---

## Post #4 by @akshay_pillai (2021-09-21 16:21 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="19725">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>m at all. You can create a summary table (with an extra column to identify the segmentation node) and copy each cell of the segment statistics output table to this summary table using <a href="http://apidocs.slicer.org/master/classvtkMRMLTableNode.html" rel="noopener nofollow ugc">vtkMRMLTableNode </a> methods ( <code>GetCellText</code> ,</p>
</blockquote>
</aside>
<p>Also, I want 2 segments from different segmentations to be added into one column without creating another table. For example, just selecting volume and segment and clicking add consecutively one after the other adding onto the same table. I think I could implement it if I look at some example code with table creation and manipulation.</p>

---

## Post #5 by @lassoan (2021-09-21 17:46 UTC)

<p>These examples should help:</p>
<ul>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Tables/Testing/Python/TablesSelfTest.py" class="inline-onebox">Slicer/TablesSelfTest.py at master · Slicer/Slicer · GitHub</a></li>
<li><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#measure-distance-of-points-from-surface" class="inline-onebox">Script repository — 3D Slicer documentation</a></li>
<li><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L2012-L2112" class="inline-onebox">Slicer/util.py at master · Slicer/Slicer · GitHub</a></li>
</ul>

---
