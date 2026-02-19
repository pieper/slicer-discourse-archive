---
topic_id: 38481
title: "Using Scissors In 3D Slicer By Python Script"
date: 2024-09-22
url: https://discourse.slicer.org/t/38481
---

# Using Scissors in 3D slicer by python script

**Topic ID**: 38481
**Date**: 2024-09-22
**URL**: https://discourse.slicer.org/t/using-scissors-in-3d-slicer-by-python-script/38481

---

## Post #1 by @khaled (2024-09-22 14:04 UTC)

<p>I am working with 3D Slicer for my research. In my work, I manually used the scissors tool to cut a portion of a 3D model that was generated from ultrasound data. Now, I am trying to automate this process using a Python script. These are the steps I’ve followed so far:</p>
<p>1-Loaded the DICOM file.<br>
2-Created a segment editor.<br>
3-Applied a threshold.<br>
I saw a comment from you stating that the scissors are interactive tools. As such, I used markups (curves) to define the points for the shape and activated the scissors tool with the appropriate settings (operation, shape, and slice cut). However, I am facing an issue when applying the effect of the scissors. While there are no errors, the entire model remains unchanged rather than only the intended part being cut.</p>
<p>Could you please assist me with this? Is there a way to cut across all slices automatically using curve points?</p>

---

## Post #2 by @lassoan (2024-09-30 11:22 UTC)

<p>Scissors effect does not use markups, but it intercepts mouse events. For non-interactive use you have many other options. For example, you can use Logical operators effect. Youncan construct the segmebt that you can with directly, by setting voxels. Or you can use a VTK source filter to create a shape tou desire, set in a model node, then import into the segmentation (see script repository for examples). You can also create model from markups using the MarkupsToModel extension.</p>

---

## Post #3 by @khaled (2024-09-30 11:27 UTC)

<p>So, do you mean I can cut the required part and extract it as a 3d model without using scissors? Is there a possible way to use scissors by Python script?</p>

---
