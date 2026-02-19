---
topic_id: 34173
title: "Slicer Evaluation Of Cursor Origin On Slice"
date: 2024-02-06
url: https://discourse.slicer.org/t/34173
---

# Slicer, evaluation of cursor origin on slice

**Topic ID**: 34173
**Date**: 2024-02-06
**URL**: https://discourse.slicer.org/t/slicer-evaluation-of-cursor-origin-on-slice/34173

---

## Post #1 by @alessandro_um (2024-02-06 15:24 UTC)

<p>Hello,<br>
I am learning the ropes with orienting dicoms, so I am using some well known softwares as a ground of truth, among them I’m using Slicer.<br>
Through math formulas I obtained the same data found under Volume Information (origin and rotation matrix).<br>
What I am struggling to catch are the points coordinates shown in Data Probe that show up when moving the cursor [CT.xxxxxx (coord1, coord2, coord3) ], this are the coordinates in unscaled dicom coordinates with RAS orientation?<br>
Given a point P_dcm in dicom coordinates (not oriented raw data) and having the IJK_TO_RAS_matrix, to obtain the probe position I should do: IJK_TO_RAS_matrix * P_dcm?</p>

---
