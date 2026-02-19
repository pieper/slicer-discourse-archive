---
topic_id: 32454
title: "How Can I Increase T1 Mr Images Count"
date: 2023-10-28
url: https://discourse.slicer.org/t/32454
---

# How can i increase t1 mr images count

**Topic ID**: 32454
**Date**: 2023-10-28
**URL**: https://discourse.slicer.org/t/how-can-i-increase-t1-mr-images-count/32454

---

## Post #1 by @Rumeysa_UZUMCUOGLU (2023-10-28 16:02 UTC)

<p>Hello, how can I increase the number of slices of my T1 MR images in the 3D slicer application?</p>

---

## Post #2 by @lassoan (2023-10-28 16:03 UTC)

<p>You can use the Crop volume module (it can crop and resample the image in one step). If you need more control over resampling (e.g., only make sampling dense along one axis) then you can use thr various image resampling modules (there are 3-4, with slightly different capabilities).</p>

---
