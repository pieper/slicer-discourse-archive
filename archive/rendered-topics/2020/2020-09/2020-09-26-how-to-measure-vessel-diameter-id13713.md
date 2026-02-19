---
topic_id: 13713
title: "How To Measure Vessel Diameter"
date: 2020-09-26
url: https://discourse.slicer.org/t/13713
---

# How to measure vessel diameter

**Topic ID**: 13713
**Date**: 2020-09-26
**URL**: https://discourse.slicer.org/t/how-to-measure-vessel-diameter/13713

---

## Post #1 by @Hamid (2020-09-26 03:11 UTC)

<p>I need to measure the diameters of vessels(Descending aorta and 3 vertebral arteries) in my segmented model.How can I do that?Do I need any Extension?</p>

---

## Post #3 by @chir.set (2020-09-26 20:00 UTC)

<p>If your model is created in Slicer with Segment Editor, i.e, a Segment of a Segmentation node, you can use VMTK extension for that. Use Extract Centerline to create a Centerline of the aorta, then Centerline Metrics to get the diameters in a chart and in a table. This output is more readable if you generate non-bifurcated distinct centerlines (you seem to target branches of the aorta as well).</p>
<p>(It 's better to create dedicated topics for specific problems, rather than branching off like here.)</p>

---

## Post #4 by @Hamid (2020-09-29 23:12 UTC)

<p>Thank you so much.<br>
Does anybody know the free software(even trial version) for extracting flow data from CT-images?</p>

---

## Post #5 by @Hamid (2020-09-30 16:45 UTC)

<p>I have made a thick shell from lumen. Now I need to polish the mesh model but I don’t want to get back to the ct-images and modify the model.I’d like to use a module to remove the sharp corners,fill any undesirable holes and … using the shell model.<br>
any help is appreciated</p>

---

## Post #6 by @Hamid (2020-09-30 19:43 UTC)

<p>is there any way to cut in straight line using scissors?</p>

---

## Post #7 by @Hamid (2020-09-30 20:06 UTC)

<p>I have two object in slicer 3d and want to move one of them and connect together.How can I move an abject?</p>

---

## Post #8 by @liam26 (2025-12-22 00:37 UTC)

<p>The table radius is the average of all cross-sectional radii?</p>

---
