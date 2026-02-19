---
topic_id: 44176
title: "Obb Corner Coordinates And Or Dimensions"
date: 2025-08-23
url: https://discourse.slicer.org/t/44176
---

# OBB Corner Coordinates and/or Dimensions

**Topic ID**: 44176
**Date**: 2025-08-23
**URL**: https://discourse.slicer.org/t/obb-corner-coordinates-and-or-dimensions/44176

---

## Post #1 by @liam26 (2025-08-23 02:58 UTC)

<p>I’m trying to find the dimensions of my OBB box (width, length, height) to get the height of spinal discs. Even getting the corner coordinates would be helpful so I could calculate it manually. I can’t find an existing script or get my own to work. Thank you in advance!</p>

---

## Post #2 by @mikebind (2025-08-23 04:03 UTC)

<p>This script from the script repository shows how to do this using tools from the SegmentStatistics module: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#markups-roi" rel="noopener nofollow ugc">Get oriented bounding box and display them using markups ROI node</a></p>

---

## Post #3 by @liam26 (2025-08-23 22:31 UTC)

<p>I’ve been able to display the boxes using this script but not get their dimensions. I thought they might appear as a segment when running SegmentStatistics but only the original segments appeared in the table.</p>

---

## Post #4 by @mikebind (2025-08-23 23:19 UTC)

<p>The OBB dimensions are in the <code>obb_diameter_mm</code> array after running the script.   The <code>obb_diameter_mm[0]</code> will be the length of the OBB in the x direction (i.e. the bounding box dimension along the vector <code>obb_direction_ras_x</code>.  Likewise, <code>obb_diameter_mm[1]</code> will be the length of the OBB in the y direction (along <code>obb_direction_ras_y</code>), and <code>obb_diameter_mm[2]</code>will be the remaining OBB dimension (along <code>obb_direction_ras_z</code>).</p>

---
