---
topic_id: 28434
title: "Roi Cropping And Segmentation"
date: 2023-03-17
url: https://discourse.slicer.org/t/28434
---

# ROI cropping and segmentation

**Topic ID**: 28434
**Date**: 2023-03-17
**URL**: https://discourse.slicer.org/t/roi-cropping-and-segmentation/28434

---

## Post #1 by @Nima_Yousefi (2023-03-17 19:45 UTC)

<p>Hi,</p>
<p>In case of feature extraction from ct images and for any analysis such as prediction, should we crop then segment ROI or just segmentation is enough?</p>
<p>Prof <a class="mention" href="/u/lassoan">@lassoan</a>,<a class="mention" href="/u/rbumm">@rbumm</a> I would appreciate if you share your opinions with me.</p>
<p>Thanks.</p>

---

## Post #2 by @lassoan (2023-03-18 20:11 UTC)

<p>I don’t know the context (which feature of which Slicer extension/module), but if you compute features of a segmented region then there is no need to crop the image.</p>

---
