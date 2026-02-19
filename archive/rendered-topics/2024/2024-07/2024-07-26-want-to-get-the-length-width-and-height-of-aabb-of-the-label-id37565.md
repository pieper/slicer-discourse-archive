---
topic_id: 37565
title: "Want To Get The Length Width And Height Of Aabb Of The Label"
date: 2024-07-26
url: https://discourse.slicer.org/t/37565
---

# Want to get the length width and height of AABB of the labels

**Topic ID**: 37565
**Date**: 2024-07-26
**URL**: https://discourse.slicer.org/t/want-to-get-the-length-width-and-height-of-aabb-of-the-labels/37565

---

## Post #1 by @hk_y (2024-07-26 03:34 UTC)

<p>Dear professors, I previously used the Segment Statistics module in Slicer to output the dimensions (length, width, height) of the oriented bounding box (OBB) for a label. It’s really helpful. Now, I want to output the dimensions of the axis-aligned bounding box (AABB) for the same label. What should I do?</p>

---

## Post #2 by @lassoan (2024-07-26 04:38 UTC)

<p>You could add axis-aligned binding box computation to Segment Statistics module’s Python scripts. It should be fairly easy to do it using <code>numpy.where</code>. Let us know if you need help with getting started.</p>

---
