---
topic_id: 25523
title: "Igt Volume Reconstruction Logic"
date: 2022-10-03
url: https://discourse.slicer.org/t/25523
---

# IGT Volume Reconstruction Logic

**Topic ID**: 25523
**Date**: 2022-10-03
**URL**: https://discourse.slicer.org/t/igt-volume-reconstruction-logic/25523

---

## Post #1 by @Isabella_Romero (2022-10-03 11:12 UTC)

<p>Hi,<br>
I have done a segmentation to an image, and now I am trying to do the reconstruction of it using the IGT Volume Reconstruction Module.</p>
<p>I am trying to automate it vie Python. I found the module logic with this command (logic=slicer.modules.volumereconstruction.logic()) but I do not find all the things I want to achieve.</p>
<p>I want to do the following things:<br>
Select Live volume, Select values for output spacing, Interpolation mode Linear, No optimization mode, Compounding Mode Maximum, Fill Holes Checked.</p>

---

## Post #2 by @Sunderlandkyl (2022-10-03 14:45 UTC)

<p>The volume reconstruction parameters are controlled by the “vtkMRMLVolumeReconstructionNode”.</p>

---
