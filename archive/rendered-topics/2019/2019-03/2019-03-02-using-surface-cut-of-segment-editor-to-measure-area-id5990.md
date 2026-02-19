---
topic_id: 5990
title: "Using Surface Cut Of Segment Editor To Measure Area"
date: 2019-03-02
url: https://discourse.slicer.org/t/5990
---

# Using surface cut of segment editor to measure area

**Topic ID**: 5990
**Date**: 2019-03-02
**URL**: https://discourse.slicer.org/t/using-surface-cut-of-segment-editor-to-measure-area/5990

---

## Post #1 by @muratmaga (2019-03-02 03:16 UTC)

<p>I am using surface cut to create freehand polygonial selection. Then, I go an convert this segment to a model to measure its area. However, reported area is twice as large than I expect, since it is also calculating the area behind (I think).</p>
<p>Is there away to configure surface cut to select only the external vertices?</p>

---

## Post #2 by @lassoan (2019-03-02 04:11 UTC)

<p>Yes, if you want to compute area of a 2D polygon then you need to divide the reported 3D surface by 2.</p>
<p>Among the new markups widgets (that is planned to be released early next week) there is a “closed curve” type and for that we will report 2D area (so you won’t need to divide by 2).</p>

---
