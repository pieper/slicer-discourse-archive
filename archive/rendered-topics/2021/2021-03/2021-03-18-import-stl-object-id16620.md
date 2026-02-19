---
topic_id: 16620
title: "Import Stl Object"
date: 2021-03-18
url: https://discourse.slicer.org/t/16620
---

# Import stl object

**Topic ID**: 16620
**Date**: 2021-03-18
**URL**: https://discourse.slicer.org/t/import-stl-object/16620

---

## Post #1 by @Jmarcs (2021-03-18 16:56 UTC)

<p>Operating system:<br>
Slicer version 4.11<br>
I would like to import stl object (and mix with cbct) and work with editing option. But the software doesnt convert stl to labelmodel in good quality. Do you have a solution to import and convert to binary labelmap with the same quality than the stl file<br>
Maybe you have another solution<br>
best regards .</p>

---

## Post #2 by @pieper (2021-03-18 18:13 UTC)

<p>Converting from a surface representation to a labelmap will always result in discretization (stairstep) issues.  You can choose the resolution with the Segmentation geometry dialog in the Segment Editor before importing the model as a segment.</p>

---

## Post #3 by @Jmarcs (2021-03-18 18:39 UTC)

<p>thanks but do you have a link(movie tuto …) about subject</p>

---

## Post #4 by @lassoan (2021-03-26 02:51 UTC)

<p>See detailed instructions <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#generated-surface-contains-step-artifacts">here</a>.</p>

---
