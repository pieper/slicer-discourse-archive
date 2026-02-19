---
topic_id: 25602
title: "How To Select A Model And Highlight Both The Model And The I"
date: 2022-10-08
url: https://discourse.slicer.org/t/25602
---

# How to select a model and highlight both the model and the items on the qMRMLSubjectHierarchyTreeView

**Topic ID**: 25602
**Date**: 2022-10-08
**URL**: https://discourse.slicer.org/t/how-to-select-a-model-and-highlight-both-the-model-and-the-items-on-the-qmrmlsubjecthierarchytreeview/25602

---

## Post #1 by @miniminic (2022-10-08 09:35 UTC)

<p>I want to realize the function that clicking on a model can locate the corresponding item. The current problem is that I can’t seem to select a model, and when the model is selected, how can I know which model is selected. Thanks.</p>

---

## Post #2 by @pieper (2022-10-08 15:55 UTC)

<p>If you mean clicking on the slice views or 3D views and selecting the picked model or segmentation, I heard recently that <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> may have an implementation in the works.  I’m not sure when it will be available.</p>

---

## Post #3 by @miniminic (2022-10-09 02:22 UTC)

<p>Ok, I see. So currently slicer doesn’t have a way to select models by clicking on them. Thanks for your answer</p>

---

## Post #4 by @lassoan (2022-11-24 03:05 UTC)

<p>Right now the easiest way to achieve this is to click to place a markup point to get a 3D position, and then use the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-displayable-manager-of-a-certain-type-for-a-certain-view">model displayable manager</a> to get the model node that is visible at that position using its <code>Pick3D</code> and <code>GetPickedNodeID</code> methods.</p>

---

## Post #5 by @miniminic (2022-11-24 03:09 UTC)

<p>Thanks for the help. I’ll give it a try</p>

---
