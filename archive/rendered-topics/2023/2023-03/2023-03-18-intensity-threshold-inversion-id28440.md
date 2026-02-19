---
topic_id: 28440
title: "Intensity Threshold Inversion"
date: 2023-03-18
url: https://discourse.slicer.org/t/28440
---

# Intensity threshold inversion

**Topic ID**: 28440
**Date**: 2023-03-18
**URL**: https://discourse.slicer.org/t/intensity-threshold-inversion/28440

---

## Post #1 by @mohammed_alshakhas (2023-03-18 11:04 UTC)

<p>it would be great if intensity threshold inversion is possible.</p>
<p>In some instances, you need a threshold that’s not continuous. so you can pick the intensity  you don’t want on histogram and segment the rest ABOVE AND BELOW</p>

---

## Post #2 by @lassoan (2023-03-19 20:19 UTC)

<p>Do you mean thresholding for displaying an image or thresholding in Segment Editor?</p>
<p>Rejecting an intensity range in Segment Editor is very simple: select the intensity range and apply to another segment. This works because when “Modify other segments” option is enabled (this is the default) then applying thresholding adds the regsion to the current segment and also removes that region from all the other segments.</p>

---
