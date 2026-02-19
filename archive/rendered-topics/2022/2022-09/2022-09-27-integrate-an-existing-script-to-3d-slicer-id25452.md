---
topic_id: 25452
title: "Integrate An Existing Script To 3D Slicer"
date: 2022-09-27
url: https://discourse.slicer.org/t/25452
---

# Integrate an existing script to 3D slicer

**Topic ID**: 25452
**Date**: 2022-09-27
**URL**: https://discourse.slicer.org/t/integrate-an-existing-script-to-3d-slicer/25452

---

## Post #1 by @LuisaDantas (2022-09-27 19:56 UTC)

<p>Hey</p>
<p>I developed a Python script to segment the ventricle on a semi automated way and I wanted to make it as an extension to 3D Slicer. I’m new to the software and don’t know much of it.</p>
<p>The idea of the original code is, based on labels of the heart objects and user interaction, it recognizes the left ventricle and makes contour around it, then it allows the user to edit the contour by dragging its points. What I wanted to know is if there’s a similar example to take a look (examples on labeling objects or editable polygons) or if I can somehow pass the coordinates of the contour (polygon) to the Markup Closed Curve so it can plot it.</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2022-09-28 04:22 UTC)

<p>I would recommend to complete the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">PerkLab bootcamp’s Slicer Programming tutorial</a> to get started with Slicer module development.</p>
<p>Since you are developing an interactive segmentation tool, I would recommend to implement it as a Segment Editor effect. There are several examples in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/">SegmentEditorExtraEffects extension</a> (they are all Python-scripted modules). Try all of them to see which one is the most similar to what you want to achieve.</p>

---

## Post #3 by @LuisaDantas (2022-09-28 13:06 UTC)

<p>Great I’ll try that, thank you <a class="mention" href="/u/lassoan">@lassoan</a>!</p>

---
