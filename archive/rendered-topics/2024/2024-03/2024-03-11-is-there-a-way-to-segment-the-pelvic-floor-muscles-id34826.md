---
topic_id: 34826
title: "Is There A Way To Segment The Pelvic Floor Muscles"
date: 2024-03-11
url: https://discourse.slicer.org/t/34826
---

# Is there a way to segment the pelvic floor muscles?

**Topic ID**: 34826
**Date**: 2024-03-11
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-segment-the-pelvic-floor-muscles/34826

---

## Post #1 by @Benny_Zamir (2024-03-11 17:03 UTC)

<p>Hi<br>
Is there a way to segment the pelvic floor muscles?</p>

---

## Post #2 by @lassoan (2024-03-12 04:17 UTC)

<p>You can have a look around model zoos and various segmentation models on github. If you don’t find any pre-trained model then you can train your own: get a few hundred patient images, segment a few dozens of them, train an Auto3DSeg or nnU-net model, evaluate the results, if results are not good enough then add a few dozens more, etc. - keep repeating until the results are good enough. You may be able to use your segmentation model even when it is not perfect yet - maybe it already works well for simple cases and you only need to manually segment the more difficult cases. You can use the MONAILabel extension to streamline the process.</p>

---
