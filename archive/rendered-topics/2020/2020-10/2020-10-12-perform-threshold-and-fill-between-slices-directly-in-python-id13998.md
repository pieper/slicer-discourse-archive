---
topic_id: 13998
title: "Perform Threshold And Fill Between Slices Directly In Python"
date: 2020-10-12
url: https://discourse.slicer.org/t/13998
---

# Perform "threshold" and "fill between slices" directly in python

**Topic ID**: 13998
**Date**: 2020-10-12
**URL**: https://discourse.slicer.org/t/perform-threshold-and-fill-between-slices-directly-in-python/13998

---

## Post #1 by @fredrik (2020-10-12 14:28 UTC)

<p>Hi, I have a binary image where slices are already labeled, and want to generate a volume by interpolating between slices. I was able to do this easily in the 3D-slicer GUI by performing 1) a threshold segmentation and then 2) a fill between slices operation. However I wonder if it is possible to perform these operations directly in python without using the GUI?<br>
Thanks,<br>
Fredrik</p>

---

## Post #2 by @lassoan (2020-10-12 14:31 UTC)

<p>All Slicer features are available to be used without GUI, from Python scripting. See many examples of automating segmentation using Python script here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---

## Post #3 by @fredrik (2020-10-13 12:06 UTC)

<p>Great! Thanks a lot for the help!</p>

---
