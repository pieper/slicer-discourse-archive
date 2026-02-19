---
topic_id: 20721
title: "Dont Know How To Use Fast Marching"
date: 2021-11-22
url: https://discourse.slicer.org/t/20721
---

# Don't know how to use Fast marching

**Topic ID**: 20721
**Date**: 2021-11-22
**URL**: https://discourse.slicer.org/t/dont-know-how-to-use-fast-marching/20721

---

## Post #1 by @Gabriella-Rus (2021-11-22 09:39 UTC)

<p>Hi! I try to work with “fast marching” from segmentation extension but when I press initialize button, nothing happens. What I am doing wrong?</p>

---

## Post #2 by @chir.set (2021-11-22 10:27 UTC)

<p>Seed your segment first.</p>

---

## Post #3 by @Gabriella-Rus (2021-11-22 10:30 UTC)

<p>:))) was the first thing I did.</p>

---

## Post #4 by @lassoan (2021-11-23 17:19 UTC)

<p>Try to follow this short tutorial, using the exact same data set, painting similar seed in a similar location. If it works then try to do things similarly in your data set.</p>
<p>If you run into problems then you may post a screen capture video or an example scene file (saved as .mrb) so that we can have a better idea why it does not behave as you expect.</p>
<p>Note that Fast marching works well for easy segmentation problems: when there is a very clear strong contrast difference between the object of interest and the background. For non-trivial segmentation tasks, you may get better results with “Grow from seeds” or “Local thresholding” methods - and there are a number of others. Let us know what you want to segment, on what imaging modality, for what purpose and we can make more specific recommendations.</p>

---
