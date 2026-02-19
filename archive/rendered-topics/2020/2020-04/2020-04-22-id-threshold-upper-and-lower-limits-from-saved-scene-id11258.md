---
topic_id: 11258
title: "Id Threshold Upper And Lower Limits From Saved Scene"
date: 2020-04-22
url: https://discourse.slicer.org/t/11258
---

# ID threshold upper and lower limits from saved scene

**Topic ID**: 11258
**Date**: 2020-04-22
**URL**: https://discourse.slicer.org/t/id-threshold-upper-and-lower-limits-from-saved-scene/11258

---

## Post #1 by @mccarthyvetsurg (2020-04-22 23:10 UTC)

<p>Is there anyway to identify threshold limits from a saved scene of an STL for example.  I can upload the volume and it has the threshold outlined, but am not able to see the threshold limits used to make the STL.  Thanks!</p>

---

## Post #2 by @muratmaga (2020-04-23 06:14 UTC)

<p>It is not guaranteed to give you the exact numbers but you can try this:</p>
<ol>
<li>Import your volume,</li>
<li>Import your stl file as a segmentation (expand options and change Description to “Segmentation” from Model)</li>
</ol>
<p>If the geometry preserved between those two (i.e., segmentation line up in the correct anatomical area), then go to <code>Segment Statistics</code>, and calculate the metrics for that segment. Reported min and max  values are your likely threshold ranges.</p>

---
