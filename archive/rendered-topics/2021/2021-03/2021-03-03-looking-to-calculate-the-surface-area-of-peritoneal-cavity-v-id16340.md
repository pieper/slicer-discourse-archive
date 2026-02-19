---
topic_id: 16340
title: "Looking To Calculate The Surface Area Of Peritoneal Cavity V"
date: 2021-03-03
url: https://discourse.slicer.org/t/16340
---

# Looking to calculate the surface area of peritoneal cavity via MRI / CT

**Topic ID**: 16340
**Date**: 2021-03-03
**URL**: https://discourse.slicer.org/t/looking-to-calculate-the-surface-area-of-peritoneal-cavity-via-mri-ct/16340

---

## Post #1 by @rhughen77 (2021-03-03 17:40 UTC)

<p>This would include the surface area of the peritoneal cavity (lining or peritoneum) itself and , if possible, the surface area of the organs inside the peritoneum. Ideally selectively by organ, also if possible.  Has this been done? Thanks, Ric</p>

---

## Post #2 by @lassoan (2021-03-03 21:05 UTC)

<p>If you <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">segment</a> the peritoneal cavity and each organ of interest then you can get the surface areas automatically using Segment Statistics module.</p>

---
