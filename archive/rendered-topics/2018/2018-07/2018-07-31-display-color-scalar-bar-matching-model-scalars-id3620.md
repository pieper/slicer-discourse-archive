---
topic_id: 3620
title: "Display Color Scalar Bar Matching Model Scalars"
date: 2018-07-31
url: https://discourse.slicer.org/t/3620
---

# Display color scalar bar matching model scalars

**Topic ID**: 3620
**Date**: 2018-07-31
**URL**: https://discourse.slicer.org/t/display-color-scalar-bar-matching-model-scalars/3620

---

## Post #1 by @Sam_Horvath (2018-07-31 18:41 UTC)

<p>I would like to display a scalar bar that matches the color node/data range of the scalars on a model I am viewing.  I can use the colors module to display a scalar bar, but the range is fixed at max… What is the best way to create the scalar bar that I need?</p>

---

## Post #2 by @lassoan (2018-08-02 08:35 UTC)

<p>Set scalar range of the color node to match the scalar range you use in Models module. You need to create an editable copy of the color node (click the “Copy” button next to the node selector in Colors module) to edit the scalar range of the color node.</p>

---
