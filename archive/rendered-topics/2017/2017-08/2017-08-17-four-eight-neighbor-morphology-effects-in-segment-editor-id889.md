---
topic_id: 889
title: "Four Eight Neighbor Morphology Effects In Segment Editor"
date: 2017-08-17
url: https://discourse.slicer.org/t/889
---

# Four/Eight Neighbor Morphology Effects in Segment Editor

**Topic ID**: 889
**Date**: 2017-08-17
**URL**: https://discourse.slicer.org/t/four-eight-neighbor-morphology-effects-in-segment-editor/889

---

## Post #1 by @moselhy (2017-08-17 18:09 UTC)

<p>I find that Segment Editor’s Margin effect does not achieve the same job as Editor’s “Four Neighbor” erode effect. What resources would be useful to implement a tool where the user selects neighbor type and erode/dilate then apply it to the segment?</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2017-08-17 18:53 UTC)

<p>Segment editor’s Margin effect uses a sphere shaped structuring element, which allows adding/removing margin by a specific size (regardless of pixel size and segment surface normal direction).</p>
<p>For noise removal, I would suggest to use methods available in Smoothing effect.</p>
<p>The legacy Editor’s 4/8-neighbor erode/dilate effect was very limited (mostly usable only for removing very small amount of random noise), as it grew diamond-shaped regions, with shape depending on the volume spacing.</p>

---
