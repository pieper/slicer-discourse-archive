---
topic_id: 3658
title: "How To Connect Sub Branches With Together"
date: 2018-08-04
url: https://discourse.slicer.org/t/3658
---

# How to connect sub-branches with together?

**Topic ID**: 3658
**Date**: 2018-08-04
**URL**: https://discourse.slicer.org/t/how-to-connect-sub-branches-with-together/3658

---

## Post #1 by @shahrokh (2018-08-04 11:40 UTC)

<p>Hi Slicer developers and users</p>
<p>I have a large bunch of parallel branches and one oblique branch (approximately 300 branches). Obviously, these branches do not collied with together. I extract these branches from CT imaging using Effects of “Segment Editor” firstly and then “Extract Skeleton”.<br>
In several areas, these branches are cut off (disconnected) and each branch becomes a few subbranches (3-4 subbranches). I want to connect these subbranches automatically. How can I do it?<br>
Please guide me.<br>
Best regards,<br>
Shahrokh</p>

---

## Post #2 by @lassoan (2018-08-04 21:36 UTC)

<p>For specific problems like this, you may need to develop your own algorithm.</p>
<p>However, probably you can avoid breaking up of branches if you resample the volume before segmentation to have smaller voxels (vessel diameters should be at least 5-10 voxels).</p>

---
