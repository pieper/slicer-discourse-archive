---
topic_id: 42475
title: "Centre Line In Two Separated Structures"
date: 2025-04-07
url: https://discourse.slicer.org/t/42475
---

# Centre line in two separated structures

**Topic ID**: 42475
**Date**: 2025-04-07
**URL**: https://discourse.slicer.org/t/centre-line-in-two-separated-structures/42475

---

## Post #1 by @desireeb (2025-04-07 19:41 UTC)

<p>Hello!<br>
I need to get the centre line from two separate structures which are on the same segmentation.<br>
When I set up the centre line, works only for one of the two structures.<br>
Many thanks!</p>

---

## Post #2 by @lassoan (2025-04-08 14:09 UTC)

<p>Centerline is created between inlet and outlet points. In each island in the segment you need to have at least one inlet and one outlet point. You can toggle between inlet/outlet by changing the “selected” state of the markup point.</p>
<p>Alternatively, you can split the segment so that each segment contains only one contiguous region. You can then extract centerline separately in each segment.</p>

---
