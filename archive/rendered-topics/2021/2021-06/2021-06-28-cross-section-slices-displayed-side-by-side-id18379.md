---
topic_id: 18379
title: "Cross Section Slices Displayed Side By Side"
date: 2021-06-28
url: https://discourse.slicer.org/t/18379
---

# Cross Section Slices Displayed Side-by-Side

**Topic ID**: 18379
**Date**: 2021-06-28
**URL**: https://discourse.slicer.org/t/cross-section-slices-displayed-side-by-side/18379

---

## Post #1 by @dsoto (2021-06-28 17:43 UTC)

<p>I want to determine changes in a very specific area of an MRI over time. Specifically, I want to draw a line through an organ and have it take the same line from all 300 frames in a data set and display them side-by-side. Is this possible in Slicer?</p>

---

## Post #2 by @lassoan (2021-06-28 22:36 UTC)

<p>You can extract a line profile of a 3D volume using “Line Profile” module (in Sandbox extension). If you have a time sequence of 300 frames then you need to do some Python scripting (see relevant examples <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#browse-a-sequence-and-access-currently-displayed-nodes">here</a>).</p>

---

## Post #3 by @dsoto (2021-06-29 20:17 UTC)

<p>Thank you, Dr. Lasso!</p>

---
