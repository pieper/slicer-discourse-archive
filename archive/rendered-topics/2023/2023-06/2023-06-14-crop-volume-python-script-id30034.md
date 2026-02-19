---
topic_id: 30034
title: "Crop Volume Python Script"
date: 2023-06-14
url: https://discourse.slicer.org/t/30034
---

# Crop volume python script

**Topic ID**: 30034
**Date**: 2023-06-14
**URL**: https://discourse.slicer.org/t/crop-volume-python-script/30034

---

## Post #1 by @Mani_Barathi (2023-06-14 10:20 UTC)

<p>Please help me with the python scripting for crop volume to crop the brain?</p>

---

## Post #2 by @lassoan (2023-06-16 14:30 UTC)

<p>Do you want to crop with a box-shaped ROI or you want to do skull stripping (blank out everything outside the brain)?</p>

---

## Post #3 by @Mani_Barathi (2023-06-17 03:39 UTC)

<p>I need python script for both blank out everything outside the brain and cropping box-shaped ROI</p>

---

## Post #4 by @lassoan (2023-06-17 13:15 UTC)

<p>For skull stripping, I would recommend HDBet or SwissSkullStripper extension.</p>
<p>For cropping with an ROI box, you can use the logic class of the Crop volume module.</p>

---

## Post #5 by @Mani_Barathi (2023-06-20 11:42 UTC)

<p>please provide me the python script for swissskullstripper</p>

---

## Post #6 by @lassoan (2023-06-28 03:10 UTC)

<p>SwissSkullStripper is a CLI module that you can use from Python as described <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-run-a-cli-module-from-python">here</a>.</p>

---
