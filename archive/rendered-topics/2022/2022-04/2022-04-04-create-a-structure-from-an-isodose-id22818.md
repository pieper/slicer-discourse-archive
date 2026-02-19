---
topic_id: 22818
title: "Create A Structure From An Isodose"
date: 2022-04-04
url: https://discourse.slicer.org/t/22818
---

# create a structure from an isodose 

**Topic ID**: 22818
**Date**: 2022-04-04
**URL**: https://discourse.slicer.org/t/create-a-structure-from-an-isodose/22818

---

## Post #1 by @skefs (2022-04-04 15:00 UTC)

<p>Dear all,<br>
I would like from a dose matrix to create a structure containing the isodose of my choice. Not having found the solution to my problem, I therefore refer to you. maybe you would have a solution to create a structure from an isodose.</p>
<p>In advance, thank you for your answer</p>

---

## Post #2 by @lassoan (2022-04-05 04:31 UTC)

<p>Isodose module generates a model. You can convert the model to a segment in an existing segmentation by drag-and-dropping the model into the segmentation in Data module. Alternatively, you can right-click on the model node in Data module and choose convert to segmentation.</p>

---
